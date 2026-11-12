# Part 8: Hebi, "she said it was a flow roll"
5.8 s, 1080x1920. One shot, Flow-native from real frame f004 (crop P6-seated-back) plus the real Hebi print. Still: Flow image mode take 3 (12 Nov 08:24, 0 credits). Clip: P8-clip-take1 (Omni 1.1 Flash, 720p, the highest free option; 6 s; 08:44:30). Raw master kept at `incoming/2026-11-12/P8-clip-take1.mp4`.

## Frame review (raw clip, every 0.25 s plus full-res checks at 0.5, 2.5, 4.5, 5.9)
- Print: stable in every frame, no redraw, no sleeve or front writing. SHIZEN mark steady.
- Wearer: arms and hands still; breathing plus a slow head turn left (1.75 to 3.75 s) showing a natural profile. No warping.
- Background: people stay in place with small movements, no grappling, no logos, no late room or angle change. Some far faces sit close to the original reel people, so the focus-falloff mask (`pipeline/video/part8/dof-mask.png`, gblur 6, hard above y 480, fading out by y 620, her head kept sharp) is applied: `incoming/2026-11-12/P8-clip-take1-dof.mp4`.

## Edit (`pipeline/video/part8/p8-v1.json`)
in 0.1 to 5.9, crop [680,1209,20,40], low-res pass 432x768 then up, soft 0.8, text y 230 over the blurred background: "she said it was / a flow roll" 0 to 2.48 s, "the snake had / other plans" 2.5 to 5.8 s. Sparta bed start 3.43: loudness dips 2.0 to 2.3 s and the drop lands at about 2.6 s, on the text switch and mid head turn.

## /ttevaluate: PASS 20/22
Standing rules: all OK (native TikTok Sans text, creator voice, no end card, no zooms, passes as phone video, one story).
| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Hook | 2 | Frame 1 shows the snake print plus "she said it was a flow roll", an open loop |
| 2 | Curiosity gap | 1 | Payoff is a pun, not a reveal |
| 3 | Voice | 2 | Reads like a grappler's comment |
| 4 | Legibility | 2 | 2 lines, 2.5 s and 3.3 s, top safe zone |
| 5 | Sound | 2 | Gym ambience plus drop on the punchline; works muted |
| 6 | Pacing | 2 | Head turn 1.75 to 3.75 s, text switch at 2.5 s |
| 7 | Length/loop | 1 | 5.8 s, under 7 s; still pose loops cleanly |
| 8 | Comment pull | 2 | Tag ask about the viewer's gym |
| 9 | Brand restraint | 2 | Product on the garment only |
| 11 | Cohesion | 2 | Calm after "a flow roll", snake print pays off "the snake" |
| 10 | Honesty | 2 | No claims; AI label per Nic's standing decision |

## Posting
- File: `video-v1-post.mp4`, 6,547,612 bytes, sha256 5c39b378..., H.264 1080x1920 + AAC.
- Caption (TikTok and IG): she said it was a flow roll 🐍 the snake had other plans. tag the girl who lies about flow rolls #bjj #nogi #rashguard #womensbjj #bjjhumor
- Manual AI label OFF (Nic, 11 Nov 14:02:56). Keep the Your brand / promotional disclosure. Stop on any AI-related flag.
- TikTok first, then IG. Send Nic both links.
