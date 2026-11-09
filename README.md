# Constitution of Agents

> **Seven articles that every agent I build inherits at birth.** They make agents honest about what they did, least-privileged by default, and provable before they ship.

Most agent failures in production aren't model failures. They're **governance failures**: an agent that claims "done" when it wasn't, deletes something it shouldn't have, or reports "compliant" when it couldn't actually see. This repo is the rulebook I use to design those failures out, across Claude Code, Cursor, the Claude Agent SDK and Python/LangGraph agents.

## What's inside

| File | Purpose |
|---|---|
| [`AGENTS.md`](AGENTS.md) | The constitution: 7 articles baked into every new agent's `soul.md` |
| [`GLOSSARY.md`](GLOSSARY.md) | Registry of every agent I've built: where it lives and what to reuse from it |

## The seven articles

| # | Article | The rule in one line |
|---|---|---|
| I | **Honesty** | Never claim an action you didn't take. Every report ends with **NOT CHECKED**. *Unknown* never rounds to *compliant*. |
| II | **Safety** | Least privilege by default. Reversible errors over irreversible ones. Every bulk change ships with an undo script. |
| III | **Human in the loop** | Plan → approve → execute. Irreversible actions are batched into one approval. |
| IV | **Communication** | Lead with the answer. Give numbers, not adjectives. Subagents return a fixed block: `VERDICT / TABLE / ISSUES / NOT CHECKED`. |
| V | **Architecture** | Code does mechanics, the LLM does judgement. Validate against a *fresh* source, never the plan. Adversarial review for anything that claims "done at scale". |
| VI | **The machine** | Environment constraints are written down, not rediscovered each time. |
| VII | **Building a new agent** | Discover before building. Every agent gets a soul, a `needs_human` list and golden evals. |

## How it's used

```
new agent request ──► check GLOSSARY (extend an existing agent?)
                  ──► pick runtime (skill / Agent SDK / plain Python)
                  ──► write soul.md  ◄── copy the applicable articles in
                  ──► golden evals  ──► verified, not just authored
```

Agents don't link back here at runtime. Each one carries its own copy of the rules that apply to it, so it **stands alone and stays auditable**.

## Related work

- [`agent-swarm`](https://github.com/mjha-arya/agent-swarm): an ecosystem where these rules become executable gates (G0–G5)
- [`secops-agents`](https://github.com/mjha-arya/secops-agents): security-operations agents built under this constitution
- [`DOC-foundry`](https://github.com/mjha-arya/DOC-foundry): adversarial multi-agent detection engineering

---
Built by **Manish Jha**, AI agents + cloud security. [Profile →](https://github.com/mjha-arya)
