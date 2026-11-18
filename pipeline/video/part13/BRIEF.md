# Part 13: source hunt (new gym, new composition)
Treatment waits for Part 12's 4 h numbers; the source does not. The Coastal class video is used up for this composition (Parts 10, 11, 12 from 34:30 to 35:00).

## What to find (prompt method v1: pose first, two people only)
Same composition that has worked: one adult man with his back to the camera, sitting or kneeling, calm, touching nobody; one other adult close to him facing the camera (face 60 px or more at native size), still, hands visible and clear of the lead. A 9:16 crop of just those two, 600x1066 or larger, with no captions, bright windows, door glass or wordmarks; nobody else in the crop. Everyone clearly adult; nobody well known.

## Where to look (ranked)
1. Other long, uncut, static-camera class recordings from small gyms on YouTube, filmed from the mat edge behind seated students (search: "no gi class" full class; "adult no gi" class recording; "nogi fundamentals" class; "jiu jitsu class" technique breakdown full). The talk between drills is where this composition happens; sample those parts.
2. Coastal Jiu Jitsu's other uploads (same channel, other class recordings) if they use a different room or camera position.
3. Open-mat vlogs with a static phone on the wall.
Skip highlight reels, known instructors' instructionals, competition footage, anything with burned-in titles.

## Process
Instinct sends a 15-second survey zip (browser frames, low-res fine) per candidate video; Claude screens and names exact timestamps; Instinct extracts untouched native frames; Claude crops in code to the two people and fills the template card from PLAYBOOK "Prompt method v1" (Ryu by default, design confirmed after the 4 h numbers). No Flow before Claude's frame PASS.

## 18 Nov 09:50 Won BJJ "Full No Gi Class" (FWls2Lj28Og, 86:44, 522 storyboard frames every 10 s): REJECTED whole source
- Fisheye action camera: strong barrel distortion across the frame (Flow would inherit warped bodies and an action-cam look, not a phone).
- Bright window wall behind almost every person; big wall logos and banners.
- Crowded mat throughout; the few seated backs near the camera (around 50:00 to 53:40, 58:30 to 64:50, 72:00 to 75:50, 76:10 to 79:50) are low in the corner with other people overlapping, nobody facing the camera close to them; people who may be teenagers among the crowd.
- Added hunting filter: no fisheye or action-camera footage (look for straight walls and door frames in the thumbnail).

## 18 Nov 09:59 "210330 Nogi" (pvjVUrGEW_U, 34:23, 208 storyboard frames every 10 s): REJECTED whole source
- A huge hall (event or mass open mat) shot from floor level: hundreds of small people across the whole horizon in every frame, which cannot be cropped out or fully replaced; harsh rows of overhead strip lights.
- 6:00 to 7:30: a seated man side-on, with people walking past in the foreground, nobody facing the camera close to him. 23:00 to 24:10: two seated men side-on to the camera facing each other, not a back to the camera. Rest is rolling or contact.
- Added hunting filter: small rooms only (a wall within a few metres behind the subjects); skip events and big halls.
- Also screened out by Instinct: Fulshear nELvlBOtnaA (fisheye, wall logos), N2-NMbGrvFI (windows, gi), Ian Lieberman 2Kqf5UA2w-I (Zoom class).

## 18 Nov 10:08 6am BJJ Warrior (fzHz5tXg-kg, 43:47, 264 storyboard frames): REJECTED whole source
- 8:30 to 11:10 (the talking pause): the instructor stands side-on in a hoodie in front of a huge round gym wordmark; the seated students between him and the camera face the camera or sit side-on; the only back to the camera (red cap, olive top) sits at the bottom-right edge, cut off, far from the instructor (both cannot fit one 9:16 crop with nobody between them).
- 13:20 to 17:30: groups drilling on the floor, mostly in contact, side-on; doors and the big logo behind.
- Rest: drilling, rolling, standing.
- Also screened out by Instinct: Force Open Mat qBqGS0j2PPQ (high wide camera, bright open door, people far away), Arroyo 6Zr9c56i-K4 (wide corner lens, crowd, contact demo).

## Widening the pool (fallback composition, if no two-person frame by end of 19 Nov)
A SOLO frame: one adult man with his back to the camera, sitting or kneeling, calm, filling most of a 9:16 crop, nobody else in the crop. Far more common (any bystander watching a roll). The conflict then lives in the text instead of a watching coach (Part 10's hook formula: a conflict line on screen from frame 1). Same filters otherwise (straight lens, small room, no captions, windows or wordmarks behind him, clearly adult, nobody well known).

## 18 Nov 10:17 Meerkatsu "Nogi Sweeps from Closed guard" (z0ySGw_Nm7w, 8:59, 109 frames every 5 s): REJECTED
- Wide static tutorial shot: the people fill only about a fifth to a quarter of the frame height, so a 600x1066 crop leaves the back at about 20% of the crop height (rule: 40%+) and faces about 30 px (rule: 60+). Cropping tighter would drop below the minimum crop size and need upscaling.
- 1:30 to 1:35: the seated back's legs are tangled with the partner's (contact); the partner faces side-on, not the camera. 3:20 to 3:25: both side-on, mid-explanation with gestures.
- Burned-in technique subtitles on most frames (would sit inside a crop's bottom third).
- The channel owner is a known BJJ blogger and illustrator who appears on camera (nobody well known rule).
- Also screened out by Instinct: ChokeDeal3r rIY7Ise6Obs (frosted window wall), Spectrum I-sWw-yFpdE (gi, big logos), Kyuzo masB5WZX7yU (huge wordmarks), Fightness edZ8Xfm1J4M (low-res 4:3, captions).
- Size reminder for screening thumbnails: the back must fill roughly the lower 40% or more of the FULL frame height (people that look small in a 16:9 thumbnail are too small).
