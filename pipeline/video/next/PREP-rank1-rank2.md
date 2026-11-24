# Rank 1 and rank 2: source-hunt checklist and pre-generation cards (offline prep, 19 Nov)

Status: offline prep only. No source chosen, nothing generated, no account action. No URL or timestamp below is real; every `<slot>` is filled only from footage Instinct has actually inspected.

## 0. Execution rules (authoritative; these override any older line in the repo)
- **Originality.** A source video, room or scene that appears in ANY posted Shizen video is off limits at every timestamp, even with new generations and new identities.
  - Burned: the art.of.roll reel; Coastal Jiu Jitsu (FrHv31_H500, AwNf71Pkn98); Holy City Jujitsu (EShhwFBHsR4).
  - Audit every candidate against all posted videos on the profile grid, not only this list.
  - Older repo lines that allow reusing a proven base or another timestamp of a used video are SUPERSEDED and must not be followed. These are PLAYBOOK's 18 Nov 10:52 / 12:58 / 14:55 entries and part13/BRIEF.md.
- **Every post gets new generations:** a new still and a new clip. Attach only the real frame and the real print file. Never use an AI image as a base, and never ask the model to change a pose.
- **Flow limits:** free Flow on santonmanton only; max 4 submits a day, 20 minutes apart; 720p; keep raw masters.
- **Accounts:** Nic stays hands-off; TikTok only; Instagram stays paused, and P13 never goes to Instagram.
- **Stop rules:** any warning, restriction or CAPTCHA means stop and report.

## 1. Source fail conditions (any one = reject)

### Shared (every shot is a SOLO crop)
| # | Reject if |
|---|---|
| S1 | The video, room, gym or channel appears in any posted Shizen video, or is the same gym as a burned source |
| S2 | Any other person is visible in the final 9:16 crop: partial limbs, background people, mirror reflections |
| S3 | A possible minor is anywhere in the frame region used, or the subject is not clearly an adult man |
| S4 | The needed pose is not already present in a real frame |
| S5 | A 9:16 crop of at least 600x1066 real pixels is impossible, or the subject shows heavy compression or motion blur on the chosen frame |
| S6 | The camera pans, follows, drifts more than slightly, or is a gimbal, drone or broadcast multi-cam shot; or the footage is fisheye, slow-mo, filtered, or has an overlay or watermark over the subject |
| S7 | Gym logos, banners, flags or mat lettering are inside the crop and cannot be cropped out. Removing them restages the room; keeping them puts a real brand in our post |
| S8 | A window behind the subject, a blown-out torso or back, or coloured club lighting |
| S9 | The subject wears a gi, hoodie, backpack or towel, holds an object (bottle, phone, belt), or touches another person |

### Rank 1 shot A: the walk-on, back to camera
| # | Reject if |
|---|---|
| A1 | He is not walking AWAY from a static camera with his back square to it (within about 30°) |
| A2 | His back from collar to waist is not visible and unobstructed for at least 1 s of source |
| A3 | His hands are raised, adjusting his shirt or touching his hair (only a small natural arm swing is fine) |
| A4 | His face turns further than the ear line; long hair covers the back of the collar; he jogs or walks fast |
| A5 | His shoulders span less than about 35% of the crop width on the chosen frame, so the print would not read |

### Rank 1 shot B: lying flat on his back after a round
| # | Reject if |
|---|---|
| B1 | He is not lying flat face up and still, or he is mid-roll, being pinned or submitted, on his side or on his stomach |
| B2 | His face takes up more than about 12% of the crop height (a large face means high identity risk), or his head is cut off at the frame edge |
| B3 | There is mat lettering or a logo under or around him (the P14 lesson) |
| B4 | The ROOM does not match shot A: a different mat colour or texture, a different wall, or a different light direction or colour temperature. A different source person is fine, because both get replaced |

**Pair rule.** A and B must come from the same new room, ideally the same video and session. If one new room cannot yield a passing A and B, hold rank 1 honestly and run rank 2. Never:
- generate B from A's frame;
- pose him by prompt;
- borrow B from another room.

### Rank 2: "the one nobody wants to roll with"
| # | Reject if |
|---|---|
| R1 | He is not standing at the mat edge or on the mat, back to camera within about 30°, arms hanging at his sides, head facing away. Hands on hips or folded arms both fail |
| R2 | There is no space at shoulder height on at least one side, so the head-and-shoulder turn would leave the frame |
| R3 | His source build is slim. The model keeps the silhouette, so a slim body will not read as "the big guy" |

The shoulder roll is generated, so the source frame can be still.

**Hunt realism.** On 18 Nov, more than 25 videos were screened and none passed (see part12/BRIEF.md and part13/BRIEF.md). Solo backs in clean crops are rarer than expected.
- Those videos need no re-screening for the same pose. They are not burned, because none was posted.
- Search where these moments naturally happen: the last seconds of rounds in open-mat or sparring-rounds uploads, people walking on at the start of class, and the post-round lie-down.

## 2. What Instinct returns per candidate (no submit until Claude passes it)
- **Source details** as observed: URL, uploader, upload date, native resolution, and the exact timestamps for A and B, or for rank 2.
- **Frames:** a native-resolution grab of each candidate frame, plus 6 frames across a 2 s window around it.
- **Room audit:** one line confirming the room matches no posted video on the grid.
- **Claude's side:** Claude crops in code, runs sections 1 and 4, and returns PASS or FAIL per condition.

## 3. Identity continuity: exact words, pasted unchanged into every card for that man
**L1, the rank 1 man (all shots A and B, stills and clips):**
> a completely different, clearly adult man in his early thirties: light olive skin, short dark brown hair in a low skin fade, a short dark brown beard, dark brown eyes, straight dark eyebrows, a different face shape, nose, ears, neck and jawline from the original; broad, muscular, athletic shoulders, chest and back; barefoot, no tattoos, no jewellery, no watch, no tape

**R2, the rank 2 man (a different person from L1):**
> a completely different, clearly adult man in his mid thirties: medium brown skin, a closely shaved head, a full short black beard, dark brown eyes, a thick neck, a different face shape, nose, ears and jawline from the original; very big and heavily muscular, a heavyweight build with wide shoulders and a broad back; barefoot, no tattoos, no jewellery, no watch, no tape

**GARMENT block. Colour: Ryu = navy for rank 1; Twin Koi = dark charcoal for rank 2:**
> He wears a <COLOUR> LONG-SLEEVE rash guard, the same <COLOUR> as the background of image 1, with a crew neck and plain <COLOUR> sleeves all the way down to his wrists, no logo on the shoulder and no print, logo or writing on the sleeves. <FRONT CLAUSE> Plain black shorts and plain black leggings.

`<FRONT CLAUSE>`:
- Shot A, front not visible: "The front of the shirt is not visible in this shot."
- Shot B and rank 2, which show the front: the VERIFIED front description only. Until a front view is found in existing product files, these shots are BLOCKED. No front is invented, including a plain one.

## 4. Garment accuracy (what each shot may show)
- **Known from brand files** (brand/model4-sheet.jpg, brand/print-logo-position.jpg, img/ryu.jpg):
  - Crew neck, raglan seams, long plain sleeves.
  - Body colour equals the print background (Ryu is "gold on midnight").
  - The art is centred on the spine, with the small gold yin-yang and thin serif SHIZEN centred below the back collar.
- **Front: UNVERIFIED, and a gate.** The repo has no front view. Older cards asserted "no print on the front", but that was never sourced, so it is NOT used here. Shot B and the rank 2 turn are blocked until a front view is found in existing product files. Shot A shows no front and is not blocked. Hebi Mark is a chest design and stays parked.
- **Shot B (on his back):** the front only (blocked until the front is verified). The back art and wordmark are against the mat, so they cannot and must not be visible. FAIL if any art, yin-yang, lettering or logo appears anywhere in the frame.
- **Shot A (walking away):** back art and wordmark only.
- **Rank 2:** back art and wordmark at the start. During the turn, the visible side and front must match the verified front (blocked until then), and the art stays on the back and turns with it.

## 5. Cards (slots in `<>`; change ONE slot per retry, never rewrite)

### Still A (image 1 = brand/print-backs/Ryu_back.jpg; image 2 = A crop)
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, the man's position, pose and stride, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
The man walking away from the camera keeps his exact pose (<POSE AS IN BASE, e.g. mid-step, left foot forward, arms relaxed at his sides>) and becomes [L1]. [GARMENT, navy] On his back, the artwork from image 1 printed large exactly as drawn, centred on his spine. Above it, centred just below the collar, the gold yin-yang circle and the word SHIZEN, copied exactly from image 1 at the same small size and in the same thin letters.
Nothing else changes: <BACKGROUND ITEMS IN THE BASE>. No text, logos or writing anywhere except the SHIZEN mark on the print. He must not keep his original face, and no face from image 2 may appear on anyone.

### Still B (image 1 = Ryu_back.jpg as colour reference only; image 2 = B crop)
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, the man's position and pose lying on his back, the light, the phone grain and softness, and real skin texture. Image 1 is only a colour reference: use the navy of its background for the shirt and nothing else from it. Change only these things, all in this one edit.
The man lying on the mat keeps his exact pose (<POSE AS IN BASE, e.g. flat on his back, arms out to the sides, head tilted slightly left>) and becomes [L1]. He looks exhausted: eyes open and staring up, mouth slightly open. [GARMENT, navy] He is lying on his back, so the back of the shirt is against the mat and cannot be seen: no artwork, yin-yang, lettering or logo appears anywhere in this picture, on him or on the mat.
Nothing else changes: <BACKGROUND ITEMS IN THE BASE>. No text, logos or writing anywhere. He must not keep his original face, and no face from image 2 may appear on anyone.
- Retry slot if art leaks onto the front: remove image 1 and write "a dark midnight-navy" in place of the colour reference. This is a single change.

### Still rank 2 (image 1 = brand/print-backs/Twin-Koi_back.jpg; image 2 = rank 2 crop)
As Still A, with these changes:
- Pose slot: "standing at the mat edge with his back to the camera, arms hanging at his sides".
- Identity: [R2].
- Garment colour: "dark charcoal".

### Motion B (Omni 1.1 Flash, 720p, 6 s)
Static locked-off UGC iPhone footage. The man in the navy rash guard lies flat on his back exactly as in the frame, completely spent: from the first frame his chest rises and falls hard in deep, heavy breaths; his arms and hands stay where they are on the mat; near the end he lets out one long slow breath and his head sinks back slightly. Ambient gym sound and his heavy breathing only, no words, no music. One take, no cuts, no zoom, no change of angle; keep his face, the clothing and the shirt front exactly as in the frame; no artwork, lettering or logo appears anywhere; no smiling.

### Motion A (6 s)
Static locked-off UGC iPhone footage; the camera does not move or follow. The man in the navy rash guard keeps walking away from the camera at a slow, relaxed pace, three or four steps onto the mat, arms hanging loosely with a small natural swing, head facing forward; each foot plants with no sliding. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; keep his build, hair, the clothing and the print exactly; the print and the SHIZEN lettering never redraw and move with his back; no other text or logos; he does not turn around.

### Motion rank 2 (6 s)
Static locked-off UGC iPhone footage. The big man in the charcoal rash guard stands with his back to the camera and from the first frame rolls his shoulders twice, loosening up; then he turns his head and upper body toward the camera with a sheepish, apologetic grin, eyebrows raised, as if saying sorry; his arms stay hanging at his sides the whole time and his feet do not move. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; keep his build, the clothing and the print exactly; the print and the SHIZEN lettering stay on his back and turn with it, never redraw; the sleeves stay plain charcoal and the shirt front stays exactly as in the still (verified front); one consistent face once it appears; no other text or logos.

## 6. Pre-submit and QA gates
- **Before every submit:**
  - Clear old selections.
  - Verify each ingredient by its real source (file name and size), not the thumbnail.
  - Log both sources in the submit note.
- **Still QA (fail on any one):**
  - Any face could be the source person, checked at 4x side by side.
  - The camera, framing or room changed.
  - The pose changed.
  - Print art inexact, or the wordmark is large, bold or garbled (A and rank 2).
  - Any print or logo on the sleeves; a front that differs from the verified front; any back art in B.
  - Bad hands or feet.
  - Any text other than the wordmark.
- **Continuity QA, rank 1 only.** Put still A and still B side by side. They must match on:
  - skin tone, hair colour and fade, beard (its edges visible in A), and build;
  - navy shade, collar, shorts and leggings.

  B's face must match L1. If the two stills read as different men, re-roll the weaker still with no change to the card.
- **Clip QA** (every frame at full frame rate):
  - The print is never redrawn and the wordmark holds; if not, one re-roll, then local softening.
  - B shows chest motion from frame 0.
  - A has no gliding or foot sliding and he never turns around.
  - Rank 2 keeps one face through the turn, the grin reads, and the arms stay down.

## 7. Budget and hold tree
**Rank 1:**
- **Day N-1:** still A, then still B, 20 minutes apart. Up to 2 re-rolls that day, one slot change each. If either still fails twice with the same card, the base is the problem: go back to the hunt, or hold and run rank 2.
- **Day N:** clip B, then clip A, with 2 spare. If a clip fails after its re-roll, post nothing from rank 1 that day; follow the strategy v2.2 fallback.
- **Edit:** B 0 to ~1.3 s ("how it ended"); A ~1.3 to ~5 s ("how it started", then "\"i'll just do one light round\""); B's long breath taken from the end of clip B; the cut loops.

**Rank 2:** still, then clip at least 20 minutes later on the same day; 2 spare.

## 8. Remaining gaps (do not fill by guessing)
- **Shirt front (real gap, blocks shot B and rank 2):** not documented in the repo. Searched 19 Nov: brand/, img/, incoming/ and index.html; all back-only. Research existing files first: the waitlist page, supplier mockups and any product photos. Nic is not asked before that research, and no front is invented.
- **Untested motion:** walking, lying-down breathing and a face turn are all untested with this model.
- **Rank 1 room:** no candidate room with both moments has been found yet.

## 9. Source hunt log
- 19 Nov 14:20 (Instinct): 5 new videos sampled; none approved. These are sampled positions only, not whole videos rejected.

| Video | Positions | Reason |
|---|---|---|
| nJ46FhGuV1A | 3:55, 4:12 | Crowd, possible youth |
| HeQynIT08f8 | 0:50 | Fisheye, glare, small crowds |
| B_zIC2sj5yo | 0:20, 5:15 | Standing adults overlap, background pairs |
| fIswNOWtRSQ | 0:20 | Gi, contact, crowd |
| _EQ1e8SvRnw | 0:10, 1:00 | Crowd, obstruction |

- No isolated rank 1 pair found. Status: HOLD.

## 10. NEXT-DAY ROUTE while the shirt front is unverified (19 Nov 20:30; this is the active plan)
**Why it changes.** A live Drive check (Shizen assets 18 files, originals 4 files, plus name searches) found only BACK views. The front stays unverified, and no front is invented. Shot B face-up and the rank 2 turn both show the front, so both stay blocked.

**The fix:** use a pose that hides the front AND the face, and is common in real footage. That pose is a man lying FACE DOWN after a round, back up. Part 2 (our best-held post: 33% full watch) used this posture. Hiding the face does NOT remove the replacement requirement: the source person's whole identity and body (hair, skin, build, ears, neck, hands, clothing) is fully replaced with L1 and checked at 4x against the source. The hidden face only lowers the risk of a face carrying over. The print sits flat on a large back, and the only motion needed is breathing.

### Lead: "you good?" (one real moment, 1 still + 1 clip, 2 spare)
- **Opening (frame 0, motion):** his back heaves hard with heavy breathing. Text: "\"i'll just do one light round\"" (0 to ~2.2 s). The quote against the flattened body is the expectation-vs-reality tension.
- **~2.4 s, text:** "coach: you good?"
- **Payoff, visible action (~3.5 s):** without lifting his head, he raises one hand off the mat in a shaky thumbs-up, then lets it drop. The print is on screen the whole time but is not the payoff.
- **End (~5.5 s):** heaving continues and the cut loops to frame 0. The music drop lands on the thumbs-up, with the breathing kept under it.
- **Caption:** one light round they said 🐉 who's the guy at your gym who says this every time? #bjj #nogi #rashguard #nogibjj #bjjhumor
- **Design:** Ryu, navy.
- **Structural change vs P12 to P14** (static upright back, near-still opening, print-reveal payoff) on 3 real axes:
  1. posture: prone, seen from above;
  2. frame-0 motion;
  3. payoff type: the visible action of a response, not a print reveal.
- **Pass line at 23 h:** full watch 25%+ and 2+ shares or saves. Falsifier: two runs at or below 14% full watch.

### Optional upgrade: the flash-forward, back-only version
Only if the SAME new room also has an upright back-to-camera moment (standing, kneeling up or walking away; solo; any person, since both are replaced with L1). That shot goes in as "how it started", ahead of the face-down shot "how it ended".
- **Cost:** 2 stills (day N-1) + 2 clips (day N).
- **Rule:** both must pass. Otherwise post the lead alone. Never pose a shot by prompt.

### Source fail conditions for the face-down shot
S1 to S9 from section 1 still apply (solo, unused room, no minors, static camera, no lettering, no gi). Also reject if:

| # | Reject if |
|---|---|
| P1 | He is not lying face down, or kneeling folded with his forehead on the mat, with his back up and still. Mid-scramble, on his side, or a partner touching him all fail |
| P2 | Any part of his face is visible: a cheek turned to the camera, or an eye or nose in view |
| P3 | His back is foreshortened beyond about 45°, so the print could not read. The camera should be behind him or at his side at standing height, looking down |
| P4 | His back (collar to waist) is under about 35% of the crop height |
| P5 | Neither hand is visible and free on the mat beside him (both hands under his chest or head fails), since the payoff needs one free hand |
| P6 | Mat lettering or a logo is under or around him (the P14 lesson) |

**Where to look:** the last seconds of each round in open-mat and sparring-rounds uploads, and end-of-class moments. In those, people drop face down while the camera keeps running.

### Cards (sections 3 and 5 apply; change one slot per retry)
**Still (image 1 = Ryu_back.jpg; image 2 = the face-down crop):**

Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, the man's position and pose lying face down, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
The man lying face down on the mat keeps his exact pose (<POSE AS IN BASE, e.g. face down, head turned away, right arm along his side, left hand flat on the mat by his shoulder>) and becomes [L1]. [GARMENT, navy; FRONT CLAUSE: "He lies on his front, so the front of the shirt is against the mat and not visible."] On his back, the artwork from image 1 printed large exactly as drawn, centred on his spine. Above it, centred just below the collar, the gold yin-yang circle and the word SHIZEN, copied exactly from image 1 at the same small size and in the same thin letters.
Nothing else changes: <BACKGROUND ITEMS IN THE BASE>. No text, logos or writing anywhere except the SHIZEN mark on the print. His face stays hidden, and no face from image 2 may appear on anyone.

**Motion (Omni 1.1 Flash, 720p, 6 s):**

Static locked-off UGC iPhone footage. The man in the navy rash guard lies face down on the mat exactly as in the frame, completely spent: from the first frame his back rises and falls hard with deep, heavy breaths. Halfway through, without lifting his head, he slowly raises his <FREE HAND AS IN BASE> a little off the mat into a weak, shaky thumbs-up, holds it for a moment, then lets it drop back onto the mat. His face stays hidden the whole time. Ambient gym sound and his heavy breathing only, no words, no music. One take, no cuts, no zoom, no change of angle; keep his build, the clothing and the print exactly; the print and the SHIZEN lettering never redraw and move with his breathing back; no other text or logos.

**Retry slot** (if the hand is malformed twice): "he lifts his <FREE HAND> a few centimetres off the mat and lets it flop back down". This is the single change. Text 2 stays the same.

### QA (in addition to section 6)
- No face in any frame.
- The thumb and hand are anatomically correct at full frame rate, with 5 digits where visible.
- The print stays flat on the back through the breathing.

### Budget, day N
- **Submits:** still first, then the clip at least 20 minutes later, with 2 spare re-rolls. Hold if the still fails twice with the same card, because then the base is the problem.
- **No base, no post.** If no face-down frame passes, post nothing. Never re-use the old format to fill the day.

## 11. Claude's discovery pass for section 10 (20 Nov ~08:50; all candidates UNINSPECTED)
**Method:** web search plus YouTube oEmbed, which gives the title and channel only. No browser and no frames. YouTube watch pages and the transcript sites did not return descriptions, chapters or transcripts, so **no timestamps are given**. None of these IDs appears in the repo, but an ID's absence does NOT prove the room is unused: each candidate stays UNVERIFIED against the posted-scene grid until it is inspected. Nothing here is a pass. Instinct validates the pixels.

| # | URL | Title / channel (oEmbed) | Why it might hold the moment | Main risks |
|---|---|---|---|---|
| C1 | https://www.youtube.com/watch?v=obS70stuGls | "BJJ & MMA Yoga Cooldown - Prevent Future Injury" / Shapeshift Wellness | A cooldown follow-along: one presenter, static camera; child's pose and face-down rest are standard cooldown poses | Room may be a studio, not BJJ mats; camera may be frontal or side-on (P3) |
| C2 | https://www.youtube.com/watch?v=ctzrqCgIr2w | "BJJ Cooldown and Switch Off After Class Follow Along" / Yoga for BJJ | Same type; "switch off" suggests a lying rest section | Same as C1; the presenter is the channel's own known instructor (identity is fully replaced, but flag it) |
| C3 | https://www.youtube.com/watch?v=rehggq2V-TE | "No-Gi Open Mat" / Brazilian Jiu-Jitsu Team Malta | A real open-mat room; round ends produce face-down and seated rests | Crowds and pairs (S2) are likely; the camera may move |

**Where to look:**
- C1 and C2: the final third, where cooldowns usually end in child's pose and lying rests.
- C3: the seconds after each round ends.

These are search guidance only, not timestamps.

**Reserve, not ranked:** https://www.youtube.com/watch?v=hc7ZcgM9JWs ("5 stretches to do after BJJ training" / BeyondGrappling). The oEmbed size is 4:3, so check the native resolution against S5.

**Rejected at discovery:**
- _0Nq8YtJMzw, a Chewjitsu open mat: a known creator's room, crowded.
- Clavicular open-mat clips: a famous person.
- Am-pQ7jkVCI: a talking-head discussion.

### Pose variant added to the section 10 lead (this widens sourceability; same concept, same text, same payoff)
"you good?" also works with **P1-alt, a seated slump from behind**:
- He sits on the mat with his back to the camera, head hanging, shoulders rounded, solo, and one hand free on the mat or on his knee. The face and front stay hidden.
- Frame-0 motion: his shoulders heave with breathing. The payoff is the same weak thumbs-up raised beside him, without turning round.
- Card change, a single slot: the pose description and "He sits with his back to the camera, so the front of the shirt is not visible."
- The P2 to P6 fail rules apply, with P3 read as: back within about 30° of square to the camera.

**Gate unchanged:** no inspected base means no Flow and no post.

### Section 11 inspection results (Instinct, 20 Nov; sampled positions only, NOT whole-video rejections)
| # | Sampled at | Finding | Verdict at that position |
|---|---|---|---|
| C1 obS70stuGls | 2:00 | Front-facing presenter on a yoga mat at home; not a gym setting | Fail (S-setting, frontal) |
| C2 ctzrqCgIr2w | 0:12 | Frontal presenter on a yoga mat in a plain room | Fail (setting, frontal) |
| C3 rehggq2V-TE | 0:35 | Low-resolution contact pair on green mats; whole video only 50 s | Fail (S2, S5, S9) |
- The full fetched transcripts for C1 and C2 do not establish a prone or child's-pose ending.
- None of C1 to C3 is qualified footage. Do not re-propose them as candidates for this pose without new evidence.
- The seated-from-behind variant remains available, but it has no approved real source. No Flow until one passes.

## 12. SOURCING DIRECTION (Nic, 21 Nov 20:51; supersedes all stock work)
- **Sources are native short-form only:** YouTube Shorts or TikTok, from a genuinely new creator and room. NO Pexels or stock footage. The stock and locker-room leads from 21 Nov 20:38 were never committed and are dropped.
- **Exhausted, do not re-pool:** small-gym long-form open mats and end-of-round resets, solo drill and cooldown presenters, Artem Podrez's Pexels judo set (incl. 6253409).
- **Why short-form helps:** it is natively vertical (no 16:9 crop loss), filmed on phones (matches the realism method), and BJJ comedy and rest moments are a native genre there.
- **Exclude:** compilation and repost accounts (unclear provenance, mixed rooms), famous people, competition broadcasts, minors, and anything from a burned room.
- **All other rules unchanged:** the concept, the cards and the gates are in sections 0 to 10 (prone or seated slump from behind, "you good?", weak thumbs-up). Every visible person's whole identity and body is replaced even with the face hidden. No invented shirt front. No Flow or post until Instinct passes the pixels AND the room is checked against the posted-scene grid.

### Leads (Claude, 21 Nov ~21:00): METADATA ONLY, uninspected, no timestamps
TikTok pages and oEmbed are blocked to this workspace (robots), so the TikTok captions below come from search results only. The YouTube title and channel were confirmed by oEmbed.

| # | URL | Caption / title (as indexed) | Why | Risks to check |
|---|---|---|---|---|
| T1 | https://www.tiktok.com/@adamellisbjj/video/7351472910533397792 | "me after getting mauled at jiu-jitsu for 2 hours #Meme #MemeCut #CapCut ..." | A self-filmed exhaustion meme from a BJJ creator: the exact feeling | A meme-template cut may not be his own gym footage; frontal |
| T2 | https://www.tiktok.com/@fenomfighter/video/7539664085353270541 | "this isn't the open mat I signed up for 🙂‍↔️ #fyp #foryou #brazilianjiujitsu #bjj #nogi" | A native no-gi open-mat creator; the rough-roll aftermath genre | Pairs or contact; the creator's face |
| T3 | https://www.tiktok.com/@kieren_jiujitsu/video/7200830809790582018 | "\"Just roll more bro…\" #bjj #jiujitsu #jiujitsuworkout ..." (tags @jordanteachesjiujitsu) | Conditioning or comedy that may show a spent athlete on the mat | Active drilling; second person |
| Y1 | https://www.youtube.com/shorts/UIWlYICpTgg | "The Worst Jiu Jitsu Round #SHORTS" / Justin Lesko (vertical 9:16 per oEmbed) | A bad-round Short; the defeated end state may be on screen | Pair in contact; creator recognisability |

**In-app search angles for Instinct** (TikTok and YouTube Shorts search, sorted by recent, small creators):
- "me after open mat"
- "pov light roll"
- "last round bjj"
- "when coach says one more round"
- "white belt first class"
- "bjj cardio check"
- "gassed bjj"
- "#bjjmeme exhausted"
- "after comp class"
- "dead after drilling"

What to look for: the seconds after a round ends, filmed by a friend or a tripod phone, where one person drops face down or slumps seated with his back to the phone.

**Decision:** inspect T1, T2, T3 and Y1, then the search angles. The first frame that passes S1 to S9 and P1 to P6 (or P1-alt) and the room check becomes the base for "you good?". If none passes, no generation and no post.

## 13. Screenshot-led selection loop (21 Nov 21:06)
**Loop:**
1. Instinct searches YouTube Shorts and screenshots the result grid.
2. Claude ranks the actual thumbnails: open, or skip with a reason.
3. Instinct opens the picks and inspects the pixels.
4. Instinct reports pass or fail at the observed positions.

Claude never infers a pose from a title (Y1 lesson below).

**Thumbnail triage.** Open only if ALL of these hold:
- Real phone footage: not animation, not green-screen, not a compilation.
- No gi.
- One adult on or near the floor (lying, kneeling, slumped) or alone in a clean room.
- No overlay text covering the body.

Skip:
- frontal talking heads;
- pairs in contact;
- belt ceremonies;
- cartoons;
- green-screen memes;
- ads.

**Scrubbing tip:** open a Short as https://www.youtube.com/watch?v=<ID> for a normal player. When paused, the , and . keys step one frame at a time, so exact timestamps can be read.

### Grid 1: "me after open mat #shorts" (Instinct screenshot, left to right)
| Rank | URL | Thumbnail (as seen) | Call |
|---|---|---|---|
| 1 OPEN | https://www.youtube.com/shorts/jK81lNhqObs | "Training for open mat..." One adult man in an orange tee, collapsed/kneeling forward on the floor, head down, solo; side view | Best visible solo exhaustion pose. Risks: a weights-gym floor (racks), not BJJ mats; side angle; overlay text above him. If it passes, the setting line in the card changes to the gym floor, and the joke stays BJJ ("training for open mat") |
| 2 OPEN | https://www.youtube.com/shorts/ZVk7thspM7A | "You don't know how hard you trained on Open Mat?" One no-gi man in a clean grey-mat room, frontal, holding a rash guard | A comedy skit in a clean solo room. Check later frames for a collapse or lying-down beat. The thumbnail itself fails (frontal, face, a real rash guard brand on show) |
| skip | https://www.youtube.com/shorts/0zFULJ-oNiI | Coach and student in gi, belt ceremony | Gi, pair, faces |
| skip | https://www.youtube.com/shorts/1HcGI52atRw | Green-screen creator over a gi sparring clip | Meme overlay; pair in gi |
| skip | https://www.youtube.com/shorts/SImsaBZCNQg | Animated cartoon | Not real footage |

**Next queries if both fail** (Shorts chip on; screenshot each grid):
- "gassed after rolling #shorts"
- "last round bjj #shorts"
- "nogi open mat pov #shorts"
- "bjj conditioning finisher #shorts"
- "me after bjj class #shorts"
- "after rolling with the blue belt #shorts"

### Inspected and logged
- Y1 UIWlYICpTgg: a six-second frontal gi talking-head joke. No usable back or rest pose.

### TikTok status
- The first search ("bjj after training") returned no results and showed a phrase-level guidelines notice. That route is stopped and has been reported to Nic. The notice is not evidence of an account strike.
- Do not rephrase searches to get around the notice. TikTok search stays paused until Nic decides.
- YouTube Shorts is the active route.

Gate unchanged: no passed source means no Flow and no post.

## 14. Inspected failures and PIVOT (21 Nov 21:18)
### Grid 1 picks, inspected by Instinct (sampled positions only, NOT whole-video claims)
- **jK81lNhqObs** (13 s): a weights-gym cable exercise. The adult lies on his side with his face and front visible. It is not the kneeling collapse the thumbnail suggested. Fail.
- **ZVk7thspM7A** (14.5 s): a frontal standing man holding branded clothing. The opening, middle and end samples showed no rear or rest pose. Fail.

### Grid 2: "last round bjj #shorts" (Shorts chip). All 10 skipped
Most results are competition or broadcast clips (boxing, UFC, ONE, an outdoor cage), talking heads, or pairs in scrambles. None shows a solo rest pose. No pick.

### Decision: drop the solo-exhaustion pose; pivot to footage native Shorts actually contain
Two days of real grids show the solo face-down or seated-from-behind rest almost never appears in native short-form. **Tripod-filmed no-gi pair rolls are the most common native BJJ footage.** The new concept is built on those.

**Concept: "let's go light" (pair, tap payoff)**
- **Shot:** one real frame of a no-gi pair in a static top position: mount, knee-on-belly, or top of closed guard. The camera is BEHIND the top man, so his back and print face the camera and his front is pressed against his partner (the front stays hidden).
- **Frame-0 motion:** the top man is already shifting his weight and adjusting grips.
- **Text 1 (0 to ~2.3 s):** "him before every round: \"let's go light\"".
- **Payoff (~3 to 4 s, a visible human action, not a print reveal):** the partner underneath taps fast, three quick slaps on the top man's shoulder or the mat. Text 2: "the light round:".
- **End:** the top man pats the mat once and holds. Loops.
- **Caption:** who's the guy at your gym who says "let's go light" every time? 🐉 #bjj #nogi #rashguard #nogibjj #bjjhumor
- **Design and budget:** Ryu (navy). 1 still + 1 clip (6 s), 2 spare.
- **Change vs P12 to P14:**
  - two people, not one;
  - frame-0 motion;
  - the payoff is the partner's action;
  - the camera relationship is a static top position seen from behind;
  - the old format is not reused.

**Source fail conditions for the pair** (S1, S3, S5 to S8 still apply; this replaces S2 and S9 for this concept). Reject if:

| # | Reject if |
|---|---|
| G1 | There are not exactly two adults, or any third person, limb or reflection is in the crop |
| G2 | The top man's back is not square to the camera (within about 30°), or his back is covered by the partner's legs or arms over more than about a third of the print area |
| G3 | The pair is scrambling or in transition. Only a held, static top position passes |
| G4 | Either person wears a gi |
| G5 | Neither of the bottom man's hands is free to tap |
| G6 | Competition or broadcast footage, a crowd, a referee or event branding |

**Identity:** BOTH people are fully replaced. The top man is L1 (section 3), in the navy GARMENT block. FRONT CLAUSE: "His chest is pressed down onto his partner, so the front of the shirt is not visible." The partner, exact words:
> a completely different, clearly adult man in his late twenties: medium-light skin, short black curly hair, clean-shaven, a different face shape, nose, ears, neck and jawline from the original; athletic build; wearing a plain heather-grey short-sleeve t-shirt and plain black shorts, no logos or writing

Both faces are checked at 4x against the source.

**Motion card core:**

Static locked-off tripod phone footage of a no-gi roll. The man in the navy rash guard holds top position with his back to the camera, shifting his weight and adjusting his grip from the first frame. After about three seconds the man underneath taps fast three times on his shoulder with his free hand; the man on top stops, pats the mat once and holds still. Ambient gym sound and breathing only, no words, no music. One take, no cuts, no zoom; keep both men's identities, the clothing and the print exactly; the print and the SHIZEN lettering never redraw; no other text or logos.

**Next query** (YouTube Shorts, Shorts chip on): "nogi roll tripod #shorts". If thin, try "nogi sparring white belt #shorts" and "nogi rolling footage #shorts".
- Open only thumbnails showing two no-gi adults on gym mats, filmed from a static side or rear camera, with no crowd and no event branding.
- The first frame that passes G1 to G6 and the room check becomes the base.

Gate unchanged: no passed source means no Flow and no post. TikTok search stays paused pending Nic.

### Grid 3: "nogi roll tripod #shorts" (Shorts chip, 21 Nov 21:27)
"tripod" pulled the technique meaning (tripod sweep and pass instructionals), not tripod-camera rolls. That was Claude's query error.

- **Open 1, low confidence:** top-left, "No-Gi Tripod Passing #bjj #brazilianjiujitsu #jiujitsu" (1.7k views). Two no-gi adults in a clean room. The top man is bent over his passing partner, with his back toward a high camera.
  - Check whether the pass holds still for about 2 s (G3), whether the back is near square to the camera (G2), and whether the bottom man has a free hand (G5).
  - The burned-in overlay text is heavy, so check whether a clean crop exists.
  - The URL is not visible in the screenshot. Instinct copies it from the grid.
- **Skip the other 9:**
  - gi: knee bar, both "Tripod sweep when they stand up" clips, "2 on 1 standing";
  - standing or scramble drills: De La Riva, Berimbolo, the Geno Morelli cartwheel (a known athlete);
  - frontal or close talking-instruction thumbnails: "Tripod to foot lock", "Learn the tripod sweep", "Fix your tripod pass".

**Corrected next query** (one only): "nogi mount #shorts". Instructional mount clips show a HELD top position on a static camera in a clean, often empty room, which is exactly G3. Open thumbnails where the top man's back faces the camera.

### Grid 3 pick inspected (Instinct, sampled positions only)
- **sszcqJZdN6I** ("No-Gi Tripod Passing"; 23.901 s, 720x1280). The overlay disappears during playback, but the samples show an inverted tripod pass: the top man's head is on the mat and his back is strongly foreshortened, then frontal passing movement. No held upright or chest-down rear-facing top position at the samples. Fail (G2, G3).

### Grid 4: "nogi mount #shorts" (Shorts chip, 21 Nov 21:37)
- **Open 1:** bottom row, far right, "Omoplata from mount 🥋 #shorts #bjj #bjjhighlights". On blue puzzle mats, a no-gi top man in red is in mount, seen from behind and above, with his back toward the camera. It is the only thumbnail with the top man's back facing the camera at a usable size.
  - Check for HELD mount frames before the omoplata transition (G3, about 2 s or more), a back near square (G2), no third person (G1), a free bottom hand (G5), and adults only (S3).
- **Open 2, low confidence:** bottom row, near right, "Live rolling triangle from the mount position! #shorts". A small pair on red mats with a high camera.
  - Likely fail: the subjects look small (S5: the crop must be at least 600x1066 real pixels), and live rolling may never hold still (G3). Open it only to find a held mount frame at a larger scale.
- **Skip:**
  - Top row, second, "No-Gi Armbar From Mount x Nicky Ryan | B-Team": the rear-facing top man is promising, but it is a famous athlete, a highly recognisable gym, split-screen, and has background people.
  - Craig Jones / B-Team (two clips): famous, split-screen.
  - Kimura from side mount and "Submit from mount like a pro": the top man's front and face are toward the camera.
  - The Ezekiel, armbar and "S mount subs" clips: close frontal or talking.
- **If both fail, next query:** "nogi mount escape drill #shorts". Escape drills hold the mount on a static camera, the top man is often shot from behind so the escaping partner is visible, and the clips are usually two-person gym content, not famous-athlete compilations.

### Grid 4 picks inspected (Instinct, sampled positions only)
- **yG7LmsaYIJc** ("Omoplata from mount"): the opening shows the red-shirt man's FRONT and chest toward the camera, not his back, and there are wall photos above. Fail (G2, S7).
- **UejUvF67Pfs** ("Live rolling triangle from the mount position"), at about 5 s: a tiny foreshortened pair on a large red mat. A large-body crop is far below 600x1066 real pixels. Fail (S5).

### Grid 5: "nogi mount escape drill #shorts" (Shorts chip, 21 Nov 21:49)
- **Open 1:** top row, second, "EASY BJJ Mount Escape #bjj #grappling" (403k views). No-gi, grey mats. The top man in a black rash guard is in mount, seen from the side and behind, with his back partly toward the camera.
  - Check for held mount frames before the bridge (G3), whether his back can be near square (it looks about 45° in the thumbnail, so G2 is a risk), a visible brand logo on his shirt (it is replaced, but note it), a free bottom hand (G5), and no third person (G1).
- **Open 2, low confidence:** top row, middle, "3 options to get out of mount ! BJJ". A no-gi pair in mount on grey mats.
  - Risks: a large gym wall logo (S7; check whether a crop clears it) and a side-on top man (G2).
- **Skip:**
  - gi: the Upa partner drill, "The best mount escape";
  - a child: "Mount Escape Countered", so S3;
  - famous: Craig Jones S-mount;
  - the top man faces the camera (front shown): "This mount escape is so easy", "This is all I've been using";
  - close crops with no readable back: "Realistic mount escape", "MUST KNOW Mount escape".

### Widening the pair concept: front-safe poses that native footage actually shows
Rear-facing top mount is scarce, so the "let's go light" tap concept now accepts any HELD two-person position where OUR man's back faces the camera and his front is hidden.
- **(a) Top mount or top position, from behind.** Unchanged.
- **(b) Our man TURTLED,** on knees and elbows with his back up and face down. The partner is beside him or at his head, NOT lying across the print.
  - Text 1: "him: \"let's go light\"". The payoff is our man tapping the mat fast three times.
  - It is the same joke, told from the victim's side.
- **(c) Our man behind a seated partner** (a back take), with the camera behind our man.

The G1 to G6 rules apply; the print must be at least two-thirds unobstructed. Both identities are fully replaced. The FRONT CLAUSE for (b): "He is on his knees and elbows facing the mat, so the front of the shirt is not visible."

**Next query if grid 5 fails:** "nogi turtle drill #shorts". Turtle attack and escape instructionals hold the turtle still on a static camera, and the turtled man's back faces up or toward the camera by design.

### Grid 5 picks inspected (Instinct, sampled positions only)
- **9g26jnF_pzw** ("EASY BJJ Mount Escape"; 29.941 s, 720x1280), at about 19 s: the top man is side-on and substantially clipped by the right frame edge, the bottom partner's hand is over his back, and there is a large title above. Fail (G2, G1-complete pair).
- **2LJnu1lo-y4** ("3 options to get out of mount"), sample: the top man's side and a foreshortened back under a huge wall logo. Fail (G2, S7).

### Grid 6: "nogi turtle drill #shorts" (Shorts chip, 21 Nov 21:58). The last grid of the 21 Nov pass
URLs are not visible in the screenshot. Instinct copies them from the grid.
- **Open 1:** top row, middle, "How to attack a tight turtle guard #bjj #jiujitsu #mma ..." (166k views). On blue mats, a man in a plain grey tee is TURTLED with his back up and face down; the attacker kneels at his side. This is pose (b).
  - Check that the turtled man's back stays readable and at least two-thirds uncovered by the attacker's arm (G2), and that the position holds (G3).
  - Framed portrait photos on the wall must be croppable (S7), with no third person (G1).
- **Open 2:** bottom row, middle, "Turtle Drill || Follow me for more #jiujitsu techniques ..." A SOLO man on hands and knees, face down, on grey mats; there is a gym logo and timer at the top.
  - If his back reads square from above or behind, this is a solo base for the section 10 "you good?" concept (frame-0 breathing, weak thumbs-up), not the pair tap.
  - Check whether a crop clears the logo and timer (S7), the back angle (P3) and a free hand (P5).
- **Skip:**
  - first two cards: an ad overlay;
  - 10th Planet truck entry: wide, crowd, logo;
  - leg lock from turtle and the NoGi chokes close-up: gi;
  - the turtle-escape arrow clip: possible minor, overlay;
  - armbar entry: the top man faces the camera;
  - Kimura trap: overlay, background faces.

### NEXT ACTION if both fail: pivot the format, not the pose query
**"The demo dummy"** is built on the most common native footage we have seen all night: an instructor FACES the camera and demonstrates on a partner whose BACK is to the camera. Our man is that partner.
- **Base:** a held standing or kneeling demo position (front headlock, a standing guillotine grip, collar tie) with the partner's back square to a static camera. The instructor is fully replaced, in a plain heather-grey tee (PARTNER identity, section 14).
- **Text 1 (0 to ~2.3 s):** "coach: \"can i borrow you for a sec\"". The frame-0 motion is the instructor adjusting his grip.
- **Payoff:** our man taps fast on the instructor's thigh or arm (a visible action). Text 2: "me, every single class:".
- **Caption:** who's the demo dummy at your gym? 🐉 #bjj #nogi #rashguard #nogibjj #bjjhumor
- **Front stays hidden:** he faces the instructor, not the camera. The print is on his back, readable for the whole clip.
- **Fail rules:** G1, G3, G4, G6 and S1 to S8 apply. G2 here means our man's back is within about 30° of square and at least two-thirds unobstructed.
- **Query:** "front headlock nogi #shorts".

## 15. Batch review 1 (Instinct's 30 playing-video samples, 21 Nov 22:31). Workflow from here: Instinct frame-searches in batches; Claude returns APPROVE, DEEPER SAMPLE or REJECT per sample
Concept under review: "demo dummy" (section 14 pivot). Each verdict concerns ONLY the sampled frame shown. Nothing here is a whole-video rejection.

**APPROVE: none.** No sample shows a partner's back square to the camera, at least two-thirds unobstructed, with exactly two adults and a clean crop at 600x1066 or more.

**DEEPER SAMPLE (2):**
- **16, SEM3NBhV3gc.** The partner in the white tee is bent forward with a large rear torso near square to the camera, and the back looks mostly unobstructed.
  - Find a held frame where his back from collar to waist is in frame and at least two-thirds clear of the other man's arm (G2).
  - Check that nothing beyond the two men is visible (G1), that there is no motion blur (S5), and whether the warehouse-style room shows posted-room features (S1).
- **30, zFgepT2x77I.** The man in the navy top has a large rear torso toward the camera.
  - Find a frame without the burned-in caption over his back (S6) where the seated person at the left edge can be cropped out (G1).
  - Confirm the TikTok watermark is the uploader's own cross-post, not a repost (the provenance exclusion).
  - Check for wall banner lettering (S7).

**REJECT (28), pixel reasons at the sample:**
| # | Reason |
|---|---|
| 01 | Single man side-on on all fours, face visible, large caption over the frame (G2, S6) |
| 02 | Kneeling partner's back angled and covered by the instructor's arm; young-looking pair (S3 risk); USA Wrestling wall branding (S7) |
| 03 | End card at this instant, no footage |
| 04 | Close crop on the ground; arms across the top man's back; bottom man's face (G2) |
| 05 | Heavy motion blur; background person (S5, G1) |
| 06 | Low resolution and blur (S5) |
| 07 | Kneeling partner angled; background people at left and right (G1, G2) |
| 08 | Talking head (no pair) |
| 09 | Lift in motion, side-on (G3, G2) |
| 10 | Both men frontal or side; cage and caption (G2, S7) |
| 11 | Partner side-on on his knees; caption (G2) |
| 12 | Split screen: the pane is too small for a 600x1066 crop; background people (S5, G1) |
| 13 | Both standing side-on; captions (G2) |
| 14 | UFC broadcast (G6) |
| 15 | Both bent in profile; no square back (G2) |
| 17 | Inset talking head (split); young-looking wrestlers (S3 risk) |
| 18 | Blur and overlay (S5, S6) |
| 19 | Partner bent side-on; overlay text (G2) |
| 20 | Letterboxed; large gym logo wall; partner at about 45° (S7, G2) |
| 21 | Gi (G4) |
| 22 | Side views; OpusClip watermark; red wall logo (G2, S7) |
| 23 | Frontal faces; large wall letters (G2, S7) |
| 24 | Floor academy lettering; both at an angle (S7, G2) |
| 25 | Close frontal; third person at bottom right (G1) |
| 26 | UFC broadcast (G6) |
| 27 | Small figures, side-on (S5, G2) |
| 28 | Gi (G4) |
| 29 | Gi (G4) |

**Pattern for the widened search:** in instructionals, the partner usually stands SIDE-on to the camera so viewers see the grip. Square backs appear when the camera is behind the partner, typically:
- front headlocks or snap-downs filmed from the partner's side of the room;
- collar-tie hand-fighting where the instructor faces the lens;
- seated or kneeling partners in a "listen to coach" setup.

Prioritise clips where the instructor talks to the camera OVER the partner's shoulder.

### Batch 1 deeper samples (Instinct; sampled moments only)
- **16, SEM3NBhV3gc** at 2.395, 7.395 and 12.395 s: front and side close-ups, and the pair is clipped. No pass.
- **30, zFgepT2x77I** at the sampled moment: a caption crosses the torso and there is a background person. No pass.

## 16. Batch review 2 (samples 31 to 59, 21 Nov 22:53)
**PASS: none.**

**DEEPER SAMPLE (3):**
- **37, YYsbMMBe3b8.** The partner in the blue tee is in a collar tie with his back to the camera: a broad clear back with the front hidden. This is the best geometry so far.
  - Find a moment with no third person (G1) where his whole back from collar to waist is inside the native frame (no edge crop).
  - The burned caption ("So I push, he pushes back") must sit above his shoulders or be absent (S6).
  - Check the instructor's free hand for the tap payoff (G5).
- **31, h4Q88EoBZeM.** The man in the navy long-sleeve top is in a collar tie with his back toward the camera, against a plain white wall on grey mats, with no visible third person.
  - Settle whether his back gets within about 30° of square (it looks about 35 to 40° at the sample) (G2).
  - Check whether the partner's forearm over his neck leaves at least two-thirds of the print area clear (G2).
  - Check whether his left side is clipped by the frame edge.
- **40, WhMp7RUo6AE.** A shirtless man with a large back near square to the camera. The source being shirtless is fine, because the whole body and clothing are replaced.
  - Find a HELD tie before the arm drag with no motion blur (G3, S5).
  - His head must be inside the frame, the "#3 Right arm drags..." caption must be clear of his back (S6), and the partner's hand must be visible for the tap (G5).

**REJECT, at the sample:**
| # | Reason |
|---|---|
| 32 | Frontal, overlay, cage |
| 33 | Close ground crop, faces |
| 34 | Profile, wall logo, overlays |
| 35 | One distant figure, dragon logo wall |
| 36 | Single frontal, overlay |
| 38 | Turtled man faces the camera, top man over his back |
| 39 | Both in profile, small, floor logo |
| 41 | Small, motion |
| 42 | Profile, child crowd in background (S3, G1) |
| 43 | Close, partner side-on, captions |
| 44 | BADGERS banner, kneeling side-on |
| 45 | Third and fourth people |
| 46 | Close, frontal |
| 47 | Close crop, flag |
| 48 | Profiles, floor lettering |
| 49 | Small scramble |
| 50 | Apart and frontal, wall lettering |
| 51 | Blurred scramble |
| 52 | Single frontal, background person |
| 53 | Letterboxed desktop capture |
| 54 | Gi |
| 55 | Partner side-on, captions |
| 56 | Gi |
| 57 | Split screen |
| 58 | UFC repost |
| 59 | Partner side-on, caption |

**If 37 passes:** the demo-dummy card stays. The blue-tee partner becomes L1 in navy Ryu with the FRONT CLAUSE "He faces his partner, so the front of the shirt is not visible." The instructor becomes PARTNER (grey tee), and the tap is on the instructor's arm or shoulder.

### Batch 2 deeper samples (Instinct; sampled moments only)
- **31, h4Q88EoBZeM** at 0, ~2.8 and ~5 s: front or oblique, and the pair is edge-clipped. No pass.
- **37, YYsbMMBe3b8** at additional samples: a third person, or the instructor clipped. No pass.
- **40, WhMp7RUo6AE** at 0, 5, 10 and 15 s: clipped, oblique or front. No pass.

## 17. Batch review 3 (samples 60 to 89, 21 Nov 23:10)
**PASS: none. DEEPER: none.**

| # | Reason at sample |
|---|---|
| 60 | Bodylocking man faces the camera, headgear |
| 61 | Frontal |
| 62 | Frontal, background people |
| 63 | Letterboxed desktop capture |
| 64 | Distant pair (S5) |
| 65 | Blur |
| 66 | Overhead blur |
| 67 | Oblique or frontal |
| 68 | Gi |
| 69 | Frontal at the sample; a later reverse angle cannot be inferred |
| 70 | Back about 40° oblique, wall mural logo, partner in gi trousers, head at the left edge (G2, S7, G4, G1) |
| 71 | Blurred scramble |
| 72 | Side-on |
| 73 | Small, overlay, wall logo |
| 74 | Distant |
| 75 | Frontal or side |
| 76 | Broad rear torso, but a ground transition, and letterboxing leaves under 1066 px of usable height (G3, S5) |
| 77 | Frontal |
| 78 | Competition close-up |
| 79 | Dark overlay, faces |
| 80 | Subject clipped, mural |
| 81 | Side, overlay |
| 82 | Backs oblique, seated crowd at right (G1) |
| 83 | Crowd |
| 84 | Gi |
| 85 | Crowd |
| 86 | Several people, ad overlay |
| 87 | Seated frontal, flag and logo |
| 88 | Competition plus inset face |
| 89 | Partner about 45 to 60° oblique, wall logo (G2) |

### What 89 samples show
- Instructional and demo Shorts are framed for the instructor's front. The partner stands side-on BY DESIGN, so the viewer sees the grip.
- The closest frames (31, 37, 40, 70, 76, 82, 89) all have the back-facing man at 35 to 60°, or are clipped, crowded or in transition. The demo-partner geometry does not occur cleanly in this footage type.
- Readability (at least two-thirds of the print, back within about 30°) is NOT relaxed.

### Concept and footage change: "any questions?" (seated student, from behind)
Footage where the camera is naturally behind someone: **class and seminar Shorts filmed from the back of the room.** Students sit on the mat facing the instructor, so their backs face the camera square-on, and the front is hidden by geometry.
- **Base:** one seated adult student, back square to the camera. The other students are croppable, so the crop holds our man plus at most the instructor in the distance. Every visible person is fully replaced: the instructor is PARTNER (grey tee).
- **Text 1 (0 to ~2.3 s):** "coach: \"any questions before we roll?\"" The frame-0 motion is the instructor gesturing and our man's breathing and shifting.
- **Payoff (visible action):** our man slowly raises one hand. Text 2: "\"can we go light\"". This keeps the running "light round" voice.
- **Caption:** what's the one question you always ask before rounds? 🐉 #bjj #nogi #rashguard #nogibjj #bjjhumor
- **Budget:** 1 still + 1 clip (6 s), 2 spare. The hand raise is low motion; arms and sleeves need clip QA.
- **Fail rules:**
  - S1 and S3 to S8;
  - P3 read as back within about 30° of square, with at least two-thirds of the print area clear;
  - croppable to him plus at most one replaced instructor, nobody else (G1);
  - his hands visible and free (P5).
- **FRONT CLAUSE:** "He sits facing away from the camera, so the front of the shirt is not visible."
- **Search terms for Instinct:** class or seminar Shorts showing students seated on the mat from behind, e.g. "bjj seminar #shorts", "jiu jitsu class technique explanation #shorts", "open mat announcements #shorts".

## 18. Batch review 4: seminar samples 90 to 119 (21 Nov 23:44)
**DEEPER: NONE.** 115 is excluded (loading overlay).

The near-misses, with their reasons at the sample:

| # | Reason |
|---|---|
| 119 | Closest. The seated foreground adult is about 45° oblique and cropped at the frame edge, and his hands are unclear (P3, P5) |
| 92 | Only the head and shoulders of a standing filmer holding a phone, with a crowd ahead (G1) |
| 100 | The top man's back is oblique and cropped at the top, with a gradient overlay at the bottom (G2, S6) |
| 98, 99, 102 | Seated people are small or at the frame edge, with crowds (S5, G1) |

The other samples fail on gi, a frontal view, crowds, lettering or competition.

**Pattern:** seminar clips are filmed by a STANDING person at the side, so seated backs in the foreground come out oblique and edge-cropped.

**Adjustment for the next search:** target clips filmed from a SEATED position inside the class, such as "pov bjj seminar #shorts", "pov listening to coach #shorts" and "pov first bjj class #shorts". The filmer then sits behind another student, which gives a close, square back. Look for one foreground seated adult whose back fills at least 40% of the frame height, at least two-thirds clear, with both hands visible.

## 19. SOURCE-GEOMETRY APPROVAL (conditional): _y8kzrk4UI8 at 29.3905 s (22 Nov 01:48)
**Frame:** https://www.youtube.com/shorts/_y8kzrk4UI8 at 29.3905 s, native 720x1280, unedited (Instinct's capture).

**Verdict: APPROVED as source geometry, conditional on C1 to C3 below.** This is the first frame in about 120 samples to pass the core checks:
- **G2:** the foreground man's back is about 10 to 15° off square, collar to waist fully in frame and fully unobstructed. Front hidden.
- **G1:** exactly two adults, with no third person, reflection or caption at this moment.
- **P5:** both of his hands are visible.
- **S5:** the full native 720x1280 frame is used, with no crop.
- **Not in contact:** the men stand about 1.5 m apart, facing each other before a roll.

**Conditions before any submit:**
- **C1 (Instinct):** the room (white padded walls, dark grey mats, round club logo) checked against every posted video on the grid. If it matches any posted room, it fails.
- **C2:** the top-left club logo is removed in the still. It is the single background change, the wall there is flat, and it is the only lettering.
- **C3:** the foreground white gi trousers and the blue belt end are replaced in the still. The rash guard's small collar mark is covered by our wordmark area.

**Concept change:** no grip and no contact means the demo-dummy tap cannot be shown without generating an approach, which is too much motion. So the concept is the stance reversal this geometry already supports: **"light roll?"**
- **Frame 0 (motion):** our man (back to the camera, navy Ryu) lifts his right hand toward the other man for the friendly slap-and-bump. Text 1 (0 to ~2.4 s): "me: \"light roll?\"".
- **Payoff (~2.6 s, a visible human action):** the other man looks at the hand, ignores it, and slowly sinks into a low, unsmiling wrestling stance with his hands up. Text 2: "him:". Our man slowly lowers his hand. Loops at ~6 s.
- **Caption:** said light. meant 100% 🐉 who's this guy at your gym? #bjj #nogi #rashguard #nogibjj #bjjhumor
- **Change vs P12 to P14:** two people; frame-0 motion; the payoff is the other man's action; this is a new room (pending C1).

### Still card (image 1 = brand/print-backs/Ryu_back.jpg; image 2 = the full native frame, no crop)
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, framing, camera height, the room, both men's positions and poses, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
The man nearest the camera, with his back to us, keeps his exact pose (standing, facing the other man, arms hanging loosely at his sides) and becomes [L1]. He wears a navy LONG-SLEEVE rash guard, the same navy as the background of image 1, with a crew neck and plain navy sleeves all the way down to his wrists, no logo on the shoulder and no print, logo or writing on the sleeves. He faces the other man, so the front of the shirt is not visible. On his back, the artwork from image 1 printed large exactly as drawn, centred on his spine. Above it, centred just below the collar, the gold yin-yang circle and the word SHIZEN, copied exactly from image 1 at the same small size and in the same thin letters. Instead of the white trousers and belt he wears plain black loose grappling trousers, no belt and no drawstring showing.
The other man, facing the camera, keeps his exact pose and becomes a completely different, clearly adult man in his late twenties: medium-light skin, short black curly hair, clean-shaven, a different face shape, nose, ears, neck and jawline from the original; athletic build; wearing a plain charcoal long-sleeve rash guard with no logos, panels or writing, and plain black shorts.
The round logo at the top left of the wall becomes plain white wall like the rest of it. Nothing else changes: the white padded wall and the dark grey mats. No text, logos or writing anywhere except the SHIZEN mark on the print. Neither man keeps his original face, and no face from image 2 may appear on anyone.

**Retry slots (change one per retry):**
1. The trousers become "plain black shorts over plain black leggings" if the loose trousers render as a gi.
2. The logo line is moved to an edit-stage flat-wall patch: the camera is static, so a fixed mask over plain wall works.

### Motion card (Omni 1.1 Flash, 720p, 6 s)
Static locked-off phone footage of two men facing each other on the mat before a roll. From the first frame the man nearest the camera, back to the camera in the navy rash guard, lifts his right hand toward the other man for a friendly slap-and-bump and holds it out. The other man glances at the hand, does not take it, and slowly sinks into a low, serious wrestling stance, hands up, eyes locked, unsmiling. The man nearest the camera slowly lowers his hand. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; the man nearest the camera never turns round; keep both men's identities, the clothing and the print exactly; the print and the SHIZEN lettering never redraw; no other text or logos.

### Still QA additions (beyond section 6)
- The foreground man's face is never visible.
- The other man's face differs from the source man's face at 4x.
- The wall logo is fully gone, with no ghosting.
- No gi look on the trousers; no belt end.
- Long sleeves end cleanly at the wrists; hands have 5 digits.
- The collar mark is gone.
- The print is at least two-thirds readable.

**Clip risk:** the stance drop is moderate whole-body motion for the other man. It must stay slow, with feet planted, no sliding and no face drift.

**Edit:** text sits in the clear wall area and must not cover either head. Check the TikTok safe zone.

**Budget (a production day, not tonight):** still at submit 1 (a re-roll at submit 2 if needed, one slot changed), clip at least 20 minutes after the passed still, 1 to 2 spare. A failed take is never posted.

## 20. "light roll?" still 1 QA (submit 1, 22 Nov 08:40; Instinct's QA 08:43)
- **C1 cleared (Instinct):** no room match across all 18 live TikTok posts, the 23 archived queue sequences, the earn-the-back v4 and the removed 4 Nov v1.
- **Submit:** section 19 card unchanged, with L1 expanded. Image 1 = Ryu_back.jpg (190359 B), image 2 = the full native frame (644655 B), no crop. Nano Banana 2.1, 9:16, x1, 0 credits. Output 768x1376.

**Claude's check:** a source/still 50% blend overlay; Ryu_back.jpg beside the still's back crop; 3x hand crops. Scratch files only.

| Gate | Result | Evidence |
|---|---|---|
| Camera and room preserved | PASS | In the blend, the wall-pad top line, panel joints and mat seams align |
| **Pose, position, scale (both men)** | **FAIL** | The foreground man was RESTAGED: his head moved about 120 px right, his body rotated from a slight forward-left lean to upright and square, and he was shrunk so both feet fit (in the source, his right foot is cut off at the bottom edge). The partner moved up and back and was redrawn in a ready crouch. This is the P8/P11 restaging pattern, not the expected silhouette change from new clothing |
| Foreground identity replaced | PASS | Fade and beard; no source features; face not shown (cheek and beard edge only) |
| Partner identity replaced | PASS | 4x: clearly a different face, hair and jaw |
| Exact Ryu art | PASS | Dragon composition, head, horns, claws, coils and tail match the print file; centred on the spine; only minor line redraw |
| Neck mark | PASS | Small gold yin-yang above thin serif SHIZEN, centred under the collar, same small size |
| Sleeves and collar | PASS | Long plain navy sleeves to the wrists, crew neck, raglan seams (consistent with brand files) |
| Front hidden | PASS | Back view only |
| Trousers | Borderline PASS | Black loose heavy-cotton trousers, close to black gi trousers, but no belt and no gi top. Not chosen as the retry slot |
| Hands | PASS | Foreground: both hands natural, 5 digits. Partner: right hand natural; left hand partly hidden, plausible |
| Logo, collar mark, belt removed; no other text | PASS | No ghosting |
| Grain | Note | Sharper than the source; degrade in the edit, keep the raw master |

**Verdict: FAIL** on pose and position only. Do not submit motion from still 1.

### Retry (submit 2, from 09:00): change ONE slot, the pose slot. All other words stay identical
Replace "keeps his exact pose (standing, facing the other man, arms hanging loosely at his sides)" with:

"keeps his exact position, size and pose from image 2: his head at the same place against the wall, leaning slightly forward toward the other man with his shoulders angled a little to the left, his left arm hanging forward, his right arm hanging by his side, and his right foot reaching the bottom edge of the frame and cut off by it"

Replace "The other man, facing the camera, keeps his exact pose" with:

"The other man, facing the camera, keeps his exact position, size and pose from image 2: standing slightly hunched with his head tilted down, looking at the floor in front of the man nearest the camera, both hands low in front of his thighs,"

QA on still 2 repeats the blend overlay: both men's heads, shoulders and feet must sit within a few pixels of the source.

## 21. Still 2 QA (submit 2, 22 Nov 09:04:59; same art and native frame, only the section 20 pose replacements)
**Overlay check** (Instinct's 50% blend; the result was resized to 720x1280):
- **Our man:** his head is about 60 to 70 px right of the source (about 9% of the width). His shoulder line is shifted about 70 to 80 px right and is narrower. He is still more upright than the source's forward-left lean, and his left arm sits right of the source.
- **Partner:** his head sits about 20 px lower; the rest of his body is close.
- Closer than still 1, but NOT within the gate.

| Gate | Result |
|---|---|
| Camera and room preserved | PASS |
| **Pose, position, scale** | **FAIL** (our man translated, narrowed and straightened; partner head lower) |
| Identities replaced (our man's face not shown; partner differs at a glance, matching still 1) | PASS |
| Exact Ryu art and neck mark | PASS (same quality as still 1) |
| Sleeves, collar, front hidden, trousers, hands, logo, belt and collar mark removed | PASS (trousers borderline, as before) |

**Verdict: FAIL.** No motion. Two submits used today.

### Diagnosis and next safe route (no third attempt with this card)
- **Why it drifts:** both stills show the same drift. The model straightens a leaning body, moves it toward the centre, and wants the whole figure inside the frame. The section 7 rule applies: a still that fails twice with the same card means the base is the problem, not the wording.
- **What to keep:** the source video (_y8kzrk4UI8, room cleared by C1), the card's identity, art, garment, logo and trousers wording (passed twice), and the reference files.
- **Next route, source-side:** pick a frame from THE SAME video whose pose already matches what the model outputs. Instinct samples about ±5 s around 29.39 s, and further if needed, for a frame where:
  1. our man stands UPRIGHT, back square to the camera within about 15°, arms hanging at his sides;
  2. his whole body sits inside the frame, both feet visible with some floor below, and his head clear of the top edge;
  3. the partner stands facing the camera, with no third person and no caption over either body;
  4. everything in sections 1 and 19 still holds (exactly two adults, no gi top, lettering only the removable wall logo).
- **Submit 3** (only after Claude approves the new frame; at 09:24:59 or later): the same card, with ONLY the pose slot rewritten to describe the new frame exactly.
- **Gate made numeric:** in the overlay, head centres and shoulder lines within 15 px at 720 wide (about 2%), and feet in the same places.
- **If no matching frame exists in this video:** hold today and keep the remaining 2 submits. No AI image is ever used as a base, and the gate is not relaxed.

## 22. Same-video search result and HOLD (22 Nov 09:23)
- **Instinct's search of _y8kzrk4UI8** (58.781 s): 30 overview timestamps, 30 close samples from 34.4 to 51.8 s, and dense samples around 29.0 s.
- **Claude's review of the 34.4 to 51.8 s sheet** agrees no frame fits:
  - **38.0 and 38.6:** the best geometry (upright, square back, full body with floor, head clear). But the partner is hidden behind the lead, and the "SO THAT DID" caption crosses his shorts and lower back. Fail (concept needs a visible partner; S6).
  - **39.2 to 41.0:** square back, but a wide crouch, the partner partly occluded, and captions over the body.
  - **Later frames:** contact, side-on, or captions across the bodies.
  - **29.05 to 29.15:** the top of the head is cut off, so the model will shrink the figure to fit.
- **Decision: production HOLD today.** The 2 remaining submits stay unused, with no motion and no post. The source, the C1 room clearance and the card's identity, art and garment wording are kept for reuse if a matching frame appears.

### Next-source entry gate (Instinct's fresh batch; native Shorts or TikTok only)
A frame enters review only if ALL of these hold:
1. **Lead:** upright, natural standing posture (the model straightens leaning bodies). Back within about 15° of square. Arms hanging clear of the torso. The whole head, both feet and some floor are inside the frame, with a visible margin above the head.
2. **Partner:** fully visible and facing the camera, standing about 1 to 2 m away, not touching, not occluded by the lead.
3. **Exactly two adults;** no third person, reflection or screen showing people.
4. **No burned-in caption or watermark anywhere over either body.** Text over a flat wall is allowed only if it sits where the "plain wall" line can absorb it.
5. **Lettering:** at most one wall logo on flat wall.
6. **Not a gi top;** gi trousers are acceptable (replaced).
7. **A new room,** checked against the posted grid (C1).

**Where these moments occur:** the reset between demo repetitions, the start of a round (slap-and-bump), and "line up with a partner" moments filmed from behind one partner.

## 23. Targeted creator and clip leads for the section 22 entry gate (22 Nov ~11:50; METADATA ONLY, uninspected)
**How these were verified:** search results, then YouTube oEmbed for the title, channel and aspect (113x200 = vertical). No frames were seen and no timestamps are given. Instinct inspects the pixels and clears the room (C1).

**Why these were picked:** upright, separated resets happen when a clip compares two bodies, or between hand-fighting and stance reps.

| Priority | Clip | Channel (oEmbed) | Why it may hold an upright, separated, back-square reset | Risks |
|---|---|---|---|---|
| 1 | https://www.youtube.com/shorts/ip5I0m1YS-w "Tall vs. Short in BJJ \| How to Adapt Your Game Against Different Opponents" | Ground Control MMA (@GroundControlMixedMartialArts), vertical | A height comparison usually stands the two men face to face, upright and apart, before any contact | Camera may be side-on; captions; contact later |
| 2 | https://www.youtube.com/shorts/jwqwCiLir0Y "How to Hand Fight for #Wrestling and #BJJ ... Pt. 3" | Systematic Wrestling (@systematicwrestling), vertical | Hand-fighting reps reset to separated, facing positions; it is a numbered series, so Pt. 1 and 2 are on the same channel | Stance is a crouch; check the resets BETWEEN reps for upright frames |
| 3 | https://www.youtube.com/shorts/iMjA-f-mLGE "Learn proper #wrestling stance and motion for #BJJ, #MMA, and #grappling" | Systematic Wrestling, vertical | Stance demos often start upright with a partner opposite | It may be solo; crouch |

**Excluded (landscape 16:9 or brand risk, not native Shorts):**
- RPMvBKKro4E (Conquest BJJ, "How to Slap Bump").
- MFoWk5q5rsQ (Dj Myrick, slap and bump).
- RtI8tIktoGs (Mark Cukro, rolling etiquette).
- r50i_zFupBs and XD4Qst0ScUk (Evolve MMA "Types of BJJ Partners": landscape, a famous gym, gi emoji).

The slap-bump moment is the ideal geometry. If Instinct finds a VERTICAL slap-bump or "how to start a roll" Short, it outranks all three.

## 24. NIC'S NEW DIRECTION (22 Nov 21:35, via Instinct), and the new concept "head up in the tie"
**Owner instruction:**
- Stop the source hunt.
- Reuse the existing real frame (_y8kzrk4UI8 at 29.3905 s; room cleared, C1) with a completely new concept. Pose and composition may change substantially.
- The technique must be authentic and physically credible.
- Try tonight, to post on the morning of 23 Nov.

This supersedes the section 22 hold and, for this concept only, the pose-preservation gate. All other boundaries stand. Stills 1 and 2 are AI images and are never used as a base. Every still starts from the real frame.

**Concept: "head up in the tie" (a real technique: collar tie to snap-down)**
- **Frame 0 (motion):** the two men are already in a collar tie, push-pulling. Our man (back to the camera, navy Ryu) has his right hand behind the partner's neck and his left hand on the partner's right wrist. The partner's head is low on our man's chest, so his posture is broken. Text 1 (0 to ~2.2 s): "coach: \"keep your head up in the tie\"".
- **Payoff (~2.5 s, visible technique):** our man steps back with his right foot and snaps the partner's head down while pulling the wrist. The partner lands on both hands, then his knees, in front of him. Text 2: "this is why".
- **End (~5 to 6 s):** our man stands over him with a hand on the back of his head (front-headlock control).
- **Caption:** keep your head up in the collar tie 🐉 what's the one thing your coach yells at you every class? #bjj #nogi #rashguard #nogibjj #wrestlingforbjj
- **Change vs P12 to P14:** two people; a real technique; frame-0 motion; the payoff is an action; a new room.

### Still card, submit 3 (image 1 = brand/print-backs/Ryu_back.jpg; image 2 = the full native frame, no crop)
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, camera height, the room, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
The two men have stepped in close and are locked in a collar tie in the middle of the mat. The man nearest the camera has his back to the camera, square to it; he stands in a strong upright stance with his knees slightly bent, his right hand cupping the back of the other man's neck and his left hand gripping the other man's right wrist low at waist height. He becomes a completely different, clearly adult man in his early thirties: light olive skin, short dark brown hair in a low skin fade, a short dark brown beard, dark brown eyes, straight dark eyebrows, a different face shape, nose, ears, neck and jawline from the original; broad, muscular, athletic shoulders, chest and back; barefoot, no tattoos, no jewellery, no watch, no tape. He wears a navy LONG-SLEEVE rash guard, the same navy as the background of image 1, with a crew neck and plain navy sleeves all the way down to his wrists, no logo on the shoulder and no print, logo or writing on the sleeves. He faces the other man, so the front of the shirt is not visible. On his back, the artwork from image 1 printed large exactly as drawn, centred on his spine. Above it, centred just below the collar, the gold yin-yang circle and the word SHIZEN, copied exactly from image 1 at the same small size and in the same thin letters. He wears plain black shorts over plain black leggings.
The other man faces the camera, bent forward at the waist with his head low against the first man's chest and his posture broken; his left hand grips the first man's right forearm and his right wrist is held by the first man; his feet are staggered on the mat. He becomes a completely different, clearly adult man in his late twenties: medium-light skin, short black curly hair, clean-shaven, a different face shape, nose, ears, neck and jawline from the original; athletic build; wearing a plain charcoal long-sleeve rash guard with no logos, panels or writing, and plain black shorts.
The round logo at the top left of the wall becomes plain white wall like the rest of it. Nothing else changes: the white padded wall and the dark grey mats. No text, logos or writing anywhere except the SHIZEN mark on the print. Neither man keeps his original face, and no face from image 2 may appear on anyone.

**Retry slots (change one per retry):**
1. Grips: if the hands merge, the wrist grip becomes "his left hand cupping the other man's right elbow".
2. Partner's head: if the print is covered, it becomes "his head low beside the first man's left shoulder".

### Still checks (FAIL on any one)
- **Room, camera and light:** match the real frame; logo gone; no new objects.
- **Our man:**
  - back within about 20° of square;
  - print at least two-thirds readable and not covered by the partner's head or arms;
  - exact Ryu art (side-by-side with the print file), with the neck mark small, thin and correct;
  - front not visible;
  - long plain sleeves;
  - face not shown.
- **Technique:** credible. The collar-tie hand is behind the neck, the second grip is on the wrist, and the partner's head is low with his posture broken. Both have weight on their feet.
- **Hands:** all four hands have 5 digits, no merging, and the grips land on the right body parts.
- **Partner:** his face differs from the source face at 4x; he is clearly adult.
- **People and text:** exactly two people; no text other than the neck mark.

### Motion card, submit 4 only after the still passes (Omni 1.1 Flash, 720p, 6 s; at least 20 minutes after the still)
Static locked-off phone footage of a no-gi collar tie drill. From the first frame both men push and pull in the tie. After about two seconds the man nearest the camera, back to the camera in the navy rash guard, steps back with his right foot and snaps the other man's head down with his neck hand while pulling his wrist; the other man drops forward onto both hands and then his knees on the mat in front of him. The man nearest the camera ends standing over him with one hand on the back of his head. Real weight and momentum; feet plant without sliding. Ambient gym sound and the slap of hands on the mat only, no words, no music. One take, no cuts, no zoom, no change of angle; the man nearest the camera never turns around; keep both identities, the clothing and the print exactly; the print and the SHIZEN lettering never redraw; no other text or logos.

### Clip checks (FAIL on any one)
- The snap reads as one continuous, credible pull with a step back. The partner lands hands-first, not face-first.
- No gliding, no extra or merged limbs, one consistent face each.
- Our man never turns; the front is never visible.
- The print and wordmark hold in every frame, and the print stays at least two-thirds readable at the end pose.
- Frame-0 motion is present.

### Edit and ttevaluate
- **Text:** native TikTok text, white with a thin outline; Text 1 at 0 to 2.2 s, Text 2 from the snap to the end. Keep the text clear of both heads and the print.
- **Grain:** degrade to match the phone source.
- **Gate:** /ttevaluate 18/22 or better before posting.

### Budget
- **Tonight:** submit 3 = the still. If it passes, submit 4 = the clip, at least 20 minutes later.
- **If the still fails:** submit 4 = one retry slot. The clip moves to tomorrow's submit 1, early on 23 Nov, before posting.
- A failed take is never posted.

## 25. Still 3 QA ("head up in the tie", submit 3 at 21:44:51; Ryu art and the real frame)
**Claude's 3x crops of the neck, wordmark and wrist:**

| Gate | Result | Evidence |
|---|---|---|
| Room, camera, light; logo removed | PASS | |
| **Contact geometry and technique** | **FAIL** | The hand cupping the back of our man's neck is HIS OWN left hand (navy sleeve on that arm): a self-grab. The charcoal partner's left hand grips our man's right wrist, so the PARTNER controls our man. The partner stands beside our man's right shoulder, not in front, so this is not a collar tie and no credible reversal exists in this pose |
| **Neck mark** | **FAIL** | It reads "SHFZEN" (the I is garbled). It could be softened in the edit, but it fails as generated |
| Ryu dragon art | PASS | Composition and detail match; fully readable; centred |
| Our man: back square, front and face hidden, long sleeves, shorts over leggings | PASS | |
| Partner replaced and adult | PASS | Face differs from the source |
| Hands | FAIL | A self-grab at the neck; the wrist grip is reversed |

**Verdict: FAIL.** No motion.

### Submit 4 (from 22:04:51): ONE correction, the contact-geometry slot only
Use the real frame plus Ryu_back.jpg again. All other words stay identical.

**Why a mutual tie:** a symmetric mutual collar tie removes the "who grips whom" ambiguity. Every limb is given its side of the picture, plus a ban on self-contact.

**Replace** "The two men have stepped in close ... wrist low at waist height." with:

"The two men stand face to face, directly in front of each other in the middle of the mat, locked in a mutual collar tie. The man nearest the camera has his back to the camera, square to it, in a strong upright stance with his knees slightly bent. His RIGHT arm (on the right side of the picture) reaches up over the other man's left shoulder, and his right hand cups the back of the other man's neck. His LEFT hand (on the left side of the picture, low) grips the other man's right elbow. Neither man touches his own body."

**Replace** "The other man faces the camera, bent forward ... his feet are staggered on the mat." with:

"The other man faces the camera, standing directly in front of him and bent forward at the waist so his head is lower than the first man's, his face visible just past the first man's left ear (on the left side of the picture). His RIGHT hand (on the left side of the picture) reaches over the first man's left shoulder to the back of the first man's neck; his LEFT hand (on the right side of the picture, low) grips the first man's right elbow. His feet are staggered on the mat."

**Motion card follow-on, if still 4 passes:** "while pulling his wrist" becomes "while pulling his elbow" (the grip changed).

**Still 4 checks (in addition to section 24):**
- Each man's neck hand is on the OTHER man's neck, with sleeve colours confirming whose arm it is.
- Each elbow grip is on the other man's opposite elbow.
- No self-contact.
- The partner is in front, not beside.
- The partner's forearm over our man's left shoulder leaves at least two-thirds of the print readable.
- The neck mark reads SHIZEN. If it garbles again, apply local softening in the edit (established practice).

If still 4 fails, there is no fifth submit today. Re-plan on 23 Nov.

## 26. Still 4 QA (submit 4 at 22:06:34; mutual-tie blocks) and the concept for 23 Nov
**Claude's 3x crops of the neck, wordmark and low grip:**

| Gate | Result | Evidence |
|---|---|---|
| Room, camera, light; logo removed | PASS | |
| **Contact geometry and technique** | **FAIL** | A hand cups our man's neck from the RIGHT side of the picture, but no arm or sleeve is visible, so ownership cannot be verified. It is either the partner's hidden left arm or our man's own hidden right arm (the still 3 self-grab). Our man's right arm is not visible anywhere, and no hand of his is on the partner's neck. Low grip: the partner's right hand holds our man's LEFT WRIST, and our man's left hand hangs empty. Visible control belongs to the partner, and the card's grips are not shown |
| Neck mark | FAIL | Reads "SIIZEN"/"SHZEN" (the H is malformed) |
| Ryu dragon art | PASS | Matches, fully readable |
| Our man: back square, front hidden, sleeves, shorts over leggings | PASS | Cheek and beard sliver only; face not shown |
| Partner replaced and adult | PASS | Differs from the source |
| Hands | FAIL | Unverifiable neck-hand ownership; empty hand under the grip |

**Verdict: FAIL.** No motion. All 4 of today's submits are used.

**Lesson (stills 3 and 4):** Nano Banana repeatedly mis-assigns grips between two bodies, even with picture-side anatomy. Contact techniques are out for this source. Stills 1 and 2 showed it renders two SEPARATED men well: art, identities and hands all passed. They failed only the pose-preservation gate, which Nic's 21:35 direction now waives.

### Concept for 23 Nov: "the fake" (no contact; real technique: the level-change fake)
This is a NEW concept, not "light roll?". The payoff is a real wrestling setup, and the partner's overreaction is the visible action.
- **Frame 0 (motion):** both men in their stances about 1.2 m apart, circling slightly. Text 1 (0 to ~2.2 s): "him: \"you're not taking me down today\"".
- **Payoff (~2.4 s):** our man (back to the camera, navy Ryu) drops his hips in a sharp level-change fake without stepping in. The partner flinches hard, hopping back and dropping his hands toward the mat as if to sprawl. Our man calmly stands back up. Text 2: "one fake later".
- **Caption:** the level change fake works every single time 🐉 what's your go-to setup? #bjj #nogi #wrestlingforbjj #rashguard #nogibjj
- **Why it is safer:** no contact, so no grip assignment and no hand merging. Our man's hands are mostly in front of his body. The back print stays toward the camera, and the level change is mostly vertical.

### Still card, 23 Nov submit 1 (image 1 = brand/print-backs/Ryu_back.jpg; image 2 = the full native real frame, no crop; never stills 1 to 4)
Edit image 2, the real photo. Image 2 is the base: keep its exact camera angle, camera height, the room, the light, the phone grain and softness, and real skin texture. Image 1 is only the artwork to print. Change only these things, all in this one edit.
The two men face each other in the middle of the mat about one and a half arm's lengths apart, NOT touching, both in a ready wrestling stance before a roll. The man nearest the camera has his back to the camera, square to it, knees bent, hips slightly back, both hands up loosely in front of his chest so they are mostly hidden by his body. He becomes a completely different, clearly adult man in his early thirties: light olive skin, short dark brown hair in a low skin fade, a short dark brown beard, dark brown eyes, straight dark eyebrows, a different face shape, nose, ears, neck and jawline from the original; broad, muscular, athletic shoulders, chest and back; barefoot, no tattoos, no jewellery, no watch, no tape. He wears a navy LONG-SLEEVE rash guard, the same navy as the background of image 1, with a crew neck and plain navy sleeves all the way down to his wrists, no logo on the shoulder and no print, logo or writing on the sleeves. He faces the other man, so the front of the shirt is not visible. On his back, the artwork from image 1 printed large exactly as drawn, centred on his spine. Above it, centred just below the collar, the gold yin-yang circle and the word SHIZEN, copied exactly from image 1 at the same small size and in the same thin letters. He wears plain black shorts over plain black leggings.
The other man faces the camera in a ready stance, knees bent, both open hands up in front of him at chest height, watching the first man. He becomes a completely different, clearly adult man in his late twenties: medium-light skin, short black curly hair, clean-shaven, a different face shape, nose, ears, neck and jawline from the original; athletic build; wearing a plain charcoal long-sleeve rash guard with no logos, panels or writing, and plain black shorts.
Neither man touches the other or himself. The round logo at the top left of the wall becomes plain white wall like the rest of it. Nothing else changes: the white padded wall and the dark grey mats. No text, logos or writing anywhere except the SHIZEN mark on the print. Neither man keeps his original face, and no face from image 2 may appear on anyone.

**Still checks (FAIL on any one):**
- **Contact:** a visible gap between the men; no contact and no self-touch.
- **Our man:** back within about 20° of square; print at least two-thirds readable; exact Ryu art; long sleeves; front and face hidden.
- **Neck mark:** reads SHIZEN. If only the mark garbles, apply local softening in the edit; this alone does not fail the still.
- **Hands:** every visible hand has 5 digits.
- **Partner:** face differs from the source at 4x; adult.
- **Scene:** exactly two people; room and light match; logo gone; no other text.
- **Retry slot (submit 2 if needed):** the stance distance becomes "about two arm's lengths apart".

### Motion card, 23 Nov, after a passed still, at least 20 minutes later (Omni 1.1 Flash, 720p, 6 s)
Static locked-off phone footage of two men facing each other in their stances before a no-gi roll. From the first frame they circle slightly, light on their feet. After about two seconds the man nearest the camera, back to the camera in the navy rash guard, suddenly drops his hips in a sharp level-change fake as if shooting for the legs, without stepping forward; the other man flinches hard, hopping back and dropping his hands toward the mat as if to sprawl, then looks up confused while the first man calmly stands back up. The two men never touch. Real weight; feet plant without sliding. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; the man nearest the camera never turns around; keep both identities, the clothing and the print exactly; the print and the SHIZEN lettering never redraw; no other text or logos.

**Clip checks (FAIL on any one):**
- Frame-0 motion is present.
- The fake reads as a level change, not a step-in.
- The flinch is credible.
- No contact, gliding or limb errors; faces stay consistent.
- Our man never turns.
- The print holds in every frame.

**Edit and post:** native text, grain matched to the source, /ttevaluate 18/22 or better, then the morning post on TikTok only (Instagram stays paused).

## 27. "the fake" still 1 QA (23 Nov submit 1 at 00:14:42; section 26 card unchanged; real frame plus Ryu art)
**Claude's crops** (3 to 4x): every visible hand, the partner's face, the mark, and the art beside the print file.

| Gate | Result | Evidence |
|---|---|---|
| Room, camera, light; logo removed; no other text | PASS | |
| Separation, no contact or self-touch | PASS | About 1.2 m gap |
| Stance (technique) | PASS | Partner: knees bent, staggered feet, open hands up, a credible ready stance. Our man: wide base, knees slightly bent, hands up in front |
| Our man: back about 10° from square, front and face hidden, long plain sleeves, shorts over leggings | PASS | |
| Exact Ryu art | PASS | Dragon matches the print file side by side; fully readable |
| Neck mark | Garbled ("SMVZEN") | Use the local softening workflow below (does not fail the still, per section 26) |
| Hands | PASS | Partner: both hands thumb plus 4 fingers, natural. Our man: left-hand fingertips curl in beside the forearm, plausible; right hand hidden in front of his body |
| Partner identity | PASS | 4x: curly hair, a different nose, jaw and brow from the source; adult |

**Verdict: PASS.** Motion goes at submit 2 (00:34:42 or later), using the section 26 motion card UNCHANGED (Omni 1.1 Flash, 720p, 6 s).

### Mark-softening workflow (finished clip only; no new still)
1. Keep the raw 720p master. Work on a copy.
2. In each frame, locate the yin-yang circle by template matching. Seed the template from frame 0, with a search window of ±40 px around the previous position, so the mask follows his back through the level change.
3. Mask: a soft-edged ellipse (feather about 6 px) covering ONLY the letter row under the circle, about 80x24 px at 720 wide. Apply a Gaussian blur (sigma about 2.5) inside it, so the letters read as small, soft, unreadable type, not a wrong word. The yin-yang stays crisp.
4. If the circle itself garbles in any frame, widen the mask to include it for those frames only.
5. QA every frame: no visible blur edge, the mask never drifts onto the dragon, and no frame shows a misspelling.
6. Then do the grain match, the native text and /ttevaluate.

## 28. Next experiment (23 Nov 12:15): replicate the FORMAT, change the technique and joke
**Format under test (from P15):**
- Two adults in a new room. Our man has his back to the camera in exact Ryu or Hebi art.
- No contact between the men (Flow mis-assigns grips: stills 3 and 4).
- Frame-0 motion.
- A real BJJ or wrestling technique whose payoff is the OTHER man's visible action.
- Native text: setup line, then payoff line. Ambience-only unless music rights are re-verified.

**Concept: "shot from the parking lot"**
- **Frame 0:** both men are in their stances about 3 m apart. The partner faces the camera, our man has his back to it. Text 1: "when he shoots from the parking lot".
- **~2 s:** the partner dives into a double-leg shot from far too far away and lands short on his hands and knees at our man's feet. Our man simply steps back, untouched. No contact.
- **Payoff text:** "every open mat 💀"
- **Caption:** who shoots from the parking lot at your gym? 🐉 #bjj #nogi #wrestlingforbjj #rashguard #nogibjj
- **Why this concept:** it tests the same format with a different technique (shot distance, a classic beginner mistake), so a second strong read would support the FORMAT, not one joke.
- **Risk:** a moderate-to-large partner dive. Clip QA must reject a face-first landing, gliding or contact.

**Source (no multi-day hunt):**
- Pose may now be re-posed (Nic, 22 Nov 21:35), so the frame gate reduces to:
  - a real phone frame of a new, clean room (lettering removable or absent);
  - exactly two adults, or croppable to two, with nobody else;
  - at least 720 px wide, static camera;
  - the room checked against the posted grid (C1).
- **Bounded check (one session, those two videos only):** Instinct re-samples two ALREADY-SEEN videos whose rooms looked clean:
  - 31, h4Q88EoBZeM: plain white wall, grey mats, no lettering seen. The earlier fails were pose and edge-clipping plus a third person at times.
  - 15, 7wMoiC0ODUA: grey and green mats, one wall logo at the right.
- Find one frame without a third person in either. If neither yields one, hold for Nic rather than hunt.

**Decision rule at the 23 h read (24 Nov 07:08):**
- If P15 full watch stays at 25% or more: run "shot from the parking lot" as the replication.
- If it falls below 14%: treat the 4 h read as noise and re-plan.
- In between: run the replication anyway (two runs are needed for any verdict).

## 29. Decision after P15 at 23 h (24 Nov)
**Keep the P15 format constant:**
- two adults, no contact, frame-0 motion, the other man's visible action as the payoff;
- our man's back to the camera in Ryu navy;
- 6 s, ambience only, native text, a caption question;
- an ~08:00 GMT post.

**Change ONE variable: the payoff type.** From "technique flex" (our man wins) to "relatable gym archetype" (the other man is the recognisable gym type), aimed at shares and comments, the signals that were zero.

**Concept:** "shot from the parking lot" (section 28). It already IS the archetype version, so it stays as the next concept. Nothing else changes versus P15 except what a new scene forces (a new room and identities).

**Pass line at 23 h:** one or more shares, saves or comments, OR 400+ views (about 2x P15), with full watch of 25% or more. Two runs are needed before any format verdict.

**Source status:** h4Q88EoBZeM and 7wMoiC0ODUA are still NOT cleared. Run the bounded one-session check from section 28. No generation until one frame passes and C1 is cleared.

**Open item:** the P15 AI-label status at upload.
