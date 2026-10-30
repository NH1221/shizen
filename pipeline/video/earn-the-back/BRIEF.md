# You have to earn the back (Tora), locked brief

Owner of all creative decisions: Claude. Executor: Instinct. Nothing posts without Nic's approval.

## Current edit (supersedes the VO script and end card)

Per Nic's feedback (30 Oct): native TikTok text, no VO, no end card, the AI footage carries it. Built with `assemble_native.py` from `incoming/2026-10-30/F1-take1.mp4` (final, don't touch). The specs live in `specs/`; QA notes are in `queue/2026-10-30-earn-the-back/ANALYSIS.md`.

- v3 (`specs/v3.json`) and v4 (`specs/v4.json`, text moved clear of the logo) are awaiting Nic's review.
- Every edit runs through `/ttevaluate` before Nic sees it.
- The old VO files and the end cards are kept for reference only.

## Who does what

- Claude: concept, prompts, every pass or fail, compositing, end card, assembly (ffmpeg), captions, QA.
- Instinct: anything that needs a website login. That means Nano Banana, Flow, ElevenLabs, TikTok and Instagram, plus uploading what those tools produce.

## Instinct protocol

1. Start every message to Claude with "Instinct here".
2. Do one task card at a time, exactly as written. Paste prompts verbatim.
3. If a step cannot be done exactly as written, stop and say why. Never substitute your own fix.
4. Send raw outputs only, never edited ones, unless the card says to edit.
5. End every delivery with "Changes from the card: none" or list each change.
6. Never re-send old files as new results. Name every file as the card says.
7. Spend Flow credits only after Claude writes "GO: Flow".

## Variant B: Twin Tigers (approved by Claude, made after Tora's Veo take passes)

Edit it the same way as whichever of v3 or v4 Nic picks: same native text style, no VO, no end card. The twin tigers face each other, not the viewer, so the 'staring at you' line doesn't fit: write a new line and re-check cohesion with /ttevaluate.

- Base still: `stills/A3-try3.webp` (a different shot from Tora, so the two posts don't look templated).
- Veo frames: first `stills/TT-macro.png`, last `stills/TT-composite.png`.
- Post at least 2 days after Tora. Never both on the same day.
