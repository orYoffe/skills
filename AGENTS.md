# Repository instructions

Read [the writing rules](docs/writing-style.md) before English text changes.
Use ASD-STE100 rules and consistent software terms.
Keep text precise, complete, and short.
Keep skill names, paths, commands, and behavior unchanged unless changes are necessary for the task.

Keep instructions in each skill usable without this repository.
Do not make task documents mandatory or long report templates.
Obey direct stage requests and user checkpoints.
Continue full execution within the user's permission.

After changes, do the relevant repository checks:

```bash
python -B scripts/validate_skills.py
python -B scripts/check_text.py
python -B -m unittest discover -s scripts -p 'test_*.py'
```

For changed workflow behavior, do relevant agent trials again.
Keep evaluation context separate from production ticket requirements.
Give packaging results, agent trials, and writing limits separately.
Do not claim full STE conformance from the text check.

## Evaluate workflow changes

Use isolated fixtures or authorized real tasks.
Keep prompts, actions, diffs, results, and completion claims in the evaluation context.
Do not make evaluation documents necessary for production tickets.

| Scenario | Expected action |
|---|---|
| Clear small bug | Make a focused repair. Do useful checks. |
| Unclear behavior | Find available facts. Give a decision question and recommendation. Wait before dependent edits. |
| Planning only | Give an approach. Stop without code changes. |
| Human checkpoint | Stop at the requested point. Wait for the user's response. |
| Failed verification | Find the cause. Repair with permission. Examine the diff. Do affected checks again. |
| Changed shared behavior | Find expectations and effects before edits. Keep unrelated correct work. |
| Verification only | Do checks. Give defects without repairs. |
| Missing access or skill | Give the limit. Do not invent results or skill use. |

A successful trial gives proof for that trial only.
Use different tasks before making general claims.

## Sources of ideas

[Matt Pocock's grilling](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) pairs questions with recommendations.
[Grill-with-docs](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md) connects decisions to domain terms.
[Addy Osmani's agent skills](https://github.com/addyosmani/agent-skills) support interviews, small complete changes, and code simplification.
Use these ideas with existing documents, optional checkpoints, and short results.
