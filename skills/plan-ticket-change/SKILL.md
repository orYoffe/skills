---
name: plan-ticket-change
description: Use to examine codebase effects and select an approach for a software ticket. Use before implementation or after a structural problem appears.
---

# Plan Ticket Change

## Examine the codebase

1. Read the expected behavior and project instructions.
2. Examine the current diff and related code.
3. Read the code path from the entry point to the result.
4. Find shared code, callers, and related tests.
5. Find contracts and behavior that must stay unchanged.

A difference between current and requested behavior is normal for a change or bug fix.
Go to `clarify-ticket-behavior` only for an unresolved requirement, compatibility decision, or product choice.

## Select the approach

Select the smallest change that gives required behavior and uses codebase patterns.
Use suitable existing patterns.
Do not add layers or options for possible future requirements.

Include a refactor only when it makes the required change correct, clear, or safe to verify.
Keep optional cleanup outside the task.
If a related change exceeds agreed behavior or task limits, get the necessary decision before implementation.
Effects on other users do not require a new decision when those effects are already agreed.

For a large change, select small parts with complete behavior.
Select useful tests for each part and each affected contract.
For code with weak test coverage, find a way to protect existing behavior before a large refactor.

Keep the approach in context. Show important choices and reasons.
Do not make a plan document unless requested or necessary.

## Use the result

Within the full workflow, go to `implement-review-ticket` with the approach and test method.
For a direct request, give the approach and stop.
If new information changes the approach, examine only the affected work again.

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
