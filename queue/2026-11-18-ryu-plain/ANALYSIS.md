# Part 12: Ryu, "coach asked him to wear something plain / this is the plain one"
4.1 s, 1080x1920. Standalone (no sequel). One shot from the real Coastal frame 35:00 (crop `incoming/2026-11-17/src/P12-coastal-2100-crop-v2.png`, two people only), both fully replaced (face check passed on still v4), real Ryu print. Still v4 (18 Nov 08:47:17, FINAL card 2bbcfe7, prompt method v1). Clip P12-clip-v1: Omni 1.1 Flash, 720p, 6 s, 09:08:42, raw master `incoming/2026-11-18/P12-clip-v1.mp4` (2,561,324 bytes).

## Clip review (every 0.25 s; full-res wordmark, coach face and hands at 0.0, 3.0, 5.9)
- Camera locked, no cuts or zoom; room unchanged; two people only.
- Dragon stable in every frame, no redraw. WORDMARK reads SHIZEN in thin serif at 2x in frame 0, mid-clip and the last frame: gate passed, no softening.
- Lead: small natural head bob, arms and hands still. Coach: hands stay on hips throughout; looks down at the back, small head movement, ends on a tight-lipped, unimpressed pout (no smile). The requested single head shake is subtle, not a clear shake; the pout carries the beat instead.
- Faces consistent with still v4 throughout. Audio: ambience about -46 LUFS, no words or music.

## Edit (`pipeline/video/part12/p12-v1.json`)
in 1.9 to 5.95 (the coach's look and pout), crop [690,1227,15,0], low-res pass, soft 0.8, TikTok Sans 52 at y 330 over the coach's chest (clear of both faces and the print). "coach asked him to wear / something plain" 0 to 1.58 s; "this is the plain one" 1.6 s to the end. Sparta start 4.45: quiet 1.1 to 1.45 s, drop at about 1.6 s on the payoff. Ends on the pout; still pose loops into frame 1.

## /ttevaluate: PASS 20/22
Standing rules all OK.
| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Hook | 2 | Frame 1: coach staring down at the dragon plus a setup line |
| 2 | Curiosity gap | 2 | "something plain" pays off on the dragon at 1.6 s |
| 3 | Voice | 2 | Gym-mate deadpan |
| 4 | Legibility | 2 | 2 lines 1.6 s; 1 line 2.5 s; clear of faces and buttons |
| 5 | Sound | 2 | Drop on the payoff; works muted |
| 6 | Pacing | 2 | Payoff at 1.6 s, pout at the end; nothing flat over 3 s |
| 7 | Length/loop | 1 | 4.1 s by design (the test variable); loops cleanly |
| 8 | Comment pull | 2 | "what's the loudest rash guard at your gym?" |
| 9 | Brand restraint | 2 | Product on the garment only |
| 11 | Cohesion | 2 | Plain request, loud dragon, unimpressed coach |
| 10 | Honesty | 2 | No claims; AI label per Nic's decision |
Point lost on 7 (under 7 s) is the deliberate experiment; curiosity scored 2 because the payoff is visual, unlike Part 8's pun.

## Posting
- File `video-v1-post.mp4` (size and sha in the commit message).
- Caption: he genuinely thinks this is low key 🐉 what's the loudest rash guard at your gym? #bjj #nogi #rashguard #nogibjj #bjjhumor
- Manual AI label OFF, auto labels untouched, TikTok Your brand ON. Any AI warning, restriction or takedown: stop and report. TikTok first, then IG.
- Measure at 4 h vs Part 10: full watch over 25%, average over 75% of length (3.1 s), 0:01 over 70%, likes 15 or more, views over 700.
