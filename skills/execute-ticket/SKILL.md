---
name: execute-ticket
description: Use for implementation or continuation of software tickets. Select behavior, planning, implementation, code review, and verification stages. Keep user decisions and results short.
---

# Execute Ticket

Help the user complete a software task with less mental effort.
Use only the necessary stages. Change the method to meet the user's request.

## Select the work

1. Read the task and project instructions.
2. Find the requested result and task limits.
3. Find each requested checkpoint.
4. Select the first stage that needs work.

A request to plan, examine, or verify does not give permission for code changes.
An implementation request gives permission for the necessary code changes and checks.
Use established decisions and test results when they still apply.
Do not start a new interview for every ticket.

## User choices

Use preferences from the conversation or existing project instructions.
Do not make a configuration file necessary.

| User request | Action |
|---|---|
| Plan only | Give the approach. Stop before code changes. |
| One question at a time | Give one decision question. Wait for the answer. |
| Wait for code review | Show the diff. Stop at the requested checkpoint. |
| Verify without repairs | Do the checks. Give defects without code changes. |
| Use our method | Use the applicable project method. |

## Select a stage

| Work needed | Skill |
|---|---|
| Find expected behavior | `clarify-ticket-behavior` |
| Select code changes | `plan-ticket-change` |
| Write and examine code | `implement-review-ticket` |
| Verify behavior | `verify-ticket-change` |

Find skills by their frontmatter names. Use the available catalog, project folders, or personal skill folders.
Read each skill before use. A skill name alone does not load its instructions.
If a skill is missing, give that limit. Do its work from the available instructions.

## Use new results

For an unclear requirement, go to behavior.
For an unsuitable code structure, go to planning.
For a code defect with clear requirements, go to implementation.
For an environment or fixture failure, stay in verification until the cause is clear.

If a failure repeats without new information, stop the repeated action. Find the missing information or decision.
Do not weaken tests to get a pass.

## Complete the task

For clarification, finish with testable expected results and resolved necessary decisions.
For planning, finish with an approach, affected contracts, and a test method.
For implementation and review, finish with the permitted code changes and supported findings.
For review only, finish with supported findings and the examined revision.
For verification, finish with current results and any missing checks.

For a stage-only task, stop when that stage is complete.
A completed plan or code review does not mean the implementation is verified.
For full implementation, make sure the results apply to the current code.
Do not identify work as verified while a necessary check or decision is missing.

For user tests, give a short set of actions and expected results. Identify the task as ready for those tests.
Continue from the user's results. Do not tell the user to give the ticket again.

## Work rules

Obey the task limits and project instructions. Use permission that the user already gave.
Keep unrelated user changes. Do not publish or change external systems without permission.

Use the ticket, code, and conversation as the work record. Do not make task documents unless requested or necessary.
Keep decisions and test results in context. If context is missing, read the source again.
Do not invent access, results, or user approval.

Within `execute-ticket`, continue to the next necessary stage. Stop at each checkpoint that the user requests.
For a direct stage request, complete that stage and stop. Do not start other work without permission.

If a result changes an earlier decision, go to the first affected stage.
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

Start with the result or necessary decision. Give the source, effect, and next action only when necessary.

Give a recommendation with each decision question. At a checkpoint, give the remaining work. At that checkpoint, wait for the user.

For completed work, give the change and tests. Give the limits of verification.

Do not add empty sections or routine logs. Give more detail only when requested or necessary for the task.
