---
name: verify-ticket-change
description: Verify acceptance behavior and relevant regressions for implemented software tickets. Use after implementation/review, after human test feedback, or after changes invalidate earlier evidence. Diagnose failures and return to behavior, planning, or implementation as needed.
---

# Verify Ticket Change

## Validate the subject

Check latest acceptance examples, affected surfaces, current diff, and previous evidence. Confirm the version/environment under test corresponds to the current code. Review any changes that have not yet been reviewed; return to `implement-review-ticket` when required.

## Gather evidence

1. Run the project's required checks and relevant targeted tests. Exercise the changed runtime behavior when tooling and access allow, including consequential edge/failure cases and affected existing features.
2. Distinguish passing static checks from demonstrated runtime behavior. A successful build alone does not establish acceptance. A mocked unit test does not establish an external integration works.
3. Compare observed results to expected behavior. Diagnose failures before changing code. Establish whether a failure is introduced by the task, pre-existing, a bad test/fixture, or an environment limitation.
4. Route clear code defects to `implement-review-ticket`, impact/architecture issues to `plan-ticket-change`, and unclear or changed expectations to `clarify-ticket-behavior`. Update relevant acceptance examples after a decided behavior change; never quietly change them to excuse a failure.
5. After changes, re-review the diff and rerun invalidated checks. Broaden testing when shared impact or new failures justify it; reuse evidence that still applies. Do not repeatedly rerun unchanged passing checks without a reason.

## Human testing and completion

Perform all feasible checks yourself. For checks requiring the user, give a small batch: action, expected result, and any setup required. Prioritize scenarios that need human judgment or unavailable access. Avoid handing the user a long generic QA checklist.

When user feedback arrives, request only missing reproduction details needed for diagnosis; reuse ticket context. Treat a reported result as evidence with its stated limits, not proof that every scenario passed.

Mark verified only when relevant acceptance and regression evidence apply to the current code and no material decision remains unresolved. Otherwise state the precise limitation or remaining check. Finish briefly with changed behavior, verification performed, and unresolved issues. Never claim deployment, human signoff, or release approval from test success alone.

## Working contract

- For a named stage handoff, load the corresponding skill by exact frontmatter name from the available catalog or personal-skills checkout, not a hardcoded sibling directory. Report a missing component briefly and perform its responsibility from the available workflow; never claim it was loaded.
- Use the ticket, repository, and conversation as the working record. Do not create per-change briefs, plans, checklists, reports, or other process files unless explicitly requested or required by the project. Keep working state in conversation context; do not expose a ledger after every stage.
- Keep these facts available internally: desired behavior and examples; scope and non-goals; unresolved decisions; affected surfaces and chosen approach; current diff; verification evidence and remaining checks. Reconstruct missing facts from source evidence on resume; never assume a previous stage passed.
- Read relevant project instructions and respect the user's authorized scope. Use available tools to do the work. Never invent repository access, execution results, skill invocation, or test evidence.
- Ask only when an answer materially changes behavior, scope, compatibility, or risk and cannot be established from evidence. State the decision, recommended option, and consequence briefly. Continue independent work while waiting; do not implement a consequential unresolved choice.
- Infer routine implementation details and proceed. Do not request approval at every stage. Follow actual authorization boundaries for publication, external messages, and irreversible actions; do not invent approval gates.
- Communicate meaningful findings and decisions concisely; omit routine logs, repeated plans, and pasted code unless requested. Give reviewers a few relevant file/function pointers and decision reasons, not a narration of every edit.
- Treat the user's correction or observed result as new evidence. Identify which assumptions it invalidates, retain valid work, and reopen only affected stages. After any code change, review the resulting diff and rerun checks whose evidence became stale.
- Diagnose a failed check before routing it. Distinguish implementation defects, structural problems, requirement ambiguity, and environment failures. Never weaken assertions or redefine acceptance simply to obtain a pass.
- End stage work with an internal handoff: validated facts, consequential changes, unresolved issues, and next stage. When working within the coordinated workflow, continue to that stage automatically; do not ask the user to invoke it. For an explicitly limited request, respect the requested stopping point.

## Exact output format

Keep routine stage handoffs internal and continue automatically. When a consequential user decision is needed, give the question, recommended option, and consequence in a short paragraph. For a completed or blocked task, give changed behavior, relevant verification evidence, and any remaining decision or human check in a few sentences or bullets. Omit empty items and mandatory headings; do not produce a separate report.
