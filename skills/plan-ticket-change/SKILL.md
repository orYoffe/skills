---
name: plan-ticket-change
description: Investigate codebase impact and choose a focused implementation for a software ticket. Use after behavior clarification, when planning necessary refactoring or related feature adjustments, or when implementation/testing reveals architectural or dependency problems.
---

# Plan Ticket Change

## Validate behavior against the codebase

Read the established behavior, relevant project instructions, current diff, and entry points. Trace the real path across UI, state, services, storage, shared utilities, or external contracts as applicable. Inspect callers and existing tests rather than relying solely on filenames.

Treat a difference between current and requested behavior as expected for a change or bug fix. Return to `clarify-ticket-behavior` only when evidence reveals an unresolved contradiction in the desired behavior, an unclear compatibility requirement, or a consequential product choice affecting adjacent features.

## Choose the approach

1. Identify affected components and consumers, invariants to preserve, and likely regression surfaces. Check whether other features depend on the same code or data contract.
2. Choose the smallest coherent change that fits established patterns. Prefer existing abstractions; avoid adding frameworks, layers, broad renames, or hypothetical extensibility.
3. Include refactoring only when needed for correctness, understandable implementation, or safe verification. Separate necessary refactoring from optional cleanup. Explain consequential refactoring briefly; do not require a ceremonial plan approval.
4. Adjust related code when necessary to keep established behavior consistent. Ask for a decision when the adjustment changes other users' behavior or materially expands scope; do not quietly redefine another feature.
5. Select verification based on the acceptance examples and affected boundaries. Identify meaningful automated checks and any interaction that will require runtime or human testing. Inspect baseline failures when relevant and feasible.
6. Sequence work in small coherent pieces with distinguishable behavior and structural changes when practical. Keep the approach internally; show only consequential tradeoffs or decisions.

## Exit and return

Proceed to `implement-review-ticket` with a concrete approach, affected surfaces, and verification strategy. Reopen this stage if new evidence changes architecture or impact. Reuse unaffected code and checks; do not restart the whole investigation.

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
