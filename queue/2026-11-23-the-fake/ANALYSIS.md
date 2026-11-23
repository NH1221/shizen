# "the fake": 23 Nov TikTok post (Instagram paused)

## Raw clip QA (Claude, every frame of 144 at 24 fps; contact sheets plus zooms)
**Source and generation:**
- Real frame _y8kzrk4UI8 at 29.3905 s (room cleared, C1) plus Ryu_back.jpg, giving "the fake" still 1 (PASS, section 27).
- Clip: Omni 1.1 Flash, 720p, 6 s, Frames mode (23 Nov 00:37:22, 10 credits).
- Raw master sha256 799601ae909cc4f32ec9e87ac6aa745e342e1a1f44b07196b5aab5b58eb49dde.

**Timeline:**
- Frames 0 to 50 (0 to 2.1 s): circling and hand-fighting distance. Motion from frame 0.
- Frames 52 to 75 (2.2 to 3.1 s): our man drops his hips in a wide level change; his back stays to the camera.
- Frames 76 to 89 (3.2 to 3.7 s): the partner flinches back into a low defensive crouch, hands toward his knees.
- Frames 90 to 143: both stand up; the partner looks confused.

**Results:**
- **No contact:** hands come close at frames 12 to 20 (hand-fighting range); there is no grab.
- **Never turns:** our man never turns and his front is never visible.
- **Partner:** one consistent face; adult.
- **Print:** stable and readable in every frame.
- **Movement:** foot steps are plausible (he steps back slightly toward the camera as he rises); no gliding.
- **Verdict: PASS.**
- **Technique note:** the fake is a wide, upright-torso level change rather than a head-first shot feint. It reads as "drops levels"; acceptable.

## Edit
- **Mark:** soften_mark.py tracks the yin-yang circle per frame (multi-scale template; minimum match 0.60 at frame 62, mid-squat; checked visually). It blurs ONLY the letter row under the circle (sigma 2.6 x scale, feathered ellipse). The circle stays crisp, the letters read as small soft type, and no misspelling is visible. Track log: pipeline/video/fake/track.csv.
- **Grade:** assemble_b.py, one phone grade (0.7 soft, 432-line downsample, light warmth, grain 7), 1080x1920 at 30 fps.
- **Sound:** Sparta cut with the drop on the flinch (start 2.78 s), ambience at 0.6, loudness -14 LUFS.
- **Files:**
  - fake-v1-post-clean.mp4: NO text, for native in-app text.
  - fake-v1-post-text.mp4: same, with the TikTok Sans text burned in (fallback).
  - Both two-pass x264 at 9 Mbps.

## /ttevaluate (burned-text version): PASS 20/22
**Standing rules:** all OK. Native text style; creator voice; no end card or product-only shot; no zooms; reads as phone video; cohesive.

| # | Check | Score | Evidence |
|---|---|---|---|
| 1 | Hook | 2 | Frame 1 shows two men squared up, and "him: you're not taking me down today" opens a challenge |
| 2 | Curiosity gap | 2 | The challenge (0 s) is paid off by the fake and flinch (3.2 s) |
| 3 | Script voice | 2 | "him: ..." and "one fake later" are native BJJ-TikTok phrasing |
| 4 | Text legibility | 1 | 2 lines for 2.25 s, then 1 line for 2.8 s, clear of both heads. But the burned text at y 118 to 226 sits under TikTok's top tabs. Placed in-app just below the tabs, this scores 2 |
| 5 | Sound | 2 | The drop hits the flinch; ambience is real; the story works muted |
| 6 | Pacing | 2 | A new beat every 1 to 2 s; no dead stretch |
| 7 | Length and loop | 1 | 6 s (under the 7 s band). The end (both standing) does not loop seamlessly into the start (stances) |
| 8 | Comment pull | 2 | The caption asks for the viewer's go-to setup |
| 9 | Brand restraint | 2 | The print is visible throughout and never pitched |
| 11 | Cohesion | 2 | Challenge, fake, then a caption about the fake: one story |
| 10 | Honesty | 2 | No claims. The AI label stays per Nic (11 Nov): manual label off, "Your brand" disclosure on |

## Posting (TikTok only, morning of 23 Nov)
**Upload** fake-v1-post-clean.mp4 and add native text:
- **Text 1:** him: "you're not taking me down today"
  - Timing 0.0 to 2.2 s.
  - Classic (TikTok Sans) font, white with the outline style (no background box), centred.
  - Placed just BELOW the top For You and Following tabs and above our man's head, about 12 to 18% down the frame. Two lines are fine.
- **Text 2:** one fake later
  - Timing 3.2 s to the end, same style and position.
- **Fallback:** if the in-app timing is fiddly, post fake-v1-post-text.mp4 instead (text already burned in) and add no app text.

**Settings:**
- Keep the original sound.
- **Caption:** the level change fake works every single time 🐉 what's your go-to setup? #bjj #nogi #wrestlingforbjj #rashguard #nogibjj
- **Disclosures:** AI-generated label OFF (Nic, 11 Nov); "Your brand" content disclosure ON.

**Rules:**
- No promo or brand comments, and no engagement manipulation.
- Stop and report on any warning, restriction or CAPTCHA.
- Never post to Instagram while it is paused.

**Reads:** 4 h and 23 h, the same fields as P14. Compare with the P10, P11 and P14 23 h reads (age-matched).

## 23 Nov 01:00 update: audio rights and AI label (Instinct's challenge)
**Music rights**
- The repo holds a record: queue/2026-11-09-part3/ANALYSIS.md. It was verified by Instinct on 9 Nov and names "Sparta" by Arulo on Mixkit, under the Mixkit Stock Music Free License, with verbatim licence quotes.
- The local file hash matches that record: sha256 91d6af08f5152622af3a8f58523f54a5a023b6189be9e62a0c385c5ca361b8a8.
- Claude could NOT re-verify it today. The licence page fetch was not permitted in time, and a web search did not surface the Mixkit track page. Earlier use is not proof.
- **Rights are therefore NOT re-established for this post. Post the ambience-only versions** unless Instinct re-verifies both the Mixkit track listing and the licence page today.

**Ambience-only files** (video stream unchanged: the last-frame md5 7564656cfb089a74e21c275c486405fe is identical to v1; the mark softening and grade are unchanged):

| File | Contents | sha256 |
|---|---|---|
| fake-v2-amb-post-clean.mp4 | No text | 0675c917... |
| fake-v2-amb-post-text.mp4 | TikTok Sans text burned in | d4d9bfb8... |

- Both use the raw generated gym ambience only, loudnorm to -18.4 LUFS, true peak -1.3 dBFS.
- Instinct listens once before posting to confirm there are no generated words or music artefacts in the ambience.
- The v1 music files stay in the queue, NOT for posting.

**/ttevaluate re-score for v2-amb: PASS 19/22.**
- Check 5 (sound) drops to 1: the ambience is plausible and the story works muted, but there is no musical lift on the payoff.
- All other scores are unchanged.

**AI label: correction**
- Claude's earlier line ("AI-generated label OFF") misstated the rule. Nic's 11 Nov instruction: leave the MANUAL label off and let TikTok apply any AUTOMATIC label. Instinct verified that TikTok requires realistic AI scenes and people to be labelled.
- The edit re-encodes the Flow clip, so any embedded content credentials are very likely stripped, and an automatic label may not appear.
- **At upload, check whether TikTok applies an AI label automatically.**
  - If it does: proceed under Nic's instruction.
  - If it does not: the post would be an unlabelled realistic AI video, which does NOT meet TikTok's requirement. Do not post. Report to Nic and ask him to decide between switching on the manual AI label for this post and holding.
