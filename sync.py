"""Copy the constitution into every agent repo listed in targets.txt.

Cursor and cursor-agent read AGENTS.md at a repo's root, so each target gets the constitution
inside a managed block. Anything outside the block (repo-specific rules) is left untouched.
Claude Code loads it via an @import in ~/.claude/CLAUDE.md, so it needs no copy.

    python sync.py            # write
    python sync.py --dry-run  # show what would change
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
START = "<!-- constitution:start (synced from Constitution-of-Agents; edit there, then run sync.py) -->"
END = "<!-- constitution:end -->"


def block() -> str:
    return f"{START}\n{(HERE / 'AGENTS.md').read_text(encoding='utf-8').strip()}\n{END}"


def merged(existing: str, new_block: str) -> str:
    if START in existing and END in existing:
        head, rest = existing.split(START, 1)
        tail = rest.split(END, 1)[1]
        return head + new_block + tail
    return new_block + ("\n\n" + existing if existing.strip() else "\n")


def main(dry: bool) -> int:
    targets = [l.strip() for l in (HERE / "targets.txt").read_text(encoding="utf-8").splitlines()
               if l.strip() and not l.startswith("#")]
    new_block = block()
    for t in targets:
        root = Path(t)
        if not root.is_dir():
            print(f"MISSING  {t}")
            continue
        f = root / "AGENTS.md"
        old = f.read_text(encoding="utf-8") if f.exists() else ""
        new = merged(old, new_block)
        if new == old:
            print(f"same     {f}")
            continue
        print(f"{'would ' if dry else ''}write {f}")
        if not dry:
            f.write_text(new, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main("--dry-run" in sys.argv))
