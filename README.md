# Skills

Reusable, repository-scoped skills for rigorous software delivery and agent-assisted engineering.

## Collection

- [`code-review`](skills/code-review/SKILL.md) — evidence-driven review across correctness, security, architecture, performance, tests, and operations.
- [`agent-usage-review`](skills/agent-usage-review/SKILL.md) — assess delegation, context, tool use, verification, safety, and agent workflow quality.
- [`service-improvement`](skills/service-improvement/SKILL.md) — diagnose and improve service performance, reliability, structure, observability, and operability.

Each skill is self-contained and can be installed or copied independently. The `SKILL.md` frontmatter is intentionally specific so compatible agents can discover the right workflow from the task description.

## Routing and composition

Choose one primary skill from the task’s center of gravity:

| Request | Primary skill | Optional companion |
| --- | --- | --- |
| Review a PR, commit, diff, or agent-authored change | [`code-review`](skills/code-review/SKILL.md) | [`agent-usage-review`](skills/agent-usage-review/SKILL.md) when delegation or tool behavior is part of the change |
| Assess prompts, delegation, subagents, tools, or agent traces | [`agent-usage-review`](skills/agent-usage-review/SKILL.md) | [`code-review`](skills/code-review/SKILL.md) for code changes produced by the workflow |
| Diagnose or improve a running or planned service | [`service-improvement`](skills/service-improvement/SKILL.md) | [`code-review`](skills/code-review/SKILL.md) for the implementation diff; [`agent-usage-review`](skills/agent-usage-review/SKILL.md) for agentic operations |

Use the companion only when it answers a distinct question. Keep the primary skill’s report as the decision record and carry companion findings into its follow-up section.

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
