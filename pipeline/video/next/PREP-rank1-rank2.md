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
> He wears a <COLOUR> LONG-SLEEVE rash guard, the same <COLOUR> as the background of image 1, with a crew neck and plain <COLOUR> sleeves all the way down to his wrists, no logo on the shoulder and no print, logo or writing on the sleeves or front. Plain black shorts and plain black leggings.

## 4. Garment accuracy (what each shot may show)
- **Known from brand files** (brand/model4-sheet.jpg, brand/print-logo-position.jpg, img/ryu.jpg):
  - Crew neck, raglan seams, long plain sleeves.
  - Body colour equals the print background (Ryu is "gold on midnight").
  - The art is centred on the spine, with the small gold yin-yang and thin serif SHIZEN centred below the back collar.
- **Front:** the repo has no front view. Every card so far specifies a plain front, so that is the working spec, NOT a verified fact (see section 8). Hebi Mark is a chest design and stays parked.
- **Shot B (on his back):** the front only. The back art and wordmark are against the mat, so they cannot and must not be visible. FAIL if any art, yin-yang, lettering or logo appears anywhere in the frame.
- **Shot A (walking away):** back art and wordmark only.
- **Rank 2:** back art and wordmark at the start. During the turn, the visible side and front stay plain, and the art stays on the back and turns with it.

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
Static locked-off UGC iPhone footage. The man in the navy rash guard lies flat on his back exactly as in the frame, completely spent: from the first frame his chest rises and falls hard in deep, heavy breaths; his arms and hands stay where they are on the mat; near the end he lets out one long slow breath and his head sinks back slightly. Ambient gym sound and his heavy breathing only, no words, no music. One take, no cuts, no zoom, no change of angle; keep his face, the clothing and the plain shirt front exactly; no artwork, lettering or logo appears anywhere; no smiling.

### Motion A (6 s)
Static locked-off UGC iPhone footage; the camera does not move or follow. The man in the navy rash guard keeps walking away from the camera at a slow, relaxed pace, three or four steps onto the mat, arms hanging loosely with a small natural swing, head facing forward; each foot plants with no sliding. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; keep his build, hair, the clothing and the print exactly; the print and the SHIZEN lettering never redraw and move with his back; no other text or logos; he does not turn around.

### Motion rank 2 (6 s)
Static locked-off UGC iPhone footage. The big man in the charcoal rash guard stands with his back to the camera and from the first frame rolls his shoulders twice, loosening up; then he turns his head and upper body toward the camera with a sheepish, apologetic grin, eyebrows raised, as if saying sorry; his arms stay hanging at his sides the whole time and his feet do not move. Ambient gym sound only, no words, no music. One take, no cuts, no zoom, no change of angle; keep his build, the clothing and the print exactly; the print and the SHIZEN lettering stay on his back and turn with it, never redraw; the sleeves and shirt front stay plain charcoal; one consistent face once it appears; no other text or logos.

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
  - Any print or logo on the sleeves or front; any art in B.
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
- **Shirt front:** the actual front is not documented in the repo. If Instinct finds a front view in existing product files, the GARMENT block is updated to match it. Nic is not asked.
- **Untested motion:** walking, lying-down breathing and a face turn are all untested with this model.
- **Rank 1 room:** no candidate room with both moments has been found yet.
