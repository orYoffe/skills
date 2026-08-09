---
name: code-review
description: Evidence-driven review of pull requests, commits, branches, working trees, patches, and pasted code before merge or release. Use for correctness, security, contracts, architecture, performance, tests, operations, dependencies, documentation, and maintainability; use agent-usage-review for orchestration behavior.
---

# Evidence-Driven Code Review

Review the change in the context of the repository that will run it. Produce a read-only, severity-ordered review grounded in source evidence, repository conventions, contracts, and validation results. Do not edit code, Git state, dependencies, or external systems unless the user separately asks for implementation.

Treat agent-authored code exactly like human-authored code: do not trust its summary, claimed tests, or proposed fixes without checking them independently.

## Operating rules

- Review the requested scope and its dependencies; do not silently expand into an unrelated refactor.
- Prefer facts, tests, traces, and repository rules over personal preference or generic “best practice.”
- A finding must identify the changed behavior, evidence, impact, and a practical fix. If evidence is missing, report a hypothesis separately and say how to verify it.
- Report one issue per finding, anchor it to the narrowest useful file and line when possible, and keep IDs stable across review passes (`F-001`, `F-002`, …).
- Prioritize security, data loss, correctness, contract, and availability risks over polish.
- Do not block for formatting, naming, or architecture preferences that are not required by a repository rule, contract, measurable risk, or established local pattern. Use `NIT` only for non-blocking, actionable polish.
- Do not call a change “perfect.” The gate is whether it is safe and improves the codebase enough to approve within the stated scope.
- Preserve uncertainty: a failed or unavailable check is not a pass, and a plausible concern is not a confirmed defect.

## Workflow

### 1. Freeze scope and reconstruct intent

Identify the review target and baseline before interpreting code:

1. For a PR or URL, record repository, base/head, commits, linked issue, author intent, reviewers/owners, and CI state. For a local target, record `git status --short`, the base commit or comparison range, and whether changes are staged, unstaged, or untracked. Never discard or rewrite user work.
2. Inspect `git diff --stat`, `git diff --name-status`, and the complete diff. Include deletions, renames, generated files, configuration, migrations, lockfiles, workflows, and tests.
3. Read the closest applicable repository guidance: `AGENTS.md`, `CONTRIBUTING*`, `README*`, design docs, package manifests, CI workflows, CODEOWNERS, and configuration. Search for the nearest analogous implementation, tests, and ownership boundary.
4. Establish the evidence priority: explicit task or acceptance criteria → executable tests and schemas/contracts → repository rules and existing behavior → nearby established patterns → external guidance. Record conflicts instead of silently choosing one.
5. State the intended behavior, changed surface, affected users/data/systems, risk hotspots, and exclusions. If intent cannot be established, mark it `Intent unknown` and limit conclusions; do not convert a guess into a blocking finding.

For a nearly empty or greenfield repository, say which conventions are unavailable. Do not invent conventions from the reviewer’s preferences.

### 2. Review the change in context

Read each changed file one at a time, then read the enclosing functions/classes/modules and relevant callers, callees, schemas, configs, and tests. Compare old and new behavior, not just changed lines.

Trace important paths end to end:

`entry point → parsing/validation → authorization → state/data transformation → persistence or external call → response/output → logging/metrics/recovery`

Check both success and failure paths, including retries, timeouts, cancellation, concurrency, partial failure, rollback, feature flags, migrations, and compatibility with existing data. Follow values across module, process, service, and trust boundaries. For an agent-authored change, independently reproduce the key claims and inspect for hidden scope, prompt-influenced assumptions, or unreviewed generated code.

### 3. Run evidence-producing validation

Discover the project’s prescribed commands before choosing substitutes. Run the smallest targeted checks first, then the relevant full suite. Typical checks, adapted to the repository, are:

```text
git diff --check
<format/lint command>
<type-check/static-analysis command>
<targeted unit/integration tests>
<full relevant test suite>
<build/package command>
<security/dependency scan, if configured>
<smoke test, migration rehearsal, benchmark, or load check when risk warrants it>
```

Record every command exactly with `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN`, plus the relevant output or reason. A command that cannot run because a tool, service, fixture, credential, or environment is missing is `BLOCKED`, not `PASS`. Do not install packages, change lockfiles, mutate databases, deploy, or access production merely to make a check pass without explicit authorization.

Use static analysis and security scanners as evidence and triage input, not as a replacement for reasoning. Manually inspect business logic, data flow, authorization, and complex security controls; automated tools routinely miss context-dependent flaws.

### 4. Apply the review matrix

Cover every applicable row. Mark a row `N/A` only with a reason, and `BLOCKED` when required evidence could not be obtained.

| Area | Questions to answer | Preferred evidence |
| --- | --- | --- |
| Intent and context | Does the change solve the stated problem, preserve required behavior, and fit the affected user or business flow? | Issue/spec, before/after behavior, acceptance tests, linked decisions |
| Correctness | Are control flow, state transitions, error handling, ordering, types, units, and invariants correct? | Enclosing code, callers/callees, tests, reproducible scenario |
| Edge cases and resilience | What happens for empty, null, duplicate, stale, huge, malformed, retried, concurrent, timed-out, or partially failed inputs? | Boundary tests, race/timeout reasoning, retry/idempotency behavior |
| Security | Are trust boundaries, input validation, output encoding, injection, authn/authz, session/token handling, secrets, crypto, file/command access, SSRF, abuse/rate limits, privacy, and error leakage safe? | Data-flow trace, threat model, security tests/scans, secure defaults |
| Data and API contracts | Are schemas, status/error semantics, pagination, versioning, compatibility, serialization, migrations, ownership, and idempotency preserved? | OpenAPI/GraphQL/schema files, consumers, fixtures, migration rehearsal |
| Architecture | Are responsibilities, boundaries, dependencies, extension points, and failure domains appropriate and consistent with the system? | Architecture docs, analogous modules, dependency direction, ownership |
| Performance and capacity | Does it add hot-path work, N+1 queries, unbounded memory/queues, blocking I/O, excessive fan-out, bad indexes, unnecessary serialization, or cache inconsistency? | Query plans, complexity, benchmarks, limits, representative workload |
| Tests | Do tests verify observable behavior and failure modes, isolate state, remain deterministic, and cover the risk introduced? | Test diff, targeted runs, fixtures, mutation/property/contract tests when useful |
| Observability and operations | Can operators detect, diagnose, and recover from failure? Are logs safe and useful, metrics/traces/alerts, timeouts, health checks, rollout, migration, rollback, and runbooks aligned? | Instrumentation, dashboards/alerts, deploy config, rollback plan, runbook |
| Dependencies and supply chain | Are new or changed dependencies necessary, maintained, pinned/resolved correctly, licensed appropriately, and free of known or configuration-induced risk? | Manifest/lockfile diff, dependency review, advisories, provenance, build scripts |
| Documentation and user impact | Are public behavior, configuration, usage, migration, release notes, and generated docs updated where the change requires it? | README/API docs, examples, changelog, migration notes |
| Maintainability | Is the design understandable, cohesive, testable, and consistent with local patterns without duplicating ownership or hiding complexity? | Code structure, names/comments for intent, duplication scan, future-change impact |

For security-sensitive changes, additionally identify assets, entry points, trust boundaries, attacker-controlled inputs, security controls, and likely abuse paths. For service changes, identify SLO/error-budget impact, capacity limits, backpressure, degradation behavior, and rollback criteria.

### 5. Classify and prioritize findings

Use the highest justified severity, not the most alarming wording:

- `P0` — catastrophic or actively exploitable risk: probable data loss, systemic outage, credential compromise, or equivalent. Stop approval immediately.
- `P1` — high-impact correctness, security, data, availability, or contract defect likely to affect production or block safe rollout. Request changes.
- `P2` — material but bounded defect, regression, missing protection/test, operational risk, or maintainability issue that should normally be fixed in this change. Request changes when it affects the stated scope; otherwise make it an explicit follow-up.
- `P3` — low-impact, non-blocking improvement with clear value and evidence. Do not hold the change solely for P3.
- `NIT` — optional style or readability polish. Use sparingly and never block.

Label confidence separately: `confirmed` (reproduced or directly proven), `high` (strongly implied by code/contract), `medium` (plausible but missing a decisive fact), or `low` (request for investigation). Only `confirmed` or `high` findings should normally affect the gate; a medium/low hypothesis may block only when the potential impact is severe and the missing evidence is a required safety check.

Write findings as: **evidence → impact → why this change causes it → specific remediation or verification**. Avoid vague advice, duplicate findings, speculative “could” statements presented as fact, and requests to rewrite working code merely to match personal taste.

### 6. Use review-tool mechanics correctly

When a PR review tool is available, review the purpose/context first, inspect the diff file-by-file, use line- or file-scoped comments for actionable issues, group pending comments, and submit one summary decision. Re-review changed lines after each new commit; stale approvals or changed files require a fresh review according to repository protection rules.

If no connector is available, emit ready-to-post comments and clearly say they were not posted. Never claim to have approved, requested changes, merged, commented, or run CI without evidence.

## Stop and approval gate

Stop and return `CANNOT_COMPLETE` or `REQUEST_CHANGES` when any of the following is true:

- intent, baseline, affected contract, or required repository rule is missing enough to prevent a safe judgment;
- a confirmed `P0`/`P1` exists, or an unverified safety-critical risk remains blocked on required evidence;
- required lint, type, test, build, migration, security, or dependency validation fails or is blocked;
- the diff changes behavior outside the declared scope, leaves an incompatible API/data migration, or cannot be safely rolled back;
- the reviewer cannot establish coverage of an applicable matrix area.

Return `APPROVE` only when scope and intent are understood, every applicable matrix area is covered or explicitly marked `N/A`/`BLOCKED`, required validation passes, no unresolved blocking finding remains, and the change is a net improvement to code health. Return `COMMENT_ONLY` when there are no blocking findings but useful P2/P3/NIT feedback or hypotheses remain. An approval is not a claim that no defects exist; it is a bounded decision based on the recorded evidence.

## Exact output format

Return this structure exactly, keeping sections even when empty. Replace every placeholder such as `<target>` or `<...>` with evidence from the review; write `None` when a section has no entries.

```markdown
# Code review: <target>

## Decision
<APPROVE | REQUEST_CHANGES | COMMENT_ONLY | CANNOT_COMPLETE>

## Scope and intent
- Target/base: <...>
- Intent: <... or Intent unknown>
- Changed surface and risk hotspots: <...>
- Exclusions or blocked context: <... or None>

## Validation
| Command | Result | Evidence or reason |
|---|---|---|
| `<exact command>` | PASS/FAIL/BLOCKED/NOT RUN | <short result> |

## Coverage
| Matrix area | Status | Evidence or reason |
|---|---|---|
| Intent and context | COVERED/N/A/BLOCKED | <...> |
| Correctness | COVERED/N/A/BLOCKED | <...> |
| Edge cases and resilience | COVERED/N/A/BLOCKED | <...> |
| Security | COVERED/N/A/BLOCKED | <...> |
| Data and API contracts | COVERED/N/A/BLOCKED | <...> |
| Architecture | COVERED/N/A/BLOCKED | <...> |
| Performance and capacity | COVERED/N/A/BLOCKED | <...> |
| Tests | COVERED/N/A/BLOCKED | <...> |
| Observability and operations | COVERED/N/A/BLOCKED | <...> |
| Dependencies and supply chain | COVERED/N/A/BLOCKED | <...> |
| Documentation and user impact | COVERED/N/A/BLOCKED | <...> |
| Maintainability | COVERED/N/A/BLOCKED | <...> |

## Findings
### F-001 — [P1] <short title> — `<path>:<line>` — confidence: confirmed
- Evidence: <specific code, contract, test, command, or reproduction>
- Impact: <user/system/security consequence>
- Why this change causes it: <before/after reasoning>
- Recommendation: <smallest safe fix or required decision>

<Repeat in severity order. Write `None` when empty.>

## Hypotheses and follow-ups
- H-001 — [P2/P3] <unconfirmed concern>; evidence missing: <...>; verify with: <...>; not a confirmed finding.

<Write `None` when empty.>

## Strengths
- <specific evidence-backed positive observation>

## Residual risk and approval gate
- Required follow-ups: <... or None>
- Residual uncertainty: <... or None>
- Gate rationale: <why the decision follows from scope, coverage, findings, and validation>
```

## References

Use these as external guidance, not as a substitute for repository-specific evidence:

- [Google Engineering Practices — Code Review](https://google.github.io/eng-practices/review/)
- [Google — The Standard of Code Review](https://google.github.io/eng-practices/review/reviewer/standard.html)
- [Google — What to Look For in a Code Review](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
- [OWASP Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html)
- [GitHub Docs — Reviewing proposed changes in a pull request](https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/reviewing-proposed-changes-in-a-pull-request)
- [GitHub Docs — Adding agent skills](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [Comparable skill collection pattern](https://github.com/JUNERDD/skills/tree/main/skills/code-review)
