---
name: clarify-ticket-behavior
description: Clarify desired behavior and acceptance scenarios for a software ticket with minimal questions. Use as the behavior stage of Execute Ticket, when requirements conflict or are incomplete, or when review/testing reveals a product decision. Do not trigger for unrelated writing or generic product brainstorming.
---

# Clarify Ticket Behavior

## Check the starting point

Read the ticket, latest user decisions, relevant current behavior, and any reported failures. Treat ticket wording as intent and existing code as evidence of current behavior; neither automatically resolves contradictions. Distinguish a requested change from an existing contract that must be preserved.

## Establish behavior

1. Identify the user/problem, trigger, expected observable result, and non-goals. For a bug, distinguish actual from expected behavior and reproduce when feasible.
2. Establish a few concrete acceptance examples, including the main path and consequential boundaries or failure states. Consider permissions, empty states, invalid input, persistence, and interaction with adjacent behavior only where relevant.
3. Inspect code or tests enough to avoid asking questions the repository can answer. Treat missing product decisions as decisions, not implementation details.
4. Ask only consequential unresolved questions, ideally one focused batch with recommendations. For example: "When a filter changes, should selection persist? I recommend clearing it to avoid acting on hidden items." Do not demand exhaustive acceptance criteria or signoff for ordinary fixes.
5. Keep examples internally or briefly in conversation where clarification is needed. Do not generate a separate requirements document or update an external ticket without authorization.

## Exit and return

Proceed to `plan-ticket-change` when behavior is sufficiently clear to implement and verify, including compatibility constraints. When reopening after feedback, identify the changed rule and affected acceptance examples, preserve previous valid decisions, and require impact reassessment before editing code. Treat substantial newly requested behavior as a scope decision; do not silently bundle it into the original task.

## Working contract

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
