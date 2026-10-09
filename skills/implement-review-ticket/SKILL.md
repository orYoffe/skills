---
name: implement-review-ticket
description: Use for implementation of an agreed software change and examine its diff. Use for code defects or code review comments. Keep review-only requests read-only.
---

# Implement and Review Ticket

## Before code changes

Read the latest behavior, approach, project instructions, and diff.
For an unresolved requirement, go to `clarify-ticket-behavior`.
For an unsuitable approach, go to `plan-ticket-change`.
For a review-only request, examine the code without repairs.

## Write the change

Write a small part with complete behavior.
Use the project's code patterns.
Add tests when they protect behavior or the project requires them.
Do not add tests that only repeat the code structure.

Examine each part before the next part.
Do useful checks within your permissions and tool capabilities.
If the user requests code review before tests, stop at that checkpoint.
Do not complete a large feature in one step without checks.

## Simplify the code

Use clear code. Fewer lines alone do not make code better.
Before removal of a helper or branch, find the behavior or constraint that it protects.
Simplify only within the task limits.
Make sure the required behavior stays unchanged.
Use a project review method when requested or required.

## Examine the full diff

Examine behavior, error paths, permissions, shared consumers, and data contracts.
Examine state changes and asynchronous actions where applicable.
Find duplicate logic, unnecessary branches, and abstractions without a present purpose.
Make sure tests still examine behavior.

Correct defects within the permitted task. Then examine the changed code again.
If a user comment changes behavior, go to behavior.
If a comment changes the approach, go to planning.
Explain a suggestion that conflicts with a required contract.

## Use the result

Within the full workflow, go to `verify-ticket-change` with the diff and current test results.
For a direct request, stop at the requested result.
Give a few file or function pointers for human code review.
Do not call your own code review independent.

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
