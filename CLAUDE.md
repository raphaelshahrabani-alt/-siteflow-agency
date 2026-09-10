# Project memory

## Always use the humanizer skill

The `humanizer` skill lives in this repo at `.claude/skills/humanizer/SKILL.md`. Read it
before writing, do not work from memory of it. Version 3.0.0, MIT, based on Wikipedia's
"Signs of AI writing."

Two triggers make the skill mandatory.

First, any request to humanize. This includes "humanize this", "humanise", "make this
sound human", "make this sound like me", "de-AI this", "remove the AI tells", and any
wording that asks for the same thing in another language.

Second, any request to write or revise long-form prose. Essays, academic papers, reports,
research summaries, literature reviews, case studies, proposals, cover letters, personal
statements, articles, and blog posts all count. Draft the text first, then run the skill's
full four-step process over the draft, and return the rewritten version. Never return a
first draft.

### How to run it

Follow the skill's four steps in order: mark the tells strongest first, draft the rewrite,
check the draft, write the final version. The check in step 3 is not optional. Search the
final text for the five tells that survive rewrites most often: a not-X-but-Y contrast, a
one-line closer, a dash, a triad, a bold label.

Ask for a writing sample when the text should sound like a specific person. A sample
overrides the pattern list, including the rule against dashes.

### What to return

When asked to write something, return only the final text. That is the skill's embedded
mode. When given text to humanize, return the draft, the list of remaining patterns, and
the final version, which is the skill's default. Either way, say so if a needed fact is
missing instead of filling the gap.

When a file is named, rewrite prose only and write just the final text to the file. Leave
code blocks, inline code, commands, paths, YAML metadata, data, and link targets unchanged.

### Academic and factual writing

The skill's voice rule puts academic work in the neutral, plain register, so the writer's
opinions and asides that a blog post keeps do not belong here.

Four patterns do most of the work in academic text:

§13 inflated significance. Cut "marks a pivotal moment", "underscores its importance",
"reflects a broader", and any closing paragraph about the future. End on the last concrete
fact.

§17 borrowed authority. Never invent a source, a citation, a statistic, or an author. Cut
"experts argue" and "studies show" when no named source sits behind them. Name what the
real source said when there is one.

§23 knowledge-limit disclaimers and guesses. No "as of my last update", no "while specific
details are limited", and no plausible-sounding guess presented as a fact.

§12 overused AI words. Academic drafts fill up with crucial, key, robust, underscore,
highlight, delve, intricate, and landscape. Cut them.

Also apply §8 (no em or en dashes), §19 (no bold labels on list items), and §20 (sentence
case headings, no decoration, no rule between every section).

Requirements from the user about the source material still hold. Do not add a claim the
source does not support in order to make a sentence read better.
