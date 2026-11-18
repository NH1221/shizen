# Part 12: source hunt (Coastal, new composition)
Pull untouched native 1920x1080 frames from https://www.youtube.com/watch?v=FrHv31_H500, sampling every 15 s across the whole video EXCEPT 34:00 to 34:50. Send 6 to 10 candidates with timestamps.
Wanted: a different composition from Parts 10 and 11, for example the lead seated or kneeling from a new angle (more square-on back, or further from the camera), the coach standing at the left or kneeling, or the lead standing with his back to the camera while the coach faces him.
Criteria: one adult man with his back to the camera, calm, touching nobody; one other adult facing the camera close to him (face about 60 px or more); a 9:16 crop of just these two at least 600x1066 with no captions, bright windows, door glass or wordmarks; everyone clearly adult; nobody well known.
No Flow until Claude passes a frame.

## 17 Nov 09:34 survey review (186 frames, every 15 s, 34:00 to 34:50 excluded)
- 0:00 to 11:15: wide shots from the far corner; people tiny. No.
- 11:30 to 28:30, 30:00 to 33:45, 35:15 to 47:15: drilling or rolling (contact), wide shots, people facing the camera without a back in front of them, or windows behind. No. (19:15 to 20:15 has a big seated back at right but nobody near him facing the camera; 42:00 to 42:15 and 44:45 are men facing the camera.)
- 28:45 to 29:15: a seated back with a standing man facing the camera at arm's length, but the two span about 675 to 810 px native (wider than a 608 px 9:16 crop), the door glass sits above the seated man's head, and at 29:00 the standing man is mid-gesture. Backup only.
- 35:00: the best. The lead sits hunched forward in the foreground (back square to the camera, arms around his knees), the standing man directly behind him faces the camera with a hand on his hip (face about 120 px native). The left seated man and the windows fall outside a crop of about x 1100 to 1708. Risk: a background man walking near x 1035 to 1170 at the crop's left edge. It is the same two real people and spot as Parts 10 and 11, a few seconds later, which suits a third part of the series (same spot on the mat every class); every identity is replaced and face-checked again.
## Native frames to extract (untouched 1920x1080)
35:00.0, 35:01.5, 35:03.0, 35:04.5 (to find a moment with the walking man clear of the crop), plus backup 29:10.0 and 29:15.0.

## 17 Nov 09:41 native-frame review: PASS coastal-2100 (35:00.0)
- 35:00.0 chosen: the lead sits hunched forward, back square to the camera, arms around his knees; the standing man directly behind him faces the camera, hands on hips, still (face about 100 px). Nobody touches anyone (his hand is on his own hip behind the lead's head).
- 35:01.5 rejected: lead plus standing man span about 700 px, wider than a 608 crop. 35:03 (turning) and 35:04.5 (bending down) rejected. 29:10 (pointing) and 29:15 (the pair spans about 780 px) rejected.
- Base: real crop x 1110 to 1718, full height: `incoming/2026-11-17/src/P12-coastal-2100-crop.png` (608x1080, native pixels, sha 32efe5fd...). Inside: the lead, the standing man, the bag and bench, and half of a man at the far left edge walking away with his back to the camera (no face visible; he is replaced too). Outside: the instructor, the windows, the door and the fan.

## Still card (ready; DESIGN set after Part 11's 4 h numbers, default Nami in navy; image 1 = <DESIGN>_back.jpg, image 2 = P12-coastal-2100-crop.png). Built from the v1/v5 wording that held the scene:
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, every person's position and pose, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
First, the man sitting on the mat in the foreground keeps his exact pose (sitting hunched forward with his arms around his knees, his back to the camera, his head down) and becomes a completely different, clearly adult man in his early thirties: light olive skin, short dark brown hair in a low skin fade, a short dark brown beard, a different ear, neck and jawline from the original; broad, muscular, athletic shoulders and back. He wears a <COLOUR> LONG-SLEEVE rash guard, the same <COLOUR> as the background of image 1, with plain sleeves all the way down to his wrists, no logo on the shoulder and no print on the sleeves or front, and the artwork from image 1 printed large on his back exactly as drawn, centred on his spine. Above it, centred just below the collar, the gold yin-yang circle and the word SHIZEN, copied exactly from image 1 at the same small size and in the same thin letters. Plain black shorts and plain black leggings.
Second, the man standing behind him keeps his exact position and standing pose with his hands on his hips and becomes a completely different, clearly adult East Asian man in his late thirties: short black hair, clean-shaven, a different face shape, nose, eyes and ears from the original; lean and visibly muscular, in a fitted plain grey short-sleeve rash guard and black shorts. He looks down at the seated man's back with a flat, unimpressed expression, mouth closed.
Third, the man at the far left edge walking away keeps his position and becomes a different adult man with short dark hair, in a plain black rash guard.
Nothing else changes: plain wall, white mat, the bench and the bag. No text, logos or writing anywhere except the SHIZEN mark on the print. Nobody may keep their original face or head.

Gates: as Part 11 (overlay with room, wall, camera height and lead pose matching; coach within about 60 px, hands clear of the lead; 4x face check of every visible person against coastal-2100; print faithful; wordmark matches the art and reads SHIZEN at 2x; plain long sleeves; all adult; mat texture; hands and feet).

## FINAL treatment (17 Nov, after Part 11 at 4 h)
- Standalone, not a sequel. DESIGN: Ryu (`brand/print-backs/Ryu_back.jpg`), COLOUR: navy. Nami parked (its stacked symmetric waves are as intricate as Hebi-Mark, which this model could not draw).
- Variable: length about 4 s, ending just after the payoff (Part 10 lost most viewers at 0:02 and ran 3.4 s past its payoff).
- Text: "coach asked him to wear / something plain" 0 to ~1.6 s; "this is the plain one" from ~1.6 s (on the music drop) to the end, over the coach's head shake.
- Caption: he genuinely thinks this is low key 🐉 what's the loudest rash guard at your gym? #bjj #nogi #rashguard #nogibjj #bjjhumor
- Success at 4 h vs Part 10: full watch over 25%, average watch over 75% of length, 0:01 over 70%, likes at or above 15, views over 700.

## FINAL still card (image 1 = brand/print-backs/Ryu_back.jpg, image 2 = incoming/2026-11-17/src/P12-coastal-2100-crop.png; Flow image mode, Nano Banana 2.1, 0 credits, 9:16, x1)
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, every person's position and pose, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
First, the man sitting on the mat in the foreground keeps his exact pose (sitting hunched forward with his arms around his knees, his back to the camera, his head down) and becomes a completely different, clearly adult man in his early thirties: light olive skin, short dark brown hair in a low skin fade, a short dark brown beard, a different ear, neck and jawline from the original; broad, muscular, athletic shoulders and back. He wears a navy LONG-SLEEVE rash guard, the same navy as the background of image 1, with plain navy sleeves all the way down to his wrists, no logo on the shoulder and no print on the sleeves or front, and the artwork from image 1 printed large on his back exactly as drawn, centred on his spine. Above it, centred just below the collar, the gold yin-yang circle and the word SHIZEN, copied exactly from image 1 at the same small size and in the same thin letters. Plain black shorts and plain black leggings.
Second, the man standing behind him keeps his exact position and standing pose with his hands on his hips and becomes a completely different, clearly adult East Asian man in his late thirties: short black hair, clean-shaven, a different face shape, nose, eyes and ears from the original; lean and visibly muscular, in a fitted plain grey short-sleeve rash guard and black shorts. He looks down at the seated man's back with a flat, unimpressed expression, mouth closed.
Third, the man at the far left edge walking away keeps his position and becomes a different adult man with short dark hair, in a plain black rash guard.
Nothing else changes: plain wall, white mat, the bench and the bag. No text, logos or writing anywhere except the SHIZEN mark on the print. Nobody may keep their original face or head.

Still gates: overlay (room, wall, camera height, lead pose exact; coach within about 60 px, hands clear of the lead); 4x face/head check of all three people against coastal-2100; Ryu faithful (as in Parts 7 and 10); wordmark matches the art and reads SHIZEN at 2x; navy long plain sleeves, shoulder logo gone; all adult; no other writing; mat texture; hands and feet.

## FINAL motion card (at least 20 min after a still pass)
Omni 1.1 Flash, Frames to Video from the passed still only, 720p, 9:16, 6 s (10 credits), x1. Keep the raw master; fresh download by direct chat attachment.
Prompt: Static locked-off UGC iPhone footage. The man in the navy rash guard sits completely still, hunched forward with his head down, breathing slowly; his arms and hands do not move. The man standing behind him keeps his hands on his hips and stares down at the seated man's back, then slowly shakes his head once with a quiet sigh. The man at the far left edge stands still. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; keep every face, the clothing and the print exactly; the print and the SHIZEN lettering never redraw; no other text or logos; no smiling.
Clip gates: as Part 11, including SHIZEN in frame 0 at 2x (one re-roll if it garbles, then local softening).

## Edit plan
About 4 s from the clip's calmest start. Beat 1 to ~1.6 s, music drop and beat 2 at ~1.6 s, end about 0.6 s after the head shake finishes, on a frame matching frame 1 for the loop. Text placed clear of both faces and the print. /ttevaluate 18/22 or better.

## Still v1 (17 Nov, submitted 13:27:16): FAIL, `incoming/2026-11-17/stills/P12-v1.jpg` (record only, never use)
- HARD FACE GATE FAIL: the man at the left edge (back to the camera and bald in the source) was turned into a man in profile with dark wavy hair and a full dark beard who closely resembles the REAL standing man in coastal-2100 (side-by-side at 4x: same hair, beard line, brow and nose). The model carried a real face across to another person. Not usable.
- Lead (new olive-skinned man) and coach (new clean-shaven East Asian man) passed the face check; Ryu faithful; wordmark serif, reads SHIZEN at 2x; navy long plain sleeves; positions close.
- Lesson: every extra person in the crop is another chance for a real face to survive or move. Crop out anyone who is not needed BEFORE the edit.

## Base v2: crop x 1180 to 1788 (`incoming/2026-11-17/src/P12-coastal-2100-crop-v2.png`, 608x1080 native, sha df836761...)
Only the lead and the standing man. The walking man is gone (the bag strap remains at the left edge); the lead's knees and forearms are cut at the left edge (phone framing); the fan stays outside.

## Still card v2 (today's last submit, no earlier than 13:47:16; image 1 = Ryu_back.jpg, image 2 = P12-coastal-2100-crop-v2.png). The v1 card with the "Third" sentence removed, nothing else changed:
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, every person's position and pose, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
First, the man sitting on the mat in the foreground keeps his exact pose (sitting hunched forward with his arms around his knees, his back to the camera, his head down) and becomes a completely different, clearly adult man in his early thirties: light olive skin, short dark brown hair in a low skin fade, a short dark brown beard, a different ear, neck and jawline from the original; broad, muscular, athletic shoulders and back. He wears a navy LONG-SLEEVE rash guard, the same navy as the background of image 1, with plain navy sleeves all the way down to his wrists, no logo on the shoulder and no print on the sleeves or front, and the artwork from image 1 printed large on his back exactly as drawn, centred on his spine. Above it, centred just below the collar, the gold yin-yang circle and the word SHIZEN, copied exactly from image 1 at the same small size and in the same thin letters. Plain black shorts and plain black leggings.
Second, the man standing behind him keeps his exact position and standing pose with his hands on his hips and becomes a completely different, clearly adult East Asian man in his late thirties: short black hair, clean-shaven, a different face shape, nose, eyes and ears from the original; lean and visibly muscular, in a fitted plain grey short-sleeve rash guard and black shorts. He looks down at the seated man's back with a flat, unimpressed expression, mouth closed.
Nothing else changes: plain wall, white mat, the bench and the bag. No text, logos or writing anywhere except the SHIZEN mark on the print. Nobody may keep their original face or head.
Added gate: no third person may appear. Motion then goes tomorrow (first slot after the refresh) if v2 passes.

## Still v2 (17 Nov, submitted 13:48:31): INVALID, `incoming/2026-11-17/stills/P12-v2-INVALID-wrong-input.jpg` (record only, never use, never attach)
- Execution error caught by Instinct: Flow's "Add to prompt" kept the previously selected v1 GENERATED image (9a9e8210) as image 2 instead of the uploaded crop-v2. So this output is an edit of an AI image (breaks the real-reference rule) and still shows the third person. It says nothing about whether card v2 works.
- Today's submits: 4 of 4 used. No Flow until tomorrow.

## Pre-submit ingredient check (new standing step, every Flow submit)
Before pressing generate: open each attached ingredient and confirm its source is the intended upload (file name, size or source URL), not just the thumbnail. Image 1 must be the brand print file; image 2 must be the real crop. Clear any previously selected generated image from the prompt first. Record both ingredient sources in the submit note.

## 18 Nov production plan
1. First slot after the account refresh (no earlier than 08:15): still with card v2 above, image 1 = brand/print-backs/Ryu_back.jpg, image 2 = incoming/2026-11-17/src/P12-coastal-2100-crop-v2.png (sha df836761...), after the ingredient check.
2. Claude checks: overlay against crop-v2; 4x face check of BOTH people against coastal-2100 (the lead and the standing man); no third person; Ryu faithful; wordmark reads SHIZEN at 2x; navy long plain sleeves; mat texture; hands and feet.
3. If it fails, one more still the same day (at least 20 min later) with whatever single fix the review names.
4. On a pass, the clip at least 20 min later with the two-person motion card below.

## Motion card v2 (two-person base; replaces the motion card above)
Omni 1.1 Flash, Frames to Video from the passed still only, 720p, 9:16, 6 s (10 credits), x1. Keep the raw master; fresh download by direct chat attachment.
Prompt: Static locked-off UGC iPhone footage. The man in the navy rash guard sits completely still, hunched forward with his head down, breathing slowly; his arms and hands do not move. The man standing behind him keeps his hands on his hips and stares down at the seated man's back, then slowly shakes his head once with a quiet sigh. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; keep both faces, the clothing and the print exactly; the print and the SHIZEN lettering never redraw; no other text or logos; no smiling.
Clip gates: as Part 11, including SHIZEN in frame 0 at 2x and no third person appearing.

## FINAL cards for 18 Nov (prompt method v1; supersede every earlier P12 card)
What changed from card v2 and why: only the last sentence, which now forbids reusing any face from image 2 (P12 v1 moved a real face onto another person). Untested; everything else is the template wording that held the scene in P10 v1, P11 v5 and P12 v1. The third-person sentence is gone because the crop no longer contains a third person.

### Still (image 1 = brand/print-backs/Ryu_back.jpg; image 2 = incoming/2026-11-17/src/P12-coastal-2100-crop-v2.png, sha df836761...; Flow image mode, Nano Banana 2.1, 9:16, x1, 0 credits)
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, every person's position and pose, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
First, the man sitting on the mat in the foreground keeps his exact pose (sitting hunched forward with his arms around his knees, his back to the camera, his head down) and becomes a completely different, clearly adult man in his early thirties: light olive skin, short dark brown hair in a low skin fade, a short dark brown beard, a different ear, neck and jawline from the original; broad, muscular, athletic shoulders and back. He wears a navy LONG-SLEEVE rash guard, the same navy as the background of image 1, with plain navy sleeves all the way down to his wrists, no logo on the shoulder and no print on the sleeves or front, and the artwork from image 1 printed large on his back exactly as drawn, centred on his spine. Above it, centred just below the collar, the gold yin-yang circle and the word SHIZEN, copied exactly from image 1 at the same small size and in the same thin letters. Plain black shorts and plain black leggings.
Second, the man standing behind him keeps his exact position and standing pose with his hands on his hips and becomes a completely different, clearly adult East Asian man in his late thirties: short black hair, clean-shaven, a different face shape, nose, eyes and ears from the original; lean and visibly muscular, in a fitted plain grey short-sleeve rash guard and black shorts. He looks down at the seated man's back with a flat, unimpressed expression, mouth closed.
Nothing else changes: plain wall, white mat, the bench and the bag. No text, logos or writing anywhere except the SHIZEN mark on the print. Neither man may keep his original face, and no face from image 2 may appear on anyone.

### Motion (Omni 1.1 Flash, Frames to Video from the passed still only, 720p, 9:16, 6 s, 10 credits, x1)
Static locked-off UGC iPhone footage. The man in the navy rash guard sits completely still, hunched forward with his head down, breathing slowly; his arms and hands do not move. The man standing behind him keeps his hands on his hips and stares down at the seated man's back, then slowly shakes his head once with a quiet sigh. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; keep both faces, the clothing and the print exactly; the print and the SHIZEN lettering never redraw; no other text or logos; no smiling.

## NEXT-RUN CHECKLIST (18 Nov)
1. 08:15 or later. In Flow image mode, clear the prompt and remove every previously selected image.
2. Upload brand/print-backs/Ryu_back.jpg and incoming/2026-11-17/src/P12-coastal-2100-crop-v2.png fresh. Open each ingredient and confirm its file name and size: image 1 = Ryu_back.jpg, image 2 = P12-coastal-2100-crop-v2.png (608x1080). No generated image anywhere in the prompt.
3. Paste the still card above exactly. Nano Banana 2.1, 9:16, x1. Generate once. Note the time and both ingredient sources.
4. Send the untouched still by direct chat attachment. Wait for Claude's gate result. No motion before a PASS.
5. If FAIL: Claude names one slot or phrase to change (never a rewrite). Submit 2 no earlier than 20 min after submit 1, steps 1 to 4 again.
6. On PASS: no earlier than 20 min later, Frames to Video from that passed still only (confirm the ingredient is the passed still), Omni 1.1 Flash, 720p, 9:16, 6 s, x1; paste the motion card exactly.
7. Download the raw clip fresh into a new folder; attach it directly; do not edit or re-encode. Claude checks every frame and SHIZEN in frame 0.
8. If the clip's wordmark garbles: one re-roll at least 20 min later; if that garbles too, Claude softens it in the edit.
9. Maximum 4 submits; stop at the first Flow warning; no other accounts, no purchases.

## Still v3 (18 Nov, submitted 08:18:41, FINAL card 2bbcfe7, verified ingredients): FAIL on the wordmark only; kept as FALLBACK
- PASS: overlay (room, wall, bench, camera height and framing match crop-v2; lead's head and back within about 20 px, slightly more upright but same hunched-forward pose; coach in place, hands on hips, clear of the lead); 4x face check (lead: new olive-skinned man vs the source's Black man with greying hair; coach: new clean-shaven East Asian man vs the source's bearded man with wavy hair; neither could be the original); no third person; Ryu faithful (as in Parts 7 and 10); navy long plain sleeves, shoulder logo gone; hands and feet correct; no clipped pixels. The bag area changed slightly (extra bags), background only.
- FAIL: the wordmark is the right small serif style but the letters are malformed at 2x (the E and N come out reversed or broken, reading roughly "SHIZƎN"). Same wording that rendered correctly in P11 v5 and P12 v1, so this is model variance, not the prompt.
- Decision: one retry with the SAME FINAL card, unchanged (method rule: variance is not fixed by rewording). Submit 2 no earlier than 08:38:41, same verified ingredients.
- If the retry passes every gate, use it. If it fails on anything, use v3 as the pass with the wordmark softened locally in the edit (Part 10 method, logged), so the remaining submits go to the clip.

## Still v4 (18 Nov, submitted 08:47:17, same FINAL card and verified ingredients): PASS, chosen over v3
- Wordmark: small thin serif under the yin-yang, reads SHIZEN at 2x (the N is slightly soft but correct). Gate passed; v3 fallback not needed.
- Overlay: room, wall, bench, camera height and framing match crop-v2; lead in the same hunched-forward pose (slightly more upright, within about 20 px); coach in place, hands on hips, clear of the lead.
- 4x face check: lead new (olive skin, low fade, beard vs the source's Black man with greying hair); coach new (clean-shaven East Asian vs the source's bearded man with wavy hair). No third person.
- Ryu faithful; navy long plain sleeves, shoulder logo gone; hands and feet correct; mat keeps texture.
- Note: an unchanged card fixed the wordmark on the second roll, consistent with variance (method rule 7).
- Motion: no earlier than 09:07:17 (20 min after this submit; spacing is between submits), Motion v2 card from the FINAL cards section, Frames to Video from P12-v4 only.
