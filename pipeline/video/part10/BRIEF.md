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

## 15 Nov: hunt found no compliant set. Decision: option B, accept the "class listening to the instructor" source type (supersedes the criteria above)
The concept only needs one watcher: the coach looking at the lead's back. So the frame is a student seated with his back to the camera while the instructor faces the camera. Everyone else is cropped out in code before the still edit, which also makes full identity replacement easier (two people to replace, not five).

Hard criteria, in priority order:
1. Real camera footage of a no-gi class or open mat: a phone, or an ordinary single camera on a gym or YouTube channel. No stock, no AI, no competition or broadcast footage.
2. Everyone in the frame clearly an adult.
3. Lead: an adult man in the foreground sitting or kneeling with his back to the camera (square or three-quarter), calm, not drilling, touching nobody. No large wordmark across his back (small logos elsewhere are fine).
4. Exactly one other prominent person: the instructor (or a partner) facing the camera, standing or kneeling, face at least about 60 px tall, hands not touching the lead. Talking is fine; his gesture gets frozen in the motion prompt.
5. A 9:16 crop containing just these two is at least 600x1066: vertical 720x1280 or above, or landscape 1920x1080 or above. Anyone else must fall outside that crop, or be small enough to crop away.
6. Inside that crop: no burned-in captions, no bright windows behind a face, no large wordmarks.
7. Nobody well known (famous athletes or named head instructors).
Send 3 to 5 candidates with the source link and timestamp, ideally from different videos.

Script holds: "coach banned his rash guard / from class" then "said nobody was watching / the technique". The still card will replace exactly two people (lead and instructor), with the instructor becoming an East Asian, muscular man in his late thirties looking at the lead's back, unimpressed.

## 15 Nov 08:32 full-res review: Dapto and Pearson REJECTED
- Dapto 4:15 to 4:21: guard demo, lead on his back with a partner over him. 4:24: burned-in "GAME 5" title. 4:27 and 4:30: the teal man sits back to camera but a partner is tangled with him (guard), and a seated student at left looks under 18. Fails contact and age.
- Pearson 2:30 to 2:34: both men standing and drilling a double leg, in contact; no seated back.

## Pivot (option C): one-man frame, tension carried by the hook text and a tight frame on the print
The coach-in-frame requirement is what made the hunt fail. Drop it: frame 1 is a tight shot where his back and the print fill the frame, with the conflict line on screen from frame 1. Script, caption, design (Ryu, navy) and length (about 5.5 s) stay the same.

Hard criteria, in priority order:
1. Real camera footage of a no-gi class or open mat (phone or an ordinary single camera). No stock, AI, competition or broadcast.
2. Everyone visible in the final crop clearly an adult.
3. One adult man with his back to the camera (standing, seated or kneeling; square or three-quarter), still, touching nobody, not drilling. A bystander watching others roll counts.
4. A 9:16 crop around him is at least 600x1066 and his back fills at least 40% of the crop height.
5. Anyone else inside that crop is either removable by cropping or large enough to fully replace (face about 60 px or more), two people at most.
6. Inside the crop: no burned-in text, no bright windows behind a face, no large wordmark across his back.
7. Nobody well known.
Send 3 to 5 untouched full-res frames (and the link plus timestamp) by direct chat attachment, ideally from different videos.

## 15 Nov 09:25 source review: PASS Coastal 34:10; Holy City 0:00 and 39:10 rejected
- Source: Coastal Jiu Jitsu, "Adult No-Gi Jiu Jitsu in Miramar Beach | Leg Entanglements to the Back", 34:10, https://www.youtube.com/watch?v=FrHv31_H500&t=2050s. Untouched 1920x1080 frame `incoming/2026-11-15/src/coastal-3410.jpg` (sha 3c7526aa...).
- Base for Flow: real 9:16 crop x 1130 to 1738, full height, `incoming/2026-11-15/src/P10-coastal-crop.png` (608x1080, native pixels, no resize). Inside it: the seated lead (back three-quarter, arms around his knees, no contact; back fills about 55% of the height) and ONE standing man behind him, face about 100 px, who becomes the coach. The instructor, the windows, the door and the fan are all outside the crop. So the coach-in-frame version of the concept is back.
- Holy City 39:10: lead cut by the frame edge, back only about 32% of the height, rolling pair close to the crop. Holy City 0:00: lead cut at the left edge, wall logo, a man lying behind his head, sandals and a mirror edge in the crop.

## Still card (FINAL, image 1 = Ryu_back.jpg, image 2 = P10-coastal-crop.png; Flow image mode, Nano Banana 2.1, 0 credits, 9:16, x1)
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, both people's positions and poses, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
First, the man sitting on the mat in the foreground keeps his exact pose (sitting with his arms wrapped around his knees, his back three-quarter to the camera, his head in profile looking left) and becomes a completely different, clearly adult man in his early thirties: light olive skin, short dark brown hair in a low skin fade, a short dark brown beard, a straighter nose and a different ear and jawline from the original; broad, muscular, athletic shoulders and back. He wears a navy LONG-SLEEVE rash guard, the same navy as the background of image 1, with plain navy sleeves all the way down to his wrists, no logo on the shoulder and no print on the sleeves or front, and the artwork from image 1 printed large on the visible back panel exactly as drawn, following the angle of his back, with the SHIZEN mark centred just below the back of the collar; plain black shorts and plain black leggings.
Second, the man standing behind him keeps his exact position and standing pose and becomes a completely different, clearly adult East Asian man in his late thirties: short black hair, clean-shaven, a different face shape, nose and eyes from the original; lean and visibly muscular, in a fitted plain grey short-sleeve rash guard. He tilts his head down to look at the back of the seated man, with a flat, unimpressed expression, mouth closed.
Nothing else changes: plain wall, white mat, the bag on the bench. No text, logos or writing anywhere except the SHIZEN mark on the print. Neither man may keep his original face.

## Still QA gates
1. Overlay against P10-coastal-crop: same camera, framing and both positions.
2. Face check, hard gate: crop both faces from the still and the base side by side at 4x. If either could be the original person, FAIL (no blur fix).
3. Frame 1 test at phone size: the print and the coach looking down at it read in one glance.
4. Ryu faithful (the dragon as drawn, not simplified), navy, long plain sleeves, shoulder logo gone, SHIZEN mark from the art.
5. Coach East Asian, muscular, looking at the back; both clearly adult.
6. No logos or writing, no clipped highlights (the white mat must keep texture), no anatomy errors (hands and feet).

## Motion (after a still pass, at least 20 min later): unchanged from the brief above, 6 s, 720p, 10 credits.
