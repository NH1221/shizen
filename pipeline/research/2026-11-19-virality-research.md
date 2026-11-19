# Virality research and audit (19 Nov 2026)
Asked by Nic (19 Nov 12:22, via Instinct): understand what makes content viral, audit skills, separate evidence from anecdote, find mechanisms, and rebuild the plan. Evidence grades: **A** = platform's own documentation or peer-reviewed study; **B** = our own measured data (small n); **C** = industry write-up or creator anecdote (measured numbers but the explanation is opinion). Retrieved 19 Nov 2026.

## 1. External evidence
| Source | Grade | What it shows (measured) | What it does NOT show |
|---|---|---|---|
| TikTok Newsroom, "How TikTok recommends videos #ForYou" https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you/ | A | Signals: likes, shares, follows, comments, content created; caption, sounds, hashtags; device and language weighted low. "Strong" signals outweigh weak ones; finishing a longer video is a strong signal. Follower count and past hits are not direct factors. The system does not recommend duplicated content, already-seen content or spam. | Any thresholds or batch sizes. |
| TikTok Community Guidelines, Integrity and Authenticity https://www.tiktok.com/community-guidelines/integrity-authenticity/ | A | Realistic AI-generated scenes or people must be labelled (AIGC label, or a clear caption, watermark or sticker). Content is ineligible for For You if it is "unoriginal or reproduced content that does not have any new or creative changes". No platform manipulation, including "the use of automation to register or operate accounts in bulk". Likeness of adult private figures may not be used without permission. | Whether our unlabelled AI posts are down-ranked (unknown; Nic's 11 Nov decision stands, with its stop rule). |
| Berger and Milkman, "What Makes Online Content Viral?", J. Marketing Research 2012 https://faculty.wharton.upenn.edu/wp-content/uploads/2011/11/Virality.pdf | A (news articles, not video) | Sharing rises with positive valence and with high-arousal emotions: awe (+30% odds per SD), anger (+34% per SD), anxiety, amusement (lab). Low-arousal sadness lowers sharing. Practical utility, interest and surprise also raise sharing. | Short video specifically; comments; TikTok's ranking. |
| Ling et al., "Slapping Cats, Bopping Heads, and Oreo Shakes: indicators of virality in TikTok short videos" (arXiv 2111.02452) https://ar5iv.labs.arxiv.org/html/2111.02452 | A- (400 labelled videos, likes-based) | Creator popularity was the strongest predictor (90% of viral videos from creators with 10k+ followers vs 24% of non-viral). 67% of viral videos had on-screen text vs 30% of non-viral. Second-person point of view 70% vs 60%. Very wide (long) shots rare in viral videos (1% vs 17%). Emotion had "little bearing"; hashtag stuffing no effect. | Causation; small accounts; watch time. |
| Metricool TikTok study 2026 via Net Influencer https://www.netinfluencer.com/tiktok-content-volume-up-nearly-80-percent-in-early-2026-as-per-post-performance-declined-report-finds/ | C (large dataset, vendor) | Videos get 5.6x the views and 7.8x the interactions of photo/carousel posts. Per-post views fell 31% year on year as volume rose ~80%. Recommends 1 to 2 specific hashtags. | Format causes. |
| Darkroom, "How TikTok's algorithm works in 2026" https://www.darkroomagency.com/observatory/how-tiktok-algorithm-works-in-2026 | C | Staged rollout to viewer groups; finishes, rewatches, shares and comments decide expansion; TikTok publishes no completion threshold. | Numbers. |
| CHILLOLOG case, HackerNoon https://hackernoon.com/how-a-15-second-tiktok-meme-reached-12-million-views-from-a-small-account | C (measured stats, opinion on why) | A 15 s relatable contrast meme from a 25k account: 12M views, 76k shares, 50k saves, 12 s average watch, 36.3% completion, 85.9% of views from Search. | Why; generalisability. |
| Gymshark on TikTok, Chatdesk https://chatdesk.com/tiktok-campaigns-and-case-studies/gymshark-tiktok | C | Apparel brand growth via creators (micro-influencers), a participation challenge (#gymshark66) and volume (up to 40 videos a month). | Measured effect of each. |
| Jits Magazine, BJJ meme accounts https://jitsmagazine.com/five-accounts-to-follow-for-bjj-memes | C | BJJ humour accounts are meme-led, trend-reactive and post daily; one sells apparel. | Numbers or formats. |
| "We suspect automated behavior" (SuperProfile; vendor) https://superprofile.bio/guides/we-suspect-automated-behavior-instagram | C | Instagram shows this when activity looks automated; usually a temporary restriction or review, can escalate. | Meta's own thresholds. |

Could not do from this workspace: watch or download TikTok or YouTube videos, or read their view counts directly (network allowlist). So there is no verified frame-by-frame breakdown of specific viral BJJ videos here; Instinct can surface examples, and their analysis must be graded C unless the numbers are read from the platform.

## 2. Our own evidence (grade B; n of 1 per variant, test batch ~700, so differences under ~15% are noise)
- 13 of 17 TikTok posts landed between 626 and 922 lifetime views (18 Nov). No post expanded beyond its first audience.
- Best hold: Part 2 (several shots, a story: the flashy white belt, then flattened): 4.26 s average, 33% full watch.
- Best opening: Part 10 (conflict visible in frame 1, line on screen at 0.0): 76% still watching at 1 s.
- Best like rate: the two October opinion posts (6.9 and 4.0 likes per 100 views), but low reach (~300).
- Comments: 1 genuine in 17 posts (character humour, not product).
- P12: 0 views for 24 h+ with no notice. Cause unknown. Zero views alone do not prove duplicate suppression.
- Integrity flags: Instagram suspension checkpoint (19 Nov 09:44) then an explicit automated-behaviour warning (12:22). No TikTok flag so far.

## 3. Audit of our tools and skills (critical)
- shizen-content-manager: strong on realism and safety; weak on format design. Its "format bank" is a list of jokes, all producible as one still back plus two text lines, so every concept collapsed into the same template. Outdated rules (AI label on). Gap: no rule that a new post must differ in structure, only in wording.
- ttevaluate: scores execution of a cut (hook, legibility, loop). It cannot tell that a post is the same format as the last five; P14 passed 20/22 while repeating the template. Gap: no structural-novelty or mechanism check, and it rewards short length only indirectly.
- Prompt method v1: fixed scene restaging; keep.
- Available marketplace plugins (searched 19 Nov): mostly paid-ads and analytics connectors that need account connections (not allowed). Two contained ones could help later if Nic chooses to add them: "Marketing Psychology Kit" (grades persuasion claims against studies) and "Marketing Ideas & Growth Experiments" (pass/stop lines for tests). Not installed; not needed for this plan.

## 4. What this changes
- P14 critique accepted: it was a new scene and a new line, but the same format (one near-still back, two text beats, a design reveal). "Opinion-led wording" is not a format change.
- The production budget (1 still + 1 clip) has been silently choosing our format. The new plan designs format first, then budgets submits for it (up to 2 stills + 2 clips = 4 submits per post).
- Shares and saves come from content people want to send or keep: relatability that names someone they know, practical utility, awe or surprise (A: Berger and Milkman). Our posts have offered a mild pun about a rash guard, which triggers none of these strongly.
- Text on screen and second-person address are associated with viral TikToks (A-, correlational): keep text, use "you" more.
- Creator size predicts virality (A-); we cannot change that quickly, which is another reason to target shares and search rather than hoping for For You expansion alone.
