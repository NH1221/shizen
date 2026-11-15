# Part 10: Ryu, "coach banned his rash guard from class"
5.6 s, 1080x1920. One shot from a real frame (Coastal Jiu Jitsu 34:10, cropped in code to `incoming/2026-11-15/src/P10-coastal-crop.png`) plus the real Ryu print. Still P10-v1 (both people fully replaced, face check passed). Clip P10-clip-v1: Omni 1.1 Flash, 720p, 6 s, raw master `incoming/2026-11-15/P10-clip-v1.mp4`.

## Clip review (every 0.25 s; full-res at 0.0, 0.3, 1.0, 2.0, 2.5, 3.5, 3.8, 4.1, 4.2, 4.5, 4.6, 5.9)
- Camera locked, no cuts or zoom. Lead still, arms and hands unmoving, small breathing and head movement. Coach keeps arms crossed, lowers his eyes and gives a tight-lipped, exasperated pout around 3.8 to 4.6 s (reads human; no smile).
- Dragon stable in every frame, no redraw. Faces and clothes consistent. Feet correct. Audio ambient only (about -42 LUFS), no words or music detected.
- One fault: the small SHIZEN wordmark is redrawn as garbled letters ("SIIIZEW") from frame 0 (small text at 720p). The yin-yang mark is fine. Fix: a soft local blur on the wordmark only (`pipeline/video/part10/mark-soft-mask.png`, gblur 2.2) so it reads as soft phone-camera text; at 2x zoom on the final it is unreadable, not misspelled. `incoming/2026-11-15/P10-clip-v1-soft.mp4`.
- Lesson: small wordmarks garble in 720p motion. Next stills: keep the SHIZEN mark at least the size of the art file's proportion or check it first in every clip.

## Edit (`pipeline/video/part10/p10-v1.json`)
0.0 to 5.6, crop [690,1227,15,20], low-res pass, soft 0.8. Text TikTok Sans size 50, y 1170 (61 to 66% of the frame, over the dark sleeve and shorts, clear of both faces and the right-side buttons): "coach banned his / rash guard from class" 0 to 2.18 s; "said nobody was watching / the technique" 2.2 to 5.6 s. Sparta start 3.68: quiet 1.7 to 2.0 s, drop at about 2.25 s.

## /ttevaluate: PASS 21/22
Standing rules all OK.
| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Hook | 2 | Frame 1: coach glaring down at the dragon plus "coach banned his rash guard from class" (conflict and an open loop at 0.0 s) |
| 2 | Curiosity gap | 2 | Why was it banned? Paid off at 2.2 s |
| 3 | Voice | 2 | Classmate gossip register |
| 4 | Legibility | 2 | 2 lines each, 2.2 s and 3.4 s, mid-frame safe zone |
| 5 | Sound | 2 | Ambience, drop on the payoff, works muted |
| 6 | Pacing | 2 | Text switch 2.2 s, coach pout 3.8 to 4.6 s |
| 7 | Length/loop | 1 | 5.6 s (under 7) by design for completion; static shot loops |
| 8 | Comment pull | 2 | "does your gym have a dress code?" |
| 9 | Brand restraint | 2 | Product on the garment only |
| 11 | Cohesion | 2 | Coach staring at the back, banned line, "nobody was watching the technique" |
| 10 | Honesty | 2 | No claims; AI label per Nic's decision |

## Posting
- File `video-v1-post.mp4`, 6,169,905 bytes, sha256 1491fd63..., H.264 1080x1920 + AAC, 5.63 s.
- Caption (TikTok and IG): he still wears it to open mat 🐉 does your gym have a dress code? #bjj #nogi #rashguard #nogibjj #bjjhumor
- Manual AI label OFF, auto labels untouched, TikTok Your brand ON. Any AI warning, restriction or takedown: stop posting and report. TikTok first, then IG (alternate profile route if the IG upload stalls).
- Measure at 4 h and 23 h: 0:01 retention (target over 70%), full watch (over 25%), views (over 1,500).
