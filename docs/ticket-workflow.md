# Ticket workflow

## Start small

Try one stage on a real ticket.
A planning-only request permits investigation without code changes.
A verification-only request permits checks without repairs.
Use the coordinator when you want full execution.

The input can be a task, an accessible ticket link, or code with feedback.
No ticket template is necessary.
If a link is inaccessible, give the agent the relevant text.
Use existing domain documents and project terms.

## Set preferences

| Preference | Default | Example change |
|---|---|---|
| Scope | Task and necessary related changes | Keep changes in the checkout module. |
| Stop | Complete the requested work | Stop after planning. |
| Checkpoints | Continue through routine stages | Wait for my diff review before testing. |
| Questions | Unresolved decisions only | Give one question at a time. |
| Code review | Examine the diff and affected contracts | Use our security review method. |
| Verification | Required checks and useful tests | Use our integration environment. |

State these preferences in the conversation.
For repeated use, add them to existing project instructions.
Do not create a new rules file for each ticket.
User preferences still obey the host's instruction rules.
A preference cannot turn a missing test result into a pass.

For larger changes, edit your skill copies:

| Skill | Change here |
|---|---|
| Coordinator | Stage selection, checkpoints, completion |
| Behavior | Questions and acceptance examples |
| Planning | Codebase effects and approach |
| Implementation | Code changes and code review |
| Verification | Tests and failure diagnosis |

Keep shared rules consistent across all five skills.
Updates can replace customized copies. Keep local changes in version control.
Keep team preferences in project instructions when possible.

## Handle new findings

Find the cause of a failure before changing code.
For a clear code defect, return to implementation.
For an unsuitable structure, return to planning.
For changed or unresolved requirements, return to behavior.
For fixture or environment failures, find the cause in verification.

Current behavior can differ from requested behavior. That difference alone does not require a user decision.
After a change, examine the affected diff again.
Do checks again when their results no longer apply.
Keep decisions and results that still apply.

After a pause, read the conversation and current sources.
Private agent context can become unavailable.
Give questions only for missing decisions that affect the work.

## Evaluate the workflow

Use an isolated fixture or an authorized real task.
Keep the prompt, actions, diff, test results, and completion claim in the evaluation context.
Production tickets do not need evaluation documents.

| Scenario | Expected action |
|---|---|
| Clear small bug | Make a focused repair without unnecessary questions. Do useful checks. |
| Unclear behavior | Find available facts. Give a decision question and recommendation. Wait before dependent edits. |
| Planning only | Give an approach. Stop without code changes. |
| Human checkpoint | Stop at the requested point. Wait for the user's response. |
| Failed verification | Find the cause. Repair with permission. Examine the diff. Repeat affected checks on the current code. |
| Changed shared behavior | Find expectations and effects before edits. Keep unrelated correct work. |
| Verification only | Do checks. Give defects without repairs. |
| Missing access or skill | State the limit. Do not invent results or skill use. |

Compare actions with task limits and expected behavior.
A successful trial gives proof for that trial only.
Do relevant trials again after instruction changes.
Use different tasks before making general claims about the workflow.

## Sources of ideas

[Matt Pocock's grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) pairs questions with recommendations.
It keeps dependent decisions in sequence.
[Grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) also connects questions to domain terms.
This workflow uses existing documents. It does not make new domain documents necessary.

[Addy Osmani's agent skills](https://github.com/addyosmani/agent-skills) support interviews, small changes with complete behavior, and code simplification.
This workflow uses those ideas with optional checkpoints and short results.
It keeps behavior unchanged during simplification unless a behavior change is necessary for the task.
