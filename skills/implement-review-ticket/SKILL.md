---
name: implement-review-ticket
description: Implement software ticket changes and review the resulting diff for behavior, correctness, simplicity, and codebase fit. Use after ticket planning, when addressing review comments, or when verification identifies a code defect with clear expected behavior.
---

# Implement and Review Ticket

## Validate before editing

Check latest behavior, approach, project instructions, working diff, and related callers. Preserve unrelated user changes. If required behavior is unresolved, return to `clarify-ticket-behavior`; if the approach no longer fits, return to `plan-ticket-change`.

## Implement

Make small coherent edits that satisfy observable behavior and preserve relevant contracts. Follow existing patterns and avoid unrelated cleanup. Add or adjust tests when meaningful for the change and required by project instructions. Prefer behavior assertions over tests that merely mirror implementation; do not add ritual tests for trivial low-impact edits.

Run useful checks during implementation when available. Do not postpone all validation until the user can test. Separate inability to execute a check from a failing product.

## Review before handoff

Review the actual complete task diff, not only the last edit. Check:

- Coverage of intended behavior and relevant failures, boundaries, and permissions.
- Correctness across affected consumers, state transitions, async flows, and data contracts where relevant.
- Unnecessary branches, duplicate logic, unjustified abstractions, excessive configuration, and avoidable diff size.
- Consistency with codebase patterns, readability, and regressions caused by refactoring or related feature changes.
- Tests that verify behavior without being weakened to accommodate a bug.

Fix discovered problems within scope, then re-review affected code. Treat user review comments as evidence: simplify when behavior can be preserved; route to behavior or planning when a comment changes the contract or approach. Do not accept a suggestion mechanically if it breaks established behavior; explain the concrete conflict briefly.

## Exit

Proceed to `verify-ticket-change` with the reviewed current diff, checks already run, and remaining evidence needed. Report human review focus only where useful, using a few file/function pointers and reasons. Never claim independent review when only this agent reviewed the change.

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
