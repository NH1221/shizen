# Two videos, 2 Nov (Claude directs, Instinct executes, Nic approves each before posting)

## Lessons applied to both
1. Frame 1 shows a person, readable in under 0.5 s. No macro openers.
2. One text line, 8 words or fewer, native TikTok style. Must pass /ttevaluate (cohesion rule).
3. Stills-first: Nano Banana still, then Claude passes it, then Flow. Claude composites the real print in code. Flow never sees a bare design image.
4. Realism (Omni guide): name what must survive from the still, name both ends of any camera move, use phone-camera terms ("natural smartphone zoom", "handheld phone footage"), and state "no text of any kind in frame". The Jennings video's transcript is still pending (see the Instinct card).

## Video A: Twin Tigers turtle (follow-up to earn the back)
- Omni 1.1 Flash 720p, image-to-video from `incoming/2026-10-30/stills/TT-composite.png` (already passed).
- Text, 0 to 4 s: "pov: he turtles and you see this"
- Caption: rolled with him all year and never knew this was on his back 😭 #bjj #jiujitsu #rashguard #nogi #bjjhumor

## Video B: open mat reactions, then the reveal
- 3 reaction shots at Omni 480p (zoomed-phone look), about 1.2 s each in the cut. Then the reveal at Omni 720p, about 5 s: a man walks away from camera down a big busy academy with Tora on his back, and people turn to look.
- Text over the reactions: "everyone at open mat tonight". Over the reveal: no text.
- Caption: walked into open mat in this and the whole room went quiet 🐅 would you roll in it? #bjj #jiujitsu #rashguard #nogi #bjjlifestyle
- Post A and B a few hours apart, after Nic approves each.

## Video B storyboard v2 (Jennings method plus template research, 2 Nov)
Template evidence (`incoming/2026-11-02/3-reaction-template.md`): the top formats are walking past strangers whose reactions are the content, with the person or outfit as the payoff. 4 of the top 5 use original ambient sound. The two shortest (10 s and 13 s) rank 2nd and 3rd by views. The closest commercial analogue is a dress brand (@lucyintheskystore, 8.9M).

| Time | Shot | Model | Text |
|---|---|---|---|
| 0.0 to 1.3 | R1: man between rounds freezes mid-sip, eyes track past the camera | Omni Flash 480p | "pov: you wear this to open mat" |
| 1.3 to 2.6 | R2: two partners stop drilling, one taps the other, both look | Omni Flash 480p | (same line holds) |
| 2.6 to 3.9 | R3: the coach at the mat edge, slow nod | Omni Flash 480p | (same line holds) |
| 3.9 to 10.0 | REV: handheld phone from behind; he walks away down the academy, Tora on his back, heads turning | Omni 720p | none |

- Sound: original gym ambience from the clips. No music, no VO, no scripted lines.
- Loop: the last frame (his back moving away) cuts straight into R1 (a face looking toward the camera) and reads as "next person reacting".
- Caption: walked into open mat in this and the whole room went quiet 🐅 would you roll in it? #bjj #jiujitsu #rashguard #nogi #peoplesreactions

## Omni prompt template (Jennings three parts; lock it, then only swap the action)
1. Scene: "[Static locked-off | handheld] UGC iPhone footage, [zoomed in from across the room, soft and grainy]. [Action in one sentence.]"
2. Dialogue: none. The audio is "ambient gym sound only: mats, distant voices, no words spoken to camera".
3. Fixed rules: "One take, no jump cuts. Keep the face, skin texture, clothing and print exactly as in the image. Natural micro-movements, no smiling unless stated. No text, captions or logos appear. No camera zoom unless stated."

## Sourcing decision (2 Nov, after the IG hunt)
The real-source hunt closed with zero usable frames (TikTok, Flickr, Wikimedia, Instagram). R1 to R3 and REV are now Nano Banana Pro stills, generated in one shot each. Faces are the weakest part of this video; Nic is told that plainly. If Nic sends his own gym photo, it replaces the REV still.

Still rules for all four: 9:16, highest resolution, Nano Banana Pro (original, not v2), 2 generations per card, both uploaded raw. Nobody wears cream (only REV does). No logos, text or patches anywhere. Claude composites Tora onto REV in code; the REV back stays plain.

Files: `incoming/2026-11-02/stills/R1-a.png`, `R1-b.png`, `R2-a.png`, `R2-b.png`, `R3-a.png`, `R3-b.png`, `REV-a.png`, `REV-b.png`.

## Real source (2 Nov, from Nic): art.of.roll reel DeE1HHyAP8F, 720x1280
Frames picked by Claude (one per second, f_NNN = second NNN). Instinct extracts the sharpest frame within +/-0.5 s at full res to `incoming/2026-11-02/src/fNNN.png`, then runs the Nano Banana Pro edit prompts from Claude's message.
- R1 sip freeze: f034 (two men against the wall under the bottle shelf). Backup: none.
- R2 pair turn: f006 (seated group mid-room). Backup: f005.
- R3 coach nod: f010 (Nic's standing bearded man; floor rollers removed). Backup: f013.
- REV walk-away: f004 (long room, windows, seated groups); man added walking away, blank cream back. Backup: f037.
- Never use f002 or f003 (burned-in text).

## Nic's changes (2 Nov, 15:26): two-shot reveal, Twin Tigers, print placement
- The reveal becomes two shots. REV-1: he walks toward the camera (plain front), people turn their heads as he passes. REV-2: from behind, he walks away and the back print is revealed.
- Design: Twin Tigers, not Tora. Print placement fixed to match the product mockup (`img/tora-pair.jpg`): SHIZEN mark just below the collar, tigers across the shoulder blades at about 70% of back width. Old Tora composite is retired.
- Storyboard v3: R1 0 to 1.3, R2 1.3 to 2.6, R3 2.6 to 3.9 (text "pov: you wear this to open mat"), REV-1 3.9 to about 6.4 (front walk-in, no text), REV-2 about 6.4 to 10.5 (back reveal, no text). Loop: his back walking away cuts to R1.
- Files: REV-2 start frame `stills/REV2-TT-composite.png` (720x1280). REV-1 still to come: Nano Banana edit of `REV-a.png` turning him to face the camera.

## Nic's rule (2 Nov, 15:29): the print is placed in image generation, not in code
Supersedes lesson 3 ("Claude composites the real print in code"). Instinct attaches the real print file (`brand/print-backs/<Design>_back.jpg`) to the Nano Banana Pro edit and the model places it. Claude passes or fails the result against the original art (artwork unchanged, mark below the collar, tigers across the shoulder blades at about 70% of back width, as in `img/tora-pair.jpg`). Claude's code composites are retired.
- REV-1 pick: REV1-a, mirrored (`stills/REV1-a-flip.png`) so the room reads as the opposite end from REV-2 (windows on the left facing him, on the right behind him). Safe to mirror: the front is plain, with no text.

## New basis from Nic (2 Nov, 20:35): `src/NIC-base.jpg`
Supersedes REV1-a, REV1-a-flip and REV2-a. Nic's edit of f004: open doorway in the far wall (right of centre), the man walking toward camera from it.
Chain (Nano Banana Pro, one-shot edits, 2 runs each, Claude passes each before the next):
1. `REV1-final`: from NIC-base. New face and race for every person vs the TikTok original; his cream tee becomes a plain cream long-sleeve rash guard; the man in the blue long-sleeve rash guard (right of frame, behind him) looks at his back.
2. `REV2-plain`: reverse angle, same room, camera 2 m behind him; identity and outfit from REV1-final; plain back.
3. `REV2-final`: Twin Tigers generated onto the back of REV2-plain from `brand/print-backs/Twin-Tigers_back.jpg`.
Flow: Omni 1.1 Flash 720p x1. B-REV1 4 s from REV1-final; B-REV2 8 s from REV2-final. B-R1 to B-R3 unchanged.
Storyboard v4: R1, R2, R3 (0 to 3.9 s, text "pov: you wear this to open mat"), REV1 (to about 6.4 s), REV2 back reveal (to about 10.5 s), loop to R1.

## Calibration notes (2 Nov, 22:25)
- Nic accepts REV2-final-a, but for future prints wants the tigers slightly smaller and higher: about 60% of back width, tigers starting just below the SHIZEN mark.
- B-REV2 take 2: the crowd thins and the room drifts in the final frames. Use the opening ~4 s only.
- Reactions run at Omni 1.1 Flash 720p (Flow has no 480p; 360p rejected for faces). Softness is added in the edit.
