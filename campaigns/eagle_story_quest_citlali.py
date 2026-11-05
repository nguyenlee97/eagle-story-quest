"""
Citlali Story Quest #1 -- 5-Chapter Pure Branching Visual Novel Campaign Pack
Title: "Where the Night-Wind Keeps Your Hue" (`campaign_id = "citlali_sq1_color_of_eternity"`)
Target Runtime: C:\\Users\\LENOVO\\Desktop\\GTA\\Project Eagle\\gta sa gameplay-lab
Plug-and-Play Contract: exports both `STORY_QUEST_CAMPAIGN` and `STORY_QUEST_CAMPAIGNS`.
"""
from __future__ import annotations

STORY_QUEST_CAMPAIGN: dict = {'char_id': 'citlali',
 'ped_id': 49430,
 'display_name': 'Citlali',
 'campaign_id': 'citlali_sq1_color_of_eternity',
 'title': 'Where the Night-Wind Keeps Your Hue',
 'subtitle': 'Opalstar Chronicle: Act I -- The Color of Eternity',
 'version': '1.1.0',
 'theme_rgb': [192, 132, 252],
 'chapters': [{'chapter_id': 'CH1',
               'index': 1,
               'title': 'Chapter 1 -- The Key, the Novel & the Leaking Thought',
               'entry_node': 'N01'},
              {'chapter_id': 'CH2',
               'index': 2,
               'title': 'Chapter 2 -- Two Centuries of Wildflowers & Static',
               'entry_node': 'N09'},
              {'chapter_id': 'CH3',
               'index': 3,
               'title': 'Chapter 3 -- Three Paths Into the Loom',
               'entry_node': 'N18_A1'},
              {'chapter_id': 'CH4',
               'index': 4,
               'title': 'Chapter 4 -- Prism, Clamp & Counter-Weave',
               'entry_node': 'N20_A3'},
              {'chapter_id': 'CH5',
               'index': 5,
               'title': 'Chapter 5 -- The Color That Outlasts the Stars',
               'entry_node': 'N34_CH5_CONVERGE'}],
 'initial_state': {'bond': 0, 'insight': 0, 'flags': []},
 'flag_catalog': {'F01_SEAL_FROST_READ': {'title': 'Bleached Doorway Ward',
                                          'clue_hint': 'Read the colorless frost siphoning rose-lavender '
                                                       "pigment inward from Citlali's lintel."},
                  'F02_NOVEL_SECRET_KEPT': {'title': 'Guarded Bookshelf Latch',
                                            'clue_hint': "Protected Citlali's warded lower novel "
                                                         "compartment from Ororon's cabbage ambush without "
                                                         'peeking.'},
                  'F03_SIX_KITSUNE_VERSE': {'title': 'Six Kitsune & Starlight Slip',
                                            'clue_hint': 'Read the opening line of Six Kitsune and '
                                                         "Huitzilin's woven seven-knot Starlight Borrowing "
                                                         'slip.'},
                  'F04_HAND_PROMISE_GIVEN': {'title': 'Under-Table Palm Promise',
                                             'clue_hint': 'Offered your open palm at dusk and promised '
                                                          'only Citlali holds your memory-color in '
                                                          'Natlan.'},
                  'F05_APHID_LOOM_TRACE': {'title': 'Chalk-White Aphid Trace',
                                           'clue_hint': 'Isolated the Night-Kingdom chromatic unraveling '
                                                        "pitch from Ororon's bleached phlogiston aphids."},
                  'F06_GRAFFITI_TRUTH_HEARD': {'title': "Huitzilin's Corner Flower",
                                               'clue_hint': "Spared Huitzilin's faded seven-petal wall "
                                                            'mark and heard why Citlali never banned '
                                                            'challengers.'},
                  'F07_ROSE_HANDKERCHIEF': {'title': 'Rose-Lavender Handkerchief',
                                            'clue_hint': "Carries Citlali's rose-lavender handkerchief "
                                                         'knotted with warm Descender gold.'},
                  'F08_QUENEPA_CONFESSION': {'title': 'Shattered Quenepa Frost',
                                             'clue_hint': "Caught Citlali's frost-numbed wrist over "
                                                          'spilled clear water and traced her meridian '
                                                          'drain.'},
                  'F09_ETERNAL_HUE_VOW': {'title': 'Soul-Bridge Eternal Vow',
                                          'clue_hint': 'Refused to sever the Soul-Bridge during the White '
                                                       'Surge, binding Descender gold openly to her '
                                                       'thread.'},
                  'F10_OPAL_SPINDLE_THREAD': {'title': 'First-Era Opal Spindle',
                                              'clue_hint': "Possesses Huitzilin's unbleached Opal Spindle "
                                                           "(or Ororon's crystallized harmonic lattice)."},
                  'F11_CLAW_IKTOMI_FEATHER': {'title': "Claw's Iridescent Feather",
                                              'clue_hint': 'Collected the half-bleached seven-color down '
                                                           'feather shed by Elder Tlapo on Day One.'}},
 'endings': {'END_TRUE': {'rank': 'TRUE ENDING',
                          'title': 'Where the Night-Wind Keeps Your Hue',
                          'summary': 'Awakening the Ancient Name Ukumbuko beside Tumaini and binding their '
                                     'wrists in rose-lavender silk at Verona sunrise, Citlali overturns '
                                     'two centuries of solitude with an eternal vow.'},
             'END_GOOD': {'rank': 'GOOD ENDING',
                          'title': 'Sixty-Day Candlelight',
                          'summary': "Sealing the First-Era Scroll inside Xilonen and Mavuika's Sixty-Day "
                                     "Phlogiston Stasis Clamp saves Citlali safely -- trading Ukumbuko's "
                                     'awakening and long-range telepathy for warm rooftop feasts.'},
             'END_NEUTRAL': {'rank': 'NEUTRAL ENDING',
                             'title': 'The Uncracked Spine',
                             'summary': 'The Night-Wind chronicle is restored and Citlali inherits '
                                        'Ukumbuko with quiet grace, yet a polite pane of glass leaves her '
                                        'deepest wish uncracked like the pristine volumes on her shelf.'},
             'END_BAD_1': {'rank': 'BAD ENDING I',
                           'title': 'White Canvas on Verona Shore',
                           'summary': "Releasing Citlali's hand lets her mend the ancestral tear alone at "
                                      'the cost of every memory of Aether -- leaving her healthy under '
                                      'bright Verona sun while their mental link falls silent forever.'},
             'END_BAD_2': {'rank': 'BAD ENDING II',
                           'title': 'Prisoners of the Seventh Hue',
                           'summary': 'Caught inside the Seven-Hued quarantine sphere without the complete '
                                      'Prism Key, Aether and Citlali keep every shared memory and thought '
                                      'inside a timeless painted twilight study.'}},
 'nodes': {'N01': {'node_id': 'N01',
                   'chapter_id': 'CH1',
                   'title': 'Salt Mist & Challenger Paint',
                   'day_label': 'Day 1 - Morning',
                   'location': 'Verona Cliffside - Night-Wind Sanctuary Steps',
                   'beats': [{'beat_id': 'N01_B01',
                              'speaker': 'Narrator',
                              'text': 'Morning sea-spray drifts up the terraced basalt steps of Verona '
                                      'Point, carrying the crisp scent of crushed copal incense and wet '
                                      'cliffside agave.',
                              'inner_thought': 'Even miles from Smoke-Drift Canyon, Citlali managed to '
                                               'pick the single cliff where nobody visits by accident.',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B02',
                              'speaker': 'Narrator',
                              'text': 'Below the limestone parapet, turquoise rollers comb white foam '
                                      "across Verona's quiet cove while wind-chimes carved from night-jade "
                                      'clink softly in the eaves.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B03',
                              'speaker': 'Narrator',
                              'text': 'Across the outer plaster of her secluded sanctuary, fresh turquoise '
                                      'and vermilion graffiti shouts a dozen boastful challenges at Granny '
                                      "Itztli -- the stubborn rite of Huitzilin's shamanic heirs.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B04',
                              'speaker': 'Aether',
                              'text': "'Face my spirit-motes at dawn, Great Shaman!' ...Funny how every "
                                      'single challenger still leaves a clean margin around her front '
                                      "lantern so the soot won't stain her weave.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B05',
                              'speaker': 'Narrator',
                              'text': 'Resting against my palm is the small brass-and-obsidian key Citlali '
                                      'pressed into my hand alongside her rose-lavender handkerchief after '
                                      'we left the Seven-Hued Ruins.',
                              'inner_thought': "She told me to unlock the door myself so I wouldn't wake "
                                               'her by pounding on the wood.',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B06',
                              'speaker': 'Narrator',
                              'text': 'In two hundred years of living behind seven-layered wards, only one '
                                      "outlander has ever carried a spare key to Granny Itztli's front "
                                      'door.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B07',
                              'speaker': 'Aether',
                              'text': 'Paimon stayed down at the harbor bakery negotiating over honeyed '
                                      'grainfruit tarts, which leaves me one quiet check-in before noon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B08',
                              'speaker': 'Narrator',
                              'text': 'Yet as my boots reach the top flagstone, the warm coastal breeze '
                                      'drops ten degrees in a single stride.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B09',
                              'speaker': 'Narrator',
                              'text': 'Thin, colorless mist curls off the carved obsidian lintel -- faint '
                                      'against the bright morning sun, yet sharp enough to prickle across '
                                      'my fingertips.',
                              'inner_thought': "That chill doesn't feel like ordinary sea-wind.",
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N02'}]},
           'N02': {'node_id': 'N02',
                   'chapter_id': 'CH1',
                   'title': 'The Whisper Behind the Latch',
                   'day_label': 'Day 1 - Morning',
                   'location': 'Verona Cliffside - Obsidian Doorframe',
                   'beats': [{'beat_id': 'N02_B01',
                              'speaker': 'Narrator',
                              'text': 'Before my knuckles even graze the keyhole, a familiar, sleep-mussed '
                                      'voice blooms directly between my temples -- the shared memory-link '
                                      'that never faded after we tracked Ororon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B02',
                              'speaker': 'Citlali',
                              'text': '...',
                              'inner_thought': '...noisy sea-gulls... wait, no, those footsteps on the '
                                               'third flagstone carry warm golden phlogiston...!',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B03',
                              'speaker': 'Narrator',
                              'text': 'Inside the shuttered study, a muffled thump betrays a pillow '
                                      'hitting the cedar floor, followed by the frantic hiss of snack '
                                      'wrappers being swept out of sight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B04',
                              'speaker': 'Citlali',
                              'text': '...',
                              'inner_thought': 'Is he actually using the key?! Did I leave empty Quenepa '
                                               "jars by the rug?! Don't panic, Citlali, project mystic "
                                               'composure!',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B05',
                              'speaker': 'Narrator',
                              'text': 'Every half-awake complaint slips across our mental bridge '
                                      'completely unguarded whenever her pulse jumps.',
                              'inner_thought': 'Two hundred years of feared shamanic authority, undone by '
                                               'one unannounced breakfast visit.',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B06',
                              'speaker': 'Citlali',
                              'text': '...',
                              'inner_thought': 'Sit straight, drape the shawl over your knees, pretend '
                                               "you've been divining star-charts since five in the "
                                               'morning--!',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B07',
                              'speaker': 'Narrator',
                              'text': 'I bite back a grin, lifting the brass key toward the lock -- then '
                                      'hesitate as sunlight catches the carved obsidian doorframe.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B08',
                              'speaker': 'Narrator',
                              'text': 'Right beside the brass keyhole, pale white rime is crystallizing '
                                      'along a Night-Wind ward that ought to shimmer vivid rose-lavender.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B09',
                              'speaker': 'Narrator',
                              'text': 'Even as the morning sun warms the stone, a hairline thread of color '
                                      'seems to be draining backward through the cedar seam.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C01',
                              'prompt': 'Citlali is scrambling to look composed inside, while white rime '
                                        'clings to her doorway seal:',
                              'options': [{'opt_id': 'C01_A_INSPECT_WARD',
                                           'label': 'Brush two fingers across the colorless frost on her '
                                                    'obsidian ward to read its Ley-frequency before '
                                                    'unlocking.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F01_SEAL_FROST_READ']},
                                           'next_node': 'N03',
                                           'reaction_beats': [{'beat_id': 'N02_C01A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Under my Color-of-Memory sight, '
                                                                       "the frost isn't ordinary Cryo "
                                                                       "elemental residue. The ward's "
                                                                       'rose-lavender pigment has been '
                                                                       'sucked inward toward the back '
                                                                       'room, leaving bleached white ash.',
                                                               'inner_thought': 'Something inside her '
                                                                                'sanctuary was drawing '
                                                                                'heavily on Night-Wind '
                                                                                'memory-threads before '
                                                                                'dawn.',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N02_C01A_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Where my golden phlogiston brushes '
                                                                       'the bleached stone, the chalky '
                                                                       'rime briefly chimes like taut '
                                                                       'loom-silk under strain.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N02_C01A_R3',
                                                               'speaker': 'Aether',
                                                               'text': 'Better remember that pattern. Now '
                                                                       "-- let's not keep Natlan's most "
                                                                       'dignified recluse waiting.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C01_B_USE_KEY_WARMLY',
                                           'label': 'Give a polite two-tap warning so she can straighten '
                                                    'her shawl, then turn her key gently with warm '
                                                    'pastries in hand.',
                                           'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N03',
                                           'reaction_beats': [{'beat_id': 'N02_C01B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Two light taps on the cedar panel '
                                                                       'earn an immediate, wordless sigh '
                                                                       'of relief across our mental '
                                                                       'bridge, followed by the soft click '
                                                                       'of her brass key turning smoothly '
                                                                       'in the lock.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N02_C01B_R2',
                                                               'speaker': 'Citlali',
                                                               'text': '...',
                                                               'inner_thought': 'Oh, thank the Night-Wind '
                                                                                'he tapped first -- wait, '
                                                                                'is that warm honeyed '
                                                                                'grainfruit I smell?!',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N02_C01B_R3',
                                                               'speaker': 'Aether',
                                                               'text': 'Coming in, Granny Itztli. Better '
                                                                       'hide whatever cushion just hit the '
                                                                       'floor.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_02_key_frost_ward_diff.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': []},
           'N03': {'node_id': 'N03',
                   'chapter_id': 'CH1',
                   'title': 'Nest of the Great Shaman',
                   'day_label': 'Day 1 - Late Morning',
                   'location': 'Sanctuary Study - Divination Cushions',
                   'beats': [{'beat_id': 'N03_B01',
                              'speaker': 'Narrator',
                              'text': 'Sunlight spills across woven Night-Wind tapestries, low cedar '
                                      'tables, and an impressive corner drift of candied-nut wrappers '
                                      'hastily kicked beneath a velvet throw.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_03_sanctuary_wake_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B02',
                              'speaker': 'Narrator',
                              'text': 'Perched atop a stack of embroidered divination cushions, Citlali '
                                      'sits bolt upright with her chin tilted ten degrees higher than '
                                      'necessary.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_03_sanctuary_wake_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B03',
                              'speaker': 'Citlali',
                              'text': "You have remarkable nerve strolling into a Great Shaman's sanctum "
                                      'before midday, Traveler. Do outlanders consider clocks a decorative '
                                      'myth?',
                              'inner_thought': "Is my braid crooked?! Tell me my hair isn't sticking up "
                                               'like an Iktomisaur crest!',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_03_sanctuary_wake_base.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N03_B04',
                              'speaker': 'Aether',
                              'text': 'Your hair looks fine, Citlali -- not a single Iktomisaur crest in '
                                      'sight. And I used the exact key the homeowner handed me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_03_sanctuary_wake_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B05',
                              'speaker': 'Narrator',
                              'text': 'Citlali freezes mid-reach for her teacup, realization dawning a '
                                      'half-second too late that she never spoke a word about her hair '
                                      'aloud.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_04_sanctuary_blush_itzpapa_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B06',
                              'speaker': 'Citlali',
                              'text': 'Y-You eavesdropping little--! Snatching stray surface thoughts out '
                                      'of the air is peak bad manners! Keep your golden ears out of my '
                                      'head before I hex them shut!',
                              'inner_thought': 'Why does this stupid memory-bond get louder every time he '
                                               'stands within five paces of me?!',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_04_sanctuary_blush_itzpapa_diff.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N03_B07',
                              'speaker': 'Narrator',
                              'text': 'She snatches both plush Tzitzimimeh -- Citlalin and Itzpapa -- '
                                      'squeezing their round stuffed bellies up to her chin like twin '
                                      'battlements while the clingy little spirits wiggle contentedly.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_04_sanctuary_blush_itzpapa_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B08',
                              'speaker': 'Aether',
                              'text': "In my defense, you're the one projecting at town-crier volume. Were "
                                      'you up reading again, or did another challenger paint your wall at '
                                      'dawn?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_04_sanctuary_blush_itzpapa_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B09',
                              'speaker': 'Citlali',
                              'text': 'Meditating on seasonal Ley-tides, obviously! Unlike certain '
                                      "carefree vagabonds, Natlan's sole Great Shaman has astronomical "
                                      'charts to maintain!',
                              'inner_thought': "Don't look at my hands, don't look at my hands... tuck "
                                               "your thumbs under Itzpapa's ears before they shiver...",
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_04_sanctuary_blush_itzpapa_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B10',
                              'speaker': 'Narrator',
                              'text': "Even with her fingers hidden behind the plush skull-spirit's "
                                      'fringe, faint violet shadows linger beneath her rose-gold eyes -- '
                                      'deeper than an all-night novel binge.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_04_sanctuary_blush_itzpapa_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B11',
                              'speaker': 'Aether',
                              'text': 'Well, astronomical charts go better with warm honeyed flatbread. '
                                      'Even baleful stars of the North and South need breakfast.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_04_sanctuary_blush_itzpapa_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B12',
                              'speaker': 'Citlali',
                              'text': 'Hmph. Leave the basket beside Citlalin, then. Since you went to the '
                                      'trouble of climbing fifty basalt steps, it would demean a tribal '
                                      'elder to send food away cold.',
                              'inner_thought': 'Still warm from the harbor oven... Ugh, how is a '
                                               'two-hundred-year-old recluse supposed to stay aloof around '
                                               'him?',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_04_sanctuary_blush_itzpapa_diff.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N03_B13',
                              'speaker': 'Narrator',
                              'text': "As she breaks off a corner of honeyed crust behind Itzpapa's plush "
                                      'ear, the tense line of her shoulders softens into the sunny coastal '
                                      'hush.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_04_sanctuary_blush_itzpapa_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N04'}]},
           'N04': {'node_id': 'N04',
                   'chapter_id': 'CH1',
                   'title': 'Cabbages, Latches & Iktomi Down',
                   'day_label': 'Day 1 - Noon',
                   'location': 'Sanctuary Study & Sea-Terrace Rail',
                   'beats': [{'beat_id': 'N04_B01',
                              'speaker': 'Narrator',
                              'text': 'Before Citlali can take a second bite of flatbread, two brisk '
                                      'knocks rattle the open doorframe -- and Ororon steps straight '
                                      'inside lugging a burlap sack of cabbages nearly his own width.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B02',
                              'speaker': 'Ororon',
                              'text': 'Morning, Granny. Oh -- Gramps is already here! That saves me a trip '
                                      'down to the harbor. The roundest cabbages grew facing the west wind '
                                      'this week, so I figured you two needed fiber.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B03',
                              'speaker': 'Citlali',
                              'text': 'Stop calling him Gramps in my living room, you insolent sprout! Who '
                                      "taught you to barge through a shaman's warded doorway carrying half "
                                      'a farm?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N04_B04',
                              'speaker': 'Ororon',
                              'text': "You left the outer ward unlatched for Gramps, didn't you? Besides, "
                                      'this big green one looked lonely in the patch, and-- whoa, slippery '
                                      'rug--!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B05',
                              'speaker': 'Citlali',
                              'text': 'Watch your boots! There is an empty Quenepa Berry wine jar right '
                                      'beside the lower cedar--!',
                              'inner_thought': 'Not the lower shelf! All seven privacy runes on my secret '
                                               'novel compartment are going to pop open!',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B06',
                              'speaker': 'Narrator',
                              'text': "Too late: Ororon's heel clips the pale glass Quenepa bottle, "
                                      'sending his elbow thudding into the carved cedar bookshelf.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B07',
                              'speaker': 'Narrator',
                              'text': 'With a soft lavender spark, a concealed lower cabinet door clicks '
                                      'half an inch ajar right behind his calf.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B08',
                              'speaker': 'Narrator',
                              'text': 'At the exact same instant, heavy wings beat outside the open '
                                      "terrace arch. Elder Tlapo -- Claw, Huitzilin's towering "
                                      'two-hundred-year-old Iktomisaur -- alights on the stone rail.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B09',
                              'speaker': 'Narrator',
                              'text': "Ruffling his ancient plumage toward the sanctuary's back room, Claw "
                                      'shakes loose a strangely bleached, pale-iridescent wing feather '
                                      'onto the sunlit stone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C02',
                              'prompt': "Citlali's secret bookshelf latch is popping open behind Ororon "
                                        'while Elder Tlapo signals from the terrace:',
                              'options': [{'opt_id': 'C02_A_SHIELD_BOOKSHELF',
                                           'label': "Steady Ororon's cabbage sack with one shoulder and "
                                                    "click Citlali's secret bookshelf panel shut without "
                                                    'peeking inside.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F02_NOVEL_SECRET_KEPT']},
                                           'next_node': 'N05',
                                           'reaction_beats': [{'beat_id': 'N04_C02A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Pivoting smoothly behind Ororon, I '
                                                                       'catch the rolling Quenepa bottle '
                                                                       'with my boot and press the warded '
                                                                       'cedar panel back until its hidden '
                                                                       'rune-latch locks tight.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02A_R2',
                                                               'speaker': 'Ororon',
                                                               'text': 'Huh? Thanks, Gramps -- thought I '
                                                                       'bumped a loose board there for a '
                                                                       'second.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02A_R3',
                                                               'speaker': 'Citlali',
                                                               'text': 'A-Ahem! Adequate reflexes, '
                                                                       'Traveler. As for you, Ororon -- '
                                                                       'drop the vegetables in the kitchen '
                                                                       'and go check your aphid hives '
                                                                       'before I turn you into compost!',
                                                               'inner_thought': "...he didn't peek inside. "
                                                                                'He actually clicked the '
                                                                                'seal shut for me without '
                                                                                'teasing. My ears are '
                                                                                'burning...',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C02_B_CHECK_CLAW_FEATHER',
                                           'label': 'Let Citlali handle Ororon while you step out to Elder '
                                                    'Tlapo and examine the pale-iridescent feather on the '
                                                    'rail.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F11_CLAW_IKTOMI_FEATHER']},
                                           'next_node': 'N05',
                                           'reaction_beats': [{'beat_id': 'N04_C02B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'While Citlali lectures Ororon over '
                                                                       'rolling cabbages inside, Elder '
                                                                       'Tlapo nudges the shed feather into '
                                                                       'my palm with his scarred beak on '
                                                                       'the sunlit terrace.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02B_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Half of the Iktomisaur down still '
                                                                       'shimmers with two-century-old '
                                                                       'seven-color memory dye -- while '
                                                                       'its quill tip is bleached the '
                                                                       'exact chalk-white of drained '
                                                                       'Ley-silk.',
                                                               'inner_thought': "Even Huitzilin's old "
                                                                                'companion senses an '
                                                                                'ancestral weave losing '
                                                                                'its color nearby.',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02B_R3',
                                                               'speaker': 'Aether',
                                                               'text': 'I hear you, old friend. Let me '
                                                                       'tuck this feather safely inside my '
                                                                       "coat before Granny asks what we're "
                                                                       'whispering about.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_05_ororon_cabbage_chaos.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': []},
           'N05': {'node_id': 'N05',
                   'chapter_id': 'CH1',
                   'title': 'Spotless Spines from Inazuma',
                   'day_label': 'Day 2 - Afternoon',
                   'location': 'Sanctuary Study - Warded Bookshelf',
                   'beats': [{'beat_id': 'N05_B01',
                              'speaker': 'Narrator',
                              'text': 'When I return the next afternoon with small cedar wedges to level '
                                      'her wobbly bookcase, salt-bright sunlight slants across rows of '
                                      'dog-eared Yae Publishing House paperbacks.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B02',
                              'speaker': 'Narrator',
                              'text': 'Reincarnated archons, melodramatic bake-danuki romances, dog-eared '
                                      'anthologies read five times over -- every lower shelf bears the '
                                      'cozy wear of two hundred solitary nights.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B03',
                              'speaker': 'Narrator',
                              'text': 'Only the topmost shelf gleams completely free of dust. Resting '
                                      'there on embroidered silk coasters are the first-edition copies of '
                                      "'Pretty Please, Kitsune Guuji?' and 'A Legend of Sword' I brought "
                                      'her from Inazuma -- their spines still uncracked.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B04',
                              'speaker': 'Aether',
                              'text': "Still haven't opened the top shelf, Citlali? I starting to think "
                                      'you display them like sacred relics.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B05',
                              'speaker': 'Citlali',
                              'text': "Don't get smug staring up there! First editions lose collector "
                                      'value if you bend the binding carelessly -- I am merely waiting for '
                                      'an occasion worthy of opening them!',
                              'inner_thought': 'As if I could risk creasing the only books in two '
                                               'centuries someone carried across oceans just for me...',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N05_B06',
                              'speaker': 'Narrator',
                              'text': 'Setting my wooden mallet down, I tap the last cedar wedge beneath '
                                      'the corner post until the tall frame sits rock-steady.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B07_F02',
                              'speaker': 'Narrator',
                              'text': 'Glancing down at the lower cabinet I shielded from Ororon '
                                      'yesterday, Citlali hesitates -- then taps two fingers to disengage '
                                      'her seven privacy runes and lifts out a slim indigo-bound volume '
                                      'herself.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F02_NOVEL_SECRET_KEPT']}},
                             {'beat_id': 'N05_B08_F02',
                              'speaker': 'Citlali',
                              'text': '...Since you were polite enough not to snoop yesterday, I suppose '
                                      "letting you see the cover won't kill me.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F02_NOVEL_SECRET_KEPT']}},
                             {'beat_id': 'N05_B07_NOF02',
                              'speaker': 'Narrator',
                              'text': 'Down beside the lower cabinet Ororon bumped yesterday, the loosened '
                                      'rune-latch still rests half-open -- revealing a slim indigo-bound '
                                      'volume that slid onto the velvet cushion during the commotion.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F02_NOVEL_SECRET_KEPT']}},
                             {'beat_id': 'N05_B08_NOF02',
                              'speaker': 'Citlali',
                              'text': 'Ack -- stupid Ororon loosened the seventh latch after all! Hand '
                                      'that here carefully before the dust touches the endpapers!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F02_NOVEL_SECRET_KEPT']}},
                             {'beat_id': 'N05_B09',
                              'speaker': 'Aether',
                              'text': "'New Chronicles of the Six Kitsune'... Even in Inazuma City, hardly "
                                      'anyone finds an intact copy of this volume.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B10',
                              'speaker': 'Narrator',
                              'text': 'Between its cream pages glints a narrow strip of hand-loomed cloth '
                                      'far older than Yae Publishing House paper.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B11',
                              'speaker': 'Narrator',
                              'text': 'Woven in seven mineral hues that catch the coastal light like prism '
                                      'glass, the antique bookmark marks the very first page.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_06_bookshelf_novels_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N06'}]},
           'N06': {'node_id': 'N06',
                   'chapter_id': 'CH1',
                   'title': "Huitzilin's Woven Bookmark",
                   'day_label': 'Day 2 - Late Afternoon',
                   'location': 'Sanctuary Study - Window Alcove',
                   'beats': [{'beat_id': 'N06_B01',
                              'speaker': 'Narrator',
                              'text': 'Citlali snatches the slim volume against her collarbone, though not '
                                      'before that stiff, two-hundred-year-old woven bookmark slip peeks '
                                      'clearly above its opening page.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B02',
                              'speaker': 'Narrator',
                              'text': "Right beside the antique seven-color silk strip sits the novel's "
                                      "printed first sentence: 'Stories relating to memory always seem to "
                                      'have to do with those moments where you gain something and lose it '
                                      "straight away.'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B03',
                              'speaker': 'Aether',
                              'text': "'Gain something and lose it straight away'... No wonder you tucked "
                                      'a Night-Wind weave right against that line.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B04',
                              'speaker': 'Citlali',
                              'text': "It's just an obscure kitsune fable with decent prose! And the "
                                      'bookmark is a scrap of old practice cloth I happened to have lying '
                                      'around -- stop analyzing my reading habits!',
                              'inner_thought': 'Huitzilin wove that dye-cipher twenty years before she '
                                               'withered... Why did this stupid Inazuman sentence sound '
                                               'just like us?',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B05',
                              'speaker': 'Narrator',
                              'text': 'Her thumb strokes the faded indigo cover with an involuntary '
                                      'tenderness that belies every sharp word.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B06',
                              'speaker': 'Citlali',
                              'text': 'Mortals in Inazuma write as if sixty summers were an eternity, yet '
                                      'somehow a kitsune sitting under a shrine tree understood the exact '
                                      'ache of outliving every voice you know.',
                              'inner_thought': 'Except yours, Traveler... Yours is the first golden thread '
                                               "that won't blow away with one dry season.",
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B07',
                              'speaker': 'Narrator',
                              'text': 'Across the woven bookmark strip, seven tiny knotted threads form an '
                                      'inverted Night-Wind loom notation -- a counter-current pattern '
                                      'distinct from standard tribal scrolls.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B08',
                              'speaker': 'Narrator',
                              'text': "Meanwhile, Citlali's cheeks flush deeper rose as she realizes I am "
                                      'standing close enough to read both page and ribbon over her sleeve.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C03',
                              'prompt': "Citlali hugs 'New Chronicles of the Six Kitsune' tight, ears "
                                        'scarlet to their tips:',
                              'options': [{'opt_id': 'C03_A_READ_KITSUNE_CIPHER',
                                           'label': 'Ask gently about the inverted seven-knot loom pattern '
                                                    "woven into Huitzilin's antique bookmark slip.",
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F03_SIX_KITSUNE_VERSE']},
                                           'next_node': 'N07',
                                           'reaction_beats': [{'beat_id': 'N06_C03A_R1',
                                                               'speaker': 'Citlali',
                                                               'text': '...Sharp eyes, as usual. Huitzilin '
                                                                       "called that knot 'Starlight "
                                                                       "Borrowing' -- reversing a "
                                                                       "memory-scroll's draw so night sky "
                                                                       'phlogiston carries the tension '
                                                                       "instead of the weaver's pulse.",
                                                               'inner_thought': 'Dangerous to attempt '
                                                                                'solo, though... it takes '
                                                                                'two synchronized minds '
                                                                                'just to hold the warp '
                                                                                'steady.',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03A_R2',
                                                               'speaker': 'Aether',
                                                               'text': 'Seven inverted knots feeding off '
                                                                       'overhead starlight instead of '
                                                                       'living breath... No wonder she '
                                                                       'left the sample with you.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03A_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'Even from a single careful look, '
                                                                       "Huitzilin's seven-knot sequence "
                                                                       'imprints cleanly onto my memory '
                                                                       'alongside that haunting opening '
                                                                       'line.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C03_B_TEASE_ITZPAPA_CUSHION',
                                           'label': 'Close your eyes politely and hand Itzpapa over so '
                                                    'Granny Itztli can bury her blushing face in dignity.',
                                           'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N07',
                                           'reaction_beats': [{'beat_id': 'N06_C03B_R1',
                                                               'speaker': 'Citlali',
                                                               'text': 'I do NOT need emotional support '
                                                                       'plushies from a cheeky outlander! '
                                                                       '...Give me Itzpapa anyway, the sea '
                                                                       'breeze is chilly on my chin!',
                                                               'inner_thought': 'Why is he always gentle '
                                                                                'right when anyone else '
                                                                                'would laugh at me...?',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                                                               'voice_emotion': 'vn_shy_blush'},
                                                              {'beat_id': 'N06_C03B_R2',
                                                               'speaker': 'Aether',
                                                               'text': 'Eyes completely shut, Great '
                                                                       'Shaman. Nobody saw a thing except '
                                                                       'Citlalin.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03B_R3',
                                                               'speaker': 'Narrator',
                                                               'text': "Muffled behind Itzpapa's round "
                                                                       "crown, the rhythm of Citlali's "
                                                                       'thoughts settles into a warm, '
                                                                       'reluctant purr of relief.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_07_six_kitsune_cipher_diff.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': []},
           'N07': {'node_id': 'N07',
                   'chapter_id': 'CH1',
                   'title': 'Lanterns & Gossip at Dusk',
                   'day_label': 'Day 3 - Sunset',
                   'location': 'Coastal Promenade - Grainfruit Stall',
                   'beats': [{'beat_id': 'N07_B01',
                              'speaker': 'Narrator',
                              'text': 'By sunset of the third day, Mualani and Kachina manage a minor '
                                      'miracle: luring Citlali down to a lantern-strung coastal stall with '
                                      'grilled grainfruit skewers and sparkling fruit punch.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B02',
                              'speaker': 'Mualani',
                              'text': 'See, Kachina? I told you knocking non-stop works! Having Granny '
                                      'Itztli and Tumaini at the same table practically guarantees good '
                                      'surf for a month!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': 'outing_arrive_photo'},
                             {'beat_id': 'N07_B03',
                              'speaker': 'Citlali',
                              'text': 'I only came down because Paimon threatened to practice nose-flute '
                                      'ballads outside my bedroom shutter! Sit straight, Kachina, you have '
                                      'glaze on your nose.',
                              'inner_thought': 'Alright, fine, the sea breeze feels nice... especially '
                                               'since he pulled out the bench right beside his.',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N07_B04',
                              'speaker': 'Kachina',
                              'text': 'Ehehe, sorry Granny! Here, I saved you the crispiest honey-glazed '
                                      'skewer! Oh -- Paimon was just telling us about that eerie Ley Line '
                                      'anomaly up north!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B05',
                              'speaker': 'Mualani',
                              'text': 'Right, the one where the Abyss Order started weaving some spooky '
                                      'fate-loom underground! What happened in there, Paimon?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B06',
                              'speaker': 'Paimon',
                              'text': "Everything went super weird around the Night Kingdom's "
                                      'memory-threads! Nobody could see the monsters unless they shared '
                                      'perceptions --',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B07',
                              'speaker': 'Paimon',
                              'text': "-- so Aether had to walk around holding that shy girl Direidyth's "
                                      'hand the whole afternoon just to track them through the canyon!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B08',
                              'speaker': 'Narrator',
                              'text': "Across the cedar table, the wooden skewer in Citlali's fingers "
                                      'stops dead an inch from her lips.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B09',
                              'speaker': 'Narrator',
                              'text': 'Neither Paimon, Mualani, nor Kachina hears a single sound -- yet '
                                      'inside my skull alone, our private telepathic channel detonates.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N08'}]},
           'N08': {'node_id': 'N08',
                   'chapter_id': 'CH1',
                   'title': 'Why Holding Hands, Specifically?',
                   'day_label': 'Day 3 - Dusk',
                   'location': 'Coastal Promenade - Lantern Table',
                   'beats': [{'beat_id': 'N08_B01',
                              'speaker': 'Citlali',
                              'text': 'Hmph. Sounds dreadfully contrived if you ask me. Any half-competent '
                                      'shaman could trace residual Ley-miasma with an obsidian mirror '
                                      "instead of clinging to someone's fingers like a lost toddler.",
                              'inner_thought': "Holding hands?! Why holding hands specifically?! Couldn't "
                                               'they tie a spirit-cord to a sleeve--what kind of shameless '
                                               'excuse is that!',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N08_B02',
                              'speaker': 'Aether',
                              'text': 'Funny. If memory serves, a certain Great Shaman near Smoke-Drift '
                                      "Canyon didn't reach for an obsidian mirror either. She turned "
                                      "around and said, 'Here, give me your hand.'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B03',
                              'speaker': 'Citlali',
                              'text': 'Th-That was a strictly utilitarian sense-transfer incantation to '
                                      "find my errant grandson! Don't lump secret Night-Wind shamanic arts "
                                      'in with--stop grinning into your juice cup, Traveler!',
                              'inner_thought': 'Quiet, heart, quiet! He remembers the exact wording?! Ugh, '
                                               'if his palm brushes mine under this table I am going to '
                                               'combust...',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N08_B04',
                              'speaker': 'Mualani',
                              'text': 'Huh? Granny, your cheeks just turned the exact color of sunset '
                                      'punch! Is the chili glaze too spicy?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B05',
                              'speaker': 'Narrator',
                              'text': 'Before Citlali can snap back an excuse, a hairline crackle -- cold '
                                      'and colorless like static over dark water -- clips the final '
                                      'syllable of her mental voice.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C04',
                              'prompt': 'Paimon and Mualani are distracted by fresh skewers while Citlali '
                                        'fumes adorably beside you:',
                              'options': [{'opt_id': 'C04_A_OFFER_OPEN_PALM',
                                           'label': 'Slide your open palm quietly beneath the lantern-lit '
                                                    'table and answer her thought: only one shaman holds '
                                                    'my memory-color.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F04_HAND_PROMISE_GIVEN']},
                                           'next_node': 'N09',
                                           'reaction_beats': [{'beat_id': 'N08_C04A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Out of sight of Paimon and the '
                                                                       'girls, Citlali stares down at my '
                                                                       'open hand for three rapid '
                                                                       'heartbeats -- then slips her cool, '
                                                                       'slender fingers lightly across my '
                                                                       'palm.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_09_promenade_palm_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N08_C04A_R2',
                                                               'speaker': 'Citlali',
                                                               'text': '...Pass the chili salt, Mualani. '
                                                                       'This coastal wind is making my '
                                                                       'ears ridiculously warm.',
                                                               'inner_thought': '...unfair. Completely '
                                                                                "unfair, Traveler. Don't "
                                                                                'you dare let go until '
                                                                                'Paimon finishes that '
                                                                                'skewer.',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_09_promenade_palm_diff.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]},
                                          {'opt_id': 'C04_B_OBSERVE_SPECTRUM_GLITCH',
                                           'label': "Narrow your Color-of-Memory sight on Citlali's wrist "
                                                    'to catch why that cold white static clipped her '
                                                    'telepathy.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['SPECTRUM_GLITCH_SEEN']},
                                           'next_node': 'N09',
                                           'reaction_beats': [{'beat_id': 'N08_C04B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Focusing past the warm amber '
                                                                       'lantern glow, I catch a fleeting '
                                                                       'ring of bleached white light '
                                                                       "pulsing beneath Citlali's bracelet "
                                                                       '-- identical to an aftershock from '
                                                                       'that northern Loom-of-Fate tear.',
                                                               'inner_thought': "Her memory-aura didn't "
                                                                                'just flutter from '
                                                                                'embarrassment -- '
                                                                                'something pulled at its '
                                                                                'rose-lavender edge from '
                                                                                'below.',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N08_C04B_R2',
                                                               'speaker': 'Citlali',
                                                               'text': 'What are you squinting at my '
                                                                       'sleeve for? Eat your grainfruit '
                                                                       'before Paimon inhales your plate '
                                                                       'too!',
                                                               'inner_thought': '...did he notice the '
                                                                                'chill in my fingers? No, '
                                                                                'keep smiling, keep '
                                                                                'scolding...',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch1_08_promenade_friends_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': []},
           'N09': {'node_id': 'N09',
                   'chapter_id': 'CH2',
                   'title': 'Pale Lanterns in the Garden',
                   'day_label': 'Day 4 - Misty Morning',
                   'location': 'Sanctuary Back Wall - Herb Patch',
                   'beats': [{'beat_id': 'N09_B01',
                              'speaker': 'Narrator',
                              'text': 'Thick coastal fog rolls over Verona Point on the fourth morning, '
                                      'muffling the distant crash of the western surf beneath a silver '
                                      'hush.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B02',
                              'speaker': 'Narrator',
                              'text': "Behind the sanctuary's rear stone wall -- well out of earshot of "
                                      "Citlali's shuttered bedroom -- Ororon waves me over beside Elder "
                                      'Tlapo.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B03',
                              'speaker': 'Ororon',
                              'text': "Gramps, keep your voice low. Granny hasn't come out yet, and Claw "
                                      "wouldn't stop tapping my windowpane before sunrise.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B04',
                              'speaker': 'Aether',
                              'text': 'Claw fetched you himself? Show me what you found, Ororon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B05',
                              'speaker': 'Narrator',
                              'text': 'Ororon lifts a ventilated glass jar tucked inside his cloak. Half a '
                                      'dozen phlogiston aphids cling sluggishly to a mint twig inside -- '
                                      'their shells drained from warm golden-amber to chalky bone-white.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B06_F01',
                              'speaker': 'Aether',
                              'text': 'That chalk-white residue... It matches the colorless frost I read '
                                      'on her front doorway ward on Day One.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F01_SEAL_FROST_READ']}},
                             {'beat_id': 'N09_B06_NOF01',
                              'speaker': 'Aether',
                              'text': "I've never seen phlogiston aphids turn completely colorless without "
                                      'dying. They look like living chalk.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F01_SEAL_FROST_READ']}},
                             {'beat_id': 'N09_B07',
                              'speaker': 'Ororon',
                              'text': "They perched by the high stone vent of Granny's inner weaving room "
                                      "around midnight. None of them are hurt -- it's like every drop of "
                                      'color in their shells got drunk up by the mist.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B08',
                              'speaker': 'Ororon',
                              'text': 'Every night since the new moon cycle started four days ago, that '
                                      'inner room hums like an overloaded Wayob totem -- and then goes '
                                      'dead silent before dawn.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B09',
                              'speaker': 'Narrator',
                              'text': 'Beside us, Elder Tlapo presses his scarred forehead briefly against '
                                      'my sleeve, ancient amber eyes clouded with unmistakable dread.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B10',
                              'speaker': 'Narrator',
                              'text': 'Through the thick stone wall, our shared telepathic channel lies '
                                      'eerily quiet -- Citlali sleeping the leaden, dreamless sleep of '
                                      'sheer spiritual depletion.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N10'}]},
           'N10': {'node_id': 'N10',
                   'chapter_id': 'CH2',
                   'title': 'Chalk-White Phlogiston',
                   'day_label': 'Day 4 - Morning',
                   'location': 'Sanctuary Back Wall - Herb Patch',
                   'beats': [{'beat_id': 'N10_B01',
                              'speaker': 'Narrator',
                              'text': 'Elder Tlapo lowers his feathered crest, scratching three concentric '
                                      'arcs into the damp garden earth -- the Night-Wind glyph for an '
                                      'ancestral scroll seam.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B02',
                              'speaker': 'Ororon',
                              'text': "Granny always acts like she's invincible so the tribe won't worry "
                                      'about her. Even during the Abyss war, she scolded everyone else for '
                                      "being reckless while carrying half the Night-Wind's divinations "
                                      'alone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B03',
                              'speaker': 'Aether',
                              'text': "And if anyone asks whether she's tired, she threatens to break "
                                      'their legs.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B04',
                              'speaker': 'Ororon',
                              'text': "Exactly! If I ask her about these aphids directly, she'll claim "
                                      "she's inventing cabbage pesticide and hurl Itzpapa at my head.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B05',
                              'speaker': 'Ororon',
                              'text': "You're the only soul in Natlan whose voice reaches past her walls, "
                                      'Gramps. How do you want to handle this?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B06',
                              'speaker': 'Narrator',
                              'text': 'Inside the glass jar, a faint film of bleached dust clings to the '
                                      "cork stopper, pulsing in slow sympathy with the sanctuary's "
                                      'foundation stone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C05',
                              'prompt': 'Ororon holds out the jar of chalk-white phlogiston aphids beside '
                                        'the misty garden wall:',
                              'options': [{'opt_id': 'C05_A_TRACE_PALE_APHIDS',
                                           'label': "Touch a thread of golden phlogiston to the jar's "
                                                    'chalky dust to isolate the exact Night-Kingdom static '
                                                    'frequency.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F05_APHID_LOOM_TRACE']},
                                           'next_node': 'N11',
                                           'reaction_beats': [{'beat_id': 'N10_C05A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'The instant my golden resonance '
                                                                       'touches the glass, the chalky film '
                                                                       'shivers at a deep, hollow pitch -- '
                                                                       'chromatic unraveling along the '
                                                                       "Night Kingdom's archive border, "
                                                                       'triggered by that recent '
                                                                       'Loom-of-Fate shock.',
                                                               'inner_thought': 'Not an illness from '
                                                                                'outside. Something inside '
                                                                                'her loom chamber is '
                                                                                'drinking living '
                                                                                'memory-color every '
                                                                                'midnight.',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05A_R2',
                                                               'speaker': 'Ororon',
                                                               'text': 'Whoa -- look at their wings! Every '
                                                                       'aphid in the jar twitched back '
                                                                       'toward warm amber the second your '
                                                                       'golden light hit them!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05A_R3',
                                                               'speaker': 'Aether',
                                                               'text': 'Keep those aphids safe by your '
                                                                       'tuning fork, Ororon. That exact '
                                                                       'frequency may save her life before '
                                                                       'the week is out.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C05_B_HUMOR_GRAMPS_ORORON',
                                           'label': "Clap Ororon's shoulder warmly: tell him 'Gramps' will "
                                                    "stay close to Granny all week so she can't lock "
                                                    'everyone out.',
                                           'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N11',
                                           'reaction_beats': [{'beat_id': 'N10_C05B_R1',
                                                               'speaker': 'Ororon',
                                                               'text': 'Phew... Hearing you say that takes '
                                                                       'a boulder off my chest. Granny '
                                                                       "pretends she's made of obsidian, "
                                                                       'but she wears every feeling right '
                                                                       'on her sleeve around you.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05B_R2',
                                                               'speaker': 'Aether',
                                                               'text': "Don't let her catch you saying "
                                                                       'that unless you want cabbages '
                                                                       'orbiting your ears.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05B_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'From behind the upper terrace '
                                                                       'screen, a faint, flustered ripple '
                                                                       'crosses the mental link -- Citlali '
                                                                       'just woke up and caught the warm '
                                                                       'tail end of my promise.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_01_ororon_aphid_garden.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': []},
           'N11': {'node_id': 'N11',
                   'chapter_id': 'CH2',
                   'title': 'Two Centuries of Paint',
                   'day_label': 'Day 4 - Afternoon',
                   'location': 'Verona Sanctuary - Outer Graffiti Wall',
                   'beats': [{'beat_id': 'N11_B01',
                              'speaker': 'Narrator',
                              'text': 'By late afternoon the coastal fog lifts into clear bronze light. '
                                      'Citlali steps outside with her wide sleeves tied back in lavender '
                                      'ribbon, levitating a wooden bucket of soapy water toward the '
                                      'graffitied outer wall.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_02_graffiti_wall_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B02',
                              'speaker': 'Citlali',
                              'text': "Three more loudmouthed novices from Huitzilin's lineage tried their "
                                      'luck before lunch. Honestly -- six seconds against Itzpapa and they '
                                      'call that graduation prep?',
                              'inner_thought': 'Good... keep your voice brisk, Citlali. If you sound '
                                               "tired, he'll ask why your fingers shook holding the ladle.",
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_02_graffiti_wall_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N11_B03',
                              'speaker': 'Aether',
                              'text': "Six whole seconds? You're going soft on the younger generation, "
                                      'Granny Itztli. Pass me the second scrub-brush.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_02_graffiti_wall_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B04',
                              'speaker': 'Citlali',
                              'text': 'I was letting them finish chanting their names before bouncing them '
                                      'into the bushes! ...Here. Start on that hideous turquoise saurian '
                                      'doodle before it sets.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_02_graffiti_wall_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B05',
                              'speaker': 'Narrator',
                              'text': 'Warm suds hiss against sun-baked plaster as we scrub side by side, '
                                      'turquoise and vermilion boasts dissolving in bright rivulets down '
                                      'the stone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_02_graffiti_wall_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B06',
                              'speaker': 'Aether',
                              'text': 'You know, one scary containment rune across the bottom stair would '
                                      'stop every challenger from ever reaching this wall.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_02_graffiti_wall_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B07',
                              'speaker': 'Citlali',
                              'text': 'And waste perfectly good phlogiston on brats with paintbrushes? '
                                      "Scrubbing keeps my wrists limber, that's all!",
                              'inner_thought': 'Liar... If the wall ever stayed clean for a whole year, '
                                               'this cliff would feel like a tomb.',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_02_graffiti_wall_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B08',
                              'speaker': 'Narrator',
                              'text': 'Working down toward the corner foundation stone, my brush pauses '
                                      'inches from a tiny, sun-faded seven-petal wildflower painted in '
                                      'antique mineral ochre.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_02_graffiti_wall_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B09',
                              'speaker': 'Narrator',
                              'text': 'Decades of scrubbed plaster gleam clean all around it -- proving '
                                      'Citlali has washed carefully around that single corner flower '
                                      'hundreds of times.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_02_graffiti_wall_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N12'}]},
           'N12': {'node_id': 'N12',
                   'chapter_id': 'CH2',
                   'title': "Next Year's Wildflowers",
                   'day_label': 'Day 4 - Sunset',
                   'location': 'Verona Sanctuary - Sunset Foundation Stone',
                   'beats': [{'beat_id': 'N12_B01',
                              'speaker': 'Narrator',
                              'text': "Sunset turns the western surf molten gold. Citlali's brush slows, "
                                      'hovering a breath above that tiny seven-petal corner mark without '
                                      'touching a single bristle to it.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B02',
                              'speaker': 'Citlali',
                              'text': '...Huitzilin painted that corner mark the night we fought to our '
                                      'only draw. Back when I still assumed everyone strong stayed young '
                                      'just as effortlessly as I did.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N12_B03',
                              'speaker': 'Citlali',
                              'text': 'Twenty years later we crossed paths again, and I saw the silver '
                                      'threads at her temples. That night I watched a meteor cut the sky '
                                      'and finally admitted what two hundred years meant for me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B04',
                              'speaker': 'Aether',
                              'text': 'That was when you asked her about the wildflowers after the dry '
                                      'season.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B05',
                              'speaker': 'Citlali',
                              'text': 'She smiled and told me wildflowers always bloom again when the '
                                      'rains return. And I snapped right back -- how does that help the '
                                      "flowers standing here today? None of them ever feel next year's "
                                      'sun.',
                              'inner_thought': "In the Seven-Hued Ruins I finally heard her answer: 'the "
                                               "color of memories.' Yet watching gold fade still terrifies "
                                               'me...',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B06',
                              'speaker': 'Narrator',
                              'text': 'Amber light catches the pale rose cascade of her hair as she lowers '
                                      'the wooden brush into the bucket, her knuckles white on the rim.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B07',
                              'speaker': 'Citlali',
                              'text': "After she died, I shut my gate and swore I wouldn't collect more "
                                      "faces just to bury them. Keeping Huitzilin's answer safe for the "
                                      'dead was easy.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B08',
                              'speaker': 'Citlali',
                              'text': 'Letting someone living step past my door while time keeps '
                                      'marching... what if even a star-traveler eventually leaves only '
                                      'faded ochre on stone?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B09',
                              'speaker': 'Narrator',
                              'text': 'As she lifts a small shamanic water-seal to rinse the upper wall, a '
                                      'faint shimmer of rose-lavender mist slips from her fingertips into '
                                      'the dusk.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C06',
                              'prompt': "Citlali's fingertips hover near Huitzilin's two-hundred-year-old "
                                        'corner mark in the sunset:',
                              'options': [{'opt_id': 'C06_A_SPARE_HUITZILIN_MARK',
                                           'label': 'Guide her wet sleeve gently clear of the seven-petal '
                                                    'mark: tell her you understand why she never banned '
                                                    'those challengers.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F06_GRAFFITI_TRUTH_HEARD']},
                                           'next_node': 'N13',
                                           'reaction_beats': [{'beat_id': 'N12_C06A_R1',
                                                               'speaker': 'Citlali',
                                                               'text': '...You really do see straight '
                                                                       'through two centuries of bluster, '
                                                                       "don't you? As long as noisy kids "
                                                                       'keep painting my wall, part of me '
                                                                       "gets to pretend she's still "
                                                                       'sending them.',
                                                               'inner_thought': 'Even if tomorrow takes '
                                                                                "everything else... I'm "
                                                                                'glad he knew why that '
                                                                                'little flower stayed on '
                                                                                'the stone.',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                                                               'voice_emotion': 'vn_tender_love'},
                                                              {'beat_id': 'N12_C06A_R2',
                                                               'speaker': 'Aether',
                                                               'text': 'And unlike dry-season petals, '
                                                                       "Citlali, I'm going to be right "
                                                                       'here arguing over paint buckets '
                                                                       'two hundred years from now.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06A_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'Together we rinse the upper '
                                                                       "plaster clean, leaving Huitzilin's "
                                                                       'small seven-petal flower glowing '
                                                                       'untouched in the amber dusk.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C06_B_ANALYZE_PIGMENT_DRAIN',
                                           'label': 'Watch the shamanic cleansing mist leaving her '
                                                    'fingertips to time the exact rate of her '
                                                    'rose-lavender pigment loss.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['PIGMENT_DRAIN_TIMED']},
                                           'next_node': 'N13',
                                           'reaction_beats': [{'beat_id': 'N12_C06B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Every seven heartbeats, the soft '
                                                                       "lavender shimmer around Citlali's "
                                                                       'fingertips drops out completely '
                                                                       'for half a second -- following the '
                                                                       'exact twelve-day tidal harmonic of '
                                                                       "Natlan's new moon.",
                                                               'inner_thought': "Whatever scroll she's "
                                                                                'feeding at midnight will '
                                                                                'hit critical depletion on '
                                                                                'the eleventh night.',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06B_R2',
                                                               'speaker': 'Aether',
                                                               'text': 'Leave the heavy rinsing to me, '
                                                                       'Citlali. Your hands are already '
                                                                       'cold from the bucket.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06B_R3',
                                                               'speaker': 'Citlali',
                                                               'text': 'Hmph... Bossy outlander. Make sure '
                                                                       "you don't splash soap near that "
                                                                       'bottom stone, then.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_03_graffiti_sunset_diff.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': []},
           'N13': {'node_id': 'N13',
                   'chapter_id': 'CH2',
                   'title': 'Meteors Above Verona Roof',
                   'day_label': 'Day 5 - Starlit Night',
                   'location': 'Sanctuary Flat Roof - Stargazing Mat',
                   'beats': [{'beat_id': 'N13_B01',
                              'speaker': 'Narrator',
                              'text': 'On the fifth night, crisp trade winds sweep every cloud from the '
                                      'coastal sky, unveiling a river of stars above Verona Point.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B02',
                              'speaker': 'Narrator',
                              'text': "Up on the sanctuary's woven stargazing roof, brass astrolabes glint "
                                      'softly beside warm herbal tea while Itzpapa and Citlalin nestle '
                                      "like twin bolsters at Citlali's knees.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B03',
                              'speaker': 'Narrator',
                              'text': 'High across the southern constellations, a pale silver meteor '
                                      'scratches a fleeting line of white fire before vanishing over the '
                                      'dark water.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B04',
                              'speaker': 'Aether',
                              'text': 'Clearer sky than even the high plateaus tonight. Did the stars tell '
                                      'Granny Itztli anything auspicious?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B05',
                              'speaker': 'Citlali',
                              'text': 'They told me certain star-travelers have far too much free time on '
                                      'their hands. Honestly... outlanders collect souvenirs at an '
                                      "alarming rate, don't they?",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N13_B06',
                              'speaker': 'Citlali',
                              'text': 'Windwheel charms from Mondstadt, glaze lilies pressed in Liyue '
                                      'ledgers, shrine slips from Inazuma... everything tossed together at '
                                      'the bottom of one bottomless pack.',
                              'inner_thought': "Just ask casually, Citlali! Don't make it sound like you "
                                               'care whether he still carries your handkerchief!',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B07',
                              'speaker': 'Aether',
                              'text': 'That sounds suspiciously specific, Citlali. Are we auditing my '
                                      'whole inventory, or asking about one rose-lavender keepsake in '
                                      'particular?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B08',
                              'speaker': 'Narrator',
                              'text': "Citlali's fingers tighten instantly around Citlalin's plush ears, "
                                      'her silhouette stiffening against the starlight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B09',
                              'speaker': 'Narrator',
                              'text': 'Yet beneath the familiar spike of embarrassment across our link '
                                      'lies a quieter, sharper fear she is trying desperately to muffle.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N14'}]},
           'N14': {'node_id': 'N14',
                   'chapter_id': 'CH2',
                   'title': 'The Rose-Lavender Keepsake',
                   'day_label': 'Day 5 - Starlit Night',
                   'location': 'Sanctuary Flat Roof - Under Falling Stars',
                   'beats': [{'beat_id': 'N14_B01',
                              'speaker': 'Citlali',
                              'text': 'I-I am making a purely academic inquiry into phlogiston retention! '
                                      'If that handkerchief I wove ended up crumpled under fifty hilichurl '
                                      'masks, see if I ever craft so much as a shoelace for you again!',
                              'inner_thought': "...please tell me its color hasn't started bleaching in "
                                               'his pocket too. If my hue stays whole on him, maybe--',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N14_B02',
                              'speaker': 'Narrator',
                              'text': 'There it is -- the real reason behind her question. Not vanity, but '
                                      'dread that the colorless drain inside her sanctuary is erasing '
                                      'every trace of her from the world.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B03',
                              'speaker': 'Aether',
                              'text': 'You never wove that handkerchief as an academic test, Citlali. You '
                                      'told me to keep your color in my memory.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B04',
                              'speaker': 'Citlali',
                              'text': "S-Semantics! A Great Shaman's memory-thread is delicate work, "
                                      "alright?! In Teyvat's Ley-winds, unattended dyes lose half their "
                                      'saturation in a season...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B05',
                              'speaker': 'Narrator',
                              'text': 'Even wrapped in her woven shawl beneath the clear stars, a subtle '
                                      'chill runs through her shoulders as the midnight sea-wind rises.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B06',
                              'speaker': 'Narrator',
                              'text': 'Across the mat, her rose-gold eyes linger nervously on my coat over '
                                      'my heart.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C07',
                              'prompt': 'Citlali hugs Citlalin tightly under the meteors, secretly '
                                        'dreading that her color is fading even on you:',
                              'options': [{'opt_id': 'C07_A_KNOT_ROSE_HANDKERCHIEF',
                                           'label': 'Draw her rose-lavender handkerchief warm from over '
                                                    'your heart and knot a fine thread of Descender gold '
                                                    'into its corner.',
                                           'effects': {'bond': 1,
                                                       'insight': 1,
                                                       'add_flags': ['F07_ROSE_HANDKERCHIEF']},
                                           'next_node': 'N15',
                                           'reaction_beats': [{'beat_id': 'N14_C07A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Unfolded between us under the '
                                                                       'starlight, her rose-lavender silk '
                                                                       'glows vivid and unblemished -- '
                                                                       'answering my golden phlogiston '
                                                                       'knot with a warm, steady chime.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_05_rooftop_handkerchief_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07A_R2',
                                                               'speaker': 'Citlali',
                                                               'text': '...Show-off. Keeping it folded in '
                                                                       "your inner breast pocket doesn't "
                                                                       "prove anything except that you're "
                                                                       'overly sentimental.',
                                                               'inner_thought': "It didn't fade! On him, "
                                                                                'outside the Ley Lines, my '
                                                                                "rose-lavender hue hasn't "
                                                                                'lost a single shade!',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_05_rooftop_handkerchief_diff.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'},
                                                              {'beat_id': 'N14_C07A_R3',
                                                               'speaker': 'Aether',
                                                               'text': 'Tucked right back over my heart -- '
                                                                       'with my gold knotted into your '
                                                                       'silk so neither shade goes '
                                                                       'anywhere.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_05_rooftop_handkerchief_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C07_B_WRAP_CLOAK_STARLIGHT',
                                           'label': 'Unclasp your warm travel cloak, drape it around '
                                                    'Citlali and Itzpapa together, and stay '
                                                    'shoulder-to-shoulder under the stars.',
                                           'effects': {'bond': 3,
                                                       'insight': 0,
                                                       'add_flags': ['CLOAK_STARLIGHT_WARMTH']},
                                           'next_node': 'N15',
                                           'reaction_beats': [{'beat_id': 'N14_C07B_R1',
                                                               'speaker': 'Citlali',
                                                               'text': "W-Wait -- you'll freeze in just "
                                                                       'your tunic! ...Ugh, stubborn '
                                                                       'outlander. Fine, sit closer then '
                                                                       'so one cloak covers both of us, '
                                                                       'idiot.',
                                                               'inner_thought': 'So warm... It smells like '
                                                                                'sunlight and star-dust. '
                                                                                'Just five more minutes '
                                                                                'before midnight calls me '
                                                                                'downstairs...',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                                                               'voice_emotion': 'vn_tender_love'},
                                                              {'beat_id': 'N14_C07B_R2',
                                                               'speaker': 'Aether',
                                                               'text': 'Plenty of warmth to spare when '
                                                                       "Granny stops pretending she's "
                                                                       'immune to night wind.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07B_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'Resting lightly against my '
                                                                       'shoulder beneath the shared cloak, '
                                                                       "Citlali's breathing slows until "
                                                                       'the roof lanterns burn low.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_04_rooftop_stars_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': []},
           'N15': {'node_id': 'N15',
                   'chapter_id': 'CH2',
                   'title': 'Opaque Stoneware in the Rain',
                   'day_label': 'Day 6 - Late Night',
                   'location': 'Sanctuary Study - Rain-Tapped Shutters',
                   'beats': [{'beat_id': 'N15_B01',
                              'speaker': 'Narrator',
                              'text': 'Cold rain lashes the cedar shutters on the sixth night, drumming '
                                      "steadily across Verona's cliffside eaves.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B02',
                              'speaker': 'Narrator',
                              'text': 'Paimon and I duck inside with a covered pot of hot stew just before '
                                      'eleven, finding Citlali already seated beside a single low oil '
                                      'lamp.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B03',
                              'speaker': 'Narrator',
                              'text': 'Lifting a dark glazed stoneware flask, Citlali pours carefully into '
                                      'two opaque, hand-painted Night-Wind ceramic goblets whose thick '
                                      'obsidian rims hide the liquid inside from view.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B04',
                              'speaker': 'Citlali',
                              'text': 'Sweet fermented Quenepa Berry vintage from last harvest. Take one '
                                      'sip to warm off the rain and then march straight back to the harbor '
                                      'inn -- a Great Shaman needs quiet tonight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B05',
                              'speaker': 'Aether',
                              'text': 'Throwing us out in a downpour before we even ladle the stew? '
                                      'Usually you at least confiscate dessert first.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B06',
                              'speaker': 'Narrator',
                              'text': 'Citlali lifts her opaque painted goblet with both hands and takes a '
                                      'slow swallow, smiling a fraction too stiffly across the lamp-lit '
                                      'reed table.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B07',
                              'speaker': 'Citlali',
                              'text': 'Tart skin, rich golden-berry finish... Almost too sweet this year, '
                                      'honestly. Hurry up and finish your plate, Paimon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B08',
                              'speaker': 'Paimon',
                              'text': 'Mmph -- hey, wait a second! Paimon just ate the very last honeyed '
                                      "grainfruit cake off Citlali's special plate right in front of her, "
                                      "and Citlali didn't glare, stomp, or threaten Paimon once!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B09',
                              'speaker': 'Paimon',
                              'text': "Aether, check Citlali's forehead! Somebody replaced Granny Itztli "
                                      'with a polite Bake-Danuki!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B10',
                              'speaker': 'Narrator',
                              'text': 'Paimon hovers in genuine alarm, completely oblivious as ever to our '
                                      "private mental bridge -- while inside my skull, Citlali's usually "
                                      'vivid presence sounds frighteningly thin, and zero scent of Quenepa '
                                      'fruit hangs in the air.',
                              'inner_thought': "Whatever is inside those opaque stoneware cups isn't "
                                               'fermented berry wine.',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_06_quenepa_lamp_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N16'}]},
           'N16': {'node_id': 'N16',
                   'chapter_id': 'CH2',
                   'title': 'White Static in the Soul-Link',
                   'day_label': 'Day 6 - Midnight',
                   'location': 'Sanctuary Study - Low Reed Table',
                   'beats': [{'beat_id': 'N16_B01',
                              'speaker': 'Narrator',
                              'text': 'Outside in the rain, the harbor bell tolls the first stroke of '
                                      'midnight -- and a low, sub-audible tremor rolls out from the '
                                      "sanctuary's locked back door.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B02',
                              'speaker': 'Narrator',
                              'text': 'Citlali flinches, reaching to set down her painted stoneware goblet '
                                      '-- and her frost-numbed fingers fail to feel the cedar table edge '
                                      'at all.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B03',
                              'speaker': 'Narrator',
                              'text': 'Hand-painted Night-Wind stoneware strikes the reed mat and splits '
                                      'cleanly in two. Clear, odorless cold water -- not pale-golden '
                                      "Quenepa wine -- soaks the hem of Citlali's skirt while white rime "
                                      'crusts every knuckle.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B04',
                              'speaker': 'Aether',
                              'text': "Citlali -- that's plain water! You couldn't taste it, or even see "
                                      'that it had no color when you poured from the kettle, could you?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B05',
                              'speaker': 'Citlali',
                              'text': "Clumsy cup... Don't make that face at me, Traveler! Do you have any "
                                      "idea how ridiculous Natlan's hero looks hovering over spilled "
                                      'water? Take Paimon back to town -- I still have scroll-work left!',
                              'inner_thought': "[...cold... don't let him touch my wrist... if the loom "
                                               "drinks his gold mark next, please don't let me forget the "
                                               'sound of his-- ...]',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                              'voice_emotion': 'outing_bump_rescue'},
                             {'beat_id': 'N16_B06',
                              'speaker': 'Paimon',
                              'text': "Wha-- Citlali's fingertips are turning white with frost! Aether, do "
                                      'something!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B07',
                              'speaker': 'Narrator',
                              'text': "Inside my mind, Citlali's thought-stream tears mid-word into jagged "
                                      'white static -- fulfilling the terrifying law she herself once '
                                      'spoke: our mental bond breaks only when one of us begins losing the '
                                      'memory of the other!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C08',
                              'prompt': "Broken stoneware gleams in clear spilled water while Citlali's "
                                        'thought-stream fractures into static:',
                              'options': [{'opt_id': 'C08_A_CATCH_FROSTED_WRIST',
                                           'label': 'Catch her frost-numbed right wrist gently to trace '
                                                    'the colorless pigment-drain climbing her meridian '
                                                    'toward the inner door.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F08_QUENEPA_CONFESSION']},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_C08A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Skin cold as glacier melt meets my '
                                                                       'palm. Under Color-of-Memory sight, '
                                                                       'a visible ribbon of rose-lavender '
                                                                       'light is being siphoned straight '
                                                                       'out of her pulse toward the locked '
                                                                       'inner Astral Loom door.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08A_R2',
                                                               'speaker': 'Citlali',
                                                               'text': 'Let go, Aether... please. My taste '
                                                                       'and peripheral color-sight have '
                                                                       'been bleeding into that room every '
                                                                       'midnight since Night One.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08A_R3',
                                                               'speaker': 'Aether',
                                                               'text': 'Then tonight is the last midnight '
                                                                       'you pay that bill by yourself.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C08_B_HOLD_THROUGH_STATIC',
                                           'label': 'Enclose both of her freezing hands against your chest '
                                                    'and project your clearest golden memory straight '
                                                    'across the static.',
                                           'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_C08B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Golden Descender warmth floods '
                                                                       'into her icy fingers. Inside my '
                                                                       'mind, the terrifying hiss of white '
                                                                       'static recedes just enough for one '
                                                                       'trembling breath to come through '
                                                                       'intact.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08B_R2',
                                                               'speaker': 'Citlali',
                                                               'text': '...Idiot. If you hold on like that '
                                                                       'when the midnight draw peaks, '
                                                                       "it'll pull you toward the seam "
                                                                       'too...',
                                                               'inner_thought': '...thank goodness. His '
                                                                                'gold is still right here. '
                                                                                'I still remember every '
                                                                                'word...',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                                                               'voice_emotion': 'vn_shy_blush'},
                                                              {'beat_id': 'N16_C08B_R3',
                                                               'speaker': 'Aether',
                                                               'text': 'Hold onto my voice, Citlali. Now '
                                                                       "show me what's behind that inner "
                                                                       'door.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_07_quenepa_shatter_diff.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': []},
           'N17': {'node_id': 'N17',
                   'chapter_id': 'CH2',
                   'title': 'The Bleaching Ukumbuko Scroll',
                   'day_label': 'Day 6 - Past Midnight',
                   'location': 'Inner Sanctum - Obsidian Astral Loom Chamber',
                   'pre_events': [{'when': {'forbid_flags': ['F07_ROSE_HANDKERCHIEF'],
                                            'min_bond': 7,
                                            'min_insight': 8},
                                   'effects': {'add_flags': ['F07_ROSE_HANDKERCHIEF',
                                                             'F07_SECOND_CHANCE_N17']}}],
                   'beats': [{'beat_id': 'N17_B01',
                              'speaker': 'Narrator',
                              'text': 'At the rear of the study, the heavy containment ward sealing '
                                      "Citlali's inner loom chamber crackles and fractures -- starved of "
                                      'the very pigment meant to hold it shut.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B01_F01',
                              'speaker': 'Aether',
                              'text': 'Just like the frost on your front lintel -- the drain has hollowed '
                                      'out your containment runes from the inside!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F01_SEAL_FROST_READ']}},
                             {'beat_id': 'N17_B02',
                              'speaker': 'Narrator',
                              'text': 'Pressing the shamanic ownership-imprint of her house key together '
                                      "with Tumaini's golden phlogiston against the weakened inner latch, "
                                      'I push the obsidian doors wide.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B03',
                              'speaker': 'Narrator',
                              'text': 'Suspended above a circular Wayob conduit hangs the towering '
                                      'First-Era Ukumbuko Chronicle Scroll -- three centuries of Masters '
                                      'of the Night-Wind dead woven around an ancient, dormant Obsidian '
                                      'Name-Core.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B04',
                              'speaker': 'Narrator',
                              'text': 'Across its lower third, a jagged scar from the recent Loom-of-Fate '
                                      'shockwave is bleaching the tapestry bone-white, drinking ribbons of '
                                      "Citlali's own rose-lavender memory-pigment to keep Huitzilin's era "
                                      'from vanishing.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B05_RESCUE',
                              'speaker': 'Narrator',
                              'text': "Inside my coat pocket, Citlali's rose-lavender handkerchief "
                                      'suddenly flares hot in sympathetic resonance with the dormant '
                                      'Name-Core -- prompting me to bind a golden phlogiston thread around '
                                      'its hem on the spot!',
                              'inner_thought': "Her living color on my person is answering the scroll's "
                                               'cry directly.',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B06',
                              'speaker': 'Citlali',
                              'text': 'Five nights left until the twelfth new-moon tide... If nobody feeds '
                                      'high-density living hue into that tear, three hundred years of '
                                      "Night-Wind souls -- and Huitzilin's last thread -- dissolve into "
                                      'white noise.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B07',
                              'speaker': 'Citlali',
                              'text': "Mavuika's raw Sacred Flame would burn mortal silk to ash, and "
                                      "Yohualtecuhtin's Ley-vessel cannot author living emotion! After two "
                                      'centuries alone, my brightest colors are Huitzilin... and you, '
                                      'Aether.',
                              'inner_thought': '[...if I let him help and fail, watching me forget him in '
                                               'front of his eyes will hurt worse than dying...]',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B08',
                              'speaker': 'Aether',
                              'text': 'Five nights is four nights more than we need -- provided Granny '
                                      'Itztli stops pretending she has to bleed in the dark alone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C09',
                              'prompt': 'Five nights remain before the New-Moon Tide consumes the '
                                        'First-Era Ukumbuko Scroll. Choose your path:',
                              'options': [{'opt_id': 'C09_ROUTE_A_SOUL_BRIDGE',
                                           'label': '[Route A - Tandem Soul-Bridge] Clasping her hand just '
                                                    'as she once clasped yours, dive directly into her '
                                                    'memory-palette to co-weave from within.',
                                           'effects': {'bond': 1, 'insight': 0, 'add_flags': ['ROUTE_A']},
                                           'next_node': 'N18_A1',
                                           'reaction_beats': [{'beat_id': 'N17_C09A_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'You started this bond by saying '
                                                                       "'Give me your hand.' Starting "
                                                                       'tomorrow midnight, Elder Tlapo '
                                                                       'guards the door while we step into '
                                                                       'that weave together.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N17_C09A_R2',
                                                               'speaker': 'Citlali',
                                                               'text': "...Reckless idiot. Don't complain "
                                                                       'to me when two hundred years of '
                                                                       'grumpy memories bury you up to '
                                                                       'your ears!',
                                                               'inner_thought': '...he really means to '
                                                                                'walk straight into my '
                                                                                'heart without '
                                                                                'flinching...',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C09_ROUTE_B_SEVEN_HUED_MAZE',
                                           'label': '[Route B - Seven-Hued Abyss] Leave Paimon on watch '
                                                    'and descend the Seven-Hued Ruins chasm with Ororon '
                                                    'and Chasca to sever the lower spindle drain.',
                                           'effects': {'bond': 0, 'insight': 1, 'add_flags': ['ROUTE_B']},
                                           'next_node': 'N22_B1',
                                           'reaction_beats': [{'beat_id': 'N17_C09B_R1',
                                                               'speaker': 'Aether',
                                                               'text': "A scroll doesn't siphon backward "
                                                                       'unless an older spindle below the '
                                                                       'Seven-Hued Ruins broke loose. '
                                                                       'Paimon, keep Granny resting till '
                                                                       'dawn -- Ororon, Chasca, and I are '
                                                                       'cutting the root!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N17_C09B_R2',
                                                               'speaker': 'Citlali',
                                                               'text': "W-Wait -- Huitzilin's lower "
                                                                       'dye-vaults are crawling with '
                                                                       'Rifthounds! You had better check '
                                                                       'in across our link every hour, '
                                                                       'Traveler!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C09_ROUTE_C_TRIBAL_COUNCIL',
                                           'label': '[Route C - Council of Six Flames] Invoke your Ancient '
                                                    'Name Tumaini to summon Mavuika, Xilonen, and her '
                                                    'Natlan friends directly to the sanctuary.',
                                           'effects': {'bond': 1, 'insight': 0, 'add_flags': ['ROUTE_C']},
                                           'next_node': 'N26_C1',
                                           'reaction_beats': [{'beat_id': 'N17_C09C_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Two hundred years of locking out '
                                                                       'people who love you ends tonight. '
                                                                       "By morning, Xilonen's chisel and "
                                                                       "Mavuika's regulated flame will be "
                                                                       'standing on your terrace.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N17_C09C_R2',
                                                               'speaker': 'Citlali',
                                                               'text': 'Are you trying to save my life or '
                                                                       'give me heart failure?! Summoning '
                                                                       'the Pyro Archon into my messy '
                                                                       'living room -- Aether, get back '
                                                                       'here!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/citlali/ch2_08_astralloom_reveal.jpg',
                                                               'voice_emotion': 'vn_playful_tease'}]}]},
                   'routing': []},
           'N18_A1': {'node_id': 'N18_A1',
                      'chapter_id': 'CH3',
                      'title': 'Stepping Into Her Palette',
                      'day_label': 'Day 7 - Midnight',
                      'location': 'Astral Loom Sanctum - Tandem Soul-Bridge',
                      'beats': [{'beat_id': 'N18_B01',
                                 'speaker': 'Narrator',
                                 'text': "We force ourselves to rest through Day Seven's afternoon rain -- "
                                         'sleeping beneath warm wool blankets while Paimon heats '
                                         'ginger-herb broth Ororon left quietly outside the gate.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B02',
                                 'speaker': 'Narrator',
                                 'text': 'When the seventh midnight approaches, seven beeswax tapers '
                                         'circle the Astral Loom basin, throwing long violet shadows up '
                                         'the towering First-Era Scroll.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B03_F11',
                                 'speaker': 'Narrator',
                                 'text': 'Perched outside the open stone transom, Elder Tlapo sets his '
                                         'pale-iridescent wing feather beside Citlalin and Itzpapa to '
                                         "steady the sanctum's outer boundary.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F11_CLAW_IKTOMI_FEATHER']}},
                                {'beat_id': 'N18_B03_NOF11',
                                 'speaker': 'Narrator',
                                 'text': 'Perched outside the open stone transom, Elder Tlapo folds his '
                                         'scarred wings like a silent sentinel while Citlalin and Itzpapa '
                                         'guard the doorway.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': '',
                                 'when': {'forbid_flags': ['F11_CLAW_IKTOMI_FEATHER']}},
                                {'beat_id': 'N18_B04',
                                 'speaker': 'Citlali',
                                 'text': 'Listen carefully before our pulses lock, Traveler. Sharing '
                                         'surface thoughts in Smoke-Drift Canyon was wading ankle-deep in '
                                         'tidewater compared to a Tandem Soul-Bridge.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B05',
                                 'speaker': 'Citlali',
                                 'text': "Inside a Night-Wind weaver's palette, centuries don't line up "
                                         'neatly like chapters. Every petty grudge, every unfinished '
                                         'regret, every night I refused to grieve properly sits right '
                                         'behind the mist.',
                                 'inner_thought': 'If he sees how pathetically lonely those two hundred '
                                                  'years really were, my dignified Granny Itztli image is '
                                                  'finished...',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B06',
                                 'speaker': 'Aether',
                                 'text': 'I stopped believing the fearsome hermit act the afternoon I saw '
                                         'seven privacy runes guarding Inazuman romance novels.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B07',
                                 'speaker': 'Citlali',
                                 'text': 'Those were literary references for shamanic allegory, and if you '
                                         'repeat that inside my own subconscious I will kick you straight '
                                         'out!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N18_B08',
                                 'speaker': 'Narrator',
                                 'text': 'Despite the scolding edge in her voice, Citlali extends both '
                                         'hands over the obsidian water-mirror without hiding the slight '
                                         'tremble in her wrists.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B09',
                                 'speaker': 'Aether',
                                 'text': 'No walls tonight, Citlali. Wherever the tide pulls, keep your '
                                         'eyes on my gold.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B10',
                                 'speaker': 'Citlali',
                                 'text': "...Don't let go first, then. Here -- give me your hands.",
                                 'inner_thought': 'Warm... Even with frost in my veins, his palms feel '
                                                  'like noon sun.',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': 'vn_shy_blush'},
                                {'beat_id': 'N18_B11',
                                 'speaker': 'Narrator',
                                 'text': 'Her cool fingers lace firmly through mine above the dark basin.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B12',
                                 'speaker': 'Narrator',
                                 'text': 'A resonant chime rings through bone and spirit alike as '
                                         'rose-lavender mist braids around Descender gold.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B13',
                                 'speaker': 'Narrator',
                                 'text': 'In a single breath, cedar walls and coastal rain dissolve away '
                                         '-- opening onto an endless horizon of living, painted twilight.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_01_soulbridge_handclasp.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N19_A2'}]},
           'N19_A2': {'node_id': 'N19_A2',
                      'chapter_id': 'CH3',
                      'title': 'Echo of the Wildflower Draw',
                      'day_label': 'Day 8 - Midnight Dive',
                      'location': "Citlali's Memory-Space - Moonlit Wildflower Field",
                      'beats': [{'beat_id': 'N19_B01',
                                 'speaker': 'Narrator',
                                 'text': 'We surface at dawn of Day Eight soaked in cold sweat, rest '
                                         'through noon over honeyed flatbreads while Paimon fusses '
                                         "anxiously outside, and dive deeper when Night Eight's Ley-tide "
                                         "opens the second stratum of Citlali's mind.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Around our boots sways a boundless Natlan plateau painted in '
                                         'luminous seven-color memory-dye, every blade of grass humming '
                                         'with preserved emotion.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B03',
                                 'speaker': 'Narrator',
                                 'text': 'Fifty paces ahead, a younger Citlali lowers her smoking obsidian '
                                         'talisman opposite a bright-eyed shaman laughing beside a sleek, '
                                         'unscarred young Claw.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B04_F06',
                                 'speaker': 'Aether',
                                 'text': "That seven-petal emblem woven on Huitzilin's sash -- it's the "
                                         'exact corner flower you spared on your sanctuary wall.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F06_GRAFFITI_TRUTH_HEARD']}},
                                {'beat_id': 'N19_B04_NOF06',
                                 'speaker': 'Aether',
                                 'text': "So that's Huitzilin in her prime... Even her laughter sounds "
                                         'like wind through canyon chimes.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': '',
                                 'when': {'forbid_flags': ['F06_GRAFFITI_TRUTH_HEARD']}},
                                {'beat_id': 'N19_B05',
                                 'speaker': 'Citlali',
                                 'text': 'Our tenth duel -- and the only draw either of us ever conceded. '
                                         'Watch what happens to the sky when time starts moving, Aether.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B06',
                                 'speaker': 'Narrator',
                                 'text': 'Like wet watercolor under sudden rain, decades wash across the '
                                         "meadow in heartbeats. Huitzilin's dark braids streak silver, "
                                         'then thin into translucent mist.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B07',
                                 'speaker': 'Narrator',
                                 'text': 'One after another, elders, apprentices, and childhood rivals '
                                         'blur into faceless grey silhouettes and blow away -- leaving the '
                                         'younger Citlali standing utterly alone in cold dry-season rain.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B08',
                                 'speaker': 'Citlali',
                                 'text': 'Twenty years turned into a hundred before I dared look out my '
                                         'window again. Every mortal voice I cared for dissolved like '
                                         "dry-season petals -- leaving only Huitzilin's wildflowers.",
                                 'inner_thought': 'Every voice except the golden one holding my hand right '
                                                  'now...',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B09',
                                 'speaker': 'Aether',
                                 'text': 'Look at the far ridge, Citlali -- the Loom-of-Fate tear is '
                                         'gnawing straight into the edge of this meadow!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B10',
                                 'speaker': 'Narrator',
                                 'text': 'Along the northern horizon of the memory-field, jagged '
                                         'bone-white static devours grass and starlight alike.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B11',
                                 'speaker': 'Narrator',
                                 'text': 'Above the advancing static, seven painted constellations pulse '
                                         'in faint Counter-Weave lines while the solitary memory-echo of '
                                         'young Citlali shivers in the rain.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C10_A',
                                 'prompt': "Inside Citlali's 200-year memory meadow, white static creeps "
                                           "toward Huitzilin's sky:",
                                 'options': [{'opt_id': 'C10_A1_READ_WILDFLOWER_ECHO',
                                              'label': 'Study how Huitzilin tied her wildflower '
                                                       'dye-threads to recurring starlight constellations '
                                                       'above the meadow.',
                                              'effects': {'bond': 0,
                                                          'insight': 2,
                                                          'add_flags': ['WILDFLOWER_STAR_ANCHOR']},
                                              'next_node': 'N20_A3',
                                              'reaction_beats': [{'beat_id': 'N19_C10A1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Looking upward through '
                                                                          'Color-of-Memory sight, I spot '
                                                                          "Huitzilin's subtle trick: she "
                                                                          'anchored her seven-color warp '
                                                                          'to overhead star-paths rather '
                                                                          'than fragile mortal heartbeats.',
                                                                  'inner_thought': 'With that stellar '
                                                                                   'anchor, we can '
                                                                                   'redirect the Ukumbuko '
                                                                                   "Scroll's tension "
                                                                                   'tomorrow night.',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N19_C10A1_R2',
                                                                  'speaker': 'Citlali',
                                                                  'text': 'Wait -- she tied the upper warp '
                                                                          'to the southern circumpolar '
                                                                          'stars?! Even I missed that '
                                                                          'angle because I was staring at '
                                                                          'the flowers!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N19_C10A1_R3',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Got the stellar bearing locked. '
                                                                          "Come on -- let's surface before "
                                                                          'dawn drains your pulse.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C10_A2_SHELTER_YOUNG_CITLALI',
                                              'label': 'Step beside Citlali and weave golden warmth over '
                                                       'her solitary memory-echo so two centuries of rain '
                                                       'stop falling on her.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N20_A3',
                                              'reaction_beats': [{'beat_id': 'N19_C10A2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Raising my free hand, I arch a '
                                                                          'canopy of warm Descender gold '
                                                                          'above both the Citlali beside '
                                                                          'me and the lonely girl standing '
                                                                          'in two-hundred-year-old rain.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N19_C10A2_R2',
                                                                  'speaker': 'Citlali',
                                                                  'text': "...You can't retroactively "
                                                                          'spoil a memory from a hundred '
                                                                          'and eighty years ago, dummy... '
                                                                          'Even if it does make the whole '
                                                                          'meadow stop shivering.',
                                                                  'inner_thought': 'Golden light right '
                                                                                   'where the cold rain '
                                                                                   "used to sit... Don't "
                                                                                   'look at me like that '
                                                                                   "or I'll lose my "
                                                                                   'concentration!',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                                                  'voice_emotion': 'vn_shy_blush'},
                                                                 {'beat_id': 'N19_C10A2_R3',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Fed by unhesitating warmth, the '
                                                                          'painted wildflowers brighten at '
                                                                          'our feet, pushing the white '
                                                                          'static back a dozen paces till '
                                                                          'dawn.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3a_02_huitzilin_wildflowers.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': []},
           'N20_A3': {'node_id': 'N20_A3',
                      'chapter_id': 'CH4',
                      'title': 'The White Surge Crossroads',
                      'day_label': 'Day 9 - Midnight Undertow',
                      'location': 'Deep Memory Core - The Golden-Rose Knot',
                      'beats': [{'beat_id': 'N20_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Day Nine passes in hushed preparation over hot ginger tea while '
                                         'rain drums relentlessly against the cliffside sanctuary.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B02',
                                 'speaker': 'Narrator',
                                 'text': 'When we descend on the ninth midnight into the deepest chamber '
                                         "of Citlali's soul-palette, the Night Kingdom seam below bucks "
                                         'like a wounded leviathan.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B03',
                                 'speaker': 'Narrator',
                                 'text': 'At the very center of her inner sky burns a breathtaking nexus '
                                         'of intertwined rose-lavender and radiant star-gold -- louder, '
                                         'warmer, and brighter than two centuries of solitude around it.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B04',
                                 'speaker': 'Aether',
                                 'text': 'Every thread at the core of your palette... Citlali, these are '
                                         'all our memories together -- Smoke-Drift Canyon, the Seven-Hued '
                                         'Ruins, the harbor lanterns, the key!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B05',
                                 'speaker': 'Citlali',
                                 'text': "Don't stare at them right now! Because they're the brightest "
                                         'living colors inside me, the torn scroll is locking straight '
                                         'onto that nexus!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B06',
                                 'speaker': 'Narrator',
                                 'text': 'Without warning, a towering wall of colorless static roars up '
                                         'from the lower abyss and lunges straight for our clasped hands!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B07',
                                 'speaker': 'Citlali',
                                 'text': "No -- it's tracing your gold mark back across our bridge! Let go "
                                         'of my hand right now, Aether!',
                                 'inner_thought': '[...please let go... I would rather forget everything '
                                                  'myself than watch my curse hollow out the one person '
                                                  'I--!]',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': 'outing_bump_rescue'},
                                {'beat_id': 'N20_B08',
                                 'speaker': 'Citlali',
                                 'text': 'If that Loom-of-Fate undertow crosses our link unhindered, it '
                                         'could tear holes straight through YOUR memories of your sister '
                                         "and your journey! Drop the link -- that's an order from Granny "
                                         'Itztli!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B09_F04',
                                 'speaker': 'Aether',
                                 'text': 'Under that lantern table on Day Three, I promised only one '
                                         "shaman holds my memory-color -- and I don't break promises when "
                                         'the wind turns cold!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F04_HAND_PROMISE_GIVEN']}},
                                {'beat_id': 'N20_B09_NOF04',
                                 'speaker': 'Aether',
                                 'text': 'If I drop your hand here, that white tide swallows every memory '
                                         'of us inside you in ten seconds flat!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'forbid_flags': ['F04_HAND_PROMISE_GIVEN']}},
                                {'beat_id': 'N20_B10',
                                 'speaker': 'Narrator',
                                 'text': "Tears of sheer terror flash silver at the corners of Citlali's "
                                         'eyes as white rime climbs both our forearms.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B11',
                                 'speaker': 'Narrator',
                                 'text': 'With all her remaining strength, she braces her heels and tries '
                                         'to wrench her freezing fingers out of my grip before the wave '
                                         'crests.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C11_A',
                                 'prompt': "White static surges at the golden-rose core of Citlali's "
                                           'memories as she begs you to let go:',
                                 'options': [{'opt_id': 'C11_A1_ETERNAL_HUE_VOW',
                                              'label': 'Interlace all ten fingers tighter and pour your '
                                                       'open Descender heart across the link, vowing to '
                                                       'carry her color across eternity.',
                                              'effects': {'bond': 2,
                                                          'insight': 1,
                                                          'add_flags': ['F09_ETERNAL_HUE_VOW']},
                                              'next_node': 'N21_A4',
                                              'reaction_beats': [{'beat_id': 'N20_C11A1_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Take every ounce of gold you '
                                                                          "need, Citlali! My memory isn't "
                                                                          "bound to Teyvat's Ley Lines -- "
                                                                          'whatever the Night-Wind drinks, '
                                                                          'I will reflect right back into '
                                                                          'your hands!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A1_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Striking an outlander soul '
                                                                          'unrecorded in Irminsul, the '
                                                                          'colorless wave shatters '
                                                                          'harmlessly into golden spray -- '
                                                                          'feeding double light straight '
                                                                          "back into Citlali's "
                                                                          'rose-lavender core!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A1_R3',
                                                                  'speaker': 'Citlali',
                                                                  'text': 'Aether--! ...You reckless, '
                                                                          'impossible outlander... Your '
                                                                          'heart is ringing so loudly '
                                                                          "inside my head I can't even "
                                                                          'hear the static anymore...',
                                                                  'inner_thought': "He didn't flinch. Not "
                                                                                   'a single corner of his '
                                                                                   'soul flinched away '
                                                                                   'from my two hundred '
                                                                                   'years...',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                                                  'voice_emotion': 'vn_tender_love'}]},
                                             {'opt_id': 'C11_A2_DESCENDER_FIREWALL',
                                              'when': {'min_insight': 6},
                                              'unlock_badge': '[Quarantine Protocol -- Severs Emotional '
                                                              'Link]',
                                              'lock_hint': '[LOCKED: Needs Insight 6 -- Clinical '
                                                           'Ley-Quarantine]',
                                              'label': '[Quarantine Protocol -- Severs Emotional Link] '
                                                       'Erect a cold, unfeeling Descender firewall between '
                                                       'your minds to block the static clinically.',
                                              'effects': {'bond': 0,
                                                          'insight': 2,
                                                          'add_flags': ['COLD_FIREWALL_NO_VOW']},
                                              'next_node': 'N21_A4',
                                              'reaction_beats': [{'beat_id': 'N20_C11A2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Compressing my outlander aura '
                                                                          'into a rigid, mirror-cold '
                                                                          'geometric slab, I slam an '
                                                                          'impermeable barrier directly '
                                                                          'across our shared telepathic '
                                                                          'channel -- halting the white '
                                                                          'surge dead in its tracks.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A2_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'The static stops instantly, yet '
                                                                          'on the far side of that '
                                                                          'clinical glass, the warm duet '
                                                                          'of our thoughts drops to a '
                                                                          'hollow silence.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A2_R3',
                                                                  'speaker': 'Citlali',
                                                                  'text': '...Oh. You walled your thoughts '
                                                                          'off completely. ...No, that was '
                                                                          'smart, Traveler. Keeping an '
                                                                          "elder's messy feelings behind "
                                                                          'glass is much safer for both of '
                                                                          'us.',
                                                                  'inner_thought': '[...muffled behind '
                                                                                   'cold glass: see, '
                                                                                   'Citlali? Even he had '
                                                                                   'to shut the door once '
                                                                                   'it got too close...]',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C11_A3_YIELD_TO_HER_PRIDE',
                                              'label': 'Trust her desperate warning as Great Shaman and '
                                                       'release her hand before the static crosses into '
                                                       'your mind.',
                                              'effects': {'bond': -1, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N30_BAD1_1',
                                              'reaction_beats': [{'beat_id': 'N20_C11A3_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'For one fatal fraction of a '
                                                                          'second, my grip loosens in '
                                                                          'obedience to her cry.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A3_R2',
                                                                  'speaker': 'Citlali',
                                                                  'text': 'Forgive me, Aether -- live '
                                                                          "brightly under next year's sun!",
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A3_R3',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Before I can lunge back, '
                                                                          'Citlali shoves my chest with a '
                                                                          'burst of lavender wind that '
                                                                          'hurls my consciousness straight '
                                                                          'out of her memory-space!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_01_whitesurge_crossroads_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': []},
           'N21_A4': {'node_id': 'N21_A4',
                      'chapter_id': 'CH4',
                      'title': 'Counter-Weaving on Night Ten',
                      'day_label': 'Day 10 - Eve of the New Moon',
                      'location': 'Deep Memory Core - Before the Obsidian Name-Core',
                      'beats': [{'beat_id': 'N21_B01',
                                 'speaker': 'Narrator',
                                 'text': "After sleeping away Day Ten's exhaustion side by side on the "
                                         "sanctuary rug under Citlalin's watchful plush gaze, we share "
                                         'quiet roast grainfruit at dusk.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B02',
                                 'speaker': 'Narrator',
                                 'text': 'When the tenth night falls -- twenty-four hours before the '
                                         'New-Moon Tide -- we descend one last time to the root of the '
                                         'First-Era warp.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B03',
                                 'speaker': 'Narrator',
                                 'text': "Suspended at the base of the scroll's inner loom floats the "
                                         "dormant Obsidian Name-Core of Citlali's Vision ancestor, wrapped "
                                         'in frayed seven-color threads.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B04',
                                 'speaker': 'Aether',
                                 'text': 'Look at the tension lines around that obsidian core. Every '
                                         'frayed strand is trying to pull living warmth inward just to '
                                         'stay intact until tomorrow midnight.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B05',
                                 'speaker': 'Citlali',
                                 'text': 'That core has slept inside the chronicle since before '
                                         "Huitzilin's era. Normally, waking an Ancient Name from inside a "
                                         "weave without Xilonen's forge would tear a lone shaman apart.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B06',
                                 'speaker': 'Citlali',
                                 'text': 'Yet if two synchronized minds re-seat the warp tonight using an '
                                         'inverted stellar knot, overhead night-phlogiston will carry the '
                                         'load instead of our pulses!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B07_F03',
                                 'speaker': 'Aether',
                                 'text': "Huitzilin's seven-knot 'Starlight Borrowing' pattern from your "
                                         'Six Kitsune bookmark...',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F03_SIX_KITSUNE_VERSE']}},
                                {'beat_id': 'N21_B07_NOF03',
                                 'speaker': 'Aether',
                                 'text': 'An inverted seven-knot pattern? I never saw the exact knot '
                                         'sequence written out...',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': '',
                                 'when': {'forbid_flags': ['F03_SIX_KITSUNE_VERSE']}},
                                {'beat_id': 'N21_B08',
                                 'speaker': 'Narrator',
                                 'text': 'Around the obsidian core, silver-violet loom threads hum louder, '
                                         'demanding either an exact seven-knot inversion or eight hours of '
                                         'brute elemental bracing.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B09',
                                 'speaker': 'Citlali',
                                 'text': 'Take the lead thread, Traveler -- my hands move wherever yours '
                                         'guide them tonight.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C12_A',
                                 'prompt': 'On the eve of the New Moon, the frayed Ukumbuko warp awaits a '
                                           'final weave pattern:',
                                 'options': [{'opt_id': 'C12_A1_UKUMBUKO_COUNTERWEAVE',
                                              'when': {'all_flags': ['F09_ETERNAL_HUE_VOW',
                                                                     'F03_SIX_KITSUNE_VERSE'],
                                                       'any_flags': ['F01_SEAL_FROST_READ',
                                                                     'F04_HAND_PROMISE_GIVEN',
                                                                     'F08_QUENEPA_CONFESSION',
                                                                     'WILDFLOWER_STAR_ANCHOR'],
                                                       'min_insight': 8},
                                              'unlock_badge': '[STARLIGHT BORROWING UNLOCKED]',
                                              'lock_hint': '[LOCKED: Needs Eternal Vow + Six Kitsune '
                                                           'Cipher + Seam/Heart Clue + Insight 8]',
                                              'label': "Weave Huitzilin's 'Starlight Borrowing' seven-knot "
                                                       'cipher from Six Kitsune across your open vow so '
                                                       'night phlogiston carries the tension!',
                                              'effects': {'bond': 3,
                                                          'insight': 1,
                                                          'add_flags': ['UKUMBUKO_WEAVE_PRIMED']},
                                              'next_node': 'N34_CH5_CONVERGE',
                                              'reaction_beats': [{'beat_id': 'N21_C12A1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Guided by the exact seven-knot '
                                                                          "inversion from Huitzilin's "
                                                                          'woven bookmark slip, our joined '
                                                                          'hands loop rose-lavender and '
                                                                          'Descender gold into a '
                                                                          'self-sustaining stellar '
                                                                          'lattice!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N21_C12A1_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Instantly, the crushing siphon '
                                                                          "lifts off Citlali's meridians "
                                                                          'as coastal starlight pours down '
                                                                          'through the sanctum transom to '
                                                                          "bear the scroll's weight.",
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N21_C12A1_R3',
                                                                  'speaker': 'Citlali',
                                                                  'text': "Huitzilin's Starlight Borrowing "
                                                                          "-- it's holding! For the first "
                                                                          'time in six nights, my '
                                                                          'fingertips are actually warm, '
                                                                          'Aether!',
                                                                  'inner_thought': 'Two synchronized minds '
                                                                                   'holding the warp as '
                                                                                   'one... Tomorrow '
                                                                                   'midnight, we finish '
                                                                                   'this together!',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                                                  'voice_emotion': 'vn_sweet_happy'}]},
                                             {'opt_id': 'C12_A2_RAW_GOLD_VIGIL',
                                              'label': 'Without the complete Starlight Borrowing '
                                                       'counter-cipher, brace the torn seam through sheer '
                                                       'raw golden stamina until tomorrow night.',
                                              'effects': {'bond': -3,
                                                          'insight': 1,
                                                          'add_flags': ['RAW_VIGIL_STRAIN']},
                                              'next_node': 'N34_CH5_CONVERGE',
                                              'reaction_beats': [{'beat_id': 'N21_C12A2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': "Lacking Huitzilin's inverted "
                                                                          'knot pattern to offload the '
                                                                          'draw, I clamp the frayed border '
                                                                          'with raw elemental force '
                                                                          'through eight grueling hours.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N21_C12A2_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'The scroll stabilizes before '
                                                                          "dawn, saving Citlali's life -- "
                                                                          'yet the unbuffered backlash '
                                                                          'scorches our shared telepathic '
                                                                          'bridge raw and numb with '
                                                                          'exhaustion.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N21_C12A2_R3',
                                                                  'speaker': 'Citlali',
                                                                  'text': '...Your hands are shaking from '
                                                                          'carrying my slack, Traveler. '
                                                                          'Keep a safe step back tomorrow '
                                                                          'night once the core stabilizes, '
                                                                          'alright?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4a_02_counterweave_diff.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': []},
           'N30_BAD1_1': {'node_id': 'N30_BAD1_1',
                          'chapter_id': 'CH4',
                          'title': 'Seven Barriers on the Study Door',
                          'day_label': 'Day 10 - Midnight',
                          'location': 'Sanctuary Study - Outside the Sealed Sanctum',
                          'beats': [{'beat_id': 'N30_B01',
                                     'speaker': 'Narrator',
                                     'text': "My back slams hard against Citlali's warded cedar bookshelf "
                                             'in the waking study, knocking two paperbacks onto the reed '
                                             'mat.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B02',
                                     'speaker': 'Narrator',
                                     'text': 'Before I can scramble upright, seven overlapping '
                                             'violet-white shamanic barriers snap shut across the inner '
                                             'Astral Loom doorway like guillotine blades of solid light.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B03',
                                     'speaker': 'Aether',
                                     'text': "Citlali! Open this ward right now -- don't feed that "
                                             'golden-rose knot into the scroll alone!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B04',
                                     'speaker': 'Paimon',
                                     'text': 'Citlali! Stop being stubborn and let us in! Paimon promises '
                                             'never to eat your honeyed cakes again -- please open the '
                                             'door!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B05',
                                     'speaker': 'Narrator',
                                     'text': 'I drive golden phlogiston against the seven-layered ward '
                                             'until my knuckles split, yet nothing dents the pinnacle '
                                             "defensive arts of Natlan's sole Great Shaman.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B06',
                                     'speaker': 'Narrator',
                                     'text': "Behind the translucent violet glass, Citlali's silhouette "
                                             'weaves furiously through the tenth and eleventh midnights -- '
                                             'feeding every luminous rose-gold thread of our shared days '
                                             'directly into the ancestral tear.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B07',
                                     'speaker': 'Narrator',
                                     'text': 'One by one, the warm echoes inside my skull flicker out like '
                                             'seaside lanterns in a gale: the promenade table, the woven '
                                             'bookmark, the spare key, Smoke-Drift Canyon.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B08',
                                     'speaker': 'Citlali',
                                     'text': '...',
                                     'inner_thought': "...thank you for the Inazuman books, Aether. Don't "
                                                      'knock too loudly when I forget why I gave you my '
                                                      'key...',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B09',
                                     'speaker': 'Narrator',
                                     'text': 'At the stroke of New-Moon Midnight, a soft snap severs the '
                                             'final gossamer strand between our minds -- followed by '
                                             'absolute silence.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B10',
                                     'speaker': 'Narrator',
                                     'text': 'When dawn of the twelfth day finally dissolves the seven '
                                             'barriers, the First-Era Ukumbuko Scroll hangs whole and '
                                             'radiant above the basin.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B11',
                                     'speaker': 'Narrator',
                                     'text': 'The inner chamber is empty, the terrace gate unlatched '
                                             'toward the sunny harbor below.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_01_sealed_door_diff.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [{'default': True, 'next_node': 'N31_BAD1_2'}]},
           'N31_BAD1_2': {'node_id': 'N31_BAD1_2',
                          'chapter_id': 'CH4',
                          'title': 'Stranger on Verona Shore',
                          'day_label': 'Day 12 - Bright Afternoon',
                          'location': 'Verona Beach Boardwalk - Wine Merchant Stall',
                          'beats': [{'beat_id': 'N31_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Under brilliant afternoon sun down on Verona Beach, gulls '
                                             'wheel lazily above turquoise surf.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B02',
                                     'speaker': 'Narrator',
                                     'text': "Standing at a coastal merchant's counter inspecting pale "
                                             'bottles of Quenepa Berry wine is Citlali -- color restored '
                                             'to her cheeks, frost gone from her steady fingers, '
                                             'completely whole.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B03',
                                     'speaker': 'Aether',
                                     'text': '...Citlali.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B04',
                                     'speaker': 'Narrator',
                                     'text': 'She turns at the sound of her name. Her rose-gold eyes meet '
                                             'mine without a flicker of blush, annoyance, or recognition.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B05',
                                     'speaker': 'Narrator',
                                     'text': 'Only the cool, guarded distance of two-hundred-year-old '
                                             'Granny Itztli looks back at an unfamiliar outlander.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B06',
                                     'speaker': 'Citlali',
                                     'text': 'Can I help you, outlander? If you came seeking a divination '
                                             'from Granny Itztli, take a number with the tribal elders -- '
                                             "I don't take walk-in petitions on the beach.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                     'voice_emotion': 'greet_doorstep'},
                                    {'beat_id': 'N31_B07',
                                     'speaker': 'Narrator',
                                     'text': 'Inside my skull, where her flustered voice once argued over '
                                             'braids, cabbages, and holding hands, stretches a soundless, '
                                             'unanswering void.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                     'voice_emotion': ''}],
                          'choice': {'choice_id': 'C19_BAD1',
                                     'prompt': 'Citlali waits with polite, unrecognizing eyes beside the '
                                               'sunlit surf:',
                                     'options': [{'opt_id': 'C19_A_RETURN_HOUSE_KEY',
                                                  'label': 'Set her brass-and-obsidian house key quietly '
                                                           'on the counter beside her wine bottle, telling '
                                                           'her she dropped it.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD1_KEY_RETURNED']},
                                                  'next_node': 'END_BAD_1',
                                                  'reaction_beats': [{'beat_id': 'N31_C19A_R1',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'Metal clicks softly against '
                                                                              'sun-bleached cedar as I '
                                                                              'place her spare sanctuary '
                                                                              'key beside her Quenepa jar.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N31_C19A_R2',
                                                                      'speaker': 'Citlali',
                                                                      'text': 'Huh? My sanctuary '
                                                                              'ward-key...? Strange -- I '
                                                                              'never carry a spare down to '
                                                                              'the market, yet it bears my '
                                                                              'own seal.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N31_C19A_R3',
                                                                      'speaker': 'Citlali',
                                                                      'text': '...Well, thank you for '
                                                                              'returning it, Traveler. '
                                                                              'Leaving something like this '
                                                                              "in a stranger's pocket "
                                                                              'would have given me no end '
                                                                              'of trouble.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N31_C19A_R4',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'She tucks the key into her '
                                                                              'sash and walks up the cliff '
                                                                              'steps alone -- leaving me '
                                                                              'under bright coastal sun, '
                                                                              'the sole witness still '
                                                                              'carrying her rose-lavender '
                                                                              'color in a silent mind.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                                                      'voice_emotion': ''}]},
                                                 {'opt_id': 'C19_B_SEND_SILENT_THOUGHT',
                                                  'label': 'Keep the key over your heart, smile politely '
                                                           "so you don't trouble her, and send one last "
                                                           'silent greeting down the dead link.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD1_SILENT_THOUGHT']},
                                                  'next_node': 'END_BAD_1',
                                                  'reaction_beats': [{'beat_id': 'N31_C19B_R1',
                                                                      'speaker': 'Aether',
                                                                      'text': 'My mistake, Great Shaman. '
                                                                              'Enjoy the vintage -- last '
                                                                              "harvest's Quenepa goes well "
                                                                              'with quiet afternoons.',
                                                                      'inner_thought': 'Sleep in as late '
                                                                                       'as you want from '
                                                                                       'now on, Citlali. '
                                                                                       "I'll remember both "
                                                                                       'halves for us.',
                                                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N31_C19B_R2',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'My mental words go out into '
                                                                              'empty air and return no '
                                                                              'echo at all.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N31_C19B_R3',
                                                                      'speaker': 'Citlali',
                                                                      'text': '...Odd fellow. Why did my '
                                                                              'chest sting just looking at '
                                                                              'that golden scarf? Must '
                                                                              'have stayed up reading too '
                                                                              'late last night.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N31_C19B_R4',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'As her footsteps fade up '
                                                                              'the graffitied steps toward '
                                                                              'two uncracked novels whose '
                                                                              'giver she will never '
                                                                              'recall, the tide washes our '
                                                                              'footprints smooth into '
                                                                              'white sand.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad1_02_stranger_shore.jpg',
                                                                      'voice_emotion': ''}]}]},
                          'routing': []},
           'N22_B1': {'node_id': 'N22_B1',
                      'chapter_id': 'CH3',
                      'title': 'Wings Over the Seven-Hued Gorge',
                      'day_label': 'Day 7 - Noon Dive',
                      'location': "Seven-Hued Ruins Chasm - Chasca's Gun-Frame",
                      'beats': [{'beat_id': 'N22_B01',
                                 'speaker': 'Narrator',
                                 'text': 'After snatching four hours of dawn sleep while Paimon barricades '
                                         "Citlali's tea table with cushions and warm soup, Ororon and I "
                                         'ride north at full gallop.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B02',
                                 'speaker': 'Narrator',
                                 'text': 'High above the mist-choked sinkhole beneath the Seven-Hued '
                                         'Ruins, Flower-Feather peacemaker Chasca banks her giant airborne '
                                         'gun-frame alongside the cliff lip.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B03',
                                 'speaker': 'Chasca',
                                 'text': 'Right on time, Tumaini. Hold tight to the saddle-rail, both of '
                                         'you -- Rifthounds have been circling this lower gorge since '
                                         'daybreak.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B04',
                                 'speaker': 'Chasca',
                                 'text': "Whatever broke loose beneath Huitzilin's old dye-chambers smells "
                                         'like prime memory-carrion to Abyssal scavengers.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B05_F05',
                                 'speaker': 'Ororon',
                                 'text': 'My spirit-compass is locking straight onto the chalk-white '
                                         'static frequency we sampled off those garden aphids, Gramps -- '
                                         'three strata below the old maze floor!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F05_APHID_LOOM_TRACE']}},
                                {'beat_id': 'N22_B05_NOF05',
                                 'speaker': 'Ororon',
                                 'text': 'Even without a pre-tuned sample, I can feel cold colourless air '
                                         'whistling up from three strata below the old maze floor, Gramps!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': '',
                                 'when': {'forbid_flags': ['F05_APHID_LOOM_TRACE']}},
                                {'beat_id': 'N22_B06',
                                 'speaker': 'Narrator',
                                 'text': 'Wind howls past our cloaks as Chasca noses the heavy Phlogiston '
                                         'frame into a steep spiral descent, blasting two lunging '
                                         'Rifthound whelps off the cliff wall with crisp Anemo shells.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B07',
                                 'speaker': 'Narrator',
                                 'text': 'Halfway down the vertical drop, a furious, unmistakable voice '
                                         'crackles across our long-distance telepathic link from Verona '
                                         'Cove.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B08',
                                 'speaker': 'Citlali',
                                 'text': '...',
                                 'inner_thought': 'Aether, you sneaky reckless idiot! Did you put Paimon '
                                                  'on tea-guard duty while you dragged Ororon into an '
                                                  'unmapped chasm?!',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B09',
                                 'speaker': 'Aether',
                                 'text': 'Stay tucked under that quilt, Granny Itztli -- Chasca has the '
                                         "air clear, and we're bringing back the lower counterweight "
                                         'before Night Eleven!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B10',
                                 'speaker': 'Citlali',
                                 'text': '...',
                                 'inner_thought': "Don't 'Granny Itztli' me over a hundred-mile soul-link! "
                                                  'If a single Rifthound claw scratches you, see who '
                                                  'patches your coat!',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B11',
                                 'speaker': 'Ororon',
                                 'text': 'Judging by the way Gramps is smiling at nothing, Granny just '
                                         'woke up from her nap.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B12',
                                 'speaker': 'Chasca',
                                 'text': 'Landing ledge dead ahead -- brace your boots and keep blades '
                                         'out!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_01_chasca_ororon_canyon.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N23_B2'}]},
           'N23_B2': {'node_id': 'N23_B2',
                      'chapter_id': 'CH3',
                      'title': "Huitzilin's False Mural",
                      'day_label': 'Day 8 - Subterranean Camp & Vault',
                      'location': 'Seven-Hued Sub-Stratum - Solidified Dye Gallery',
                      'beats': [{'beat_id': 'N23_B01',
                                 'speaker': 'Narrator',
                                 'text': 'We camp overnight on a glowing blue-mushroom ledge, sharing '
                                         "Ororon's roasted grainfruit rations while Chasca holds the upper "
                                         'skylight clear against circling Abyss hounds.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B02',
                                 'speaker': 'Narrator',
                                 'text': 'At noon of Day Eight, Ororon and I breach a sealed First-Era '
                                         'gallery below the Seven-Hued maze where walls of solidified '
                                         'memory-dye twist like frozen rainbows.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B03',
                                 'speaker': 'Ororon',
                                 'text': 'Careful where you step, Gramps. Huitzilin built optical traps '
                                         "down here to hide the Night-Wind's auxiliary loom hardware "
                                         'during the cataclysm.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B04',
                                 'speaker': 'Narrator',
                                 'text': 'Half-buried inside a cracked mural socket at the center of the '
                                         'arch glints an unbleached First-Era Opal Spindle -- the lost '
                                         "lower counterweight to Citlali's sanctuary scroll!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B05',
                                 'speaker': 'Aether',
                                 'text': 'Look at the fracture around that spindle socket -- when the '
                                         'Loom-of-Fate shockwave hit up north, this counterweight slipped '
                                         "out of alignment and turned Citlali's scroll into a siphon!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B06',
                                 'speaker': 'Narrator',
                                 'text': 'Before I can cross the flagstones, a translucent lavender astral '
                                         'projection of Citlali shimmers into view beside the arch -- sent '
                                         "down her sanctuary's Wayob line to scout ahead of us!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B07',
                                 'speaker': 'Citlali',
                                 'text': '...',
                                 'inner_thought': "[...don't touch the left plinth, Aether, it's rigged "
                                                  'with a counter-seal-- ack, the ceiling masonry is '
                                                  'shearing--!]',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B08',
                                 'speaker': 'Narrator',
                                 'text': "Though Citlali's astral form is intangible to falling stone, the "
                                         'collapsing ward-ring violently twists her mental tether -- '
                                         'threatening to whiplash her waking spirit!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B09',
                                 'speaker': 'Ororon',
                                 'text': 'Gramps, the mural arch is coming down in three seconds!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B10',
                                 'speaker': 'Ororon',
                                 'text': 'Either you pry that Opal Spindle free right now before the '
                                         "rubble seals it, or you catch Granny's astral tether with your "
                                         'gold light before the recoil slams into her chest!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C13_B',
                                 'prompt': "The seven-color mural socket is crumbling beside Citlali's "
                                           'wavering intangible projection:',
                                 'options': [{'opt_id': 'C13_B1_CLAIM_OPAL_SPINDLE',
                                              'label': "Vault to the mural socket and pry Huitzilin's "
                                                       'unbleached Opal Spindle free before the stone '
                                                       'seals over it!',
                                              'effects': {'bond': 0,
                                                          'insight': 2,
                                                          'add_flags': ['F10_OPAL_SPINDLE_THREAD']},
                                              'next_node': 'N24A_B3',
                                              'reaction_beats': [{'beat_id': 'N23_C13B1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Driving my dull blade into the '
                                                                          'fissure, I wrench the ancient '
                                                                          'Opal Spindle intact into my '
                                                                          'hand a heartbeat before tons of '
                                                                          'bleached masonry bury the '
                                                                          'alcove!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N23_C13B1_R2',
                                                                  'speaker': 'Citlali',
                                                                  'text': '...',
                                                                  'inner_thought': '[...ngh--! Rough '
                                                                                   'landing on my end, '
                                                                                   "dummy, don't fret -- "
                                                                                   'just hold onto that '
                                                                                   'spindle tight!]',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N23_C13B1_R3',
                                                                  'speaker': 'Ororon',
                                                                  'text': 'Clean grab, Gramps! That '
                                                                          'First-Era opal still holds all '
                                                                          'seven ancestral hues!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C13_B2_STEADY_PROJECTION_LINK',
                                              'label': "Let the stone bury the socket and clasp Citlali's "
                                                       'wavering astral tether with warm golden light to '
                                                       'cushion the recoil on her heart!',
                                              'effects': {'bond': 2,
                                                          'insight': 0,
                                                          'add_flags': ['PROJECTION_STEADIED']},
                                              'next_node': 'N24A_B3',
                                              'reaction_beats': [{'beat_id': 'N23_C13B2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Ignoring the falling rubble '
                                                                          'over the mural socket, I wrap '
                                                                          "both hands around Citlali's "
                                                                          'intangible lavender tether and '
                                                                          'absorb the ward-snap harmlessly '
                                                                          'into my golden aura.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N23_C13B2_R2',
                                                                  'speaker': 'Citlali',
                                                                  'text': '...',
                                                                  'inner_thought': '[...you caught my '
                                                                                   'projection instead of '
                                                                                   'the artifact... idiot, '
                                                                                   'even intangible I felt '
                                                                                   'how warm your hands '
                                                                                   'were...]',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                                                  'voice_emotion': 'vn_shy_blush'},
                                                                 {'beat_id': 'N23_C13B2_R3',
                                                                  'speaker': 'Ororon',
                                                                  'text': 'The stone sealed the spindle, '
                                                                          'Gramps -- wait! My tuning fork '
                                                                          'caught the harmonic imprint off '
                                                                          "Granny's steadied tether!",
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3b_02_seven_hued_mural.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': []},
           'N24A_B3': {'node_id': 'N24A_B3',
                       'chapter_id': 'CH4',
                       'title': 'Through the Wayob Conduit',
                       'day_label': 'Day 9 - Deep Monochrome Vault',
                       'location': 'Seven-Hued Core - Inverted Loom Basin',
                       'beats': [{'beat_id': 'N24A_B01',
                                  'speaker': 'Narrator',
                                  'text': 'After bandaging scraped knuckles over a second brief rest-camp '
                                          'and descending the final spiral stair on Day Nine, Ororon and I '
                                          'step onto the floor of the deepest sub-basin.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B02',
                                  'speaker': 'Narrator',
                                  'text': 'Here at the root of the chromatic siphon, every mineral vein '
                                          "has been bleached to eerie monochrome -- even Ororon's Electro "
                                          'sparks crackle pale chalk-grey.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B03',
                                  'speaker': 'Aether',
                                  'text': 'The air down here feels like standing inside an unpainted '
                                          'canvas.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B04',
                                  'speaker': 'Narrator',
                                  'text': 'Suddenly, the ancient Wayob Ley-Conduit carved into the rear '
                                          "wall flares violet! High up the shaft, Paimon's panicked voice "
                                          "echoes faintly down Chasca's lowered rope-line --",
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B05',
                                  'speaker': 'Paimon',
                                  'text': 'Aetheeer! Paimon looked away for two seconds to stir the soup '
                                          "and Citlali stepped straight through her sanctum's Wayob ring!",
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B06',
                                  'speaker': 'Narrator',
                                  'text': 'Out of the violet portal stumbles Citlali in the flesh -- '
                                          'wrapped in her shawl, clutching Itzpapa to her ribs, breathing '
                                          'hard against the draining cold!',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B07',
                                  'speaker': 'Aether',
                                  'text': 'Citlali?! Why on earth did you cross the conduit physically in '
                                          'your condition?!',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B08',
                                  'speaker': 'Citlali',
                                  'text': "Because I finally deciphered Huitzilin's bottom margin note "
                                          'back home, you reckless pair!',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B09',
                                  'speaker': 'Citlali',
                                  'text': "This chamber isn't just a counterweight vault -- it's an "
                                          'emergency Seven-Hued Quarantine Sphere! On Night Ten, it seals '
                                          'corrupted weaves permanently from the INSIDE!',
                                  'inner_thought': "[...static screaming... my knees won't hold... I "
                                                   "couldn't let that sphere lock him down here without "
                                                   'me...!]',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': 'outing_bump_rescue'},
                                 {'beat_id': 'N24A_B10',
                                  'speaker': 'Ororon',
                                  'text': 'Granny, watch out -- frost on the step!',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B11',
                                  'speaker': 'Narrator',
                                  'text': 'Her boots slip on rime-slick obsidian, and I lunge forward to '
                                          'catch her shivering physical weight squarely against my chest.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B12',
                                  'speaker': 'Citlali',
                                  'text': "D-Don't scold me... If this vault closes without a seven-color "
                                          'prism refraction, whoever stands inside becomes the living plug '
                                          'for the Night Kingdom leak forever...',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B13',
                                  'speaker': 'Narrator',
                                  'text': 'Right on cue, white frost crawls across the Wayob ring behind '
                                          'us, sealing our return portal solid!',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''}],
                       'choice': None,
                       'routing': [{'default': True, 'next_node': 'N24B_B4'}]},
           'N24B_B4': {'node_id': 'N24B_B4',
                       'chapter_id': 'CH4',
                       'title': 'Spirit-Tuning in Monochrome',
                       'day_label': 'Day 9 - Late Night',
                       'location': 'Seven-Hued Core - Rising Quarantine Mist',
                       'beats': [{'beat_id': 'N24B_B01',
                                  'speaker': 'Ororon',
                                  'text': 'Gramps, the Wayob conduit behind us is frozen solid -- and '
                                          "Chasca's rope-shaft overhead is narrowing fast as the "
                                          'quarantine dome wakes up!',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B02',
                                  'speaker': 'Narrator',
                                  'text': 'High above the narrowing ceiling aperture, Chasca fires '
                                          'wind-anchors into the stone rim to hold an escape gap open as '
                                          'long as humanly possible.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B03',
                                  'speaker': 'Chasca',
                                  'text': "My Anemo cables won't hold this stone iris past midnight "
                                          "tomorrow! Whatever prism trick breaks Huitzilin's lock, line it "
                                          'up now!',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B04',
                                  'speaker': 'Narrator',
                                  'text': 'In my arms, Citlali shivers against the rising monochrome mist, '
                                          'every third word of her telepathy dropping into hollow white '
                                          'hiss.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B05',
                                  'speaker': 'Citlali',
                                  'text': '...need the exact focal point above the basin... otherwise even '
                                          'an Opal Spindle scatters harmlessly off the dome...',
                                  'inner_thought': '[...hold me tighter, Aether... the grey mist is '
                                                   'blurring the edges of the lantern stall...]',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B06',
                                  'speaker': 'Ororon',
                                  'text': "I've got my Night-Wind spirit-tuning fork ready, Gramps! Do we "
                                          "map the basin's acoustic node first, or stabilize Granny's "
                                          'color-link?!',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B07',
                                  'speaker': 'Narrator',
                                  'text': 'Pale mist curls ankle-deep across the obsidian floor, drinking '
                                          'warmth and hue from every stone.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B08',
                                  'speaker': 'Narrator',
                                  'text': 'Only the golden pulse in my palm and the rose-lavender thread '
                                          "around Citlali's heart still cast color in the dark.",
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                  'voice_emotion': ''}],
                       'choice': {'choice_id': 'C14_B',
                                  'prompt': 'White quarantine mist climbs the vault walls as Day Ten '
                                            'approaches:',
                                  'options': [{'opt_id': 'C14_B1_TUNE_ORORON_HARMONIC',
                                               'label': "Direct Ororon's Night-Wind spirit-tuning fork "
                                                        'onto the basin rim to map the exact seven-color '
                                                        'refraction node.',
                                               'effects': {'bond': 0,
                                                           'insight': 2,
                                                           'add_flags': ['ORORON_HARMONIC_TUNED']},
                                               'next_node': 'N25_B5_GATE1',
                                               'reaction_beats': [{'beat_id': 'N24B_C14B1_R1',
                                                                   'speaker': 'Narrator',
                                                                   'text': 'Striking his bronze '
                                                                           'spirit-tuning fork against the '
                                                                           'obsidian rim at my mark, '
                                                                           'Ororon sends a crisp violet '
                                                                           'ripple ringing across the '
                                                                           'monochrome dome.',
                                                                   'inner_thought': '',
                                                                   'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                                                   'voice_emotion': ''},
                                                                  {'beat_id': 'N24B_C14B1_R2',
                                                                   'speaker': 'Ororon',
                                                                   'text': 'Got the harmonic locked! Every '
                                                                           'echo off the vault walls is '
                                                                           'converging on one focal point '
                                                                           'six feet above the central '
                                                                           'basin!',
                                                                   'inner_thought': '',
                                                                   'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                                                   'voice_emotion': ''},
                                                                  {'beat_id': 'N24B_C14B1_R3',
                                                                   'speaker': 'Aether',
                                                                   'text': 'Mark that focal point with '
                                                                           'phlogiston chalk -- when '
                                                                           'midnight hits, we strike right '
                                                                           'there!',
                                                                   'inner_thought': '',
                                                                   'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                                                   'voice_emotion': ''}]},
                                              {'opt_id': 'C14_B2_WHISPER_ACROSS_STATIC',
                                               'label': "Press your forehead to Citlali's and speak every "
                                                        'shared coastal memory aloud so her eyes stay '
                                                        'anchored on your gold.',
                                               'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                               'next_node': 'N25_B5_GATE1',
                                               'reaction_beats': [{'beat_id': 'N24B_C14B2_R1',
                                                                   'speaker': 'Aether',
                                                                   'text': 'Listen to my voice, Citlali -- '
                                                                           'warm flatbreads on Day One, '
                                                                           'cedar wedges under your '
                                                                           'bookcase, chili skewers by the '
                                                                           'surf, your hand under the '
                                                                           'lantern table.',
                                                                   'inner_thought': '',
                                                                   'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                                                   'voice_emotion': ''},
                                                                  {'beat_id': 'N24B_C14B2_R2',
                                                                   'speaker': 'Citlali',
                                                                   'text': '...Uncracked Inazuma books... '
                                                                           "Huitzilin's little "
                                                                           'wildflower... Keep talking, '
                                                                           'Aether, I can still see your '
                                                                           'gold clearly...',
                                                                   'inner_thought': 'Even in monochrome '
                                                                                    'stone, his voice puts '
                                                                                    'every single color of '
                                                                                    'me back together...',
                                                                   'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                                                   'voice_emotion': 'vn_tender_love'},
                                                                  {'beat_id': 'N24B_C14B2_R3',
                                                                   'speaker': 'Narrator',
                                                                   'text': 'Steadied against my '
                                                                           "collarbone, Citlali's pulse "
                                                                           'regains a clear rose-lavender '
                                                                           'glow as the tenth midnight '
                                                                           'approaches.',
                                                                   'inner_thought': '',
                                                                   'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                                                   'voice_emotion': ''}]}]},
                       'routing': []},
           'N25_B5_GATE1': {'node_id': 'N25_B5_GATE1',
                            'chapter_id': 'CH4',
                            'title': 'The Inverted White Horizon',
                            'day_label': 'Day 10 - Midnight',
                            'location': 'Seven-Hued Core - Quarantine Sphere Aperture',
                            'pre_events': [{'when': {'forbid_flags': ['F10_OPAL_SPINDLE_THREAD'],
                                                     'all_flags': ['PROJECTION_STEADIED',
                                                                   'ORORON_HARMONIC_TUNED'],
                                                     'min_count_in': {'count': 3,
                                                                      'pool': ['F01_SEAL_FROST_READ',
                                                                               'F03_SIX_KITSUNE_VERSE',
                                                                               'F05_APHID_LOOM_TRACE',
                                                                               'F08_QUENEPA_CONFESSION',
                                                                               'PIGMENT_DRAIN_TIMED']},
                                                     'min_insight': 11},
                                            'effects': {'add_flags': ['F10_OPAL_SPINDLE_THREAD',
                                                                      'F10_HARMONIC_RECOVERED']}}],
                            'beats': [{'beat_id': 'N25_B01',
                                       'speaker': 'Narrator',
                                       'text': "At the first stroke of Day Ten's midnight, the stone vault "
                                               'ceiling vanishes into a blinding Inverted White Horizon!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_B02',
                                       'speaker': 'Narrator',
                                       'text': "Huitzilin's three-century-old quarantine sphere descends "
                                               'like an avalanche of silent snow, contracting toward the '
                                               'basin to seal the corrupted weave for eternity.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_B03_RECOV',
                                       'speaker': 'Ororon',
                                       'text': 'Gramps, catch! Combining your three seam diagnostics with '
                                               "Granny's steadied projection tether, my tuning fork just "
                                               'crystallized a harmonic Opal Spindle out of pure '
                                               'phlogiston!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': '',
                                       'when': {'all_flags': ['F10_HARMONIC_RECOVERED']}},
                                      {'beat_id': 'N25_B03_ORIG',
                                       'speaker': 'Narrator',
                                       'text': "At my belt, Huitzilin's recovered First-Era Opal Spindle "
                                               'vibrates like a struck bell against the descending white '
                                               'dome.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': '',
                                       'when': {'all_flags': ['F10_OPAL_SPINDLE_THREAD'],
                                                'forbid_flags': ['F10_HARMONIC_RECOVERED']}},
                                      {'beat_id': 'N25_B03_NONE',
                                       'speaker': 'Narrator',
                                       'text': 'Without an Opal Spindle in hand, the empty focal point '
                                               'above the basin drinks my raw golden sparks without '
                                               'refracting a single hue!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': '',
                                       'when': {'forbid_flags': ['F10_OPAL_SPINDLE_THREAD']}},
                                      {'beat_id': 'N25_B04',
                                       'speaker': 'Citlali',
                                       'text': 'To cleave a Seven-Hued quarantine seal, you have to thread '
                                               'a living personal dye-token through an Opal Spindle at the '
                                               'exact chromatic angle!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_B05',
                                       'speaker': 'Chasca',
                                       'text': 'Cables snapping up here, Traveler -- the stone iris is '
                                               'down to four feet!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_B06',
                                       'speaker': 'Ororon',
                                       'text': "I'm bracing the outer lip with Electro -- you and Granny "
                                               'have three heartbeats before the white dome locks from '
                                               'within!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_B07',
                                       'speaker': 'Narrator',
                                       'text': "Citlali's cold fingers tighten around my sleeve as "
                                               'blinding colorless light presses down to our shoulders.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_B08',
                                       'speaker': 'Aether',
                                       'text': 'Hold onto me, Citlali -- now or never!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                       'voice_emotion': ''}],
                            'choice': {'choice_id': 'C15_B_GATE1',
                                       'exclusive_rescue_gate': True,
                                       'prompt': 'The Inverted White Horizon closes overhead around '
                                                 'Citlali and you:',
                                       'options': [{'opt_id': 'C15_B_PRISM_KEY_UNLOCK',
                                                    'when': {'all_flags': ['F07_ROSE_HANDKERCHIEF',
                                                                           'F10_OPAL_SPINDLE_THREAD'],
                                                             'any_flags': ['F03_SIX_KITSUNE_VERSE',
                                                                           'F05_APHID_LOOM_TRACE',
                                                                           'F08_QUENEPA_CONFESSION',
                                                                           'SPECTRUM_GLITCH_SEEN'],
                                                             'min_insight': 10},
                                                    'unlock_badge': '[COMBINATION GATE #1 -- SEVEN-COLOR '
                                                                    'PRISM KEY]',
                                                    'lock_hint': '[LOCKED: Needs Rose Handkerchief + Opal '
                                                                 'Spindle + Chromatic Clue + Insight 10]',
                                                    'label': "Thread Citlali's rose-lavender handkerchief "
                                                             'through the Opal Spindle to refract your '
                                                             'Descender gold into seven blazing hues and '
                                                             'cleave the white dome!',
                                                    'effects': {'bond': 2,
                                                                'insight': 1,
                                                                'add_flags': ['COMBO1_CLEARED']},
                                                    'next_node': 'N34_CH5_CONVERGE',
                                                    'reaction_beats': [{'beat_id': 'N25_C15_OK_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Wrapping her '
                                                                                'rose-lavender silk tight '
                                                                                'around the Opal Spindle '
                                                                                'at the exact refraction '
                                                                                'angle we mapped, I drive '
                                                                                'golden phlogiston '
                                                                                'straight through the '
                                                                                'crystal core!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_02_prism_gate_diff.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N25_C15_OK_R2',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Seven dazzling tribal '
                                                                                'hues erupt across the '
                                                                                'monochrome abyss -- '
                                                                                'shattering the white '
                                                                                'quarantine dome like '
                                                                                'sugar-glass and '
                                                                                'realigning the lower '
                                                                                'counterweight in a single '
                                                                                'chord!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_02_prism_gate_diff.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N25_C15_OK_R3',
                                                                        'speaker': 'Citlali',
                                                                        'text': 'My handkerchief and '
                                                                                "Huitzilin's spindle -- "
                                                                                'you turned them into a '
                                                                                'living prism! Look, the '
                                                                                'siphon back toward my '
                                                                                'sanctuary just reversed!',
                                                                        'inner_thought': 'Magnificent... '
                                                                                         'Only my golden '
                                                                                         'Traveler could '
                                                                                         'paint seven '
                                                                                         'colors straight '
                                                                                         'through solid '
                                                                                         'stone!',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_02_prism_gate_diff.jpg',
                                                                        'voice_emotion': 'vn_sweet_happy'},
                                                                       {'beat_id': 'N25_C15_OK_R4',
                                                                        'speaker': 'Narrator',
                                                                        'text': "Catching Chasca's "
                                                                                'wind-line with Ororon '
                                                                                'cheering beside us, we '
                                                                                'rocket up into the clear '
                                                                                'night air toward tomorrow '
                                                                                "midnight's final "
                                                                                'threshold!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_02_prism_gate_diff.jpg',
                                                                        'voice_emotion': ''}]},
                                                   {'opt_id': 'C15_B_BLIND_DIVE_WHITEOUT',
                                                    'label': 'Without the complete Seven-Color Prism Key, '
                                                             'shield Citlali in your arms and lunge '
                                                             'bare-handed toward the closing aperture!',
                                                    'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                    'next_node': 'N32_BAD2_1',
                                                    'reaction_beats': [{'beat_id': 'N25_C15_FAIL_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'With only seconds left '
                                                                                'and one gap narrow enough '
                                                                                'for a single person, I '
                                                                                'shove Ororon clear '
                                                                                "through Chasca's "
                                                                                'wind-ring so the boy '
                                                                                'survives!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N25_C15_FAIL_R2',
                                                                        'speaker': 'Ororon',
                                                                        'text': 'GRAMPS! GRANNY -- NO!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N25_C15_FAIL_R3',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Pulling Citlali tight '
                                                                                'against my chest to '
                                                                                'shield her from the '
                                                                                'crush, I watch the stone '
                                                                                'iris and white horizon '
                                                                                'slam shut above our '
                                                                                'heads!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                                                        'voice_emotion': ''}]}]},
                            'routing': []},
           'N32_BAD2_1': {'node_id': 'N32_BAD2_1',
                          'chapter_id': 'CH4',
                          'title': 'The Sealed Quarantine Sphere',
                          'day_label': 'Timeless Twilight',
                          'location': 'Inside the Seventh Hue - Painted Sanctuary',
                          'beats': [{'beat_id': 'N32_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Blinding white silence swallows the stone vault, weightless '
                                             'and painless as deep snow.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B02',
                                     'speaker': 'Narrator',
                                     'text': "By locking onto both Citlali's Great Shaman weave and my "
                                             "boundless Descender phlogiston inside its core, Huitzilin's "
                                             'quarantine sphere plugs the Night Kingdom leak permanently.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B03',
                                     'speaker': 'Narrator',
                                     'text': 'Three hundred years of Masters of the Night-Wind souls up in '
                                             'the sanctuary scroll are saved -- bought with two living '
                                             'anchors.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/ch4b_01_monochrome_vault_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B04',
                                     'speaker': 'Narrator',
                                     'text': 'When my eyes open again, the cold monochrome stone is gone.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B05',
                                     'speaker': 'Narrator',
                                     'text': 'Warm rose-lavender twilight fills an exact, brush-stroked '
                                             "replica of Citlali's cliffside bookshelf study -- cushions, "
                                             'astrolabe, Itzpapa, Citlalin, and rows of Inazuman novels '
                                             'intact to the last detail.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B06',
                                     'speaker': 'Narrator',
                                     'text': 'Yet across the cedar windowpane, painted silver raindrops '
                                             'hang motionless in mid-air.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B07',
                                     'speaker': 'Aether',
                                     'text': "...No tide sound. Even the candle flame isn't flickering.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B08',
                                     'speaker': 'Narrator',
                                     'text': "Inside my mind, Citlali's telepathic presence rings clearer "
                                             'and warmer than bell-glass; not a single shared memory has '
                                             'faded.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B09',
                                     'speaker': 'Narrator',
                                     'text': 'Yet when I touch the front latch, the brass handle is '
                                             'painted seamlessly into immutable canvas.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B10',
                                     'speaker': 'Narrator',
                                     'text': 'Beyond that painted window lies no Verona surf, no rising '
                                             'stars, and no road back to Teyvat.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B11',
                                     'speaker': 'Narrator',
                                     'text': 'Across the woven rug, Citlali rises slowly to her knees, '
                                             'staring at my golden scarf as the truth of our survival '
                                             'sinks in.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [{'default': True, 'next_node': 'N32B_BAD2_2'}]},
           'N32B_BAD2_2': {'node_id': 'N32B_BAD2_2',
                           'chapter_id': 'CH4',
                           'title': 'Prisoners of the Seventh Hue',
                           'day_label': 'Eternal Dusk',
                           'location': 'Painted Sanctuary & Waking Vault Stone',
                           'beats': [{'beat_id': 'N32B_B01',
                                      'speaker': 'Narrator',
                                      'text': 'Far outside in the waking Seven-Hued chamber, Ororon, '
                                              'Chasca, and a tearful Paimon lay fresh mountain wildflowers '
                                              'beside two unmoving, hand-clasped sleepers resting '
                                              'peacefully on obsidian stone.',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_B02',
                                      'speaker': 'Narrator',
                                      'text': 'Breathing softly in unbroken stasis while seasons turn '
                                              'overhead, neither sleeper wakes -- because their souls now '
                                              'inhabit the seventh hue within.',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_B03',
                                      'speaker': 'Citlali',
                                      'text': 'Why did you shove Ororon out instead of yourself, you '
                                              'monumental fool?!',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_B04',
                                      'speaker': 'Citlali',
                                      'text': 'Do you understand what you just traded?! You were meant to '
                                              'cross countless worlds -- not spend eternity locked inside '
                                              'a painted room with a selfish two-hundred-year-old recluse!',
                                      'inner_thought': "Why isn't he regretting it?! Stop smiling at me "
                                                       "while I'm crying -- how can I scold you when you "
                                                       'chose me over the whole sky?!',
                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_B05',
                                      'speaker': 'Narrator',
                                      'text': 'She catches both lapels of my tunic, hot tears spilling '
                                              'down onto my knuckles as her forehead drops against my '
                                              'chest.',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_B06',
                                      'speaker': 'Aether',
                                      'text': 'Ororon made it out alive, three centuries of Night-Wind '
                                              "dead are safe, and for once Granny Itztli can't claim time "
                                              'is going to turn me to dust and leave her behind.',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_B07',
                                      'speaker': 'Citlali',
                                      'text': "...Idiot. Insufferable, golden-hearted idiot... There's no "
                                              'sunrise in here to count the years by anymore.',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_B08',
                                      'speaker': 'Narrator',
                                      'text': 'Her fists unclench against my coat, resting softly over my '
                                              'heartbeat in the unchanging amber dusk.',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                      'voice_emotion': ''}],
                           'choice': {'choice_id': 'C20_BAD2',
                                      'prompt': 'Inside the timeless painted study where outside centuries '
                                                'pass like silent rain:',
                                      'options': [{'opt_id': 'C20_A_OPEN_SIX_KITSUNE_TOGETHER',
                                                   'label': 'Reach up to the painted spotless shelf and '
                                                            "finally open 'New Chronicles of the Six "
                                                            "Kitsune' together on the rug.",
                                                   'effects': {'bond': 0,
                                                               'insight': 0,
                                                               'add_flags': ['BAD2_KITSUNE_READ']},
                                                   'next_node': 'END_BAD_2',
                                                   'reaction_beats': [{'beat_id': 'N32B_C20A_R1',
                                                                       'speaker': 'Narrator',
                                                                       'text': 'Sitting side by side '
                                                                               'against the cushions, I '
                                                                               'lift down the painted copy '
                                                                               'of her most guarded book '
                                                                               'and rest it open across '
                                                                               'both of our laps.',
                                                                       'inner_thought': '',
                                                                       'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                                                       'voice_emotion': ''},
                                                                      {'beat_id': 'N32B_C20A_R2',
                                                                       'speaker': 'Citlali',
                                                                       'text': '...Read slowly, Traveler. '
                                                                               'Unlike every book outside, '
                                                                               'nobody is ever going to '
                                                                               'print a sequel down here, '
                                                                               'so you had better make '
                                                                               'each chapter last a '
                                                                               'decade.',
                                                                       'inner_thought': 'Gaining something '
                                                                                        'and never losing '
                                                                                        'it again... What '
                                                                                        'a cruel, gentle '
                                                                                        'prison you built '
                                                                                        'us.',
                                                                       'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                                                       'voice_emotion': 'vn_tender_love'},
                                                                      {'beat_id': 'N32B_C20A_R3',
                                                                       'speaker': 'Aether',
                                                                       'text': 'Then when we finish the '
                                                                               "last page, we'll make up "
                                                                               'chapters of our own.',
                                                                       'inner_thought': '',
                                                                       'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                                                       'voice_emotion': ''},
                                                                      {'beat_id': 'N32B_C20A_R4',
                                                                       'speaker': 'Narrator',
                                                                       'text': 'While generations bloom '
                                                                               'and wither beyond the '
                                                                               'silent stone, '
                                                                               'rose-lavender and gold '
                                                                               'burn undimmed inside the '
                                                                               'seventh hue forever.',
                                                                       'inner_thought': '',
                                                                       'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                                                       'voice_emotion': ''}]},
                                                  {'opt_id': 'C20_B_INTERLACE_PAINTED_HANDS',
                                                   'label': 'Interlace your fingers with hers against the '
                                                            'painted windowpane and promise no star '
                                                            'outside shines brighter than her hue.',
                                                   'effects': {'bond': 0,
                                                               'insight': 0,
                                                               'add_flags': ['BAD2_HANDS_JOINED']},
                                                   'next_node': 'END_BAD_2',
                                                   'reaction_beats': [{'beat_id': 'N32B_C20B_R1',
                                                                       'speaker': 'Narrator',
                                                                       'text': 'Our joined palms rest '
                                                                               'against the cool painted '
                                                                               'glass where unchanging '
                                                                               'twilight reflects two '
                                                                               'silhouettes as one.',
                                                                       'inner_thought': '',
                                                                       'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                                                       'voice_emotion': ''},
                                                                      {'beat_id': 'N32B_C20B_R2',
                                                                       'speaker': 'Citlali',
                                                                       'text': "...Don't ever dare get "
                                                                               'bored of my nagging, '
                                                                               'Aether. Even after a '
                                                                               'thousand painted '
                                                                               "midnights, I'm not letting "
                                                                               'go of this hand.',
                                                                       'inner_thought': 'No dry season, no '
                                                                                        'goodbyes, no '
                                                                                        'fading gold... '
                                                                                        'Just stay right '
                                                                                        'here with me.',
                                                                       'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                                                       'voice_emotion': 'vn_tender_love'},
                                                                      {'beat_id': 'N32B_C20B_R3',
                                                                       'speaker': 'Aether',
                                                                       'text': 'A thousand midnights is '
                                                                               'barely a warm-up, Citlali.',
                                                                       'inner_thought': '',
                                                                       'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                                                       'voice_emotion': ''},
                                                                      {'beat_id': 'N32B_C20B_R4',
                                                                       'speaker': 'Narrator',
                                                                       'text': "Cradled inside Huitzilin's "
                                                                               'eternal canvas, the '
                                                                               'traveler of the stars '
                                                                               'folds his wings for good '
                                                                               '-- trading every horizon '
                                                                               'for one unforgotten hand.',
                                                                       'inner_thought': '',
                                                                       'cg': 'ui_assets/story_quest_cgs/citlali/end_bad2_painted_twilight.jpg',
                                                                       'voice_emotion': ''}]}]},
                           'routing': []},
           'N26_C1': {'node_id': 'N26_C1',
                      'chapter_id': 'CH3',
                      'title': "Raiding Granny's Hermitage",
                      'day_label': 'Day 7 - Bright Morning',
                      'location': 'Verona Sanctuary - Crowded Study',
                      'beats': [{'beat_id': 'N26_B01',
                                 'speaker': 'Narrator',
                                 'text': "By nine o'clock on the seventh morning, Citlali's secluded "
                                         'cliffside hermitage sounds like championship week at the Sacred '
                                         'Flame Stadium.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B02',
                                 'speaker': 'Narrator',
                                 'text': "Summoned at dawn under Tumaini's banner, Pyro Archon Mavuika, "
                                         'master smith Xilonen, Mualani, Kachina, Ororon, and Paimon crowd '
                                         'every cushion in the sunlit study.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B03',
                                 'speaker': 'Citlali',
                                 'text': 'Out! Every single loudmouthed one of you, OUT! Who gave the Pyro '
                                         'Archon permission to step over my laundry basket -- and Aether, '
                                         'wipe that victorious look off your face!',
                                 'inner_thought': 'Bundled in three blankets clutching Itzpapa in front of '
                                                  'Mavuika and Xilonen -- I am going to perish of shame '
                                                  'before midnight!',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N26_B04',
                                 'speaker': 'Mualani',
                                 'text': "No can do, Granny! Paimon told us you couldn't even taste water "
                                         'last night, so Kachina and I are officially taking over kitchen '
                                         'duty until further notice!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B05',
                                 'speaker': 'Kachina',
                                 'text': 'I-I brought warming crystals from the Children of Echoes to tuck '
                                         "around your ankles too, Granny Itztli! Please don't hex us!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B06',
                                 'speaker': 'Ororon',
                                 'text': 'And I moved my prime cabbages onto the porch so they can keep '
                                         'watch with Claw.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B07',
                                 'speaker': 'Citlali',
                                 'text': 'Cabbages are NOT guard animals, Ororon! Look at my rug -- two '
                                         'hundred years of sacred solitude trampled in ten minutes!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B08',
                                 'speaker': 'Narrator',
                                 'text': 'Stepping forward from the inner sanctum doorway after inspecting '
                                         'the bleaching First-Era Scroll, Mavuika folds her arms with a '
                                         'warm, unyielding smile.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B09',
                                 'speaker': 'Mavuika',
                                 'text': 'Two centuries of quietly shielding the Masters of the Night-Wind '
                                         'from the dark, Citlali -- and you really thought Natlan would '
                                         'let its sole Great Shaman pay a Loom-of-Fate debt alone?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B10',
                                 'speaker': 'Mavuika',
                                 'text': 'You scolded all of us often enough during the Abyss war to value '
                                         'our lives. Today, we return the lecture.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B11',
                                 'speaker': 'Citlali',
                                 'text': "I-I wasn't trying to be a martyr, Lord Mavuika! Raw Pyro "
                                         'vitality burns First-Era memory silk -- calling the Stadium '
                                         'would have turned three hundred years of Night-Wind elders to '
                                         'cinder!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B12',
                                 'speaker': 'Xilonen',
                                 'text': 'Raw Pyro would, sure. Good thing your golden Traveler dragged a '
                                         'Name-Engraver out of her morning nap too.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B13',
                                 'speaker': 'Narrator',
                                 'text': 'Setting a heavy leather case of obsidian tuning chisels onto the '
                                         'cedar table, Xilonen taps the inner sanctum doorframe '
                                         'thoughtfully.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B14',
                                 'speaker': 'Xilonen',
                                 'text': 'That dormant Obsidian Name-Core woven into the center of your '
                                         "scroll isn't ordinary stone, Granny -- it's an unawakened "
                                         'First-Era Ancient Name waiting for its rightful bearer.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B15',
                                 'speaker': 'Aether',
                                 'text': "Which means with Xilonen's forge rig and Mavuika stepping down "
                                         "the Sacred Flame, we don't have to let that tear drink another "
                                         'drop of your pulse.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B16',
                                 'speaker': 'Citlali',
                                 'text': '...Hmph. Do whatever noisy tinkering you want on the terrace, '
                                         'then. Just stay away from my top bookshelf!',
                                 'inner_thought': '...idiots. Every single one of them... Why does this '
                                                  'noisy room feel warmer than twenty quilts?',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': 'vn_shy_blush'},
                                {'beat_id': 'N26_B17',
                                 'speaker': 'Narrator',
                                 'text': "Burying her nose behind Itzpapa while accepting Mualani's "
                                         'steaming soup bowl, Citlali lets her shoulders drop into the '
                                         'first safe rest she has known all week.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_01_mavuika_xilonen_council.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N27_C2'}]},
           'N27_C2': {'node_id': 'N27_C2',
                      'chapter_id': 'CH3',
                      'title': 'Obsidian Chisel & Blanket Granny',
                      'day_label': 'Day 8 - Afternoon',
                      'location': "Sanctuary Sea-Terrace - Xilonen's Forge Rig",
                      'beats': [{'beat_id': 'N27_B01',
                                 'speaker': 'Narrator',
                                 'text': 'After a full night of uninterrupted sleep guarded by Kachina and '
                                         "Ororon, Day Eight finds Xilonen's portable phlogiston anvil "
                                         'humming briskly on the sunny sea-terrace.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Sparks of turquoise and gold dance into the salt breeze while '
                                         'Elder Tlapo watches attentively from the limestone parapet.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B03_F11',
                                 'speaker': 'Xilonen',
                                 'text': 'This shed feather you collected off Claw on Day One is pure '
                                         'gold, Tumaini -- its half-bleached tip gives my calipers an '
                                         "exact baseline for the scroll's ancestral dye weave.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F11_CLAW_IKTOMI_FEATHER']}},
                                {'beat_id': 'N27_B03_NOF11',
                                 'speaker': 'Xilonen',
                                 'text': "Even measuring from outside the silk casing, Claw's wing-hum is "
                                         "helping me narrow down the scroll's ancestral dye pitch.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': '',
                                 'when': {'forbid_flags': ['F11_CLAW_IKTOMI_FEATHER']}},
                                {'beat_id': 'N27_B04',
                                 'speaker': 'Aether',
                                 'text': "What's the verdict on waking that embedded Name-Core without "
                                         'tearing the First-Era silk, Xilonen?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B05',
                                 'speaker': 'Xilonen',
                                 'text': "Here's the honest smith's breakdown. Because that Obsidian "
                                         'Name-Core sits woven inside three centuries of fragile chronicle '
                                         'threads, working externally gives us two distinct builds.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B06',
                                 'speaker': 'Xilonen',
                                 'text': 'Build One is a Sixty-Day Phlogiston Stasis Clamp: thick '
                                         "containment rings that freeze the scroll's tear in amber glass. "
                                         'Zero danger to Granny, guaranteed survival --',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B07',
                                 'speaker': 'Xilonen',
                                 'text': "-- though clamping the weave leaves the Ancient Name 'Ukumbuko' "
                                         'permanently asleep, damps her long-range telepathy, and needs '
                                         'Mavuika and me to recharge it every sixty days.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B08',
                                 'speaker': 'Aether',
                                 'text': 'And Build Two?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B09',
                                 'speaker': 'Xilonen',
                                 'text': "An Ancient Name Resonance Bridge -- linking 'Tumaini' directly "
                                         "to 'Ukumbuko' so Citlali inherits the name and heals the scroll "
                                         'permanently on Night Eleven.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B10',
                                 'speaker': 'Xilonen',
                                 'text': "Catch is, an Ancient Name won't answer blank metal. I need a "
                                         'living cloth dyed in her hue, exact physical bleed measurements, '
                                         'AND someone who knows at least two guarded truths of her heart.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B11',
                                 'speaker': 'Narrator',
                                 'text': "Across the sunny terrace, bundled up in Mualani's fluffy "
                                         'surf-shawl with Citlalin on her knees, Citlali pretends to read '
                                         'a paperback upside down while peeking nervously toward our '
                                         'anvil.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B12',
                                 'speaker': 'Citlali',
                                 'text': '...',
                                 'inner_thought': 'Why are Xilonen and Aether both glancing over here?! Is '
                                                  'my blanket slipping, or are they plotting something '
                                                  'embarrassing?!',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B13',
                                 'speaker': 'Xilonen',
                                 'text': "We've got till dusk before Mavuika tests the flame coils. Want "
                                         'to calibrate groove spacing with me, or go check on our shy '
                                         'patient?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C16_C',
                                 'prompt': 'Xilonen sets up her obsidian groove calipers while Citlali '
                                           'sulks shyly in her blanket:',
                                 'options': [{'opt_id': 'C16_C1_CALIBRATE_XILONEN_CHISEL',
                                              'label': 'Work at the anvil with Xilonen to measure the '
                                                       "First-Era scroll's physical groove spacing against "
                                                       "Tumaini's resonance.",
                                              'effects': {'bond': 0,
                                                          'insight': 2,
                                                          'add_flags': ['XILONEN_CHISEL_TUNED']},
                                              'next_node': 'N28_C3',
                                              'reaction_beats': [{'beat_id': 'N27_C16C1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': "Holding Tumaini's golden "
                                                                          'phlogiston steady beside '
                                                                          "Xilonen's crystal gauge, I help "
                                                                          'her score seven micron-precise '
                                                                          'harmonic channels along the '
                                                                          'obsidian bridge blank.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N27_C16C1_R2',
                                                                  'speaker': 'Xilonen',
                                                                  'text': 'Clean calibration! With these '
                                                                          'groove tolerances locked onto '
                                                                          'my chisel, the physical bleed '
                                                                          'side of the Resonance Bridge is '
                                                                          'rock-solid.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N27_C16C1_R3',
                                                                  'speaker': 'Citlali',
                                                                  'text': '...',
                                                                  'inner_thought': 'Look at him focusing '
                                                                                   'at the forge with '
                                                                                   'sleeves rolled up... '
                                                                                   'Hmph, at least wipe '
                                                                                   'the soot off your '
                                                                                   'cheek, Traveler.',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C16_C2_COMFORT_SHY_GRANNY',
                                              'label': "Bring hot grainfruit tea over to Citlali's terrace "
                                                       "chair and keep her company away from the crowd's "
                                                       'teasing.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N28_C3',
                                              'reaction_beats': [{'beat_id': 'N27_C16C2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Pouring a fresh cup of spiced '
                                                                          'grainfruit tea, I pull a low '
                                                                          "stool beside Citlali's sunlit "
                                                                          'wicker chair and quietly turn '
                                                                          'her upside-down paperback '
                                                                          'right-side up.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N27_C16C2_R2',
                                                                  'speaker': 'Citlali',
                                                                  'text': 'I-I was testing how the kerning '
                                                                          "looked inverted! ...Don't tell "
                                                                          'Mualani or Mavuika I said this, '
                                                                          'alright?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N27_C16C2_R3',
                                                                  'speaker': 'Citlali',
                                                                  'text': 'Having the house noisy for two '
                                                                          'days... actually made the '
                                                                          'midnight cold feel a lot '
                                                                          'smaller.',
                                                                  'inner_thought': 'Especially when you '
                                                                                   'pull your chair right '
                                                                                   'beside mine like '
                                                                                   'this...',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch3c_02_xilonen_forge_terrace.jpg',
                                                                  'voice_emotion': 'vn_shy_blush'}]}]},
                      'routing': []},
           'N28_C3': {'node_id': 'N28_C3',
                      'chapter_id': 'CH4',
                      'title': 'Stepping Down the Sacred Flame',
                      'day_label': 'Day 9 - Evening',
                      'location': 'Astral Loom Sanctum - Regulator Ring',
                      'beats': [{'beat_id': 'N28_B01',
                                 'speaker': 'Narrator',
                                 'text': 'By dusk of the ninth day, Xilonen mounts three carved obsidian '
                                         'regulator coils around the Astral Loom basin while Mualani and '
                                         'Kachina brace cooling mist-shells along the walls.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Standing at the southern point of the circle, Mavuika ignites a '
                                         'single, hair-fine filament of golden-crimson Sacred Flame above '
                                         'her gloved palm.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B03',
                                 'speaker': 'Mavuika',
                                 'text': "Steady on the outer coils, everyone. I'm bringing the Sacred "
                                         'Flame down to one-hundredth of combat output so we warm the '
                                         "ancient dye without singing Huitzilin's silk.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B04_F05',
                                 'speaker': 'Ororon',
                                 'text': 'My garden aphids are glowing warm amber again beside the outer '
                                         "coil -- we're right on the edge of the sweet spot, Gramps!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F05_APHID_LOOM_TRACE']}},
                                {'beat_id': 'N28_B04_NOF05',
                                 'speaker': 'Ororon',
                                 'text': 'The air static around the lower border is dropping fast, Gramps '
                                         '-- the regulator ring is catching!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'forbid_flags': ['F05_APHID_LOOM_TRACE']}},
                                {'beat_id': 'N28_B05',
                                 'speaker': 'Narrator',
                                 'text': 'Bathed in soft amber-violet light, the bleached white scar '
                                         'across the First-Era Scroll stops spreading for the first '
                                         'evening since the new moon began.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B06',
                                 'speaker': 'Kachina',
                                 'text': 'Whoa... Look inside the center of the tapestry! That black stone '
                                         'is pulsing like a heartbeat!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B07',
                                 'speaker': 'Citlali',
                                 'text': "...'Sooner or later, you will inherit my name -- once you know "
                                         "why.' Over a century ago on the night I received my Cryo Vision, "
                                         'that stone whispered those exact words.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B08',
                                 'speaker': 'Mavuika',
                                 'text': "'Ukumbuko' -- Memory. No other shaman in two hundred years has "
                                         'carried the spiritual weight to wake it, Citlali.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B09',
                                 'speaker': 'Citlali',
                                 'text': 'Or maybe I spent two hundred years hiding from it because '
                                         "inheriting 'Memory' felt like volunteering to be the last person "
                                         'left in an empty room.',
                                 'inner_thought': 'Until a certain golden outlander walked in with my '
                                                  'spare key and refused to leave...',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B10',
                                 'speaker': 'Mavuika',
                                 'text': 'Too much Pyro vitality scorches delicate Night-Wind silk; too '
                                         'little leaves the Loom-of-Fate scar hungry.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B11',
                                 'speaker': 'Mavuika',
                                 'text': "Give us the final cue, Traveler -- you know Citlali's rhythm "
                                         'better than anyone in Natlan.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B12',
                                 'speaker': 'Narrator',
                                 'text': "Across the fire-lit chamber, Citlali's rose-gold eyes lock onto "
                                         'mine, awaiting my lead.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C17_C',
                                 'prompt': 'Mavuika holds the stepped-down Sacred Flame steady awaiting '
                                           'your final tuning cue:',
                                 'options': [{'opt_id': 'C17_C1_MAP_SACRED_FLAME_RATIO',
                                              'label': 'Guide Mavuika and Xilonen to the exact harmonic '
                                                       'step-down ratio where Pyro warmth illuminates '
                                                       'Night-Wind dye without burning it.',
                                              'effects': {'bond': 1, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N29_C4_GATE2',
                                              'reaction_beats': [{'beat_id': 'N28_C17C1_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Ease the flame down one more '
                                                                          'notch and weave seven parts '
                                                                          'Night-Wind mist around one '
                                                                          'filament of gold -- right '
                                                                          'there!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N28_C17C1_R2',
                                                                  'speaker': 'Mavuika',
                                                                  'text': 'Seven parts moonlight mist to '
                                                                          'one spark of Sacred Flame -- '
                                                                          "look at the scroll's border! "
                                                                          'Not a single thread singed, and '
                                                                          'the Name-Core is singing!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N28_C17C1_R3',
                                                                  'speaker': 'Citlali',
                                                                  'text': '...Show-off. Even the Pyro '
                                                                          'Archon takes tuning notes from '
                                                                          'you now.',
                                                                  'inner_thought': 'My fingers stopped '
                                                                                   'aching the second his '
                                                                                   'ratio clicked into '
                                                                                   'place...',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                                                  'voice_emotion': 'vn_sweet_happy'}]},
                                             {'opt_id': 'C17_C2_PROMISE_NO_SOLITUDE',
                                              'label': 'Speak openly across the telepathic link in front '
                                                       'of everyone: promise Citlali she will never face '
                                                       'another century behind locked doors.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N29_C4_GATE2',
                                              'reaction_beats': [{'beat_id': 'N28_C17C2_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': '...',
                                                                  'inner_thought': 'Look around this room, '
                                                                                   'Citlali -- and look at '
                                                                                   'me. Next year, next '
                                                                                   'decade, next century, '
                                                                                   'that room is never '
                                                                                   'going empty again.',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N28_C17C2_R2',
                                                                  'speaker': 'Citlali',
                                                                  'text': '...Projecting sappy speeches '
                                                                          'while the Pyro Archon is '
                                                                          'standing five feet away ought '
                                                                          'to be illegal, Traveler.',
                                                                  'inner_thought': "...don't stop, though. "
                                                                                   "Hearing you say 'next "
                                                                                   "century' like a "
                                                                                   'promise makes me brave '
                                                                                   'enough to try.',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                                                  'voice_emotion': 'vn_tender_love'},
                                                                 {'beat_id': 'N28_C17C2_R3',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Answering the steady warmth of '
                                                                          "her pulse, Mavuika's "
                                                                          'stepped-down flame settles '
                                                                          'naturally into gentle '
                                                                          'equilibrium around the basin.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': []},
           'N29_C4_GATE2': {'node_id': 'N29_C4_GATE2',
                            'chapter_id': 'CH4',
                            'title': 'Clamp of Glass or Bridge of Names',
                            'day_label': 'Day 10 - Evening',
                            'location': "Astral Loom Sanctum - Xilonen's Finished Plates",
                            'beats': [{'beat_id': 'N29_B01',
                                       'speaker': 'Narrator',
                                       'text': 'On the evening of Day Ten -- twenty-four hours before the '
                                               'New-Moon Tide -- Xilonen wipes forge-sweat from her brow '
                                               'and sets two finished obsidian housings onto the sanctum '
                                               'altar.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B02',
                                       'speaker': 'Narrator',
                                       'text': 'Outside on the terrace, Mualani, Kachina, Ororon, and '
                                               'Paimon hush their chatter, peering respectfully through '
                                               'the open archway.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B03',
                                       'speaker': 'Xilonen',
                                       'text': 'Both housings are ready ahead of schedule. Left housing is '
                                               'the Sixty-Day Phlogiston Stasis Clamp -- foolproof '
                                               'containment glass.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B04',
                                       'speaker': 'Xilonen',
                                       'text': 'Lock it tonight and the scroll freezes safely before '
                                               "tomorrow's tide, though 'Ukumbuko' stays unawakened behind "
                                               "glass and Granny's long-range link goes quiet.",
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B05',
                                       'speaker': 'Xilonen',
                                       'text': 'Right housing is the Ancient Name Resonance Bridge -- '
                                               "built to carry 'Ukumbuko' safely out of the silk beside "
                                               "'Tumaini' at midnight tomorrow.",
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B06',
                                       'speaker': 'Mavuika',
                                       'text': 'To engrave a living Resonance Bridge without shattering '
                                               "under the tide, Xilonen's chisel needs four anchors:",
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B07',
                                       'speaker': 'Mavuika',
                                       'text': "A personal cloth dyed in Citlali's living hue, verified "
                                               'physical bleed data, at least two intimate truths of her '
                                               'guarded heart, and unshakable bond between your two souls.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B08',
                                       'speaker': 'Citlali',
                                       'text': 'Either way, three hundred years of Night-Wind history '
                                               "survive... Don't gamble recklessly on my pride if a single "
                                               'piece feels uncertain, Aether.',
                                       'inner_thought': 'Yet if anyone in all the stars truly knows every '
                                                        "hidden shelf of my heart... it's you.",
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B09',
                                       'speaker': 'Mavuika',
                                       'text': 'Neither choice dishonors Natlan. One chooses gentle '
                                               'safety; the other claims a destiny two centuries in the '
                                               'making.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B10',
                                       'speaker': 'Xilonen',
                                       'text': 'My chisel is hot, Tumaini. Which plate goes onto the '
                                               'Astral Loom?',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B11',
                                       'speaker': 'Narrator',
                                       'text': 'Candlelight gleams across smooth obsidian on the left and '
                                               'open phlogiston channels on the right.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B12',
                                       'speaker': 'Narrator',
                                       'text': 'Beside me, Citlali holds her breath, her cool fingers '
                                               'brushing my wrist in silent trust.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B13',
                                       'speaker': 'Aether',
                                       'text': 'Here is our answer, Xilonen.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                       'voice_emotion': ''}],
                            'choice': {'choice_id': 'C18_C_GATE2',
                                       'prompt': 'Xilonen holds out the Resonance Bridge blank and the '
                                                 'Sixty-Day Stasis Clamp:',
                                       'options': [{'opt_id': 'C18_C_NAME_CONDUIT_UNLOCK',
                                                    'when': {'all_flags': ['F07_ROSE_HANDKERCHIEF'],
                                                             'any_flags': ['F01_SEAL_FROST_READ',
                                                                           'F05_APHID_LOOM_TRACE',
                                                                           'F08_QUENEPA_CONFESSION',
                                                                           'F11_CLAW_IKTOMI_FEATHER',
                                                                           'XILONEN_CHISEL_TUNED'],
                                                             'min_count_in': {'count': 2,
                                                                              'pool': ['F02_NOVEL_SECRET_KEPT',
                                                                                       'F03_SIX_KITSUNE_VERSE',
                                                                                       'F04_HAND_PROMISE_GIVEN',
                                                                                       'F06_GRAFFITI_TRUTH_HEARD']},
                                                             'min_insight': 7,
                                                             'min_bond': 10},
                                                    'unlock_badge': '[COMBINATION GATE #2 -- UKUMBUKO '
                                                                    'RESONANCE BRIDGE]',
                                                    'lock_hint': '[LOCKED: Needs Handkerchief + Bleed '
                                                                 'Proof + 2 Heart Truths + Insight 7 + '
                                                                 'Bond 10]',
                                                    'label': "Lay Citlali's rose-lavender handkerchief "
                                                             "across Xilonen's plate to engrave the "
                                                             'Ukumbuko Resonance Bridge for tomorrow '
                                                             'midnight!',
                                                    'effects': {'bond': 2,
                                                                'insight': 1,
                                                                'add_flags': ['COMBO2_CLEARED']},
                                                    'next_node': 'N34_CH5_CONVERGE',
                                                    'reaction_beats': [{'beat_id': 'N29_C18_OK_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': "Under Xilonen's blazing "
                                                                                "chisel and Mavuika's "
                                                                                'steady flame, the '
                                                                                'obsidian plate drinks the '
                                                                                'rose-lavender and gold of '
                                                                                "Citlali's handkerchief -- "
                                                                                'ringing with an ancient '
                                                                                'Night-Wind chord that '
                                                                                'makes every lantern '
                                                                                'flare!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_02_name_conduit_diff.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N29_C18_OK_R2',
                                                                        'speaker': 'Xilonen',
                                                                        'text': 'Listen to that resonance! '
                                                                                'Every groove accepted her '
                                                                                'heart-signature on the '
                                                                                'first strike -- '
                                                                                "'Ukumbuko' is wide awake "
                                                                                'inside the silk!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_02_name_conduit_diff.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N29_C18_OK_R3',
                                                                        'speaker': 'Citlali',
                                                                        'text': "That chord... It's the "
                                                                                'exact voice from the '
                                                                                'night I received my '
                                                                                'Vision! Tomorrow at '
                                                                                'midnight, Aether -- walk '
                                                                                'me to the threshold!',
                                                                        'inner_thought': 'With him and all '
                                                                                         'of them standing '
                                                                                         'behind me, I '
                                                                                         "don't have to "
                                                                                         'hide from that '
                                                                                         'name anymore!',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_02_name_conduit_diff.jpg',
                                                                        'voice_emotion': 'vn_sweet_happy'},
                                                                       {'beat_id': 'N29_C18_OK_R4',
                                                                        'speaker': 'Mavuika',
                                                                        'text': 'Rest well tonight, Great '
                                                                                'Shaman. Tomorrow '
                                                                                'midnight, Natlan welcomes '
                                                                                "'Ukumbuko' home!",
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_02_name_conduit_diff.jpg',
                                                                        'voice_emotion': ''}]},
                                                   {'opt_id': 'C18_C_SIXTY_DAY_STASIS_CLAMP',
                                                    'label': "Choose protective caution: lock Xilonen's "
                                                             'Sixty-Day Phlogiston Stasis Clamp around the '
                                                             'scroll so Citlali faces zero risk tomorrow '
                                                             'night.',
                                                    'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                                    'next_node': 'N33_GOOD_1',
                                                    'reaction_beats': [{'beat_id': 'N29_C18_CLAMP_R1',
                                                                        'speaker': 'Aether',
                                                                        'text': 'No gambles with your '
                                                                                'life, Citlali. Lock the '
                                                                                'Stasis Clamp, Xilonen -- '
                                                                                "we'll gladly come back "
                                                                                'every sixty days to keep '
                                                                                'her safe.',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N29_C18_CLAMP_R2',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Heavy obsidian '
                                                                                'containment rings slide '
                                                                                'into place around the '
                                                                                'First-Era Scroll with a '
                                                                                'deep amber hum, freezing '
                                                                                'the white unraveling scar '
                                                                                'instantly behind thick '
                                                                                'phlogiston glass.',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N29_C18_CLAMP_R3',
                                                                        'speaker': 'Citlali',
                                                                        'text': '...Overprotective dummy. '
                                                                                'Letting an Ancient Name '
                                                                                'sleep just to keep an old '
                                                                                'recluse in one piece... '
                                                                                'Thank you, Aether.',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/citlali/ch4c_01_sacred_flame_regulator_base.jpg',
                                                                        'voice_emotion': ''}]}]},
                            'routing': []},
           'N33_GOOD_1': {'node_id': 'N33_GOOD_1',
                          'chapter_id': 'CH4',
                          'title': 'Sixty-Day Candlelight',
                          'day_label': 'Day 12 - Warm Sunset',
                          'location': 'Sanctuary Rooftop - Lantern Feast',
                          'beats': [{'beat_id': 'N33_B01',
                                     'speaker': 'Narrator',
                                     'text': 'New-Moon Midnight passes over Verona Point without a single '
                                             'drop of lost memory or frostbite.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B02',
                                     'speaker': 'Narrator',
                                     'text': "Down in the quiet sanctum below, Xilonen's obsidian Stasis "
                                             'Clamp hums like a warm hearth -- holding the unfinished '
                                             'First-Era Scroll safely suspended inside amber phlogiston '
                                             'glass.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B03',
                                     'speaker': 'Narrator',
                                     'text': 'Up on the flat stargazing roof by sunset of the twelfth day, '
                                             'strings of paper lanterns sway above sizzling skewers, sweet '
                                             'Quenepa Berry punch, and laughter.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B04',
                                     'speaker': 'Mualani',
                                     'text': "Glasses up, everyone! To Granny Itztli's clean bill of "
                                             'health -- and to invading this roof every sixty days with '
                                             'fresh surf-and-turf barbecue whenever Xilonen and Mavuika '
                                             'recharge the clamp!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': 'outing_arrive_photo'},
                                    {'beat_id': 'N33_B05',
                                     'speaker': 'Kachina',
                                     'text': 'Yay! That means six guaranteed rooftop parties a year! Even '
                                             'Citlalin and Itzpapa got little flower leis!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B06',
                                     'speaker': 'Ororon',
                                     'text': 'I already planted a sixty-day cabbage calendar by the back '
                                             'fence so nobody loses count, Granny. Gramps gets the cushion '
                                             'right next to yours every single cycle.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B07',
                                     'speaker': 'Xilonen',
                                     'text': "Just don't hang wet laundry on my regulator rings "
                                             "downstairs, alright? Precision smithing isn't a drying rack.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B08',
                                     'speaker': 'Mavuika',
                                     'text': "To Natlan's Great Shaman -- may your house never be too "
                                             'quiet again.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B09',
                                     'speaker': 'Citlali',
                                     'text': 'Hmph! Turning solemn shamanic maintenance into a recurring '
                                             'picnic... Every last one of you has zero respect for your '
                                             'elders!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': 'vn_playful_tease'},
                                    {'beat_id': 'N33_B10',
                                     'speaker': 'Paimon',
                                     'text': "Hehe, look at Citlali refilling everyone's Quenepa cups "
                                             'while she complains! And she tasted the glaze right away '
                                             'tonight!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B11',
                                     'speaker': 'Narrator',
                                     'text': 'Later, as the others gather down by the parapet to watch '
                                             'Elder Tlapo catch grilled fish in mid-air, Citlali and I '
                                             'linger side by side near the corner lantern.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B12',
                                     'speaker': 'Narrator',
                                     'text': 'There is an honest, bittersweet price to our caution.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B13',
                                     'speaker': 'Narrator',
                                     'text': 'Downstairs behind thick amber glass, the Ancient Name '
                                             "'Ukumbuko' remains uninherited -- a century-old calling left "
                                             'gently unanswered.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B14',
                                     'speaker': 'Narrator',
                                     'text': "Whenever thick sea-fog rolls in at dusk, Citlali's "
                                             'peripheral color-sight still dims slightly around the edges, '
                                             'and our once-effortless telepathy no longer carries across '
                                             'town.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B15',
                                     'speaker': 'Aether',
                                     'text': 'Do you regret not waking the name last night, Citlali?',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B16',
                                     'speaker': 'Citlali',
                                     'text': '...Ask me two weeks ago and my pride might have sulked. '
                                             'Looking at Mualani burning skewers while Ororon lectures a '
                                             "cabbage? I think 'Granny Itztli' is plenty of name for one "
                                             'lifetime.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B17',
                                     'speaker': 'Narrator',
                                     'text': 'Hugging Itzpapa against her knees, Citlali leans her temple '
                                             'lightly against my shoulder in the warm candlelight.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B18',
                                     'speaker': 'Narrator',
                                     'text': 'The instant her shoulder touches mine, a soft, crystal-clear '
                                             'voice blooms across the shortened range of our link.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B19',
                                     'speaker': 'Citlali',
                                     'text': "Don't think a sixty-day maintenance schedule gets you off "
                                             'the hook, Traveler. You had better be on this roof before '
                                             'the fifty-ninth sunset -- every single time.',
                                     'inner_thought': '...even if our link only works shoulder-to-shoulder '
                                                      'now, that just gives me an excuse to keep you '
                                                      'close.',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': 'vn_sweet_happy'},
                                    {'beat_id': 'N33_B20',
                                     'speaker': 'Narrator',
                                     'text': 'Under string-lights and falling coastal stars, we clink '
                                             'painted goblets of real golden Quenepa wine -- counting time '
                                             'not in centuries lost, but in candlelit returns.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/citlali/end_good_rooftop_candlelight.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [],
                          'ending_id': 'END_GOOD'},
           'N34_CH5_CONVERGE': {'node_id': 'N34_CH5_CONVERGE',
                                'chapter_id': 'CH5',
                                'title': 'The Iridescent Threshold',
                                'day_label': 'Day 11 - New-Moon Midnight',
                                'location': 'Night Kingdom Loom Threshold - Obsidian Basin',
                                'beats': [{'beat_id': 'N34_B01',
                                           'speaker': 'Narrator',
                                           'text': 'Midnight of the eleventh night arrives under a '
                                                   "moonless velvet sky. Below the Astral Loom's open "
                                                   "conduit, the boundary between Verona's cliffside "
                                                   'sanctum and the Night Kingdom shimmers like liquid '
                                                   'opal.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_B02',
                                           'speaker': 'Narrator',
                                           'text': 'Three centuries of woven Night-Wind tapestries billow '
                                                   'weightlessly around the obsidian basin as the '
                                                   'twelve-day Ley-tide reaches its zenith.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_B03_RTA_OK',
                                           'speaker': 'Narrator',
                                           'text': 'Outside the threshold ring, Elder Tlapo spreads his '
                                                   "ancient wings while Huitzilin's Starlight Borrowing "
                                                   'lattice hums steadily across our joined palms.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_A', 'UKUMBUKO_WEAVE_PRIMED']}},
                                          {'beat_id': 'N34_B03_RTA_STRAIN',
                                           'speaker': 'Narrator',
                                           'text': 'Outside the threshold ring, Elder Tlapo stands watch '
                                                   "while the raw elemental strain of last night's vigil "
                                                   'leaves a thin, cautious hush across our link.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_A', 'RAW_VIGIL_STRAIN']}},
                                          {'beat_id': 'N34_B03_RTB',
                                           'speaker': 'Narrator',
                                           'text': 'At the conduit perimeter, Ororon and Chasca steady the '
                                                   'seven-color refraction beam still singing from '
                                                   "Huitzilin's recovered Opal Spindle.",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_B']}},
                                          {'beat_id': 'N34_B03_RTC',
                                           'speaker': 'Narrator',
                                           'text': 'Around the outer sanctum, Mavuika and Xilonen hold the '
                                                   'newly engraved Ukumbuko Resonance Bridge level, '
                                                   "linking the sanctuary altar directly to the scroll's "
                                                   'inner Name-Core.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_C']}},
                                          {'beat_id': 'N34_B04',
                                           'speaker': 'Narrator',
                                           'text': 'From the starry depths of the reconstructed Ley-vessel '
                                                   '-- sustained eternally since the Captain took his seat '
                                                   "upon the throne -- Yohualtecuhtin's serene presence "
                                                   'ripples across the mist.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_B05',
                                           'speaker': 'Yohualtecuhtin',
                                           'text': 'The vessel of the Night Kingdom stands unbroken, Great '
                                                   'Shaman, yet cosmic law forbids the realm of the dead '
                                                   'from authoring living emotion.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_B06',
                                           'speaker': 'Yohualtecuhtin',
                                           'text': 'Only a living heart can choose why it remembers. Step '
                                                   'forward beside Tumaini, daughter of the Night-Wind, '
                                                   'and answer the name that has waited since your Vision '
                                                   'night.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_B07',
                                           'speaker': 'Aether',
                                           'text': "Right beside you, Citlali. Let's answer together.",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/citlali/ch5_01_nightkingdom_threshold.jpg',
                                           'voice_emotion': ''}],
                                'choice': None,
                                'routing': [{'default': True, 'next_node': 'N35'}]},
           'N35': {'node_id': 'N35',
                   'chapter_id': 'CH5',
                   'title': 'Ukumbuko -- The Living Hue',
                   'day_label': 'Day 11 - Midnight',
                   'location': 'Night Kingdom Loom Threshold - Before the Name-Core',
                   'beats': [{'beat_id': 'N35_B01',
                              'speaker': 'Narrator',
                              'text': 'Out of the mist-shrouded hues rises the First-Era Obsidian '
                                      'Name-Core, echoing with the ancestral words Citlali first heard '
                                      "over a century ago: 'Sooner or later, you will inherit my name -- "
                                      "once you know why.'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_02_ukumbuko_awakening_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B02',
                              'speaker': 'Narrator',
                              'text': 'Standing before the floating black crystal, Citlali lowers her '
                                      'hands from her sleeves -- neither Itzpapa nor seven shamanic walls '
                                      'standing between her heart and the threshold.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_02_ukumbuko_awakening_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B03_F06',
                              'speaker': 'Citlali',
                              'text': 'For two hundred years after Huitzilin left that seven-petal mark on '
                                      'my wall, I told myself weaving scrolls was just a way to pass the '
                                      'centuries without getting hurt again.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_02_ukumbuko_awakening_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F06_GRAFFITI_TRUTH_HEARD']}},
                             {'beat_id': 'N35_B03_NOF06',
                              'speaker': 'Citlali',
                              'text': 'For two hundred years after Huitzilin faded into the dry season, I '
                                      'told myself locking my gate was the only sensible way for a '
                                      'long-lived shaman to survive.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_02_ukumbuko_awakening_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F06_GRAFFITI_TRUTH_HEARD']}},
                             {'beat_id': 'N35_B04',
                              'speaker': 'Citlali',
                              'text': "In the Seven-Hued Ruins I learned Huitzilin's answer -- that the "
                                      'color of memories outlasts mortality. Yet I still treated memory '
                                      'like a grave-offering meant only for those already gone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_02_ukumbuko_awakening_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B05_OPEN',
                              'speaker': 'Citlali',
                              'text': 'Not anymore. Looking at the golden light beside me, I finally know '
                                      "my wish: memory isn't losing something straight away -- it is "
                                      'daring to let someone living carry your color forward!',
                              'inner_thought': 'Hear me clearly, ancestor -- and hear me clearly, Aether! '
                                               'I am done hiding behind two hundred years!',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_02_ukumbuko_awakening_base.jpg',
                              'voice_emotion': 'vn_sweet_happy',
                              'when': {'all_flags': ['F07_ROSE_HANDKERCHIEF'],
                                       'forbid_flags': ['COLD_FIREWALL_NO_VOW', 'RAW_VIGIL_STRAIN'],
                                       'min_bond': 12}},
                             {'beat_id': 'N35_B05_MUTED',
                              'speaker': 'Citlali',
                              'text': 'Even if a shaman keeps a pane of quiet glass around her own foolish '
                                      'heart... I still refuse to let three centuries of Night-Wind lives '
                                      'fade into blank white mist!',
                              'inner_thought': "[...behind quiet glass: let this name protect the tribe's "
                                               'colors, even if I keep mine tucked safely away...]',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_02_ukumbuko_awakening_base.jpg',
                              'voice_emotion': '',
                              'when': {'any_of': [{'forbid_flags': ['F07_ROSE_HANDKERCHIEF']},
                                                  {'any_flags': ['COLD_FIREWALL_NO_VOW',
                                                                 'RAW_VIGIL_STRAIN']},
                                                  {'max_bond': 11}]}},
                             {'beat_id': 'N35_B06',
                              'speaker': 'Narrator',
                              'text': 'Obsidian facets split open in a shower of opal fire! Answering '
                                      "Tumaini's golden blaze at my side, the ancient glyph 'Ukumbuko -- "
                                      "Memory' engraves itself in luminous rose-lavender above Citlali's "
                                      'palm!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_02_ukumbuko_awakening_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B07',
                              'speaker': 'Yohualtecuhtin',
                              'text': 'The Night Kingdom witnesses your answer, Ukumbuko. Weave now -- and '
                                      'mend what fate tore asunder.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_02_ukumbuko_awakening_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N36_LOOM_CRESCENDO'}]},
           'N36_LOOM_CRESCENDO': {'node_id': 'N36_LOOM_CRESCENDO',
                                  'chapter_id': 'CH5',
                                  'title': 'Mirror Outside the Ley Lines',
                                  'day_label': 'Day 11 - Past Midnight',
                                  'location': 'Night Kingdom Loom Threshold - Chromatic Zenith',
                                  'beats': [{'beat_id': 'N36_B01',
                                             'speaker': 'Narrator',
                                             'text': 'As Ukumbuko and Tumaini lock into harmonic unison, '
                                                     'the First-Era Chronicle drinks deep -- and triggers '
                                                     'an ontological miracle no mortal Ley Line could '
                                                     'produce alone.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                             'voice_emotion': ''},
                                            {'beat_id': 'N36_B02',
                                             'speaker': 'Narrator',
                                             'text': 'Every drop of living rose-lavender pigment Citlali '
                                                     'pours into the Loom-of-Fate scar strikes my Fourth '
                                                     'Descender memory outside Irminsul and reflects '
                                                     'straight back into her spirit, doubled in golden '
                                                     'radiance!',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                             'voice_emotion': ''},
                                            {'beat_id': 'N36_B03',
                                             'speaker': 'Aether',
                                             'text': 'Nothing lost, nothing consumed -- every color you '
                                                     'give comes straight back to you through me!',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                             'voice_emotion': ''},
                                            {'beat_id': 'N36_B04',
                                             'speaker': 'Narrator',
                                             'text': 'Across fifty feet of ancient silk, bone-white static '
                                                     'transforms into indestructible ribbons of '
                                                     'rose-lavender, starlight opal, and Descender gold -- '
                                                     'sealing three hundred years of Night-Wind history '
                                                     'permanently!',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                             'voice_emotion': ''},
                                            {'beat_id': 'N36_B05_OPEN',
                                             'speaker': 'Citlali',
                                             'text': "It's holding -- not a single memory lost, not a "
                                                     'single thread bleached! Whoa -- wait, why did '
                                                     'gravity suddenly turn sideways--?!',
                                             'inner_thought': "Catch me, catch me, don't let me face-plant "
                                                              'right after inheriting an Ancient Name!',
                                             'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                             'voice_emotion': 'outing_bump_rescue',
                                             'when': {'all_flags': ['F07_ROSE_HANDKERCHIEF'],
                                                      'forbid_flags': ['COLD_FIREWALL_NO_VOW',
                                                                       'RAW_VIGIL_STRAIN'],
                                                      'min_bond': 12}},
                                            {'beat_id': 'N36_B05_MUTED',
                                             'speaker': 'Citlali',
                                             'text': 'The seam is sealed -- every ancestral thread '
                                                     'intact... Ah -- steady the step, Traveler, the '
                                                     'conduit is receding fast!',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                             'voice_emotion': 'outing_bump_rescue',
                                             'when': {'any_of': [{'forbid_flags': ['F07_ROSE_HANDKERCHIEF']},
                                                                 {'any_flags': ['COLD_FIREWALL_NO_VOW',
                                                                                'RAW_VIGIL_STRAIN']},
                                                                 {'max_bond': 11}]}}],
                                  'choice': {'choice_id': 'C21_CH5',
                                             'prompt': 'As the iridescent loom shockwave recedes, Citlali '
                                                       'sways weightlessly at the threshold rim:',
                                             'options': [{'opt_id': 'C21_A_CALL_HER_ACROSS_LINK',
                                                          'label': "Call 'Citlali -- Ukumbuko!' straight "
                                                                   'across your mental bridge as you catch '
                                                                   'her back into the waking sanctum.',
                                                          'effects': {'bond': 2,
                                                                      'insight': 0,
                                                                      'add_flags': ['CH5_VOICE_LINK_CALL']},
                                                          'next_node': 'N37_SANCTUARY_MORNING',
                                                          'reaction_beats': [{'beat_id': 'N36_C21A_R1',
                                                                              'speaker': 'Narrator',
                                                                              'text': 'Guided home by the '
                                                                                      'sound of both her '
                                                                                      'names ringing '
                                                                                      'clearly inside our '
                                                                                      'shared channel, '
                                                                                      'Citlali lands '
                                                                                      'lightly against my '
                                                                                      'shoulder as '
                                                                                      'salt-crisp coastal '
                                                                                      'air rushes back '
                                                                                      'into our lungs.',
                                                                              'inner_thought': '',
                                                                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                                                              'voice_emotion': ''},
                                                                             {'beat_id': 'N36_C21A_R2',
                                                                              'speaker': 'Citlali',
                                                                              'text': '...Calling both '
                                                                                      'names at once '
                                                                                      'inside my head is '
                                                                                      'cheating, '
                                                                                      'Traveler... Give me '
                                                                                      'five minutes before '
                                                                                      'anyone turns on a '
                                                                                      'lamp...',
                                                                              'inner_thought': '',
                                                                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                                                              'voice_emotion': ''}]},
                                                         {'opt_id': 'C21_B_ANCHOR_TUMAINI_PULSE',
                                                          'label': "Clasp her wrist over Tumaini's warm "
                                                                   'golden pulse, grounding her heartbeat '
                                                                   'step-for-step onto solid coastal '
                                                                   'stone.',
                                                          'effects': {'bond': 2,
                                                                      'insight': 0,
                                                                      'add_flags': ['CH5_TUMAINI_PULSE_ANCHOR']},
                                                          'next_node': 'N37_SANCTUARY_MORNING',
                                                          'reaction_beats': [{'beat_id': 'N36_C21B_R1',
                                                                              'speaker': 'Narrator',
                                                                              'text': 'Anchored to the '
                                                                                      'steady rhythm of '
                                                                                      "Tumaini's golden "
                                                                                      'phlogiston against '
                                                                                      "her palm, Citlali's "
                                                                                      'boots touch warm '
                                                                                      'sanctuary flagstone '
                                                                                      'without a trace of '
                                                                                      'frost.',
                                                                              'inner_thought': '',
                                                                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                                                              'voice_emotion': ''},
                                                                             {'beat_id': 'N36_C21B_R2',
                                                                              'speaker': 'Citlali',
                                                                              'text': '...Warm stone, warm '
                                                                                      'hands... Just let a '
                                                                                      'dignified elder '
                                                                                      'rest her eyes for '
                                                                                      'five minutes, '
                                                                                      'alright...?',
                                                                              'inner_thought': '',
                                                                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_03_loom_crescendo_diff.jpg',
                                                                              'voice_emotion': ''}]}]},
                                  'routing': []},
           'N37_SANCTUARY_MORNING': {'node_id': 'N37_SANCTUARY_MORNING',
                                     'chapter_id': 'CH5',
                                     'title': 'Sweet Quenepa Before Sunrise',
                                     'day_label': 'Day 12 - Pre-Dawn',
                                     'location': 'Sanctuary Study - Sun-Touched Quilt',
                                     'beats': [{'beat_id': 'N37_B01',
                                                'speaker': 'Narrator',
                                                'text': 'First pink light of the twelfth day filters '
                                                        'through the cedar shutters, warming the repaired '
                                                        'First-Era Scroll resting serenely in the inner '
                                                        'room.',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': ''},
                                               {'beat_id': 'N37_B02',
                                                'speaker': 'Narrator',
                                                'text': 'Curled under a soft woven quilt with Itzpapa and '
                                                        'Citlalin tucked beside her elbow, Citlali blinks '
                                                        'awake to the unmistakable aroma of warm Quenepa '
                                                        'Berry glaze.',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': ''},
                                               {'beat_id': 'N37_B03',
                                                'speaker': 'Paimon',
                                                'text': "She's awake! Paimon tested the glaze three times "
                                                        "just to make sure it's extra sweet -- go on, "
                                                        'Citlali, tell Paimon if your tongue works again!',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': ''},
                                               {'beat_id': 'N37_B04',
                                                'speaker': 'Citlali',
                                                'text': 'Tested it three times means you ate half the '
                                                        'tray, you greedy little floaty thing!',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': 'greet_doorstep'},
                                               {'beat_id': 'N37_B05',
                                                'speaker': 'Narrator',
                                                'text': 'Taking a cautious nibble off a glazed pastry '
                                                        'corner, Citlali goes completely still -- '
                                                        'rose-gold eyes widening as sunlit color floods '
                                                        'her cheeks.',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': ''},
                                               {'beat_id': 'N37_B06',
                                                'speaker': 'Citlali',
                                                'text': '...Tart berry skin, roasted grainfruit crunch, '
                                                        'honeyed golden pulp... Every single note of taste '
                                                        'and color is back.',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': ''},
                                               {'beat_id': 'N37_B07_CALL',
                                                'speaker': 'Aether',
                                                'text': 'Good morning, Ukumbuko. No more white static in '
                                                        'your ears?',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': '',
                                                'when': {'all_flags': ['CH5_VOICE_LINK_CALL']}},
                                               {'beat_id': 'N37_B07_PULSE',
                                                'speaker': 'Aether',
                                                'text': 'Fingers warm all the way to the tips, Citlali -- '
                                                        "just like when Tumaini's pulse grounded us at "
                                                        'midnight.',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': '',
                                                'when': {'all_flags': ['CH5_TUMAINI_PULSE_ANCHOR']}},
                                               {'beat_id': 'N37_B08_OPEN',
                                                'speaker': 'Citlali',
                                                'text': 'Hmph. Adequate nursing work, I suppose. Come walk '
                                                        'out to the cliff rail before Paimon demands a '
                                                        'medal -- the dawn breeze is clearest before six.',
                                                'inner_thought': 'Crystal clear... Every beat of his heart '
                                                                 'sounds warmer than bell-glass inside my '
                                                                 'head!',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': 'vn_sweet_happy',
                                                'when': {'all_flags': ['F07_ROSE_HANDKERCHIEF'],
                                                         'forbid_flags': ['COLD_FIREWALL_NO_VOW',
                                                                          'RAW_VIGIL_STRAIN'],
                                                         'min_bond': 14}},
                                               {'beat_id': 'N37_B08_MUTED',
                                                'speaker': 'Citlali',
                                                'text': '...No static at all, Traveler. Thank you. Step '
                                                        'out to the cliff rail with me for a moment -- '
                                                        'there is a proper thank-you a Great Shaman owes '
                                                        "Natlan's hero.",
                                                'inner_thought': '[...faint behind polite glass: keep your '
                                                                 "composure, Citlali. Don't ask for more "
                                                                 'than you earned...]',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_04_morning_tea_sanctuary.jpg',
                                                'voice_emotion': '',
                                                'when': {'any_of': [{'forbid_flags': ['F07_ROSE_HANDKERCHIEF']},
                                                                    {'any_flags': ['COLD_FIREWALL_NO_VOW',
                                                                                   'RAW_VIGIL_STRAIN']},
                                                                    {'max_bond': 13}]}}],
                                     'choice': None,
                                     'routing': [{'default': True, 'next_node': 'N38'}]},
           'N38': {'node_id': 'N38',
                   'chapter_id': 'CH5',
                   'title': 'Footsteps Down the Cove',
                   'day_label': 'Day 12 - Sunrise',
                   'location': 'Verona Sanctuary - Terrace & Cliff Path',
                   'beats': [{'beat_id': 'N38_B01',
                              'speaker': 'Narrator',
                              'text': 'Passing her leveled cedar bookshelf on the way outside -- where '
                                      "'New Chronicles of the Six Kitsune' and her spotless Yae first "
                                      'editions catch the early rose light -- we step onto the cliff path.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_05_verona_cliff_sunrise_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B02',
                              'speaker': 'Narrator',
                              'text': "Along the outer sanctuary plaster, Huitzilin's tiny seven-petal "
                                      'ochre flower gleams dry and bright above the clean basalt steps.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_05_verona_cliff_sunrise_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B03_RTA',
                              'speaker': 'Narrator',
                              'text': 'Down by the garden gate, Ororon tips a quiet salute beside Paimon '
                                      'while Elder Tlapo circles once overhead before gliding inland -- '
                                      'giving the two of us the whole sunrise headland to ourselves.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_05_verona_cliff_sunrise_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['ROUTE_A']}},
                             {'beat_id': 'N38_B03_RTB',
                              'speaker': 'Narrator',
                              'text': 'Down on the lower steps, Ororon, Chasca, and Paimon wave fondly as '
                                      'Elder Tlapo lifts into the morning thermals -- leaving the two of '
                                      'us quiet privacy along the upper sea-cliff.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_05_verona_cliff_sunrise_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['ROUTE_B']}},
                             {'beat_id': 'N38_B03_RTC',
                              'speaker': 'Narrator',
                              'text': 'Down along the lower cove trail, Mavuika, Xilonen, Mualani, '
                                      'Kachina, Ororon, and Paimon wave warm congratulations beside Elder '
                                      'Tlapo before tactfully heading toward town for breakfast.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_05_verona_cliff_sunrise_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['ROUTE_C']}},
                             {'beat_id': 'N38_B04',
                              'speaker': 'Aether',
                              'text': 'Looks like everyone unanimously decided Granny Ukumbuko earned a '
                                      'quiet morning.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_05_verona_cliff_sunrise_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B05',
                              'speaker': 'Narrator',
                              'text': 'Out at the very tip of Verona Point, golden sunrise breaks across '
                                      'the western surf, painting the limestone rail in the exact '
                                      "rose-lavender and gold of last night's weave.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/ch5_05_verona_cliff_sunrise_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N39_VERONA_DAWN_CLIFF'}]},
           'N39_VERONA_DAWN_CLIFF': {'node_id': 'N39_VERONA_DAWN_CLIFF',
                                     'chapter_id': 'CH5',
                                     'title': 'Where the Night-Wind Turns',
                                     'day_label': 'Day 12 - Golden Sunrise',
                                     'location': 'Verona Point Headland - Above the Western Surf',
                                     'beats': [{'beat_id': 'N39_B01',
                                                'speaker': 'Narrator',
                                                'text': "Sea wind lifts the pale rose strands of Citlali's "
                                                        'hair as she turns to face me above the rolling '
                                                        'western surf. Behind us, Itzpapa and Citlalin '
                                                        'doze contentedly on the warm stone.',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_06_verona_cliff_turn_diff.jpg',
                                                'voice_emotion': ''},
                                               {'beat_id': 'N39_B02',
                                                'speaker': 'Citlali',
                                                'text': 'Two hundred years of counting every dry season... '
                                                        'and one stubborn outlander walks through my door '
                                                        "and turns an old hermit into 'Ukumbuko' in twelve "
                                                        'days.',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_06_verona_cliff_turn_diff.jpg',
                                                'voice_emotion': ''},
                                               {'beat_id': 'N39_B03',
                                                'speaker': 'Aether',
                                                'text': 'The name was always yours, Citlali. You just '
                                                        'needed a reason to want tomorrow.',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_06_verona_cliff_turn_diff.jpg',
                                                'voice_emotion': ''},
                                               {'beat_id': 'N39_B04',
                                                'speaker': 'Narrator',
                                                'text': 'Her slender fingers hover half an inch from the '
                                                        "rail beside my hand -- poised on the razor's edge "
                                                        'between two centuries of practiced retreat and a '
                                                        'lifetime she has never once dared ask for aloud.',
                                                'inner_thought': '',
                                                'cg': 'ui_assets/story_quest_cgs/citlali/ch5_06_verona_cliff_turn_diff.jpg',
                                                'voice_emotion': ''}],
                                     'choice': {'choice_id': 'C22_FINAL',
                                                'prompt': "Sunrise gilds Verona Point as Citlali's hand "
                                                          'hesitates beside yours:',
                                                'options': [{'opt_id': 'C22_TRUE_ETERNAL_VOW',
                                                             'when': {'all_flags': ['F07_ROSE_HANDKERCHIEF'],
                                                                      'forbid_flags': ['COLD_FIREWALL_NO_VOW',
                                                                                       'RAW_VIGIL_STRAIN'],
                                                                      'min_bond': 14},
                                                             'unlock_badge': '[TRUE ENDING -- COLOR OF '
                                                                             'ETERNITY]',
                                                             'lock_hint': '[LOCKED: Needs Rose '
                                                                          'Handkerchief + Open Unstrained '
                                                                          'Link + Bond 14]',
                                                             'label': 'Tie her rose-lavender handkerchief '
                                                                      'softly around your joined wrists '
                                                                      'and ask Ukumbuko to stain your '
                                                                      'immortal memory forever.',
                                                             'effects': {'bond': 3,
                                                                         'insight': 0,
                                                                         'add_flags': ['TRUE_ETERNITY_SEALED']},
                                                             'next_node': 'N40',
                                                             'reaction_beats': [{'beat_id': 'N39_C22_TRUE_R1',
                                                                                 'speaker': 'Narrator',
                                                                                 'text': 'Drawing out her '
                                                                                         'rose-lavender '
                                                                                         'handkerchief '
                                                                                         'threaded with '
                                                                                         'Descender gold, '
                                                                                         'I catch her '
                                                                                         'hesitating hand '
                                                                                         'gently and loop '
                                                                                         'the soft silk '
                                                                                         'around both of '
                                                                                         'our wrists.',
                                                                                 'inner_thought': '',
                                                                                 'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                                                                                 'voice_emotion': ''},
                                                                                {'beat_id': 'N39_C22_TRUE_R2',
                                                                                 'speaker': 'Aether',
                                                                                 'text': 'No glass between '
                                                                                         'us, Citlali -- '
                                                                                         'keep your hue '
                                                                                         'knotted to mine '
                                                                                         'for good.',
                                                                                 'inner_thought': '',
                                                                                 'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                                                                                 'voice_emotion': ''}]},
                                                            {'opt_id': 'C22_NEUTRAL_UNCRACKED_SPINE',
                                                             'label': 'Inclining your head with warm '
                                                                      'respect to Great Shaman Ukumbuko, '
                                                                      'promise to drop by whenever your '
                                                                      'travels pass the coast.',
                                                             'effects': {'bond': 0,
                                                                         'insight': 0,
                                                                         'add_flags': []},
                                                             'next_node': 'N42',
                                                             'reaction_beats': [{'beat_id': 'N39_C22_NEUT_R1',
                                                                                 'speaker': 'Narrator',
                                                                                 'text': 'Reading the '
                                                                                         'quiet half-step '
                                                                                         'of reserve '
                                                                                         'between us, '
                                                                                         'Citlali slips '
                                                                                         'her fingertips '
                                                                                         'neatly back '
                                                                                         'inside her wide '
                                                                                         'shamanic sleeves '
                                                                                         'with a composed, '
                                                                                         'wistful smile.',
                                                                                 'inner_thought': '',
                                                                                 'cg': 'ui_assets/story_quest_cgs/citlali/end_neutral_uncracked_spine.jpg',
                                                                                 'voice_emotion': ''},
                                                                                {'beat_id': 'N39_C22_NEUT_R2',
                                                                                 'speaker': 'Aether',
                                                                                 'text': 'Congratulations '
                                                                                         'on inheriting '
                                                                                         'Ukumbuko, '
                                                                                         'Citlali. '
                                                                                         'Whenever the '
                                                                                         'road brings us '
                                                                                         'back to Verona '
                                                                                         'Point, Paimon '
                                                                                         'and I will '
                                                                                         'knock.',
                                                                                 'inner_thought': '',
                                                                                 'cg': 'ui_assets/story_quest_cgs/citlali/end_neutral_uncracked_spine.jpg',
                                                                                 'voice_emotion': ''}]}]},
                                     'routing': []},
           'N40': {'node_id': 'N40',
                   'chapter_id': 'CH5',
                   'title': 'Overturning the Opening Line',
                   'day_label': 'Day 12 - Sunrise',
                   'location': 'Verona Point Headland - Bound in Rose-Lavender',
                   'beats': [{'beat_id': 'N40_B01',
                              'speaker': 'Citlali',
                              'text': "W-What do you think you're doing tying a Great Shaman's wrist in "
                                      'broad daylight, Traveler?! If Mualani or Ororon peeks up from the '
                                      'beach right now--!',
                              'inner_thought': "...don't untie it. Please, whatever you do, don't ever "
                                               'untie it...',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N40_B02',
                              'speaker': 'Aether',
                              'text': 'Your mental voice just betrayed you in record time, Citlali.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B03',
                              'speaker': 'Narrator',
                              'text': 'Looking down at the rose-lavender silk binding our pulses together, '
                                      'Citlali exhales a shaky laugh -- letting her proud posture melt '
                                      'against my arm.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B04_F03',
                              'speaker': 'Citlali',
                              'text': "...Shut up! You read that opening line in 'New Chronicles of the "
                                      "Six Kitsune,' didn't you? For decades I believed every story about "
                                      'memory meant gaining something precious and losing it straight '
                                      'away.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F03_SIX_KITSUNE_VERSE']}},
                             {'beat_id': 'N40_B04_NOF03',
                              'speaker': 'Citlali',
                              'text': "...Shut up! For two hundred dry seasons since Huitzilin's "
                                      'wildflowers faded, I believed letting anyone into my heart meant '
                                      'gaining warmth only to lose it straight away.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F03_SIX_KITSUNE_VERSE']}},
                             {'beat_id': 'N40_B05',
                              'speaker': 'Narrator',
                              'text': 'Bright, unashamed tears catch the sunrise along her lashes as she '
                                      'drops the very last guard across our telepathic bridge -- two '
                                      'centuries of hoarded tenderness pouring through like morning sun.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B06',
                              'speaker': 'Citlali',
                              'text': "Turns out two hundred years doesn't teach you everything after all, "
                                      'Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B07',
                              'speaker': 'Citlali',
                              'text': 'When an immortal star-traveler refuses to let go... some stories '
                                      'about memory are about gaining someone and keeping him forever.',
                              'inner_thought': 'Every single color I am -- take all of it with you, my '
                                               'golden Traveler.',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_01_wrist_ribbon_tears.jpg',
                              'voice_emotion': 'vn_sweet_happy'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N41'}]},
           'N41': {'node_id': 'N41',
                   'chapter_id': 'CH5',
                   'title': 'Until the Stars Diminish',
                   'day_label': 'Day 12 - Radiant Morning',
                   'location': 'Verona Point Headland - Sunrise Horizon',
                   'beats': [{'beat_id': 'N41_B01',
                              'speaker': 'Narrator',
                              'text': 'Interlacing all ten fingers with mine inside the rose-lavender silk '
                                      'knot while Itzpapa and Citlalin float buoyantly in the warm '
                                      'sea-breeze, Citlali steps close and rests her forehead against '
                                      'mine.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_02_eternal_sunrise_vow.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B02_F04',
                              'speaker': 'Aether',
                              'text': "From that first 'Give me your hand' in Smoke-Drift Canyon to every "
                                      'horizon ahead -- my hand is yours, Citlali.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_02_eternal_sunrise_vow.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F04_HAND_PROMISE_GIVEN']}},
                             {'beat_id': 'N41_B02_NOF04',
                              'speaker': 'Aether',
                              'text': 'Across every dry season and every sea of stars ahead -- my hand is '
                                      'yours, Citlali.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_02_eternal_sunrise_vow.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F04_HAND_PROMISE_GIVEN']}},
                             {'beat_id': 'N41_B03',
                              'speaker': 'Narrator',
                              'text': "Above Verona's sparkling surf, two Ancient Names -- Tumaini and "
                                      'Ukumbuko, Hope and Memory -- chime as a single chord.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_02_eternal_sunrise_vow.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B04',
                              'speaker': 'Citlali',
                              'text': 'From this point on, I will always be by your side -- until the '
                                      'stars diminish, the flames die out, and the smoke dissipates into '
                                      'nothing.',
                              'inner_thought': 'Until the stars diminish, the flames die out, and the '
                                               'smoke dissipates into nothing -- I am yours, Aether.',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_02_eternal_sunrise_vow.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N41_B05',
                              'speaker': 'Narrator',
                              'text': 'Spoken aloud into the salt-sweet morning and echoed simultaneously '
                                      'across an unbreakable soul-link, Ukumbuko and Tumaini watch the '
                                      'twelfth sun climb high above a world whose colors will never fade.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_true_02_eternal_sunrise_vow.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_TRUE'},
           'N42': {'node_id': 'N42',
                   'chapter_id': 'CH5',
                   'title': 'The Uncracked Spine',
                   'day_label': 'Day 12 - Clear Morning',
                   'location': 'Verona Cliff Steps - Polite Farewell',
                   'beats': [{'beat_id': 'N42_B01',
                              'speaker': 'Citlali',
                              'text': 'Natlan owes Tumaini yet another debt, Traveler. Thanks to you, the '
                                      'First-Era Chronicle is whole, and the Masters of the Night-Wind '
                                      'finally have a Great Shaman worthy of the name Ukumbuko.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_neutral_uncracked_spine.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N42_B02',
                              'speaker': 'Narrator',
                              'text': 'Deliberately, gently, Citlali dials the volume of our shared '
                                      'telepathic bridge down to a faint, courteous murmur -- sparing both '
                                      'of us the ache of thoughts neither quite dared bridge.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_neutral_uncracked_spine.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B03',
                              'speaker': 'Aether',
                              'text': "Take care of yourself, Citlali -- and don't skip breakfast when you "
                                      'get absorbed in a new chapter.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_neutral_uncracked_spine.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B04',
                              'speaker': 'Citlali',
                              'text': 'Keep the front-door key if you like, alright? Just remember to '
                                      'knock twice before coming in -- a dignified elder has light novels '
                                      'to catch up on.',
                              'inner_thought': '[...faintly, behind closed shutters: safe travels, golden '
                                               'star...]',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_neutral_uncracked_spine.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N42_B05',
                              'speaker': 'Narrator',
                              'text': "Walking down the coastal basalt steps toward Paimon's waiting wave, "
                                      'I glance back once at the cliffside terrace.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_neutral_uncracked_spine.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B06',
                              'speaker': 'Narrator',
                              'text': 'Framed against the bright morning sky clutching Itzpapa, Citlali '
                                      'watches the harbor road in quiet poise.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_neutral_uncracked_spine.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B07',
                              'speaker': 'Narrator',
                              'text': 'Alive, honored, and whole -- yet still preserving her deepest wish '
                                      'uncracked, like the pristine volumes gleaming untouched on her '
                                      'highest shelf.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/citlali/end_neutral_uncracked_spine.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_NEUTRAL'}}}

STORY_QUEST_CAMPAIGNS: list[dict] = [STORY_QUEST_CAMPAIGN]
