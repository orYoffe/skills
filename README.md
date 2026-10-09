# Skills

Use these skills to complete software tasks with less reading.
Start with a ticket. Use the stages that the task needs.
Keep decisions in the ticket, code, and conversation.

## Start here

Install the five ticket skills from your project directory:

```bash
npx skills add orYoffe/skills --skill execute-ticket clarify-ticket-behavior plan-ticket-change implement-review-ticket verify-ticket-change
```

The [skills CLI](https://github.com/vercel-labs/skills) needs Node.js and npm.
Select your agent when the CLI gives you that choice.
For manual installation, copy full skill folders into your agent's skills directory.
Keep `SKILL.md` and `agents/` together.
The agent needs access to the ticket and codebase.

Give the agent a task:

```text
Use $execute-ticket for this ticket: <task or link>.
```

Use your host's skill picker if its syntax differs.
A skill name alone does not load its instructions.
The coordinator reads each necessary skill.
If a skill is missing, the coordinator states that limit.

## Make it yours

Give preferences in the conversation. No configuration file is necessary.

| Desired work | Example request |
|---|---|
| Plan only | Investigate this ticket. Stop before code changes. |
| Human code review | Show me the diff. Wait for my review before testing. |
| Sequential questions | Give me one decision question at a time. |
| Behavior decisions | Help me define the behavior before implementation. |
| Verification only | Do the checks. Give defects without repairs. |
| Team method | Obey our project instructions and code review method. |

For implementation, the coordinator continues through the necessary stages.
It stops at your checkpoints and unresolved decisions.
For a direct stage request, that skill completes its stage and stops.
Small fixes need less planning. Existing work can start at code review or verification.
The workflow does not make extra documents necessary for each ticket.

Keep repeated preferences in existing project instructions or your skill copies.
Read the [workflow guide](docs/ticket-workflow.md) for changes and evaluation scenarios.

## Collection

| Ticket skill | Work |
|---|---|
| [`execute-ticket`](skills/execute-ticket/SKILL.md) | Select stages and use new results. |
| [`clarify-ticket-behavior`](skills/clarify-ticket-behavior/SKILL.md) | Find expected behavior and product choices. |
| [`plan-ticket-change`](skills/plan-ticket-change/SKILL.md) | Examine codebase effects and select an approach. |
| [`implement-review-ticket`](skills/implement-review-ticket/SKILL.md) | Write, simplify, and examine code. |
| [`verify-ticket-change`](skills/verify-ticket-change/SKILL.md) | Verify behavior and find failure causes. |

Install all five for full execution. You can also use each stage separately.
Each skill includes its necessary work rules.
These skills give instructions to an agent. They are not a background service.

## Routing and composition

Select one primary skill for a detailed examination:

| Request | Primary skill | Optional companion |
|---|---|---|
| Examine a diff, commit, or pull request | [`implement-review-ticket`](skills/implement-review-ticket/SKILL.md) | `agent-usage-review` for agent workflow effects |
| Examine prompts, tools, or agent traces | [`agent-usage-review`](skills/agent-usage-review/SKILL.md) | `implement-review-ticket` for resulting code |
| Improve a service | [`service-improvement`](skills/service-improvement/SKILL.md) | `implement-review-ticket` for the change |

For code review without repairs, give `implement-review-ticket` a review-only request.

Use the companion only for a separate necessary question.
Combine findings into one short result.
Detailed examination does not need a long report.

## Writing and checks

Use [ASD-STE100 writing rules](docs/writing-style.md) for English text.
Keep instructions short, precise, and complete.
Keep code identifiers and commands unchanged.

```bash
python -B scripts/validate_skills.py
python -B scripts/check_text.py
python -B -m unittest discover -s scripts -p 'test_*.py'
```

CI does these checks on pull requests and pushes to `main`.
Structure tests examine packaging, metadata, and links.
The text check finds long sentences, long paragraphs, and contractions in Markdown and skill metadata.
These checks do not prove agent behavior or full STE conformance.
Use the [evaluation scenarios](docs/ticket-workflow.md#evaluate-the-workflow) to examine agent behavior.
