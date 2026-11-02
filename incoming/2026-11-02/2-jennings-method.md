# Jennings AI-UGC realism method (extracted 2 Nov 2026)
Source: https://youtu.be/kvf2lRSGixg ("I stopped using seedance and now my AI UGC looks 100% real (Copy me)", Kristian Jennings, 31 min).
Extraction basis: the video's full published caption transcript (verbatim, in this folder as 1-kvf2lRSGixg-transcript.txt) plus storyboard frame previews at 1:05 / 7:02 / 10:08 / 14:45 / 21:09. The video stream itself could not be played in the browser used (media buffering blocked), so this is transcript-grounded, not watched.

## STEP 1 - FIND A REAL REFERENCE (50% of the whole effort)
Find a real UGC video from a real creator (TikTok for younger avatars, Instagram for millennial, Facebook for older) and take a still frame. It must be a real photo from a real phone: the baked-in noise, grain, skin pores and micro-detail are what escape the uncanny valley - AI-generated reference images animate waxy because those imperfections are not there to be animated.
Selection criteria:
- (a) intentional framing, body position, camera angle
- (b) natural light but NO overexposed highlights (shiny skin blown to white = dead data = glossy waxy animation)
- (c) background with some personality and depth, not busy, not a blank wall
- avoid frames with captions where possible
If a reference just will not animate right (~1 in 10), discard and find a new reference - never fight the video model.

## STEP 2 - CREATE THE AVATAR with Nano Banana Pro
Model: Nano Banana Pro (the original, NOT Nano Banana 2; avoid GPT image models - too perfect).
- Mandatory identity change: eye colour, nose, skin pigmentation etc - it must be impossible that the reference person and your avatar are the same person without plastic surgery (deepfake law).
- Keep or adjust the background (greenery works well).
- Add accessories and outlier features (earrings, necklace, one earphone only, a visible mic - which also creates "audio logic" for clear voice audio).
- CRITICAL: one-shot the prompt - ALL changes in ONE generation, never sequential edits; each edit feathers pixels and that AI-perfection shows when animated. Regenerate the full prompt until happy.

## STEP 3 - ANIMATE with Gemini Omni (he stresses: NOT Omni Flash)
Via Omni Video: upload the reference image + prompt.
Three-part prompt structure:
1. SET THE SCENE - explicit camera movement ("static locked off shot" or "handheld UGC iPhone shot"), camera type ("UGC iPhone footage"), what is happening, avatar behaviour ("mouth moving naturally, keeping eye contact with the camera", energy level)
2. DIALOGUE in quotation marks - swap line by line
3. FIXED RULES - stack every correction after harsh review (energy, confidence, pace, smiling) plus "one take, no jump cuts"
Lock the prompt, then generate line by line. Capitalising a word in the dialogue changes which word the avatar stresses. Durations are only 4/6/8/10s: if a line lands between durations, pad the dialogue with nonsense words and go up a duration, then cut the padding in the edit.

## Time split
50% obsessing over the reference image, 25% dialling the prompt, 25% generation. Script and storyboard before any assets: rules for the ad, KISS, calm clear delivery beats hyper-fast editing, avatar should have underlying authority for the angle, message dialled before production.

## Platform constraints (verified 2 Nov 2026, apply to publishing)
- TikTok Community Guidelines require labelling realistic AI-generated people/content; unlabelled realistic AIGC can be removed. Source: https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content
- Meta labels AI content and expects self-disclosure ("AI info"); plan with the AI label ON.
- No fake "genuine customer" endorsements, no identifiable real people as fans; reactions video is a fictional POV skit; every reference transformed beyond recognition per step 2.
