# Constitution of Agents

Rules and the agent glossary Manish uses **when creating a new agent**, in Claude Code, Cursor, the Agent SDK or Python.
Running agents don't load this. Each new agent gets the relevant rules baked into its own soul at creation.

| File | Purpose |
|---|---|
| `AGENTS.md` | The constitution: rules to bake into every new agent |
| `GLOSSARY.md` | Every agent, where it lives, and what to copy from it. Check it before building |

## How a builder loads it

| Builder | Trigger |
|---|---|
| Claude Code | `create-agent` skill (`~/.claude/skills/create-agent`) |
| Cursor | `/create-agent` command (`~/.cursor/commands/create-agent.md`) |

## Changing a rule

Edit `AGENTS.md` and commit. Existing agents don't change automatically. Update a soul by hand if the rule matters to it.
