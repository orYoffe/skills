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
