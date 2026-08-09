---
name: service-improvement
description: Assess or improve a running, planned, or production software service across performance, reliability, structure, contracts, security, observability, deployability, resilience, operability, testing, dependency risk, and maintainability. Use for service diagnosis and operational improvement; use code-review for an isolated diff and agent-usage-review for agent orchestration.
---

# Service Improvement

## Purpose

Assess a software service as a socio-technical system, then improve the highest-value risks with evidence. Fit recommendations to the repository, runtime, workload, operating model, and user-facing objectives. Stay framework-agnostic until the discovered service makes a framework-specific choice relevant.

Do not call a change an improvement without a baseline, a causal hypothesis, a bounded change, and post-change verification. Do not invent measurements, SLOs, architecture, ownership, incidents, or user impact; label them `unknown` and state how to obtain them.

## Operating rules

- Preserve the existing project’s conventions, compatibility promises, deployment model, and security boundaries.
- Start read-only. Modify code only when the current user request explicitly authorizes implementation; keep each change small and independently reversible.
- Prefer production-safe evidence: read-only queries, existing dashboards, traces, logs, profilers, tests, static analysis, dependency metadata, and staging/load-test results. Redact secrets and personal data.
- Separate facts, inferences, hypotheses, and recommendations. Tie every material finding to a file, symbol, query, metric, trace, log pattern, test, incident, or documented assumption.
- Optimize for user-visible outcomes and SLOs, not isolated CPU, memory, latency, or code-style scores.
- Never trade security, correctness, durability, or reliability for speed without explicitly documenting the tradeoff and approval boundary.
- Stop or narrow the work when evidence is insufficient, production access is risky, a migration is irreversible, or the requested change exceeds scope.

## Workflow

### 1. Establish scope and safety

Record the service name, repository and revision, environments, user journeys or consumers in scope, requested outcome, constraints, change window, and whether implementation is authorized. Identify prohibited actions such as production writes, destructive migrations, secret access, or load generation against live traffic.

Define a review horizon:

- **Snapshot review:** repository and configuration only; state runtime unknowns.
- **Operational review:** include dashboards, incidents, traces, logs, deploy history, and dependency health.
- **Improvement implementation:** make only approved changes, with a rollback path and verification evidence.

Classify service maturity as `design/greenfield`, `pre-production`, or `production`. For `design/greenfield`, do not invent runtime measurements, owners, SLOs, incidents, or topology. Use `N/A` when a surface is genuinely outside the service or maturity stage, `unknown` when the evidence should exist but was not obtained, and `gap` when a required control is absent. Give a reason for `N/A`; do not require an owner or action for a truly non-applicable area.

### 2. Discover service topology and context

Build a compact context map before evaluating components. Inspect, as applicable:

- entry points, protocols, routes, authentication, authorization, and public versus internal surfaces;
- synchronous and asynchronous flows, queues, schedulers, workers, caches, databases, object stores, third-party APIs, and control-plane dependencies;
- deployment units, regions/zones, replicas, autoscaling, configuration, feature flags, secrets, certificates, and runtime limits;
- data entities, ownership, consistency requirements, retention, migrations, backups, restore procedures, and contract/version boundaries;
- build/test/release pipelines, environments, on-call ownership, runbooks, alert routes, incident history, and change history.

Use repository search and manifests first. Then validate the map against runtime evidence or documentation. Mark each edge as `confirmed`, `inferred`, or `unknown`, and call out single points of failure, shared dependencies, fan-out, bottlenecks, and blast-radius boundaries.

### 3. Define workload, user impact, and SLO thinking

Describe the workload by traffic shape and failure sensitivity:

- request, event, batch, or mixed workload;
- steady state, peaks, bursts, seasonality, concurrency, payload sizes, hot keys, retries, and fan-out;
- read/write mix, synchronous latency budget, freshness, throughput, ordering, duplicate tolerance, and data-loss tolerance;
- critical user journeys and acceptable degradation or graceful fallback.

Find existing SLIs/SLOs, SLAs, error budgets, capacity limits, and alert thresholds. If absent, propose provisional indicators rather than claiming targets. Prefer user-facing availability and latency distributions such as p50/p95/p99, correctness/freshness, queue age, and recovery time. Distinguish:

- **SLI:** the measured service behavior;
- **SLO:** the target over a stated window and population;
- **SLA:** an external commitment with consequences;
- **error budget:** the allowed unreliability implied by the SLO.

Check that alerts represent user impact or imminent SLO risk, that burn-rate or equivalent early-warning logic exists where appropriate, and that excluded traffic and error classification are explicit.

### 4. Establish a baseline before changing anything

Capture timestamp, revision, environment, workload, sample window, measurement method, and confidence for every baseline. At minimum seek:

- request volume, concurrency, success/error rate by class, p50/p95/p99 latency, saturation, and resource utilization;
- dependency latency/error/timeout/retry rates, queue depth and age, cache hit/miss behavior, database query latency/locks/connections, and storage/network limits;
- deployment frequency, change failure rate, rollback/restore time, incident frequency, alert noise, toil, and recovery evidence;
- test coverage that matters to behavior, flaky tests, build duration, vulnerability/dependency findings, and unsupported runtime versions.

If a measurement cannot be collected, write `not measured`, explain why, and give the lowest-risk collection method. Do not use averages to hide tail latency, aggregate errors to hide a failing route, or lab results as production proof.

### 5. Diagnose bottlenecks and failure modes

Form a ranked hypothesis list. Trace a representative request or work item end to end, then correlate service signals with dependency and deploy timelines. For each suspected bottleneck, identify the limiting resource, queue or critical path, saturation point, and causal evidence. Distinguish capacity limits from coordination, algorithmic, I/O, lock, serialization, network, dependency, and retry-amplification problems.

Use profiling, query plans, flame graphs, traces, load tests, fault injection, or controlled experiments only when safe and representative. Avoid speculative rewrites, premature caching, unbounded concurrency, or tuning a component without checking its neighbors and failure behavior.

### 6. Review the service across all dimensions

Use the following checklist; mark each area `healthy`, `risk`, `gap`, or `N/A`, with evidence and an owner/action unless it is `N/A`.

| Dimension | Inspect for | Common anti-patterns |
| --- | --- | --- |
| Performance and capacity | tail latency, critical path, algorithmic complexity, allocations, I/O, query plans, batching, caching, concurrency, quotas, load shedding, capacity headroom | optimizing averages, N+1 calls, unbounded fan-out, unbounded queues, synchronous work on request paths, retries multiplying load |
| Reliability and SLOs | user-facing SLIs, error budget, dependency budget, graceful degradation, idempotency, correctness, recovery objectives | alerts on host symptoms only, hidden errors, false-success responses, no budget policy, assuming redundancy equals recovery |
| Code structure | boundaries, cohesion, coupling, ownership, dependency direction, error handling, configuration, test seams | god modules, circular dependencies, duplicated policy, global mutable state, business logic in adapters, catch-and-ignore errors |
| API and data contracts | schemas, validation, authz, compatibility, pagination, idempotency, timeouts, versioning, events, replay, consistency, migrations | implicit contracts, breaking changes, mass assignment, ambiguous nulls, unbounded payloads, dual writes without reconciliation |
| Security and privacy | threat model, authn/authz, tenant isolation, input/output handling, secrets, SSRF, sensitive logging, crypto, supply chain, auditability | trusting client ownership, overly broad service accounts, secrets in config/logs, unsafe deserialization, missing rate limits, unreviewed third-party APIs |
| Observability | structured logs, metrics, traces, correlation, semantic names, cardinality, dashboards, SLO alerts, runbooks, signal retention | high-cardinality labels, logs without context, PII in telemetry, alerts without action, missing trace propagation, dashboards without user SLIs |
| Deployability and change safety | reproducible artifacts, CI gates, migrations, config separation, canary/blue-green, feature flags, health checks, rollback and roll-forward | manual releases, big-bang changes, irreversible migrations, untested rollback, flags that never expire, startup probes used as readiness |
| Resilience and recovery | timeouts, bounded retries with jitter, circuit/bulkhead isolation, backpressure, failover, backups, restore tests, chaos/game days, RTO/RPO | retry storms, cascading failure, shared pools, fail-open security, backup-only recovery plans, untested failover |
| Operability | ownership, on-call load, runbooks, safe diagnostics, capacity forecasts, toil, incident and postmortem actions | tribal knowledge, noisy alerts, manual repetitive repair, no escalation path, runbooks that cannot be executed |
| Testing and verification | unit/component/contract/integration/e2e tests, property and load tests, failure paths, migration tests, security checks, determinism | only happy-path tests, flaky suites tolerated, production-only discovery, tests coupled to implementation, no performance regression gate |
| Dependency risk | direct/transitive dependencies, versions, licenses, CVEs, maintenance, support windows, API quotas, failure modes, exit strategy | unpinned builds, abandoned packages, one-provider dependency, unlimited vendor retries, no inventory or upgrade path |
| Maintainability | readability, documentation, invariants, ownership, complexity, safe defaults, deletion of obsolete paths, cost and toil | clever abstractions, stale docs, permanent compatibility shims, dead flags, duplicated configuration, no feedback loop |

For security findings, use risk-based verification and current authoritative guidance; do not infer safety from a clean linter or dependency scanner alone.

For security, dependency, and release evidence, look for the applicable combination of lockfiles or pinned inputs, dependency/advisory results, secret scanning, SBOM, build provenance or attestation, signed immutable artifacts, and CI policy results. Record each artifact as present, absent, or `N/A` with the exact command, workflow result, or source. Do not call supply-chain risk assessed when these inputs were not checked.

### 7. Prioritize findings

Score each finding with explicit reasoning:

- **Severity:** `P0` active catastrophic user, security, data, or recovery risk; `P1` material outage, data-integrity, security, or SLO risk; `P2` meaningful degradation, recurring toil, capacity, maintainability, or future risk; `P3` low-risk hygiene or optional improvement.
- **Urgency:** time to impact, exploitability, error-budget burn, upcoming load/change, and detectability.
- **Confidence:** `high`, `medium`, or `low`, based on direct evidence and reproducibility.
- **Effort and reversibility:** smallest safe change, blast radius, migration complexity, and rollback difficulty.

Recommend an ordered backlog using `impact × confidence ÷ effort`, adjusted for security, correctness, and irreversibility. Group related work only when it can be tested and rolled back as a unit. Treat P0/P1 security or data risks as escalation items, not optimization backlog.

### 8. Design and implement improvements safely

For each approved change, write a hypothesis in the form: “If we change **X**, then **Y** will improve for **Z** workload because **evidence**.” Define:

1. smallest change and affected components;
2. pre-change checks and invariants;
3. risk, blast radius, dependencies, and resource/cost impact;
4. rollout controls: flag, canary, shadow, rate limit, migration phase, or staged traffic where useful;
5. exact rollback or roll-forward procedure, including data and configuration consequences;
6. for a canary, the population, control comparison, minimum sample or observation window, absolute SLO guardrails, abort authority, and rollback decision;
7. success, guardrail, and abort thresholds;
8. owner, observation window, and cleanup of temporary flags or instrumentation.

Prefer additive, backward-compatible, independently deployable steps. For schema changes, use expand–migrate–contract or an equivalent compatibility strategy; verify reads, writes, rollback behavior, and reconciliation before removing old paths. Keep timeouts, retries, queue sizes, concurrency, and resource limits bounded and observable.

### 9. Verify and close the loop

Run the narrowest useful checks first, then broaden as risk requires: formatter/linter, type/static analysis, unit and component tests, contract and migration tests, security/dependency checks, representative load or benchmark tests, fault/recovery tests, deployment dry runs, and post-deploy telemetry comparison. Re-measure the same baseline dimensions under a comparable workload.

Do not claim causality from an uncontrolled before/after comparison. Explain confounders, sample size/window, statistical or operational uncertainty, and whether the change met its guardrails. Revert, disable, or stop rollout when an abort threshold is crossed. Record residual risk and a follow-up measurement if verification is incomplete.

## Common anti-patterns to flag

- “Make it faster” without a user journey, workload, baseline, or target.
- Treating CPU, memory, uptime, or test coverage as a proxy for service quality.
- Changing multiple coupled variables so no causal conclusion is possible.
- Adding retries, caching, concurrency, or replicas without budgets, invalidation, isolation, or backpressure.
- Relying on timeouts alone without cancellation, idempotency, and bounded work.
- Deploying code and incompatible data changes together with no rollback plan.
- Using logs as an unstructured database, emitting secrets/PII, or putting unbounded identifiers in metric labels.
- Treating “no alerts” as health when telemetry, ownership, or alert coverage is missing.
- Recommending a rewrite, new platform, or new dependency before proving the bottleneck and migration economics.
- Closing a finding because a scanner is clean while correctness, abuse cases, authorization, recovery, or operational behavior remain untested.

## Exact output format

Return the following sections in this order. Keep the headings and field names stable so the report can be compared over time. Replace every placeholder. When a section has no entries, write `None`; use `unknown`, `not measured`, or `N/A` only with the semantics defined above.

```markdown
# Service Improvement Report

## 1. Executive summary
- Service / revision:
- Scope and authorization:
- Overall assessment: [healthy | needs targeted improvement | high risk | blocked by missing evidence]
- Top three actions:

## 2. Context and topology
- User journeys / consumers:
- Environments and deployment units:
- Request or work-item path:
- Dependencies and data stores:
- Confirmed / inferred / unknown edges:
- Ownership and operational context:

## 3. Workload and objectives
- Workload shape and assumptions:
- Existing or provisional SLIs/SLOs/SLAs:
- Error budget / capacity constraints:
- Critical degradation and recovery expectations:

## 4. Baseline evidence
| Signal | Value and window | Source / command | Confidence | Gap |
|---|---|---|---|---|

## 5. Findings
For each finding:
### [ID] [P0–P3] Short title
- Dimension:
- Status: [healthy | risk | gap | N/A]
- Evidence:
- User / business / operational impact:
- Root cause or hypothesis:
- Confidence:
- Recommendation:
- Smallest safe change:
- Risk and blast radius:
- Rollback / abort plan:
- Verification and success guardrails:

## 6. Prioritized improvement plan
| Rank | Finding IDs | Change | Impact | Confidence | Effort | Reversibility | Owner / next step |
|---|---|---|---|---|---|---|---|

## 7. Verification record
- Checks run and results:
- Before/after comparison:
- Production or staging observation window:
- Regressions, confounders, and residual risk:
- Rollback exercised or remaining gap:

## 8. Files, commands, and sources
- Files or runtime artifacts inspected:
- Commands, queries, dashboards, traces, or tests used:
- Authoritative references consulted:
| Source | URL | Version / publication date | Consulted date | Relevant section / principle | Project-specific adaptation |
|---|---|---|---|---|---|
- Changed files (if implementation was authorized):

## 9. Decision and follow-up
- Decision: [proceed | stage | stop | rollback | needs owner input]
- Explicit assumptions:
- Open questions / missing evidence:
- Follow-up owner and date:
```

Never omit a section. If no implementation was authorized, put proposed changes in the plan and leave changed files empty. A canary or rollout is not verified without comparable control evidence, a sufficient observation window, an explicit abort authority, and a recorded rollback decision.

## Authoritative references

Consult the current versions when the review touches these areas; use them as principles, not as a substitute for service-specific evidence:

- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/): SLOs, monitoring, alerting, toil, load management, incident response, configuration, and canarying.
- [Google SRE monitoring](https://sre.google/workbook/monitoring/): monitoring for alerting, diagnosis, visualization, and capacity planning.
- [Google SRE canarying releases](https://sre.google/workbook/canarying-releases/): reproducible/automated builds and tests, small changes, staged rollout, and rollback evaluation.
- [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/): consistent names and attributes across traces, metrics, logs, profiles, and resources.
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x04-release-notes/): API authorization, resource consumption, SSRF, inventory, misconfiguration, and unsafe API consumption risks.
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/): verifiable application security controls; use the current released version.
- [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final): secure development practices and vulnerability-risk reduction across the SDLC.
- [AWS Well-Architected Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html): foundations, change management, fault isolation, recovery, backups, and resilience testing.

For every source used in a report, record its URL, version or publication date, consulted date, relevant section or principle, and the project-specific adaptation. If a source cannot be dated or retrieved, mark that limitation as `unknown`.

When a source is vendor-specific, translate its principle into the project’s platform and record that adaptation in the report.
