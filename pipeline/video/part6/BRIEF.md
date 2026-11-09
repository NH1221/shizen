# Part 6: "she said it was her first class / first class rash guard though"
## Why (from data so far, no retention inferred where we don't have it)
- Part 3 at 4 h: 438 TikTok views, 3 likes, 0 comments. That's in the same range as earlier posts (open mat v4 610 at 4 h, earn the back 248 at 4 h): the one-shot pun format holds reach but hasn't broken out, and comments are still 0.
- Every Shizen video so far has a male subject. One variable this time: a woman wearing the print, same pun-plus-drop format. Women are a large share of the rash guard market and of BJJ TikTok, and nothing we've posted speaks to them.
## Shot
- One low-motion shot, Flow-native, Tora print.
- Base: `incoming/2026-11-09/src/P6-seated-back.png`, crop of real frame 3.5 s (`f003-5.jpg`, x500-1080, y880-1911): a woman with a ponytail sitting on the mat, back three-quarter to camera.
- Clip: arms planted; only breathing, the ponytail settling, and a small head turn. Background people keep stretching.
- Edit: same phone treatment, plus the focus-falloff mask if any background face survives.
## Text and caption
- 0 to 2.5 s: "she said it was her first class"
- Drop: "first class rash guard though"
- Caption: she said it was her first class 🐅 tag the girl at your gym who sandbagged you #bjj #nogi #rashguard #womensbjj #bjjgirls
- Hypothesis: a female subject plus womensbjj tags reaches a new cluster: views at 4 h above Part 3's 438.
## Source change (9 Nov 13:12): no new upload needed
Flow upload failed this afternoon. Use the real frame already uploaded to Flow this morning instead: `P3C-seated-back.png` (project c69fc794, from real frame f004). It's the same woman with a ponytail sitting back-to-camera, from a different moment of the reel. Tora is already in project b93f4822. Use the picker's "Select project" to pull each asset; no generated image is used as a reference.
## 9 Nov 13:23: Flow "unusual activity" on the P6 still (not charged). Part 6 moves to tomorrow.
- Edit spec ready: `pipeline/video/part6/p6-v1.json` (two-line text beats, drop at 2.5 s, same phone treatment). Crop and focus mask to be set from the real clip.
- No Gemini still: a Gemini still can't reach Flow (no export), so it can't become motion. Not worth a generation.
