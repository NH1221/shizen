# Part 10: "coach banned his rash guard" (Ryu), first-second test
Status: plan approved by Claude; waiting for a new real source frame. Instinct does not submit anything until Claude passes the frame and issues the final still card.

## Diagnosis and hypothesis
Nine posts at ~700 views, 99.9% For You, most viewers gone at 0:01. Frame 1 has always been a calm back with a setup line. Hypothesis: a frame 1 that already shows conflict (classmates' faces turned to the print, a coach in shot) plus a conflict hook line lifts 0:01 retention above 70% and completion above 25% at about 5.5 s. Success: 0:01 retention > 70%, full watch > 25%, and views past 1,500 (breaking the test batch). One main variable: the first second. Design held at Ryu (best likes so far).

## Concept
Classmate POV at a no-gi class. A muscular adult man sits on the mat with his back to the camera in a navy Ryu rash guard. Two or three classmates near him, and an East Asian coach, are already looking at his back. Text: the coach has banned the rash guard; the payoff is why.

- Text beat 1 (0.0 to 2.2 s, on screen from frame 1): "coach banned his rash guard / from class"
- Text beat 2 (2.2 to 5.5 s, on the music drop): "said nobody was watching / the technique"
- Caption: he still wears it to open mat 🐉 does your gym have a dress code? #bjj #nogi #rashguard #nogibjj #bjjhumor

## Source frame criteria (Instinct hunt)
Must have all of these:
1. Real phone footage of a no-gi class or open mat (not DSLR, competition, stock or AI). 720p or above.
2. Lead: one clearly adult man sitting or kneeling with his back square or near-square to the camera, in the foreground or mid-ground, back filling at least a third of the frame height, arms resting.
3. Two to four other people in frame, ideally facing the camera side or towards the lead, each with a face large enough to be clearly re-identified (at least about 60 px tall at 720 wide). Nobody tiny in the distance unless the frame can be cropped to remove them.
4. A standing or kneeling instructor in frame is a bonus (he will become the East Asian coach).
5. Everyone clearly an adult. Natural light, no blown windows behind people, no burned-in captions, few logos, nobody mid-gesture near the lead.
Send 3 to 5 candidates with the source URL. Claude picks, crops in code to remove distant people, and writes the still card.

## Still card template (finalised after the frame is chosen; image 1 = Ryu_back.jpg, image 2 = the cropped real frame)
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, every person's position and pose, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
First, the man sitting with his back to the camera keeps his exact pose and position and becomes a clearly adult man in his early thirties with a completely different head and face: [hair, skin, build specifics], broad, muscular, athletic. He wears a navy LONG-SLEEVE rash guard, the same navy as the background of image 1, plain navy sleeves to the wrists, no print on the sleeves or front, and the artwork from image 1 printed large on his back exactly as drawn, centred on his spine, with the SHIZEN mark centred below the collar; plain black shorts.
Second, [for each other person, by position]: keeps their exact position and pose, turns their head to look at the back of the man in the navy rash guard, and becomes a completely different adult between 25 and 45: [named face, skin, hair, build for each]. [Instructor]: becomes an East Asian man in his late thirties, lean and visibly muscular, short black hair, fitted plain grey short-sleeve rash guard, looking at the man's back with a flat, unimpressed expression.
All clothing on everyone becomes plain black, grey or navy with no logos, patterns or writing. No text, logos or writing anywhere except the SHIZEN mark on the print. Nobody may keep their original face.

## Still QA gates (all must pass)
- Overlay against the base: same camera, framing and positions.
- Face check: crop every face from the still and the base side by side; any face that could be the original person FAILS (no blur fix).
- Frame 1 test: at phone size, within one glance you see the print and at least two faces looking at it.
- Ryu faithful (as drawn, not redrawn), navy, long plain sleeves, SHIZEN mark from the art.
- Everyone clearly adult, no logos or writing, no clipped highlights, no anatomy errors.

## Motion (after a still pass; at least 20 min later)
Omni 1.1 Flash, Frames to Video, 720p (highest free), 9:16, 6 s (10 credits), x1. Keep the raw master.
Prompt: Static locked-off UGC iPhone footage. The man in the navy rash guard sits still with his back to the camera, breathing slowly; his arms and hands do not move. The people around him keep looking at his back; one of them leans slightly closer, and the coach slowly shakes his head once. Nobody grapples. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; keep faces, clothing and the print exactly; the print never redraws; no text or logos; no smiling.

## Edit spec (pipeline/video/part10/p10-v1.json, built from p9-v1.json)
- in 0.0 to about 5.6 s (cut before any late artefact), no focus-falloff mask by default (faces must already be fully new); crop to make the back and the watching faces fill the frame.
- Low-res pass 432x768 then up, soft 0.8, grain, colour match.
- Text y about 230 (or wherever it clears all faces and the print), TikTok Sans 600, white, thin outline, beats as above; beat 1 visible on frame 1.
- Sparta: set start so the drop lands at 2.2 s (start = 3.43 - 0.35 = 3.08), verify from the loudness envelope.
- Loop: end on a still frame that matches frame 1.
- /ttevaluate 18/22 or better with hook scored 2. Posting file two-pass x264 9 Mbps, under 10 MB.

## Posting
Manual AI label OFF, auto labels untouched, TikTok Your brand ON. Any AI warning, restriction or takedown stops posting immediately. Log 4 h and 23 h numbers against 0:01 retention, full watch and views.

## 14 Nov 09:30 source review: Roger Gracie Academy HQ YouTube frames (2:42, 2:44, 2:45) REJECTED, no generation
- Landscape 1280x720: a 9:16 crop is only about 405x720, below the bank size, and would need the model to invent pixels.
- No usable lead: the foreground man faces the camera side-on with his face visible; the only back (2:45) is mid-drill with a partner over him, which invites contact and limb motion.
- The back where the print goes carries a large third-party wordmark, plus sponsor logos on shorts and rash guards; a lot for one edit to remove.
- A named academy's own produced video with identifiable instructors and students, likely not phone footage; bright windows behind.
- Tighter hunting criteria: native vertical phone video (TikTok, Reels, Shorts), 1080x1920 preferred and 720x1280 minimum; a lead whose back is to the camera and NOT in a drill or in contact; no big wordmark on the lead's back; avoid gyms' or famous athletes' own promo channels and anyone well known.
