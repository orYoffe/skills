---
name: clarify-ticket-behavior
description: Use to find expected behavior for a software ticket. Use when requirements are missing or conflict. Use after feedback changes a requirement.
---

# Clarify Ticket Behavior

## Find the expected result

1. Read the ticket and latest user decisions.
2. Examine the related code and tests.
3. Read existing domain terms and decisions.
4. Find the expected result and task limits.
5. Give concrete examples for the main behavior and important failure cases.

For a bug, compare actual and expected behavior.
Use existing code as a source of facts. Get required behavior from the ticket and user decisions.
Use examples to explain terms with different possible meanings.
Do not make a glossary or decision document unless requested or necessary.

## Give decision questions

Find facts from available sources before you give the user a question.
Give questions only for choices that affect behavior, task limits, compatibility, or risk.
Give each question with a recommendation and reason.

If one choice depends on another choice, give the questions in sequence.
Wait for each necessary answer. Continue work that does not depend on that answer.
You can group independent questions if the user prefers that method.

For a requested interview, examine the related choices in more detail.
Stop when expected results are testable and necessary decisions within the task limits are resolved.
Do not extend the interview to unrelated choices.
Do not make a new approval necessary for routine decisions.

## Use the result

Within the full workflow, go to `plan-ticket-change` when behavior is clear enough to implement and verify.
For a direct request, give the behavior result and stop.

After feedback, give the changed requirement. Update the affected examples.
Examine the effect on related code before code changes.
Keep earlier decisions that still apply.

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
