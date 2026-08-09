---
name: agent-usage-review
description: Review AI agent or subagent orchestration, prompts, tool permissions, traces, delegation, and handoffs. Use for agentic workflow safety, verification, approvals, retries, cost, latency, observability, and stopping decisions; use code-review for ordinary code changes and service-improvement for runtime service diagnosis.
---

# Agent Usage Review

## Purpose

Evaluate whether an agentic workflow is safe, understandable, efficient, and dependable for its stated objective. Inspect the actual task, code, configuration, prompts, traces, artifacts, tests, and operational constraints available in the workspace. Recommend the smallest high-value changes, and separate observed facts from inferences and open questions.

Do not assume a particular model provider, SDK, orchestration framework, connector, or command. Use only capabilities that are present and explicitly available. Do not implement mutations merely because the review identifies them; this skill produces an assessment and a plan unless the user separately authorizes implementation.

## Review stance

- Optimize for correctness, safety, and user control before autonomy or speed.
- Prefer a simple single-agent or deterministic workflow when it satisfies the objective; justify added agents with a measurable benefit.
- Treat delegation as an interface: define the subtask, allowed inputs, allowed actions, expected output, failure contract, and owner of the result.
- Use source evidence over plausible explanations. Label every material conclusion as observed, inferred, or unverified.
- Review the system that exists, including repository conventions and surrounding services; do not grade it against an imagined architecture.
- Make feedback specific, prioritized, respectful, and verifiable. Do not block on style preferences or speculative risks without an impact path.

## Risk boundary for delegation and tools

Classify each agent step and tool operation before recommending delegation or automation:

| Class | Examples | Default treatment |
|---|---|---|
| R0: observational | Read files, inspect configuration, parse traces, compare outputs, inspect test results | Safe to delegate with bounded context; redact secrets and unrelated data. |
| R1: local and reversible | Create a draft, write a temporary artifact, run a local check, edit an explicitly scoped working file | Delegate only with an explicit path/scope, rollback method, and postcondition check. |
| R2: external or consequential | Send messages, change shared systems, publish, merge, deploy, modify production data, spend money, or delete data | Require explicit human approval or an existing policy gate; verify the target and result independently. |
| R3: high-impact or irreversible | Security-sensitive changes, destructive operations, access changes, legal/financial commitments, or production actions with difficult rollback | Keep human ownership of the decision and execution unless a documented control authorizes otherwise. |

Treat a tool as consequential when its side effects are unclear. Never infer that a read-looking operation is harmless if it can expose credentials, trigger billing, change remote state, or disclose private data. Recommend least privilege, scoped credentials, redaction, expiry, and auditability without naming a platform-specific mechanism.

## Repeatable workflow

### 1. Establish objective and review boundary

Record:

- The user outcome, acceptance criteria, and non-goals.
- The system boundary: agents, subagents, prompts, tools, services, data, state, artifacts, and humans in the path.
- The requested review depth and the evidence actually available.
- Any constraints on privacy, latency, budget, reliability, or permitted mutations.

If the objective or boundary is unclear, state the ambiguity and continue with a bounded review. Do not silently expand scope.

### 2. Build an evidence-backed system map

Trace one representative task end to end. Build a compact map of:

`request → planner/router → delegated task(s) → tool/state effects → artifact handoff → evaluator/synthesizer → user or external action`

For each node, capture its role, input contract, output contract, tools, permissions, state, owner, and termination rule. For each edge, capture the dependency, data passed, validation, retry behavior, and whether the edge is sequential, parallel, or conditional.

Inspect, when present:

- Agent and subagent definitions, prompts, routing rules, schemas, and configuration.
- Task plans, execution traces, logs, tool-call records, intermediate outputs, and failure reports.
- Tests, fixtures, evaluation cases, benchmarks, runbooks, security policies, and approval records.
- Repository structure, service boundaries, conventions, build/test commands, and deployment constraints.

Do not treat a prompt, plan, or claimed capability as proof of runtime behavior. Mark claims that lack a trace, test, or implementation path as unverified.

### 3. Review delegation boundaries and role clarity

Ask:

- Is each subtask cohesive, bounded, and independently verifiable?
- Is there one clear owner for orchestration, synthesis, and consequential actions?
- Are roles distinct, or are multiple agents redundantly planning, editing, or deciding?
- Does each delegated task state what it may do, must not do, and must return?
- Is the delegation worth its coordination, context, latency, and failure cost?
- Could a deterministic function, validator, or human decision replace an agent?

Flag unbounded instructions such as “handle everything,” agents that can redefine their own scope, and handoffs that transfer decision authority without transferring evidence or accountability.

### 4. Review context, data, and prompt hygiene

Trace the minimum context required for each step. Check for:

- Unnecessary repository, conversation, user, or tool output copied into prompts.
- Sensitive data, credentials, hidden instructions, or private outputs crossing trust boundaries.
- Prompt injection paths through files, web content, tool results, user-controlled fields, or subagent output.
- Conflicting instructions, stale state, duplicated context, oversized history, or unclear precedence.
- Lossy summaries that omit constraints, provenance, uncertainty, or required fields.
- Untrusted agent output being inserted into a later prompt as if it were an instruction.

Recommend typed, minimal handoffs with provenance and explicit trust labels. Redact secrets in reports; quote only the minimum evidence needed to reproduce a finding.

### 5. Review dependency ordering and concurrency safety

Construct the dependency graph before recommending parallelism. Check:

- Whether every consumer waits for the data or artifact it needs.
- Whether parallel branches are truly independent and have disjoint write scopes.
- Shared files, mutable state, rate limits, locks, ordering requirements, duplicate work, and conflicting updates.
- Idempotency and deduplication for retries or repeated delivery.
- Deterministic merge/synthesis behavior when branches disagree.

Use sequential execution for dependent or conflicting work. Use parallel execution only when the speed or diversity benefit is material, inputs are stable, side effects are isolated, and the join step validates completeness and conflicts.

### 6. Review tools, credentials, and approvals

For every tool-capable agent, identify:

- The exact capability and whether it is read-only, reversible, consequential, or irreversible.
- The narrowest resource, identity, data, and time scope required.
- Whether secrets can appear in prompts, logs, traces, artifacts, errors, or generated code.
- Input validation, output validation, authorization, rate limits, audit records, and failure behavior.
- The human approval point for high-impact, external, or irreversible actions.

Separate “the agent may prepare” from “the agent may execute.” Require a reviewable preview, target confirmation, and postcondition verification before consequential execution.

### 7. Review verification, evaluation, and truthfulness

Check that each important claim or mutation has an appropriate verification path:

- Unit, integration, end-to-end, property, security, or regression checks as appropriate.
- Independent checks of external state rather than trusting a success message or rendered confirmation.
- Evaluation cases covering happy paths, edge cases, adversarial inputs, tool failures, partial completion, and conflicting outputs.
- A baseline and measurable success criteria for quality, safety, cost, and latency.
- Separation of generation from evaluation where an independent check reduces correlated failure.
- Evidence provenance, uncertainty, and explicit handling of “not checked.”

Call out unverified claims, self-approval, evaluator leakage, tests that only inspect implementation details, and evaluations that omit failure or adversarial cases. Do not convert confidence language into evidence.

### 8. Review failure, retry, and stopping behavior

For each failure mode, determine whether the workflow:

- Classifies transient, permanent, policy, validation, authorization, and dependency failures.
- Retries only safe/idempotent work with bounded attempts, backoff, and a clear budget.
- Preserves the original error, evidence, and partial artifacts across retries.
- Avoids duplicate side effects and retry storms.
- Escalates after a threshold or on high-impact uncertainty.
- Stops on success, irrecoverable failure, missing approval, budget exhaustion, conflicting evidence, or scope breach.
- Reports partial completion and residual risk instead of claiming success.

Flag loops that can continue indefinitely, retries that change the task without approval, silent fallback to weaker controls, and “done” conditions based only on the agent saying it is done.

### 9. Review handoffs, operations, and economics

Inspect whether handoffs are durable and actionable:

- Use a stable artifact or structured result with owner, status, inputs, outputs, provenance, timestamp/version, assumptions, and next action.
- Preserve links between decisions and the evidence that supports them.
- Define who can resume, reject, revise, or close the work.
- Track useful operational signals: success and failure by stage, retries, escalations, tool errors, latency, token/input-output volume where available, cost, queue depth, and user-visible quality.
- Identify bottlenecks, redundant calls, oversized context, serial work that can be safely parallelized, and parallel work whose join cost outweighs its benefit.
- Add privacy-aware logs and correlation identifiers without logging secrets or full sensitive prompts by default.

Recommend instrumentation only when it answers a review question or supports an operational decision.

### 10. Prioritize and produce the report

Rank findings by consequence and likelihood, adjusted for evidence quality and reversibility:

- **P0 Critical:** immediate high-impact safety, security, privacy, integrity, or irreversible-action risk; stop or gate the workflow.
- **P1 High:** likely correctness, reliability, authorization, data-loss, or major cost/latency issue; fix before scale or release.
- **P2 Medium:** meaningful maintainability, observability, evaluation, or efficiency gap; schedule a bounded improvement.
- **P3 Low:** localized clarity, ergonomics, or optimization opportunity; address when touching the area.
- **P4 Informational:** observation, question, or optional experiment with no current blocking risk.

Every finding must contain a concrete failure mode, evidence, impact, recommendation, owner or decision-maker, and verification method. Do not report a generic checklist as a finding.

## Review dimensions checklist

Use this checklist as a coverage aid, not as a substitute for evidence:

- Objective and acceptance criteria are explicit.
- Delegation boundaries are narrow and justified.
- Roles and decision ownership are unambiguous.
- Context is minimal, current, provenance-preserving, and appropriately trusted.
- Prompt injection and instruction/data confusion have a mitigation path.
- Dependencies are ordered; parallel work is independent and safely joined.
- Writes have ownership, scope, idempotency, conflict handling, and rollback.
- Tools and credentials use least privilege and avoid secret leakage.
- Consequential actions have approval and independent postcondition checks.
- Claims, outputs, and mutations are verified by suitable tests or evidence.
- Evaluations cover edge cases, adversarial inputs, failures, and regressions.
- Retries are bounded, classified, safe, and observable.
- Partial results, escalation, and stopping conditions are explicit.
- Artifacts have schemas, provenance, ownership, and usable handoff state.
- Cost and latency are measured or bounded, not guessed.
- Logs, traces, metrics, and privacy controls support diagnosis.
- The workflow can degrade safely or return control to a human.

## Exact output format

Return the following sections in this order. Use the shared priority, confidence, evidence-status, and control-status vocabulary in `README.md`. Keep the report concise enough to act on; include only findings supported by evidence or clearly labeled inference. Replace every placeholder. When a section has no entries, write `None`; use `unknown` for evidence that should exist but was not obtained.

```markdown
# Agent Usage Review

## Executive summary
- **Scope:** [task/codebase/workflow and evidence reviewed]
- **Overall assessment:** [sound / needs targeted changes / unsafe to operate as-is / unable to assess]
- **Top risks:** [up to three finding IDs and one-line risks]
- **Recommended decision:** [proceed / proceed with gates / pause and remediate / gather evidence]

## System map
| Stage/agent | Role and owner | Inputs → outputs | Tools/effects | Risk class | Evidence |
|---|---|---|---|---|---|
| ... | ... | ... | ... | R0–R3 | ... |

## Control coverage
| Dimension | Status (covered / partial / gap / blocked / N/A) | Evidence | Needed control |
|---|---|---|---|
| Delegation boundaries | ... | ... | ... |
| Role clarity and ownership | ... | ... | ... |
| Context and prompt hygiene | ... | ... | ... |
| Dependencies and concurrency | ... | ... | ... |
| Tools, credentials, and approvals | ... | ... | ... |
| Verification and evaluation | ... | ... | ... |
| Failure, retry, and stopping | ... | ... | ... |
| Artifact handoffs | ... | ... | ... |
| Cost, latency, and efficiency | ... | ... | ... |
| Observability and operations | ... | ... | ... |

## Prioritized findings
### AUR-001 — [short title]
- **Priority:** [P0–P4]
- **Dimension:** [one dimension]
- **Status:** [observed / inferred / unverified]
- **Evidence:** [file, trace, test, output, or explicit absence; quote minimally]
- **Failure mode and impact:** [what can go wrong, who/what is affected, likelihood if supportable]
- **Recommendation:** [smallest actionable change]
- **Owner/approval:** [role responsible and whether human approval is required]
- **Verification:** [test, measurement, review, or postcondition that proves improvement]
- **Residual risk:** [remaining uncertainty or accepted tradeoff]

<!-- Repeat the finding block. If there are no material findings, write: “No material findings supported by the available evidence.” -->

## Prioritized improvement plan
### Now
1. [P0/P1 changes, gates, or evidence collection]
### Next
1. [P2 changes with measurable acceptance criteria]
### Later / optional
1. [P3/P4 experiments or cleanup]

## Verification plan
| Change or claim | Check | Pass condition | Owner | When |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Open questions and assumptions
- **[Question/assumption]:** [why it matters and how to resolve it]

## Stopping decision
- **Stop or escalate if:** [approval missing, scope breach, unsafe tool, repeated failure, conflicting evidence, budget/retry limit, or other concrete condition]
- **Safe completion condition:** [what must be true before declaring the workflow complete]
- **Residual risk accepted by:** [named role, or “not established”]
```

When reviewing only a design, label runtime behavior as unverified and propose a forward test. When reviewing only traces, avoid inferring code structure that the trace cannot establish. When evidence is missing, make evidence collection the recommendation rather than filling the gap with assumptions.

## Delegation guidance for the reviewer

If additional agents are available, delegate only bounded R0 checks by default: independent inventory, trace extraction, test-result review, or a focused dimension review. Give each delegate the minimum task-local context, an explicit output schema, and no authority to mutate external state. Run checks in parallel only when their inputs and write scopes are independent; otherwise order them by dependency.

Use one synthesis pass to reconcile duplicate or conflicting findings. Require each delegate to return evidence, confidence, unknowns, and suggested verification—not just a verdict. Do not let an evaluator see the intended answer, prior diagnosis, or hidden expected findings when testing whether the review generalizes. Do not count multiple agents repeating the same unsupported claim as corroboration.

## Completion standard

Consider the review complete only when the stated boundary has been covered, every dimension is marked with evidence or “unknown,” material findings are prioritized and actionable, high-risk actions have an approval path, verification is defined for recommended changes, and the report states explicit stopping and residual-risk conditions.
