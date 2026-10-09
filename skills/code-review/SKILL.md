---
name: code-review
description: Use for a read-only examination of a PR, commit, diff, or code change. Find defects in behavior, security, contracts, tests, and maintainability.
---

# Code Review

Examine a code change against its task and codebase.
Do not change code or external systems unless the user requests repairs.

## Find the versions for comparison

1. Find the repository, base revision, and changed revision.
2. Read the task and project instructions.
3. Examine the full diff, including configuration and generated files.
4. Read the related code, callers, contracts, and tests.
5. Find the expected behavior and task limits.

Keep unrelated user work unchanged.
If necessary information is missing, give that limit.
An agent's summary is not proof.

## Examine the change

Examine important input, permission, state, storage, and output paths.
Examine success and failure behavior.
Use the following areas as an internal guide.
Do not print the full guide in routine results.

| Area | Examine |
|---|---|
| Behavior | Expected results, boundaries, ordering, retries, cancellation, and partial failures. |
| Security | Input handling, permissions, data isolation, secrets, logs, and unsafe external access. |
| Contracts | Schemas, consumers, compatibility, migrations, and duplicate requests. |
| Structure | Responsibilities, dependencies, code patterns, and unnecessary complexity. |
| Performance | Hot paths, query counts, memory, queues, and resource limits. |
| Tests | Behavior assertions, failure cases, isolation, and repeatable results. |
| Operations | Detection, recovery, alerts, deployment, and rollback. |
| Dependencies | Versions, support, license terms, advisories, and build sources. |
| Documents | Changed behavior, configuration, and user instructions. |

Use required project checks. Start with checks for the changed area.
Use wider checks when the effects make them necessary.
Without permission, do not install dependencies or change live data only to make checks pass.
Record each command and result in context.
Use `PASS`, `FAIL`, `BLOCKED`, or `NOT RUN` for check results.

## Select findings

Give each finding a source, effect, and smallest useful correction.
Identify observed defects and unverified concerns separately.
Keep finding IDs stable during later code review.
Do not block a change for a style preference.

| Priority | Meaning |
|---|---|
| P0 | Immediate severe security, data, or system failure. |
| P1 | High-impact defect that prevents safe release. |
| P2 | Important bounded defect within the change. |
| P3 | Small improvement that does not block release. |
| P4 | Information or an optional experiment. |

## Select the decision

Use `REQUEST_CHANGES` for a supported blocking defect or a failed necessary check.
Use `CANNOT_COMPLETE` when missing information prevents a useful decision.
Use `COMMENT_ONLY` for useful findings that do not block the change.
Use `APPROVE` only when necessary checks pass and no supported blocking finding remains.
An approval applies only to the examined version and task limits.
Code review approval does not give permission to merge or release.

## Work rules

Obey the task limits and project instructions. Use permission that the user already gave.
Keep unrelated user changes. Do not publish or change external systems without permission.

Use the ticket, code, and conversation as the work record. Do not make task documents unless requested or necessary.
Keep decisions and test results in context. If context is missing, read the source again.
Do not invent access, results, or user approval.

Stop at each checkpoint that the user requests.
Do not start other work without permission.

If new information changes a decision, examine that decision again.
Keep work that is still correct. After code changes, examine the diff again.
Do tests again when their results no longer apply.

## English text

Use ASD-STE100 rules for English text. Use approved words with their approved meanings.
Use necessary software terms consistently. Keep sentences within 20 words.
Write in the active voice.
Give one instruction per sentence. Use each technical term with one meaning.
Do not use contractions. Keep commands and identifiers unchanged.
Keep user updates short. Show decisions, problems, and results.

## Exact output format

Start with the code review decision and examined revision. Give the source, effect, and next action only when necessary.
Give a recommendation with each decision question. At a checkpoint, give the remaining work. At that checkpoint, wait for the user.
For completed work, give the change and tests. Give the limits of verification.
Do not add empty sections or routine logs. Give more detail only when requested or necessary for the task.
