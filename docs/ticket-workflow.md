# Use the ticket framework

[Start with installation](../README.md#start-in-two-steps) if the framework is not installed.

## Choose how to start

| Task | Request |
|---|---|
| Full execution | Use `$execute-ticket` for this ticket. |
| Find expected behavior | Use `$clarify-ticket-behavior`. Stop before planning. |
| Plan without edits | Use `$plan-ticket-change`. Stop before code changes. |
| Implement agreed behavior | Use `$implement-review-ticket` for the agreed change. |
| Code review only | Use `$implement-review-ticket`. Give findings without repairs. |
| Verify existing work | Use `$verify-ticket-change`. Give defects without repairs. |

For full execution, `execute-ticket` reads the necessary stage skills.
If a skill or source is unavailable, the agent gives that limit.

## Example: fix a discount bug

### Give the ticket and limits

```text
Use $execute-ticket to fix invalid discount acceptance.
Percentages from 0 to 100 are valid. Other percentages must raise ValueError.
Keep invoice behavior unchanged.
Show me the diff and wait for my review before testing.
```

### Examine the change

The agent examines the code and related tests. It makes the focused change and gives the diff.
It waits at the requested checkpoint.

```text
The range guard now rejects invalid percentages.
Invoice code and existing tests are unchanged.
Tests have not run. I am waiting for your review.
```

### Continue or adjust

```text
The diff looks correct. Continue with the relevant tests.
```

For changed requirements, give the new behavior instead.
The agent examines affected code and does the affected checks again.
You do not need to repeat the ticket.

## Set your preferences

| Preference | Example |
|---|---|
| Questions | Give me one decision question at a time. |
| Scope | Keep changes inside the checkout module. |
| Team method | Use our project instructions and security review method. |
| Test access | Use our integration environment. I will do device tests. |

Keep repeated preferences in existing project instructions.
No configuration file or ticket template is necessary.
For deeper changes, edit your skill copies and keep them in version control.
Updates can replace customized copies.

## Use test feedback

| Finding | Next stage |
|---|---|
| Clear code defect | Implementation and code review |
| Unsuitable approach | Planning |
| Changed or unclear expectation | Behavior |
| Environment or fixture failure | Verification and diagnosis |

The agent keeps decisions and results that still apply.
After repairs, it examines the diff and does affected checks again.
For tests that need your access, it gives actions and expected results.

## What belongs to this framework?

The framework contains the five skills in the [framework table](../README.md#framework-skills).
[Independent skills](independent-skills.md) have separate installation and usage.
They are not necessary for this workflow.
