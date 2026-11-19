# Dev's Year in Review — v2 prompts (for ElevenLabs remake)

## Changes from v1
1. **Computer room is no longer grim.** It's now a small, lived-in but decent studio with a new reference image (prompt below). That affects Part 1 (2am coding) and Part 2 (3am under the blanket).
2. **Part 1 opens on a close-up of Mina**, not a wide two-shot.
3. **Bus scene: Dev is asleep with his mouth closed. No drool.**
4. Timing fixes from the v1 audio check:
   - Part 1: in v1, "I travelled a lot, always on the move" spilled onto the studio shot. It must now finish *inside* the bus shot.
   - Part 2: in v1, "Got really into running" spilled onto the phone shot. It must now finish *inside* the bus-chase shot.
   - Part 2: "big-budget" came out as "big butch". The line is now spelled out so it's pronounced clearly.
5. Part 3: in v1, a blurry ghost of Dev was left behind the dog in the final shot. The prompt now says explicitly that Dev is fully gone.

## Reference images (in `references/`)
| File | Used as |
|---|---|
| 01_dev_present_look.png | Dev, present-day look |
| 02_dev_memory_look.png | Dev, memory look |
| 03_mina.png | Mina |
| 04_mr_park_landlord.png | Mr. Park |
| 05_bruno_dog.png | Bruno |
| 06_bruno_disguise.png | Bruno in disguise |
| 07_ninjutsku_app_screen.png | Phone app screen |
| 10_loc_rooftop_bar.png | Rooftop bar |
| 11_loc_night_bus.png | Night bus |
| **12_loc_studio_apartment.png → REPLACE with new image below** | Dev's studio |
| 13_loc_kitchenette.png | Kitchenette |
| 14_loc_bus_stop.png | Bus stop |
| 15_loc_living_room.png | Living room |
| 16_loc_mr_park_office.png | Mr. Park's office |

---

## NEW reference image — Dev's studio apartment (16:9, photoreal)

> Photoreal wide interior of a small, modest studio apartment at night, no people. A clean wooden desk against the wall with three monitors glowing soft blue, a mechanical keyboard, a mesh office chair, a couple of energy-drink cans and a mug neatly beside the keyboard. A neatly made low bed with a grey duvet beside the desk. Warm desk lamp, a small potted plant, a few framed movie posters, a bookshelf with figurines, fairy lights along the wall, venetian blinds with a hint of city neon outside. Lived-in and a little cluttered like a young creative's home, but clean, cozy and decent — not dirty, not run-down, no stains, no trash. Mixed lighting: warm lamp plus cool monitor glow. Shot on ARRI Alexa 35, 24mm, eye level, fine film grain, Kodak Vision3 look, live-action realism, no text, no logos.

---

## PART 1 — Rooftop intro (20s, 16:9)

**Refs:** @image1 = 01_dev_present_look · @image2 = 02_dev_memory_look · @image3 = 03_mina · @image4 = 10_loc_rooftop_bar · @image5 = 11_loc_night_bus · @image6 = NEW studio apartment

```
IDENTITY LOCK — MAINTAIN EXACTLY, ZERO DRIFT ACROSS ALL 20 SECONDS. The character reference images are multi-panel model sheets: use them ONLY for appearance; never show panels, grey backgrounds or split layouts on screen.
@image1 — DEV, PRESENT-DAY LOOK. Take his face, short dark faded hair, skin tone, stubble, stocky build and his mustard velvet blazer, lime-green vest, gold chain, gold aviator sunglasses, cream chinos and white sneakers ENTIRELY from @image1. His face never changes.
@image2 — DEV, MEMORY LOOK. The SAME man with the SAME face as @image1, but with messy bed-head hair, the faded grey t-shirt, navy track pants and blue flip-flops from @image2. He wears this look in every memory scene.
@image3 — MINA. Take her face, long dark hair with see-through bangs and half-up knot, black leather jacket, white top, jeans and gold hoops ENTIRELY from @image3.
OTHER CHARACTER — one bus passenger: a tired, broad, bearded middle-aged man in an orange hi-vis work jacket. Appears only on the bus.
ENVIRONMENTS — @image4 is the rooftop bar (PRESENT): reproduce it exactly, the brick bar on the left, water tower, palms, string lights, round metal bistro table with two lemonades, smoggy skyline at golden hour. @image5 is the night bus interior (MEMORY). @image6 is Dev's small studio apartment (MEMORY): a modest, cozy, lived-in room with a clean desk, three monitors, warm desk lamp, plant, posters and a neatly made bed — reproduce it exactly; it is NOT dirty or run-down.
SCENE: A comedy short. PRESENT scenes are warm golden hour. MEMORY scenes are cooler and more muted than the rooftop, but natural, not grim. HARD CUTS between locations. Only the named characters appear; no extra people anywhere except the one bus passenger.
CRITICAL — frame one is a CLOSE-UP of Mina's face at the bistro table, already mid-conversation. Do not show anyone arriving.
PERFORMANCE STYLE: grounded deadpan comedy. Dev is supremely confident on the rooftop; in memories he is a tired, slightly pathetic everyman. Natural speed throughout, no slow motion.
AUDIO — GENERATE NATIVE AUDIO WITH THE VIDEO. English. Dev's voice is the SAME voice in every line, on screen and in voiceover. Lines clearly separated, never overlapping, accurate lip-sync for on-screen speakers. Each voiceover line must START AND FINISH inside its own shot — never let a line run across a cut:
 • 0:00–0:02 — MINA, warm and curious: "So... how was your year?"
 • 0:02–0:04 — DEV, smug: "Honestly? A year of more."
 • 0:04.5–0:07.5 — DEV off-screen voiceover, smug, heard ONLY over the bus shot (nobody on screen moves their mouth; Dev is asleep): "I travelled a lot. Always on the move."
 • 0:08.5–0:10.5 — DEV off-screen voiceover, heard ONLY over the studio typing shot (his mouth stays closed while typing): "Built my own AI app."
 • 0:13–0:14.5 — DEV on screen, into his phone, urgent: "Write my landlord an excuse."
 • 0:14.5–0:16.5 — PHONE ASSISTANT, calm polite synthetic female voice from the phone speaker: "I can't help with that. Calling your landlord."
 • 0:17–0:18 — DEV, panicked: "NO—!"
No other words. Sound design: rooftop city hum, distant traffic, glasses clink; bus engine drone, air-brake hiss, a soft snore; keyboard clacking, a bright notification ding at 0:12, a phone dial tone ringing from 0:17. NO MUSIC SCORE.
TIMELINE:
0:00–0:02 — CLOSE-UP on Mina at the bistro table on the @image4 rooftop, golden hour, string-light bokeh behind her. She holds her SMARTPHONE (not a microphone) up like a podcast mic toward camera-right (toward Dev) and asks her question with a curious smile.
0:02–0:04 — Close-up on Dev in the @image1 look: he slowly slides on his gold aviators and answers, chin up. Slight push-in.
0:04–0:08 — HARD CUT to the @image5 night bus. Dev in the @image2 look is asleep with his head resting on the bearded passenger's shoulder, MOUTH CLOSED, peaceful, NO DROOL, nothing wet on the jacket. The passenger turns and stares dead into the camera, unamused. Static handheld, cold green fluorescent light.
0:08–0:12 — HARD CUT to the @image6 studio at 2am. Dev sits in the mesh office chair typing fast at three blue-glowing monitors; warm desk lamp on, room tidy and cozy. At 0:12 a notification pops on the centre monitor (screen text blurry and unreadable) and his eyes go wide.
0:12–0:17 — Dev grabs his phone and talks into it; the phone answers; his face drops in horror. Medium close-up, monitor and lamp light on his face.
0:17–0:20 — Dev yells "NO" and tosses the phone onto the neatly made bed, where it keeps ringing, screen glowing. He freezes, staring at it. Locked-off wide, no camera movement.
CAMERA PACKAGE: ARRI ALEXA 35, anamorphic primes at T2, ISO 800, 24fps 180-degree shutter, natural motion blur. Rooftop on a smooth slider; memory scenes slightly handheld.
LENS BEHAVIOUR: oval anamorphic bokeh, soft flares off the string lights and sun, mild edge distortion, slight vignetting.
GRADE AND SENSOR: rooftop matches @image4 — warm golden amber with soft smog haze; bus matches @image5 — cool green fluorescent; studio matches @image6 — cozy mix of warm lamp and cool monitor blue. Filmic highlight rolloff, fine organic grain, Kodak Vision3 character.
PHOTOREAL: real skin texture and pores, real fabric and hair movement, live-action photographic realism, not rendered, not stylised, no CGI look. No readable text, no logos.
```

---

## PART 2 — Memory montage (20s, 16:9)

**Refs:** @image1 = 02_dev_memory_look · @image2 = 13_loc_kitchenette · @image3 = 14_loc_bus_stop · @image4 = NEW studio apartment · @image5 = 07_ninjutsku_app_screen

```
IDENTITY LOCK — MAINTAIN EXACTLY, ZERO DRIFT ACROSS ALL 20 SECONDS. The character reference is a multi-panel model sheet: use it ONLY for appearance; never show panels or grey backgrounds on screen.
@image1 — DEV, MEMORY LOOK. Take his face, messy bed-head dark hair, stubble, skin tone, stocky build, faded grey t-shirt, navy track pants and blue flip-flops ENTIRELY from @image1. He wears exactly this in every frame. His face never changes.
KEY PROP — @image5 is the NINJUTSKU phone app screen: dark purple UI, orange ninja-mask logo, a huge glowing hot-pink button. When the phone screen is shown it looks like @image5.
ENVIRONMENTS — @image2 tiny kitchenette with coil stove, beige fridge and a smoke detector on the ceiling. @image3 boulevard bus stop with palms, strip mall and a plain white city bus. @image4 Dev's small studio apartment — modest, cozy, lived-in, clean desk with three monitors and a neatly made bed — now dark at 3am; it is NOT dirty or run-down.
SCENE: Comedy short, MEMORY scenes only: muted, slightly cool and tired-looking, but natural, not grim. HARD CUTS between locations. Dev is the only person on screen; the bus driver is never seen.
CRITICAL — frame one opens with Dev already at the stove mid-cooking. Do not show him entering.
PERFORMANCE STYLE: grounded deadpan comedy, a tired everyman taking himself far too seriously. Natural speed, no slow motion.
AUDIO — GENERATE NATIVE AUDIO WITH THE VIDEO. English. Dev's voice is the SAME voice in every line. Off-screen voiceover lines are Dev's smug narration and his mouth does not move for them. Each voiceover line must START AND FINISH inside its own shot — never let a line run across a cut:
 • 0:00–0:02.5 — DEV voiceover, smug: "Learned to cook. Fusion cuisine."
 • 0:05–0:06 — DEV on screen, coughing, kissing his fingertips: "Chef's kiss."
 • 0:07–0:09.5 — DEV voiceover, heard ONLY over the bus-chase shot: "Got really into running."
 • 0:12–0:15 — DEV voiceover, clearly enunciated: "I'm a filmmaker now. Big-budget action."
 • 0:18–0:20 — DEV on screen, whispering to himself under the duvet: "...one more."
No other words. Sound design: sizzling saucepan, a shrill smoke-detector beeping from 0:03, towel flapping, coughing; slapping flip-flops on pavement, panting, bus engine pulling away, one short bus horn honk at 0:10; in the dark studio soft screen taps, a cartoon whoosh on each tap, and a goat bleat from the phone at 0:17. NO MUSIC SCORE.
TIMELINE:
0:00–0:03 — @image2 kitchenette. Close-up: Dev, utterly focused, uses tweezers to place a single herb leaf on a neat mound of curly instant ramen noodles on a white plate, then squeezes a fancy swirl of ketchup. Smoke curls up from the saucepan behind him.
0:03–0:06 — The smoke detector shrieks. Dev grabs a dish towel and frantically waves it at the ceiling, coughing through the smoke, then turns to camera and proudly kisses his fingertips.
0:06–0:11 — HARD CUT to the @image3 bus stop. The plain white city bus pulls away from the stop down the road. Dev runs IN THE ROAD DIRECTLY BEHIND THE BUS, chasing its rear bumper, arms pumping, one arm reaching out toward the back of the bus, t-shirt flapping, one flip-flop flying off his foot. Camera low, behind Dev, so we see Dev's back with the rear of the bus just ahead of him, the gap slowly growing. The bus keeps going and honks once. Dev slows, stops in the middle of the road, and doubles over with hands on knees, gasping, as the bus shrinks into the distance.
0:11–0:16 — HARD CUT to the @image4 studio at 3am, dark except the phone glow. Dev lies on his neatly made bed with the grey duvet pulled over his head like a tent, his face lit only by his phone. Insert close-up of the phone screen matching @image5: his thumb jabs the big glowing pink button, and the preview flashes to a silly new video thumbnail each time.
0:16–0:20 — Back on his face under the duvet, grinning like a maniac in the phone glow, he whispers his line and taps again. Locked-off close-up, no camera movement.
CAMERA PACKAGE: ARRI ALEXA 35, anamorphic primes at T2, ISO 800, 24fps 180-degree shutter, natural motion blur. Slightly handheld; tracking vehicle for the bus chase.
LENS BEHAVIOUR: oval anamorphic bokeh, mild edge distortion, slight vignetting, phone-screen glow blooming softly.
GRADE AND SENSOR: match @image2, @image3 and @image4 — muted, slightly cool, with yellowish fluorescent in the kitchen and soft blue phone light at night. Filmic highlight rolloff, fine organic grain, Kodak Vision3 character.
PHOTOREAL: real skin texture and sweat, real smoke behaviour, real fabric movement, live-action photographic realism, not rendered, not stylised, no CGI look. No readable text except the phone UI, no logos.
```

---

## PART 3 — Ending (20s, 16:9)

**Refs:** @image1 = 01_dev_present_look · @image2 = 02_dev_memory_look · @image3 = 03_mina · @image4 = 04_mr_park_landlord · @image5 = 05_bruno_dog · @image6 = 06_bruno_disguise · @image7 = 15_loc_living_room · @image8 = 10_loc_rooftop_bar · @image9 = 16_loc_mr_park_office

v1 audio timing was correct. The only change is the final shot (no ghost Dev).

```
IDENTITY LOCK — MAINTAIN EXACTLY, ZERO DRIFT ACROSS ALL 20 SECONDS. Character references are multi-panel model sheets: use them ONLY for appearance; never show panels or grey backgrounds on screen.
@image1 — DEV, PRESENT-DAY LOOK: face, short dark faded hair, stubble, stocky build, mustard velvet blazer, lime vest, gold chain, gold aviators, cream chinos, white sneakers ENTIRELY from @image1.
@image2 — DEV, MEMORY LOOK: the SAME face as @image1 with messy bed-head, faded grey t-shirt and navy track pants from @image2.
@image3 — MINA: face, long dark hair with bangs and half-up knot, black leather jacket, white top, jeans, gold hoops ENTIRELY from @image3.
@image4 — MR. PARK, her father, the landlord: face, grey moustache, gold reading glasses low on his nose, white polo, ENTIRELY from @image4. He appears ONLY on a phone screen in a video call.
@image5 — BRUNO the dog: tan short-haired mutt, one folded ear, curled tail, red collar, from @image5.
@image6 — BRUNO IN DISGUISE: the same dog wearing the mustard velvet blazer, lime vest, gold chain and gold aviators from @image6.
ENVIRONMENTS — @image7 dim living room with a brown corduroy couch and cold TV glow (MEMORY). @image8 the golden-hour rooftop bar with the round metal bistro table and two lemonades (PRESENT). @image9 Mr. Park's wood-panelled office with venetian-blind shadows, seen only inside the phone screen.
SCENE: comedy short. MEMORY is muted and cool; PRESENT rooftop is warm golden hour. HARD CUTS. On the rooftop there are exactly two seats at the table and no other people.
CRITICAL — frame one opens with Dev already on the couch crying into Bruno. Do not show anyone sitting down.
PERFORMANCE STYLE: grounded deadpan comedy. Natural speed, no slow motion.
AUDIO — GENERATE NATIVE AUDIO WITH THE VIDEO. English. Dev's voice is the SAME voice in every line. Lines clearly separated, never overlapping, accurate lip-sync for on-screen speakers:
 • 0:01–0:04 — DEV off-screen voiceover, smug (his mouth does not move; he only sobs on screen): "And emotionally? I've really grown."
 • 0:07–0:09 — MINA, sweet: "Wow. My dad's going to love this."
 • 0:09–0:10 — DEV, confused: "Your dad?"
 • 0:12–0:15 — MR. PARK on the phone speaker, stern: "Filmmaker, huh? Then make my rent appear."
 • 0:18–0:19 — BRUNO: one short confident bark.
No other words. Sound design: TV murmur, loud ugly sobbing, dog paws trotting away on carpet; rooftop city hum; a vinyl record-scratch stop at 0:15; a cartoon whoosh at 0:17. NO MUSIC SCORE.
TIMELINE:
0:00–0:06 — @image7 living room at night. Dev in the @image2 look sobs dramatically into Bruno's neck on the couch, TV glow on their faces. Bruno looks bored, wriggles free, hops off and trots out of frame. Dev keeps crying face-down into the cushion. Locked-off medium-wide.
0:06–0:09 — HARD CUT to the @image8 rooftop, golden hour. Mina lowers her phone, smiling sweetly at Dev, and says her line. Dev in the @image1 look, sunglasses on, smiles proudly, then his smile falters on "Your dad?"
0:09–0:12 — Mina turns her phone screen toward Dev. Over-the-shoulder push-in onto the phone.
0:12–0:15 — Close-up of the phone screen: a video call with Mr. Park in his @image9 office, glaring over his reading glasses, delivering his line.
0:15–0:17 — Close-up on Dev: he panics, sunglasses slipping down his nose, fumbles out his own phone and jabs the screen.
0:17–0:20 — HARD CUT, same two-shot as 0:06: Dev has COMPLETELY VANISHED — no trace of him anywhere in frame, no silhouette, no blur, no partial body, no shadow. His chair is occupied ONLY by Bruno in the @image6 disguise — blazer, chain and aviators — sitting upright facing Mina. The background behind Bruno is clean, empty rooftop. Bruno barks once. Mina blinks. FREEZE on the final frame.
CAMERA PACKAGE: ARRI ALEXA 35, anamorphic primes at T2, ISO 800, 24fps 180-degree shutter, natural motion blur. Rooftop on a smooth slider.
LENS BEHAVIOUR: oval anamorphic bokeh, soft flares off string lights and the low sun, mild edge distortion, slight vignetting.
GRADE AND SENSOR: living room matches @image7 — muted cold TV blue; rooftop matches @image8 — soft warm golden pastel haze. Filmic highlight rolloff, fine organic grain, Kodak Vision3 character.
PHOTOREAL: real skin texture, tears, real dog fur and movement, live-action photographic realism, not rendered, not stylised, no CGI look. No readable text, no logos.
```
