#!/usr/bin/env bash
# Install the skills knowledge base for Claude Code.
#   ./install.sh user              -> ~/.claude (all projects)
#   ./install.sh project <dir>     -> <dir>/CLAUDE.md + <dir>/.claude/skills
#   ./install.sh plugins [--apply] -> turn off plugins listed in config/plugin-profile.yaml
set -euo pipefail
KB="$(cd "$(dirname "$0")" && pwd)"
MODE="${1:-user}"
MARK_BEGIN="<!-- skills-kb:begin -->"; MARK_END="<!-- skills-kb:end -->"

merge_md() {  # merge_md <target-file>: replace or append the managed block; back up only on change
  local t="$1"; mkdir -p "$(dirname "$t")"; touch "$t"
  python3 - "$t" "$KB" "$MARK_BEGIN" "$MARK_END" <<'PY'
import os, re, shutil, sys, time
t, kb, b, e = sys.argv[1:]
body = open(os.path.join(kb, "CLAUDE.md")).read().strip()
# Relative KB paths would point nowhere from other projects: make them absolute.
body = re.sub(r"`(docs|config|catalog|scripts)/", lambda m: f"`{kb}/{m.group(1)}/", body)
cur = open(t).read()
rest = re.sub(re.escape(b) + r".*?" + re.escape(e) + r"\n?", "", cur, flags=re.S).rstrip()
new = (rest + "\n\n" if rest else "") + f"{b}\n{body}\n{e}\n"
if new == cur:
    print(f"unchanged {t}")
else:
    if cur.strip():
        shutil.copy2(t, f"{t}.bak.{int(time.time())}")
    open(t, "w").write(new)
    print(f"merged skills guide into {t}")
PY
}

point_router() {  # point_router <SKILL.md>: rewrite ../../ to the KB path (portable; no sed -i)
  python3 - "$1" "$KB/" <<'PY'
import sys; f,kb=sys.argv[1:]; s=open(f).read(); open(f,"w").write(s.replace("../../",kb))
PY
}

case "$MODE" in
  user)
    merge_md "$HOME/.claude/CLAUDE.md"
    mkdir -p "$HOME/.claude/skills"
    rm -rf "$HOME/.claude/skills/skill-router"; cp -r "$KB/skills/skill-router" "$HOME/.claude/skills/"
    point_router "$HOME/.claude/skills/skill-router/SKILL.md"
    echo "installed skill-router -> ~/.claude/skills/skill-router (points at $KB)"
    ;;
  project)
    P="${2:?usage: install.sh project <dir>}"; P="$(cd "$P" && pwd)"
    merge_md "$P/CLAUDE.md"
    mkdir -p "$P/.claude/skills"; rm -rf "$P/.claude/skills/skill-router"
    cp -r "$KB/skills/skill-router" "$P/.claude/skills/"
    point_router "$P/.claude/skills/skill-router/SKILL.md"
    ENC="${P//[\/.]/-}"; MEM="$HOME/.claude/projects/$ENC/memory"
    mkdir -p "$MEM"; for f in "$KB"/memory/*.md; do b=$(basename "$f"); [ "$b" = MEMORY.md ] && continue; cp "$f" "$MEM/"; done
    if [ -f "$MEM/MEMORY.md" ] && ! grep -q skills-inventory "$MEM/MEMORY.md"; then
      tail -n +5 "$KB/memory/MEMORY.md" >> "$MEM/MEMORY.md"; else [ -f "$MEM/MEMORY.md" ] || cp "$KB/memory/MEMORY.md" "$MEM/"; fi
    echo "installed into $P (CLAUDE.md, .claude/skills/skill-router, memory at $MEM)"
    ;;
  plugins)
    shift; python3 "$KB/scripts/plugin_profile.py" "$@"
    ;;
  *) echo "usage: $0 user | project <dir> | plugins [--apply]"; exit 1;;
esac
