---
name: service-improvement
description: Use to examine or improve a software service. Use for performance, reliability, security, contracts, operations, and recovery. Change code only with the user's permission.
---

# Service Improvement

Find service problems from source records and measurements.
Start read-only. Change the service only within the user's permitted task.

## Find the task limits

Find the service, revision, environment, user paths, goal, and task limits.
Find permitted actions and production limits.
For a planned service, do not invent runtime measurements or operating targets.

Examine entry points, data paths, queues, stores, dependencies, and deployment units.
Use code and configuration first. Compare them with runtime records when available.
Identify uncertain connections as unverified.

## Find baseline results

Find the workload, time window, environment, and measurement method.
Find existing service targets and limits.
If targets are missing, propose targets rather than state them as established facts.

Use user-visible measures such as errors, response time, data freshness, queue age, and recovery time.
Examine distributions when averages hide important results.
Record missing measurements as not measured.
Do not use laboratory results as proof of production behavior.

## Find the cause

Examine a representative request or work item.
Compare failures with dependency, workload, and deployment changes.
Find the limiting resource or failing contract.
Use profiling or controlled tests only when safe and representative.
Do not propose a rewrite, cache, or increased concurrency without a supported reason.

## Examine the service

| Area | Examine |
|---|---|
| Performance | Slow paths, query counts, resource limits, queues, and capacity. |
| Reliability | User targets, correct results, dependency limits, and degraded behavior. |
| Structure | Ownership, boundaries, dependencies, error paths, and repeated policy. |
| Contracts | Schemas, compatibility, events, duplicate requests, and migrations. |
| Security | Permissions, isolation, secrets, unsafe inputs, logs, and dependency sources. |
| Operations | Logs, metrics, traces, alerts, instructions, and operational ownership. |
| Deployment | Reproducible builds, checks, staged changes, health signals, and rollback. |
| Recovery | Timeouts, bounded retries, load control, backups, and restore tests. |
| Tests | Behavior, integration, load, failures, migrations, and recovery. |
| Dependencies | Versions, advisories, support, quotas, and supply-chain records. |
| Maintenance | Clear code, current docs, obsolete paths, cost, and manual work. |

Identify real defects and unverified concerns separately.
Record unavailable checks and areas outside the task.
One clean scanner result does not prove security.

## Make permitted changes

Select a small change with a clear expected effect.
Find tests that protect existing behavior.
For a risky change, set success limits and stop limits before deployment.
Find a rollback method that includes data and configuration effects.
For a canary, set its sample, control, time window, and person with stop authority.
Keep migration steps compatible until consumers can use the new contract.

Do the useful project checks. Compare the same measures under comparable workloads.
Give other possible causes that the comparison cannot exclude.
If a stop limit is exceeded, use the permitted stop or rollback method.
Do not call a change an improvement without supporting results.

## Give findings

Put findings in sequence by effect, urgency, confidence, and repair effort.
Use P0 for critical defects, P1 for high impact, and P2 for important bounded defects.
Use P3 for small improvements and P4 for information.
Give a source, expected user effect, smallest correction, and verification method.
Give remaining risk or missing measurements.

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
