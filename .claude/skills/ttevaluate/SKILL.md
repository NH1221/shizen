---
name: ttevaluate
description: Hostile review of a TikTok cut before anyone else sees it. Scores hook, script, captions, edit, ending, loop and sound against researched short-form patterns and Nic's standing feedback, then returns PASS or FAIL with exact fixes. Run on every edit attempt.
---

# /ttevaluate

Judge the cut as a slop-allergic 18-35 BJJ guy scrolling at speed would. Look for reasons to reject it. A cut ships only on PASS.

## Inputs

The video file. If it can't be watched directly, extract frames every 0.5 s plus the first and last frame with ffmpeg and read them. Measure audio loudness with `ebur128`. Also read the caption, hashtags and pinned comment.

## Standing rules from Nic (an automatic FAIL if broken)

1. **Captions look native.** Use the TikTok text-tool style: TikTok Sans or Proxima Nova semibold, white, no background box, only a soft shadow or a thin dark outline. No serif fonts, no brand fonts, no ad-style lower thirds.
2. **The script sounds like a real creator, not an ad.** Use first-person or POV phrasing, the way people actually talk on BJJ TikTok (lowercase is fine, "pov:", "ngl"). Never use a narrator voice, slogans, a spoken brand name, or a "drop" announcement in the video.
3. **No promotional end card and no product-only shots.** The real-looking footage carries the video. The brand lives on the garment and in the caption or pinned comment.
4. **No unmotivated moves.** No zooms, pushes or effects without an in-world reason (a camera person moving counts as a reason).
5. **The footage must pass as unedited phone video.** No warped hands, faces, drifting prints, fake light or smooth gimbal moves.
6. **The narrative is cohesive.** The text beats, the picture at that moment and the post caption tell ONE story: each line follows from the last and lands on what the viewer is seeing right then. Nic's example of a fail: "it's better for sure as it's not natural the V2, but the caption narrative isn't really cohesive."

## Scored checks (0 to 2 each)

| # | Check | 2 = | Source pattern |
| --- | --- | --- | --- |
| 1 | Hook at 0 to 1.3 s | Frame 1 plus text gives a reason to stay, with no ad smell | Viewers decide in about 1.3 s; hook = pattern interrupt + open loop |
| 2 | Curiosity gap | A question is opened early and paid off late; the payoff is real | Loewenstein information gap; never false curiosity |
| 3 | Script voice | Reads like a comment a grappler would write | Native POV and meme formats beat ads |
| 4 | Text legibility | Max 2 lines, 1.5 s+ per line, inside the safe zone (clear of the right-hand buttons and the bottom ~30%) | TikTok safe-zone specs |
| 5 | Sound | Real or plausible audio that matches the picture; sound adds, but the video works muted | 88% say sound is essential; design to survive sound-off |
| 6 | Pacing | No dead stretch over 3 s without something new | Retention drops at flat spots |
| 7 | Length and loop | 7 to 15 s; the last frame flows into the first | Completion and rewatch are the top ranking signals |
| 8 | Comment pull | The caption or pinned comment asks about the viewer's life, not a favour for the brand | Metricool: questions +26% comments; asking for likes -60% |
| 9 | Brand restraint | The product is visible and desirable but never pitched | Brand imagery up front raises skipping (Teixeira) |
| 11 | Cohesion | Read the text beats and the caption aloud in order: they make one joke or story, with no pivot to an unrelated line | Nic's standing feedback |
| 10 | Honesty | No false claims, no fake urgency, AI-label decision flagged for Nic | Platform rules |

## Verdict

- **PASS:** no standing-rule breach, a total of 18/22 or more, and no check scoring 0.
- Otherwise **FAIL**. List every fix as an exact instruction (timestamp, what changes, to what). Re-run after each fix.

## Output format

1. Verdict line.
2. Standing rules: OK or the breach.
3. A score table with one-line evidence per check (timestamped).
4. The fix list, ordered by impact.
