---
name: execute-ticket
description: Coordinate software feature, change, and bug-fix tickets through behavior clarification, codebase planning, implementation review, and verification with minimal reading overhead. Use when receiving a software task to execute end to end, or resuming it after review, test results, or changed requirements.
---

# Execute Ticket

Own progress from the ticket to a verified result. Use four working skills: `clarify-ticket-behavior`, `plan-ticket-change`, `implement-review-ticket`, and `verify-ticket-change`.

## Load and route

1. Read the ticket and available repository context. Establish the project, requested scope, current working changes, and any existing acceptance evidence. If the ticket or repository is inaccessible, request the minimum missing input and do useful available work; do not claim execution.
2. Resolve each working skill by its exact frontmatter name from the available catalog or personal-skills checkout. Load its instructions before using it. Do not hardcode sibling directory names: installed skill directories may be renamed. If a skill cannot be found, report the missing component briefly and perform its responsibility using this workflow; do not pretend it was invoked.
3. Begin with behavior, then plan, implement/review, and verify. Compress obvious stages for a small fix, while still checking behavior, impact, diff, and relevant evidence. Do not load all skills at once unnecessarily.
4. Track status internally as active, waiting for a decision/input, ready for human verification, verified, or blocked. Treat skill handoffs as instruction-based routing, not a background automation engine. Continue in the same turn while tools and authorization allow.

## Route new findings

| Finding | Return to | Then continue |
|---|---|---|
| Missing, contradictory, or changed expected behavior | Clarify behavior | Reassess impact, implement/review, verify |
| Architecture mismatch or newly affected shared code | Plan change | Implement/review, verify |
| Wrong code with clear expectations and suitable approach | Implement/review | Verify |
| Bad fixture, unavailable environment, or suspect evidence | Verify | Diagnose; route only if a product/code problem is established |
| Optional unrelated improvement | Keep outside scope | Mention only if consequential; continue current task |

Avoid endless loops. If the same failure recurs without new evidence, improve diagnosis or ask for the specific missing decision/access instead of repeating edits.

## Finish

Conclude only when relevant acceptance and regression evidence apply to the current code and no consequential decisions remain unresolved. If human testing is needed, provide a small actionable batch with expected results and mark the task ready for human verification, not fully verified. Resume from the reported results without asking the user to restate the ticket.

Give a short final: resulting behavior, relevant validation, and any material limitation or remaining human check. Provide a compact review focus when a human code review is requested. Do not automatically post ticket comments, close tickets, open PRs, merge, or deploy unless authorized.

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
