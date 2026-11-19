# Community content-skill repos: audit and what was adapted (19 Nov 2026)
Cloned read-only (shallow) into a scratch folder; only Markdown and JSON rubrics were read. No installer or script was executed; nothing was installed into ~/.claude/skills; no accounts, keys or connections. All four are MIT-licensed; adapted ideas are paraphrased and credited below.

| Repo (commit) | What it is | Useful | Not useful / caution |
|---|---|---|---|
| github.com/vyralcontent/content-skills (349e495) MIT | 7 skills: short-form, TikTok, Reels, Shorts, hooks, ideas, captions. | formats.md (before/after "flash the after first, then rewind"; meme/relatable; "you're doing it wrong"; listicle); metrics-honesty.md ("pattern-matching, not prediction"; never invent videos or stats); idea-evaluation.md (hook-conception test, backup idea per slot, distill to hook/payoff/format/length). | Marketing for a paid product inside the skill; MrBeast/Galloway frameworks are anecdotal (C); fixed length bands assume talking-head creators. |
| github.com/hadi-a-azeez/viral-agent (2e550e6) MIT | 5 skills for animated explainer reels: find, script, voice, animate, check. | viral-check/rubric.json: six hook questions, esp. Q4 "Does the picture move in the first second?", Q3 "Would a stranger care?", Q5 "Does the hook open a question only the end closes?". Honest framing: "It can't predict views". | Scripts (check.py etc.) not run; animated-explainer pipeline does not fit real-footage AI video; Instagram-specific zones. |
| github.com/artemnovitckii/content-skills (1c6e909) MIT | storytelling, viral-hooks, voice, dumbify, anti-AI-writing. | storytelling: beats joined by BUT or THEREFORE, never "and then"; write the last line first; last line should loop into the hook; "Never fabricate biography". | Long-form/talking-head focus; examples are business stories. |
| github.com/Ootto-AI/claude-content-skills (691875a) MIT | ~60 short prompt skills for social. | series-planner: a named recurring series must state a "follow reason" or it is weak; comment-mining. | Most are thin prompt templates; install.sh copies into ~/.claude/skills (not run); vendor ads in every file; "virality" skill's winners/flops are their own unverified anecdotes. |

## Adapted into format-lab (paraphrased)
1. Frame-0 motion gate (hadi Q4): something visibly moves in the first second, and the picture shows what the words say. All our posts since 9 Nov opened on a near-still back.
2. Stranger test (hadi Q3): a non-BJJ-follower and a non-follower of Shizen must get it in frame 1.
3. Open loop closed only at the end (hadi Q5, vyral idea test): the payoff is in the last second, and the hook cannot be understood without it.
4. BUT/THEREFORE beats and end-first writing (artem): each text beat turns the previous one; the last line hands back into the first for the loop.
5. No fabricated biography (artem): no first-person "I/me" stories presented as the account's real life. Fictional characters in third person only.
6. Backup per slot (vyral): every planned post names a backup concept that fits the same base and the remaining submits, so a failed take is never posted to fill a day.
7. Series follow-reason (Ootto): a recurring series is only worth naming if missing an episode would bother someone.
8. Honesty doctrine (vyral, hadi): plans state patterns and hypotheses, never predicted views; never invent example videos or numbers.
