# Constitution of Agents

Rules shared by every agent Manish builds, in Claude Code, Cursor, the Agent SDK and Python.

| File | Purpose |
|---|---|
| `AGENTS.md` | The constitution. Keep it short: every agent loads it on every run |
| `GLOSSARY.md` | Every agent, where it lives, what to copy from it. Read on demand, not auto-loaded |
| `sync.py` + `targets.txt` | Copies `AGENTS.md` into each agent repo (managed block) so Cursor picks it up |

## How each platform loads it

| Platform | Mechanism |
|---|---|
| Claude Code (all sessions, subagents) | `@import` line in `~/.claude/CLAUDE.md` |
| Cursor / `cursor-agent` | `AGENTS.md` at each repo root, written by `python sync.py` |
| Claude Agent SDK agents | Need `setting_sources=["user", "project"]` so CLAUDE.md loads, or read `AGENTS.md` into the system prompt |
| Python LangGraph agents (AgentK etc.) | Read `AGENTS.md` alongside `soul.md` into the system prompt |

## Changing a rule

Edit `AGENTS.md` → `python sync.py` → commit.
