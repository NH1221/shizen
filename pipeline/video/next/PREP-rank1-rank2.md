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
