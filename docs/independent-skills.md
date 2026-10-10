# Independent skills

These tools are separate from the [ticket framework](../README.md).
They are not workflow stages or required companions.
Install and use each tool only for its own task.
These examples use Codex syntax. See [agent setup](ticket-workflow.md#agent-setup) for other agent commands.

## Examine an agent workflow

[`agent-usage-review`](../skills/agent-usage-review/SKILL.md) examines how agents use prompts, context, tools, permissions, and test results.
Use it for repeated work, weak verification, unsafe tool actions, or unclear handoffs.
It starts read-only and gives supported findings.

### Install

```bash
npx skills add orYoffe/skills \
  --skill agent-usage-review
```

### Use

```text
Use $agent-usage-review to examine
these agent traces and prompts.
Find repeated work and weak
verification. Give findings without
repairs.
```

## Examine a software service

[`service-improvement`](../skills/service-improvement/SKILL.md) examines service performance, reliability, security, contracts, operations, and recovery.
Use it to find causes from code, configuration, runtime records, and measurements.
It starts read-only. Code changes need permission within the task.

### Install

```bash
npx skills add orYoffe/skills \
  --skill service-improvement
```

### Use

```text
Use $service-improvement to examine
this service's slow responses.
Compare code paths and available
measurements. Give findings without
code changes.
```

## Keep the tasks separate

These skills can produce findings that later become tickets.
Use the ticket framework for implementation of those tickets.
Neither tool is part of the framework's default execution or installation.
