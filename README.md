# Skills

Reusable, repository-scoped skills for rigorous software delivery and agent-assisted engineering.

## Collection

- [`code-review`](skills/code-review/SKILL.md) — evidence-driven review across correctness, security, architecture, performance, tests, and operations.
- [`agent-usage-review`](skills/agent-usage-review/SKILL.md) — assess delegation, context, tool use, verification, safety, and agent workflow quality.
- [`service-improvement`](skills/service-improvement/SKILL.md) — diagnose and improve service performance, reliability, structure, observability, and operability.

### Ticket execution workflow

- [`execute-ticket`](skills/execute-ticket/SKILL.md) — coordinate a ticket from intended behavior to verified changes.
- [`clarify-ticket-behavior`](skills/clarify-ticket-behavior/SKILL.md) — establish expected behavior and resolve consequential questions.
- [`plan-ticket-change`](skills/plan-ticket-change/SKILL.md) — inspect codebase impact and choose a focused approach.
- [`implement-review-ticket`](skills/implement-review-ticket/SKILL.md) — implement, review, and simplify the complete change.
- [`verify-ticket-change`](skills/verify-ticket-change/SKILL.md) — verify acceptance and regressions, and route feedback to the right stage.

Each skill is self-contained and can be installed or copied independently. The `SKILL.md` frontmatter is intentionally specific so compatible agents can discover the right workflow from the task description.

## Routing and composition

Choose one primary skill from the task’s center of gravity:

| Request | Primary skill | Optional companion |
| --- | --- | --- |
| Review a PR, commit, diff, or agent-authored change | [`code-review`](skills/code-review/SKILL.md) | [`agent-usage-review`](skills/agent-usage-review/SKILL.md) when delegation or tool behavior is part of the change |
| Assess prompts, delegation, subagents, tools, or agent traces | [`agent-usage-review`](skills/agent-usage-review/SKILL.md) | [`code-review`](skills/code-review/SKILL.md) for code changes produced by the workflow |
| Diagnose or improve a running or planned service | [`service-improvement`](skills/service-improvement/SKILL.md) | [`code-review`](skills/code-review/SKILL.md) for the implementation diff; [`agent-usage-review`](skills/agent-usage-review/SKILL.md) for agentic operations |

Use the companion only when it answers a distinct question. Keep the primary skill’s report as the decision record and carry companion findings into its follow-up section.

## Executing tickets with minimal reading

Use `$execute-ticket` with a ticket and an accessible codebase. Install all five workflow skills into the agent's supported skill directory; for local Codex, copy these five folders into the project's `.codex/skills/` directory. The coordinator resolves working skills by their frontmatter names and continues through them as needed.

The ticket, code, and conversation are the working record. The workflow creates no extra process documents, proceeds through routine decisions, and surfaces only consequential choices, findings, review focus, and verification results. Stages check prior assumptions and reopen only affected work. Changed behavior returns to clarification, architectural problems to planning, and code defects to implementation; affected changes are reviewed and tested again.

The workflow performs its own concise code review. Use the existing standalone review skills when a separate, detailed assessment is requested; their report formats are not required at every ticket stage. Tasks requiring human testing are marked ready for that testing rather than fully verified. These skills are agent instructions, not a background automation engine.

## Shared report vocabulary

Skills use the following common vocabulary so findings remain comparable when reports are composed:

- **Priority:** `P0` critical, `P1` high, `P2` material, `P3` low, `P4` informational; use `NIT` only for optional polish.
- **Confidence:** `confirmed`, `high`, `medium`, or `low`.
- **Evidence status:** `observed`, `inferred`, or `unverified`; use `unknown` when expected evidence was not obtained.
- **Control status:** `covered`, `partial`, `gap`, `blocked`, or `N/A` with a reason.

## Local validation

Run the dependency-free collection validator before opening a PR:

```text
python scripts/validate_skills.py
```

It checks skill names, frontmatter, UI metadata, default prompts, Markdown fences, and bidirectional README indexing. The regression suite also checks validator edge cases, output-template headings, and primary routing rows. The validator remains a structural smoke test; use each skill’s workflow and project-specific tests for behavioral quality.

The repository workflow runs both commands on pull requests and pushes to `main`.

## Design principles

- Start from the task, repository conventions, and system context.
- Treat measurements, tests, and source evidence as stronger than assumptions.
- Prioritize actionable findings by impact and confidence.
- Separate required fixes from preferences and document residual uncertainty.
- Prefer small, reversible improvements with explicit verification and rollback criteria.
