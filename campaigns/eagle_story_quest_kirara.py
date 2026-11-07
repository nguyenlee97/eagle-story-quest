"""
Kirara -- Story Quest #1 (5 Chapters -- Pure Branching Visual Novel)
Title: "The Last Parcel of Autumn" ("Where Two Tails Cross the Chinju Mist")
Campaign ID: "kirara_sq1_last_parcel_of_autumn" | char_id = "kirara" | ped_id = 49432
Target Runtime: StoryQuestEngine v2.0 + WaifuLink Card Hub v2.0 + Genshin BGM Engine v1.1

Scale & Verified Causal Metrics:
- 5 Chapters | 46 Scene Nodes (N01..N46) | 22 Choices (C01..C22) | 12 Clues/Flags (F01..F12)
- 2 Combination Gates (C15_B_GATE1, C18_C_GATE2) + N17 Second-Chance Pre-Event + C12_A2 Redemption
- 47 Unique 1376x768 (16:9) CGs (1 Poster + 36 Base + 10 Camera-Locked Diffs)
- State Space: Core = 6,396 | Full Rational = 7,491 | Open-Choice Tree = 11,300 (0% dead stat deltas)
"""
from __future__ import annotations

from typing import Any

STORY_QUEST_CAMPAIGN: dict[str, Any] = {'char_id': 'kirara',
 'ped_id': 49432,
 'display_name': 'Kirara',
 'campaign_id': 'kirara_sq1_last_parcel_of_autumn',
 'title': 'The Last Parcel of Autumn',
 'subtitle': 'Where Two Tails Cross the Chinju Mist',
 'poster_cg': 'ui_assets/story_quest_cgs/kirara/kirara_sq1_poster.jpg',
 'synopsis': "A century-old Chinju lacquer box knots its leaking mist-cord around Kirara's fragile "
             "human-world thread. Walk Inazuma's autumn streets beside the twin-tailed courier before her "
             'final delivery turns her back into a nameless, one-tailed stray cat.',
 'version': '2.1.0',
 'theme_rgb': [52, 211, 153],
 'chapters': [{'chapter_id': 'CH1',
               'index': 1,
               'title': 'Chapter 1 -- Gold-Star Delivery Under Falling Maples',
               'entry_node': 'N01'},
              {'chapter_id': 'CH2',
               'index': 2,
               'title': 'Chapter 2 -- Promises Kept Across Quiet Porches',
               'entry_node': 'N09'},
              {'chapter_id': 'CH3',
               'index': 3,
               'title': 'Chapter 3 -- Three Roads Before the Moonless Night',
               'entry_node': 'N18_A1'},
              {'chapter_id': 'CH4',
               'index': 4,
               'title': 'Chapter 4 -- The Root-Torii Threshold at 22:55',
               'entry_node': 'N29_A4'},
              {'chapter_id': 'CH5',
               'index': 5,
               'title': 'Chapter 5 -- Where Two Tails Cross the Chinju Mist',
               'entry_node': 'N38_CH5_CONVERGE'}],
 'initial_state': {'bond': 0, 'insight': 0, 'flags': []},
 'flag_catalog': {'F01_FIVE_STAR_STAMP': {'title': 'Five-Star Paw-Stamp Partner',
                                          'clue_hint': "Signed Kirara's autumn Narukami escort manifest at "
                                                       'Ritou Pier with a five-star cat-paw mark.'},
                  'F02_NEKOMANMA_HEARTH': {'title': "Grandma's Three-Breath Rule",
                                           'clue_hint': "Memorized Grandma's nekomanma rule at Kiminami: "
                                                        'cool every steaming bowl three breaths for a '
                                                        "cat's tongue."},
                  'F03_HITOYO_CORD_WEAVE': {'title': 'Counter-Spun Mist-Cord Weave',
                                            'clue_hint': 'Used Elemental Sight by Chinju Brook to trace '
                                                         "the counter-clockwise coil around Kirara's "
                                                         'Hitoyo no Ito.'},
                  'F04_ROOFTOP_TAIL_CODE': {'title': 'Hanamizaka Rooftop Tail-Code',
                                            'clue_hint': "Swore a pinky promise above Inazuma's lanterns: "
                                                         'two loops of her twin tails around your wrist '
                                                         "mean 'never go alone.'"},
                  'F05_WAX_SEAL_CIPHER': {'title': "Kajiro's Three-Stroke Wax Cipher",
                                          'clue_hint': "Copied Master Kajiro's three-stroke urushi "
                                                       "wax-seal cipher from Master Gensai's cedar "
                                                       'apprentice ledger.'},
                  'F06_GRANDMA_BOX_CUSHION': {'title': "Twin-Tail Sketch Under Grandma's Cushion",
                                              'clue_hint': 'Tucked a tiny sketch of twin cat-tails beneath '
                                                           "the sun-warmed cotton cushion in Kirara's "
                                                           'childhood wooden box.'},
                  'F07_SILK_BELL_RIBBON': {'title': 'Suzu-Ori Silk Chime-Tassel',
                                           'clue_hint': "Keeps Kirara's emerald-and-gold Suzu-Ori "
                                                        'chime-tassel -- woven with a blessed strand of '
                                                        'her own Hitoyo no Ito.'},
                  'F08_PAW_MIST_PULSE': {'title': 'Mayoi-Giri Ley-Pulse Cadence',
                                         'clue_hint': "Timed the exact heartbeat cadence of Chinju's mist "
                                                      "against Kirara's cold cat-paw on Mt. Yougou's "
                                                      'stairs.'},
                  'F09_LANTERN_VOW': {'title': 'Shared Lantern Vow in the Frost-Mist',
                                      'clue_hint': "Stepped straight inside Chinju's inner frost-mist "
                                                   "mirage to cover Kirara's trembling hands with yours."},
                  'F10_NARUKAMI_PAPER_BELL': {'title': 'Narukami Paper-Bell Ward',
                                              'clue_hint': "Received Raiden Ei and Yae Miko's "
                                                           'Electro-blessed Sakura Paper-Bell to attune '
                                                           'the 22:55 mist seam.'},
                  'F11_CAT_TONGUE_CHILL': {'title': 'Early Cat-Tongue Chill Spotted',
                                           'clue_hint': 'Noticed on Night One that Kirara sipped steaming '
                                                        'miso two breaths early with a faintly cool right '
                                                        'fingertip.'},
                  'F12_AMAKANE_MAPLE_DEED': {'title': 'Twin-Maple Inheritance Deed',
                                             'clue_hint': "Witnessed the Yashiro Commission's stamped "
                                                          'Amakane deed naming Koharu legal heir to '
                                                          "Kajiro's doorstep."}},
 'endings': {'END_TRUE': {'rank': 'TRUE ENDING',
                          'title': 'Delivered to Your Side',
                          'tone': 'true',
                          'summary': 'Grounding the centenary cord together and watching Grandma Koharu '
                                     "unseal her grandfather's combs, Aether clips Suzu-Ori beneath "
                                     "Kirara's left bow as her twin tails claim his side beneath Inazuma's "
                                     'starlit lanterns.'},
             'END_GOOD': {'rank': 'GOOD ENDING',
                          'title': 'Warm Box Until First-Sakura',
                          'tone': 'warm',
                          'summary': "Sealing Chinju's hollow under Yae Miko's Five-Torii Ward suspends "
                                     'the mist-cord for ninety days -- buying sunlit mornings over warm '
                                     "nekomanma in Chiori's loft until First-Sakura sap rises."},
             'END_NEUTRAL': {'rank': 'NEUTRAL ENDING',
                             'title': 'Five-Star Regular',
                             'tone': 'warm',
                             'summary': "The hundred-year lacquer box reaches Koharu's hands and Kirara's "
                                        'cat-tongue reclaims its warmth, leaving Aether as Komaniya '
                                        "Express's most cherished five-star regular across Inazuma's "
                                        'autumn roofs.'},
             'END_BAD_1': {'rank': 'BAD ENDING I',
                           'title': 'The Unclaimed Box on the Porch',
                           'tone': 'tragic',
                           'summary': "Retreating from Chinju's mirage forces an emergency ninety-day "
                                      'quarantine seal; ashamed of her rasping voice and unfinished route, '
                                      "Kirara spends the season curled alone in cat form beneath Grandma's "
                                      'veranda.'},
             'END_BAD_2': {'rank': 'BAD ENDING II',
                           'title': 'The Nameless Cat on the Porch',
                           'tone': 'tragic',
                           'summary': 'Locked outside the 22:50 mist wall, Kirara burns every strand of '
                                      'her human-world thread to finish the delivery alone -- leaving a '
                                      'nameless, one-tailed stray cat curled beside a dimmed grey Vision '
                                      'at dawn.'}},
 'nodes': {'N01': {'node_id': 'N01',
                   'chapter_id': 'CH1',
                   'title': 'Special Delivery at Maple Pier',
                   'day_label': 'Day 1 - 03:30 PM (Ritou Harbour)',
                   'location': 'Ritou Harbour - Maple Pier',
                   'bgm_bucket': 'vn_daily_sweet',
                   'beats': [{'beat_id': 'N01_B01',
                              'speaker': 'Narrator',
                              'text': "Crisp Kogarashi sea wind sweeps crimson maple leaves across Ritou's "
                                      'timber pier as the autumn silk packet from Fontaine drops anchor in '
                                      'the bay.',
                              'inner_thought': 'Inazuma in late autumn always smells of roasted tea, sea '
                                               'salt, and dry cedar.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B02',
                              'speaker': 'Paimon',
                              'text': "Ooh, look over by the customs archway, Aether! Isn't that Charlotte "
                                      'adjusting her Kamera tripod beside a mountain of Chioriya silk '
                                      'crates?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B03',
                              'speaker': 'Charlotte',
                              'text': 'Monsieur Verite, hold focus on the harbor roof! Rumor has it '
                                      "Komaniya Express's fastest courier clears the customs tiles in a "
                                      'single bound --',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B04',
                              'speaker': 'Narrator',
                              'text': 'Before Charlotte can press her shutter, a boxy emerald parcel with '
                                      'painted whiskers hurtles off the maple-draped gable and lands '
                                      'weightlessly on padded paws right in front of my boots.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B05',
                              'speaker': 'Narrator',
                              'text': 'Pale Dendro leaves swirl in a cheerful pop. Out springs Kirara, '
                                      'brass collar bell chiming brightly while both fluffy tawny-blonde '
                                      'tails swish in crisp synchronization behind her.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B06',
                              'speaker': 'Kirara',
                              'text': 'Komaniya Express, Gold-Level Courier Kirara reporting on the dot! '
                                      'Wait -- Aether?! And Paimon too! What a five-star stroke of luck '
                                      'meeting you two right at Ritou Pier!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N01_B07',
                              'speaker': 'Aether',
                              'text': 'Good to see you, Kirara. Still treating rooftops like open '
                                      'highways, I see.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B08',
                              'speaker': 'Kirara',
                              'text': 'Hehe, streets have handcarts and customs queues, whereas roof tiles '
                                      'only have pigeons and sunshine! Miss Chiori shipped six bolts of '
                                      'autumn brocade ahead of her own visit this week.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N01_B09',
                              'speaker': 'Charlotte',
                              'text': 'Magnificent entrance, Miss Kirara! One quick quote for The '
                                      "Steambird's Fontaine-Inazuma craft special -- is it true you "
                                      "personally cleared Komaniya's entire back-shelf of unclaimed "
                                      'parcels?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B10',
                              'speaker': 'Kirara',
                              'text': 'Every single one -- well, almost! Leaving an undelivered parcel '
                                      'gathering dust feels like having a fishbone stuck sideways in my '
                                      'throat!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': 'outing_arrive_photo'},
                             {'beat_id': 'N01_B11',
                              'speaker': 'Narrator',
                              'text': "At that word 'almost,' Kirara's left ear twitches ever so slightly. "
                                      'Tucked deep inside her canvas courier satchel, beneath the bright '
                                      'Fontaine waybills, rests the corner of an old black-and-gold '
                                      'lacquer box.',
                              'inner_thought': 'A faint, wintry scent of wet forest moss clings to that '
                                               'old lacquer corner.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B12',
                              'speaker': 'Kirara',
                              'text': "Say, Aether -- since you're heading up to Inazuma City anyway, "
                                      'Komaniya HQ approved an escort stipend for my high-value autumn '
                                      'Narukami run! Care to walk the maple road with me?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                              'voice_emotion': 'vn_playful_tease'}],
                   'choice': {'choice_id': 'C01',
                              'prompt': 'Kirara holds out her cedar clipboard and brass ink-pad while '
                                        "balancing Chiori's silk crates:",
                              'options': [{'opt_id': 'C01_A',
                                           'label': 'Sign her autumn Narukami escort manifest and press a '
                                                    'five-star cat-paw stamp beside your name.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F01_FIVE_STAR_STAMP']},
                                           'next_node': 'N02',
                                           'reaction_beats': [{'beat_id': 'N01_C01A_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Hand over the brush, partner. '
                                                                       'Consider me officially signed onto '
                                                                       'your Narukami route -- complete '
                                                                       'with a five-star paw endorsement '
                                                                       'in advance.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_stamp_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N01_C01A_R2',
                                                               'speaker': 'Kirara',
                                                               'text': 'Purr-- ahem! I mean, thank you '
                                                                       'kindly, esteemed partner! When you '
                                                                       'stamp five stars upfront like '
                                                                       'that, both my tails start wagging '
                                                                       'before I can even tell them to '
                                                                       'behave!',
                                                               'inner_thought': 'Clue Secured [Five-Star '
                                                                                "Paw-Stamp]: I'm "
                                                                                "officially Kirara's "
                                                                                'autumn route partner.',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_stamp_diff.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C01_B',
                                           'label': "Steady the toppling silk crates for Charlotte's photo "
                                                    'and ask quietly about the antique lacquer box in her '
                                                    'bag.',
                                           'effects': {'bond': 1, 'insight': 2, 'add_flags': []},
                                           'next_node': 'N02',
                                           'reaction_beats': [{'beat_id': 'N01_C01B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Let me shoulder the top two '
                                                                       'brocade bolts so Charlotte gets a '
                                                                       'clean shot. That black-and-gold '
                                                                       'lacquer box in your satchel looks '
                                                                       "older than anything off Fontaine's "
                                                                       'ship.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N01_C01B_R2',
                                                               'speaker': 'Kirara',
                                                               'text': 'Sharp eyes as always! The Yashiro '
                                                                       'shrine-road crew turned it into '
                                                                       'our Heritage Shelf last night -- '
                                                                       'Waybill Zero-Zero-Hyakki. Once we '
                                                                       'drop off these silks, help me '
                                                                       'track down its porch!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_ritou_pier_base.jpg',
                                                               'voice_emotion': 'outing_cruise'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N02': {'node_id': 'N02',
                   'chapter_id': 'CH1',
                   'title': 'Goldfish Sparks on Hanamizaka Slope',
                   'day_label': 'Day 1 - 05:45 PM',
                   'location': 'Hanamizaka Slope - Naganohara Fireworks Porch',
                   'bgm_bucket': 'hub_cozy',
                   'beats': [{'beat_id': 'N02_B01',
                              'speaker': 'Narrator',
                              'text': 'By late afternoon, sunset gilds the stepped eaves of Hanamizaka in '
                                      "burnished copper. After checking Paimon and me into the Travelers' "
                                      'Inn beside Aisa Bathhouse, we walk Kirara up the slope toward '
                                      'Komaniya HQ.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B02',
                              'speaker': 'Yoimiya',
                              'text': 'Hey there -- Aether, Paimon, and Kirara! Perfect timing! Pops and I '
                                      'just finished rolling a fresh batch of moisture-proof autumn '
                                      'goldfish sparklers!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B03',
                              'speaker': 'Paimon',
                              'text': 'Yoimiya! Are those the ones that fizz like little orange koi even '
                                      "in sea fog? Wait -- what's that big fuse barrel sitting behind the "
                                      'water tub?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B04',
                              'speaker': 'Yoimiya',
                              'text': 'Oh, wait -- the apprentice lit a festival test shell down on the '
                                      'beach cliff! Cover your ears for one second --!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B05',
                              'speaker': 'Narrator',
                              'text': 'CRACK-BOOM! A crisp concussion echoes off the coastal bluff. Beside '
                                      "me, Kirara's spine arches rigid, both tails puffing to twice their "
                                      'width as she drops to one knee with her hands over her ears --',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B06',
                              'speaker': 'Kirara',
                              'text': 'Nyaa--!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': 'outing_bump_rescue'},
                             {'beat_id': 'N02_B07',
                              'speaker': 'Narrator',
                              'text': 'Dead silence hangs for half a second beneath the fluttering shop '
                                      'noren. Kirara claps both gloved hands over her mouth, cheeks '
                                      'flushing crimson to the roots of her blonde hair.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B08',
                              'speaker': 'Kirara',
                              'text': 'I-I cleared my throat! That was a totally human throat-clearing '
                                      'noise! Nobody heard a cat just now, right, Aether?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N02_B09',
                              'speaker': 'Yoimiya',
                              'text': 'Hahaha, sorry, sorry, Kirara! Here -- take a voucher for warm '
                                      'Tricolor Dango down the street on me to make up for the scare!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B10',
                              'speaker': 'Narrator',
                              'text': 'As I help Kirara to her feet, my fingers brush her courier satchel. '
                                      'Through the canvas weave, a hairline ribbon of silver-blue mist '
                                      'curls out from the old lacquer box and brushes her right wrist like '
                                      'frost.',
                              'inner_thought': "That thread of mist didn't drift away in the breeze -- it "
                                               "curled straight toward Kirara's pulse.",
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B11',
                              'speaker': 'Aether',
                              'text': 'Your satchel feels cold on one side, Kirara. Did something spill '
                                      'inside?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B12',
                              'speaker': 'Kirara',
                              'text': "Oh, that's just old Chinju cedar lacquer staying cool from the "
                                      "forest! Come on -- my stomach's rumbling louder than Yoimiya's "
                                      "fireworks, and Kiminami's lantern counter just lit up!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_hanamizaka_spark_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N03'}],
                   'ending_id': None},
           'N03': {'node_id': 'N03',
                   'chapter_id': 'CH1',
                   'title': 'Sashimi & Childhood Wood-Grain',
                   'day_label': 'Day 1 - 07:30 PM',
                   'location': 'Kiminami Restaurant - Lantern Counter',
                   'bgm_bucket': 'vn_daily_sweet',
                   'beats': [{'beat_id': 'N03_B01',
                              'speaker': 'Narrator',
                              'text': "Amber paper lanterns sway gently under Kiminami Restaurant's cedar "
                                      "eaves. Armed with Yoimiya's voucher, Paimon darts happily down the "
                                      'slope to claim fresh Tricolor Dango before the stall closes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B02',
                              'speaker': 'Narrator',
                              'text': 'Left side by side at the counter, I order a gleaming Sashimi '
                                      'Platter and two bowls of warm nekomanma -- steamed rice topped with '
                                      'shaved bonito flakes and a splash of mild dashi.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B03',
                              'speaker': 'Kirara',
                              'text': 'Fresh sea bream sashimi AND bonito rice -- with zero hard crab '
                                      'shells to crack! Aether, you really do know the way straight to a '
                                      "nekomata's heart!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N03_B04',
                              'speaker': 'Aether',
                              'text': "You mentioned once that Butter Crab shells are a courier's worst "
                                      'enemy. Judging by how your tails are swaying, bonito rice wins by a '
                                      'landslide.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B05',
                              'speaker': 'Kirara',
                              'text': 'Nothing in Teyvat beats nekomanma on a cool evening. Back before I '
                                      'grew a second tail or knew a single human word, an old grandma out '
                                      'in rural Konda found me shivering in the rain.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B06',
                              'speaker': 'Kirara',
                              'text': 'She lined a square wooden Komaniya Express box with sun-dried '
                                      'cotton, set down a little dish of warm rice and bonito flakes, and '
                                      "gave a nameless stray kitten the name 'Kirara.'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N03_B07',
                              'speaker': 'Aether',
                              'text': "'Ki' for woven silk, and 'Ra' for good fortune.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B08',
                              'speaker': 'Kirara',
                              'text': 'You remembered! Every time Grandma left for town, I climbed the '
                                      "tallest cedar on the hill to watch Inazuma City's lanterns glow "
                                      'like fireflies until she came home.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B09',
                              'speaker': 'Kirara',
                              'text': 'The night I wished hardest to walk beside her and make her smile, I '
                                      'leaped down from that cedar branch -- and landed on two human feet '
                                      'with a Dendro Vision shining at my hip.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N03_B10',
                              'speaker': 'Narrator',
                              'text': 'Her emerald eyes soften in the lantern glow as her left hand pats '
                                      'the courier satchel resting right beside her stool -- never more '
                                      "than an arm's reach away.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N04'}],
                   'ending_id': None},
           'N04': {'node_id': 'N04',
                   'chapter_id': 'CH1',
                   'title': 'Two Breaths Too Soon',
                   'day_label': 'Day 1 - 08:15 PM',
                   'location': 'Kiminami Eaves - Night Lanterns',
                   'bgm_bucket': 'vn_tender_romance',
                   'beats': [{'beat_id': 'N04_B01',
                              'speaker': 'Narrator',
                              'text': 'Anna sets two lacquered cups of freshly ladled red-miso soup on the '
                                      'counter, white steam curling briskly into the night air.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B02',
                              'speaker': 'Kirara',
                              'text': "Grandma always laughed at my cat's tongue whenever soup came off "
                                      "the hearth. 'Blow on it three slow breaths first, little Kirara,' "
                                      "she'd say, 'or you'll dance around the veranda!'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N04_B03',
                              'speaker': 'Narrator',
                              'text': 'Yet even as she tells the story, Kirara blows only once -- two '
                                      'breaths earlier than her own rule -- and takes a quiet sip from the '
                                      'steaming rim without fanning her tongue at all.',
                              'inner_thought': 'Wait... that miso cup just came off a rolling boil, and '
                                               'her right index fingertip on the rim looks pale.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B04',
                              'speaker': 'Kirara',
                              'text': 'Huh...? Oh, Anna must have poured mine slightly cooler tonight. '
                                      'Still delicious though!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B05',
                              'speaker': 'Narrator',
                              'text': 'She rubs the tip of her right index finger absently against her '
                                      'palm, as though waking a hand that rested briefly against a cold '
                                      'windowpane.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C02',
                              'prompt': 'White steam rises between you as Kirara sets down the hot miso '
                                        'cup two breaths early:',
                              'options': [{'opt_id': 'C02_A',
                                           'label': "Commit Grandma's three-breath nekomanma rule to heart "
                                                    'and promise to cook it properly whenever autumn '
                                                    'nights turn chill.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F02_NEKOMANMA_HEARTH']},
                                           'next_node': 'N05',
                                           'reaction_beats': [{'beat_id': 'N04_C02A_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Steamed rice, soft shaved bonito, '
                                                                       'zero hard shells, and three slow '
                                                                       'breaths to cool the broth first. '
                                                                       'Next cold night on our route, let '
                                                                       "me cook Grandma's nekomanma for "
                                                                       'you.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02A_R2',
                                                               'speaker': 'Kirara',
                                                               'text': 'Hehe, deal! Careful what you '
                                                                       'promise, Aether -- once you feed a '
                                                                       'cat warm bonito rice by hand, '
                                                                       "she'll show up on your porch every "
                                                                       'single evening!',
                                                               'inner_thought': "Clue Secured [Grandma's "
                                                                                'Hearth Rule]: Cool every '
                                                                                'steaming bowl three '
                                                                                "breaths for Kirara's "
                                                                                'cat-tongue.',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]},
                                          {'opt_id': 'C02_B',
                                           'label': 'Touch the steaming cup rim and ask gently why her '
                                                    "heat-shy cat's tongue and right fingertip barely felt "
                                                    'the heat.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F11_CAT_TONGUE_CHILL']},
                                           'next_node': 'N05',
                                           'reaction_beats': [{'beat_id': 'N04_C02B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'My cup is still too hot to sip, '
                                                                       'Kirara, yet you drank yours after '
                                                                       'one breath -- and your right index '
                                                                       'finger felt cool when you passed '
                                                                       'me the chopsticks.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02B_R2',
                                                               'speaker': 'Kirara',
                                                               'text': 'E-Eh? Did I really? Ever since I '
                                                                       'brushed the moss off that old '
                                                                       'Chinju waybill last night, my '
                                                                       'right fingertips have felt a tiny '
                                                                       'bit sleepy... probably just autumn '
                                                                       'wind!',
                                                               'inner_thought': 'Clue Secured [Early '
                                                                                'Cat-Tongue Chill]: '
                                                                                'Touching Waybill '
                                                                                '#00-Hyakki already dulled '
                                                                                'her warmth sensitivity '
                                                                                'slightly.',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_kiminami_nekomanma_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N05': {'node_id': 'N05',
                   'chapter_id': 'CH1',
                   'title': 'Waybill Zero-Zero-Hyakki',
                   'day_label': 'Day 2 - 09:00 AM',
                   'location': 'Kamisato Estate - Maple Courtyard',
                   'bgm_bucket': 'hub_cozy',
                   'beats': [{'beat_id': 'N05_B01',
                              'speaker': 'Narrator',
                              'text': 'Morning sunlight filters through crimson maples in the Kamisato '
                                      'Estate courtyard. Kamisato Ayaka kneels across a low cedar table, '
                                      'turning hundred-year-old mulberry pages beside the black-and-gold '
                                      'lacquer box.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B02',
                              'speaker': 'Kamisato Ayaka',
                              'text': 'Thank you for bringing this to my attention, Aether, Paimon, and '
                                      'Miss Kirara. Our shrine-road masons uncovered this parcel beneath a '
                                      'subsided root arch in lower Chinju Forest two nights ago.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B03',
                              'speaker': 'Narrator',
                              'text': "Across the box's lid gleams a delicate gold maki-e crest of twin "
                                      'maple leaves framing a tiny bell, sealed at the seam with dark red '
                                      'customer wax and bound outside by a braided silver-indigo cord.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B04',
                              'speaker': 'Paimon',
                              'text': 'Whoa, not a speck of rot after lying under tree roots! Who sent it, '
                                      'Ayaka?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B05',
                              'speaker': 'Kamisato Ayaka',
                              'text': 'Unlike the Great Hyakkiyakou five centuries ago, a smaller '
                                      'Centenary Autumn Night-Parade of minor youkai and tsukumogami '
                                      'gathered in Chinju Forest exactly one hundred autumns past.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B06',
                              'speaker': 'Kamisato Ayaka',
                              'text': 'This waybill bears an early Komaniya relay mark and a nekomata '
                                      'paw-seal. It was consigned by a Hanamizaka lacquerer named Kajiro '
                                      "to 'The House Beneath Twin Red Maples, Amakane Island.'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B07',
                              'speaker': 'Kirara',
                              'text': 'I ran every lane on Amakane Island at dawn before meeting you! All '
                                      'the old lot numbers were redrawn seventy years ago to widen the '
                                      "festival grounds -- nobody recognized 'Kajiro's House' by that old "
                                      'title.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N05_B08',
                              'speaker': 'Aether',
                              'text': 'What about Lady Yae Miko? If a century-old youkai cord is wrapped '
                                      'around this parcel, the Guuji of Grand Narukami Shrine would know '
                                      'its exact law.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B09',
                              'speaker': 'Kamisato Ayaka',
                              'text': 'I sent a swift runner up Mt. Yougou at sunrise, Aether. Lady Guuji '
                                      'sailed three days ago to preside over outer-island autumn '
                                      "purification rites along Kannazuka's border shrines.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B10',
                              'speaker': 'Kamisato Ayaka',
                              'text': 'Her shrine maiden left word that Lady Miko will return to Grand '
                                      'Narukami Shrine at dusk on Day Seven. Until then, she advised '
                                      'checking the exact brook arch in Chinju Forest where the box '
                                      'surfaced.',
                              'inner_thought': 'Lady Miko returns on Day Seven -- which gives us five days '
                                               "to trace both the forest cord and Kajiro's family line.",
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_yashiro_ledger_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N06'}],
                   'ending_id': None},
           'N06': {'node_id': 'N06',
                   'chapter_id': 'CH1',
                   'title': 'Where the Mist-Cord Tugs',
                   'day_label': 'Day 2 - 04:30 PM',
                   'location': 'Chinju Forest - Outer Moonlit Brook',
                   'bgm_bucket': 'vn_mystic_tension',
                   'beats': [{'beat_id': 'N06_B01',
                              'speaker': 'Narrator',
                              'text': "Stepping beneath Chinju Forest's torii gate feels like crossing "
                                      'from golden afternoon straight into eternal indigo twilight. '
                                      'Glowing blue flowers line the mossy brook while Paimon hovers close '
                                      'to my shoulder.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B02',
                              'speaker': 'Aether',
                              'text': 'Before we go closer to the lower arch, Kirara -- let me hold your '
                                      "satchel on the bank so the mist doesn't chill your wrist.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B03',
                              'speaker': 'Kirara',
                              'text': 'I... I tried leaving the box on my sorting shelf at Komaniya HQ '
                                      'this morning, Aether. The moment I walked ten paces past the '
                                      'doorway, the braided cord yanked straight against my chest like a '
                                      'fishhook.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B04',
                              'speaker': 'Kirara',
                              'text': 'When I infused Dendro into the faded nekomata seal on Night Zero to '
                                      'read the smudged ink, the old pact-cord mistook me for the original '
                                      "twin-tailed courier... and knotted itself to my Vision's thread.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B05',
                              'speaker': 'Narrator',
                              'text': 'As Kirara kneels on a mossy stone above the brook, a ribbon of '
                                      'silver-blue vapor rises from the sunken archway downstream. The '
                                      'braided cord on the lacquer box pulses once -- cold and sharp.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B06',
                              'speaker': 'Narrator',
                              'text': "For three slow heartbeats, Kirara's pupils narrow into vertical "
                                      'emerald slits. She stares transfixed at a wet pebble tumbling in '
                                      'the current, her lips parting without a word.',
                              'inner_thought': 'Her expression just went completely blank -- like a wild '
                                               'forest cat watching water instead of a courier.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B07',
                              'speaker': 'Kirara',
                              'text': "...Shiny stone... wait -- w-waybill! I meant to say 'waybill'! "
                                      'Mrow, why did that word slip right off my tongue for a second?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B08',
                              'speaker': 'Paimon',
                              'text': 'Kirara?! Your hands are shivering -- stay right by Aether!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C03',
                              'prompt': 'Silver-blue brook mist tugs at the braided cord linking the '
                                        "lacquer box to Kirara's Dendro Vision:",
                              'options': [{'opt_id': 'C03_A',
                                           'label': "Steady Kirara's shoulder with one warm hand while "
                                                    'focusing Elemental Sight to inspect the exact weave '
                                                    'of the spirit cord.',
                                           'effects': {'bond': 1,
                                                       'insight': 2,
                                                       'add_flags': ['F03_HITOYO_CORD_WEAVE']},
                                           'next_node': 'N07',
                                           'reaction_beats': [{'beat_id': 'N06_C03A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': "Anchoring Kirara's trembling "
                                                                       'shoulder against my side, I open '
                                                                       'Elemental Sight. A delicate '
                                                                       'emerald-gold filament -- her '
                                                                       'human-world thread, Hitoyo no Ito '
                                                                       '-- shines between her heart and '
                                                                       'her Dendro Vision.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03A_R2',
                                                               'speaker': 'Aether',
                                                               'text': 'I see it clearly now. The indigo '
                                                                       'pact-cord is wound three turns '
                                                                       'counter-clockwise around your '
                                                                       'green thread -- cutting it by '
                                                                       'force would snap both, so it has '
                                                                       'to be unwound from the inside.',
                                                               'inner_thought': 'Clue Secured '
                                                                                '[Counter-Spun Cord '
                                                                                'Weave]: Three '
                                                                                'counter-clockwise turns '
                                                                                'bind the pact-cord around '
                                                                                "Kirara's Hitoyo no Ito.",
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03A_R3',
                                                               'speaker': 'Kirara',
                                                               'text': 'Having your hand on my shoulder '
                                                                       'snapped the fog right out of my '
                                                                       'head... Thank you, Aether. Knowing '
                                                                       "how it's tied makes it way less "
                                                                       'scary!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]},
                                          {'opt_id': 'C03_B',
                                           'label': "Clasp both of Kirara's cold hands immediately and "
                                                    'guide her up out of the damp brook hollow toward '
                                                    'sunlit Byakko Plain.',
                                           'effects': {'bond': 2, 'insight': 1, 'add_flags': []},
                                           'next_node': 'N07',
                                           'reaction_beats': [{'beat_id': 'N06_C03B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Enough mist for one afternoon -- '
                                                                       'hold onto my hands and step up '
                                                                       'onto the dry sunlit ridge with me '
                                                                       'first.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03B_R2',
                                                               'speaker': 'Kirara',
                                                               'text': '...Your palms are always warm, '
                                                                       'like roof tiles after noon sun. '
                                                                       'Sorry for spacing out like a stray '
                                                                       "kitten back there -- my head's "
                                                                       'clear again now!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_chinju_brook_base.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N07': {'node_id': 'N07',
                   'chapter_id': 'CH1',
                   'title': 'Fireflies Over Inazuma City',
                   'day_label': 'Day 3 - 05:50 PM',
                   'location': 'Hanamizaka High Tile Ridge',
                   'bgm_bucket': 'vn_daily_sweet',
                   'beats': [{'beat_id': 'N07_B01',
                              'speaker': 'Narrator',
                              'text': "After a full third day canvassing Hanamizaka's older timber guilds, "
                                      "Paimon curls up early at our Travelers' Inn room beside Aisa "
                                      'Bathhouse with a stack of Yae Publishing House light novels.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B02',
                              'speaker': 'Narrator',
                              'text': 'Outside my window, two light taps sound against the wooden shutter. '
                                      'Kirara perches effortlessly on the eaves, beckoning me up to the '
                                      'highest clay-tile ridge overlooking Inazuma City.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B03',
                              'speaker': 'Kirara',
                              'text': 'Watch your step on that third tile -- it wobbles when autumn dew '
                                      'settles! Here, sit right beside me. Best VIP viewing box in all '
                                      'Narukami, zero Mora admission!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': 'outing_arrive_photo'},
                             {'beat_id': 'N07_B04',
                              'speaker': 'Narrator',
                              'text': 'Below our dangling boots, dusk deepens from plum to velvet indigo. '
                                      'One by one, hundreds of street lanterns flicker awake along '
                                      "Hanamizaka's winding stairs until the whole valley shimmers.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B05',
                              'speaker': 'Aether',
                              'text': 'From up here, the lantern streets really do look like a river of '
                                      'golden fireflies drifting toward the sea.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B06',
                              'speaker': 'Kirara',
                              'text': "Right?! That's the exact sight I stared at from my cedar treetop "
                                      'every winter evening when I was little -- wishing I had hands to '
                                      "carry parcels and a voice to say 'Special delivery!'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N07_B07',
                              'speaker': 'Kirara',
                              'text': 'Human beings pack so much love into tiny boxes, Aether. Dried plums '
                                      "for a homesick guard in Ritou, silk hairpins for a sister's "
                                      'wedding... every box is a warm promise asking to reach a porch.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N07_B08',
                              'speaker': 'Narrator',
                              'text': 'A cool sea breeze lifts a crimson maple leaf past her cheek. Both '
                                      'of her tawny tails slow their cheerful sway and curl closer to the '
                                      'clay tile between our hands.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N08'}],
                   'ending_id': None},
           'N08': {'node_id': 'N08',
                   'chapter_id': 'CH1',
                   'title': 'Two Loops Around Your Wrist',
                   'day_label': 'Day 3 - 06:30 PM',
                   'location': 'Inazuma City Overlook - First Stars',
                   'bgm_bucket': 'vn_tender_romance',
                   'beats': [{'beat_id': 'N08_B01',
                              'speaker': 'Narrator',
                              'text': "Above Tenshukaku's distant silhouette, the first autumn stars "
                                      'pierce the twilight sky. Kirara rests her chin on her knees, '
                                      'courier satchel tucked snugly against her side.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B02',
                              'speaker': 'Kirara',
                              'text': 'Hey, Aether... can I ask something silly? Suppose -- just suppose '
                                      '-- a stray cat forgot every human word she ever learned, and forgot '
                                      'how to walk on two legs.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B03',
                              'speaker': 'Kirara',
                              'text': "Do you think she'd still know how to follow these lantern lights "
                                      'back to the person she wanted to walk beside?',
                              'inner_thought': 'Beneath her light tone, her twin tails are trembling ever '
                                               'so faintly against the roof tile.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B04',
                              'speaker': 'Aether',
                              'text': "You aren't asking about an imaginary cat, Kirara. That moment by "
                                      'Chinju Brook yesterday scared you more than you let on.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B05',
                              'speaker': 'Kirara',
                              'text': 'Ugh, Lady Miko warned me my tails always give away every fib before '
                                      "I finish the sentence! I'm not giving up Waybill Zero-Zero-Hyakki "
                                      "-- I just don't want to vanish mid-route without warning.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C04',
                              'prompt': "Under the first autumn stars, Kirara's twin tails hover shyly "
                                        'beside your wrist on the warm roof tiles:',
                              'options': [{'opt_id': 'C04_A',
                                           'label': 'Hook your pinky finger with hers and set a secret '
                                                    'rooftop tail-code: two loops around your wrist mean '
                                                    "'never go alone.'",
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F04_ROOFTOP_TAIL_CODE']},
                                           'next_node': 'N09',
                                           'reaction_beats': [{'beat_id': 'N08_C04A_R1',
                                                               'speaker': 'Aether',
                                                               'text': "Then let's make a courier's rule "
                                                                       "that doesn't even need human "
                                                                       'words. Hook your pinky with mine '
                                                                       '-- whenever words feel heavy, wrap '
                                                                       'both tails twice around my wrist, '
                                                                       "and I won't let go.",
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_tailcode_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N08_C04A_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Before she even answers aloud, '
                                                                       'both soft, warm tails glide across '
                                                                       'the tile and loop twice around my '
                                                                       'right wrist -- snug as braided '
                                                                       'silk.',
                                                               'inner_thought': 'Clue Secured [Rooftop '
                                                                                'Tail-Code]: Two loops of '
                                                                                "Kirara's twin tails "
                                                                                'around my wrist mean '
                                                                                "'stay right beside me.'",
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_tailcode_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N08_C04A_R3',
                                                               'speaker': 'Kirara',
                                                               'text': 'H-Hey, tails, wait for my pinky '
                                                                       'first! ...Hehe. Pinky-sealed and '
                                                                       'tail-stamped, Aether -- no solo '
                                                                       'detours allowed!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_tailcode_diff.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C04_B',
                                           'label': 'Look calmly into her emerald eyes and promise to '
                                                    'trace every clue of the Chinju cord before her voice '
                                                    'ever fades.',
                                           'effects': {'bond': 1, 'insight': 2, 'add_flags': []},
                                           'next_node': 'N09',
                                           'reaction_beats': [{'beat_id': 'N08_C04B_R1',
                                                               'speaker': 'Aether',
                                                               'text': "You won't have to test whether a "
                                                                       'stray remembers the lanterns, '
                                                                       'Kirara. Tomorrow morning we take '
                                                                       "the ferry to Seirai's Asase Shrine "
                                                                       'and ask the oldest talking cat in '
                                                                       'Inazuma about that seal.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N08_C04B_R2',
                                                               'speaker': 'Kirara',
                                                               'text': 'Provisional Head Priestess Neko! '
                                                                       "Why didn't I think of her?! With a "
                                                                       'partner this sharp, no '
                                                                       'hundred-year mystery stands a '
                                                                       'chance!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch1_rooftop_fireflies_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N09': {'node_id': 'N09',
                   'chapter_id': 'CH2',
                   'title': 'The Cat Who Waited Five Centuries',
                   'day_label': 'Day 4 - 10:00 AM (Seirai Island)',
                   'location': 'Seirai Island - Asase Shrine Porch',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'beats': [{'beat_id': 'N09_B01',
                              'speaker': 'Narrator',
                              'text': "Ever since we calmed Seirai's thunderclouds months ago, the morning "
                                      'ferry from Narukami crosses calm autumn water to Koseki landing in '
                                      'forty-five quiet minutes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B02',
                              'speaker': 'Narrator',
                              'text': "Up on Asase Shrine's sunlit wooden offering box sits Provisional "
                                      'Head Priestess Neko, glossy black fur sleek in the sea breeze while '
                                      'shrine cats nap across the empty floorboards.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B03',
                              'speaker': 'Neko',
                              'text': 'Hm? It is the golden-haired person and the noisy floating child -- '
                                      'and a loud two-tailed calico smelling of cardboard and city ink. '
                                      'Have you brought fish for this shrine?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B04',
                              'speaker': 'Kirara',
                              'text': 'Fresh dried bonito from Ritou, Lady Neko! Please take one look at '
                                      'the paw-seal on this lacquer box in my satchel -- did an older '
                                      'nekomata leave this mark a hundred autumns ago?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N09_B05',
                              'speaker': 'Neko',
                              'text': "Sniff... Ah. That is Kohaku's claw-mark, paired with a Chinju "
                                      'Musubi Pact-Cord. Foolish Kohaku was always running errands for '
                                      'short-lived humans instead of napping in sunbeams.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B06',
                              'speaker': 'Aether',
                              'text': 'Do you know how a Musubi Pact-Cord is untied without hurting the '
                                      'courier carrying it, Neko?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B07',
                              'speaker': 'Neko',
                              'text': 'Only by placing the sealed box before a living heir of the promised '
                                      'doorstep -- or before the Moonless Night of Kogarashi drains the '
                                      "courier's human-thread dry to pay the road toll.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B08',
                              'speaker': 'Neko',
                              'text': 'Though I do not see why losing human words troubles you, little '
                                      'two-tails. Hibiki stepped out five hundred years ago; I simply '
                                      'groom my whiskers on this porch and wait. Villages come and go like '
                                      'clouds.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B09',
                              'speaker': 'Narrator',
                              'text': 'Wind rustles the faded wooden ema plaques around the deserted '
                                      "shrine. Beside me, Kirara's cat-ear ribbons droop low as she looks "
                                      'across the empty courtyard where no human footsteps echo.',
                              'inner_thought': "Neko's peaceful five-hundred-year solitude is the exact "
                                               'mirror of everything Kirara fears becoming.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B10',
                              'speaker': 'Kirara',
                              'text': "...I couldn't wait on an empty porch for a hundred years, Aether. "
                                      "Even if my paws wore thin, I'd rather pack myself into a box and "
                                      'leap straight to the doorstep of the people I love.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_asase_neko_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N10'}],
                   'ending_id': None},
           'N10': {'node_id': 'N10',
                   'chapter_id': 'CH2',
                   'title': "The Maple-Bell Crest & Koharu's Name",
                   'day_label': 'Day 4 - 03:00 PM',
                   'location': "Tenryou Outskirts - Master Gensai's Lacquer Workshop",
                   'bgm_bucket': 'vn_melancholy_memory',
                   'beats': [{'beat_id': 'N10_B01',
                              'speaker': 'Narrator',
                              'text': 'Returning to Narukami after noon, Kirara leads us down a quiet '
                                      "cedar lane behind Tenryou's artisan quarter to deliver raw urushi "
                                      'tree-sap to eighty-two-year-old Master Gensai.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B02',
                              'speaker': 'Narrator',
                              'text': 'Slanted autumn sunlight catches floating gold dust in the workshop. '
                                      "Though cataracts cloud Master Gensai's eyes, his weathered thumb "
                                      'recognizes the raised maki-e crest on the box at first touch.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B03',
                              'speaker': 'Master Gensai',
                              'text': 'Heavens above... twin maple leaves cradling a shrine bell! My late '
                                      'grandfather trained at the bench right beside young Master Kajiro a '
                                      'hundred autumns ago!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B04',
                              'speaker': 'Kirara',
                              'text': "You know Kajiro's family, Master Gensai?! Please -- did his bride "
                                      'ever live beneath the twin red maples on Amakane Island?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': 'outing_bump_rescue'},
                             {'beat_id': 'N10_B05',
                              'speaker': 'Master Gensai',
                              'text': 'His young wife Hina waited there! An autumn fever took poor Kajiro '
                                      'the week of the Night-Parade, yet Hina raised their child beneath '
                                      'those very maples before the festival avenue was renamed.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B06',
                              'speaker': 'Master Gensai',
                              'text': "Better still -- Kajiro and Hina's seventy-four-year-old "
                                      'granddaughter, Madam Koharu, is alive and well today! She tends the '
                                      "Twin-Maple Tea Stall down by Amakane Island's western landing!",
                              'inner_thought': "Madam Koharu -- Kajiro and Hina's 74-year-old "
                                               "granddaughter at Amakane's Twin-Maple Tea Stall! We have "
                                               'our living heir!',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B07',
                              'speaker': 'Paimon',
                              'text': 'Hooray! Then we can run straight over to Amakane Island and hand '
                                      'Madam Koharu the box right now, right?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B08',
                              'speaker': 'Narrator',
                              'text': 'Yet the instant Kirara lifts the box an inch toward the workshop '
                                      'door with Amakane in mind, the indigo Musubi Pact-Cord flashes icy '
                                      'blue and tightens around her right wrist like an iron ring!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B09',
                              'speaker': 'Kirara',
                              'text': "Nngh--! It won't budge off my thread! The pact-cord is still locked "
                                      "to Chinju Forest's root-gate... If I hand this over before the "
                                      'forest knot is discharged, the backlash will hit Grandma Koharu '
                                      'too!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B10',
                              'speaker': 'Master Gensai',
                              'text': "My grandfather's cedar apprentice ledger sits on that high shelf, "
                                      'young Traveler, right beside a mortar of gold maki-e powder my '
                                      'stiff knuckles can scarce grind today.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C05',
                              'prompt': "Now that Madam Koharu's name and Amakane tea stall are known, "
                                        'Master Gensai gestures toward his cedar ledger and gold mortar:',
                              'options': [{'opt_id': 'C05_A',
                                           'label': 'Open the centenary cedar apprentice ledger and copy '
                                                    "Kajiro's three-stroke urushi wax-seal cipher while "
                                                    "steadying Kirara's wrist.",
                                           'effects': {'bond': 1,
                                                       'insight': 2,
                                                       'add_flags': ['F05_WAX_SEAL_CIPHER']},
                                           'next_node': 'N11',
                                           'reaction_beats': [{'beat_id': 'N10_C05A_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Look at this entry from one '
                                                                       'hundred autumns back, Kirara -- '
                                                                       'Kajiro recorded the exact '
                                                                       'three-stroke urushi cipher stamped '
                                                                       'beneath the red customer wax to '
                                                                       'prove true lineage at a spirit '
                                                                       'gate.',
                                                               'inner_thought': "Clue Secured [Kajiro's "
                                                                                'Wax-Seal Cipher]: Copied '
                                                                                'the three-stroke urushi '
                                                                                "cipher linking Kajiro's "
                                                                                "seal to Koharu's branch.",
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05A_R2',
                                                               'speaker': 'Kirara',
                                                               'text': 'You copied every stroke clean onto '
                                                                       'rice paper -- AND helped me set '
                                                                       "Master Gensai's sap jars in order! "
                                                                       'Now once we clear the Chinju knot, '
                                                                       'Grandma Koharu gets her '
                                                                       "grandfather's parcel safe and "
                                                                       'sound!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]},
                                          {'opt_id': 'C05_B',
                                           'label': 'Kneel beside Kirara to warm and grind the gold maki-e '
                                                    "powder so Master Gensai's aged hands can feel his "
                                                    "guild's craft again.",
                                           'effects': {'bond': 2, 'insight': 1, 'add_flags': []},
                                           'next_node': 'N11',
                                           'reaction_beats': [{'beat_id': 'N10_C05B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Kirara and I take turns warming '
                                                                       'the stone pestle until the fine '
                                                                       'gold powder gleams like autumn '
                                                                       "pollen beneath Master Gensai's "
                                                                       'smiling fingertips.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05B_R2',
                                                               'speaker': 'Kirara',
                                                               'text': 'Seeing Master Gensai smile like '
                                                                       'that reminds me why I love every '
                                                                       'stop on my route, Aether. Knowing '
                                                                       'Grandma Koharu is waiting at '
                                                                       'Twin-Maple Tea Stall makes my '
                                                                       'chest feel ten times lighter!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_gensai_lacquer_base.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N11': {'node_id': 'N11',
                   'chapter_id': 'CH2',
                   'title': 'Secret Parcel on the Cedar Path',
                   'day_label': 'Day 5 - 04:00 PM',
                   'location': 'Konda Countryside - Cedar Hedge Path',
                   'bgm_bucket': 'vn_daily_sweet',
                   'beats': [{'beat_id': 'N11_B01',
                              'speaker': 'Narrator',
                              'text': "Late afternoon on Day Five paints Konda's golden rice paddies in "
                                      'warm persimmon light. Back in town, Paimon happily guards our place '
                                      "in line at Tomoki's stall for special dango milk.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B02',
                              'speaker': 'Narrator',
                              'text': 'Down a quiet cedar hedge path away from the main village road, '
                                      'Kirara slows to padded cat-silent steps, cradling a small '
                                      'gift-wrapped bundle of Watatsumi Sango Pearls and a knitted shawl.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B03',
                              'speaker': 'Aether',
                              'text': 'That cedar tree on the ridge behind the thatched roof -- this is '
                                      "your Grandma's house, isn't it?",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B04',
                              'speaker': 'Kirara',
                              'text': "Shh, keep your voice low -- Grandma's taking her afternoon nap "
                                      "inside! I've never brought another person down this path before... "
                                      'not even Miss Chiori.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N11_B05',
                              'speaker': 'Aether',
                              'text': "Why leave 'Mystery Packages' on the veranda instead of knocking and "
                                      'drinking tea with her in human form?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B06',
                              'speaker': 'Kirara',
                              'text': "Normally I'm just shy she'd fuss over me -- though sometimes I "
                                      'still curl up in her lap in cat form! Today, though... if my voice '
                                      "cracked into a meow mid-sentence, she'd worry herself sick.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B07',
                              'speaker': 'Narrator',
                              'text': 'She peeks fondly around the bamboo gatepost, emerald eyes shining '
                                      'with quiet devotion as wind chimes tinkle under the thatched eaves.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N12'}],
                   'ending_id': None},
           'N12': {'node_id': 'N12',
                   'chapter_id': 'CH2',
                   'title': "Sun-Aired Cotton on Grandma's Veranda",
                   'day_label': 'Day 5 - 05:15 PM',
                   'location': "Grandma's Wooden Veranda",
                   'bgm_bucket': 'vn_tender_romance',
                   'beats': [{'beat_id': 'N12_B01',
                              'speaker': 'Narrator',
                              'text': "Right beside the sunny corner of Grandma's wooden veranda sits a "
                                      'weathered square Komaniya Express crate -- patched carefully with '
                                      'cedar slats and lined with a freshly sun-aired cotton cushion.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B02',
                              'speaker': 'Narrator',
                              'text': 'Next to the wooden box rests a clean porcelain saucer of shaved '
                                      'bonito flakes, set out that very afternoon in case a certain tawny '
                                      'kitten wandered home.',
                              'inner_thought': 'Even after years apart, Grandma airs that little cotton '
                                               'cushion in the sun every single week.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B03',
                              'speaker': 'Kirara',
                              'text': '...It still smells like sunshine and dried lavender, just like the '
                                      'day she named me. As long as this little box sits on her porch, '
                                      "part of me knows where 'Kirara' began.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N12_B04',
                              'speaker': 'Narrator',
                              'text': 'When Kirara kneels to tie the silk ribbon around her Sango Pearl '
                                      'gift package, her right fingertips stiffen slightly in the cool '
                                      'dusk -- letting a sharp cat-claw nick the ribbon edge.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B05',
                              'speaker': 'Kirara',
                              'text': "Ah... clumsy claws. Hold still, silly fingers, don't fray Grandma's "
                                      'autumn ribbon...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C06',
                              'prompt': "Sunset warms Kirara's childhood wooden box on the veranda as her "
                                        'stiff right fingers struggle with the gift ribbon:',
                              'options': [{'opt_id': 'C06_A',
                                           'label': 'Sketch two intertwined cat-tails on a maple-paper '
                                                    "slip and tuck it beneath Grandma's sun-warmed cushion "
                                                    'with her.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F06_GRANDMA_BOX_CUSHION']},
                                           'next_node': 'N13',
                                           'reaction_beats': [{'beat_id': 'N12_C06A_R1',
                                                               'speaker': 'Aether',
                                                               'text': "Let's tuck this tiny drawing of "
                                                                       'two happy tails right under the '
                                                                       'cotton cushion alongside the '
                                                                       'pearls -- so Grandma knows her '
                                                                       "kitten grew strong and isn't "
                                                                       'walking alone.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06A_R2',
                                                               'speaker': 'Kirara',
                                                               'text': 'Sniff... Aether, you draw cat ears '
                                                                       'way cuter than you have any right '
                                                                       'to! Look -- even my second tail '
                                                                       'feels warmer just seeing our note '
                                                                       "resting on Grandma's porch!",
                                                               'inner_thought': "Clue Secured [Grandma's "
                                                                                'Box Cushion]: Our '
                                                                                'twin-tail note rests '
                                                                                'beneath the sun-warmed '
                                                                                'cushion where Kirara '
                                                                                'received her name.',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]},
                                          {'opt_id': 'C06_B',
                                           'label': 'Cover her stiffened right fingers gently to finish '
                                                    'tying the silk bow, noting how the claw-slip mirrors '
                                                    'her chilled wrist.',
                                           'effects': {'bond': 1, 'insight': 2, 'add_flags': []},
                                           'next_node': 'N13',
                                           'reaction_beats': [{'beat_id': 'N12_C06B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Give me your right hand for a '
                                                                       'second -- there, clean double bow, '
                                                                       'zero frayed silk. That mist-chill '
                                                                       'is creeping down from your wrist '
                                                                       'into your fingertips every evening '
                                                                       'around sunset.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06B_R2',
                                                               'speaker': 'Kirara',
                                                               'text': 'Nothing gets past you, partner... '
                                                                       "Thank you for saving Grandma's "
                                                                       'ribbon so she only sees a happy '
                                                                       'surprise when she wakes up.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_grandma_porch_base.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N13': {'node_id': 'N13',
                   'chapter_id': 'CH2',
                   'title': 'The Bare Spot Beneath Her Left Bow',
                   'day_label': 'Day 6 - 02:30 PM',
                   'location': 'Hanamizaka - Chioriya Silk Dyeing Loft',
                   'bgm_bucket': 'hub_cozy',
                   'beats': [{'beat_id': 'N13_B01',
                              'speaker': 'Narrator',
                              'text': 'Bolts of emerald, maple-crimson, and Fontaine cream silk hang from '
                                      "cedar rafters inside Chiori's temporary Hanamizaka dyeing loft "
                                      'while Paimon admires a display of miniature kimono sashes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_chioriya_loft_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B02',
                              'speaker': 'Chiori',
                              'text': 'Hold your arms level, Kirara. My trade ship sails back to Fontaine '
                                      'on Day Thirteen, so if you tear your hem scrambling over Chinju '
                                      "rocks next week, I won't be here to mend it.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_chioriya_loft_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B03',
                              'speaker': 'Kirara',
                              'text': 'Hehe, your stitching survived Sumeru desert thorns and Fontaine '
                                      'clockwork rails, Miss Chiori! One little bramble snag is '
                                      'practically a compliment!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_chioriya_loft_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N13_B04',
                              'speaker': 'Narrator',
                              'text': 'Snipping her thread clean, Chiori rises and narrows her sharp amber '
                                      "eyes -- staring straight past Kirara's brass collar bell to the "
                                      'blonde hair right beneath her dark-brown left cat-ear bow.',
                              'inner_thought': "Wait -- look right beneath Kirara's dark-brown left "
                                               'cat-ear bow! That spot is completely bare!',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_chioriya_loft_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B05',
                              'speaker': 'Chiori',
                              'text': 'Both dark-brown cat-ear bows are straight, your collar bell is '
                                      'polished... yet the emerald-and-gold Suzu-Ori silk chime-tassel I '
                                      'wove beneath your left bow is missing, Kirara.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_chioriya_loft_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B06',
                              'speaker': 'Kirara',
                              'text': 'M-Mrow?! Oh! I just unclipped Suzu-Ori onto the pin tray for five '
                                      "minutes so your shears wouldn't catch the silk cord while you "
                                      'checked my collar!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_chioriya_loft_base.jpg',
                              'voice_emotion': 'outing_bump_rescue'},
                             {'beat_id': 'N13_B07',
                              'speaker': 'Chiori',
                              'text': 'Hmph. You begged me to weave a shed, Dendro-blessed strand of your '
                                      "own Hitoyo no Ito into that tassel's core, and haven't taken it off "
                                      'for a single day in a year.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_chioriya_loft_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B08',
                              'speaker': 'Chiori',
                              'text': "I'm stepping into the back room to press a spare obi sash -- and "
                                      'leaving my spare brass loft key on the counter before Day Thirteen. '
                                      'Aether, ask your courier why that chime-tassel went quiet.',
                              'inner_thought': 'Chiori handed me the exact opening: Suzu-Ori holds a '
                                               "living filament of Kirara's own Hitoyo no Ito!",
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_chioriya_loft_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N14'}],
                   'ending_id': None},
           'N14': {'node_id': 'N14',
                   'chapter_id': 'CH2',
                   'title': 'Suzu-Ori on the Maple Balcony',
                   'day_label': 'Day 6 - 03:15 PM',
                   'location': 'Chioriya Loft - Maple Balcony',
                   'bgm_bucket': 'vn_tender_romance',
                   'beats': [{'beat_id': 'N14_B01',
                              'speaker': 'Narrator',
                              'text': "Out on the sunlit maple balcony overlooking Hanamizaka's roofs, "
                                      'Kirara cradles the small emerald-and-gold silk chime-tassel in both '
                                      'palms while Paimon browses fabric swatches inside.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_ribbon_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B02',
                              'speaker': 'Narrator',
                              'text': 'Beneath her dark-brown left cat-ear ribbon, the lock of blonde hair '
                                      'where Suzu-Ori always hangs looks strangely bare in the clear '
                                      'autumn light.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_ribbon_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B03',
                              'speaker': 'Kirara',
                              'text': "Miss Chiori's eyes are scarier than customs inspectors... Look, "
                                      'Aether. Normally, whenever I walk or laugh, the tiny bell on '
                                      'Suzu-Ori chimes softly in time with my human pulse.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_ribbon_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B04',
                              'speaker': 'Kirara',
                              'text': 'Because she wove a blessed strand of my own Hitoyo no Ito inside '
                                      'the silk, it answers my warmth. But twice this morning when the '
                                      "Chinju box pulsed cold, Suzu-Ori didn't make a sound.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_ribbon_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B05',
                              'speaker': 'Kirara',
                              'text': "If I have to wade deeper into Chinju Forest's mud after Lady Miko "
                                      "returns tomorrow... I'm terrified I'll drop Suzu-Ori in the mist "
                                      'and forget it was ever mine.',
                              'inner_thought': "Suzu-Ori isn't an ordinary ornament -- it carries a living "
                                               "strand of Kirara's human-world thread.",
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_ribbon_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C07',
                              'prompt': 'Beneath her bare left cat-ear bow, Kirara holds the Vision-woven '
                                        'Suzu-Ori silk chime-tassel out in trembling palms:',
                              'options': [{'opt_id': 'C07_A',
                                           'label': 'Ask to keep Suzu-Ori safe over your heart until '
                                                    'Waybill #00-Hyakki is delivered, promising to clip it '
                                                    'back yourself.',
                                           'effects': {'bond': 1,
                                                       'insight': 1,
                                                       'add_flags': ['F07_SILK_BELL_RIBBON']},
                                           'next_node': 'N15',
                                           'reaction_beats': [{'beat_id': 'N14_C07A_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Entrust Suzu-Ori to me until we '
                                                                       "finish this delivery, Kirara. I'll "
                                                                       'keep it right inside my breast '
                                                                       'pocket over my heartbeat -- and '
                                                                       'clip it back beneath your left bow '
                                                                       'with my own hands.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_entrust_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07A_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'The instant her fingers place the '
                                                                       'emerald-and-gold silk tassel into '
                                                                       'my open palm, the tiny brass bell '
                                                                       'lets out one clear, sunlit chime '
                                                                       'between our joined hands.',
                                                               'inner_thought': 'Keepsake Entrusted '
                                                                                '[Suzu-Ori Silk '
                                                                                "Chime-Tassel]: Kirara's "
                                                                                'Hitoyo-woven chime-tassel '
                                                                                'rests safe over my heart.',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_entrust_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07A_R3',
                                                               'speaker': 'Kirara',
                                                               'text': 'It chimed right away in your '
                                                                       'hand...! Okay, partner -- hold '
                                                                       'onto my favorite piece of being '
                                                                       "'Kirara' until I earn it back on "
                                                                       'the last porch!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_entrust_diff.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]},
                                          {'opt_id': 'C07_B',
                                           'label': "Cup both of Kirara's trembling hands around Suzu-Ori "
                                                    'against her own warm chest until her heartbeat makes '
                                                    'the bell chime.',
                                           'effects': {'bond': 3, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N15',
                                           'reaction_beats': [{'beat_id': 'N14_C07B_R1',
                                                               'speaker': 'Aether',
                                                               'text': "Feel here, Kirara -- don't hide it "
                                                                       'away like something already lost. '
                                                                       'Rest both hands against your own '
                                                                       'heartbeat with mine until the '
                                                                       'chill passes.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_entrust_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07B_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Wrapped inside my warm palms '
                                                                       "against her collarbone, Kirara's "
                                                                       'breathing steadies -- and after '
                                                                       'three quiet beats, Suzu-Ori '
                                                                       'answers her pulse with a soft, '
                                                                       'golden chime.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_entrust_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07B_R3',
                                                               'speaker': 'Kirara',
                                                               'text': '...You really know how to make a '
                                                                       "girl's heart race loud enough to "
                                                                       'wake brass, Aether. For tonight, '
                                                                       "I'll tuck Suzu-Ori safely inside "
                                                                       'my sleeve pocket so it stays '
                                                                       'clean!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_balcony_entrust_diff.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N15': {'node_id': 'N15',
                   'chapter_id': 'CH2',
                   'title': "The Guuji's Verdict Under Sacred Sakura",
                   'day_label': 'Day 7 - 06:00 PM',
                   'location': 'Grand Narukami Shrine - Sacred Sakura',
                   'bgm_bucket': 'vn_mystic_tension',
                   'beats': [{'beat_id': 'N15_B01',
                              'speaker': 'Narrator',
                              'text': 'Violet dusk gathers beneath the drifting petals of the Sacred '
                                      'Sakura as Guuji Yae Miko returns from her outer-island rites, '
                                      "lifting Kirara's right wrist in the glow of a kitsune ward.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_narukami_miko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B02',
                              'speaker': 'Yae Miko',
                              'text': 'My, my... leave Narukami for five days, and our most diligent '
                                      'little nekomata goes tangling her Hitoyo no Ito inside a centenary '
                                      "Musubi Pact-Cord from Kohaku's era.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_narukami_miko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B03',
                              'speaker': 'Aether',
                              'text': "Can your shrine fire or Ei's blade sever the indigo cord off the "
                                      'lacquer box, Miko?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_narukami_miko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B04',
                              'speaker': 'Yae Miko',
                              'text': 'Perish the thought, little one. Unlike kitsune born of ancient '
                                      'bloodlines, Kirara spun her human form from a fragile thread of '
                                      'name, memory, and human warmth -- Hitoyo no Ito.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_narukami_miko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B05',
                              'speaker': 'Yae Miko',
                              'text': 'That pact-cord is braided straight around her thread. Strike the '
                                      'box with Electro or fox-fire, and Hitoyo no Ito snaps in the same '
                                      'instant -- turning her irreversibly into a mute, one-tailed stray '
                                      'cat.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_narukami_miko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B06',
                              'speaker': 'Kirara',
                              'text': 'How... how long do we have before the Chinju gate calls the waybill '
                                      'due, Lady Miko?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_narukami_miko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B07',
                              'speaker': 'Yae Miko',
                              'text': "Chinju's subterranean root-veins reverse polarity only twice a "
                                      'year, on biannual moonless syzygies: ninety days apart on '
                                      'Early-Spring First-Sakura Night, and forty-eight hours from now.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_narukami_miko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B08',
                              'speaker': 'Yae Miko',
                              'text': 'At 23:00 on Night Nine -- the Moonless Night of Kogarashi -- the '
                                      'sunken Ne-no-Torii arch will demand full delivery. Its outer mist '
                                      'wall rises at 22:50, and the inner ring locks at 22:55.',
                              'inner_thought': 'Forty-eight hours left: Night Nine, 22:50 outer mist wall, '
                                               '22:55 inner lock, 23:00 Kogarashi peak.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_narukami_miko_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B09',
                              'speaker': 'Yae Miko',
                              'text': "Unless an anchor unbound by Teyvat's Ley Lines stands beside her "
                                      "inside Ne-no-Torii at 23:00 to ground the toll in Madam Koharu's "
                                      'name -- or we seal the hollow for ninety days until First-Sakura -- '
                                      'the mist will drink her human self dry.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_narukami_miko_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N16'}],
                   'ending_id': None},
           'N16': {'node_id': 'N16',
                   'chapter_id': 'CH2',
                   'title': 'Dry Thunder on the Lantern Stairs',
                   'day_label': 'Day 7 - 08:00 PM',
                   'location': 'Mt. Yougou Stone Lantern Stairs',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'beats': [{'beat_id': 'N16_B01',
                              'speaker': 'Narrator',
                              'text': 'Sending Paimon ahead down the lower shrine path to order hot ginger '
                                      "tea at the gatehouse, I walk slowly beside Kirara down Mt. Yougou's "
                                      'lantern-lit stone steps.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_stairs_paw_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B02',
                              'speaker': 'Narrator',
                              'text': 'Without warning, a bolt of dry purple lightning flickers silently '
                                      'over distant Seirai waters, followed by a low roll of autumn '
                                      'thunder across the mountain ridge.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_stairs_paw_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B03',
                              'speaker': 'Narrator',
                              'text': 'Kirara gasps and stumbles against the stone railing. Beneath her '
                                      'frayed hem, her right human ankle shimmers in pale blue mist -- '
                                      'reverting for two stark seconds into a bare, trembling cat paw on '
                                      'cold stone.',
                              'inner_thought': "The mist-cord didn't just chill her fingers this time -- "
                                               'her right foot briefly lost its human shape!',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_stairs_paw_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B04',
                              'speaker': 'Kirara',
                              'text': "...D-Don't look, Aether... give me one second and it'll turn "
                                      'back...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_stairs_paw_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B05',
                              'speaker': 'Kirara',
                              'text': 'What if Night Nine comes... and I curl up in an alley box watching '
                                      "rain fall, without remembering Grandma's voice, or Komaniya "
                                      'Express, or even how to call your name...?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_stairs_paw_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B06',
                              'speaker': 'Narrator',
                              'text': 'Silent tears spill over her lower lashes in the stone lantern '
                                      "light. Unclasping my warm traveler's cloak at once, I kneel on the "
                                      'step below her and drape the wool snugly across her trembling '
                                      'shoulders.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_cloak_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C08',
                              'prompt': 'With your warm cloak draped around her shoulders on the stone '
                                        "stairs, Kirara's chilled cat-paw trembles:",
                              'options': [{'opt_id': 'C08_A',
                                           'label': 'Press her cold cat-paw pads gently against your warm '
                                                    "wrist pulse to measure the exact cadence of Chinju's "
                                                    'mist.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F08_PAW_MIST_PULSE']},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_C08A_R1',
                                                               'speaker': 'Aether',
                                                               'text': "Look right at me, Kirara -- I'm "
                                                                       'not looking away. Rest your paw '
                                                                       'against my wrist pulse; every '
                                                                       'seventh beat, the mist ebbs for '
                                                                       'two full seconds when it hits '
                                                                       'outlander warmth.',
                                                               'inner_thought': 'Clue Secured [Mayoi-Giri '
                                                                                'Pulse Cadence]: Every '
                                                                                "seventh beat, Chinju's "
                                                                                'mist recoils for two '
                                                                                'seconds against Descender '
                                                                                'warmth.',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_cloak_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08A_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Against my steady pulse, golden '
                                                                       'warmth flows back into her ankle '
                                                                       'until human toes reform inside her '
                                                                       'sandal strap, her breathing '
                                                                       'evening out beneath my cloak.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_cloak_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C08_B',
                                           'label': 'Cradle her cold paw gently between both of your warm '
                                                    'palms until her twin tails curl tight around your '
                                                    'forearm.',
                                           'effects': {'bond': 2, 'insight': 1, 'add_flags': []},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_C08B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Whether on two human feet or four '
                                                                       "cat paws, you're still Kirara to "
                                                                       "me -- and I'm holding onto you "
                                                                       'until every last bit of warmth '
                                                                       'comes back.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_cloak_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08B_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Warmth steals back through her '
                                                                       'fingers and ankle between my palms '
                                                                       'as both of her fluffy tails wrap '
                                                                       'tight around my forearm under the '
                                                                       'lantern glow.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_shrine_cloak_diff.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N17': {'node_id': 'N17',
                   'chapter_id': 'CH2',
                   'title': 'Three Roads at Komaniya Midnight',
                   'day_label': 'Day 7 - 11:30 PM (48 Hours Before Kogarashi Peak)',
                   'location': 'Komaniya Express - Lantern Courtyard',
                   'bgm_bucket': 'vn_mystic_tension',
                   'pre_events': [{'when': {'forbid_flags': ['F07_SILK_BELL_RIBBON'],
                                            'min_bond': 11,
                                            'min_insight': 7},
                                   'effects': {'add_flags': ['F07_SILK_BELL_RIBBON',
                                                             'F07_SECOND_CHANCE_N17']}}],
                   'beats': [{'beat_id': 'N17_B01',
                              'speaker': 'Narrator',
                              'text': "Near midnight in Komaniya Express's quiet lantern courtyard, Paimon "
                                      'dozes lightly on a mail bench while Kirara and I spread our '
                                      'Narukami map beneath the eaves -- forty-eight hours before Night '
                                      'Nine.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_komaniya_crossroads_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B02',
                              'speaker': 'Kirara',
                              'text': "We know Grandma Koharu is waiting at Amakane's Twin-Maple Tea "
                                      'Stall, and we know Ne-no-Torii opens its corridor at 23:00 on Night '
                                      'Nine. Everything comes down to how we prepare these last two days.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_komaniya_crossroads_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B03_BACKUP',
                              'speaker': 'Narrator',
                              'text': 'Just before rolling up the map under the midnight courtyard '
                                      'lanterns, Kirara pauses, draws the unclipped Suzu-Ori silk '
                                      'chime-tassel from her sleeve pocket, and presses it warmly into my '
                                      'palm.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_komaniya_crossroads_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B04_BACKUP',
                              'speaker': 'Kirara',
                              'text': 'After the mountain stairs tonight... I want you keeping Suzu-Ori '
                                      "over your heart after all, Aether. You've watched every step and "
                                      'listened to every heartbeat -- keep my chime safe till the end!',
                              'inner_thought': 'Keepsake Entrusted [Suzu-Ori Silk Chime-Tassel]: Moved by '
                                               'our bond and perception, Kirara entrusted Suzu-Ori to me!',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_komaniya_crossroads_base.jpg',
                              'voice_emotion': 'vn_tender_love',
                              'when': {'all_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B05_NO_F07',
                              'speaker': 'Narrator',
                              'text': 'Before stepping back into the courtyard, Kirara carefully locks her '
                                      'unclipped Suzu-Ori chime-tassel inside her personal cedar keepsake '
                                      'box in the Komaniya duty room so forest mud cannot stain it.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_komaniya_crossroads_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_SILK_BELL_RIBBON']}},
                             {'beat_id': 'N17_B06',
                              'speaker': 'Aether',
                              'text': "Three strategies stand open before Night Nine's 23:00 Kogarashi "
                                      "convergence, Kirara. Let's choose the road we trust most.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch2_komaniya_crossroads_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C09',
                              'prompt': "Forty-eight hours before Night Nine's 23:00 Kogarashi peak, "
                                        'choose your strategy across Inazuma:',
                              'options': [{'opt_id': 'C09_ROUTE_A',
                                           'label': '[Route A: Lantern-Trail Escort] Rest and wax flares '
                                                    "with Yoimiya tomorrow, then descend into Chinju's "
                                                    'hollow ahead of the mist wall.',
                                           'effects': {'bond': 1, 'insight': 0, 'add_flags': ['ROUTE_A']},
                                           'next_node': 'N18_A1',
                                           'reaction_beats': [{'beat_id': 'N17_C09A_R1',
                                                               'speaker': 'Kirara',
                                                               'text': 'Walking straight down the sunken '
                                                                       'lantern trail side by side, huh? '
                                                                       'Count me in, partner -- with you '
                                                                       'holding the lamp, no forest mirage '
                                                                       'can scare this courier off her '
                                                                       'route!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_komaniya_crossroads_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]},
                                          {'opt_id': 'C09_ROUTE_B',
                                           'label': '[Route B: Tenshukaku & Amakane Accord] Coordinate '
                                                    'with Ayaka, Charlotte, Yae Miko, and Raiden Ei to '
                                                    'forge legal and ley-line keys.',
                                           'effects': {'bond': 0, 'insight': 1, 'add_flags': ['ROUTE_B']},
                                           'next_node': 'N23_B1',
                                           'reaction_beats': [{'beat_id': 'N17_C09B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'While you sort light local mail '
                                                                       'beside Chiori tomorrow, Paimon and '
                                                                       'I will unite Yashiro records, '
                                                                       "Tenshukaku's ward, and Amakane's "
                                                                       'heir deed before meeting you on '
                                                                       'Night Nine.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_komaniya_crossroads_base.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C09_ROUTE_C',
                                           'label': '[Route C: Serenitea Sanctuary Hearth] Shelter Kirara '
                                                    'inside the Serenitea Pot on Byakko Bluff to block '
                                                    "Chinju's external pull.",
                                           'effects': {'bond': 1, 'insight': 0, 'add_flags': ['ROUTE_C']},
                                           'next_node': 'N26_C1',
                                           'reaction_beats': [{'beat_id': 'N17_C09C_R1',
                                                               'speaker': 'Kirara',
                                                               'text': 'Staying inside your famous '
                                                                       'Serenitea Pot on Byakko Bluff '
                                                                       "until Night Nine?! Ooh, I've "
                                                                       'always wanted to curl up on an '
                                                                       'adeptal veranda -- lead the way '
                                                                       'tomorrow afternoon!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/kirara/ch2_komaniya_crossroads_base.jpg',
                                                               'voice_emotion': 'vn_playful_tease'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N18_A1': {'node_id': 'N18_A1',
                      'chapter_id': 'CH3',
                      'title': 'Goldfish Flares on the Sunken Steps',
                      'day_label': 'Day 9 - 03:30 PM',
                      'location': 'Chinju Forest - Sunken Torii Steps',
                      'bgm_bucket': 'vn_mystic_tension',
                      'beats': [{'beat_id': 'N18_B01',
                                 'speaker': 'Narrator',
                                 'text': 'After spending all of Day Eight resting at Komaniya headquarters '
                                         'and coating moisture-proof goldfish flares with Yoimiya, '
                                         "afternoon of Day Nine finds us at Chinju's sunken steps.",
                                 'inner_thought': 'Entering the lower hollow seven hours early lets us '
                                                  'cross the inner sill long before 22:50.',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B02',
                                 'speaker': 'Yoimiya',
                                 'text': 'All six wax-sealed signal tubes are dry and ready, Aether! '
                                         'Paimon and I will hold the Byakko Bluff watchpost with hot rice '
                                         'balls -- tug the flare cord once if the mist turns nasty!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B03',
                                 'speaker': 'Paimon',
                                 'text': "Be super careful down there, you two! Keep Kirara's hands warm "
                                         'and follow the paper cord markers we tied along the upper roots!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B04',
                                 'speaker': 'Kirara',
                                 'text': "Thanks, Yoimiya! Thanks, Paimon! With a full day's sleep and "
                                         'Aether lighting the lantern ahead of my boots, these mossy steps '
                                         'feel way less spooky already!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                 'voice_emotion': 'outing_cruise'},
                                {'beat_id': 'N18_B05',
                                 'speaker': 'Narrator',
                                 'text': 'Raising a warm goldfish oil-lamp in my left hand, I descend into '
                                         'the indigo canopy beside Kirara as the black-and-gold lacquer '
                                         'box hums softly against her hip.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N19_A2'}],
                      'ending_id': None},
           'N19_A2': {'node_id': 'N19_A2',
                      'chapter_id': 'CH3',
                      'title': 'Hollow of Stranded Waybills',
                      'day_label': 'Day 9 - 05:15 PM',
                      'location': 'Hollow of Stranded Waybills',
                      'bgm_bucket': 'vn_mystic_tension',
                      'beats': [{'beat_id': 'N19_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Halfway down the root ravine, pale Bake-Danuki illusion wisps '
                                         'split the stone footbridge into three shifting reflections over '
                                         'rushing dark water.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Wedged beneath a gnarled Sacred Sakura root beside the bridge '
                                         'lies a weathered scrap of indigo hemp stamped with a century-old '
                                         "paw mark -- a remnant of senior courier Kohaku's satchel.",
                                 'inner_thought': 'Kohaku made it this far down the ravine a hundred '
                                                  'autumns ago before the storm mud collapsed.',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B03',
                                 'speaker': 'Kirara',
                                 'text': 'Sniff... the mist is tangling the scent of dry stone with '
                                         'illusions, Aether. My right hand is starting to tingle again -- '
                                         'how should we cross the root bridge?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C10_A',
                                 'prompt': 'Three Bake-Danuki bridge reflections shimmer over the dark '
                                           'root-stream ahead:',
                                 'options': [{'opt_id': 'C10_A1',
                                              'label': 'Trace the old shrine-pilgrim notches carved along '
                                                       'the Sacred Sakura root bark to pick out the true '
                                                       'stone arch.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N20_A3',
                                              'reaction_beats': [{'beat_id': 'N19_C10A1_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Look at the base of the middle '
                                                                          'arch, Kirara -- shrine couriers '
                                                                          'carved three drainage notches '
                                                                          'into real stone, while illusion '
                                                                          'mist never copies water-wear.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N19_C10A1_R2',
                                                                  'speaker': 'Kirara',
                                                                  'text': 'Whoa, good eye! One tap of my '
                                                                          'boot and the two fake bridges '
                                                                          'puffed right back into '
                                                                          'dandelion smoke -- onward we '
                                                                          'go!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                                                  'voice_emotion': 'vn_sweet_happy'}]},
                                             {'opt_id': 'C10_A2',
                                              'label': 'Lift Kirara onto the dry central root-beam beside '
                                                       'you and let her twin tails wrap your forearm to '
                                                       'balance.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N20_A3',
                                              'reaction_beats': [{'beat_id': 'N19_C10A2_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Hold my forearm and match my '
                                                                          "stride, Kirara. A courier's "
                                                                          "balance and an outlander's "
                                                                          "lantern won't be fooled by "
                                                                          'tanuki smoke.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N19_C10A2_R2',
                                                                  'speaker': 'Kirara',
                                                                  'text': 'Hehe, two tails wrapped snug '
                                                                          "around my partner's arm! Even "
                                                                          'the Bake-Danuki are clapping '
                                                                          'from the bushes as we cross!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_chinju_descent_base.jpg',
                                                                  'voice_emotion': 'vn_playful_tease'}]}]},
                      'routing': [],
                      'ending_id': None},
           'N20_A3': {'node_id': 'N20_A3',
                      'chapter_id': 'CH3',
                      'title': 'Mirage of the Nameless Porch',
                      'day_label': 'Day 9 - 07:30 PM',
                      'location': 'Inner Mist Ring - Stray Porch Mirage',
                      'bgm_bucket': 'vn_melancholy_memory',
                      'beats': [{'beat_id': 'N20_B01',
                                 'speaker': 'Narrator',
                                 'text': 'By half past seven, night settles black over the ravine. Just '
                                         'outside the sunken Ne-no-Torii basin, a ring of silver-blue '
                                         'Mayoi-Giri frost-mist coils knee-high across the flagstones.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_porch_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B02',
                                 'speaker': 'Narrator',
                                 'text': "The instant Kirara's sandal touches the mist ring, the forest "
                                         'vanishes into a memory mirage -- a snow-buried mountain shrine '
                                         'porch where a starving, one-tailed kitten shivers alone.',
                                 'inner_thought': "Mayoi-Giri feeds on a youkai's oldest fear -- dragging "
                                                  'her back before she ever had a name!',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_porch_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B03',
                                 'speaker': 'Narrator',
                                 'text': 'Dropping to both knees on the frosted stone, Kirara clutches the '
                                         'humming lacquer box to her ribs as ice crystals rime her '
                                         'eyelashes and her human fingers stiffen.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_porch_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B04',
                                 'speaker': 'Kirara',
                                 'text': "...It's so cold... Nobody's coming up the mountain road tonight, "
                                         'are they...? Why was I pretending a stray cat belonged under '
                                         'warm city lanterns...',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_porch_mirage_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C11_A',
                                 'prompt': 'Frost-mist closes around Kirara inside the snow-porch mirage '
                                           'at 07:30 PM:',
                                 'options': [{'opt_id': 'C11_A1_LANTERN_VOW',
                                              'label': 'Step straight inside the freezing mist ring, cover '
                                                       'her icy hands on the box with yours, and swear a '
                                                       'shared lantern vow.',
                                              'effects': {'bond': 2,
                                                          'insight': 1,
                                                          'add_flags': ['F09_LANTERN_VOW']},
                                              'next_node': 'N29_A4',
                                              'reaction_beats': [{'beat_id': 'N20_C11A1_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': "You aren't on that snowy porch "
                                                                          "anymore, Kirara -- I'm right "
                                                                          'here inside the mist with you! '
                                                                          'Wherever this parcel goes '
                                                                          'tonight, my hands stay over '
                                                                          'yours!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_lantern_vow_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A1_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Golden outlander warmth surges '
                                                                          'from my bare palms across her '
                                                                          'knuckles, shattering the '
                                                                          'snow-porch mirage in a shower '
                                                                          'of warm amber sparks!',
                                                                  'inner_thought': 'Clue Secured [Shared '
                                                                                   'Lantern Vow]: My '
                                                                                   'Descender warmth is '
                                                                                   'now bound directly to '
                                                                                   "Kirara's hands!",
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_lantern_vow_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A1_R3',
                                                                  'speaker': 'Kirara',
                                                                  'text': '...Aether...! Your hands are '
                                                                          'burning warm even inside the '
                                                                          "frost... Thank you -- don't let "
                                                                          'go until we cross that stone '
                                                                          'arch!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_lantern_vow_diff.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C11_A2_TACTICAL_WARD',
                                              'label': 'Hold firm outside the mist seam and cleave the '
                                                       'mirage cleanly with a precision Anemo wind-screen '
                                                       'to spare her stamina.',
                                              'when': {'min_insight': 7},
                                              'unlock_badge': '[INSIGHT 7+] Tactical Anemo Shear',
                                              'lock_hint': '[LOCKED: Requires Insight 7+ to read the outer '
                                                           'mist-shear seam]',
                                              'effects': {'bond': 0,
                                                          'insight': 0,
                                                          'add_flags': ['ROUTE_A_DETACHED']},
                                              'next_node': 'N29_A4',
                                              'reaction_beats': [{'beat_id': 'N20_C11A2_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Stay down and shield your eyes, '
                                                                          'Kirara -- if we both get '
                                                                          'frostbitten before 23:00, '
                                                                          'neither of us will reach the '
                                                                          'inner arch!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_porch_mirage_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A2_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'From two paces outside the '
                                                                          'frost line, my Anemo blade '
                                                                          'slices the mirage clean in '
                                                                          'half. Kirara rises unharmed -- '
                                                                          'yet her gaze lingers quietly on '
                                                                          'the empty space where she '
                                                                          'reached for my hand.',
                                                                  'inner_thought': 'The mirage broke '
                                                                                   'cleanly without '
                                                                                   'draining us, though '
                                                                                   'keeping tactical '
                                                                                   'distance left a quiet '
                                                                                   'chill in her eyes.',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_porch_mirage_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C11_A3_RETREAT_TORII',
                                              'label': "Fire Yoimiya's emergency flare at once and haul "
                                                       'Kirara back up to the outer Chinju gate before the '
                                                       'mist deepens!',
                                              'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N21_BAD1_1',
                                              'reaction_beats': [{'beat_id': 'N20_C11A3_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'This frost is freezing your '
                                                                          "pulse too fast -- I'm pulling "
                                                                          "the emergency flare! We're "
                                                                          'retreating to the upper torii '
                                                                          'right now!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_porch_mirage_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A3_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'A crimson goldfish flare '
                                                                          'streaks up through the canopy '
                                                                          'at 07:35 PM as I lift Kirara '
                                                                          'out of the basin -- leaving '
                                                                          "Waybill #00-Hyakki's "
                                                                          'unfulfilled pull roaring behind '
                                                                          'us.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_porch_mirage_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N21_BAD1_1': {'node_id': 'N21_BAD1_1',
                          'chapter_id': 'CH3',
                          'title': 'Five-Torii Quarantine at 22:30',
                          'day_label': 'Day 9 - 10:30 PM',
                          'location': 'Chinju Outer Torii - Five-Ward Seal',
                          'bgm_bucket': 'vn_mystic_tension',
                          'beats': [{'beat_id': 'N21_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Three hours after our emergency retreat up the ravine, Guuji '
                                             'Yae Miko and four Yashiro shrine maidens plant paper gohei '
                                             "staffs across Chinju's outer stone torii at 10:30 PM.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_five_ward_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B02',
                                     'speaker': 'Narrator',
                                     'text': 'To keep the uncompleted Kogarashi surge from tearing '
                                             "Kirara's soul down the slope at 23:00, Miko seals the "
                                             'lacquer box inside the upper ward-circle and raises the '
                                             'Five-Torii Sacred Sakura Barrier.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_five_ward_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B03',
                                     'speaker': 'Yae Miko',
                                     'text': 'Hold steady, shrine maidens! This Five-Torii Quarantine Seal '
                                             "freezes both the hollow's Kogarashi tide and the ten-pace "
                                             'spatial pull of the Musubi Pact-Cord for ninety days until '
                                             'First-Sakura Night.',
                                     'inner_thought': 'The quarantine freezes the ten-pace tether so '
                                                      'Kirara survives -- yet her thread stays stretched '
                                                      'taut across the barrier.',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_five_ward_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B04',
                                     'speaker': 'Narrator',
                                     'text': 'Violet lightning lattices shut across the torii arch. '
                                             "Kirara's life is spared, yet the stretched thread scrapes "
                                             'her human vocal cords down to a painful, rasping whisper.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_five_ward_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B05',
                                     'speaker': 'Kirara',
                                     'text': "...Kh... I ran away from a customer's parcel, Aether... A "
                                             "courier who abandons her box behind a shrine seal doesn't "
                                             'deserve five stars...',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_five_ward_base.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [{'default': True, 'next_node': 'N22_BAD1_2'}],
                          'ending_id': None},
           'N22_BAD1_2': {'node_id': 'N22_BAD1_2',
                          'chapter_id': 'CH3',
                          'title': 'Autumn Leave at Konda Crossroads',
                          'day_label': 'Day 10 - 08:30 AM',
                          'location': 'Konda Maple Crossroads',
                          'bgm_bucket': 'vn_melancholy_memory',
                          'beats': [{'beat_id': 'N22_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Pale morning sun filters through falling red maples at the '
                                             'Konda crossroads. Wearing a plain autumn shawl without her '
                                             'courier mailbag, Kirara carries only a small woven bamboo '
                                             'basket.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_konda_parting_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_B02',
                                     'speaker': 'Narrator',
                                     'text': 'At dawn she submitted a ninety-day medical leave slip at '
                                             'Komaniya Express, ashamed to face customers while her voice '
                                             'rasps and her right fingers stay numb.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_konda_parting_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_B03',
                                     'speaker': 'Kirara',
                                     'text': '...Until Lady Miko reopens the ward on First-Sakura Night, '
                                             "I'm going to curl up in my small cat form beneath Grandma's "
                                             'wooden veranda... where nobody has to hear my broken voice.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_konda_parting_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_B04_F07',
                                     'speaker': 'Narrator',
                                     'text': 'Stepping forward quietly, I draw Suzu-Ori from my breast '
                                             'pocket and tie the emerald-and-gold silk chime-tassel onto '
                                             'the handle of her bamboo basket so it can watch over her '
                                             'rest.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_konda_parting_base.jpg',
                                     'voice_emotion': '',
                                     'when': {'all_flags': ['F07_SILK_BELL_RIBBON']}},
                                    {'beat_id': 'N22_B04_NOF07',
                                     'speaker': 'Narrator',
                                     'text': 'Tied neatly onto the handle of her woven bamboo basket is '
                                             'Suzu-Ori -- retrieved from her cedar keepsake box at '
                                             'Komaniya headquarters at dawn before she turned in her '
                                             'uniform badge.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_konda_parting_base.jpg',
                                     'voice_emotion': '',
                                     'when': {'forbid_flags': ['F07_SILK_BELL_RIBBON']}}],
                          'choice': {'choice_id': 'C19_BAD1',
                                     'prompt': 'With her cat ears flattened low under the Konda maples, '
                                               'Kirara bows softly to part ways:',
                                     'options': [{'opt_id': 'C19_A_CARRY_SATCHEL',
                                                  'label': 'Carry her bamboo basket silently as far as the '
                                                           'Konda wooden bridge before letting her slip '
                                                           'beneath the eaves.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD1_BRIDGE_ESCORT']},
                                                  'next_node': 'END_BAD_1',
                                                  'reaction_beats': [{'beat_id': 'N22_C19A_R1',
                                                                      'speaker': 'Aether',
                                                                      'text': 'Let me carry your basket to '
                                                                              'the Konda bridge at least, '
                                                                              'Kirara. Rest your voice '
                                                                              "beneath Grandma's porch -- "
                                                                              "I'll still be in Inazuma "
                                                                              'when spring comes.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_konda_parting_base.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N22_C19A_R2',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'At the bridge planks she '
                                                                              'gives one small, tearful '
                                                                              'nod, shifts into a tiny cat '
                                                                              'in a puff of pale '
                                                                              'leaf-light, and vanishes '
                                                                              'alone beneath the distant '
                                                                              'hedge.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_konda_parting_base.jpg',
                                                                      'voice_emotion': ''}]},
                                                 {'opt_id': 'C19_B_PROMISE_SAKURA',
                                                  'label': "Promise gently to wait before Chinju's outer "
                                                           'torii on First-Sakura Night ninety days from '
                                                           'now.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD1_SAKURA_PROMISE']},
                                                  'next_node': 'END_BAD_1',
                                                  'reaction_beats': [{'beat_id': 'N22_C19B_R1',
                                                                      'speaker': 'Aether',
                                                                      'text': "Ninety days isn't forever, "
                                                                              'Kirara. On First-Sakura '
                                                                              "Night, I'll stand at "
                                                                              "Chinju's torii with a fresh "
                                                                              'lantern when Miko lifts the '
                                                                              'ward.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_konda_parting_base.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N22_C19B_R2',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'Suzu-Ori gives one faint, '
                                                                              'lonely chime against her '
                                                                              'basket handle as she bows '
                                                                              'low without trusting her '
                                                                              'voice, turning away down '
                                                                              'the leaf-strewn country '
                                                                              'path.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/kirara/ch3a_bad1_konda_parting_base.jpg',
                                                                      'voice_emotion': ''}]}]},
                          'routing': [],
                          'ending_id': None},
           'N23_B1': {'node_id': 'N23_B1',
                      'chapter_id': 'CH3',
                      'title': 'Monsieur Verite in the Yashiro Archive',
                      'day_label': 'Day 8 - 09:30 AM',
                      'location': 'Yashiro Archive Room',
                      'bgm_bucket': 'hub_cozy',
                      'beats': [{'beat_id': 'N23_B01',
                                 'speaker': 'Narrator',
                                 'text': 'While Kirara rests her chilled fingers sorting light city '
                                         'postcards beside Chiori at Komaniya headquarters, Paimon and I '
                                         'meet Kamisato Ayaka and Charlotte in the Yashiro Archive.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_yashiro_kamera_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B02',
                                 'speaker': 'Charlotte',
                                 'text': "Hold the cedar lamp at thirty degrees, Aether! Monsieur Verite's "
                                         'macro lens can pick out century-old gold-leaf impressions even '
                                         'under faded red wax!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_yashiro_kamera_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B03',
                                 'speaker': 'Kamisato Ayaka',
                                 'text': "Look along the lower border of Waybill #00-Hyakki's rubbing -- "
                                         "'When the outer mist wall rises before Ne-no-Torii, only a "
                                         'Narukami Soul-Bell or a stamped Doorstep Heir Deed may part the '
                                         "veil.'",
                                 'inner_thought': 'Two lawful keys exist if the outer mist wall rises '
                                                  "early: an Electro-attuned Shrine Bell or Koharu's Heir "
                                                  'Deed!',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_yashiro_kamera_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B04',
                                 'speaker': 'Paimon',
                                 'text': "Whoa, Charlotte's Kamera really caught the hidden fine print! "
                                         "Let's head straight up to Tenshukaku this afternoon while Ayaka "
                                         'prepares the commission seal!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_yashiro_kamera_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N24_B2'}],
                      'ending_id': None},
           'N24_B2': {'node_id': 'N24_B2',
                      'chapter_id': 'CH3',
                      'title': "The Shogun's Veranda & Two Keys",
                      'day_label': 'Day 8 - 03:00 PM',
                      'location': 'Tenshukaku Veranda',
                      'bgm_bucket': 'vn_mystic_tension',
                      'beats': [{'beat_id': 'N24_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Afternoon maple shade dapples the high veranda of Tenshukaku as '
                                         'Raiden Ei sets down two porcelain cups of warm dango milk beside '
                                         'Guuji Yae Miko.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_tenshukaku_ei_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_B02',
                                 'speaker': 'Raiden Ei',
                                 'text': "I remember that twin-tailed courier from Mikawa's autumn "
                                         'festival grounds -- nimble, earnest, and fiercely protective of '
                                         'mortal parcels. An eternity built on broken promises would be '
                                         'hollow indeed.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_tenshukaku_ei_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_B03',
                                 'speaker': 'Yae Miko',
                                 'text': 'However, dusk comes swiftly in late autumn, little one. Before '
                                         'Night Nine falls, you only have daylight left to complete one '
                                         'formal rite in full:',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_tenshukaku_ei_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_B04',
                                 'speaker': 'Yae Miko',
                                 'text': 'Either stay here with Ei and me to attune a Sacred Sakura '
                                         "Paper-Bell to split Chinju's mist seam -- or escort the Yashiro "
                                         'elder to Amakane Island so Madam Koharu signs her Grandfather '
                                         "Kajiro's Heir Deed.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_tenshukaku_ei_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C13_B',
                                 'prompt': "On Tenshukaku's veranda, choose which formal key to complete "
                                           'before dusk on Day Eight:',
                                 'options': [{'opt_id': 'C13_B_PAPER_BELL',
                                              'label': 'Attune the Electro-blessed Narukami Paper-Bell '
                                                       'alongside Raiden Ei and Yae Miko to pierce '
                                                       "Chinju's 22:50 mist seam.",
                                              'effects': {'bond': 0,
                                                          'insight': 2,
                                                          'add_flags': ['F10_NARUKAMI_PAPER_BELL']},
                                              'next_node': 'N25_B3',
                                              'reaction_beats': [{'beat_id': 'N24_C13A_R1',
                                                                  'speaker': 'Raiden Ei',
                                                                  'text': 'Hold the folded sakura-paper '
                                                                          'bell steady, Traveler. One calm '
                                                                          'breath of Electro harmonics '
                                                                          "will make Chinju's mist "
                                                                          "recognize the Shogunate's right "
                                                                          'of passage.',
                                                                  'inner_thought': 'Clue Secured [Narukami '
                                                                                   'Paper-Bell Ward]: Ei '
                                                                                   'and Miko attuned a '
                                                                                   'Sakura Paper-Bell to '
                                                                                   'part the 22:50 mist '
                                                                                   'seam!',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_tenshukaku_ei_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N24_C13A_R2',
                                                                  'speaker': 'Yae Miko',
                                                                  'text': 'Hehe, pair that bell with a '
                                                                          "strand of the kitten's own "
                                                                          'thread and a sharp eye for the '
                                                                          "cord's weave, and no fog in "
                                                                          'Chinju will keep you out.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_tenshukaku_ei_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C13_B_MAPLE_DEED',
                                              'label': 'Escort the Yashiro registrar to Amakane Island to '
                                                       "witness Grandma Koharu's thumbprint on Kajiro's "
                                                       'Twin-Maple Heir Deed.',
                                              'effects': {'bond': 2,
                                                          'insight': 0,
                                                          'add_flags': ['F12_AMAKANE_MAPLE_DEED']},
                                              'next_node': 'N25_B3',
                                              'reaction_beats': [{'beat_id': 'N24_C13B_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': "A courier's promise belongs to "
                                                                          'the living family waiting at '
                                                                          "the doorstep. Let's witness "
                                                                          "Madam Koharu's legal heir seal "
                                                                          'on Amakane before sunset.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_tenshukaku_ei_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N24_C13B_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': "Beneath Amakane's twin red "
                                                                          'maples at dusk, '
                                                                          'seventy-four-year-old Madam '
                                                                          'Koharu presses her vermilion '
                                                                          "seal onto Grandfather Kajiro's "
                                                                          'doorstep deed with tear-bright '
                                                                          'gratitude.',
                                                                  'inner_thought': 'Clue Secured '
                                                                                   '[Twin-Maple '
                                                                                   'Inheritance Deed]: '
                                                                                   "Madam Koharu's stamped "
                                                                                   'heir deed legally '
                                                                                   'claims Waybill '
                                                                                   '#00-Hyakki!',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_tenshukaku_ei_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N25_B3': {'node_id': 'N25_B3',
                      'chapter_id': 'CH3',
                      'title': 'Fifty Sheets of Charcoal Names',
                      'day_label': 'Day 8 - 11:15 PM',
                      'location': 'Komaniya Warehouse Loft',
                      'bgm_bucket': 'vn_melancholy_memory',
                      'beats': [{'beat_id': 'N25_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Passing Komaniya Express past eleven at night to drop off warm '
                                         'ginger hand-salve, I notice a single oil lamp still flickering '
                                         'in the quiet upper warehouse loft.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_warehouse_sheets_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Upstairs, Kirara has fallen fast asleep curled over her canvas '
                                         'mailbag. Two paces beside the low desk, the sealed lacquer box '
                                         'rests on a wooden crate well inside its ten-pace tether.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_warehouse_sheets_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B03',
                                 'speaker': 'Narrator',
                                 'text': 'Scattered across the floorboards and desk lie fifty sheets of '
                                         'rough mulberry paper smudged black with charcoal -- three words '
                                         'written over and over in crooked, numbing strokes:',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_warehouse_sheets_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B04',
                                 'speaker': 'Narrator',
                                 'text': "'Kirara. Grandma. Aether. Kirara. Grandma. Aether.' On the final "
                                         'sheet beneath her charcoal-stained right knuckles, a dry tear '
                                         "ring circles: 'Do not forget how to write his name.'",
                                 'inner_thought': 'All evening while I gathered seals in town, she fought '
                                                  "her numbing fingers alone so she wouldn't forget my "
                                                  'name...',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_warehouse_sheets_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B05',
                                 'speaker': 'Kirara',
                                 'text': "...Mm... five stars... Aether... don't let me turn back into a "
                                         'nameless cat...',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_warehouse_sheets_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B06',
                                 'speaker': 'Narrator',
                                 'text': 'Swallowing the ache in my throat, I drape a clean wool blanket '
                                         'gently over her shoulders without waking her, vowing that '
                                         'tomorrow night no wall of mist will stand between us.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3b_warehouse_sheets_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N31_B4'}],
                      'ending_id': None},
           'N26_C1': {'node_id': 'N26_C1',
                      'chapter_id': 'CH3',
                      'title': 'Sanctuary on Sakura-Hued Street',
                      'day_label': 'Day 8 - 02:00 PM',
                      'location': 'Serenitea Pot - Sakura-Hued Street',
                      'bgm_bucket': 'vn_daily_sweet',
                      'beats': [{'beat_id': 'N26_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Setting the Serenitea Pot inside a sheltered maple hollow on '
                                         'Byakko Bluff overlooking Chinju Forest, I guide Kirara and '
                                         'Paimon into the golden afternoon of Silken Courtyard.',
                                 'inner_thought': "Inside the Realm Within, Chinju's external mist cannot "
                                                  "tug at Kirara's thread until we step back out.",
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_teapot_street_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B02',
                                 'speaker': 'Tubby',
                                 'text': 'Welcome to Silken Courtyard, Miss Kirara. My adeptal screen will '
                                         "block the forest's external pull until tomorrow night -- though "
                                         'do keep that lacquer box within ten paces of your side.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_teapot_street_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B03',
                                 'speaker': 'Kirara',
                                 'text': 'Whoa...! Floating islands, warm autumn sunshine, and zero creepy '
                                         'mist! Thank you so much, Lady Tubby -- even my ears feel lighter '
                                         'already!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_teapot_street_base.jpg',
                                 'voice_emotion': 'outing_arrive_photo'},
                                {'beat_id': 'N26_B04',
                                 'speaker': 'Chiori',
                                 'text': 'Hold still a second, Kirara. Since Aether lent me a Realm '
                                         'Dispatch pass, I brought fresh emerald thread for your hem -- '
                                         'and left my spare Hanamizaka loft key on your tray before my Day '
                                         'Thirteen ship to Fontaine.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_teapot_street_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B05',
                                 'speaker': 'Aether',
                                 'text': 'Rest easy inside the courtyard until tomorrow evening, Kirara. '
                                         'Here on Sakura-Hued Street, the clock belongs to us.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_teapot_street_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N27_C2'}],
                      'ending_id': None},
           'N27_C2': {'node_id': 'N27_C2',
                      'chapter_id': 'CH3',
                      'title': 'Tea Pavilion & Delivery Notes',
                      'day_label': 'Day 8 - 04:30 PM',
                      'location': 'Sakura-Hued Courtyard Pavilion',
                      'bgm_bucket': 'hub_cozy',
                      'beats': [{'beat_id': 'N27_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Late afternoon breeze drifts petals across the courtyard tea '
                                         'pavilion after Chiori returns to town. Paimon happily stacks '
                                         'tricolor dango on porcelain plates while Kirara bends over a '
                                         'small notebook.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_teapot_street_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B02',
                                 'speaker': 'Paimon',
                                 'text': "Hey Kirara, stop working on your day off! You've been drawing "
                                         'tiny roof arrows and dog warnings for every house in Hanamizaka '
                                         'for an entire hour!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_teapot_street_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B03',
                                 'speaker': 'Kirara',
                                 'text': 'Ehehe, force of habit, Paimon! Every courier keeps backup route '
                                         "notes... like how Granny Tomo on the third slope can't hear soft "
                                         'knocking, so you tap the wind-bell twice instead!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_teapot_street_base.jpg',
                                 'voice_emotion': 'vn_sweet_happy'},
                                {'beat_id': 'N27_B04',
                                 'speaker': 'Narrator',
                                 'text': 'She closes the notebook quickly with a bright smile, yet I catch '
                                         'her rubbing her right knuckles quietly beneath the table cloth '
                                         'when she thinks neither of us is watching.',
                                 'inner_thought': 'Even sheltered inside the Serenitea Pot, the box '
                                                  'sitting beside her bench is still slowly chilling her '
                                                  'right hand.',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_teapot_street_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N28_C3'}],
                      'ending_id': None},
           'N28_C3': {'node_id': 'N28_C3',
                      'chapter_id': 'CH3',
                      'title': 'Boxwood Comb on the Evening Engawa',
                      'day_label': 'Day 8 - 07:30 PM',
                      'location': 'Silken Courtyard Engawa',
                      'bgm_bucket': 'vn_tender_romance',
                      'beats': [{'beat_id': 'N28_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Warm paper lanterns glow along the wooden engawa at half past '
                                         'seven. Upstairs in the mansion loft, Paimon has already curled '
                                         'up early on a pile of silk cushions.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_engawa_tailbrush_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Dressed in a soft emerald indoor haori with the sealed lacquer '
                                         'box resting two paces down the veranda, Kirara sits beside me '
                                         'holding out a smooth boxwood comb with bashful hope.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_engawa_tailbrush_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B03',
                                 'speaker': 'Kirara',
                                 'text': "Um... since there's nobody else awake on the veranda tonight, "
                                         'Aether... would you mind helping brush the burrs out of my '
                                         'tails? My right fingers keep slipping on the comb...',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_engawa_tailbrush_base.jpg',
                                 'voice_emotion': 'vn_shy_blush'}],
                      'choice': {'choice_id': 'C16_C',
                                 'prompt': 'Under the warm veranda lanterns at 07:30 PM, Kirara rests her '
                                           'twin tails across the tatami beside her notebook:',
                                 'options': [{'opt_id': 'C16_C1',
                                              'label': 'Gently notice that her afternoon notebook is '
                                                       'written as a route-handover guide for another '
                                                       'courier, and ask quietly.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N35_C4',
                                              'reaction_beats': [{'beat_id': 'N28_C16C1_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'As I take the comb, I notice '
                                                                          'the title on your notebook '
                                                                          "cover: 'For Whoever Takes Over "
                                                                          "Hanamizaka Route 3.' You were "
                                                                          'writing a handover manual in '
                                                                          'case tomorrow goes wrong, '
                                                                          "weren't you?",
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_engawa_tailbrush_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N28_C16C1_R2',
                                                                  'speaker': 'Kirara',
                                                                  'text': '...Nothing gets past you, '
                                                                          "partner. I just couldn't bear "
                                                                          'Granny Tomo missing her '
                                                                          "medicine parcel if I'm not me "
                                                                          "anymore... Promise you'll keep "
                                                                          'brushing till I stop worrying?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_engawa_tailbrush_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C16_C2',
                                              'label': 'Brush both fluffy tails from root to tip with '
                                                       'slow, gentle strokes while telling stories of '
                                                       'starlit worlds beyond Teyvat.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N35_C4',
                                              'reaction_beats': [{'beat_id': 'N28_C16C2_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Leave every tangle to me, '
                                                                          'Kirara. Sit back against my '
                                                                          "shoulder, and I'll tell you "
                                                                          'about an autumn sea of golden '
                                                                          'reeds I once crossed between '
                                                                          'two stars.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_engawa_tailbrush_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N28_C16C2_R2',
                                                                  'speaker': 'Kirara',
                                                                  'text': 'Prrr... mmm, your hands are so '
                                                                          'warm and steady, Aether... '
                                                                          'Traveling across real stars '
                                                                          'with you sounds like the best '
                                                                          'special delivery in the '
                                                                          'universe...',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch3c_engawa_tailbrush_base.jpg',
                                                                  'voice_emotion': 'vn_tender_love'}]}]},
                      'routing': [],
                      'ending_id': None},
           'N29_A4': {'node_id': 'N29_A4',
                      'chapter_id': 'CH4',
                      'title': 'Warm Rice Balls Inside the Root Arch',
                      'day_label': 'Day 9 - 09:00 PM',
                      'location': 'Sunken Chamber Inside Ne-no-Torii',
                      'bgm_bucket': 'vn_tender_romance',
                      'beats': [{'beat_id': 'N29_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Crossing the inner stone sill of Ne-no-Torii at 08:45 PM -- more '
                                         'than two hours before the outer mist wall can rise -- we claim '
                                         'dry shelter inside a root-vaulted chamber.',
                                 'inner_thought': 'We are safely inside the inner threshold ahead of '
                                                  'schedule; no outer mist wall can lock us apart now.',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N29_B02',
                                 'speaker': 'Narrator',
                                 'text': "At nine o'clock sharp, three lively tugs ring down a braided "
                                         'hemp cord through an overhead root-chimney, lowering a bamboo '
                                         "thermal basket from Yoimiya and Paimon's bluff post.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N29_B03',
                                 'speaker': 'Kirara',
                                 'text': "Oh! Look at Paimon's little doodle pinned to the lid: 'Eat up so "
                                         "your tails stay extra fluffy!' And Yoimiya packed bonito-flake "
                                         'nekomanma rice balls wrapped in warm bamboo leaves!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                 'voice_emotion': 'vn_sweet_happy',
                                 'when': {'forbid_flags': ['ROUTE_A_DETACHED']}},
                                {'beat_id': 'N29_B03_DETACHED',
                                 'speaker': 'Kirara',
                                 'text': 'Yoimiya and Paimon lowered hot bonito rice balls in a thermal '
                                         'basket... Thank you for guiding us inside the stone sill before '
                                         'the mist wall rises, Aether.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['ROUTE_A_DETACHED']}},
                                {'beat_id': 'N29_B04',
                                 'speaker': 'Aether',
                                 'text': "Eat while they're gently warm, Kirara. We have an hour and forty "
                                         'minutes inside the vault to steady your pulse before the 22:55 '
                                         'inner seal.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N30_A5'}],
                      'ending_id': None},
           'N30_A5': {'node_id': 'N30_A5',
                      'chapter_id': 'CH4',
                      'title': 'Before the Root-Torii Pillar',
                      'day_label': 'Day 9 - 10:40 PM',
                      'location': 'Before the Root-Torii Pillar',
                      'bgm_bucket': 'vn_mystic_tension',
                      'beats': [{'beat_id': 'N30_B01',
                                 'speaker': 'Narrator',
                                 'text': 'At 10:40 PM, deep subterranean chimes echo up through the stone '
                                         'roots of Ne-no-Torii. Behind us, silver mist begins rising '
                                         "outside the sill right on Miko's warning.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N30_B02',
                                 'speaker': 'Narrator',
                                 'text': 'On the lacquer box lid, the indigo Musubi Pact-Cord coils '
                                         "counter-clockwise toward Kirara's right wrist, testing our "
                                         'anchor fifteen minutes before the corridor opens.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N30_B03',
                                 'speaker': 'Kirara',
                                 'text': 'Ten minutes until the outer wall seals, fifteen until the Hyakki '
                                         'corridor opens... How should we brace my thread before the bell '
                                         'strikes eleven, Aether?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C12_A',
                                 'prompt': 'At 10:40 PM inside Ne-no-Torii, the indigo mist-cord tightens '
                                           "around Kirara's right wrist:",
                                 'options': [{'opt_id': 'C12_A1_COUNTER_KNOT',
                                              'label': 'Weave a clockwise golden Descender counter-knot '
                                                       'timed to every seventh ley-pulse beat around her '
                                                       'wrist.',
                                              'when': {'all_flags': ['F09_LANTERN_VOW'],
                                                       'any_flags': ['F03_HITOYO_CORD_WEAVE',
                                                                     'F05_WAX_SEAL_CIPHER'],
                                                       'min_count_in': {'count': 1,
                                                                        'pool': ['F08_PAW_MIST_PULSE',
                                                                                 'F11_CAT_TONGUE_CHILL']},
                                                       'min_insight': 9},
                                              'unlock_badge': '[CLUE CONVERGENCE] Descender Counter-Knot',
                                              'lock_hint': '[LOCKED: Needs Lantern Vow + Cord/Cipher Clue '
                                                           '+ Pulse/Chill Clue + Insight 9+]',
                                              'effects': {'bond': 2,
                                                          'insight': 0,
                                                          'add_flags': ['A_CORD_TUNED']},
                                              'next_node': 'N38_CH5_CONVERGE',
                                              'reaction_beats': [{'beat_id': 'N30_C12A1_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'The mist-cord spins '
                                                                          'counter-clockwise and recoils '
                                                                          'every seventh beat -- hold my '
                                                                          "hand, Kirara, and let's lock a "
                                                                          'clockwise golden loop right '
                                                                          'between its coils!',
                                                                  'inner_thought': 'Counter-Knot Attuned: '
                                                                                   'Combining our Lantern '
                                                                                   "Vow with the cord's "
                                                                                   'spin and pulse '
                                                                                   'neutralizes the '
                                                                                   'recoil!',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N30_C12A1_R2',
                                                                  'speaker': 'Kirara',
                                                                  'text': 'Whoa...! The icy tug on my '
                                                                          'wrist went gentle all at once '
                                                                          '-- your golden thread fits '
                                                                          'right around my Hitoyo no Ito '
                                                                          'like warm sunlight!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                                                  'voice_emotion': 'vn_tender_love'}]},
                                             {'opt_id': 'C12_A2_TAILCODE_BRIDGE',
                                              'label': 'Hold out your bare wrist and invoke your '
                                                       "Hanamizaka rooftop pinky-vow: 'Two tail loops mean "
                                                       "never go alone.'",
                                              'when': {'all_flags': ['ROUTE_A_DETACHED',
                                                                     'F04_ROOFTOP_TAIL_CODE'],
                                                       'min_count_in': {'count': 1,
                                                                        'pool': ['F01_FIVE_STAR_STAMP',
                                                                                 'F02_NEKOMANMA_HEARTH',
                                                                                 'F06_GRANDMA_BOX_CUSHION']}},
                                              'unlock_badge': '[TAIL-CODE REDEMPTION] Twin-Tail Wrist '
                                                              'Promise',
                                              'lock_hint': '[LOCKED: Needs Tactical Ward Path + Rooftop '
                                                           'Tail-Code + Warmth Anchor]',
                                              'effects': {'bond': 2,
                                                          'insight': 0,
                                                          'remove_flags': ['ROUTE_A_DETACHED'],
                                                          'add_flags': ['ROUTE_A_REDEEMED']},
                                              'next_node': 'N38_CH5_CONVERGE',
                                              'reaction_beats': [{'beat_id': 'N30_C12A2_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Forgive me for standing back '
                                                                          'outside the frost ring earlier, '
                                                                          "Kirara. On Hanamizaka's roof we "
                                                                          'swore a code -- wrap both tails '
                                                                          "twice around my wrist and don't "
                                                                          'take a single step alone.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N30_C12A2_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Every trace of guarded distance '
                                                                          'melts from her emerald eyes; in '
                                                                          'an instant, both fluffy tails '
                                                                          'coil twice around my bare wrist '
                                                                          'as her fingers lace tight '
                                                                          'through mine!',
                                                                  'inner_thought': 'Bond Restored [Rooftop '
                                                                                   'Tail-Code]: Our '
                                                                                   'rooftop promise '
                                                                                   'bridged the distance '
                                                                                   'from the frost mirage '
                                                                                   'completely!',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N30_C12A2_R3',
                                                                  'speaker': 'Kirara',
                                                                  'text': '...Dummy! I was waiting for you '
                                                                          'to hold your wrist out like on '
                                                                          'the roof! Two loops locked '
                                                                          "tight -- you're stuck with me "
                                                                          'all the way through the gate '
                                                                          'now!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                                                  'voice_emotion': 'vn_tender_love'}]},
                                             {'opt_id': 'C12_A3_MIST_CURRENT_READ',
                                              'label': 'Plant your blade into the Sacred Sakura root-vein '
                                                       'to map the shifting ley-current before the 22:55 '
                                                       'lock.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N38_CH5_CONVERGE',
                                              'reaction_beats': [{'beat_id': 'N30_C12A3_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Stand close behind my shoulder, '
                                                                          'Kirara -- grounding my blade '
                                                                          'into this main root-vein shows '
                                                                          'us the exact angle the corridor '
                                                                          'will open at 22:55.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N30_C12A3_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Pale ley-lines illuminate the '
                                                                          'carved stone floor beneath our '
                                                                          'boots, bracing our footing as '
                                                                          'the outer mist wall seals '
                                                                          'behind the arch.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4a_root_torii_anchor_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N31_B4': {'node_id': 'N31_B4',
                      'chapter_id': 'CH4',
                      'title': 'Reunion Under Amakane Lanterns',
                      'day_label': 'Day 9 - 09:30 PM',
                      'location': 'Amakane Island - Twin-Maple Tea Stall',
                      'bgm_bucket': 'vn_tender_romance',
                      'beats': [{'beat_id': 'N31_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Once the Yashiro night courier delivers the final stamped '
                                         'dispatch at nine-fifteen, I sprint across the wooden causeway to '
                                         "Amakane Island's quiet Twin-Maple Tea Stall at 09:30 PM.",
                                 'inner_thought': "Seventy-five minutes' brisk march from Amakane across "
                                                  'Hanamizaka Bridge brings us to Chinju by 22:45.',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_amakane_reunion_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N31_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Waiting beneath the shuttered tea-stall lantern with the lacquer '
                                         'box strapped snug at her hip, Kirara brightens the instant she '
                                         'spots me -- faint charcoal smudges still tinting her right '
                                         'fingertips.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_amakane_reunion_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N31_B03',
                                 'speaker': 'Kirara',
                                 'text': 'You made it right on time, partner! Grandma Koharu left two warm '
                                         'roasted-barley charms hanging on the post for our walk to Chinju '
                                         'Forest -- seventy-five minutes to the sunken gate!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_amakane_reunion_base.jpg',
                                 'voice_emotion': 'greet_doorstep'}],
                      'choice': {'choice_id': 'C14_B',
                                 'prompt': "Beneath Amakane's red-maple lantern at 09:30 PM before the "
                                           'seventy-five-minute march to Chinju:',
                                 'options': [{'opt_id': 'C14_B1',
                                              'label': 'Synchronize every step of the wax-cipher and '
                                                       'mist-wall timing with Kirara as you set off toward '
                                                       'Hanamizaka Bridge.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N32_B5_GATE1',
                                              'reaction_beats': [{'beat_id': 'N31_C14B1_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': "Let's rehearse the sequence as "
                                                                          'we march, Kirara: reach the '
                                                                          'steps by 22:45, keep inside '
                                                                          'five paces of the sill, and '
                                                                          'align our seals before 22:50.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_amakane_reunion_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N31_C14B1_R2',
                                                                  'speaker': 'Kirara',
                                                                  'text': 'Got it! Every landmark and turn '
                                                                          'memorized down to the second -- '
                                                                          'Komaniya Express never misses a '
                                                                          'timed window!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_amakane_reunion_base.jpg',
                                                                  'voice_emotion': 'outing_cruise'}]},
                                             {'opt_id': 'C14_B2',
                                              'label': 'Cup her charcoal-smudged right fingers warmly '
                                                       'between your palms and promise to guard every '
                                                       'letter of her name.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N32_B5_GATE1',
                                              'reaction_beats': [{'beat_id': 'N31_C14B2_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'I stopped by the warehouse loft '
                                                                          'with hand-salve last night, '
                                                                          "Kirara. You won't ever have to "
                                                                          'write our names alone in the '
                                                                          "dark again -- I'm holding onto "
                                                                          'them with you.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_amakane_reunion_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N31_C14B2_R2',
                                                                  'speaker': 'Kirara',
                                                                  'text': '...Y-You saw all fifty practice '
                                                                          'sheets?! Mrow, my ears are '
                                                                          "burning hotter than Yoimiya's "
                                                                          'sparklers... Hold my hand tight '
                                                                          'all the way to Chinju, okay?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_amakane_reunion_base.jpg',
                                                                  'voice_emotion': 'vn_shy_blush'}]}]},
                      'routing': [],
                      'ending_id': None},
           'N32_B5_GATE1': {'node_id': 'N32_B5_GATE1',
                            'chapter_id': 'CH4',
                            'title': 'The 22:50 Mist Wall Before Ne-no-Torii',
                            'day_label': 'Day 9 - 10:50 PM',
                            'location': 'Chinju Ne-no-Torii Outer Mist Wall',
                            'bgm_bucket': 'vn_mystic_tension',
                            'beats': [{'beat_id': 'N32_B01',
                                       'speaker': 'Narrator',
                                       'text': 'Breathing hard beneath swaying indigo cedars, we reach '
                                               "Chinju's sunken steps at 10:45 PM -- only for an early "
                                               'tremor from the moonless root-vein to convulse the lacquer '
                                               'box at 10:48!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_mistwall_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N32_B02',
                                       'speaker': 'Narrator',
                                       'text': 'Before my hand can catch her belt sash, the indigo Musubi '
                                               'Pact-Cord yanks Kirara six paces across the inner stone '
                                               'sill of Ne-no-Torii!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_mistwall_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N32_B03',
                                       'speaker': 'Narrator',
                                       'text': 'At 10:50 PM sharp, a roaring silver wall of Mayoi-Giri '
                                               'mist erupts up from the threshold crack between us -- five '
                                               'minutes left before the inner ring locks forever at 10:55!',
                                       'inner_thought': 'Five minutes until 22:55! Without a homing thread '
                                                        'to Kirara AND a lawful seam key, my blade will '
                                                        'only bounce off!',
                                       'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_mistwall_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N32_B04',
                                       'speaker': 'Kirara',
                                       'text': "Aether--! Don't strike the mist with raw force or it'll "
                                               "snap my thread! Stay back if it's dangerous -- I can still "
                                               'hear you through the fog!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_mistwall_base.jpg',
                                       'voice_emotion': ''}],
                            'choice': {'choice_id': 'C15_B_GATE1',
                                       'exclusive_rescue_gate': True,
                                       'prompt': 'COMBINATION GATE #1 -- 22:50 Outer Mist Wall! Five '
                                                 'minutes remain before Ne-no-Torii locks Kirara inside '
                                                 'alone:',
                                       'options': [{'opt_id': 'C15_B_COMBO_UNLOCK',
                                                    'label': "Raise Suzu-Ori's living thread with your "
                                                             'Tenshukaku/Amakane key and wax-cord insight '
                                                             'to part the 22:50 mist seam!',
                                                    'when': {'all_flags': ['F07_SILK_BELL_RIBBON'],
                                                             'any_of': [{'all_flags': ['F10_NARUKAMI_PAPER_BELL'],
                                                                         'any_flags': ['F03_HITOYO_CORD_WEAVE',
                                                                                       'F05_WAX_SEAL_CIPHER'],
                                                                         'min_count_in': {'count': 1,
                                                                                          'pool': ['F02_NEKOMANMA_HEARTH',
                                                                                                   'F04_ROOFTOP_TAIL_CODE',
                                                                                                   'F06_GRANDMA_BOX_CUSHION',
                                                                                                   'F08_PAW_MIST_PULSE']},
                                                                         'min_insight': 11},
                                                                        {'all_flags': ['F12_AMAKANE_MAPLE_DEED',
                                                                                       'F05_WAX_SEAL_CIPHER'],
                                                                         'min_count_in': {'count': 1,
                                                                                          'pool': ['F01_FIVE_STAR_STAMP',
                                                                                                   'F08_PAW_MIST_PULSE',
                                                                                                   'F11_CAT_TONGUE_CHILL']},
                                                                         'min_insight': 9}]},
                                                    'unlock_badge': '[COMBINATION GATE #1 CLEARED] '
                                                                    'Suzu-Ori Mist-Seam Breach',
                                                    'lock_hint': '[LOCKED: Needs Suzu-Ori + '
                                                                 '(Paper-Bell/Cord-Cipher/Warmth/Insight '
                                                                 '11+ OR '
                                                                 'Maple-Deed/Wax-Cipher/Clue/Insight 9+)]',
                                                    'effects': {'bond': 2,
                                                                'insight': 1,
                                                                'add_flags': ['COMBO1_CLEARED']},
                                                    'next_node': 'N38_CH5_CONVERGE',
                                                    'reaction_beats': [{'beat_id': 'N32_C15_F10_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': "Binding Suzu-Ori's "
                                                                                'emerald Hitoyo strand to '
                                                                                "Ei and Miko's Sakura "
                                                                                'Paper-Bell, I ring the '
                                                                                'chime straight into the '
                                                                                'counter-spun seam on the '
                                                                                'seventh pulse -- cleaving '
                                                                                'a golden doorway through '
                                                                                'the silver wall at 10:53 '
                                                                                'PM!',
                                                                        'inner_thought': 'Combination Gate '
                                                                                         '#1 Cleared '
                                                                                         '[Paper-Bell '
                                                                                         'Resonance]: '
                                                                                         'Suzu-Ori + '
                                                                                         'Narukami '
                                                                                         'Paper-Bell '
                                                                                         'parted the mist '
                                                                                         'wall!',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_breakthrough_diff.jpg',
                                                                        'voice_emotion': '',
                                                                        'when': {'all_flags': ['F10_NARUKAMI_PAPER_BELL']}},
                                                                       {'beat_id': 'N32_C15_F12_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': "Wrapping Suzu-Ori's "
                                                                                'emerald Hitoyo strand '
                                                                                "around Madam Koharu's "
                                                                                'vermilion-stamped '
                                                                                'Twin-Maple Deed, I align '
                                                                                "Kajiro's three-stroke "
                                                                                'cipher against the mist '
                                                                                'wall -- parting a golden '
                                                                                'doorway at 10:53 PM!',
                                                                        'inner_thought': 'Combination Gate '
                                                                                         '#1 Cleared '
                                                                                         '[Doorstep Heir '
                                                                                         'Accord]: '
                                                                                         'Suzu-Ori + '
                                                                                         "Koharu's Heir "
                                                                                         'Deed parted the '
                                                                                         'mist wall!',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_breakthrough_diff.jpg',
                                                                        'voice_emotion': '',
                                                                        'when': {'forbid_flags': ['F10_NARUKAMI_PAPER_BELL']}},
                                                                       {'beat_id': 'N32_C15_R2',
                                                                        'speaker': 'Aether',
                                                                        'text': 'Got your hand, Kirara! '
                                                                                'Did you really think your '
                                                                                'five-star escort would '
                                                                                'let a wall of fog make '
                                                                                'you deliver alone?!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_breakthrough_diff.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N32_C15_R3',
                                                                        'speaker': 'Kirara',
                                                                        'text': 'Aether--!! Suzu-Ori '
                                                                                'chimed right against my '
                                                                                'heart through the fog! '
                                                                                'Hold tight -- the inner '
                                                                                'arch is lighting up!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_breakthrough_diff.jpg',
                                                                        'voice_emotion': 'outing_bump_rescue'}]},
                                                   {'opt_id': 'C15_B_LOCKED_MIST',
                                                    'label': 'Press both bare palms desperately against '
                                                             'the freezing silver mist wall as the 22:55 '
                                                             'inner seal tolls!',
                                                    'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                    'next_node': 'N33_BAD2_1',
                                                    'reaction_beats': [{'beat_id': 'N32_C15_FAIL_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Without the exact pairing '
                                                                                "of Kirara's living thread "
                                                                                'and a calibrated '
                                                                                'seam-cipher, the silver '
                                                                                'wall rebounds cold as '
                                                                                'iron against my palms as '
                                                                                '10:55 PM tolls across the '
                                                                                'ravine!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_mistwall_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N32_C15_FAIL_R2',
                                                                        'speaker': 'Kirara',
                                                                        'text': '...Thank you for running '
                                                                                'all the way from Amakane '
                                                                                'for me, Aether... A '
                                                                                'Gold-Level Courier never '
                                                                                'fails her final waybill '
                                                                                '-- even if she has to pay '
                                                                                'the road toll herself...',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_mistwall_base.jpg',
                                                                        'voice_emotion': ''}]}]},
                            'routing': [],
                            'ending_id': None},
           'N33_BAD2_1': {'node_id': 'N33_BAD2_1',
                          'chapter_id': 'CH4',
                          'title': 'The Toll Paid in Full',
                          'day_label': 'Day 9 - 11:15 PM to Dawn',
                          'location': 'Shattered Mist & Dormant Bead',
                          'bgm_bucket': 'vn_mystic_tension',
                          'beats': [{'beat_id': 'N33_B01',
                                     'speaker': 'Narrator',
                                     'text': "Beyond the opaque silver wall at eleven o'clock, emerald "
                                             'Dendro light flares once like a falling star -- Kirara '
                                             'pouring every strand of her Hitoyo no Ito into the corridor '
                                             'alone.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_mistwall_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B02',
                                     'speaker': 'Narrator',
                                     'text': 'Through the thinning vapor, a small silhouette bows deeply '
                                             'toward my side of the stone arch one last time, whispering '
                                             'words that dissolve into the wind before they reach me.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_gate1_mistwall_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B03',
                                     'speaker': 'Narrator',
                                     'text': 'Only when grey dawn breaks through the cedars does the mist '
                                             'collapse. On the mossy steps of an abandoned Chinju wayside '
                                             'shrine sits the centenary lacquer box -- unharmed and '
                                             'unbound.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B04',
                                     'speaker': 'Narrator',
                                     'text': 'Beside it, curled inside a weathered wooden crate next to a '
                                             'colorless, dimmed Vision shell, lies a tiny tawny-brown '
                                             'stray cat with a single thin tail and wide, uncomprehending '
                                             'emerald eyes.',
                                     'inner_thought': 'She paid the hundred-year road toll with every '
                                                      'human word, memory, and second tail she ever '
                                                      'grew...',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B05',
                                     'speaker': 'Small Stray Cat',
                                     'text': '...Mew...?',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [{'default': True, 'next_node': 'N34_BAD2_2'}],
                          'ending_id': None},
           'N34_BAD2_2': {'node_id': 'N34_BAD2_2',
                          'chapter_id': 'CH4',
                          'title': 'Warm Broth for a Nameless Porch',
                          'day_label': 'Day 10 - 06:30 AM',
                          'location': 'Abandoned Chinju Shrine Porch',
                          'bgm_bucket': 'vn_melancholy_memory',
                          'beats': [{'beat_id': 'N34_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Footsteps crunch across wet maple leaves as Yoimiya and '
                                             'Paimon hurry down the dawn trail, clutching the bamboo '
                                             'thermal jar of warm nekomanma they had cooked to celebrate '
                                             "Kirara's return.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N34_B02',
                                     'speaker': 'Paimon',
                                     'text': "Aether, the mist finally cleared! Where's Kirara -- wait... "
                                             'why is her Vision lying dark beside that old wooden box...?!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N34_B03',
                                     'speaker': 'Yoimiya',
                                     'text': "...No... Kirara...? Hey, little one, it's me, Yoimiya...! "
                                             "Why isn't she answering us, Aether...?",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N34_B04_F07',
                                     'speaker': 'Narrator',
                                     'text': 'Kneeling silently on the cold stone, I lay Suzu-Ori beside '
                                             'the wooden crate. The small one-tailed cat sniffs the silent '
                                             'brass bell curiously -- recognizing neither the ribbon nor '
                                             'her own name.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                     'voice_emotion': '',
                                     'when': {'all_flags': ['F07_SILK_BELL_RIBBON']}},
                                    {'beat_id': 'N34_B04_NOF07',
                                     'speaker': 'Narrator',
                                     'text': 'Kneeling silently on the cold stone, I hold out my '
                                             'charcoal-stained palm. The small one-tailed cat sniffs my '
                                             "fingertips cautiously -- recognizing neither Paimon's tears "
                                             "nor the name 'Kirara.'",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                     'voice_emotion': '',
                                     'when': {'forbid_flags': ['F07_SILK_BELL_RIBBON']}}],
                          'choice': {'choice_id': 'C20_BAD2',
                                     'prompt': 'In the pale Chinju dawn, the nameless one-tailed cat '
                                               'shivers inside the weathered wooden box:',
                                     'options': [{'opt_id': 'C20_A_SET_BOWL',
                                                  'label': "Ladle warm nekomanma from Yoimiya's bamboo jar "
                                                           'onto a saucer, cool it gently, and set it '
                                                           'before the porch box.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD2_PORCH_BOWL']},
                                                  'next_node': 'END_BAD_2',
                                                  'reaction_beats': [{'beat_id': 'N34_C20A_R1_F02',
                                                                      'speaker': 'Narrator',
                                                                      'text': "Remembering Grandma's rule "
                                                                              'from Kiminami, I blow three '
                                                                              'slow breaths across the '
                                                                              'steaming bonito broth so it '
                                                                              "cannot sting a cat's "
                                                                              'tongue, then set the saucer '
                                                                              'on the mossy step.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_nekomanma_diff.jpg',
                                                                      'voice_emotion': '',
                                                                      'when': {'all_flags': ['F02_NEKOMANMA_HEARTH']}},
                                                                     {'beat_id': 'N34_C20A_R1_NOF02',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'Pouring warm bonito-flake '
                                                                              'rice into a shallow saucer, '
                                                                              'I wait until the hottest '
                                                                              'steam softens in the dawn '
                                                                              'air before setting it '
                                                                              'gently beside the mossy '
                                                                              'crate.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_nekomanma_diff.jpg',
                                                                      'voice_emotion': '',
                                                                      'when': {'forbid_flags': ['F02_NEKOMANMA_HEARTH']}},
                                                                     {'beat_id': 'N34_C20A_R2',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'Stepping timidly from the '
                                                                              'box, the tiny cat laps the '
                                                                              'warm broth -- then pauses, '
                                                                              'inexplicably rubbing a wet '
                                                                              'emerald eye against my shin '
                                                                              'as if mourning someone she '
                                                                              'cannot recall.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_nekomanma_diff.jpg',
                                                                      'voice_emotion': ''}]},
                                                 {'opt_id': 'C20_B_STROKE_EAR',
                                                  'label': 'Sit quietly on the sunlit corner of the shrine '
                                                           'step so morning warmth falls across her small '
                                                           'crate without startling her.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD2_SUNLIT_STEP']},
                                                  'next_node': 'END_BAD_2',
                                                  'reaction_beats': [{'beat_id': 'N34_C20B_R1',
                                                                      'speaker': 'Aether',
                                                                      'text': 'You delivered the parcel '
                                                                              'all the way home, '
                                                                              'partner... Rest in the sun '
                                                                              'now; nobody will ever leave '
                                                                              'you cold on a mountain '
                                                                              'porch again.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N34_C20B_R2',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'After a long silence, the '
                                                                              'little one-tailed stray '
                                                                              'inches across the cedar '
                                                                              'board, tucking her paws '
                                                                              'against the edge of my '
                                                                              "traveler's cloak to fall "
                                                                              'asleep in the quiet dawn.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/kirara/ch4b_bad2_stray_cat_base.jpg',
                                                                      'voice_emotion': ''}]}]},
                          'routing': [],
                          'ending_id': None},
           'N35_C4': {'node_id': 'N35_C4',
                      'chapter_id': 'CH4',
                      'title': 'Small Hours at the Veranda Hearth',
                      'day_label': 'Day 9 - 02:15 AM',
                      'location': 'Serenitea Pot - Silken Courtyard Kitchenette',
                      'bgm_bucket': 'vn_melancholy_memory',
                      'beats': [{'beat_id': 'N35_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Inside the Realm Within, autumn nights stay mild as a '
                                         'late-afternoon breeze, yet the faint clink of porcelain wakes me '
                                         'deep in the small hours. Upstairs in the mansion loft, Paimon '
                                         'snores softly into her bolster pillow; when I slide open the '
                                         'outer screen, lantern light glows over a clay pot simmering on '
                                         'the veranda.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_broth_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N35_B02',
                                 'speaker': 'Kirara',
                                 'text': 'Mrow--?! Aether! You are supposed to be sound asleep off duty! '
                                         'Do not look at me like a cat caught raiding the fish cupboard -- '
                                         'a Gold-Level Courier always repays five-star hospitality with '
                                         'two warm bowls of nekomanma!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_startled_diff.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N35_B03',
                                 'speaker': 'Narrator',
                                 'text': 'With her dark-brown cat-ear ribbons untied for the night, her '
                                         'blonde hair falls loose over an indoor emerald haori as she '
                                         'nudges three brass Mora coins behind the tea caddy. Yet when she '
                                         'lifts the ladle, boiling dashi splashes straight across her bare '
                                         'right knuckles, and she sips from the bubbling rim without her '
                                         'eyelashes flinching once.',
                                 'inner_thought': 'She is not hiding a burn -- she genuinely felt nothing '
                                                  'at all.',
                                 'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_startled_diff.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C17_C',
                                 'prompt': "Scalding dashi clings to Kirara's unfeeling right knuckles "
                                           'beside the clay brazier.',
                                 'options': [{'opt_id': 'C17_C1',
                                              'label': 'Take the simmering ladle gently from her numb '
                                                       'fingers, guide her hand away from the steam, and '
                                                       'ask how long the chill lasted.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N36_C5_GATE2',
                                              'reaction_beats': [{'beat_id': 'N35_C17C1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Easing the wooden ladle from '
                                                                          'her unresisting grip, I dampen '
                                                                          'a clean linen cloth in cool '
                                                                          'well-water and lift her '
                                                                          'reddened right knuckles gently '
                                                                          'near my warm cheek.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_close_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N35_C17C1_B04_F02',
                                                                  'speaker': 'Aether',
                                                                  'text': 'At Kiminami on our very first '
                                                                          'night, you made me memorize '
                                                                          "Grandma's rule: 'Cool every "
                                                                          'bowl three breaths first, '
                                                                          "because a cat's tongue cannot "
                                                                          "bear boiling broth.' ...How "
                                                                          'many days has the Chinju mist '
                                                                          'been stealing the warmth from '
                                                                          'your hands, Kirara?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_close_base.jpg',
                                                                  'voice_emotion': '',
                                                                  'when': {'all_flags': ['F02_NEKOMANMA_HEARTH']}},
                                                                 {'beat_id': 'N35_C17C1_B04_NOF02',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Even on our first night at '
                                                                          'Kiminami, you blew twice on '
                                                                          'warm miso soup before taking a '
                                                                          'tiny sip -- yet scalding broth '
                                                                          'did not even make you blink '
                                                                          'just now. How many days have '
                                                                          'you been hiding how cold that '
                                                                          'Chinju cord is making your '
                                                                          'hands, Kirara?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_close_base.jpg',
                                                                  'voice_emotion': '',
                                                                  'when': {'forbid_flags': ['F02_NEKOMANMA_HEARTH']}},
                                                                 {'beat_id': 'N35_C17C1_B05',
                                                                  'speaker': 'Kirara',
                                                                  'text': '...My twin tails did not even '
                                                                          'give me away this time, and you '
                                                                          'still caught me. Aether... half '
                                                                          'an hour ago I tried to count '
                                                                          'three Mora coins on the tray, '
                                                                          'and for ten whole seconds they '
                                                                          'looked like plain round pebbles '
                                                                          'to me. If morning comes and I '
                                                                          'curl inside a box without '
                                                                          'remembering how to say your '
                                                                          'name... please do not hate me.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_tears_diff.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C17_C2',
                                              'label': 'Set the simmering ladle aside at once and cradle '
                                                       'her cold, reddened right hand against your warm '
                                                       'cheek before speaking softly.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N36_C5_GATE2',
                                              'reaction_beats': [{'beat_id': 'N35_C17C2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Setting the ladle aside at '
                                                                          'once, I cool the splash with '
                                                                          'damp linen and cradle her icy, '
                                                                          'reddened right knuckles '
                                                                          'tenderly against my warm cheek '
                                                                          'without a word of scolding.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_close_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N35_C17C2_B04_F02',
                                                                  'speaker': 'Aether',
                                                                  'text': 'At Kiminami on our very first '
                                                                          'night, you made me memorize '
                                                                          "Grandma's rule: 'Cool every "
                                                                          'bowl three breaths first, '
                                                                          "because a cat's tongue cannot "
                                                                          "bear boiling broth.' ...How "
                                                                          'many days has the Chinju mist '
                                                                          'been stealing the warmth from '
                                                                          'your hands, Kirara?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_close_base.jpg',
                                                                  'voice_emotion': '',
                                                                  'when': {'all_flags': ['F02_NEKOMANMA_HEARTH']}},
                                                                 {'beat_id': 'N35_C17C2_B04_NOF02',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Even on our first night at '
                                                                          'Kiminami, you blew twice on '
                                                                          'warm miso soup before taking a '
                                                                          'tiny sip -- yet scalding broth '
                                                                          'did not even make you blink '
                                                                          'just now. How many days have '
                                                                          'you been hiding how cold that '
                                                                          'Chinju cord is making your '
                                                                          'hands, Kirara?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_close_base.jpg',
                                                                  'voice_emotion': '',
                                                                  'when': {'forbid_flags': ['F02_NEKOMANMA_HEARTH']}},
                                                                 {'beat_id': 'N35_C17C2_B05',
                                                                  'speaker': 'Kirara',
                                                                  'text': '...My twin tails did not even '
                                                                          'give me away this time, and you '
                                                                          'still caught me. Aether... half '
                                                                          'an hour ago I tried to count '
                                                                          'three Mora coins on the tray, '
                                                                          'and for ten whole seconds they '
                                                                          'looked like plain round pebbles '
                                                                          'to me. If morning comes and I '
                                                                          'curl inside a box without '
                                                                          'remembering how to say your '
                                                                          'name... please do not hate me.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_veranda_tears_diff.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N36_C5_GATE2': {'node_id': 'N36_C5_GATE2',
                            'chapter_id': 'CH4',
                            'title': 'Decision Above the Silver Canopy',
                            'day_label': 'Day 9 - 08:30 PM',
                            'location': 'Byakko Bluff Outside the Teapot',
                            'bgm_bucket': 'vn_mystic_tension',
                            'beats': [{'beat_id': 'N36_B01',
                                       'speaker': 'Narrator',
                                       'text': 'At half past eight on Night Nine, we step back out of the '
                                               'Serenitea Pot onto the crimson maple cliff of Byakko '
                                               'Bluff. Below us, silver mist already coils through '
                                               "Chinju's dark cedars.",
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_gate2_byakko_bluff_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N36_B02',
                                       'speaker': 'Yae Miko',
                                       'text': 'Right on cue, little ones. My shrine maidens stand ready '
                                               'at the outer torii: if we cast the Five-Torii Sacred '
                                               'Sakura Ward by 09:15 PM, it will freeze the hollow and '
                                               "suspend the box's ten-pace pull for ninety days until "
                                               'First-Sakura Night.',
                                       'inner_thought': "Miko's ward safely buys ninety winter days -- or, "
                                                        'if our clues and warmth anchors are complete, we '
                                                        'descend into Ne-no-Torii tonight!',
                                       'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_gate2_byakko_bluff_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N36_B03',
                                       'speaker': 'Kirara',
                                       'text': 'Grandma Koharu has already waited so many autumns... yet '
                                               "after losing the feeling in my hand last night, I'll trust "
                                               'whichever call you make on this bluff, Aether!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_gate2_byakko_bluff_base.jpg',
                                       'voice_emotion': ''}],
                            'choice': {'choice_id': 'C18_C_GATE2',
                                       'prompt': 'COMBINATION GATE #2 -- 08:30 PM on Byakko Bluff! Descend '
                                                 "into Ne-no-Torii tonight, or invoke Miko's 90-day ward?",
                                       'options': [{'opt_id': 'C18_C_COMBO_UNLOCK',
                                                    'label': 'Weave Suzu-Ori, your mist-cord clues, and '
                                                             'your human-warmth anchors together -- '
                                                             'descend into Ne-no-Torii tonight!',
                                                    'when': {'all_flags': ['F07_SILK_BELL_RIBBON'],
                                                             'any_flags': ['F03_HITOYO_CORD_WEAVE',
                                                                           'F05_WAX_SEAL_CIPHER',
                                                                           'F08_PAW_MIST_PULSE',
                                                                           'F11_CAT_TONGUE_CHILL'],
                                                             'min_count_in': {'count': 2,
                                                                              'pool': ['F01_FIVE_STAR_STAMP',
                                                                                       'F02_NEKOMANMA_HEARTH',
                                                                                       'F04_ROOFTOP_TAIL_CODE',
                                                                                       'F06_GRANDMA_BOX_CUSHION']},
                                                             'min_insight': 8},
                                                    'unlock_badge': '[COMBINATION GATE #2 CLEARED] '
                                                                    'Hearth-Thread Descent',
                                                    'lock_hint': '[LOCKED: Needs Suzu-Ori + >=1 Mist/Cord '
                                                                 'Clue + >=2 Human-Warmth Anchors + '
                                                                 'Insight 8+]',
                                                    'effects': {'bond': 2,
                                                                'insight': 1,
                                                                'add_flags': ['COMBO2_CLEARED']},
                                                    'next_node': 'N38_CH5_CONVERGE',
                                                    'reaction_beats': [{'beat_id': 'N36_C18_PASS_R1',
                                                                        'speaker': 'Aether',
                                                                        'text': 'Stand down the '
                                                                                'quarantine, Miko -- I '
                                                                                'hold Suzu-Ori over my '
                                                                                'heart, we know the '
                                                                                "mist-cord's cadence, and "
                                                                                'we have every human '
                                                                                "memory anchoring Kirara's "
                                                                                'name. Tonight we finish '
                                                                                'Waybill #00-Hyakki '
                                                                                'together!',
                                                                        'inner_thought': 'Combination Gate '
                                                                                         '#2 Cleared '
                                                                                         '[Hearth-Thread '
                                                                                         'Descent]: Rested '
                                                                                         'and anchored, we '
                                                                                         'cross '
                                                                                         'Ne-no-Torii '
                                                                                         'before 22:50!',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_gate2_byakko_bluff_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N36_C18_PASS_R2',
                                                                        'speaker': 'Kirara',
                                                                        'text': "Yes! With a full day's "
                                                                                'rest in your sanctuary '
                                                                                'and your hand holding '
                                                                                "mine, let's bring Grandma "
                                                                                "Koharu's parcel home "
                                                                                'tonight, partner!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_gate2_byakko_bluff_base.jpg',
                                                                        'voice_emotion': 'vn_sweet_happy'}]},
                                                   {'opt_id': 'C18_C_FIRST_SAKURA_WARD',
                                                    'label': "Protect Kirara's fading warmth first -- ask "
                                                             'Yae Miko to seal Chinju Hollow for ninety '
                                                             'days until First-Sakura Night.',
                                                    'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                    'next_node': 'N37_GOOD_1',
                                                    'reaction_beats': [{'beat_id': 'N36_C18_GOOD_R1',
                                                                        'speaker': 'Aether',
                                                                        'text': 'No delivery is worth '
                                                                                "gambling Kirara's "
                                                                                'memories when her fingers '
                                                                                'went numb last night. '
                                                                                'Seal the hollow until '
                                                                                'First-Sakura Night, Miko '
                                                                                "-- we'll prepare every "
                                                                                'cipher together before '
                                                                                'spring.',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_gate2_byakko_bluff_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N36_C18_GOOD_R2',
                                                                        'speaker': 'Yae Miko',
                                                                        'text': 'A wise, tender call, '
                                                                                'little outlander. My '
                                                                                'Five-Torii Ward will hold '
                                                                                'the lacquer box and its '
                                                                                'ten-pace pull fast in '
                                                                                'slumber until the first '
                                                                                'spring blossoms wake.',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_gate2_byakko_bluff_base.jpg',
                                                                        'voice_emotion': ''}]}]},
                            'routing': [],
                            'ending_id': None},
           'N37_GOOD_1': {'node_id': 'N37_GOOD_1',
                          'chapter_id': 'CH4',
                          'title': 'Borrowed Sunshine Above Hanamizaka',
                          'day_label': 'Day 11 - 10:00 AM',
                          'location': 'Chioriya Hanamizaka Loft Balcony',
                          'bgm_bucket': 'vn_tender_romance',
                          'beats': [{'beat_id': 'N37_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Two mornings later, clear autumn sunlight warms the maple '
                                             "balcony of Chioriya Boutique's upper loft -- unlocked with "
                                             'the spare brass key Chiori left before preparing her '
                                             'Fontaine voyage.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_good_chioriya_loft_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N37_B02',
                                     'speaker': 'Narrator',
                                     'text': "Down in Chinju Forest, Yae Miko's Five-Torii Quarantine Seal "
                                             'holds the lacquer box and its ten-pace spatial tether frozen '
                                             "in stasis for ninety days. Though Kirara's right wrist "
                                             'remains too delicate for heavy mountain freight, her voice '
                                             'and smile shine whole.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_good_chioriya_loft_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N37_B03_F07',
                                     'speaker': 'Narrator',
                                     'text': 'Pinned safely onto the lapel of her warm winter shawl glints '
                                             'Suzu-Ori, returned from my pocket so its tiny bell chimes '
                                             'softly whenever she leans across the tea table.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_good_chioriya_loft_base.jpg',
                                     'voice_emotion': '',
                                     'when': {'all_flags': ['F07_SILK_BELL_RIBBON']}},
                                    {'beat_id': 'N37_B03_NOF07',
                                     'speaker': 'Narrator',
                                     'text': 'Pinned safely onto the lapel of her warm winter shawl glints '
                                             'Suzu-Ori, fetched from her cedar keepsake box at Komaniya '
                                             'headquarters so its tiny bell chimes in the morning breeze.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_good_chioriya_loft_base.jpg',
                                     'voice_emotion': '',
                                     'when': {'forbid_flags': ['F07_SILK_BELL_RIBBON']}},
                                    {'beat_id': 'N37_B04',
                                     'speaker': 'Kirara',
                                     'text': 'Fufu -- one, two, three breaths! Look, Aether, today the '
                                             'steaming nekomanma actually tingled on the tip of my tongue '
                                             "a little bit! By First-Sakura Night, we'll be super-ready!",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_good_chioriya_loft_base.jpg',
                                     'voice_emotion': 'vn_sweet_happy'},
                                    {'beat_id': 'N37_B05',
                                     'speaker': 'Aether',
                                     'text': 'And Madam Koharu smiled when we visited Amakane yesterday -- '
                                             'she said a love letter that waited a hundred years can '
                                             'happily wait one cosy winter more.',
                                     'inner_thought': 'Ninety sunlit mornings over warm nekomanma remain '
                                                      '-- and when spring sap rises, we will unseal Chinju '
                                                      'side by side.',
                                     'cg': 'ui_assets/story_quest_cgs/kirara/ch4c_good_chioriya_loft_base.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [],
                          'ending_id': 'END_GOOD'},
           'N38_CH5_CONVERGE': {'node_id': 'N38_CH5_CONVERGE',
                                'chapter_id': 'CH5',
                                'title': 'The Hyakki Lantern Threshold',
                                'day_label': 'Day 9 - 10:55 PM',
                                'location': 'Ne-no-Torii - Hyakki Lantern Threshold',
                                'bgm_bucket': 'vn_mystic_tension',
                                'beats': [{'beat_id': 'N38_B01_RA',
                                           'speaker': 'Narrator',
                                           'text': "At 10:55 PM inside Ne-no-Torii's stone vault, our "
                                                   'braced lantern vigil meets the final lock as rows of '
                                                   'spectral gold-and-indigo Hyakki lanterns bloom open '
                                                   'down the sunken corridor.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_A']}},
                                          {'beat_id': 'N38_B01_RB',
                                           'speaker': 'Narrator',
                                           'text': 'Stepping hand in hand through the cleaved silver mist '
                                                   'wall just before 10:55 PM seals behind us, we stand '
                                                   'together as spectral gold-and-indigo Hyakki lanterns '
                                                   'bloom down the corridor.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_B']}},
                                          {'beat_id': 'N38_B01_RC',
                                           'speaker': 'Narrator',
                                           'text': 'Having descended from Byakko Bluff at 10:40 PM with '
                                                   'Kirara rested and anchored, we stand inside '
                                                   'Ne-no-Torii at 10:55 PM as gold-and-indigo Hyakki '
                                                   'lanterns bloom down the corridor.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_C']}},
                                          {'beat_id': 'N38_B02',
                                           'speaker': 'Narrator',
                                           'text': 'No malice lingers in the ghostly lantern light -- only '
                                                   'the hushed reverence of a century-old night-parade '
                                                   'post road waiting for its final overdue courier.',
                                           'inner_thought': "Five minutes to eleven o'clock. Every clue "
                                                            'and promise we gathered leads down this '
                                                            'lantern aisle.',
                                           'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N38_B03',
                                           'speaker': 'Kirara',
                                           'text': 'Waybill #00-Hyakki, Komaniya Express taking over final '
                                                   'leg from senior courier Kohaku...! Stay right beside '
                                                   'my right hand, Aether!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                           'voice_emotion': ''}],
                                'choice': None,
                                'routing': [{'default': True, 'next_node': 'N39'}],
                                'ending_id': None},
           'N39': {'node_id': 'N39',
                   'chapter_id': 'CH5',
                   'title': "Senior Courier Kohaku's Bow",
                   'day_label': 'Day 9 - 11:00 PM',
                   'location': 'Phantom Courier Corridor',
                   'bgm_bucket': 'vn_mystic_tension',
                   'beats': [{'beat_id': 'N39_B01',
                              'speaker': 'Narrator',
                              'text': "As eleven o'clock tolls through the Sacred Sakura roots, a gentle "
                                      'translucent silhouette materializes before the inner stone dais -- '
                                      'a twin-tailed nekomata in a faded Edo courier cloak.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B02',
                              'speaker': 'Narrator',
                              'text': "Senior courier Kohaku's phantom eyes soften upon seeing Kirara's "
                                      'Komaniya badge, gesturing toward the indigo Musubi Pact-Cord '
                                      "wrapped around the outside of Kajiro's lacquer box.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B03',
                              'speaker': 'Aether',
                              'text': "Hear our witness, Ne-no-Torii! Master Kajiro and Lady Hina's living "
                                      "granddaughter -- Madam Koharu of Amakane Island's Twin-Maple Tea "
                                      'Stall -- awaits this parcel in the human world!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B04_TUNED',
                              'speaker': 'Narrator',
                              'text': 'Guided by our clockwise Descender counter-knot, my palm grounds the '
                                      "hundred-year road toll effortlessly into the Sacred Sakura's deep "
                                      "root-vein without a single spark burning Kirara's wrist.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['A_CORD_TUNED']}},
                             {'beat_id': 'N39_B05',
                              'speaker': 'Narrator',
                              'text': "Careful never to disturb Grandfather Kajiro's unbroken red customer "
                                      'wax seal on the lid, Kirara and I slide only the external indigo '
                                      'Musubi Pact-Cord off the lacquer box!',
                              'inner_thought': "A true courier never breaks a customer's wax seal -- only "
                                               'the external youkai pact-cord dissolves into the roots!',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B06',
                              'speaker': 'Narrator',
                              'text': "Freed of its century-old burden, Kohaku's phantom bows deeply in "
                                      'gratitude to her junior courier before dissolving into warm golden '
                                      'maple motes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N40_MIST_GRASP'}],
                   'ending_id': None},
           'N40_MIST_GRASP': {'node_id': 'N40_MIST_GRASP',
                              'chapter_id': 'CH5',
                              'title': 'Anchor of a Human Name',
                              'day_label': 'Day 9 - 11:08 PM',
                              'location': 'Collapsing Mist Corridor',
                              'bgm_bucket': 'vn_mystic_tension',
                              'beats': [{'beat_id': 'N40_B01',
                                         'speaker': 'Narrator',
                                         'text': 'As the Hyakki lantern corridor collapses back into '
                                                 'ordinary forest air at 11:08 PM, one last retreating '
                                                 'eddy of cold Mayoi-Giri vapor tugs at the loose end of '
                                                 "Kirara's Hitoyo no Ito!",
                                         'inner_thought': '',
                                         'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                         'voice_emotion': ''},
                                        {'beat_id': 'N40_B02',
                                         'speaker': 'Kirara',
                                         'text': '...Ah--! Aether, the dispersing fog is pulling at my '
                                                 'ears... everything feels dizzy for a second...',
                                         'inner_thought': '',
                                         'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                         'voice_emotion': ''}],
                              'choice': {'choice_id': 'C21_CH5',
                                         'prompt': 'As the last eddy of Chinju mist dissolves at 11:08 PM, '
                                                   "anchor Kirara's human-world thread:",
                                         'options': [{'opt_id': 'C21_A_CALL_KIRARA',
                                                      'label': 'Pull her close into your arms, call her '
                                                               "human name 'Kirara' clearly, and remind "
                                                               "her of Grandma's warm porch box.",
                                                      'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                                      'next_node': 'N41_KOMANIYA_WAKE',
                                                      'reaction_beats': [{'beat_id': 'N40_C21A_R1',
                                                                          'speaker': 'Aether',
                                                                          'text': 'Stay right with me, '
                                                                                  "Kirara! You're Kirara "
                                                                                  'of Komaniya Express -- '
                                                                                  'the girl Grandma named '
                                                                                  "under Konda's eaves, "
                                                                                  'and my irreplaceable '
                                                                                  'partner!',
                                                                          'inner_thought': '',
                                                                          'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                                                          'voice_emotion': ''},
                                                                         {'beat_id': 'N40_C21A_R2',
                                                                          'speaker': 'Kirara',
                                                                          'text': "...Kirara! That's my "
                                                                                  'name -- and your '
                                                                                  'heartbeat is loud and '
                                                                                  'warm right under my '
                                                                                  'ear! The cold fog is '
                                                                                  'completely gone!',
                                                                          'inner_thought': '',
                                                                          'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                                                          'voice_emotion': 'vn_tender_love'}]},
                                                     {'opt_id': 'C21_B_ROUTE_CHANT',
                                                      'label': 'Lace all ten fingers through hers and '
                                                               'recite her beloved Inazuma rooftops from '
                                                               'Ritou Pier to Hanamizaka.',
                                                      'effects': {'bond': 1, 'insight': 2, 'add_flags': []},
                                                      'next_node': 'N41_KOMANIYA_WAKE',
                                                      'reaction_beats': [{'beat_id': 'N40_C21B_R1',
                                                                          'speaker': 'Aether',
                                                                          'text': 'Count every stop back '
                                                                                  'home with me, Kirara: '
                                                                                  "Ritou's Maple Pier, "
                                                                                  "Kiminami's lantern "
                                                                                  "counter, Chioriya's "
                                                                                  "loft, and Amakane's "
                                                                                  'twin maples waiting '
                                                                                  'tomorrow!',
                                                                          'inner_thought': '',
                                                                          'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                                                          'voice_emotion': ''},
                                                                         {'beat_id': 'N40_C21B_R2',
                                                                          'speaker': 'Kirara',
                                                                          'text': 'Every single roof and '
                                                                                  'smile is crystal clear '
                                                                                  'in my head! Hehe, look '
                                                                                  '-- the mist cleared '
                                                                                  'right up to the stars '
                                                                                  'above Chinju!',
                                                                          'inner_thought': '',
                                                                          'cg': 'ui_assets/story_quest_cgs/kirara/ch5_hyakki_corridor_base.jpg',
                                                                          'voice_emotion': 'vn_sweet_happy'}]}]},
                              'routing': [],
                              'ending_id': None},
           'N41_KOMANIYA_WAKE': {'node_id': 'N41_KOMANIYA_WAKE',
                                 'chapter_id': 'CH5',
                                 'title': "Return of the Cat's Tongue",
                                 'day_label': 'Day 10 - 09:30 AM',
                                 'location': 'Komaniya Express - Sunlit Tea Room',
                                 'bgm_bucket': 'vn_daily_sweet',
                                 'beats': [{'beat_id': 'N41_B01',
                                            'speaker': 'Narrator',
                                            'text': 'Bright morning sunshine floods the tatami tea room of '
                                                    'Komaniya Express on Day Ten. After ten hours of '
                                                    'dreamless sleep, Kirara sits cross-legged beside '
                                                    'Paimon and me as roasted green tea steams.',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/kirara/ch5_komaniya_hot_tea_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N41_B02',
                                            'speaker': 'Narrator',
                                            'text': 'Still half-sleepy, Kirara lifts her porcelain cup '
                                                    'without blowing on it first and takes a confident '
                                                    'morning sip.',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/kirara/ch5_komaniya_hot_tea_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N41_B03',
                                            'speaker': 'Kirara',
                                            'text': 'MROWWW--?! Ack, hot, hot, hot, hooooot!! My tongue, '
                                                    'it stung the tip of my tongue!!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/kirara/ch5_komaniya_hot_tea_base.jpg',
                                            'voice_emotion': 'vn_playful_tease'},
                                           {'beat_id': 'N41_B04',
                                            'speaker': 'Paimon',
                                            'text': "Bwahaha! Both of Kirara's tails puffed up twice as "
                                                    'big as dango skewers -- wait, why is she grinning ear '
                                                    'to ear while fanning her tongue?!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/kirara/ch5_komaniya_hot_tea_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N41_B05',
                                            'speaker': 'Kirara',
                                            'text': "Hehehe! Because it's HOT, Aether!! Ten fingers, ten "
                                                    'toes, and one hundred percent genuine cat-tongue '
                                                    'warmth -- every single bit of me came all the way '
                                                    'home!',
                                            'inner_thought': "Her cat's tongue flinched at steaming tea "
                                                             'right away -- the Chinju mist-chill is '
                                                             'completely cured!',
                                            'cg': 'ui_assets/story_quest_cgs/kirara/ch5_komaniya_hot_tea_base.jpg',
                                            'voice_emotion': 'vn_sweet_happy'}],
                                 'choice': None,
                                 'routing': [{'default': True, 'next_node': 'N42'}],
                                 'ending_id': None},
           'N42': {'node_id': 'N42',
                   'chapter_id': 'CH5',
                   'title': 'A Century Unsealed Under Twin Maples',
                   'day_label': 'Day 11 - 03:30 PM',
                   'location': 'Amakane Island - Twin-Maple Tea Stall',
                   'bgm_bucket': 'vn_tender_romance',
                   'beats': [{'beat_id': 'N42_B01',
                              'speaker': 'Narrator',
                              'text': "Crimson maple leaves drift across Amakane Island's sunlit tea stall "
                                      'the next afternoon. Invited by the Yashiro Heritage Office to '
                                      'witness the centenary handover, Kamisato Ayaka and Charlotte stand '
                                      'quietly beside Paimon and me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_amakane_delivered_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B02_RB',
                              'speaker': 'Charlotte',
                              'text': "Seeing our archive rubbing come alive in Madam Koharu's hands beats "
                                      'any front-page scoop, Aether -- Monsieur Verite stays lowered out '
                                      'of respect until she finishes reading!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_amakane_delivered_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['ROUTE_B']}},
                             {'beat_id': 'N42_B02_NORB',
                              'speaker': 'Charlotte',
                              'text': "When Lady Ayaka's Heritage Office told me Komaniya Express "
                                      'recovered a hundred-year Chinju parcel intact, I rushed straight '
                                      "from Ritou -- though I'm keeping my Kamera lowered for her family "
                                      'moment!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_amakane_delivered_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['ROUTE_B']}},
                             {'beat_id': 'N42_B03',
                              'speaker': 'Kirara',
                              'text': 'Madam Koharu of Twin-Maple Tea Stall! On behalf of senior courier '
                                      'Kohaku and Komaniya Express -- Waybill #00-Hyakki, seal unbroken, '
                                      'delivered safely to your hands!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_amakane_delivered_base.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N42_B04',
                              'speaker': 'Narrator',
                              'text': 'With trembling seventy-four-year-old fingers, Madam Koharu breaks '
                                      "her Grandfather Kajiro's century-old red wax seal for the very "
                                      'first time -- lifting out a pair of gleaming Maple-Bell Lacquer '
                                      'Combs and a folded autumn vow to Grandmother Hina.',
                              'inner_thought': "After a hundred autumns, Kajiro's unbroken seal finally "
                                               "opened in his granddaughter's living hands.",
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_amakane_delivered_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B05',
                              'speaker': 'Madam Koharu',
                              'text': 'Grandmother Hina told me of these maple-bell combs until her '
                                      'ninetieth autumn... Thank you, dear courier girl -- you carried my '
                                      "grandparents' youth across a hundred years without a single "
                                      'scratch.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_amakane_delivered_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B06',
                              'speaker': 'Kamisato Ayaka',
                              'text': 'Not a dry eye under the maples... Look how proudly Kirara is '
                                      'stamping her delivery ledger, Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_amakane_delivered_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N43_ROOFTOP_DUSK'}],
                   'ending_id': None},
           'N43_ROOFTOP_DUSK': {'node_id': 'N43_ROOFTOP_DUSK',
                                'chapter_id': 'CH5',
                                'title': 'Dusk Above the Firefly Eaves',
                                'day_label': 'Day 12 - 05:45 PM',
                                'location': 'Hanamizaka High Tile Ridge',
                                'bgm_bucket': 'vn_tender_romance',
                                'beats': [{'beat_id': 'N43_B01',
                                           'speaker': 'Narrator',
                                           'text': 'Golden sunset paints the high clay tiles above '
                                                   'Hanamizaka on Day Twelve, turning the waking '
                                                   'streetlamps below into a river of warm amber fireflies '
                                                   'while Paimon bargains for dango down in the lane.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N43_B02',
                                           'speaker': 'Narrator',
                                           'text': 'Swinging her boots beside mine on our favorite '
                                                   'ridge-beam, Kirara tilts her head toward me in the '
                                                   'sunset breeze -- the small spot beneath her left '
                                                   'dark-brown cat-ear bow still waiting.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N43_B03',
                                           'speaker': 'Kirara',
                                           'text': 'Waybill #00-Hyakki is officially filed with five shiny '
                                                   'stars, Chiori finished packing her Fontaine trunks for '
                                                   "tomorrow's ship, and Inazuma's roofs are peaceful "
                                                   'again...',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                                           'voice_emotion': 'outing_cruise'},
                                          {'beat_id': 'N43_B04',
                                           'speaker': 'Kirara',
                                           'text': 'So tell me honestly before sunset fades, Aether... now '
                                                   'that this autumn manifest is complete, where does our '
                                                   'next delivery address lead?',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                                           'voice_emotion': 'vn_shy_blush'}],
                                'choice': {'choice_id': 'C22_FINAL',
                                           'prompt': "At sunset on Hanamizaka's high roof ridge, Kirara "
                                                     'waits for your answer on your next destination:',
                                           'options': [{'opt_id': 'C22_TRUE_PARTNER',
                                                        'label': 'Draw Suzu-Ori from over your heart, clip '
                                                                 'it beneath her left bow yourself, and '
                                                                 'claim her as your lifelong partner.',
                                                        'when': {'all_flags': ['F07_SILK_BELL_RIBBON'],
                                                                 'forbid_flags': ['ROUTE_A_DETACHED'],
                                                                 'any_of': [{'min_bond': 16},
                                                                            {'min_bond': 14,
                                                                             'min_insight': 14}]},
                                                        'unlock_badge': '[TRUE ENDING UNLOCKED] Lifelong '
                                                                        'Doorstep Partner',
                                                        'lock_hint': '[LOCKED: Needs Suzu-Ori + Unbroken '
                                                                     'Emotional Trust + (Bond 16+ OR Bond '
                                                                     '14+ & Insight 14+)]',
                                                        'effects': {'bond': 0,
                                                                    'insight': 0,
                                                                    'add_flags': ['TRUE_PARTNER_SEALED']},
                                                        'next_node': 'N44',
                                                        'reaction_beats': [{'beat_id': 'N43_C22_TRUE_R1',
                                                                            'speaker': 'Aether',
                                                                            'text': 'Before we pick any '
                                                                                    'map coordinate, '
                                                                                    'Kirara -- hold still '
                                                                                    'for one heartbeat. I '
                                                                                    'made you a promise on '
                                                                                    "Chiori's balcony to "
                                                                                    'return your favorite '
                                                                                    'piece of being '
                                                                                    "'Kirara' with my own "
                                                                                    'hands.',
                                                                            'inner_thought': '',
                                                                            'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                                                                            'voice_emotion': ''}]},
                                                       {'opt_id': 'C22_FIVE_STAR_REGULAR',
                                                        'label': 'Promise that wherever your travels '
                                                                 'across Teyvat roam, you will always '
                                                                 'return as her most loyal five-star '
                                                                 'regular.',
                                                        'effects': {'bond': 0,
                                                                    'insight': 0,
                                                                    'add_flags': []},
                                                        'next_node': 'N46',
                                                        'reaction_beats': [{'beat_id': 'N43_C22_NEUT_R1',
                                                                            'speaker': 'Aether',
                                                                            'text': 'Wherever the wind '
                                                                                    'leads across Teyvat, '
                                                                                    'Kirara, save the top '
                                                                                    'line of your Komaniya '
                                                                                    'manifest for me -- '
                                                                                    'your number-one '
                                                                                    'five-star regular.',
                                                                            'inner_thought': '',
                                                                            'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                                                                            'voice_emotion': ''}]}]},
                                'routing': [],
                                'ending_id': None},
           'N44': {'node_id': 'N44',
                   'chapter_id': 'CH5',
                   'title': 'Suzu-Ori Beneath Her Left Bow',
                   'day_label': 'Day 12 - 06:05 PM',
                   'location': 'Hanamizaka Rooftop - Ribbon Returned',
                   'bgm_bucket': 'vn_tender_romance',
                   'beats': [{'beat_id': 'N44_B01',
                              'speaker': 'Narrator',
                              'text': 'Drawing the warm emerald-and-gold Suzu-Ori chime-tassel from my '
                                      'breast pocket, I brush back a lock of blonde hair and clip it '
                                      'gently beneath her left dark-brown cat-ear bow.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_ribbon_tie_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N44_B02',
                              'speaker': 'Narrator',
                              'text': 'At the touch of my fingertips against her temple, the tiny brass '
                                      'bell rings out clear and joyous against her racing pulse -- '
                                      'brighter than the day she first wove it.',
                              'inner_thought': 'Suzu-Ori is home beneath her left bow -- chiming in tune '
                                               'with both our heartbeats.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_ribbon_tie_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N44_B03',
                              'speaker': 'Aether',
                              'text': 'And Chiori slipped me one more gift before sealing her luggage last '
                                      'night -- paired gold-and-emerald maple-cord bracelets braided to '
                                      'never fray in rain or mist. One for your right wrist, one for mine.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_ribbon_tie_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N44_B04',
                              'speaker': 'Kirara',
                              'text': 'Aether...! Suzu-Ori smells just like your warm cloak, and our '
                                      'wrists even match now...! Wait till dusk turns to starlight -- '
                                      "don't move an inch!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_ribbon_tie_diff.jpg',
                              'voice_emotion': 'vn_shy_blush'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N45'}],
                   'ending_id': None},
           'N45': {'node_id': 'N45',
                   'chapter_id': 'CH5',
                   'title': 'Delivered to Your Side',
                   'day_label': 'Day 12 - 07:00 PM',
                   'location': 'Starlit Inazuma Overlook',
                   'bgm_bucket': 'vn_tender_romance',
                   'beats': [{'beat_id': 'N45_B01',
                              'speaker': 'Narrator',
                              'text': 'Night deepens into a canopy of autumn stars above Inazuma City '
                                      'while thousands of golden lanterns shimmer like fireflies below. '
                                      'Leaning warmly against my shoulder, Kirara wraps both fluffy tails '
                                      'snugly around my waist and braceleted wrist.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_true_end_starlight_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N45_B02',
                              'speaker': 'Kirara',
                              'text': 'Mrow... my chest is so warm and full right now, Aether, I feel like '
                                      'I might sprout a third tail any second!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_true_end_starlight_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N45_B03',
                              'speaker': 'Aether',
                              'text': 'Two tails already claim both my wrists and my waist -- if you grow '
                                      "a third one, you'll never let me go anywhere without you.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_true_end_starlight_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N45_B04',
                              'speaker': 'Kirara',
                              'text': "That's the whole point, partner! No snowy mountain porch or forest "
                                      'mist can ever scare me again -- because wherever you stand across '
                                      'the stars is the one home this courier is delivered to forever!',
                              'inner_thought': 'Beneath the autumn stars, Suzu-Ori chimes softly between '
                                               'us -- a human name and two warm hands, bound for good.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_true_end_starlight_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_TRUE'},
           'N46': {'node_id': 'N46',
                   'chapter_id': 'CH5',
                   'title': 'Five-Star Regular at Sunset',
                   'day_label': 'Day 12 - 06:10 PM',
                   'location': 'Hanamizaka Rooftop - Sunset Bell',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'beats': [{'beat_id': 'N46_46A_B01',
                              'speaker': 'Narrator',
                              'text': 'Drawing Suzu-Ori carefully from my pocket, I place the '
                                      "emerald-and-gold silk tassel politely back into Kirara's open palm "
                                      'as sunset gilds the quiet space still lingering between us since '
                                      "Chinju's frost ring.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SILK_BELL_RIBBON', 'ROUTE_A_DETACHED']}},
                             {'beat_id': 'N46_46A_B02',
                              'speaker': 'Kirara',
                              'text': 'Thank you for keeping Suzu-Ori clean and guarding my life through '
                                      'the mist, Aether. Whenever you need a reliable courier across '
                                      'Teyvat, Komaniya Express will answer right on time.',
                              'inner_thought': 'Her voice is whole and polite, even if a gentle half-step '
                                               'of tactical caution remains unspoken between us.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SILK_BELL_RIBBON', 'ROUTE_A_DETACHED']}},
                             {'beat_id': 'N46_46B_B01',
                              'speaker': 'Narrator',
                              'text': 'Drawing Suzu-Ori from my pocket with a fond smile, I clip the silk '
                                      'chime-tassel neatly back beneath her left dark-brown bow as a '
                                      'trusted friend returning a badge of honor.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_ribbon_tie_diff.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SILK_BELL_RIBBON'],
                                       'forbid_flags': ['ROUTE_A_DETACHED']}},
                             {'beat_id': 'N46_46B_B02',
                              'speaker': 'Kirara',
                              'text': 'Hehe, Suzu-Ori is right back where it belongs! Next cherry-blossom '
                                      "season, promise you'll request me first on the manifest -- "
                                      'five-star paw stamps reserved just for my favorite regular!',
                              'inner_thought': 'Warm laughter rings across the sunset tiles between two '
                                               "cherished friends ready for tomorrow's road.",
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_ribbon_tie_diff.jpg',
                              'voice_emotion': 'vn_sweet_happy',
                              'when': {'all_flags': ['F07_SILK_BELL_RIBBON'],
                                       'forbid_flags': ['ROUTE_A_DETACHED']}},
                             {'beat_id': 'N46_46C_B01',
                              'speaker': 'Narrator',
                              'text': 'Reaching into her courier pouch with a cheerful grin, Kirara holds '
                                      'up Suzu-Ori -- fetched fresh from her cedar keepsake box at '
                                      'Komaniya headquarters that morning -- and gives the brass bell a '
                                      'bright flick.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_SILK_BELL_RIBBON', 'ROUTE_A_DETACHED']}},
                             {'beat_id': 'N46_46C_B02',
                              'speaker': 'Kirara',
                              'text': "Hear that ring, Aether? Tomorrow I'll clip Suzu-Ori back on for my "
                                      "morning shift -- and wherever you travel next, you've got lifetime "
                                      'priority shipping from your favorite courier friend!',
                              'inner_thought': 'Under the warm sunset sky, her twin tails sway happily '
                                               'beside her most trusted regular customer.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                              'voice_emotion': 'vn_sweet_happy',
                              'when': {'forbid_flags': ['F07_SILK_BELL_RIBBON', 'ROUTE_A_DETACHED']}},
                             {'beat_id': 'N46_46D_B01',
                              'speaker': 'Narrator',
                              'text': 'Rising gracefully onto the ridge tiles before sunset fades, Kirara '
                                      'touches the silk pouch holding Suzu-Ori -- retrieved quietly from '
                                      'her Komaniya cedar box that morning -- and offers a courteous '
                                      'professional bow.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['ROUTE_A_DETACHED'],
                                       'forbid_flags': ['F07_SILK_BELL_RIBBON']}},
                             {'beat_id': 'N46_46D_B02',
                              'speaker': 'Kirara',
                              'text': 'Thank you again for escorting Waybill #00-Hyakki safely through '
                                      'Chinju Forest, Honorable Traveler. Until your next commission with '
                                      'Komaniya Express -- safe journeys ahead.',
                              'inner_thought': "With a poised courier's salute, she bounds lightly across "
                                               'the sunset eaves onto her evening route alone.',
                              'cg': 'ui_assets/story_quest_cgs/kirara/ch5_rooftop_dusk_horizon_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['ROUTE_A_DETACHED'],
                                       'forbid_flags': ['F07_SILK_BELL_RIBBON']}}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_NEUTRAL'}}}

STORY_QUEST_CAMPAIGNS: list[dict[str, Any]] = [STORY_QUEST_CAMPAIGN]
