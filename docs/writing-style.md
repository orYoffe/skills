# English writing rules

Use [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) for English text in this repository.
The goal is precise text that decreases the user's mental effort.
The standard includes writing rules and a controlled dictionary.
Short sentences alone do not prove conformance.

## Write and examine text

1. Use approved words with their approved meanings and parts of speech.
2. Use necessary technical nouns and technical verbs with consistent meanings.
3. Use the same term for the same concept.
4. Write instructions in the imperative.
5. Give one instruction per sentence.
6. Use the active voice.
7. Put a necessary condition before its instruction.
8. Use explicit nouns when a pronoun can cause confusion.
9. Do not use contractions.
10. Keep paragraphs on one topic.

STE permits 20 words in a procedural sentence and 25 in a descriptive sentence.
This repository uses a stricter 20-word target for English prose.
Keep paragraphs within six sentences.
Keep noun groups short. Explain necessary technical terms.
Use American spelling.

For general instructions, prefer `examine` to `check` as a verb.
Prefer `make sure` to `verify` outside its software meaning.
Prefer `do` to `perform` when the meaning stays precise.
Do not replace a precise term with a shorter word that changes its meaning.

Keep commands, paths, identifiers, and quoted source text unchanged.
For user text in another language, respect the requested language.
Do not use STE as a reason to change behavior or technical contracts.
Do not copy the standard or its dictionary into this repository.

## Software terms

These terms have one meaning in this collection:

| Term | Meaning |
|---|---|
| Ticket | The requested software task. |
| Stage | One part of the ticket workflow. |
| Coordinator | The skill that selects stages and uses new results. |
| Checkpoint | A point where the agent waits for the user. |
| Codebase | The project's code and related files. |
| Diff | The code changes under examination. |
| Contract | Behavior that other code or users depend on. |
| Fixture | Controlled input or setup for a test. |
| Verification | Comparison of actual results with expected behavior. |
| Verify | Make that software comparison. |
| Implementation | The code changes needed for the task. |
| Refactor | Change code structure while keeping behavior unchanged. |
| Code review | Examination of code for defects and codebase fit. |
| Regression | Previously correct behavior that a change breaks. |
| Runtime | The environment in which code executes. |
| Agent trace | The recorded actions and results of an agent. |
| Baseline | Results from the version before a change. |
| Latency | Time between a request and its result. |
| Throughput | Completed work per unit of time. |

Keep established domain terms in service and security work.
Explain an unfamiliar abbreviation at first use.
Use a new technical term only when it gives a necessary, precise software meaning.

## Check limits

`python -B scripts/check_text.py` examines Markdown prose and skill metadata.
It finds sentences above 20 words and common contractions.
It ignores headings, code fences, inline code contents, and link destinations.
It treats each inline code span as one word.
It examines table cells separately and joins wrapped paragraph lines.
It also examines skill descriptions and default prompts.

The check does not examine word meanings, grammar, active voice, or every STE rule.
It does not examine Python source or workflow syntax.
Examine comments, messages, and docstrings during code review.
Use the dictionary and human judgment for a full conformance examination.
Do not describe a check pass as STE certification.

Read the official [FAQ](https://www.asd-ste100.org/STE_faq.html) and [tool guidance](https://www.asd-ste100.org/STEsoftware.html) for further limits.
