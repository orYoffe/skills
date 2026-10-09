---
name: agent-usage-review
description: Use for a read-only examination of AI agent workflows, prompts, tools, traces, and task handoffs. Find problems in user control, verification, cost, and failure handling.
---

# Agent Usage Review

Examine whether an agent workflow serves its stated task.
Start read-only. Do not repair the workflow unless the user requests changes.

## Find the task limits

Read the user goal, task limits, project instructions, and available records.
Find the agents, tools, services, data, and user decisions in the workflow.
Do not invent a provider, tool, or system structure.

Examine one actual task from request to result.
For each stage, find its inputs, outputs, owner, allowed actions, and stop condition.
Use prompts, code, configuration, traces, and tests as sources.
A prompt describes intended behavior. It does not prove actual behavior.

## Examine the workflow

| Area | Examine |
|---|---|
| Task ownership | Clear roles, task limits, result ownership, and reasons for extra agents. |
| Context | Necessary facts, source links, current state, and full constraints. |
| Trust | Private data, secrets, prompt injection, and confusion between data and instructions. |
| Task order | Required inputs, independent actions, shared writes, and conflicting results. |
| Tools | Actual capabilities, target limits, credentials, permissions, and result checks. |
| Verification | Behavior tests, failure cases, independent state checks, and limits of self-evaluation. |
| Failures | Safe retries, attempt limits, original errors, partial work, and stop conditions. |
| Handoffs | Current status, versions, decisions, source records, ownership, and next actions. |
| Operations | Useful logs, error signals, response time, cost, and repeated work. |

Use one agent when one agent can do the task well.
Use more agents only when the task and available controls justify them.
Do dependent work in sequence.
Do parallel work only when inputs and changes are independent.
Examine completeness and conflicts before combination of results.

Use narrow tool permissions. Keep secrets out of prompts, logs, and reports.
Use permission already given for external actions.
For an irreversible action, obey the applicable authorization rules.
Make sure the result matches the intended target.

## Examine failure behavior

Find the difference between temporary errors, permanent errors, missing permission, and invalid results.
Use bounded retries only for work that is safe to repeat.
Stop for missing decisions, task-limit breaches, unsafe actions, or repeated failure without new information.
Do not silently use weaker controls.

## Use test results

Identify observed, inferred, and unverified claims separately.
For a design-only review, identify runtime behavior as unverified.
For an independent evaluation, keep expected answers and prior diagnoses out of the evaluator's context.
Do not count repeated unsupported claims as independent proof.
Use useful measurements for cost and response time. Do not invent measurements.

## Give findings

Give each finding a source, failure effect, correction, and way to verify the correction.
Use P0 for critical defects, P1 for high impact, and P2 for important bounded defects.
Use P3 for small improvements and P4 for information.
Give an owner only when the source identifies the owner.
When necessary information is missing, recommend a way to get it.
Keep detailed coverage records in context unless the user requests them.

## Work rules

Obey the task limits and project instructions. Use permission that the user already gave.
Keep unrelated user changes. Do not publish or change external systems without permission.

Use the ticket, code, and conversation as the work record. Do not make task documents unless requested or necessary.
Keep decisions and test results in context. If context is missing, read the source again.
Do not invent access, results, or user approval.

Stop at each checkpoint that the user requests.
Do not start other work without permission.

If new information changes a decision, examine that decision again.
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
