"""Tests for the skills knowledge base. Run: python3 -m unittest discover -s tests -v"""
import json, os, re, subprocess, sys, tempfile, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))


def run(cmd, home=None, check=True):
    env = dict(os.environ)
    if home:
        env["HOME"] = home
    r = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise AssertionError(f"{cmd} failed ({r.returncode}):\n{r.stdout}\n{r.stderr}")
    return r


class RenderDocs(unittest.TestCase):
    def test_render_validates(self):
        out = run([sys.executable, "scripts/render_docs.py"]).stdout
        self.assertIn("ok", out)

    def test_claude_md_within_budget(self):
        self.assertLessEqual(len(open(os.path.join(ROOT, "CLAUDE.md")).read()), 2500)


class Install(unittest.TestCase):
    def setUp(self):
        self.home = tempfile.mkdtemp()
        self.repo = os.path.join(self.home, "repo")
        os.makedirs(self.repo)

    def test_no_gnu_only_sed_inplace(self):
        # BSD sed (macOS) needs a suffix after -i; this broke `install.sh user` once.
        code = "\n".join(re.sub(r"(^|\s)#.*", "", l) for l in open(os.path.join(ROOT, "install.sh")))
        self.assertNotRegex(code, r"sed\s+-i\b")

    def test_user_install_idempotent_and_absolute(self):
        run(["./install.sh", "user"], home=self.home)
        second = run(["./install.sh", "user"], home=self.home).stdout
        self.assertIn("unchanged", second)
        md = open(os.path.join(self.home, ".claude", "CLAUDE.md")).read()
        self.assertEqual(md.count("<!-- skills-kb:begin -->"), 1)
        self.assertIn(f"`{ROOT}/docs/ROUTING.md`", md)
        skill = open(os.path.join(self.home, ".claude", "skills", "skill-router", "SKILL.md")).read()
        self.assertNotIn("../../", skill)
        backups = [f for f in os.listdir(os.path.join(self.home, ".claude")) if ".bak." in f]
        self.assertEqual(backups, [], "no backup when nothing existed or changed")

    def test_project_install_preserves_existing(self):
        p = os.path.join(self.repo, "CLAUDE.md")
        open(p, "w").write("# my rules\n")
        run(["./install.sh", "project", self.repo], home=self.home)
        md = open(p).read()
        self.assertTrue(md.startswith("# my rules"))
        self.assertIn("<!-- skills-kb:begin -->", md)
        self.assertTrue(any(".bak." in f for f in os.listdir(self.repo)))


class PluginProfile(unittest.TestCase):
    def test_plan_skips_already_disabled(self):
        import plugin_profile as pp
        prof = pp.load_profile()
        first = f"{prof['disable'][0]['name']}@synced"
        todo, already = pp.plan(prof, {first: False})
        self.assertIn(first, already)
        self.assertNotIn(first, todo)

    def test_profile_names_exist_in_catalog(self):
        import plugin_profile as pp
        cat = json.load(open(os.path.join(ROOT, "catalog", "skills-catalog.json")))
        names = {p["name"] for p in cat["plugins"]}
        for item in pp.load_profile()["disable"]:
            self.assertIn(item["name"], names)

    def test_dry_run_changes_nothing(self):
        home = tempfile.mkdtemp()
        out = run(["./install.sh", "plugins"], home=home).stdout
        self.assertIn("Dry run", out)
        self.assertFalse(os.path.exists(os.path.join(home, ".claude", "settings.json")))


class FindSkill(unittest.TestCase):
    def test_primary_ranks_first(self):
        out = run([sys.executable, "scripts/find_skill.py", "debugging bug", "-n", "1"]).stdout
        self.assertIn("superpowers:systematic-debugging", out)

    def test_profile_off_hidden(self):
        out = run([sys.executable, "scripts/find_skill.py", "handoff", "-n", "20"]).stdout
        self.assertNotIn("zizi-skills:", out)


class Desktop(unittest.TestCase):
    """Files for the Claude desktop app's Chat/Cowork tabs (not Claude Code)."""

    def setUp(self):
        self.cat = json.load(open(os.path.join(ROOT, "catalog", "skills-catalog.json")))
        self.skills = {s["invoke_as"]: s for s in self.cat["skills"]}

    def test_instructions_only_name_chat_skills(self):
        text = open(os.path.join(ROOT, "desktop", "instructions.md")).read()
        self.assertLessEqual(len(text), 2500)
        for i in re.findall(r"`([\w-]+:[\w-]+)`", text):
            rec = self.skills.get(i)
            self.assertTrue(rec and rec["enabled"] and rec["source"] != "builtin", i)
        # Claude Code-only syntax and built-ins don't exist in chat.
        for cc_only in ("Skill(", "update-config", "`simplify`", "`run`", "`loop`"):
            self.assertNotIn(cc_only, text)

    def test_zip_matches_folder_and_is_uploadable(self):
        import zipfile
        z = zipfile.ZipFile(os.path.join(ROOT, "desktop", "skill-router.zip"))
        self.assertIsNone(z.testzip())
        self.assertEqual(sorted(z.namelist()), ["skill-router/ROUTING.md", "skill-router/SKILL.md"])
        for name in ("SKILL.md", "ROUTING.md"):
            on_disk = open(os.path.join(ROOT, "desktop", "skill-router", name)).read()
            self.assertEqual(z.read(f"skill-router/{name}").decode(), on_disk)
        skill = z.read("skill-router/SKILL.md").decode()
        fm = re.match(r"^---\n(.*?)\n---\n", skill, re.S).group(1)
        name = re.search(r"^name: (.+)$", fm, re.M).group(1)
        desc = re.search(r"^description: (.+)$", fm, re.M).group(1)
        self.assertRegex(name, r"^[a-z0-9-]{1,64}$")
        self.assertLessEqual(len(desc), 1024)

    def test_chat_routing_has_no_builtins(self):
        text = open(os.path.join(ROOT, "desktop", "skill-router", "ROUTING.md")).read()
        builtins = {s["id"] for s in self.cat["skills"] if s["source"] == "builtin"}
        used = set(re.findall(r"`([\w:-]+)`", text))
        self.assertEqual(used & builtins, set())


if __name__ == "__main__":
    unittest.main()
