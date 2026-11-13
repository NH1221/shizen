# Part 9: Twin Koi, "says he does jiu jitsu for inner peace"
7.8 s, 1080x1920. One shot, Flow-native from real frame f006 (crop P4-seated-back, 720x1280) plus the real Twin Koi print. Still: take 1 (13 Nov 08:25:46). Clip: Omni 1.1 Flash, 720p, true 8 s, 12 credits, 08:46:30. Raw master `incoming/2026-11-13/P9-clip-take1.mp4`, 2,969,585 bytes, sha256 170b142d... (matches Instinct's master).

## Frame review (raw, every 0.25 s; full-res checks at 0.5, 3.9 to 5.1 in 0.3 s steps, 7.9)
- Print: both koi and the SHIZEN mark hold steady in every frame; no redraw, no sleeve or front writing.
- Wearer: breathing and a small nod. From 4.0 to 5.1 s his right hand comes into view beside his elbow, fidgets and returns (motion-blurred, normal fingers, sleeve unchanged). Kept: it reads as a real fidget and lands under "tried to take my arm".
- Background: no grappling, no logos, no angle or room change. Focus-falloff mask (`pipeline/video/part9/dof-mask.png`: gblur 6, full above y 510, gone by y 640, his head kept sharp) applied: `incoming/2026-11-13/P9-clip-take1-dof.mp4`.

## Edit (`pipeline/video/part9/p9-v1.json`)
in 0.1 to 7.9, crop [660,1173,44,40] (removes the white mark at bottom-left), low-res pass, soft 0.8, text y 230: "says he does jiu jitsu / for inner peace" 0 to 3.28 s, "tried to take my arm / 4 times" 3.3 to 7.8 s. Sparta start 2.68: quiet 2.6 to 3.2 s, drop at about 3.35 s on the text switch.

## /ttevaluate: PASS 21/22
Standing rules all OK.
| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Hook | 1 | Strong print and setup line, but frame 1 is a calm seated shot with no pattern interrupt |
| 2 | Curiosity gap | 2 | "inner peace" set up, contradicted at 3.3 s |
| 3 | Voice | 2 | Reads like a training partner's complaint |
| 4 | Legibility | 2 | 2 lines each, 3.3 s and 4.5 s, top safe zone |
| 5 | Sound | 2 | Ambience, drop on the punchline; works muted |
| 6 | Pacing | 2 | Text switch 3.3 s, hand fidget 4.0 to 5.1 s, no flat stretch over 3 s |
| 7 | Length/loop | 2 | 7.8 s; still pose loops |
| 8 | Comment pull | 2 | Tag ask about the viewer's partner |
| 9 | Brand restraint | 2 | Product on the garment only |
| 11 | Cohesion | 2 | Calm koi back, "inner peace", then the arm line over the fidget |
| 10 | Honesty | 2 | No claims; AI label per Nic's decision |

## Posting
- File: `video-v1-post.mp4`, 8,781,183 bytes, sha256 eca7b29b..., H.264 1080x1920 + AAC.
- Caption: inner peace every roll 🐟 tag the guy who trains "for his mental health" #bjj #nogi #rashguard #nogibjj #bjjhumor
- Manual AI label OFF; Your brand / promotional disclosure ON; stop on any AI-related flag. TikTok first, then IG.
