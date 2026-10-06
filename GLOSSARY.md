# Agent glossary

Every agent Manish has, across Claude Code, Cursor, Python and scheduled jobs. Last full survey: **2026-10-06**.
Read this before building a new agent: extend one that already exists where you can (Constitution, Art. V.2).
**Rule:** when you create, rename or retire an agent, update its row here in the same change.

Path keys: `~` = `C:/Users/manis`, `G` = `~/OneDrive/Documents/Genie`, `H` = `%LOCALAPPDATA%/hermes`.

## Download and library (K21 / Skool)

| Agent | Platform | Path | Does | Trigger | Pattern worth copying |
|---|---|---|---|---|---|
| **AgentK** | Python LangGraph + scheduled | `G/Agents/AgentK` | Diffs the K21 Skool portal against `K21 Learning`, then downloads, files and copies to Drive | Task `AgentK` at logon | soul.md + memory stack; every report states its denominator |
| AgentK reporter | Python ReAct + scheduled | `python -m agentk agent` | Reports downloaded/missing to a webhook | `AgentK-Report`, every 3h | Picks its own tools |
| AgentK improver | Claude Code headless (Ralph loop) | `G/Agents/AgentK/improve/` | Fixes one `ISSUES.md` item per iteration, test-first | `AgentK-Improve`, Sun 11:00 | `git reset` if tests end red |
| AgentK Adversary | *brief only, to be built in Cursor* | `G/Agents/AgentK/ADVERSARY_BRIEF.md` | Tries to prove AgentK's library is incomplete or broken | — | Fresh enumeration; read-only |
| skool-course-mirror | Claude Code skill (+ Cursor copy) | `~/.claude/skills/skool-course-mirror` | Mirrors one Skool course with yt-dlp | Given a Skool URL | Orchestrator → parallel workers → independent validator |
| module-downloader | Claude Code subagent | `~/.claude/agents/module-downloader.md` | Downloads one module from a manifest | Spawned by the skill, Phase 4 | Narrow scope, Bash + Read only |
| mirror-validator | Claude Code subagent | `~/.claude/agents/mirror-validator.md` | Checks a mirror against a fresh portal enumeration | Spawned by the skill, Phase 5 | Read-only; returns a fixed `VERDICT/TABLE/ISSUES/NOT CHECKED` block |
| K21 Download Watcher | Python + scheduled | `G/Genie/second-brain/tools/k21-watcher` | Older watcher: scans and prompts, never downloads | Logon + every 4h | Likely overlaps with AgentK (candidate to retire) |
| skool-crawler | Node/Playwright tool | `G/Genie/second-brain/tools/skool-crawler` | Crawl, download and validate Skool | Manual | A tool, not an LLM agent |

## Security (SecOps, Shiva / Kartikeya)

| Agent | Platform | Path | Does | Trigger | Pattern worth copying |
|---|---|---|---|---|---|
| **senior-security** | Claude Code subagent | `~/.claude/agents/senior-security.md` | Security review of diffs and dependency bumps: Gate = Blast Radius × Capability Delta | `/security` | Reviews only; no Edit/Write tools; the parent patches |
| agentD (Defender) | Claude Agent SDK | `G/Agents/MyAgents/agentD` | Investigates Defender XDR alerts via a read-only Graph MCP | Manual | Investigate-only, no shell |
| agentC | Claude Agent SDK | `G/Agents/MyAgents/agentC` | Writes cert-expiry notification IaC | Manual | Builds only; a human deploys |
| mcpServerCreator | Claude Agent SDK | `G/Agents/MyAgents/mcpServerCreator` | Builds read-only SecOps MCP servers (Purview, Defender) | Manual | Read-only by design |
| Naarad | Python LangGraph + FastMCP | `G/Genie/shiva/shiva-prototypes/Naarad -Threat Intel News` | Daily threat brief | Manual | Publishing gated by Kartikeya + HITL interrupt |
| DOC Foundry security agent | Python LangGraph + FastMCP | `G/Genie/shiva/shiva-prototypes/Security Agents/DOC Foundry` | SOC investigation, architecture validation | Manual | `interrupt_before` HITL; offline |
| Multi-agent enterprise workflow | Python LangGraph | `G/Genie/shiva/shiva-prototypes/multi-agent-workflow-enterprise-agent-system` | Portfolio prototype of governed multi-agent work | Manual | Each agent capability-gated by Shiva |

## Delivery pipeline (MyAgents)

| Agent | Platform | Path | Does | Trigger | Pattern worth copying |
|---|---|---|---|---|---|
| agentNolan | Claude Agent SDK | `G/Agents/MyAgents/agentNolan` | PM: objective → PRD → GitHub issues | Manual, stage 1 | y/N gate; no shell |
| agentPradyuman | Claude Agent SDK | `G/Agents/MyAgents/agentPradyuman` | Program manager: roadmap, milestones, hand-offs | Hand-off from Nolan | Gates need evidence, not dates |
| agentDaya | Claude Agent SDK | `G/Agents/MyAgents/agentDaya` | DSPM tech lead: specs, ADRs, review gate; read-only DCT operator | Hand-off | Gated shell; never pushes |
| agentDino | Claude Agent SDK | `G/Agents/MyAgents/agentDino` | Developer: tested Python, one issue at a time | Hand-off from Daya | TDD; never pushes |

## Products and analysis

| Agent | Platform | Path | Does | Trigger | Pattern worth copying |
|---|---|---|---|---|---|
| **Pit Box** (Intake Classifier, Mechanism Modeller, Docs Archaeologist, Verdict Composer, Adversarial Reviewer) | Python LangGraph | `G/Agents/PitBox` | Turns a Microsoft problem statement into a cited Verdict Report | `run.py` | Adversarial reviewer, max 2 loop-backs; invented citations are downgraded in code; exit code 2 on weak evidence |
| Agent D (Databricks) | Python | `G/Genie/Agents/agent_d` | Databricks control-health discovery and audit evidence | `python -m agent_d discover` | Memory-gated stages. Not the same as MyAgents agentD |
| Upwork Agent | Python (Ollama + `claude -p` / `cursor-agent -p`) | `G/UpworkAgent` | Crawls Upwork, plans, builds demos | Manual | Sends build work to either Claude Code or Cursor |
| AgentM | Python | `G/Agents/AgentM` | Catalogued Upwork AI jobs, built demos | — | **Source lost; only .pyc files remain** |

## Assistant, briefings and personal

| Agent | Platform | Path | Does | Trigger | Pattern worth copying |
|---|---|---|---|---|---|
| **Genie** | Claude Code via Remote Control | `G/CLAUDE.md`, `G/assistant/` | Phone/voice-driven orchestrator and executor | Task `ClaudeRemoteControl` at logon | Files each instruction into the right live doc in the same turn |
| GenieDashboard | Python + `claude -p` + scheduled | `G/assistant/jobs/dashboard.py` | Executive dashboard to Telegram | Daily 09/12/15/18/21:02 | Code gathers the facts; the LLM only formats |
| GenieReminder | Python + scheduled | `G/assistant/jobs/reminder.py` | Voice reminder of open to-dos | Every 2h, 09–21 | No LLM needed |
| AgentChirp | Python + `claude -p` + scheduled | `G/Agents/AgentChirp` | X trend brief from 9 AI creators → 11:00 Telegram voice | Daily 10:50 | Read-only on X; idempotent, `--dry-run` |
| Hermes (note-taker) | Hermes | `H/SOUL.md` | Files Telegram notes into Genie docs | Telegram | Append-only; never does the work |
| Hermes skills: agentk-status, upwork-delivery-agent, hermes-quick-commands, telegram-stickers, local-agent-bootstrap | Hermes skills | `H/skills/` | Status, demos, Telegram helpers | On request | agentk-status never crawls Skool |
| my_investments_latestNews | Claude Code skill | `~/.claude/skills/my_investments_latestNews` | Investment news and suggestions per holding | `/my_investments_latestNews` | Tool allow-list |
| youtube-video-unlisting-saving, youtube-unlist-and-sort, youtube-drafts-to-unlisted | Claude Code skills | `~/.claude/skills/`, synced | YouTube Studio bulk updates | On request | Overlap: 3 skills for one job (candidates to merge) |
| tweet-forge | Claude Code skill | `G/Genie/.claude/skills/tweet-forge` | Drafts authority tweets and threads | Model-invoked | Keeps his voice separate from viral structure |
| shiva | Claude Code skill | synced | Canonical Shiva/Kartikeya positioning | Model-invoked | Single source for terminology |
| diet-log | Claude Code skill | synced | Food/exercise log → dashboard + nudges | Model-invoked | Non-shaming tone |

## Meta: how agents work

| Agent | Platform | Path | Does | Pattern worth copying |
|---|---|---|---|---|
| /explore, /security | Claude Code + Cursor commands | `~/.claude/commands`, `~/.cursor/commands` | Hand search to subagents; launch senior-security | The parent never searches itself |
| delegate-to-subagents | Cursor rule (always) | `G/Genie/.cursor/rules/` | Keeps tool output out of the main window | — |
| agentk rule | Cursor rule | `G/Agents/AgentK/.cursor/rules/agentk.mdc` | Routes K21 questions to AgentK's files | Bans crawling Skool from Cursor |
| databricks-control-tool rule | Cursor rule | `G/Genie/.cursor/rules/` + `G/databricks-control-tool-funding/cursor/` | DCT context | **Two copies that differ** |
| tight, DYUAQ, memorise, teach | Claude Code skills | `~/.claude/skills/` | Brevity; read the ask back; save the session; multi-session teaching | — |
| Learning skills: code-explainer, entire-program-explainer, technical-dry-run-style, quick-code-explainer, shadow-syntax-explainer, python-notebook-explaination, concept-visualiser, lecture-notes-generator, punchy-lecture-notes (v1, v2), medium-digest, analogy, freshness-first-research, concise-response, one-step-only, load-chat | Claude Code skills (synced) | synced skills dir | Code and lecture explainers, digests, response styles | quick-code-explainer's body doesn't match its description; v1/v2 and concise/one-step overlap |
| Hooks | Claude Code / Cursor | `~/.claude/hooks/*.ps1`, `~/.cursor/hooks.json` | recall-context, session logs, memory-claim verify | `verify-memory-claims` exists but is **not wired** |
| ClaudeCodeHistoryBackup | Scheduled | `~/OneDrive/ClaudeHistoryBackup` | 10-min history backup + SessionEnd hook | Support task, not an LLM agent |

## Retired (kept for their lessons)

| Agent | Replaced by | Lesson |
|---|---|---|
| Hermes_Orc (orchestrator) | Genie (Claude Code) | An orchestrator that only delegates loses context; the executor should orchestrate |
| Hermes_Proactive, Voice reminder | GenieDashboard, GenieReminder | Gather facts in code, let the LLM format |
| Hermes_Keeper | — | Proposed improvements but never applied them; a loop needs an executor |
| Hermes_Auditor, Hermes_Scribe | Genie's "keep the files true" rule | — |
| k21-page-download / K21 batch watcher | PAGE_WORKFLOW.md + AgentK | Batch review → one go-ahead → one continuous job |
| Myclaw (OpenClaw K21 downloader) | AgentK + skool-course-mirror | — |
| OpenClaw teams (KUBERA, CHANAKYA, AKASHVANI) | Never built | — |

## Gaps found in this survey (to fix)

- Merge the overlapping skills: 3 YouTube skills; punchy-lecture-notes v1/v2; concise-response vs one-step-only.
- Fix quick-code-explainer (its body doesn't match its description).
- Reconcile the two DCT Cursor rules.
- Retire or merge K21 Download Watcher into AgentK.
- Wire up or delete `verify-memory-claims`.
- AgentM source is lost.
