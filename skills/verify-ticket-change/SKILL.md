---
name: verify-ticket-change
description: Use to verify a software change against expected behavior and related features. Use after implementation or user test feedback. Obey verification-only task limits.
---

# Verify Ticket Change

## Find the version under test

Read the latest behavior examples, affected code, diff, and earlier results.
Make sure the test environment uses the current code.
Examine code changes that have not had code review.
Within full execution, use `implement-review-ticket` when necessary.

## Do the checks

1. Do the required project checks.
2. Do tests for changed behavior and affected contracts.
3. Examine runtime behavior when you have access.
4. Compare actual and expected results.
5. Find the cause of each failure before code changes.

A build pass does not prove runtime behavior.
A mocked test does not prove that an external integration works.
Identify new defects, existing defects, fixture errors, and environment failures.
Do not change tests or expected behavior only to get a pass.

## Find failure causes

Within full execution, send code defects to `implement-review-ticket`.
Send structural problems to `plan-ticket-change`.
Send unresolved or changed requirements to `clarify-ticket-behavior`.

For verification only, give defects without repairs without the user's permission for repairs.
After repairs, examine the diff again. Do tests again when their results no longer apply.
Add wider tests only when the effects or failures make them necessary.

## Complete verification

Do all useful checks within your access and permissions.
For user checks, give a short action list with expected results and necessary setup.
Use user feedback within the limits of what the user tested.

Identify the change as verified only when necessary results apply to the current code.
Give any missing check or decision.
A test pass does not give deployment, user approval, or release approval.

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
