"""
Furina de Fontaine 5-Chapter Pure Branching Visual Novel Campaign Pack ("Unscripted Encore")
Subtitle: "Scene 182,377 Beyond the Fountain of Tears"
Target Runtime: C:\\Users\\LENOVO\\Desktop\\GTA\\Project Eagle\\gta sa gameplay-lab
Plug-and-Play Contract: exports `STORY_QUEST_CAMPAIGN` and `STORY_QUEST_CAMPAIGNS` for `StoryQuestEngine`.
"""
from __future__ import annotations

STORY_QUEST_CAMPAIGN: dict = {'char_id': 'furina',
 'ped_id': 49428,
 'display_name': 'Furina de Fontaine',
 'campaign_id': 'furina_sq1_unscripted_encore',
 'title': 'Unscripted Encore',
 'subtitle': 'Scene 182,377 Beyond the Fountain of Tears',
 'version': '2.0.0',
 'theme_rgb': [72, 134, 247],
 'chapters': [{'chapter_id': 'CH1',
               'index': 1,
               'title': 'Chapter 1 -- The Director of Quartier Lyonnais',
               'entry_node': 'N01'},
              {'chapter_id': 'CH2',
               'index': 2,
               'title': 'Chapter 2 -- The Deafened Lutist & The Bare Hatband',
               'entry_node': 'N09'},
              {'chapter_id': 'CH3',
               'index': 3,
               'title': 'Chapter 3 -- Three Roads Around Erinnyes',
               'entry_node': 'N18_A1'},
              {'chapter_id': 'CH4',
               'index': 4,
               'title': 'Chapter 4 -- Two Gates Before the Solstice Tide',
               'entry_node': 'N28_A4'},
              {'chapter_id': 'CH5',
               'index': 5,
               'title': 'Chapter 5 -- Scene 182,377: Unscripted Encore',
               'entry_node': 'N36_CH5_CONVERGE'}],
 'initial_state': {'bond': 0, 'insight': 0, 'flags': []},
 'flag_catalog': {'F01_TEAR_RIME_CHILL': {'title': 'Tear-Rime Pulse Chill',
                                          'clue_hint': 'Felt an unnatural sub-zero chill numbing only '
                                                       "Furina's Vision-attuned right wrist on Day 1."},
                  'F02_MACARONI_RULE': {'title': 'Quartier Lyonnais House Rule',
                                        'clue_hint': "Kept Furina's midnight kitchen rule: savory first, "
                                                     'sweet to close -- never leave without sweetness.'},
                  'F03_LUCINE_CONDUIT': {'title': 'Erinnyes Solstice Conduit Lore',
                                         'clue_hint': 'Learned from Neuvillette how the sunken Erinnyes '
                                                      "cistern phase-locks to Night Nine's 11:00 PM "
                                                      'Solstice tide.'},
                  'F04_ROOFTOP_ENCORE': {'title': 'Outer Seawall Encore Pact',
                                         'clue_hint': 'Shook hands on the Outer Seawall: neither lead '
                                                      'actor ever takes a final bow while the other stays '
                                                      'behind.'},
                  'F05_LUTIST_SCORE': {'title': "Maitre Renaud's Deafened Draft",
                                       'clue_hint': "Found Renaud's brass ear-trumpet and 50-year-old "
                                                    "draft warning that soloing Act IV's Cadenza destroys "
                                                    'hearing and voice.'},
                  'F06_HARMONICA_MERCY': {'title': 'Clementine Dock Harmonica Mercy',
                                          'clue_hint': "Revealed Renaud's brass harmonica inside the lute "
                                                       'case to Celine without breaking his proud '
                                                       "teacher's promise."},
                  'F07_SAPPHIRE_PIN': {'title': "L'Etoile d'Eau (Sapphire Star Pin)",
                                       'clue_hint': "Carries Furina's Hydro-Vision-attuned sapphire-plume "
                                                    'star pin entrusted until her curtain call.'},
                  'F08_CRYSTAL_TEAR_SEEN': {'title': 'Crystal Tear-Rime Handkerchief',
                                            'clue_hint': 'Caught Furina behind the Opera wing-curtain '
                                                         'coughing frozen salt-tear rime onto white lace.'},
                  'F09_COSTAR_VOW': {'title': 'Mortal Co-Star Vow',
                                     'clue_hint': 'Crossed the burning Indemnitium footlights to stand on '
                                                  "the mirror-stage as Furina's mortal co-star."},
                  'F10_BLANK_TUNING_CRYSTAL': {'title': 'Blank Descender Tuning Quartz',
                                               'clue_hint': "Kept Freminet's uncalibrated Ley-Line quartz "
                                                            "prism attuned to the Fourth Descender's "
                                                            'unrecorded soul.'},
                  'F11_SUGAR_TIN_CLUE': {'title': 'Five Sugar Wrappers & Tea-Tin Note',
                                         'clue_hint': "Spotted five empty Demerara packets and Furina's "
                                                      "own margin note on Sigewinne's tin hiding her lost "
                                                      'sense of sweetness.'},
                  'F12_SLUICE_CADENCE': {'title': 'Marcotte Sluice-Valve Cadence',
                                         'clue_hint': 'Mastered the 12-second backflow window of Erinnyes '
                                                      'Sluice-Valve Seven alongside Clorinde and Spina di '
                                                      'Rosula.'}},
 'endings': {'END_TRUE': {'rank': 'TRUE ENDING',
                          'title': 'Unscripted Encore for Two',
                          'summary': 'Grounding 500 years of crystal tears together and retiring Seat '
                                     "Number One forever, Aether pins L'Etoile d'Eau back onto Furina's "
                                     "hat while she pins Chiori's Twin Plumes over his heart beneath "
                                     "Lucine's midnight stars."},
             'END_GOOD': {'rank': 'GOOD ENDING',
                          'title': 'Intermission Under Winter Glass',
                          'summary': "Locking the Serenitea Pot at 8:00 PM spares Furina's voice while "
                                     'Neuvillette seals the Opera Epiclese under ninety days of winter ice '
                                     '-- buying warm snowy mornings over hot macaroni to solve the cistern '
                                     'before the Spring Equinox.'},
             'END_NEUTRAL': {'rank': 'NEUTRAL ENDING',
                             'title': 'Standing Ovation from Seat Number One',
                             'summary': "Erinnyes's five-hundred-year tear cistern is cleansed and "
                                        "Furina's sweetness and voice shine whole at the Gala premiere, "
                                        'yet half a velvet railing keeps Aether applauding fondly from '
                                        'Seat Number One.'},
             'END_BAD_1': {'rank': 'BAD ENDING I',
                           'title': 'Seat Number One, Empty Stage',
                           'summary': 'Stepping back at the footlights fractures their resonance; '
                                      'Neuvillette freezes the Opera House for ninety winter days, and '
                                      'Furina boards a rainy Lumidouce steamer north behind a proud navy '
                                      'silk parasol.'},
             'END_BAD_2': {'rank': 'BAD ENDING II',
                           'title': 'The Girl Who Forgot the Rain',
                           'summary': "Locked outside the 10:55 PM Hydro-Curtain, Focalors' Gentle Veil of "
                                      'Oblivion washes every private memory since Scene 182,376 into '
                                      "Lucine to save Furina's life -- leaving one warm, unexplainable "
                                      'tear when they meet in sun-shower mist.'}},
 'nodes': {'N01': {'node_id': 'N01',
                   'chapter_id': 'CH1',
                   'title': 'Midnight by the Fountain of Tears',
                   'day_label': 'Day 1 - 00:45 AM (Erinnyes Island)',
                   'location': 'Fountain of Lucine - Moonlit Plaza',
                   'beats': [{'beat_id': 'N01_B01',
                              'speaker': 'Narrator',
                              'text': 'Past midnight on Erinnyes Island, the last rehearsal lamps of the '
                                      'Opera Epiclese dim behind silver mist, leaving only the hush of the '
                                      'Fountain of Lucine under a winter moon.',
                              'inner_thought': 'Twelve days until the Fontinalia Centennial Gala, yet the '
                                               'marble underfoot hums like an overtightened cello string.',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_midnight_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B02',
                              'speaker': 'Narrator',
                              'text': "Standing alone beside the basin's carved balustrade is a familiar "
                                      'small silhouette in navy and white -- sapphire-plume star pin '
                                      'glinting on her top hat as she listens to the falling water.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_midnight_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B03',
                              'speaker': 'Furina',
                              'text': 'Ahem! Who goes creeping across Erinnyes at a quarter to one?! Oh -- '
                                      'it is only you, Aether. Do try to announce your entrance before '
                                      "startling Fontaine's busiest stage director!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_midnight_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N01_B04',
                              'speaker': 'Aether',
                              'text': 'The Navia Line watchman mentioned the Gala crew was still testing '
                                      'the new Pneumousia Grand Organ inside the Opera House. Paimon fell '
                                      'asleep back at Hotel Debord, so I came to walk you back.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_midnight_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B05',
                              'speaker': 'Furina',
                              'text': 'Hmph. As if a seasoned director requires an escort across her own '
                                      'plaza! Though... I suppose the organ tuners have been dragging that '
                                      'lowest bass pedal rather dreadfully tonight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_midnight_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N01_B06',
                              'speaker': 'Narrator',
                              'text': 'At that exact heartbeat, a subterranean sub-bass chord booms from '
                                      "beneath the Opera Epiclese's foundation. Down in the darkness, an "
                                      'ancient mineral seal cracks with a sound like snapping glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_midnight_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B07',
                              'speaker': 'Narrator',
                              'text': 'Frost-white mist laced with jagged blue Indemnitium dust erupts '
                                      "straight out of the bronze drainage grate beneath Furina's heels, "
                                      'lashing upward toward her throat with five centuries of compressed '
                                      'grief!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_midnight_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B08',
                              'speaker': 'Aether',
                              'text': 'Furina -- get behind me!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_midnight_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B09',
                              'speaker': 'Narrator',
                              'text': 'I haul her back by the shoulder and drive my bare left palm '
                                      'straight into the rising geyser. The psychic tear-surge expects a '
                                      "native mind bound to Teyvat's Ley Lines -- instead it strikes a "
                                      'vessel from beyond the stars.',
                              'inner_thought': 'Golden starlight flares through my channels, dispersing '
                                               'the crystallized sorrow before a drop can reach my organs.',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_midnight_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B10',
                              'speaker': 'Narrator',
                              'text': 'Within three breaths the plaza air turns clear again. My lungs and '
                                      'heart remain completely unharmed, yet a piercing crystalline ring '
                                      'slices through my left ear and drains the strength clean out of my '
                                      'knees.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_kneel_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B11',
                              'speaker': 'Furina',
                              'text': 'Aether?! Hey -- look at me, do not dare close your eyes on cold '
                                      'stone! Surintendante Chevalmarin! Gentilhomme Usher! Help me lift '
                                      'his shoulders at once!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_kneel_diff.jpg',
                              'voice_emotion': 'outing_bump_rescue'},
                             {'beat_id': 'N01_B12',
                              'speaker': 'Narrator',
                              'text': 'Through the high glass chime ringing in my left ear, two luminous '
                                      "Hydro companions steady my arms while Furina hails the Opera crew's "
                                      'late-night charter boat waiting at the Navia Line pier.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_kneel_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_E1',
                              'speaker': 'Furina',
                              'text': 'Hold onto my shoulder and step onto the aquabus deck -- carefully! '
                                      'Honestly, throwing your bare palm into an unknown geyser without '
                                      'even drawing a sword... are all outlanders born without '
                                      'self-preservation?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_kneel_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_E2',
                              'speaker': 'Aether',
                              'text': 'If that frost-mist had hit your throat instead of my palm, '
                                      "Fontaine's Gala Director would be whispering in sign language "
                                      'tomorrow.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_kneel_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_E3',
                              'speaker': 'Furina',
                              'text': '...Hmph. Even half-dizzy on a midnight boat, you still know exactly '
                                      'which line disarms me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_kneel_diff.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N01_E4',
                              'speaker': 'Narrator',
                              'text': 'Across the dark Terrestrial Sea, Mademoiselle Crabaletta stands '
                                      'vigilant on the prow while Furina keeps one steady arm braced '
                                      'behind my back all the way into harbor.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_kneel_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B13',
                              'speaker': 'Narrator',
                              'text': 'Once we cross the dark inland sea back into the Court of Fontaine, '
                                      'she presses a handwritten note into the hands of a Melusine '
                                      'night-patrol officer bound for Hotel Debord -- refusing to leave me '
                                      'alone until we reach Quartier Lyonnais.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lucine_kneel_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N02'}],
                   'ending_id': None},
           'N02': {'node_id': 'N02',
                   'chapter_id': 'CH1',
                   'title': 'Chaise Longue & Velvet Curtains',
                   'day_label': 'Day 2 - 08:30 AM',
                   'location': "Quartier Lyonnais - Furina's Ground-Floor Apartment",
                   'beats': [{'beat_id': 'N02_B01',
                              'speaker': 'Narrator',
                              'text': 'Morning sunlight filters through blue velvet drapes onto a plush '
                                      'chaise longue. The crystalline ringing in my left ear has faded to '
                                      'a dull hum, replaced by the smell of fresh brioche and Paimon '
                                      'hovering two inches from my nose.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B02',
                              'speaker': 'Paimon',
                              'text': "Aether, you are awake! Officer Sedene brought Furina's note to "
                                      'Hotel Debord at dawn and Paimon flew straight over! How is your '
                                      'left ear? Can you count how many fingers Paimon is holding up?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B03',
                              'speaker': 'Aether',
                              'text': 'Loud and clear, Paimon -- especially at that volume. My stamina '
                                      'already came back overnight; it was only acoustic shock, nothing '
                                      'poisonous.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B04',
                              'speaker': 'Furina',
                              'text': 'Ahem! Naturally you recovered in record time -- you were resting '
                                      'upon the finest chaise longue in Quartier Lyonnais under '
                                      "Mademoiselle Crabaletta's personal supervision!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N02_B04B',
                              'speaker': 'Narrator',
                              'text': 'As if on cue, a tiny sapphire crab familiar perched atop the '
                                      'armrest clicks one pincer proudly and adjusts the corner of my '
                                      'pillow by half an inch.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B05',
                              'speaker': 'Narrator',
                              'text': 'Hatless in a cream-and-sapphire indoor blouse, Furina stands beside '
                                      'the tea table with faint violet shadows of a sleepless night under '
                                      'her mismatched eyes, though she lifts her chin like an empress.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B05B',
                              'speaker': 'Aether',
                              'text': 'Four empty teacups beside the lamp, Furina -- you sat up in that '
                                      'armchair watching over me until sunrise, did you not?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B05C',
                              'speaker': 'Furina',
                              'text': "Preposterous! I was merely red-inking Act Two's atrocious lighting "
                                      'cues while the apartment happened to be quiet! Do not flatter '
                                      'yourself, my dear guest!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N02_E1',
                              'speaker': 'Paimon',
                              'text': "Ooh, look at the sideboard -- fresh almond brioche from Louis's "
                                      'stall AND wild berry jam! Furina must have sprinted out to the '
                                      'bakery before the morning bell even rang!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_E2',
                              'speaker': 'Furina',
                              'text': "A brisk morning constitutional stimulates a director's blocking "
                                      'imagination, Paimon! That jam happened to be on discount!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N02_E3',
                              'speaker': 'Aether',
                              'text': 'Louis never discounts wild berry jam during Fontinalia week, '
                                      'Furina.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_E4',
                              'speaker': 'Furina',
                              'text': 'Eat your brioche before Gentilhomme Usher confiscates the butter '
                                      'knife, you overly informed Traveler!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B06',
                              'speaker': 'Narrator',
                              'text': 'Pretending merely to straighten the wool blanket, she reaches down '
                                      'to brush the back of her bare right hand across my forehead -- then '
                                      'tries to tuck that right wrist quickly back inside her lace cuff.',
                              'inner_thought': 'Wait -- the skin brushing my brow felt colder than river '
                                               'ice.',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C01',
                              'prompt': 'Furina starts to draw her bare right wrist back into her lace '
                                        'sleeve before you can notice its chill.',
                              'options': [{'opt_id': 'C01_A',
                                           'label': 'Catch her right wrist gently before she hides it and '
                                                    'check why her pulse feels ice-cold.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F01_TEAR_RIME_CHILL']},
                                           'next_node': 'N03',
                                           'reaction_beats': [{'beat_id': 'N02_C01A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Before she can slip away, I close '
                                                                       'my fingers lightly around her '
                                                                       'right wrist. Against my palm, her '
                                                                       'pulse beats beneath a faint '
                                                                       'powdery sheen like sea-salt frost '
                                                                       '-- while her left hand holding the '
                                                                       'saucer is perfectly warm.',
                                                               'inner_thought': 'Clue Recorded [Lucine '
                                                                                'Rime Chill]: Only her '
                                                                                'right wrist carries a '
                                                                                'crystalline salt-chill '
                                                                                "from last night's grate.",
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_wrist_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N02_C01A_R2',
                                                               'speaker': 'Furina',
                                                               'text': 'Eh?! W-What is the meaning of '
                                                                       "seizing your hostess's hand before "
                                                                       'breakfast?! Some of us simply have '
                                                                       'delicate circulation in winter -- '
                                                                       'release the director at once!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_wrist_diff.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C01_B',
                                           'label': 'Play along warmly with her regal hostess act and '
                                                    'thank her for sitting up beside the settee all night.',
                                           'effects': {'bond': 2, 'insight': 1, 'add_flags': []},
                                           'next_node': 'N03',
                                           'reaction_beats': [{'beat_id': 'N02_C01B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'My deepest gratitude to the Lady '
                                                                       'of Quartier Lyonnais -- and to '
                                                                       'whoever tucked a second wool '
                                                                       'blanket around my shoulders at '
                                                                       'four in the morning.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N02_C01B_R2',
                                                               'speaker': 'Furina',
                                                               'text': 'Hehe... well, a proper director '
                                                                       'never neglects her lead stagehand! '
                                                                       'Drink your hot lemon water while I '
                                                                       'still feel charitable!',
                                                               'inner_thought': 'Even as she beams, she '
                                                                                'tucks her right hand '
                                                                                'carefully into her sleeve '
                                                                                'away from the warm '
                                                                                'teapot.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N03': {'node_id': 'N03',
                   'chapter_id': 'CH1',
                   'title': 'The Torn Fourth Act of Erinnyes',
                   'day_label': 'Day 2 Afternoon to Day 3 Evening',
                   'location': 'Quartier Lyonnais - Parlor Script Table',
                   'beats': [{'beat_id': 'N03_B01',
                              'speaker': 'Narrator',
                              'text': 'That afternoon, a cheerful knock rattles the front door, admitting '
                                      'Navia with a three-tiered tower of Fontinalia macarons, Clorinde '
                                      'carrying rehearsal schedules, and Charlotte brandishing a stack of '
                                      'press badges.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B02',
                              'speaker': 'Navia',
                              'text': 'Thank goodness your ears are in one piece, partner! Once Sedene '
                                      'told us about that burst pipe at Lucine, Clorinde had the Maison '
                                      "cordon off the grate -- and Charlotte and I brought Paimon's "
                                      'official festival badge!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B03',
                              'speaker': 'Charlotte',
                              'text': "Behold: Honorary Chief Dessert-Stall Critic for The Steambird's "
                                      'Fontinalia Centennial Issue! Every daytime booth on Vasari Passage '
                                      'plus nightly bake-off tastings down in Poisson with Spina di '
                                      'Rosula!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B04',
                              'speaker': 'Paimon',
                              'text': 'Nightly pastry bake-offs in Poisson?! Aether, now that Paimon has '
                                      'verified your ears work fine, Paimon will uphold journalistic '
                                      'integrity with every ounce of stomach space she has!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B05',
                              'speaker': 'Clorinde',
                              'text': 'Which leaves one practical matter. Furina is directing the '
                                      "Centennial Gala Finale at eleven o'clock on Night Nine, and her "
                                      'late-night score revisions run past midnight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B06',
                              'speaker': 'Furina',
                              'text': 'Ahem! What Clorinde means to say is that I am reviving a '
                                      "fifty-year-old French grand opera titled 'La Derniere Vaguelette' "
                                      '-- adapted from a wordless Erinnyes stone canticle whose fourth act '
                                      'was mysteriously torn out!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N03_B07',
                              'speaker': 'Furina',
                              'text': 'And -- strictly for workflow efficiency, mind you, NOT because the '
                                      'hallway water pipes make eerie groaning noises after dark -- I '
                                      'hereby appoint Aether my Live-In Script Editor and Night Guard on '
                                      'that chaise longue!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N03_B08',
                              'speaker': 'Aether',
                              'text': 'Live-in Night Guard it is. Between blocking rehearsals by day and '
                                      'reconstructing a missing fourth act by night, you will not hear a '
                                      'single pipe groan on my watch.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_E1',
                              'speaker': 'Navia',
                              'text': 'Between you and me, partner, Furina turned down three Maison '
                                      "Gardiennage sentries this morning -- insisting only 'someone with "
                                      "theatrical sensibility' was allowed in her parlor!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_E2',
                              'speaker': 'Clorinde',
                              'text': 'Which translated into your name before I finished my first cup of '
                                      'coffee. Keep an eye on her tea kettle at night, Aether; she forgets '
                                      'to sleep when an act is unfinished.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_E3',
                              'speaker': 'Furina',
                              'text': 'I can hear every word from behind the script binder, ladies! Off to '
                                      'Poisson with your pastry badges -- my editor and I have serious '
                                      'musical history to reconstruct!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N03_E4',
                              'speaker': 'Narrator',
                              'text': 'Once the parlor grows quiet at dusk, Furina curls her feet onto the '
                                      'settee opposite mine, humming counter-melodies under her breath '
                                      'while lamplight gilds her white-and-blue curls.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B09',
                              'speaker': 'Narrator',
                              'text': 'So begins a lively two-day routine: mornings ferrying props across '
                                      'the Navia Line, afternoons watching Furina coach young chorus '
                                      'singers with dazzling precision, and quiet evenings back in her '
                                      'parlor.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_lyonnais_morning_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N04'}],
                   'ending_id': None},
           'N04': {'node_id': 'N04',
                   'chapter_id': 'CH1',
                   'title': 'Midnight Macaroni & The Crossed-Out Tea Label',
                   'day_label': 'Day 3 - 11:45 PM',
                   'location': 'Quartier Lyonnais - Kitchen',
                   'beats': [{'beat_id': 'N04_B01',
                              'speaker': 'Narrator',
                              'text': 'By a quarter to midnight on my third night in Quartier Lyonnais, '
                                      'rain patters softly against the kitchen shutter while sweet basil '
                                      'and simmering tomato cream fill the warm amber room.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B02',
                              'speaker': 'Narrator',
                              'text': 'Wearing a white lace-trimmed apron over her indoor dress, Furina '
                                      'stirs a copper saucepan with practiced concentration -- her comfort '
                                      'dish from the earliest weeks of living as an ordinary human.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B03',
                              'speaker': 'Furina',
                              'text': 'Hehe, do not underestimate macaroni a la Lyonnais! When one has '
                                      'spent five hours arguing tempo with tenors, gourmet banquets cannot '
                                      'hold a candle to honest tomato sauce and grated cheese!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N04_B03B',
                              'speaker': 'Aether',
                              'text': 'Coming from the chef who once asked Paimon whether boiling water '
                                      'needed seasoning, this smells worthy of Hotel Debord. Here -- let '
                                      'me grate the aged Marcotte cheese before the steam escapes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B03C',
                              'speaker': 'Furina',
                              'text': 'Hmph! Everyone starts somewhere in the culinary arts! Stand half a '
                                      'step closer with the grater, Assistant -- and mind you do not '
                                      'splash red sauce on my lace apron!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N04_E1',
                              'speaker': 'Narrator',
                              'text': 'Outside in the narrow courtyard lane, a late-night accordionist '
                                      'plays an old Fontainian waltz that drifts faintly through the '
                                      'rain-dappled glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_E2',
                              'speaker': 'Furina',
                              'text': 'In the Palais, twelve chefs plated cold aspics under silver domes '
                                      'five yards down a silent table. Nowadays, when sauce bubbles on '
                                      'this little stove, the whole room feels alive.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N04_E3',
                              'speaker': 'Aether',
                              'text': 'Especially with Surintendante Chevalmarin guarding the pepper mill '
                                      'like a royal scepter.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_E4',
                              'speaker': 'Furina',
                              'text': 'Naturally! Proper seasoning is half of civilization!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B04',
                              'speaker': 'Narrator',
                              'text': 'She ladles two generous bowls onto the table beside a plate of '
                                      'almond-cream petit fours, then turns toward the copper sink to '
                                      'rinse the saucepan.',
                              'inner_thought': 'Beside the kettle sits a routine herbal throat-tea tin '
                                               'from Sigewinne -- and five empty brown-sugar wrappers.',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C02',
                              'prompt': 'While Furina rinses the copper pot, steam rises from the bowls '
                                        'beside the cluttered tea tray.',
                              'options': [{'opt_id': 'C02_A',
                                           'label': 'Split the last spoonful of rich tomato-cream sauce '
                                                    'onto her plate and toast her midnight cooking.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F02_MACARONI_RULE']},
                                           'next_node': 'N05',
                                           'reaction_beats': [{'beat_id': 'N04_C02A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'I spoon the richest golden-red '
                                                                       'glaze back onto her bowl and push '
                                                                       'the plate of almond petit fours '
                                                                       'within easy reach between us. '
                                                                       'Furina turns around, blinking '
                                                                       'before beaming with theatrical '
                                                                       'ceremony.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_rule_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02A_R2',
                                                               'speaker': 'Furina',
                                                               'text': 'Ahem! Listen well and engrave our '
                                                                       'solemn house rule upon memory: '
                                                                       "'Savory first, sweet to close -- "
                                                                       "nobody leaves Furina de Fontaine's "
                                                                       'table without sweetness on their '
                                                                       "tongue!'",
                                                               'inner_thought': 'Memory Anchored [Quartier '
                                                                                'Lyonnais House Rule]: '
                                                                                'Savory first, sweet to '
                                                                                'close.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_rule_diff.jpg',
                                                               'voice_emotion': 'vn_playful_tease'}]},
                                          {'opt_id': 'C02_B',
                                           'label': 'Glance closer at the five empty Demerara sugar '
                                                    'packets and the handwriting on her throat-tea tin.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F11_SUGAR_TIN_CLUE']},
                                           'next_node': 'N05',
                                           'reaction_beats': [{'beat_id': 'N04_C02B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Beside a cold teacup thick as '
                                                                       'amber syrup lie five torn Demerara '
                                                                       'sugar packets. On the paper label '
                                                                       "of Sigewinne's routine soothing "
                                                                       "throat-tea tin, Furina's own "
                                                                       'fountain pen has scribbled '
                                                                       'frantic, crossed-out notes.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02B_R2',
                                                               'speaker': 'Narrator',
                                                               'text': "'Fifth brown-sugar packet -- why "
                                                                       'does it still taste like plain '
                                                                       'boiled water?! Right fingertips '
                                                                       'numb since the Lucine grate. DO '
                                                                       'NOT mention to Sigewinne or '
                                                                       'Monsieur Neuvillette before Gala '
                                                                       "Night!!'",
                                                               'inner_thought': 'Clue Recorded [Hidden '
                                                                                'Sweet-Taste Numbness]: '
                                                                                'Sub-stage mist numbed her '
                                                                                'sweet taste, and she is '
                                                                                'hiding it from everyone.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_kitchen_macaroni_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N05': {'node_id': 'N05',
                   'chapter_id': 'CH1',
                   'title': 'Matinee Tea at Cafe Lutece',
                   'day_label': 'Day 4 - 01:15 PM',
                   'location': 'Court of Fontaine - Cafe Lutece Terrace',
                   'beats': [{'beat_id': 'N05_B01',
                              'speaker': 'Narrator',
                              'text': 'At midday on Day Four, pale winter sunshine warms the striped '
                                      'awnings of Cafe Lutece, where Paimon rejoins us between Vasari '
                                      'pastry stalls alongside Lyney, Lynette, and Freminet.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B02',
                              'speaker': 'Paimon',
                              'text': "Lyney's troupe is performing the Gala opening illusion! Though "
                                      'Paimon has to report that Furina barely touched her strawberry tart '
                                      '-- normally she guards the berry glaze like dragon treasure!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B03',
                              'speaker': 'Lyney',
                              'text': 'A magician notices hands before faces, Lady Furina. All lunch you '
                                      'have lifted your porcelain cup with your left hand while keeping '
                                      'your gloved right fingers completely still on your lap.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B04',
                              'speaker': 'Furina',
                              'text': 'Hmph! Merely resting my baton-conducting wrist prior to evening '
                                      'rehearsals, Monsieur Lyney! Not every gesture is a sleight-of-hand '
                                      'cue!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N05_B05',
                              'speaker': 'Lynette',
                              'text': 'Deception probability: seventy-eight percent. Sipping tea...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B05B',
                              'speaker': 'Narrator',
                              'text': 'With a practiced flick of his wrist, Lyney produces a fresh Rainbow '
                                      "Rose from behind Paimon's ear -- smoothly steering cafe chatter "
                                      "away from Furina's untouched berry tart before she feels cornered.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B05C',
                              'speaker': 'Aether',
                              'text': 'Appreciate the cover, Lyney. Have the three of you noticed anything '
                                      'unusual out on Erinnyes Island during stage load-in?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B06',
                              'speaker': 'Freminet',
                              'text': 'Um... if you are rehearsing inside the Opera Epiclese, please be '
                                      'careful near the orchestra pit. When I dove beneath Erinnyes '
                                      "Island's foundation piers this morning, my brass helmet picked up a "
                                      'strange sound.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_E1',
                              'speaker': 'Paimon',
                              'text': 'Wait a second -- Furina just slid the candied strawberry right off '
                                      "her tart onto Paimon's saucer! Are you coming down with a winter "
                                      'cold, Furina?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_E2',
                              'speaker': 'Furina',
                              'text': 'Nonsense! A generous patron of the culinary press merely rewards '
                                      'her hardest-working critic! Eat up before the meringue loses its '
                                      'crispness!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': 'outing_arrive_photo'},
                             {'beat_id': 'N05_E3',
                              'speaker': 'Lyney',
                              'text': "Smoothly deflected, my lady -- though Aether's eyes did not buy a "
                                      'syllable of it.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_E4',
                              'speaker': 'Narrator',
                              'text': 'Beneath the table linen, Furina flexes her gloved right fingers '
                                      'once against her knee, testing sensation she refuses to admit is '
                                      'fading.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B07',
                              'speaker': 'Freminet',
                              'text': 'Deep behind the sealed aqueduct stone, the water was singing in a '
                                      'low minor chord -- like thousands of old tears vibrating inside '
                                      'crystal pipes.',
                              'inner_thought': 'Freminet heard singing crystal pipes directly beneath the '
                                               'Opera House foundation.',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N06'}],
                   'ending_id': None},
           'N06': {'node_id': 'N06',
                   'chapter_id': 'CH1',
                   'title': "Rain Against Palais Mermonia's Glass",
                   'day_label': 'Day 4 - 04:45 PM',
                   'location': 'Palais Mermonia - Office of the Iudex',
                   'beats': [{'beat_id': 'N06_B01',
                              'speaker': 'Narrator',
                              'text': 'Late that afternoon, while Furina stops by a Vasari printshop to '
                                      'approve Gala posters, a sudden silver shower sweeps across the '
                                      "Court as I step into Monsieur Neuvillette's high-arched office.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B02',
                              'speaker': 'Neuvillette',
                              'text': 'Thank you for coming, Aether. Ever since Sedene reported the '
                                      'midnight mist burst at the Fountain of Lucine, I have been '
                                      'reviewing pre-Masquerade engineering surveys of Erinnyes Island.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B03',
                              'speaker': 'Neuvillette',
                              'text': 'Now that Fontainians possess true human blood, Primordial seawater '
                                      'poses them no threat. Yet something far more personal sleeps '
                                      "beneath the Opera Epiclese's orchestra pit.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B04',
                              'speaker': 'Aether',
                              'text': 'Freminet mentioned hearing a low minor chord singing inside crystal '
                                      "pipes under Erinnyes Island this morning -- and Furina's right hand "
                                      'has been icy since Night One.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_E1',
                              'speaker': 'Narrator',
                              'text': 'Monsieur Neuvillette pours two crystal tumblers of cool spring '
                                      'water from Chenyu Vale, his cane resting silently beside a stack of '
                                      'centuries-old Erinnyes stone rubbings.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_E2',
                              'speaker': 'Neuvillette',
                              'text': 'For five hundred years, every citizen in that opera house applauded '
                                      "Lady Furina's performance without dreaming what each curtain cost "
                                      'her behind closed doors.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_E3',
                              'speaker': 'Aether',
                              'text': 'She will not ask Palais Mermonia for help if she thinks canceling '
                                      'the Gala would disappoint the people.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_E4',
                              'speaker': 'Neuvillette',
                              'text': 'Precisely why I am speaking to you, Aether. Before me she still '
                                      'stands on ceremony as a former colleague of state; beside you, she '
                                      'remembers she is allowed to be human.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B05',
                              'speaker': 'Neuvillette',
                              'text': 'Then the resonance has already reached her mortal nerves. Five '
                                      'centuries of solitary duty do not vanish from stone overnight '
                                      'simply because the trial ended, Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C03',
                              'prompt': "Rain streaks the tall stained glass behind Neuvillette's desk "
                                        'lined with ancient Erinnyes surveys.',
                              'options': [{'opt_id': 'C03_A',
                                           'label': 'Ask Neuvillette directly about the subterranean '
                                                    'chamber beneath the pit and why unplugging the organ '
                                                    'will not stop it.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F03_LUCINE_CONDUIT']},
                                           'next_node': 'N07',
                                           'reaction_beats': [{'beat_id': 'N06_C03A_R1',
                                                               'speaker': 'Neuvillette',
                                                               'text': 'Beneath the pit lies the Erinnyes '
                                                                       'Acoustic Cistern, lined with '
                                                                       'discarded Indemnitium crystal. For '
                                                                       'five hundred years -- 182,375 '
                                                                       "nights -- Lady Furina's silent "
                                                                       'tears flowed into Lucine and '
                                                                       'crystallized there.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03A_R2',
                                                               'speaker': 'Neuvillette',
                                                               'text': "Worse, Night One's bass test "
                                                                       'fractured its containment seal, '
                                                                       'coupling the cistern irreversibly '
                                                                       'to the natural Fontinalia Solstice '
                                                                       'Hydro-Tide peaking at eleven '
                                                                       "o'clock on Night Nine -- even if "
                                                                       'the Grand Organ is unplugged '
                                                                       'completely.',
                                                               'inner_thought': 'Clue Recorded [Erinnyes '
                                                                                'Conduit]: Unplugging the '
                                                                                'organ cannot stop the '
                                                                                '23:00 Night 9 Solstice '
                                                                                'surge; it needs '
                                                                                'phase-cancellation.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C03_B',
                                           'label': 'Ask Neuvillette how Furina has truly adjusted to '
                                                    'quiet mortal life over these past months, promising '
                                                    'to guard her pride.',
                                           'effects': {'bond': 2, 'insight': 1, 'add_flags': []},
                                           'next_node': 'N07',
                                           'reaction_beats': [{'beat_id': 'N06_C03B_R1',
                                                               'speaker': 'Neuvillette',
                                                               'text': 'She laughs more freely now than in '
                                                                       'five centuries upon the throne, '
                                                                       'Aether -- yet whenever something '
                                                                       'threatens those she cares for, she '
                                                                       'still reaches instinctively for '
                                                                       'her solitary mask.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03B_R2',
                                                               'speaker': 'Neuvillette',
                                                               'text': 'My Dragon Sovereign aura flattens '
                                                                       'surface water whenever I approach '
                                                                       'Lucine, causing the deeper echoes '
                                                                       'beneath the Opera House to hide '
                                                                       'from my inspection. Please stay '
                                                                       'close to her before Night Nine.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_palais_cafe_day_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N07': {'node_id': 'N07',
                   'chapter_id': 'CH1',
                   'title': 'Shared Umbrella Along Vasari Passage',
                   'day_label': 'Day 4 - 08:30 PM',
                   'location': 'Upper Vasari Passage -> Outer Seawall Rampart',
                   'beats': [{'beat_id': 'N07_B01',
                              'speaker': 'Narrator',
                              'text': "By half past eight, Neuvillette's rain softens to a silver mist. "
                                      'Under a single navy Fontainian umbrella, Furina walks close beside '
                                      'my shoulder along the lamplit flagstones of Vasari Passage.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B02',
                              'speaker': 'Furina',
                              'text': 'Hold the handle half an inch lower on my left, Assistant! If '
                                      "evening dampness frizzes my curls before tomorrow's music-hall "
                                      'call, the critics will be merciless!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N07_B02B',
                              'speaker': 'Aether',
                              'text': 'Half an inch lower on your side leaves my right shoulder out in the '
                                      'drizzle, Director.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B02C',
                              'speaker': 'Furina',
                              'text': 'Oh! Well -- walk half a step closer then, silly! One umbrella is '
                                      'perfectly wide enough when two people stop standing like courtroom '
                                      'statues!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N07_B02D',
                              'speaker': 'Narrator',
                              'text': 'Warm amber light from closing patisseries reflects across the wet '
                                      'cobbles as her shoulder settles lightly against my upper arm. For '
                                      'two quiet blocks, neither of us hurries.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B02E',
                              'speaker': 'Furina',
                              'text': '...For five hundred years, I used to watch couples share umbrellas '
                                      'down this lane from the high gallery of Palais Mermonia. Walking '
                                      'down here in ordinary shoes still feels like sneaking into a dream.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N07_B03',
                              'speaker': 'Narrator',
                              'text': 'Instead of turning down the stepped lane toward her ground-floor '
                                      'apartment in Quartier Lyonnais, she tugs my sleeve up the stone '
                                      'rampart to the high Outer Seawall Overlook above the inland sea.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_E1',
                              'speaker': 'Furina',
                              'text': "Look at that toy-maker's window on the corner -- tiny clockwork "
                                      'dancers spinning inside a glass music box. When I was newly '
                                      'awakened, I thought the whole city was a stage built like that.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_E2',
                              'speaker': 'Aether',
                              'text': 'And now that you stepped outside the glass box?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_E3',
                              'speaker': 'Furina',
                              'text': 'Now the cobblestones splash mud on my heels and the wind tangles my '
                                      'ribbons... and I would not trade a single puddle of it back.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N07_E4',
                              'speaker': 'Narrator',
                              'text': 'Her quiet laugh warms the chill under our shared umbrella all the '
                                      'way up the stone steps to the seawall.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B04',
                              'speaker': 'Narrator',
                              'text': 'From the elevated parapet, the view opens unbroken in two '
                                      'directions: eastward across dark water to the glowing dome of the '
                                      'Opera Epiclese on Erinnyes, and southwest past the waterfall cliffs '
                                      'toward distant Natlan.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N08'}],
                   'ending_id': None},
           'N08': {'node_id': 'N08',
                   'chapter_id': 'CH1',
                   'title': 'Overlook Above the Terrestrial Sea',
                   'day_label': 'Day 4 - 10:15 PM',
                   'location': 'Court of Fontaine - High Outer Seawall Overlook',
                   'beats': [{'beat_id': 'N08_B01',
                              'speaker': 'Narrator',
                              'text': "Night wind stirs the sapphire-plume star pin on Furina's hatband as "
                                      'she rests her white-gloved hands on the wet stone balustrade, '
                                      'gazing out toward the southwestern horizon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B02',
                              'speaker': 'Furina',
                              'text': 'Funny, is it not? In every grand opera, the audience only remembers '
                                      'a prima donna fondly if she takes her final bow while her highest '
                                      'note still rings clear.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B03',
                              'speaker': 'Furina',
                              'text': 'Once the Fontinalia curtain drops next week, a star-traveling '
                                      'witness like you has fiery horizons waiting in the west. Better you '
                                      "remember Fontaine's finest director at the top of her craft than "
                                      'fretting over backstage pipes!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N08_B04',
                              'speaker': 'Aether',
                              'text': "Natlan's roads are not going anywhere, Furina. Whenever you start "
                                      'talking like a third-act narrator wrapping up her own epilogue, it '
                                      'means you are hiding something heavy.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_E1',
                              'speaker': 'Narrator',
                              'text': 'Far below the Outer Seawall, white foam curls along the great '
                                      "waterfall drop where Fontaine's elevated waters plunge toward the "
                                      'outer world.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_E2',
                              'speaker': 'Furina',
                              'text': 'Promise me one small vanity before you answer, Aether. Even after '
                                      "you see ten more nations... do not let Fontaine's songs blur into "
                                      'background scenery in your memory.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_E3',
                              'speaker': 'Aether',
                              'text': 'As long as a certain director keeps arguing tempo in my ear, there '
                                      'is zero danger of that.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_E4',
                              'speaker': 'Narrator',
                              'text': 'A fleeting, genuine warmth softens the corner of her mouth before '
                                      'the sea breeze stirs between us again.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B05',
                              'speaker': 'Narrator',
                              'text': 'Sea wind tugs at the navy ribbons of her coat as she looks sideways '
                                      'at me, caught halfway between royal bluff and quiet vulnerability.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C04',
                              'prompt': "Beneath her breezy theatrical tone, Furina's gloved fingers "
                                        'tighten subtly on the wet parapet stone.',
                              'options': [{'opt_id': 'C04_A',
                                           'label': 'Cover her gloved hand with yours and make her swear a '
                                                    'Two-Actor Curtain Pact: no solo exits behind your '
                                                    'back.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F04_ROOFTOP_ENCORE']},
                                           'next_node': 'N09',
                                           'reaction_beats': [{'beat_id': 'N08_C04A_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'No solo exits, Furina. Swear it '
                                                                       'with me right here on the seawall: '
                                                                       'neither the director nor her '
                                                                       'assistant rewrites the final act '
                                                                       'alone behind the curtain.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_pact_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N08_C04A_R2',
                                                               'speaker': 'Furina',
                                                               'text': 'Eh...?! Honestly, how presumptuous '
                                                                       'of an assistant to lecture his '
                                                                       'director on script authority! '
                                                                       '...Fine, fine, a two-actor pact it '
                                                                       'is, if only so we do not catch '
                                                                       'cold in the mist!',
                                                               'inner_thought': 'Memory Anchored [Seawall '
                                                                                'Curtain Pact]: Neither of '
                                                                                'us rewrites the final act '
                                                                                'alone.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_pact_diff.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C04_B',
                                           'label': 'Read between the lines of her metaphor about bowing '
                                                    'out before a voice breaks, answering with quiet '
                                                    'empathy.',
                                           'effects': {'bond': 1, 'insight': 2, 'add_flags': []},
                                           'next_node': 'N09',
                                           'reaction_beats': [{'beat_id': 'N08_C04B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'I did not sit in Seat Number One '
                                                                       'just to applaud flawless high '
                                                                       'notes, Furina. Even if the score '
                                                                       'cracks or runs out of ink, I have '
                                                                       'nowhere better to be until we '
                                                                       'finish this Gala together.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N08_C04B_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Her heterochromatic eyes widen '
                                                                       'slightly under the streetlamp glow '
                                                                       'before she tips her hat brim down '
                                                                       'with a soft, unguarded exhale -- '
                                                                       'filing away more fear behind that '
                                                                       'soprano metaphor than she lets on.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch1_seawall_overlook_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N09': {'node_id': 'N09',
                   'chapter_id': 'CH2',
                   'title': 'The Workshop of Maitre Renaud',
                   'day_label': 'Day 5 - 10:00 AM',
                   'location': "Lower Court Edge - Ivy-Draped Lutist's Conservatory",
                   'beats': [{'beat_id': 'N09_B01',
                              'speaker': 'Narrator',
                              'text': 'Morning on Day Five leads us to an ivy-draped stone conservatory '
                                      'overlooking the lower canal, home to retired Opera Epiclese '
                                      'concertmaster Maitre Renaud.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B02',
                              'speaker': 'Furina',
                              'text': "Look at the arranger's cipher on Act Three's margin, Aether. Fifty "
                                      "years ago, young Maitre Renaud himself adapted 'La Derniere "
                                      "Vaguelette' into French from an old Erinnyes stone melody -- and "
                                      'withheld Act Four!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': 'outing_arrive_photo'},
                             {'beat_id': 'N09_B02B',
                              'speaker': 'Narrator',
                              'text': 'Pearwood lutes, bowed viols, and silent brass metronomes line the '
                                      'sunlit stone walls inside, smelling faintly of rosin dust and dried '
                                      'lavender.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B03',
                              'speaker': 'Narrator',
                              'text': 'Inside, silver-haired Maitre Renaud watches our entrance with '
                                      'sharp, clear dark eyes -- reading our lips half a beat before '
                                      'answering in the overly measured cadence of a musician losing his '
                                      'hearing.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B04',
                              'speaker': 'Maitre Renaud',
                              'text': "Lady Furina. If you came for Act Four's sub-bass cadenza, leave it "
                                      'buried. Fifty winters ago, one rehearsal of that chord shook '
                                      'salt-frost up through the orchestra pit floorboards.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B04B',
                              'speaker': 'Aether',
                              'text': 'What happened when you played that fourth act fifty years ago, '
                                      'Maitre Renaud?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B04C',
                              'speaker': 'Maitre Renaud',
                              'text': 'The stone tablet from Erinnyes was scored for TWO resonant '
                                      'witnesses -- a soprano melody above and an unshakable bass anchor '
                                      'below. Foolish youth that I was, I tried sounding both registers '
                                      'alone on my lute, and the rebound stole half my hearing in a night.',
                              'inner_thought': 'Two resonant witnesses: a soprano above and a bass anchor '
                                               'below!',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B05',
                              'speaker': 'Furina',
                              'text': 'Wait, Maitre! That sub-stage cistern is already waking up on its '
                                      'own! Without your harmonic inversion key, the Solstice tide on '
                                      'Night Nine will tear through the acoustics unchecked!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_E1',
                              'speaker': 'Furina',
                              'text': 'Five years ago, Maitre Renaud, Celine sang the Bellflower Aria at '
                                      'her debut with tears in her eyes -- every breath shaped the way you '
                                      'taught her!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_E2',
                              'speaker': 'Maitre Renaud',
                              'text': 'Sentimentality ruins pitch, Lady Furina! A soprano bound for the '
                                      'top of the poster has no business anchoring her tempo to an old '
                                      'lutist whose fingers -- whose standards -- grew too rigid!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_E3',
                              'speaker': 'Aether',
                              'text': "You started to say 'whose ears', Maitre, before you caught "
                                      'yourself.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_E4',
                              'speaker': 'Narrator',
                              'text': 'Renaud shoots me a fierce, startled glare -- realizing too late '
                                      'that an observant traveler is harder to bluff than a '
                                      'twenty-year-old pupil.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B06',
                              'speaker': 'Narrator',
                              'text': "Renaud's jaw tightens as his gaze drifts toward a framed Opera "
                                      'portrait of a young soprano named Celine -- the star pupil he '
                                      'famously drove out of his studio in a furious outburst five years '
                                      'ago.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N10'}],
                   'ending_id': None},
           'N10': {'node_id': 'N10',
                   'chapter_id': 'CH2',
                   'title': 'The Rosewood Stand & The Unsent Draft',
                   'day_label': 'Day 5 Afternoon to Late Night',
                   'location': "Maitre Renaud's Conservatory -> Quartier Lyonnais",
                   'beats': [{'beat_id': 'N10_B01',
                              'speaker': 'Maitre Renaud',
                              'text': 'Hmph. Before I surrender a single bar of that score, show me you '
                                      'understand its counterpoint on the clavecin. Young Traveler -- '
                                      'fetch the leather pouch of A-440 tuning forks from my rosewood '
                                      "music stand's top drawer.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B01B',
                              'speaker': 'Furina',
                              'text': 'Gladly, Maitre! Even playing lightness-first with my left hand, I '
                                      'know every measure of your third act by heart!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N10_B01C',
                              'speaker': 'Narrator',
                              'text': 'Clear, bell-like clavecin notes ripple across the conservatory as '
                                      "Furina's left fingers dance effortlessly over the ivory keys, "
                                      "softening even Renaud's stern brow.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_E1',
                              'speaker': 'Maitre Renaud',
                              'text': '...Remarkable left-hand voicing, Lady Furina. You play that '
                                      'third-act bridge not like a triumphant hymn, but like a lullaby '
                                      'sung to an exhausted child.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_E2',
                              'speaker': 'Furina',
                              'text': 'Because waves only crash loudly when they hit stone, Maitre. Out in '
                                      'deep water at night, all they ever wanted was somewhere quiet to '
                                      'rest.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_E3',
                              'speaker': 'Narrator',
                              'text': 'Sunlight motes drift across the rosewood stand as Renaud lowers his '
                                      'guard, nodding slowly toward the drawer in my hands.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_E4',
                              'speaker': 'Maitre Renaud',
                              'text': 'Deliver my old study lute case to Celine at Clementine Dock '
                                      'tomorrow sunset -- without speaking one word of excuse for me -- '
                                      'and the harmonic key of Act Four is yours.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B02',
                              'speaker': 'Narrator',
                              'text': 'While Furina seats herself gracefully at the clavecin keys, I slide '
                                      "open the rosewood drawer at Renaud's request. Right beside the "
                                      'leather tuning-fork pouch rest an engraved brass ear-trumpet and an '
                                      'unsealed draft letter.',
                              'inner_thought': 'Clinic slips for progressive inner-ear otosclerosis lie '
                                               'clipped to five years of anonymous tuition receipts for '
                                               'Celine.',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C05',
                              'prompt': 'With the drawer open in your hands, the unsent top page beside '
                                        'the tuning forks catches the afternoon light.',
                              'options': [{'opt_id': 'C05_A',
                                           'label': "Take in the visible lines of Renaud's unsent "
                                                    'confession beside the brass ear-trumpet as you lift '
                                                    'the tuning forks.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F05_LUTIST_SCORE']},
                                           'next_node': 'N11',
                                           'reaction_beats': [{'beat_id': 'N10_C05A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Written in a proud, trembling '
                                                                       "hand: 'Forgive an old fool's "
                                                                       'staged tantrum, Celine. Better you '
                                                                       'despise my arrogance on the grand '
                                                                       'stage than waste your golden prime '
                                                                       'pitying a concertmaster going '
                                                                       "stone-deaf.'",
                                                               'inner_thought': 'Clue Recorded [The '
                                                                                "Lutist's Staged Pride]: "
                                                                                'Proud artists feign '
                                                                                'coldness to spare loved '
                                                                                'ones from pitying what '
                                                                                'art broke in them.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05A_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'I close the drawer respectfully '
                                                                       'and hand over the tuning forks. '
                                                                       'All evening back in Quartier '
                                                                       "Lyonnais, as we copy Renaud's "
                                                                       'harmonic key by lamplight, that '
                                                                       'staged farewell echoes uncannily '
                                                                       "beside Furina's forced cheer.",
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C05_B',
                                           'label': 'Bring the tuning forks straight over and join Furina '
                                                    'at the clavecin for a warm four-hand sight-reading '
                                                    'duet.',
                                           'effects': {'bond': 2, 'insight': 1, 'add_flags': []},
                                           'next_node': 'N11',
                                           'reaction_beats': [{'beat_id': 'N10_C05B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Closing the drawer immediately, I '
                                                                       'pull up a stool beside Furina and '
                                                                       'take the lower bass register while '
                                                                       'her nimble left hand dances across '
                                                                       'the treble keys.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05B_R2',
                                                               'speaker': 'Furina',
                                                               'text': 'Hehe, impeccable phrasing on the '
                                                                       'counterpoint, Assistant! See, '
                                                                       'Maitre Renaud? Even the silence '
                                                                       'between two players can carry a '
                                                                       'melody! We spend all of Night Five '
                                                                       'transcribing his notes in high '
                                                                       'spirits.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_lutist_workshop_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N11': {'node_id': 'N11',
                   'chapter_id': 'CH2',
                   'title': 'Clementine Dock at Sunset',
                   'day_label': 'Day 6 - 05:15 PM',
                   'location': 'Court of Fontaine - Clementine Line Aquabus Station',
                   'beats': [{'beat_id': 'N11_B01',
                              'speaker': 'Narrator',
                              'text': 'Late on Day Six, amber sunset spills across the Clementine Line '
                                      'Aquabus dock. True to our bargain with Maitre Renaud, we carry a '
                                      'worn velvet lute case to his former pupil Celine before her evening '
                                      'boat departs.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B02',
                              'speaker': 'Furina',
                              'text': "Remember Renaud's iron condition, Aether: we are strictly forbidden "
                                      'from speaking a single word of excuse or explanation on his behalf. '
                                      'Oh, why must elderly musicians be so infuriatingly theatrical?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B03',
                              'speaker': 'Celine',
                              'text': 'Lady Furina...? Wait -- that crest on the velvet case belongs to '
                                      'Maitre Renaud! Did he send back my old study lute just to sever the '
                                      'last thread before I sing at the Gala?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B03B',
                              'speaker': 'Celine',
                              'text': 'Five winters ago he shouted that my pitch grated on his ears and '
                                      'locked his conservatory door in my face! Why send a messenger at '
                                      'sunset without even deigning to write a note?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B03C',
                              'speaker': 'Narrator',
                              'text': 'Beside me, Furina presses her gloved knuckles tight against her '
                                      'lips to stop herself from blurting out the truth, her mismatched '
                                      'eyes shining with helpless sympathy.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_E1',
                              'speaker': 'Furina',
                              'text': 'Demoiselle Celine, wait on the pier just thirty seconds! At least '
                                      'look at the polish on that pearwood case -- there is not a speck of '
                                      'dust after five winters!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_E2',
                              'speaker': 'Celine',
                              'text': 'Maitre Renaud polishes every instrument in his studio out of sheer '
                                      'perfectionism, Lady Furina. It never meant he forgave me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_E3',
                              'speaker': 'Aether',
                              'text': 'Sometimes the proudest people polish what they miss most because '
                                      'they do not know how else to apologize.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_E4',
                              'speaker': 'Narrator',
                              'text': 'Beside me, Furina blinks quickly at my words -- as if they brushed '
                                      "a lock inside her own chest as much as Celine's.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B04',
                              'speaker': 'Narrator',
                              'text': "Tears well in Celine's eyes as she takes half a step back toward "
                                      'the boarding ramp, ready to refuse the closed case out of five '
                                      'years of wounded pride.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N12'}],
                   'ending_id': None},
           'N12': {'node_id': 'N12',
                   'chapter_id': 'CH2',
                   'title': 'The Brass Tuning-Harmonica',
                   'day_label': 'Day 6 - Dusk',
                   'location': 'Clementine Line Pier -> Gaslit Arcade',
                   'beats': [{'beat_id': 'N12_B01',
                              'speaker': 'Narrator',
                              'text': 'The Aquabus departure bell rings once down the platform. Bound by '
                                      "Renaud's literal words not to speak an excuse, I hold the velvet "
                                      "case between Celine's trembling hands and Furina's silent, aching "
                                      'gaze.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B02',
                              'speaker': 'Narrator',
                              'text': "Down on the canal below, Aeval's cheerful Melusine voice announces "
                                      'five minutes until Clementine Line departure, crimson dusk turning '
                                      'the water to liquid copper.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_E1',
                              'speaker': 'Celine',
                              'text': 'If Maitre Renaud truly wanted me to forget his studio, he could '
                                      'have sent an apprentice instead of asking Lady Furina and the '
                                      'Traveler himself...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_E2',
                              'speaker': 'Narrator',
                              'text': 'Golden sunset ripples off the brass latch of the worn lute case '
                                      'balanced across my palms.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_E3',
                              'speaker': 'Aether',
                              'text': 'The Clementine Aquabus gangplank is still down for one more minute, '
                                      'Celine.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_E4',
                              'speaker': 'Narrator',
                              'text': "Celine's fingers hover timidly above the velvet lid, waiting on my "
                                      'next move.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B03',
                              'speaker': 'Furina',
                              'text': '...Aether. We promised we would not speak a word of excuse for him '
                                      "-- yet surely a stagehand's hands are allowed to check a loose "
                                      'brass clasp?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C06',
                              'prompt': 'You promised Maitre Renaud not to speak a word of excuse, yet '
                                        'Celine is seconds from turning away.',
                              'options': [{'opt_id': 'C06_A',
                                           'label': 'Say nothing at all -- simply flick open the brass '
                                                    'latch so Celine sees the childhood tuning-harmonica '
                                                    'inside.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F06_HARMONICA_MERCY']},
                                           'next_node': 'N13',
                                           'reaction_beats': [{'beat_id': 'N12_C06A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Keeping silent to the letter, my '
                                                                       'thumb flicks the brass latch open '
                                                                       'half an inch. Nestled beneath the '
                                                                       "lute strings gleams Celine's "
                                                                       'dented childhood brass '
                                                                       'tuning-harmonica beside five years '
                                                                       'of lovingly annotated Gala '
                                                                       'clippings.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06A_R2',
                                                               'speaker': 'Celine',
                                                               'text': 'That harmonica... he could barely '
                                                                       'hear the upper octave even five '
                                                                       'years ago, could he?! Excuse me, '
                                                                       'Lady Furina -- I have a stubborn '
                                                                       'old concertmaster to scold right '
                                                                       'this instant!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06A_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'After Celine sprints back down the '
                                                                       'stairs cradling the case, we walk '
                                                                       'home beneath warm gaslamps. '
                                                                       'Without a single stage flourish, '
                                                                       'Furina slows beside me and rests '
                                                                       'her temple silently against my '
                                                                       'shoulder for three long breaths.',
                                                               'inner_thought': 'Memory Anchored '
                                                                                '[Harmonica Mercy]: For '
                                                                                'three quiet breaths under '
                                                                                'the gaslamps, Furina '
                                                                                'drops every mask against '
                                                                                'my shoulder.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_lean_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C06_B',
                                           'label': "Keep the latch closed out of respect for Renaud's "
                                                    'austerity, urging Celine gently to open it once the '
                                                    'Aquabus clears the pier.',
                                           'effects': {'bond': 1, 'insight': 2, 'add_flags': []},
                                           'next_node': 'N13',
                                           'reaction_beats': [{'beat_id': 'N12_C06B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'We gave our word not to speak for '
                                                                       'him, Demoiselle Celine. Only trust '
                                                                       'the weight of that case -- and '
                                                                       'open it once the water grows '
                                                                       'quiet.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06B_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Celine hesitates, then nods and '
                                                                       'carries the velvet case aboard -- '
                                                                       'sure to discover the truth '
                                                                       'tonight. Walking back along the '
                                                                       'arcade, Furina muses quietly on '
                                                                       'why proud artists fear pity worse '
                                                                       'than solitude.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_dock_harmonica_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N13': {'node_id': 'N13',
                   'chapter_id': 'CH2',
                   'title': 'Chioriya Boutique & The Two Silver Pinholes',
                   'day_label': 'Day 7 - 03:30 PM',
                   'location': 'Court of Fontaine - Chioriya Boutique',
                   'beats': [{'beat_id': 'N13_B01',
                              'speaker': 'Narrator',
                              'text': 'Afternoon on Day Seven brings the scent of pressed silk and '
                                      'camellia oil inside Chioriya Boutique, where Chiori puts the '
                                      "finishing stitches on Furina's midnight-blue velvet Gala Director "
                                      'capelet.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B02',
                              'speaker': 'Chiori',
                              'text': 'Hold still behind that screen for ten seconds, Lady Furina. And '
                                      'stop fiddling with your cuffs -- if you snag my double-stitched '
                                      'Valenciennes lace before Opening Night, Tamoto will show no mercy.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B02B',
                              'speaker': 'Chiori',
                              'text': 'Incidentally, Aether -- hold still by the counter a moment. Let me '
                                      'measure the width of your white scarf lapel.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B02C',
                              'speaker': 'Aether',
                              'text': "My scarf lapel? I thought today's fitting was only for Furina's "
                                      'Gala capelet.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B02D',
                              'speaker': 'Furina',
                              'text': 'A-Ahem!! Purely for front-row visual symmetry, Assistant! Do not '
                                      "ask impertinent questions behind a lady's dressing screen, and "
                                      'Chiori -- not another syllable!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N13_B03',
                              'speaker': 'Narrator',
                              'text': 'From behind the painted silk screen comes a tiny metallic click. A '
                                      'moment later, Furina steps out onto the sunlit cobblestones outside '
                                      'the boutique door and spins in a crisp theatrical pirouette.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B04',
                              'speaker': 'Narrator',
                              'text': 'The midnight velvet capelet suits her royally -- yet as afternoon '
                                      'light catches her top hat, two tiny empty silver pinholes stand out '
                                      'starkly on the bare navy hatband where her sapphire-plume star pin '
                                      'always rests, while a faint blue glint peeks from her hidden right '
                                      'cuff.',
                              'inner_thought': 'Her navy hatband is completely bare -- only two tiny '
                                               'silver pinholes remain, and something sapphire glints '
                                               'inside her right cuff!',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_E1',
                              'speaker': 'Narrator',
                              'text': "On Chiori's cutting table beside a spool of gold-and-sapphire silk "
                                      'thread sits a tiny sketch pad flipped face-down at the sound of my '
                                      'boots.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_E2',
                              'speaker': 'Chiori',
                              'text': 'Eyes forward, Traveler. Good tailoring loses half its magic if the '
                                      'recipient peeks at the workbench before curtain call.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_E3',
                              'speaker': 'Aether',
                              'text': 'Between you and Furina, everyone in Fontaine has a secret script '
                                      'tucked in a sleeve this week.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_E4',
                              'speaker': 'Chiori',
                              'text': 'Some scripts are worth waiting five days to read, Aether. Pay close '
                                      'attention to her hatband when she steps outside.',
                              'inner_thought': "Chiori practically handed me a clue: watch Furina's "
                                               'hatband when she steps out!',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B05',
                              'speaker': 'Furina',
                              'text': "Ahem! Behold the Centennial Director's silhouette! Tell me "
                                      'honestly, my Seat Number One witness -- do you spot what is '
                                      'different about my ensemble today?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': 'vn_playful_tease'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N14'}],
                   'ending_id': None},
           'N14': {'node_id': 'N14',
                   'chapter_id': 'CH2',
                   'title': "L'Etoile d'Eau on the Cobblestones",
                   'day_label': 'Day 7 - 04:15 PM',
                   'location': 'Cobblestone Lane Outside Chioriya Boutique',
                   'beats': [{'beat_id': 'N14_B01',
                              'speaker': 'Narrator',
                              'text': 'Through the boutique window behind her, Chiori pauses with sewing '
                                      'shears in hand, watching the two of us with a knowing, razor-subtle '
                                      'half-smile as Furina waits on tiptoe for my answer.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B02',
                              'speaker': 'Furina',
                              'text': "Come now, Seat Number One -- surely Fontaine's sharpest-eyed "
                                      'Traveler does not need three hints when the leading lady debuts her '
                                      'Gala silhouette right in front of him!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': 'outing_arrive_photo'},
                             {'beat_id': 'N14_E1',
                              'speaker': 'Furina',
                              'text': 'Well? Look at the fall of the velvet shoulders, the silver-piped '
                                      'lapels, the immaculate tilt of my top hat!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N14_E2',
                              'speaker': 'Narrator',
                              'text': 'A gentle breeze down the cobblestone lane ruffles her '
                                      'white-and-blue curls, catching the two empty pinholes on her navy '
                                      'ribbon in clear afternoon light.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_E3',
                              'speaker': 'Aether',
                              'text': "Every stitch of Chiori's capelet is worthy of Opening Night, Furina "
                                      '-- though one detail jumps straight out at me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_E4',
                              'speaker': 'Furina',
                              'text': "Oho? Let us hear Seat Number One's verdict then!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B03',
                              'speaker': 'Narrator',
                              'text': 'Afternoon light glints off the two tiny silver pinholes on her bare '
                                      'navy hatband -- and off the tip of a familiar sapphire plume hidden '
                                      'loosely inside her right lace cuff.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C07',
                              'prompt': "Two tiny pinholes mark the bare navy ribbon of Furina's top hat "
                                        'while her right cuff hides behind her back.',
                              'options': [{'opt_id': 'C07_A',
                                           'label': 'Point straight to the two empty pinholes on her bare '
                                                    'navy hatband where her sapphire-plume star pin '
                                                    'belongs.',
                                           'effects': {'bond': 1,
                                                       'insight': 1,
                                                       'add_flags': ['F07_SAPPHIRE_PIN']},
                                           'next_node': 'N15',
                                           'reaction_beats': [{'beat_id': 'N14_C07A_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'The midnight velvet is stunning -- '
                                                                       'but your navy hatband is bare. You '
                                                                       "unpinned 'L'Etoile d'Eau' behind "
                                                                       'the folding screen and tucked it '
                                                                       'into your right cuff.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_pin_gift_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07A_R2',
                                                               'speaker': 'Furina',
                                                               'text': 'E-Eh?! Are your eyes part hawk?! '
                                                                       '...Oh, very well! Take it! Hold '
                                                                       "onto 'L'Etoile d'Eau' in Seat "
                                                                       'Number One until the Gala curtain '
                                                                       'falls, so I do not lose my nerve '
                                                                       '-- or my favorite star pin -- '
                                                                       'backstage!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_pin_gift_diff.jpg',
                                                               'voice_emotion': 'vn_shy_blush'},
                                                              {'beat_id': 'N14_C07A_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'Blushing crimson to the tips of '
                                                                       'her ears, she presses the warm '
                                                                       'silver-and-sapphire plume pin -- '
                                                                       'shimmering faintly with pure light '
                                                                       'from her own Hydro Vision -- into '
                                                                       'my palm.',
                                                               'inner_thought': 'Keepsake Entrusted '
                                                                                "[L'Etoile d'Eau]: "
                                                                                "Furina's Vision-warmed "
                                                                                'Sapphire-Plume Star Pin '
                                                                                'rests in my keeping until '
                                                                                'curtain call.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_pin_gift_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C07_B',
                                           'label': "Praise how Chiori's deep midnight velvet makes the "
                                                    'twin blues of her eyes shine like starlight on water.',
                                           'effects': {'bond': 3, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N15',
                                           'reaction_beats': [{'beat_id': 'N14_C07B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Midnight velvet was made for you, '
                                                                       'Furina. Against that dark collar, '
                                                                       'the two shades of blue in your '
                                                                       'eyes catch the sunset brighter '
                                                                       'than every chandelier in the Opera '
                                                                       'House.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07B_R2',
                                                               'speaker': 'Furina',
                                                               'text': 'H-Hmph! Springing poetic flattery '
                                                                       'in broad daylight is against union '
                                                                       'regulations, Assistant! Come along '
                                                                       'to the Opera Epiclese before my '
                                                                       'cheeks catch fire!',
                                                               'inner_thought': 'Flustered and delighted, '
                                                                                'she keeps whatever is '
                                                                                'tucked inside her right '
                                                                                'cuff hidden for now.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_barehat_base.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N15': {'node_id': 'N15',
                   'chapter_id': 'CH2',
                   'title': 'Sub-Stage Tremor at Opera Epiclese',
                   'day_label': 'Day 7 - 08:30 PM',
                   'location': 'Erinnyes Island - Opera Epiclese Empty Auditorium',
                   'beats': [{'beat_id': 'N15_B01',
                              'speaker': 'Narrator',
                              'text': "By half past eight on Night Seven, only stagehands and Clorinde's "
                                      'security detail occupy the vast crimson hall of the Opera Epiclese '
                                      "as we test Maitre Renaud's harmonic key against the Pneumousia "
                                      'Grand Organ.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B01B',
                              'speaker': 'Charlotte',
                              'text': 'Monsieur Verite is focused on the chandelier prisms, everyone! '
                                      'Sound the low test chord whenever you are ready in the pit!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B02',
                              'speaker': 'Narrator',
                              'text': 'The organist depresses a single low pedal. Instantly, the cracked '
                                      'mineral seal far below the orchestra pit splits wide open with a '
                                      'deep oceanic groan!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B03',
                              'speaker': 'Clorinde',
                              'text': 'Watch the proscenium arch! Plaster molding is coming down -- clear '
                                      'the orchestra rail!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B03B',
                              'speaker': 'Narrator',
                              'text': 'Drawing my dull blade in a flash, I intercept a falling chunk of '
                                      "gilded plaster above the violinist's stand while Gentilhomme Usher "
                                      'steadies a swaying brass sconce!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B04',
                              'speaker': 'Narrator',
                              'text': 'Gilded plaster shatters across the front pit while freezing '
                                      'salt-mist smelling of the Fountain of Lucine curls up between the '
                                      'stage floorboards -- locking the subterranean cistern into '
                                      "irreversible countdown toward Night Nine's Solstice peak.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_E1',
                              'speaker': 'Charlotte',
                              'text': 'Whew -- good reflexes with that sword, Aether! Half an inch to the '
                                      'left and my Kamera lens would be powdered sugar!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_E2',
                              'speaker': 'Clorinde',
                              'text': 'That tremor came straight up the central drainage column from the '
                                      'Fountain of Lucine. Feel the brass rail -- it is icing over in a '
                                      'heated hall.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_E3',
                              'speaker': 'Aether',
                              'text': 'Even when the organist lifted his foot off the pedal, the sub-bass '
                                      'hum beneath the stone never stopped rising.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_E4',
                              'speaker': 'Narrator',
                              'text': 'Up on the stage apron, Furina claps her gloved hands twice with '
                                      'bright, forced authority so none of the young chorus singers panic.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B05',
                              'speaker': 'Furina',
                              'text': 'Aha! Calm yourselves, everyone -- merely winter air trapped in the '
                                      'old acoustic ducts! Take fifteen minutes in the front foyer while I '
                                      'inspect the stage-right curtain rigging!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': 'vn_playful_tease'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N16'}],
                   'ending_id': None},
           'N16': {'node_id': 'N16',
                   'chapter_id': 'CH2',
                   'title': 'Behind the Crimson Wing-Curtain',
                   'day_label': 'Day 7 - 09:15 PM',
                   'location': 'Opera Epiclese - Dim Stage-Right Wing',
                   'beats': [{'beat_id': 'N16_B01',
                              'speaker': 'Narrator',
                              'text': 'Even as Furina waves the crew cheerfully toward the foyer, the '
                                      'final syllable of her laugh catches in a dry, voiceless rasp before '
                                      'she slips behind the heavy crimson stage-right wing curtain.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B02',
                              'speaker': 'Clorinde',
                              'text': 'Two reporters from the harbor press are already knocking at the '
                                      'outer vestibule, Aether. I can hold the doors, or we can both keep '
                                      'the corridor clear.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_E1',
                              'speaker': 'Clorinde',
                              'text': 'You noticed her voice catch on that last word too, did you not, '
                                      'Aether?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_E2',
                              'speaker': 'Aether',
                              'text': 'She laughed louder on the first syllable just to cover the rasp at '
                                      'the end.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_E3',
                              'speaker': 'Clorinde',
                              'text': 'If I march behind that curtain in uniform, she will stiffen her '
                                      'spine and swear she is fine until she collapses. With you, there is '
                                      'a chance.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_E4',
                              'speaker': 'Narrator',
                              'text': 'Outside in the marble vestibule, impatient knuckles rap louder '
                                      'against the double doors while cold mist curls from beneath the '
                                      'crimson velvet wing.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B03',
                              'speaker': 'Narrator',
                              'text': 'From behind the velvet wing-curtain five paces away, the air drops '
                                      'sharply colder, accompanied by a muffled, shivering intake of '
                                      'breath.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C08',
                              'prompt': 'Shadow hides Furina behind the crimson wing-curtain while '
                                        'reporters knock at the outer foyer.',
                              'options': [{'opt_id': 'C08_A',
                                           'label': 'Slip quietly behind the crimson wing-curtain to check '
                                                    'on Furina before she can hide what happened.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F08_CRYSTAL_TEAR_SEEN']},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_C08A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Parting the heavy velvet '
                                                                       'noiselessly, I catch Furina '
                                                                       'bracing one shoulder against a '
                                                                       'cold marble pillar. Pressed to her '
                                                                       'lips is a white lace handkerchief '
                                                                       'sparkling with tiny, razor-cold '
                                                                       'crystals of frozen salt-tear rime!',
                                                               'inner_thought': 'Clue Recorded [Crystal '
                                                                                'Tear Rime]: The awakened '
                                                                                'sub-stage cistern is '
                                                                                'draining warmth from her '
                                                                                'throat and freezing her '
                                                                                'tears.',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_rime_cloth_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08A_R2',
                                                               'speaker': 'Furina',
                                                               'text': '...You were supposed to stay in '
                                                                       'the foyer, Aether. It is only '
                                                                       'stage frost -- my voice will hold '
                                                                       'for forty-eight more hours. '
                                                                       'Promise me you will not panic '
                                                                       'Clorinde tonight.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_rime_cloth_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C08_B',
                                           'label': 'Stand shoulder-to-shoulder with Clorinde at the '
                                                    "vestibule to shield Furina's dignity, bringing warm "
                                                    'lemon water when she emerges.',
                                           'effects': {'bond': 2, 'insight': 1, 'add_flags': []},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_C08B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'I step beside Clorinde to turn the '
                                                                       'prying reporters politely away at '
                                                                       'the doors, then pour a steaming '
                                                                       'cup of honey-lemon water from the '
                                                                       'greenroom kettle just as Furina '
                                                                       'steps out smoothing her collar.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08B_R2',
                                                               'speaker': 'Furina',
                                                               'text': '...Thank you, Aether. Truly, '
                                                                       "nobody guards a leading lady's "
                                                                       'composure half so gracefully as '
                                                                       'you.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_opera_tremor_base.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N17': {'node_id': 'N17',
                   'chapter_id': 'CH2',
                   'title': 'Crossroads at Lucine Midnight',
                   'day_label': 'Day 7 - Midnight (48 Hours Before Gala Finale)',
                   'location': 'Erinnyes Island - Fountain of Lucine',
                   'pre_events': [{'when': {'forbid_flags': ['F07_SAPPHIRE_PIN'],
                                            'min_bond': 11,
                                            'min_insight': 7},
                                   'effects': {'add_flags': ['F07_SAPPHIRE_PIN',
                                                             'F07_SECOND_CHANCE_N17']}}],
                   'beats': [{'beat_id': 'N17_B01',
                              'speaker': 'Narrator',
                              'text': 'Midnight tolls across Erinnyes Island -- exactly forty-eight hours '
                                      "before Night Nine's eleven-o'clock Solstice peak. Outside the "
                                      'Fountain of Lucine, silver mist trembles rhythmically across the '
                                      'dark basin.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B02',
                              'speaker': 'Furina',
                              'text': 'Even with the Grand Organ powered down tonight, you can feel the '
                                      'floorboards humming, cannot you? Fifty years after Renaud hid Act '
                                      'Four, five centuries of old echoes beneath this plaza refuse to '
                                      'stay asleep.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B03_BACKUP',
                              'speaker': 'Narrator',
                              'text': 'Just before turning toward the lamp-lit path, Furina stops short, '
                                      'bites her lower lip, and pulls the unpinned Sapphire-Plume Star Pin '
                                      'from her right lace cuff -- pressing it abruptly into my palm!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_pin_gift_diff.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B04_BACKUP',
                              'speaker': 'Furina',
                              'text': "Here -- keep 'L'Etoile d'Eau' safe for me until curtain call after "
                                      'all! You have watched every step and listened to every breath I '
                                      'take this week... I trust Seat Number One with my lucky star more '
                                      'than myself!',
                              'inner_thought': "Keepsake Entrusted [L'Etoile d'Eau]: Moved by our trust "
                                               'and perception, Furina entrusted her Vision-warmed Star '
                                               'Pin to me!',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_chioriya_pin_gift_diff.jpg',
                              'voice_emotion': 'vn_shy_blush',
                              'when': {'all_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B05_NO_F07',
                              'speaker': 'Narrator',
                              'text': 'Touching the two empty pinholes on her navy hatband with a wistful '
                                      'sigh, Furina quietly draws her sapphire-plume star pin from her '
                                      'cuff and fastens it back onto her hat before facing the crossroads.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_SAPPHIRE_PIN']}},
                             {'beat_id': 'N17_E1',
                              'speaker': 'Furina',
                              'text': "Do you remember the end of 'The Little Oceanid' troupe premiere, "
                                      'Aether? Even after stepping into sunlight, a part of me always '
                                      'wondered where five hundred years of backstage tears actually went.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_E2',
                              'speaker': 'Aether',
                              'text': "Down into this plaza's roots -- waiting for someone to close the "
                                      'book properly instead of locking the cellar door.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_E3',
                              'speaker': 'Furina',
                              'text': "Two days until Night Nine's eleven-o'clock tide... Whatever path we "
                                      'pick tonight, promise me you will not look at me like fragile '
                                      'glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_E4',
                              'speaker': 'Aether',
                              'text': 'Never fragile glass, Furina. You are the strongest person in '
                                      'Fontaine -- you just do not have to carry the stage alone anymore.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B06',
                              'speaker': 'Aether',
                              'text': 'Forty-eight hours remain until the Solstice tide peaks at eleven '
                                      "o'clock on Night Nine, Furina. How we spend tomorrow and Gala Day "
                                      'decides everything.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C09',
                              'prompt': "Forty-eight hours before Night Nine's peak, three distinct paths "
                                        'open before the Fountain of Lucine:',
                              'options': [{'opt_id': 'C09_ROUTE_A',
                                           'label': '[Route A] Prepare gear with Clorinde tomorrow and '
                                                    'descend together into the Sunken Erinnyes Cistern '
                                                    'beneath Lucine.',
                                           'effects': {'bond': 1, 'insight': 0, 'add_flags': ['ROUTE_A']},
                                           'next_node': 'N18_A1',
                                           'reaction_beats': [{'beat_id': 'N17_C09A_R1',
                                                               'speaker': 'Furina',
                                                               'text': '...Down into the mirror-cistern '
                                                                       'together? Very well, my fearless '
                                                                       'co-conspirator -- pack lanterns '
                                                                       'tomorrow, and let us confront the '
                                                                       'echoes face to face!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]},
                                          {'opt_id': 'C09_ROUTE_B',
                                           'label': '[Route B] Convene an emergency engineering '
                                                    'investigation across Palais Mermonia and the Seven '
                                                    'Erinnyes Sluices.',
                                           'effects': {'bond': 0, 'insight': 1, 'add_flags': ['ROUTE_B']},
                                           'next_node': 'N23_B1',
                                           'reaction_beats': [{'beat_id': 'N17_C09B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'While you finish staging '
                                                                       'rehearsals above ground, I will '
                                                                       'coordinate with Monsieur '
                                                                       'Neuvillette, Clorinde, and '
                                                                       'Freminet across the seven aqueduct '
                                                                       'sluices to find a technical key.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C09_ROUTE_C',
                                           'label': '[Route C] Invoke Assistant Director authority: whisk '
                                                    'Furina into the Serenitea Pot on Erinnyes Bluff for '
                                                    '48 hours of vocal rest.',
                                           'effects': {'bond': 1, 'insight': 0, 'add_flags': ['ROUTE_C']},
                                           'next_node': 'N26_C1',
                                           'reaction_beats': [{'beat_id': 'N17_C09C_R1',
                                                               'speaker': 'Furina',
                                                               'text': 'Eh?! Sequestering the Gala '
                                                                       'Director inside your Realm Within '
                                                                       'for forty-eight hours of mandatory '
                                                                       'vocal rest?! Wait until Navia and '
                                                                       'Charlotte hear -- oh, do not tell '
                                                                       'me they are already on your side!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/furina/ch2_lucine_crossroads_base.jpg',
                                                               'voice_emotion': 'vn_playful_tease'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N18_A1': {'node_id': 'N18_A1',
                      'chapter_id': 'CH3',
                      'title': 'Dusk Descent at the Lucine Grate',
                      'day_label': 'Day 8 - 08:00 PM (Erinnyes Island)',
                      'location': 'Fountain of Lucine - Side Maintenance Stair',
                      'beats': [{'beat_id': 'N18_B01',
                                 'speaker': 'Narrator',
                                 'text': "All through Day Eight's pale winter daylight, Furina and I "
                                         'finalize blocking charts in Quartier Lyonnais while Clorinde '
                                         'quietly secures storm lanterns, dry rations, and a brass '
                                         'maintenance key from Palais Mermonia.',
                                 'inner_thought': "Twenty-seven hours remain before Night Nine's "
                                                  "eleven-o'clock Winter Solstice Hydro-Tide reaches peak "
                                                  'lock.',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B02',
                                 'speaker': 'Clorinde',
                                 'text': 'The side maintenance grate behind the Fountain of Lucine is '
                                         'clear, Aether. Keep this flare whistle on your belt -- I will '
                                         'return to the upper grate at noon tomorrow to lower hot rations '
                                         'and check your rope line.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B03',
                                 'speaker': 'Furina',
                                 'text': 'Ahem! Do stop looking as though you are seeing us off to the '
                                         'Fortress of Meropide, Clorinde! Mademoiselle Crabaletta, '
                                         'Gentilhomme Usher, Surintendante Chevalmarin -- light our way '
                                         'down the marble steps!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': 'outing_cruise'},
                                {'beat_id': 'N18_B03B',
                                 'speaker': 'Clorinde',
                                 'text': 'You packed three boxes of tea biscuits and only one coil of '
                                         'climbing rope, Furina. Aether -- make sure the director watches '
                                         'her step on wet limestone.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B03C',
                                 'speaker': 'Aether',
                                 'text': 'Count on me, Clorinde. See you at the upper grate at noon '
                                         'tomorrow.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B04',
                                 'speaker': 'Narrator',
                                 'text': 'Behind the bronze grate, spiral stairs carved from ancient pale '
                                         'limestone wind seventy feet below the plaza basin. With every '
                                         'turn, the air smells sharper of cold sea-salt and resonant blue '
                                         'Indemnitium.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B04B',
                                 'speaker': 'Narrator',
                                 'text': "Halfway down the damp curve, Furina's heeled boot slips an inch "
                                         'on sea-moss; before Surintendante Chevalmarin can bubble in '
                                         'alarm, my hand steadies her elbow, and she keeps holding my '
                                         'sleeve the rest of the descent.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B05',
                                 'speaker': 'Narrator',
                                 'text': 'At the bottom, our lantern beams catch a breathtaking, inverted '
                                         'amphitheater of mirrored water and crystal -- built five '
                                         'centuries ago directly beneath the umbilical conduit connecting '
                                         'Lucine and the Opera Epiclese.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_E1',
                                 'speaker': 'Furina',
                                 'text': 'Mademoiselle Crabaletta, stop pinching the moss off the '
                                         'banister! Honestly, five centuries old and this stonework still '
                                         'has better acoustics than half the salons in Quartier '
                                         'Narbonnais.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_E2',
                                 'speaker': 'Aether',
                                 'text': 'Your voice carries three times farther down here. Even a whisper '
                                         'sets the water surface shimmering.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_E3',
                                 'speaker': 'Furina',
                                 'text': 'Because Indemnitium remembers emotion as sound, Aether. Keep '
                                         'your lantern high -- the gallery arch is right ahead.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_E4',
                                 'speaker': 'Narrator',
                                 'text': 'Cool blue phosphorescence blooms across the vaulted ceiling as '
                                         'our boots touch the lower marble landing.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B06',
                                 'speaker': 'Aether',
                                 'text': 'Stay half a step inside my lantern circle, Furina. Even with the '
                                         'Grand Organ silent tonight, the water mirror down here is '
                                         "already counting down toward tomorrow's tide.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N19_A2'}],
                      'ending_id': None},
           'N19_A2': {'node_id': 'N19_A2',
                      'chapter_id': 'CH3',
                      'title': 'Gallery of 182,375 Masks',
                      'day_label': 'Day 8 - 09:30 PM',
                      'location': 'Sunken Erinnyes Cistern - Spotlight Gallery',
                      'beats': [{'beat_id': 'N19_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Lining the vaulted colonnade around the sunken cistern are '
                                         'delicate rime-crystal masks -- hundreds of thousands of them, '
                                         'formed drop by drop across one hundred eighty-two thousand, '
                                         'three hundred seventy-five sleepless nights.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B02',
                                 'speaker': 'Narrator',
                                 'text': 'High above the central mirror dais hang three antique clockwork '
                                         'Spotlight Meks engraved with old Remurian-era theater runes for '
                                         "'Shackles' and 'Chains', their sapphire lenses humming in slow "
                                         'three-part beat.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B03',
                                 'speaker': 'Furina',
                                 'text': '...Every time I wept into my pillow after a trial and forced a '
                                         'smile the next morning, the drainage channels carried the salt '
                                         'down here. Look at them, Aether -- five hundred years of '
                                         'rehearsals staring back at me.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_E1',
                                 'speaker': 'Aether',
                                 'text': 'Look closer at the masks along the third tier, Furina -- they '
                                         'are not frowning at you. Every single mask has tear-tracks '
                                         'carved on the INSIDE cheek, hidden behind a smile.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_E2',
                                 'speaker': 'Furina',
                                 'text': '...On the inside cheek? Just like -- just like every morning I '
                                         'powdered my face before stepping onto the balcony of Palais '
                                         'Mermonia.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_E3',
                                 'speaker': 'Narrator',
                                 'text': 'Gentilhomme Usher floats close beside her left knee, tipping his '
                                         'tiny Hydro top hat in silent solidarity with his creator.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_E4',
                                 'speaker': 'Aether',
                                 'text': 'They are your own endurance, crystallized in salt and light -- '
                                         'yet those three Spotlight Meks overhead are twisting the echo '
                                         'into an accusation.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B04',
                                 'speaker': 'Narrator',
                                 'text': 'A low murmur of phantom courtroom whispers ripples off the '
                                         "crystal masks -- 'Is she truly an Archon?', 'Smile wider for the "
                                         "people!' -- making Furina's right hand curl instinctively into "
                                         'her lace cuff.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C10_A',
                                 'prompt': 'Phantom courtroom murmurs echo off 182,375 crystal masks '
                                           'beneath the three Spotlight Meks:',
                                 'options': [{'opt_id': 'C10_A1',
                                              'label': 'Time the acoustic phase interval between the three '
                                                       'Spotlight Meks and the central tuning pillar.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N20_A3',
                                              'reaction_beats': [{'beat_id': 'N19_C10A1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Holding my dull blade upright '
                                                                          'like a sounding rod, I count '
                                                                          'the harmonic beats rebounding '
                                                                          'between the three Spotlight '
                                                                          'Meks and the sub-stage organ '
                                                                          'pipe overhead.',
                                                                  'inner_thought': 'Every twelve bars, an '
                                                                                   'inverted counter-chord '
                                                                                   'at the central pillar '
                                                                                   'cancels half the '
                                                                                   'standing wave!',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N19_C10A1_R2',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Those three Spotlight Meks are '
                                                                          'not judges, Furina -- they are '
                                                                          'acoustic dampeners left out of '
                                                                          'tune. Look: the central pillar '
                                                                          'has a phase-inversion node we '
                                                                          'can study.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C10_A2',
                                              'label': "Drape your warm travel scarf around Furina's "
                                                       "shoulders and hum Renaud's clavecin motif over the "
                                                       'whispers.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N20_A3',
                                              'reaction_beats': [{'beat_id': 'N19_C10A2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Unfastening my golden-white '
                                                                          'travel scarf, I wrap it snugly '
                                                                          "around Furina's trembling "
                                                                          'shoulders and softly hum the '
                                                                          'gentle four-hand clavecin '
                                                                          'melody from Quartier Lyonnais.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N19_C10A2_R2',
                                                                  'speaker': 'Furina',
                                                                  'text': '...You are slightly flat on the '
                                                                          'third measure, my dear '
                                                                          'assistant. Still... keep '
                                                                          'humming it like that. Somehow '
                                                                          'the courtroom ghosts sound '
                                                                          'terribly small beside you.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                                                  'voice_emotion': 'vn_tender_love'}]}]},
                      'routing': [],
                      'ending_id': None},
           'N20_A3': {'node_id': 'N20_A3',
                      'chapter_id': 'CH3',
                      'title': 'The Glass Wall at the Footlights',
                      'day_label': 'Day 8 - 11:30 PM',
                      'location': 'Sunken Erinnyes Cistern - Mirror Footlights',
                      'beats': [{'beat_id': 'N20_B01',
                                 'speaker': 'Narrator',
                                 'text': 'As we approach the sunken stage apron at half-past eleven, the '
                                         'three Spotlight Meks flare awake at once -- dropping a '
                                         'shimmering curtain of solid blue Indemnitium light directly '
                                         'along the footlights between us!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Psychic rime-mist coils off the mirror water, reading the '
                                         'deepest unspoken fear inside both our chests. Before my eyes '
                                         'rises an empty crimson auditorium a thousand years hence -- Seat '
                                         'Number One covered in dust long after mortal lives have faded.',
                                 'inner_thought': 'The same immortal dread that haunts every star-crossing '
                                                  'traveler: outliving the warm hand you hold.',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B03',
                                 'speaker': 'Narrator',
                                 'text': 'On the stage side of the glowing glass wall, Furina stares into '
                                         'her own reflection -- a small, powerless girl left alone under '
                                         "blinding spotlights once the Traveler's pity moves on to another "
                                         'nation.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B04',
                                 'speaker': 'Furina',
                                 'text': 'Stay back behind the footlights, Aether! Seat Number One is safe '
                                         '-- spectators are supposed to clap when the curtain falls and '
                                         'walk away unharmed! Why step onto a sinking stage for an actress '
                                         'whose play is already over?!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_E1',
                                 'speaker': 'Narrator',
                                 'text': 'Frost creeps across the brass footlight rail between our boots, '
                                         'singing in a razor-high soprano pitch that makes the air ache.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_E2',
                                 'speaker': 'Furina',
                                 'text': 'Look at that empty crimson chair in the mist behind you, Aether! '
                                         'Mortal years burn past like flash-paper to a star from beyond '
                                         'the sky -- why bind your hands to a fleeting human winter?!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_E3',
                                 'speaker': 'Aether',
                                 'text': 'Is that what this mirage is showing you on your side of the '
                                         'glass -- me walking out of the theater once your hair turns '
                                         'silver?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_E4',
                                 'speaker': 'Furina',
                                 'text': 'Do not answer unless you mean every syllable!! Five hundred '
                                         'years of acting taught me to hear a polite lie from across an '
                                         'entire auditorium!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B05',
                                 'speaker': 'Narrator',
                                 'text': 'Across the razor-cold wall of blue footlight, her ungloved '
                                         'fingertips tremble half an inch from the glass -- terrified to '
                                         'ask, terrified I might step back.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C11_A',
                                 'prompt': 'Blinding Indemnitium footlights divide Seat Number One from '
                                           "Furina's trembling hand on the stage:",
                                 'options': [{'opt_id': 'C11_A1_COSTAR_VOW',
                                              'label': 'Step straight through the burning footlights and '
                                                       'lace your fingers through hers: swear a Mortal '
                                                       'Co-Star Vow.',
                                              'effects': {'bond': 2,
                                                          'insight': 1,
                                                          'add_flags': ['F09_COSTAR_VOW']},
                                              'next_node': 'N28_A4',
                                              'reaction_beats': [{'beat_id': 'N20_C11A1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Ignoring the thousand-year '
                                                                          'mirage, I drive my boot '
                                                                          'straight across the footlight '
                                                                          'barrier! Frost-blue sparks hiss '
                                                                          'harmlessly off my golden aura '
                                                                          "as I catch both of Furina's "
                                                                          'cold hands in mine.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_vow_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A1_R2',
                                                                  'speaker': 'Aether',
                                                                  'text': 'I never came to Fontaine to '
                                                                          'pity you from a velvet chair, '
                                                                          'Furina! Tear up the solo script '
                                                                          '-- from tonight onward, I am '
                                                                          'standing right here on the '
                                                                          'boards as your co-star!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_vow_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A1_R3',
                                                                  'speaker': 'Furina',
                                                                  'text': '...Foolish, reckless co-star. '
                                                                          'Hold tight then, Aether -- '
                                                                          'because once you cross Furina '
                                                                          "de Fontaine's footlights, I "
                                                                          'will never let you retreat to '
                                                                          'the audience again!',
                                                                  'inner_thought': 'Vow Sealed [Mortal '
                                                                                   'Co-Star Vow]: The '
                                                                                   'invisible wall between '
                                                                                   'Seat Number One and '
                                                                                   'the stage shatters '
                                                                                   'into warm starlight!',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_vow_diff.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C11_A2_CRITIC_SEVER',
                                              'when': {'min_insight': 7},
                                              'unlock_badge': '[INSIGHT 7]',
                                              'lock_hint': '[LOCKED: Needs Insight 7]',
                                              'label': "Remain on the audience side and cleave the prism's "
                                                       'structural seam with cold blade precision -- '
                                                       'guarding her without crossing the line.',
                                              'effects': {'bond': 0,
                                                          'insight': 0,
                                                          'add_flags': ['DETACHED_SPECTATOR_NO_DUET']},
                                              'next_node': 'N28_A4',
                                              'reaction_beats': [{'beat_id': 'N20_C11A2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Keeping my boots planted firmly '
                                                                          'on the auditorium side of the '
                                                                          "brass rail, I read the prism's "
                                                                          'refractive nodal seam and '
                                                                          'strike the flat of my dull '
                                                                          'blade cleanly against the outer '
                                                                          'lens.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A2_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'The psychic mirage shatters '
                                                                          'into harmless mist -- saving us '
                                                                          'both without a scratch -- yet '
                                                                          'Furina slowly draws her '
                                                                          'unclasped hand back against her '
                                                                          'ribboned bodice, nodding with '
                                                                          'quiet, dignified distance.',
                                                                  'inner_thought': 'Note: The mirage is '
                                                                                   'broken, yet by staying '
                                                                                   'behind the rail I left '
                                                                                   'the glass wall between '
                                                                                   'spectator and star '
                                                                                   'intact.',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C11_A3_RETREAT_AISLE',
                                              'label': 'Step half a pace backward toward Seat Number One '
                                                       "before the thousand-year mirage: 'Come back behind "
                                                       "the rail where it is safe...'",
                                              'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N21_BAD1_1',
                                              'reaction_beats': [{'beat_id': 'N20_C11A3_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'For one fatal heartbeat, the '
                                                                          'vision of that dust-covered '
                                                                          'empty seat freezes my breath -- '
                                                                          'and my heel shifts half a step '
                                                                          'backward toward the safety of '
                                                                          'the aisle.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A3_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': "Furina's heterochromatic eyes "
                                                                          'widen by a fraction of an inch. '
                                                                          'Then, with five hundred years '
                                                                          'of practiced perfection, an '
                                                                          'impenetrable theatrical smile '
                                                                          'locks across her pale face.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N21_BAD1_1': {'node_id': 'N21_BAD1_1',
                          'chapter_id': 'CH3',
                          'title': 'Ninety Days of Winter Ice',
                          'day_label': 'Day 9 - 12:15 AM to Dawn',
                          'location': 'Sunken Cistern & Shuttered Opera Epiclese',
                          'beats': [{'beat_id': 'N21_B01',
                                     'speaker': 'Furina',
                                     'text': 'Bravo -- a sensible spectator knows exactly where the safety '
                                             "rail stands! Do forgive a dramatic director's late-night "
                                             'prank, my dear Traveler; this damp cellar is hardly fit for '
                                             'an honored guest.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_footlights_mirage_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B02',
                                     'speaker': 'Narrator',
                                     'text': 'As our resonance fractures, the cistern water surges upward '
                                             "in jagged frost waves! Hearing Clorinde's emergency whistle "
                                             'from the upper stair, a pillar of sovereign azure authority '
                                             'parts the outer cascade from above.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B03',
                                     'speaker': 'Neuvillette',
                                     'text': 'Stand clear of the basin rim, Traveler, Lady Furina. Without '
                                             'a willing dual harmonic anchor below, this cistern cannot be '
                                             "left unsealed until tonight's Solstice tide.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B03B',
                                     'speaker': 'Furina',
                                     'text': 'Wait, Monsieur Neuvillette -- if you freeze the sub-stage '
                                             'conduit from outside, the entire Opera Epiclese will be '
                                             'locked in ice all winter!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B03C',
                                     'speaker': 'Neuvillette',
                                     'text': 'An empty theater for ninety winter days is a price Fontaine '
                                             'can bear, Lady Furina. Losing you to an ungrounded rupture '
                                             'tonight is not.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B03D',
                                     'speaker': 'Narrator',
                                     'text': "Wrapped in Clorinde's spare cloak beside the plaza basin, "
                                             'Furina does not look at me once -- staring straight ahead at '
                                             'the sleet with dry, fiercely guarded eyes.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B04',
                                     'speaker': 'Narrator',
                                     'text': 'At dawn on Day Nine, emergency notices go up across every '
                                             'aquabus terminal in Fontaine: the Fontinalia Centennial Gala '
                                             'is indefinitely postponed.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_E1',
                                     'speaker': 'Clorinde',
                                     'text': 'Aether, take my hand up the last rung -- Monsieur '
                                             'Neuvillette is sealing the plaza grates right behind us!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_E2',
                                     'speaker': 'Aether',
                                     'text': 'Furina, wait on the upper step -- back at the footlights I '
                                             'only hesitated for half a breath!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_E3',
                                     'speaker': 'Furina',
                                     'text': 'Half a breath on stage is an entire missed cue, my dear '
                                             'Traveler! Go warm yourself at Hotel Debord; this director '
                                             'has winter paperwork to sign.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_E4',
                                     'speaker': 'Narrator',
                                     'text': 'Hoarfrost races across the marble basin of Lucine as '
                                             "Neuvillette's cane strikes the stone, locking the "
                                             'subterranean grief -- and our unfinished words -- under '
                                             'solid winter glass.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N21_B05',
                                     'speaker': 'Narrator',
                                     'text': 'Descending alone to the plaza rim under gray sleet, Monsieur '
                                             'Neuvillette drives a Ninety-Day Hydro-Stasis Seal straight '
                                             'through the foundations of the Opera Epiclese -- encasing '
                                             'the entire sub-stage conduit in silent winter ice until the '
                                             'Spring Equinox.',
                                     'inner_thought': "The city is spared tonight's rupture, yet the Opera "
                                                      "House stands shuttered in frost -- and Furina's "
                                                      'right wrist remains numb.',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch3a_cistern_masks_base.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [{'default': True, 'next_node': 'N22_BAD1_2'}],
                          'ending_id': None},
           'N22_BAD1_2': {'node_id': 'N22_BAD1_2',
                          'chapter_id': 'CH3',
                          'title': 'Steamer Whistle at Lumidouce Pier',
                          'day_label': 'Day 9 - 04:30 PM (Navia Line East)',
                          'location': 'Lumidouce Harbor - Northern Steamer Pier',
                          'beats': [{'beat_id': 'N22_B01',
                                     'speaker': 'Narrator',
                                     'text': 'That afternoon, Charlotte rushes word to Hotel Debord: '
                                             'unable to bear walking past the ice-sealed Opera House while '
                                             'my departure for Natlan draws near, Furina took the Navia '
                                             'Line aquabus east to Lumidouce Harbor.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_B02',
                                     'speaker': 'Narrator',
                                     'text': 'Cold winter drizzle blurs the brass cranes of Lumidouce Pier '
                                             'when I catch up to the gangplank. Beneath a navy silk '
                                             'parasol tilted neatly against the rain stands Furina beside '
                                             'two brass-cornered trunks.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_B03',
                                     'speaker': 'Furina',
                                     'text': 'Oh, do not pull such a solemn face in the rain, Traveler! '
                                             'With the Opera Epiclese closed for ninety days of winter '
                                             'maintenance, Dornman Port begged for a guest stage '
                                             'consultant -- a star must go where the footlights are warm!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_B04',
                                     'speaker': 'Narrator',
                                     'text': 'Her chin stays regally lifted, yet I see the truth behind '
                                             'her bright excuse: she is fleeing north for the ninety days '
                                             'of winter stasis, intending to return alone when the ice '
                                             'thaws at the Spring Equinox after I have already crossed '
                                             'into Natlan.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_B05_RETURN_F07',
                                     'speaker': 'Narrator',
                                     'text': 'Keeping the promise I made in Chioriya Boutique, I draw the '
                                             "velvet pouch holding 'L'Etoile d'Eau' from over my heart and "
                                             'set her sapphire-plume star pin gently atop her steamer '
                                             'trunk.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': '',
                                     'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                    {'beat_id': 'N22_B06_RETURN_F07',
                                     'speaker': 'Furina',
                                     'text': '...Ah. Ever punctual with the stage props, are you not? '
                                             'Thank you for keeping it dry until curtain down, Seat Number '
                                             'One.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': '',
                                     'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                    {'beat_id': 'N22_E1',
                                     'speaker': 'Aether',
                                     'text': 'Dornman Port is halfway across northern Mondstadt, Furina. '
                                             'You hate cold sea wind off the northern coast.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_E2',
                                     'speaker': 'Furina',
                                     'text': 'A versatile artist broadens her repertoire! Besides, cider '
                                             'and windwheel ballads will make a refreshing change from '
                                             'soggy Fontainian drizzle!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_E3',
                                     'speaker': 'Narrator',
                                     'text': 'Raindrops drum steadily on taut navy silk between us. '
                                             'Neither of us mentions the ninety-day countdown until the '
                                             'Spring Equinox thaw.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_E4',
                                     'speaker': 'Furina',
                                     'text': 'First bell from the wheelhouse... Farewell for the winter '
                                             'season, Traveler.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N22_B07',
                                     'speaker': 'Narrator',
                                     'text': "Steam hisses from the northern packet ship's funnel as "
                                             'deckhands unhook the mooring chains. Furina steps onto the '
                                             'wet gangplank, holding her navy silk parasol like a shield '
                                             'between our eyes.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                     'voice_emotion': ''}],
                          'choice': {'choice_id': 'C19_BAD1',
                                     'prompt': "Steam billows across Lumidouce Pier as Furina's northern "
                                               'steamer prepares to cast off:',
                                     'options': [{'opt_id': 'C19_A_LEAVE_BELL',
                                                  'label': 'Lay a fresh blue Lumidouce Belle quietly '
                                                           'beside her trunk without stripping away her '
                                                           'proud farewell mask.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD1_BELL_LEFT']},
                                                  'next_node': 'END_BAD_1',
                                                  'reaction_beats': [{'beat_id': 'N22_C19A_R1',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'Choosing to honor the '
                                                                              'dignity she fought five '
                                                                              'centuries to keep, I set a '
                                                                              'single rain-wet Lumidouce '
                                                                              'Belle beside her trunk and '
                                                                              'bow politely from the stone '
                                                                              'pier as the gangplank '
                                                                              'rises.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N22_C19A_R2',
                                                                      'speaker': 'Furina',
                                                                      'text': 'Safe travels to blazing '
                                                                              'Natlan, my honored Seat '
                                                                              'Number One... May every '
                                                                              'stage you pass greet you '
                                                                              'with warmer skies than '
                                                                              "Fontaine's winter.",
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N22_C19A_R3',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'Only as the steamer glides '
                                                                              'into the gray channel fog '
                                                                              'does the navy silk parasol '
                                                                              'dip forward -- hiding the '
                                                                              'small figure clutching that '
                                                                              'blue flower against her '
                                                                              'numb right wrist.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                                                      'voice_emotion': ''}]},
                                                 {'opt_id': 'C19_B_CALL_FURINA',
                                                  'label': 'Cup your hands and call her mortal name -- '
                                                           "'Furina!' -- across the steamer whistle and "
                                                           'winter rain.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD1_NAME_CALLED']},
                                                  'next_node': 'END_BAD_1',
                                                  'reaction_beats': [{'beat_id': 'N22_C19B_R1',
                                                                      'speaker': 'Aether',
                                                                      'text': 'Furina! You do not have to '
                                                                              'carry the Spring Equinox '
                                                                              'thaw alone -- send word '
                                                                              'from Dornman Port, and I '
                                                                              'will come back from the '
                                                                              'edge of Teyvat if you call!',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N22_C19B_R2',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'Through the shriek of the '
                                                                              'steam whistle, her small '
                                                                              'shoulders stiffen on the '
                                                                              'aft deck. Her gloved '
                                                                              'fingers tighten '
                                                                              'white-knuckled around the '
                                                                              'parasol handle, refusing to '
                                                                              'turn around lest I see her '
                                                                              'weeping.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N22_C19B_R3',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'She lifts her free hand in '
                                                                              'one last, trembling '
                                                                              'curtain-call wave without '
                                                                              'looking back -- vanishing '
                                                                              'into the northern rain '
                                                                              'while Seat Number One '
                                                                              'remains empty behind us.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad1_lumidouce_parasol.jpg',
                                                                      'voice_emotion': ''}]}]},
                          'routing': [],
                          'ending_id': None},
           'N23_B1': {'node_id': 'N23_B1',
                      'chapter_id': 'CH3',
                      'title': 'Emergency Briefing at Palais Mermonia',
                      'day_label': 'Day 8 - 09:30 AM',
                      'location': 'Palais Mermonia - High Judicial Study',
                      'beats': [{'beat_id': 'N23_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Rain taps steadily against the tall arched windows of Palais '
                                         'Mermonia as Monsieur Neuvillette unrolls a five-hundred-year-old '
                                         'hydro-engineering chart across his desk before Navia, Clorinde, '
                                         'Charlotte, Paimon, and me.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B02',
                                 'speaker': 'Neuvillette',
                                 'text': 'My nocturnal inspection confirmed our worst suspicion. Even if '
                                         'we disconnect the Pneumousia Grand Organ completely, tomorrow '
                                         "night's eleven-o'clock Winter Solstice Hydro-Tide will still "
                                         'force the sunken Erinnyes cistern into full acoustic rupture.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B03',
                                 'speaker': 'Navia',
                                 'text': 'Seven pressure-relief sluice-valves ring Erinnyes Island from '
                                         "Marcotte Station to the Navia Line pilings! Spina di Rosula's "
                                         'divers and Clorinde can reinforce the outer six today, while '
                                         'Freminet tests a Ley-Line resonance bell at Lucine Plaza.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B03B',
                                 'speaker': 'Paimon',
                                 'text': 'Wait -- why only six outer sluice-valves, Navia? Where is '
                                         'Sluice-Valve Number Seven?!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B03C',
                                 'speaker': 'Clorinde',
                                 'text': 'Valve Seven sits directly on the umbilical pipe between '
                                         "Marcotte's deep main and the mirror cistern's inner ring. If the "
                                         "inner curtain ever locks tomorrow night, Valve Seven's "
                                         'twelve-second backflow is the only mechanical seam in the wall.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B03D',
                                 'speaker': 'Aether',
                                 'text': "And what about Furina herself? Did she come to Palais Mermonia's "
                                         'briefing this morning?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_E1',
                                 'speaker': 'Neuvillette',
                                 'text': 'Even if we evacuated Erinnyes Island tomorrow night, an unvented '
                                         'rupture beneath Lucine would shatter five centuries of '
                                         'Fontainian hydro-veins across the Court.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_E2',
                                 'speaker': 'Navia',
                                 'text': "Not on Spina di Rosula's watch! My father helped repair "
                                         "Marcotte's outer aqueducts twenty years ago -- our riggers know "
                                         'every bronze bolt on those six outer valves!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_E3',
                                 'speaker': 'Paimon',
                                 'text': 'And Paimon and Charlotte will check every rehearsal room on '
                                         'Erinnyes so Furina cannot sneak off without supper!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_E4',
                                 'speaker': 'Clorinde',
                                 'text': 'Meet Freminet and me at the Fountain of Lucine by two-thirty, '
                                         'Aether. Time is already tight.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B04',
                                 'speaker': 'Charlotte',
                                 'text': 'Meanwhile Miss Furina locked herself inside Studio Three at the '
                                         "Opera House claiming she is 'polishing curtain bows'! Keep your "
                                         "eyes peeled out on Erinnyes, Aether -- my reporter's instinct "
                                         'says our director is hiding a solo stunt!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N24_B2'}],
                      'ending_id': None},
           'N24_B2': {'node_id': 'N24_B2',
                      'chapter_id': 'CH3',
                      'title': "Freminet's Ley-Line Quartz Bell at Lucine Plaza",
                      'day_label': 'Day 8 - 02:30 PM (Erinnyes Island)',
                      'location': 'Fountain of Lucine - Outer Drainage Rim',
                      'beats': [{'beat_id': 'N24_B01',
                                 'speaker': 'Narrator',
                                 'text': 'By mid-afternoon beside the Fountain of Lucine, Freminet kneels '
                                         'over a brass-cased Ley-Line Quartz Bell with his clockwork '
                                         'penguin Pers while Lynette records acoustic readings under a '
                                         'black umbrella.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_B02',
                                 'speaker': 'Freminet',
                                 'text': 'Um... watch the pale quartz tuning core inside the bell, '
                                         'Traveler. Whether someone is born in Fontaine or visiting from '
                                         "Mondstadt or Sumeru, anyone recorded in Teyvat's Ley Lines makes "
                                         'the quartz chime on middle C.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_B03',
                                 'speaker': 'Narrator',
                                 'text': 'Lynette tilts the bell toward Clorinde, then toward a passing '
                                         'Sumeru scholar -- chime, chime, clear as silver glass. Yet the '
                                         'instant Freminet angles the quartz ray across my chest, the '
                                         'crystal falls dead, eerie, absolute blank silence.',
                                 'inner_thought': 'Not a single ripple. To an instrument tuned to '
                                                  "Irminsul's Ley Lines, the Fourth Descender is an "
                                                  'unrecorded void.',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_B04',
                                 'speaker': 'Freminet',
                                 'text': "Ah -- I am so sorry! Pers's auxiliary mainspring must have "
                                         'slipped its final tooth in the damp air... This spare quartz '
                                         'core went completely uncalibrated when it scanned you.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_E1',
                                 'speaker': 'Lynette',
                                 'text': "Observation: Pers's gear train shows zero mechanical slippage. "
                                         'The acoustic void originates entirely from Aether.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_E2',
                                 'speaker': 'Freminet',
                                 'text': 'Eh?! From the Traveler himself? Like diving beneath sea-ice into '
                                         'water that leaves zero echo on sonar...',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_E3',
                                 'speaker': 'Aether',
                                 'text': 'Keep that reading between the four of us for now, Freminet, '
                                         "Lynette. Beneath tomorrow night's Gala, being unrecorded by "
                                         "Teyvat's Ley Lines may be our strongest shield.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_E4',
                                 'speaker': 'Narrator',
                                 'text': 'Pers gives a crisp brass salute with one flipper while harbor '
                                         'wind whips mist off the Navia Line arches.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N24_B05',
                                 'speaker': 'Clorinde',
                                 'text': "Spina di Rosula's riggers just signaled from the Marcotte "
                                         "Station aqueduct, Aether. Either examine Freminet's blank quartz "
                                         'core here, or come reinforce the six outer sluice-valves with '
                                         'Navia and me before dusk.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C13_B',
                                 'prompt': 'Two critical engineering leads open across Erinnyes Island '
                                           'before Night Eight falls:',
                                 'options': [{'opt_id': 'C13_B_CRYSTAL',
                                              'label': "Ask Freminet to entrust the 'uncalibrated' Blank "
                                                       'Tuning Quartz Crystal to you for phase-split '
                                                       'testing.',
                                              'effects': {'bond': 0,
                                                          'insight': 2,
                                                          'add_flags': ['F10_BLANK_TUNING_CRYSTAL']},
                                              'next_node': 'N25_B3',
                                              'reaction_beats': [{'beat_id': 'N24_C13A_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': "Pers's clockwork did not slip, "
                                                                          'Freminet -- this blank quartz '
                                                                          'core is tuned to my exact '
                                                                          'outlander frequency. May I '
                                                                          "carry it until tomorrow night's "
                                                                          'Gala?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N24_C13A_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Freminet nods earnestly and '
                                                                          'presses the palm-sized prism of '
                                                                          'clear, unlinked quartz into my '
                                                                          'hand; cool golden starlight '
                                                                          'hums faintly inside its facets.',
                                                                  'inner_thought': 'Item Acquired [Blank '
                                                                                   'Tuning Quartz '
                                                                                   'Crystal]: Unbound to '
                                                                                   "Teyvat's Ley Lines, "
                                                                                   'this crystal can '
                                                                                   'phase-split an '
                                                                                   'Indemnitium barrier!',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C13_B_SLUICES',
                                              'label': "Join Clorinde and Navia's crew across Marcotte "
                                                       'Station and the Navia Line pilings to master the '
                                                       'six sluice-valves.',
                                              'effects': {'bond': 2,
                                                          'insight': 0,
                                                          'add_flags': ['F12_SLUICE_CADENCE']},
                                              'next_node': 'N25_B3',
                                              'reaction_beats': [{'beat_id': 'N24_C13B_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Through four hours of cold mist '
                                                                          'alongside Clorinde and Navia, '
                                                                          'we torque down the bronze '
                                                                          'relief wheels from Marcotte '
                                                                          'Station to the Navia Line '
                                                                          'aqueduct piers -- timing how '
                                                                          "Valve Seven's backflow vents "
                                                                          'straight into the mirror '
                                                                          'cistern.',
                                                                  'inner_thought': 'Tactical Mastery '
                                                                                   '[Marcotte Sluice '
                                                                                   'Cadence]: Clorinde and '
                                                                                   'I memorized the exact '
                                                                                   '12-second backflow '
                                                                                   'window into the inner '
                                                                                   'cistern!',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N24_C13B_R2',
                                                                  'speaker': 'Clorinde',
                                                                  'text': 'Solid work, Aether -- Furina '
                                                                          'smiled with genuine relief from '
                                                                          'the Opera balcony when she saw '
                                                                          'you bracing the aqueduct team '
                                                                          'yourself. Remember our whistle '
                                                                          'signal on Valve Seven tomorrow '
                                                                          'night.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3b_quartz_bell_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N25_B3': {'node_id': 'N25_B3',
                      'chapter_id': 'CH3',
                      'title': 'The Spare Brass Key at 11:30 PM',
                      'day_label': 'Day 8 - 11:30 PM',
                      'location': "Quartier Lyonnais - Furina's Darkened Apartment",
                      'beats': [{'beat_id': 'N25_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Returning to the Court of Fontaine on the last night boat, I '
                                         'look up from the wet cobblestones of Quartier Lyonnais -- for '
                                         "the first night all week, Furina's second-floor apartment "
                                         'windows are completely dark.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B02',
                                 'speaker': 'Narrator',
                                 'text': 'The Opera night watch sent word that she camped on a sofa in '
                                         'Rehearsal Room Three on Erinnyes Island. Unease prickling at my '
                                         'neck, I draw my Assistant Director spare brass key and let '
                                         'myself quietly inside.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B03',
                                 'speaker': 'Narrator',
                                 'text': 'Moonlight slants across an eerily immaculate room. Stacked '
                                         'beside the cold hearth lie half-charred sheets of freshly ruled '
                                         "music paper -- a solo Act Four Cadenza written in Furina's own "
                                         'looping script, ending on a jagged ink blot!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B03B',
                                 'speaker': 'Narrator',
                                 'text': 'On the chaise longue where I slept on Night One, her three '
                                         'velvet Salon cushions sit plumped in neat row-order, with a '
                                         'folded wool blanket laid ready as though wishing her guest warm '
                                         'rest after she is gone.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B03C',
                                 'speaker': 'Aether',
                                 'text': "...'Scene 182,376 -- Final Solo Revision.' Furina, you stubborn, "
                                         'self-sacrificing actress -- you are trying to carry the whole '
                                         'cistern on your own throat tomorrow night!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B04_CLUES',
                                 'speaker': 'Narrator',
                                 'text': 'Beside the inkwell sit five crumpled brown-sugar packets next to '
                                         "a cold teacup and a landlord's receipt stamping six months of "
                                         'rent paid in advance -- the exact quiet house-tidying Maitre '
                                         'Renaud performed before hiding away forever.',
                                 'inner_thought': 'She never meant to conduct from the upper pit tomorrow '
                                                  'night -- she intends to descend into the cistern alone '
                                                  'at 10:55 PM!',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'any_flags': ['F05_LUTIST_SCORE', 'F11_SUGAR_TIN_CLUE']}},
                                {'beat_id': 'N25_E1',
                                 'speaker': 'Narrator',
                                 'text': 'Beside the cold stove sits her copper macaroni saucepan, '
                                         'scrubbed spotless and hung on its brass hook as if closing up a '
                                         'beloved cottage for winter.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_E2',
                                 'speaker': 'Narrator',
                                 'text': 'Tucked beneath the edge of the inkwell is a spare front-row '
                                         "ticket stamped 'SEAT NO. 1 -- ADMIT ONE' in fresh gold ink.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_E3',
                                 'speaker': 'Aether',
                                 'text': 'You wanted me safely up in the velvet stalls applauding the pipe '
                                         'organ while you went down into the cistern alone...',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_E4',
                                 'speaker': 'Narrator',
                                 'text': 'Locking her apartment door carefully behind me with the spare '
                                         'brass key, I race back through the midnight drizzle toward the '
                                         'Erinnyes ferry.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N25_B04_BASE',
                                 'speaker': 'Narrator',
                                 'text': 'Beside the inkwell sit five crumpled brown-sugar packets next to '
                                         "an untouched cup and a landlord's receipt stamping six months of "
                                         'rent paid in advance -- as if the tenant tidy-cleaned her home '
                                         'before a journey she might not return from.',
                                 'inner_thought': "Why pay half a year's rent ahead and burn a solo "
                                                  'Cadenza draft on the eve of her own Gala?!',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3b_empty_lyonnais_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'forbid_flags': ['F05_LUTIST_SCORE', 'F11_SUGAR_TIN_CLUE']}}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N29_B4'}],
                      'ending_id': None},
           'N26_C1': {'node_id': 'N26_C1',
                      'chapter_id': 'CH3',
                      'title': 'Mandatory Vocal Rest on Erinnyes Bluff',
                      'day_label': 'Day 8 - 12:00 PM (Erinnyes Island)',
                      'location': 'Cypress Bluff Above Lucine -> Serenitea Pot',
                      'beats': [{'beat_id': 'N26_B01',
                                 'speaker': 'Narrator',
                                 'text': 'High noon on Day Eight finds Navia, Charlotte, and Paimon '
                                         'standing arms-crossed in front of the Opera Epiclese rehearsal '
                                         'doors -- forming a cheerfully unbreakable blockade.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B02',
                                 'speaker': 'Navia',
                                 'text': 'Motion carried unanimously by Spina di Rosula and The Steambird! '
                                         'Assistant Director Aether has invoked emergency vocal-rest '
                                         'protocol -- we will handle the stagehands while Miss Furina '
                                         'rests inside the Serenitea Pot!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B03',
                                 'speaker': 'Furina',
                                 'text': 'Mutiny! Broad-daylight mutiny against your own director! '
                                         '...Wait, Aether, you brought the lemon-cream scones from Hotel '
                                         'Debord too? Hmph. Forty-eight hours, not a minute longer!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N26_B03B',
                                 'speaker': 'Charlotte',
                                 'text': 'Hehe, you heard her on the record, everyone! One peep of '
                                         'stage-shouting before Gala night and The Steambird prints '
                                         "'Runaway Patient Escapes Cozy Teapot'!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B03C',
                                 'speaker': 'Paimon',
                                 'text': 'Tubby already brewed fresh Bulle Fruit tea on the veranda, '
                                         'Furina! Leave the noisy pipes outside to us!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B04',
                                 'speaker': 'Narrator',
                                 'text': 'Setting the Serenitea Pot inside a sheltered cypress hollow on '
                                         "Erinnyes Bluff -- scarcely three minutes' walk above the "
                                         'Fountain of Lucine -- I guide Furina into the warm spring '
                                         'sunlight of our Fontainian Courtyard Villa.',
                                 'inner_thought': 'Safe inside the Realm Within, no stray sub-bass tremor '
                                                  'from the cistern below can scrape her throat.',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_E1',
                                 'speaker': 'Furina',
                                 'text': 'Ooh, look how tall the Lumidouce Belles grew along your '
                                         'courtyard fountain, Aether! Wait -- did Tubby set an entire '
                                         'outdoor pastry tea-cart on the upper terrace?!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': 'outing_arrive_photo'},
                                {'beat_id': 'N26_E2',
                                 'speaker': 'Aether',
                                 'text': "Strict physician's orders: warm spring breeze, zero cold mist, "
                                         'and zero rehearsals above a whisper until tomorrow evening.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_E3',
                                 'speaker': 'Furina',
                                 'text': 'Hmph. Tyranny dressed in hospitality is the most dangerous kind '
                                         'of tyranny, my dear assistant!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N26_E4',
                                 'speaker': 'Narrator',
                                 'text': 'Despite her theatrical protest, the tight knot between her '
                                         'shoulders visibly loosens as afternoon warmth wraps around her.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B05',
                                 'speaker': 'Narrator',
                                 'text': "Unpinning her heavy director's hat on the parlor stand with an "
                                         'involuntary sigh of relief, Furina sinks into the sun-warmed '
                                         'cushions as gentle breeze stirs the Lumidouce Belles outside.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N27_C2'}],
                      'ending_id': None},
           'N27_C2': {'node_id': 'N27_C2',
                      'chapter_id': 'CH3',
                      'title': 'The Salon Solitaire Contract Tribunal',
                      'day_label': 'Day 8 - 04:00 PM to Dusk',
                      'location': 'Serenitea Pot - Fontaine Villa Parlor',
                      'beats': [{'beat_id': 'N27_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Using temporary Realm Dispatch tokens so Paimon and Chiori can '
                                         'drop by with fresh tailoring pins and afternoon tea before '
                                         'returning outside at dusk, the villa parlor soon turns into an '
                                         'impromptu courtroom.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Hatless on the velvet parlor settee in a cream-and-sapphire '
                                         'cardigan, Furina appoints Gentilhomme Usher bailiff over a '
                                         "towering scroll titled 'Ninety-Nine Duties of a Permanent "
                                         "Assistant Director'.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B03',
                                 'speaker': 'Chiori',
                                 'text': 'Clause Twelve demands that Aether carry reserve macarons in rain '
                                         'or shine, yet Clause Forty-Nine transfers full archive custody '
                                         "of your scripts to him 'in case of extended vocal sabbatical'? "
                                         'Subtle as a brass tuba, Furina.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B04',
                                 'speaker': 'Furina',
                                 'text': 'Ahem! Boilerplate theatrical insurance, Chiori -- every great '
                                         'troupe files contingency clauses! Well, Aether? The Salon '
                                         'Solitaire awaits your counter-plea!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': 'outing_cruise'},
                                {'beat_id': 'N27_E1',
                                 'speaker': 'Paimon',
                                 'text': 'Hey! Clause Seventy-Three says Paimon only gets every THIRD '
                                         'damaged macaron from the prop table?! Paimon demands a recount '
                                         'from Bailiff Usher!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_E2',
                                 'speaker': 'Chiori',
                                 'text': 'Overruled by the costume department, Paimon -- last time you got '
                                         'crumbs on silk tulle, it took me two hours with a horsehair '
                                         'brush.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_E3',
                                 'speaker': 'Furina',
                                 'text': 'Order, order in the parlor! The bench now turns to the Principal '
                                         'Defendant -- Assistant Director Aether -- with quill in hand!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': 'vn_sweet_happy'},
                                {'beat_id': 'N27_E4',
                                 'speaker': 'Narrator',
                                 'text': 'Sunlight slants across Clause Forty-Nine half-buried in the '
                                         'middle of the parchment roll while Furina watches my eyes more '
                                         'closely than she pretends.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B05',
                                 'speaker': 'Narrator',
                                 'text': 'Even as she waves her quill with her left hand, she keeps her '
                                         'right wrist tucked deep inside the pleated lace cuff resting on '
                                         'her knee.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C16_C',
                                 'prompt': 'Gentilhomme Usher holds out the 99-Clause Contract scroll '
                                           'across the sunlit parlor tea table:',
                                 'options': [{'opt_id': 'C16_C1',
                                              'label': "Audit Clause 49's archive-transfer wording line by "
                                                       'line while watching how carefully she hides her '
                                                       'right cuff.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N33_C3',
                                              'reaction_beats': [{'beat_id': 'N27_C16C1_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Clause Forty-Nine is written '
                                                                          'like a final estate handover, '
                                                                          'Furina -- and you have not used '
                                                                          'your right hand to lift your '
                                                                          'teacup once all afternoon. '
                                                                          'Strike that sabbatical line; '
                                                                          'the director keeps her own '
                                                                          'scripts.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N27_C16C1_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Chiori shoots me a quiet nod of '
                                                                          'approval before using her Realm '
                                                                          'Dispatch token at dusk, while '
                                                                          'Furina tugs her right lace cuff '
                                                                          'lower with a flustered clear of '
                                                                          'her throat.',
                                                                  'inner_thought': 'Even inside this warm '
                                                                                   'realm, the sensory '
                                                                                   'chill from Night One '
                                                                                   'has crept farther past '
                                                                                   'her right wrist.',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C16_C2',
                                              'label': 'Sign with a sweeping flourish and add Clause 100: '
                                                       "'Neither party may bow out before sharing "
                                                       "dessert.'",
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N33_C3',
                                              'reaction_beats': [{'beat_id': 'N27_C16C2_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Signed in full -- provided the '
                                                                          'court ratifies Clause One '
                                                                          'Hundred: any director '
                                                                          'attempting a solo exit forfeits '
                                                                          'fifty boxes of Laullette '
                                                                          'macarons on the spot!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N27_C16C2_R2',
                                                                  'speaker': 'Furina',
                                                                  'text': 'Pffft -- fifty boxes?! '
                                                                          'Mademoiselle Crabaletta, '
                                                                          'sustain that ridiculous '
                                                                          'amendment at once before I '
                                                                          'laugh my sore throat raw!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch3c_teapot_tribunal_base.jpg',
                                                                  'voice_emotion': 'vn_sweet_happy'}]}]},
                      'routing': [],
                      'ending_id': None},
           'N28_A4': {'node_id': 'N28_A4',
                      'chapter_id': 'CH4',
                      'title': 'Noon Supply Drop & Vigil Under the Organ Pipes',
                      'day_label': 'Day 9 - 12:00 PM to 10:15 PM',
                      'location': 'Sub-Stage Acoustic Resonance Chamber',
                      'beats': [{'beat_id': 'N28_B01',
                                 'speaker': 'Narrator',
                                 'text': 'After catching four hours of sleep wrapped in dry cloaks inside '
                                         "the upper acoustic gallery, Clorinde's promised knock echoes "
                                         'from the Lucine grate at noon -- lowering hot consomme, fresh '
                                         'lamp oil, and word that the Gala crowd is gathering above.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B01B',
                                 'speaker': 'Narrator',
                                 'text': "Tucked at the top of Clorinde's wicker basket is a small "
                                         "ribboned box of Navia's lemon macarons. Furina smiles "
                                         'gratefully, nibbles half a shell while thinking I am trimming '
                                         'the lantern wick -- and swallows without a flicker of taste in '
                                         'her eyes.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B01C',
                                 'speaker': 'Furina',
                                 'text': '...Tell me something while we wait for evening, Aether. Across '
                                         'all the nations you have walked, why linger twelve winter days '
                                         "inside one retired actress's noisy basement?",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B01D',
                                 'speaker': 'Aether',
                                 'text': 'Because in Scene 182,376 I could only watch your tears through a '
                                         'Hydro window without reaching you. Tonight, I am finally in the '
                                         'same room.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B02',
                                 'speaker': 'Narrator',
                                 'text': 'By a quarter past ten that night, the colossal brass bass pipes '
                                         'of the Pneumousia Grand Organ directly above our chamber begin '
                                         'to thrum -- less than forty-five minutes before the '
                                         "eleven-o'clock Winter Solstice Hydro-Tide locks phase.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B03_F05',
                                 'speaker': 'Aether',
                                 'text': 'Furina, look at the central tuning pillar beside the mirror '
                                         'dais. Maitre Renaud wrote in his unsent draft fifty years ago '
                                         "that singing Act Four's Cadenza solo down here deafened his ears "
                                         'in a single night -- you knew it would burn out your voice!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F05_LUTIST_SCORE']}},
                                {'beat_id': 'N28_B03_NO_F05',
                                 'speaker': 'Aether',
                                 'text': 'Furina, feel how violently that central tuning pillar is '
                                         'vibrating already. If you sing the Act Four Cadenza into that '
                                         'raw pressure wave without a counter-chord, the rebound will tear '
                                         'your vocal cords apart!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'forbid_flags': ['F05_LUTIST_SCORE']}},
                                {'beat_id': 'N28_B04',
                                 'speaker': 'Furina',
                                 'text': '...If trading one mortal singing voice could quiet five hundred '
                                         "years of tears without drowning Erinnyes's Gala night, I thought "
                                         'it was a fair bargain. Only... now that you are standing down '
                                         'here beside me, I find I want terribly to keep singing tomorrow.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_E1',
                                 'speaker': 'Narrator',
                                 'text': 'Overhead, muted applause from Act Two of the Gala filters '
                                         'faintly down through sixty feet of limestone and brass organ '
                                         'conduits.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_E2',
                                 'speaker': 'Furina',
                                 'text': 'Strange, is it not? Up there tonight, two thousand people are '
                                         'dressed in silk to celebrate Fontinalia -- and for the first '
                                         'time in five hundred years, my favorite seat in the house is '
                                         'down in the dark beside one person.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': 'vn_tender_love'},
                                {'beat_id': 'N28_E3',
                                 'speaker': 'Aether',
                                 'text': 'Wait until you sing tomorrow in the daylight with every note of '
                                         'your voice intact, Furina. That hall has not heard anything yet.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_E4',
                                 'speaker': 'Narrator',
                                 'text': 'Blue Indemnitium veins along the central tuning column pulse '
                                         'brighter as 10:45 PM approaches.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B05',
                                 'speaker': 'Narrator',
                                 'text': 'My pocket watch clicks to 10:40 PM -- fifteen minutes before the '
                                         'Spotlight Meks seal the inner water curtain for the '
                                         "eleven-o'clock tide.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C12_A',
                                 'priority_unlock': True,
                                 'prompt': 'Fifteen minutes remain before the 10:55 PM lock and 11:00 PM '
                                           'Solstice peak beneath the organ pipes:',
                                 'options': [{'opt_id': 'C12_A1_HARMONIC_WARD',
                                              'when': {'all_flags': ['F09_COSTAR_VOW',
                                                                     'F03_LUCINE_CONDUIT'],
                                                       'min_insight': 9},
                                              'unlock_badge': '[TWIN-WITNESS WARD UNLOCKED]',
                                              'lock_hint': '[LOCKED: Needs Co-Star Vow + Conduit Lore + '
                                                           'Insight 9]',
                                              'label': "Combine Neuvillette's conduit lore with your "
                                                       'Co-Star Vow: carve a Twin-Witness Phase-Inversion '
                                                       'Groove into the central pillar!',
                                              'effects': {'bond': 2,
                                                          'insight': 1,
                                                          'add_flags': ['TUNED_DUET_CHORD']},
                                              'next_node': 'N36_CH5_CONVERGE',
                                              'reaction_beats': [{'beat_id': 'N28_C12A1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': "Guided by Neuvillette's "
                                                                          'structural notes and our joined '
                                                                          'pulse, Furina traces a glowing '
                                                                          'Hydro treble clef along the '
                                                                          'central tuning pillar while my '
                                                                          'starlit blade carves a matching '
                                                                          'golden counter-groove!',
                                                                  'inner_thought': 'Harmonic Ward Tuned '
                                                                                   '[Twin-Witness Duet]: '
                                                                                   'The central pillar '
                                                                                   'locks into smooth '
                                                                                   'phase-inversion ahead '
                                                                                   'of the 11:00 PM surge!',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N28_C12A1_R2',
                                                                  'speaker': 'Furina',
                                                                  'text': 'Listen -- the harsh sub-bass '
                                                                          'rattle just smoothed into a '
                                                                          'clean fifth! Places, my co-star '
                                                                          "-- the eleven-o'clock curtain "
                                                                          'is rising!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                                                  'voice_emotion': 'vn_sweet_happy'}]},
                                             {'opt_id': 'C12_A2_GREENROOM_VIGIL',
                                              'label': 'Plant yourself right beside the mirror dais with '
                                                       'your dull blade drawn, ready to take the '
                                                       'unbuffered shockwave on your own arm.',
                                              'effects': {'bond': 0, 'insight': 1, 'add_flags': []},
                                              'next_node': 'N36_CH5_CONVERGE',
                                              'reaction_beats': [{'beat_id': 'N28_C12A2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Without exact conduit '
                                                                          'coordinates to re-groove the '
                                                                          'ancient pillar in time, I wrap '
                                                                          'my leather bracer tight around '
                                                                          'my left forearm and plant my '
                                                                          'boots half a pace in front of '
                                                                          'the central tuning column.',
                                                                  'inner_thought': 'It will tear up my '
                                                                                   'guard arm when eleven '
                                                                                   "o'clock hits, but not "
                                                                                   'a single shard of rime '
                                                                                   'will reach her throat!',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N28_C12A2_R2',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Breathe from your diaphragm and '
                                                                          'focus only on your melody, '
                                                                          'Furina -- I will hold the raw '
                                                                          'shockwave off you myself!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4a_organ_vigil_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N29_B4': {'node_id': 'N29_B4',
                      'chapter_id': 'CH4',
                      'title': 'Chalice of Love on the Opera Promenade',
                      'day_label': 'Day 9 - 07:30 PM (Gala Evening)',
                      'location': 'Opera Epiclese - Dusk Marble Promenade',
                      'beats': [{'beat_id': 'N29_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Lanterns of gold and sapphire blaze along the grand marble '
                                         'promenade of the Opera Epiclese on Night Nine as velvet-clad '
                                         'guests stream off the Navia Line aquabuses.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N29_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Stepping out onto the quiet side colonnade in full ceremonial '
                                         'dress, Furina presses an embossed gold-foil Seat Number One Gala '
                                         'Playbill into my hand and lifts two crystal goblets of sparkling '
                                         'Fonta-grape reserve.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N29_B03',
                                 'speaker': 'Furina',
                                 'text': "Ahem! 'Hear me -- let us raise the chalice of love!' To my "
                                         "irreplaceable Assistant Director, without whom tonight's "
                                         'Centennial Gala could never reach its final bar! Promise me you '
                                         "will watch from Seat Number One when eleven o'clock chimes!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': 'vn_sweet_happy'},
                                {'beat_id': 'N29_B03B',
                                 'speaker': 'Aether',
                                 'text': 'Why does that toast sound suspiciously like a farewell speech, '
                                         'Furina? After seeing your apartment dark last night, I have been '
                                         'looking for you all day.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N29_B03C',
                                 'speaker': 'Furina',
                                 'text': "Oh, pish! Every great premiere puts butterflies in a director's "
                                         "stomach! Simply sit back in Seat Number One and let Fontaine's "
                                         'shining star handle the acoustics!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N29_E1',
                                 'speaker': 'Narrator',
                                 'text': 'Across the illuminated plaza fountain behind us, string quartets '
                                         'tune their violins while festival lanterns mirror like fallen '
                                         'stars on wet marble.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N29_E2',
                                 'speaker': 'Furina',
                                 'text': 'Look how happy everyone looks arriving for a show without a '
                                         'single trial on the docket, Aether. Even if tonight were the '
                                         'very last curtain I ever directed... that sight alone would be '
                                         'enough.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N29_E3',
                                 'speaker': 'Aether',
                                 'text': 'Stop speaking in past tense before Act One has even started, '
                                         'Director.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N29_E4',
                                 'speaker': 'Furina',
                                 'text': 'Hehe -- slip of the tongue! Hold your goblet steady before the '
                                         'foyer bells ring!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N29_B04',
                                 'speaker': 'Narrator',
                                 'text': 'Even beneath her radiant stage bow, the rim of her crystal '
                                         'goblet clinks faintly against her teeth -- betrayed by the '
                                         'tremor in her white-gloved right wrist.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C14_B',
                                 'prompt': 'Furina raises her sparkling grape chalice on the dusk '
                                           'colonnade three hours before the 11:00 PM peak:',
                                 'options': [{'opt_id': 'C14_B1',
                                              'label': "Inspect Act Four's exact bar count printed inside "
                                                       'the gold-foiled Gala Playbill to pinpoint her '
                                                       'sub-stage lift cue.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N30_B5_GATE1',
                                              'reaction_beats': [{'beat_id': 'N29_C14B1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Touching my glass gently to '
                                                                          'hers, I glance down at the '
                                                                          'gold-foiled program timing: a '
                                                                          "five-minute 'Orchestral Pause' "
                                                                          'is printed at 10:55 PM -- the '
                                                                          'exact minute the sub-stage '
                                                                          "conductor's lift drops!",
                                                                  'inner_thought': '10:55 PM! Five minutes '
                                                                                   'before the Solstice '
                                                                                   'peak -- Clorinde and I '
                                                                                   'must be at the '
                                                                                   'sub-stage shaft before '
                                                                                   'that lift locks!',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N29_C14B1_R2',
                                                                  'speaker': 'Aether',
                                                                  'text': 'To an unforgettable premiere, '
                                                                          'Furina. Do not think for a '
                                                                          'second that Seat Number One '
                                                                          'will take its eyes off you '
                                                                          'tonight.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C14_B2',
                                              'label': 'Set both goblets on the balustrade, fold your warm '
                                                       'hands around her freezing gloved fingers, and hold '
                                                       'them to your chest.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N30_B5_GATE1',
                                              'reaction_beats': [{'beat_id': 'N29_C14B2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Setting both crystal goblets '
                                                                          'onto the marble rail, I wrap my '
                                                                          'palms around her ice-cold white '
                                                                          'gloves and press her knuckles '
                                                                          'gently against my steady '
                                                                          'heartbeat.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N29_C14B2_R2',
                                                                  'speaker': 'Furina',
                                                                  'text': '...Oh. Always breaking blocking '
                                                                          'cues at the last second, '
                                                                          'Aether... Remember how warm '
                                                                          'your hands feel right now when '
                                                                          'the final curtain falls, all '
                                                                          'right?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4b_promenade_chalice_base.jpg',
                                                                  'voice_emotion': 'vn_shy_blush'}]}]},
                      'routing': [],
                      'ending_id': None},
           'N30_B5_GATE1': {'node_id': 'N30_B5_GATE1',
                            'chapter_id': 'CH4',
                            'title': '10:55 PM Inner-Ring Lockdown',
                            'day_label': 'Day 9 - 10:55 PM (Combination Gate #1)',
                            'location': 'Opera Sub-Stage Lift Shaft & Lucine Bulkhead',
                            'beats': [{'beat_id': 'N30_B01',
                                       'speaker': 'Narrator',
                                       'text': "At 10:54 PM, just as Act Three's applause thunders "
                                               'overhead, Furina slips out of the orchestra pit onto the '
                                               'brass sub-stage lift -- dropping alone toward the sunken '
                                               'mirror cistern!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N30_B02',
                                       'speaker': 'Narrator',
                                       'text': 'Clorinde and I sprint down the service corridor a breath '
                                               'behind her, only for the clockwork chimes to strike 10:55 '
                                               'PM! Down in the deep, all three Spotlight Meks lock phase '
                                               'and raise an impenetrable Inner-Ring Indemnitium '
                                               'Hydro-Curtain!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N30_B03',
                                       'speaker': 'Clorinde',
                                       'text': 'Both the central lift shaft and the Lucine maintenance '
                                               'stairhead just sealed simultaneously under high-pressure '
                                               'Indemnitium water! Conventional Electro blades bounce '
                                               'straight off -- Aether, four minutes remain until 11:00 '
                                               'PM!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N30_E1',
                                       'speaker': 'Clorinde',
                                       'text': 'Look at the pressure dial on the maintenance column -- '
                                               'three Spotlight Meks below are cycling in three-four waltz '
                                               "time, locking out anything bound to Fontaine's hydro-grid!",
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N30_E2',
                                       'speaker': 'Aether',
                                       'text': 'Furina is already stepping up to the central tuning pillar '
                                               "down there -- if eleven o'clock hits while she is "
                                               'ungrounded, the rebound will crush her nerves!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N30_E3',
                                       'speaker': 'Clorinde',
                                       'text': 'Give the word, Aether -- three minutes and thirty seconds '
                                               'left on the clock!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N30_E4',
                                       'speaker': 'Narrator',
                                       'text': 'Roaring sapphire spray coats my knuckles as every clue we '
                                               'gathered across nine days snaps into sharp focus!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N30_B04',
                                       'speaker': 'Narrator',
                                       'text': 'Through the roaring sapphire water-wall below, I glimpse '
                                               'Furina stepping alone onto the central mirror dais, '
                                               'lifting her chin to meet five centuries of rising crystal '
                                               'tears by herself!',
                                       'inner_thought': "Four minutes to 11:00 PM! Only Furina's Star Pin "
                                                        'paired with a Descender or Sluice-Cadence breach '
                                                        'can pierce this lock!',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                       'voice_emotion': ''}],
                            'choice': {'choice_id': 'C15_B_GATE1',
                                       'exclusive_rescue_gate': True,
                                       'prompt': '10:56 PM! An Inner-Ring Indemnitium Hydro-Curtain seals '
                                                 "every stair above Furina's solitary stage:",
                                       'options': [{'opt_id': 'C15_B_COMBO_UNLOCK',
                                                    'when': {'all_flags': ['F07_SAPPHIRE_PIN'],
                                                             'any_of': [{'all_flags': ['F10_BLANK_TUNING_CRYSTAL'],
                                                                         'min_count_in': {'count': 1,
                                                                                          'pool': ['F03_LUCINE_CONDUIT',
                                                                                                   'F05_LUTIST_SCORE',
                                                                                                   'F08_CRYSTAL_TEAR_SEEN']},
                                                                         'min_insight': 11},
                                                                        {'all_flags': ['F12_SLUICE_CADENCE'],
                                                                         'min_count_in': {'count': 2,
                                                                                          'pool': ['F03_LUCINE_CONDUIT',
                                                                                                   'F05_LUTIST_SCORE',
                                                                                                   'F08_CRYSTAL_TEAR_SEEN',
                                                                                                   'F11_SUGAR_TIN_CLUE']},
                                                                         'min_insight': 10}]},
                                                    'unlock_badge': '[COMBINATION GATE #1 UNLOCKED]',
                                                    'lock_hint': '[LOCKED: Needs Star Pin F07 + (Blank '
                                                                 'Quartz F10 & Insight 11 & Clue OR Sluice '
                                                                 'Cadence F12 & Insight 10 & 2 Clues)]',
                                                    'label': "Synchronize Furina's Sapphire Star Pin with "
                                                             'your Erinnyes engineering breakthrough to '
                                                             'tear open the Inner-Ring Hydro-Curtain!',
                                                    'effects': {'bond': 2,
                                                                'insight': 1,
                                                                'add_flags': ['COMBO1_CLEARED']},
                                                    'next_node': 'N36_CH5_CONVERGE',
                                                    'reaction_beats': [{'beat_id': 'N30_C15_F10_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': "Drawing 'L'Etoile d'Eau' "
                                                                                'from my tunic, I press '
                                                                                "Furina's Vision-warmed "
                                                                                'sapphire pin directly '
                                                                                "against Freminet's "
                                                                                'unlinked Blank Tuning '
                                                                                'Quartz Crystal and drive '
                                                                                'my Fourth Descender palm '
                                                                                'straight into the central '
                                                                                'shaft veil!',
                                                                        'inner_thought': 'Combination Gate '
                                                                                         '#1 Cleared '
                                                                                         '[Descender '
                                                                                         'Quartz Rift]: '
                                                                                         'Unbound quartz + '
                                                                                         'Vision homing '
                                                                                         'tears a '
                                                                                         'golden-blue '
                                                                                         'doorway straight '
                                                                                         'through the '
                                                                                         'lock!',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                                                        'voice_emotion': '',
                                                                        'when': {'all_flags': ['F10_BLANK_TUNING_CRYSTAL']}},
                                                                       {'beat_id': 'N30_C15_F12_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Blowing two sharp blasts '
                                                                                'on our Marcotte signal '
                                                                                'whistle, Clorinde slams '
                                                                                'Sluice-Valve Seven into '
                                                                                'twelve-second reverse '
                                                                                'backflow while I thrust '
                                                                                "'L'Etoile d'Eau' straight "
                                                                                'into the pressure seam -- '
                                                                                'splitting the blind-spot '
                                                                                'veil wide open!',
                                                                        'inner_thought': 'Combination Gate '
                                                                                         '#1 Cleared '
                                                                                         '[Marcotte '
                                                                                         'Backflow '
                                                                                         'Breach]: Sluice '
                                                                                         'cadence + Vision '
                                                                                         'homing parts the '
                                                                                         'inner water '
                                                                                         'curtain at 10:59 '
                                                                                         'PM!',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                                                        'voice_emotion': '',
                                                                        'when': {'forbid_flags': ['F10_BLANK_TUNING_CRYSTAL']}},
                                                                       {'beat_id': 'N30_C15_R2',
                                                                        'speaker': 'Aether',
                                                                        'text': 'Did you really think your '
                                                                                'Assistant Director missed '
                                                                                'the five-minute pause on '
                                                                                'the playbill, Furina?! '
                                                                                'Curtain up -- together!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                                                        'voice_emotion': ''}]},
                                                   {'opt_id': 'C15_B_FAIL_RUSH',
                                                    'label': 'Hurl every ounce of strength behind your '
                                                             'dull blade against the sealed bronze '
                                                             "bulkhead before eleven o'clock tolls!",
                                                    'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                    'next_node': 'N31_BAD2_1',
                                                    'reaction_beats': [{'beat_id': 'N30_C15_FAIL_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Blade after desperate '
                                                                                'strike crashes into the '
                                                                                'roaring Indemnitium '
                                                                                'water-lock, numbing my '
                                                                                'wrists to the bone while '
                                                                                'the wall rebounds '
                                                                                'unbroken without a tuning '
                                                                                'key or homing anchor '
                                                                                'inside!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N30_C15_FAIL_R2',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Above us, the great tower '
                                                                                'bells of Erinnyes strike '
                                                                                'the first boom of 11:00 '
                                                                                'PM -- and the shaft below '
                                                                                'erupts in blinding, '
                                                                                'soundless white foam!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                                                        'voice_emotion': ''}]}]},
                            'routing': [],
                            'ending_id': None},
           'N31_BAD2_1': {'node_id': 'N31_BAD2_1',
                          'chapter_id': 'CH4',
                          'title': "Le Voile d'Oubli",
                          'day_label': 'Day 9 - 11:00 PM',
                          'location': 'Sunken Cistern - Beneath the Parting Foam',
                          'beats': [{'beat_id': 'N31_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Down on the solitary mirror stage, five hundred years of '
                                             "compressed crystal sorrow crash inward upon Furina's "
                                             'unshielded mortal nerves -- threatening to shatter both her '
                                             'voice and her mind in a single heartbeat.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B02',
                                     'speaker': 'Narrator',
                                     'text': "In that terminal instant, one last dormant drop of Focalors' "
                                             'ancient protective grace awakens beneath the basin -- '
                                             "unfurling 'Le Voile d'Oubli', the Gentle Veil of Oblivion.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B02B',
                                     'speaker': 'Narrator',
                                     'text': 'Through the roaring sapphire veil, a faint, merciful whisper '
                                             "seems to cradle Furina's brow: 'Live on in the sunlight, my "
                                             'brave human self -- even if the heart must forget why it '
                                             "wept.'",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B03',
                                     'speaker': 'Narrator',
                                     'text': 'To sever the psychic feedback loop before it destroys her, '
                                             "the veil washes away the entire intimate thread tied to 'the "
                                             "Witness in the Teardrop' -- dissolving every private memory "
                                             "between us from Scene 182,376's troupe stage through tonight "
                                             'into the Fountain of Lucine.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B03B',
                                     'speaker': 'Clorinde',
                                     'text': 'Aether -- the pressure gauge on the bulkhead just dropped to '
                                             'zero! Stand back, the water-lock is falling!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_E1',
                                     'speaker': 'Narrator',
                                     'text': 'Down on the quiet marble dais, three tiny Hydro companions '
                                             "hover around Furina's sleeping shoulders -- gently drying "
                                             'the last salt-crystals from her lashes before vanishing into '
                                             'mist.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_E2',
                                     'speaker': 'Aether',
                                     'text': 'Furina -- can you hear me?! Your pulse is warm again!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_E3',
                                     'speaker': 'Furina',
                                     'text': '...Mm? Sir Clorinde... and the Honorable Traveler? Goodness, '
                                             'did I lose my footing on the backstage stairs before Act '
                                             'Four?',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_E4',
                                     'speaker': 'Narrator',
                                     'text': 'My heart stops cold in my chest. In her clear, healthy eyes '
                                             'shines polite gratitude -- without a flicker of Quartier '
                                             'Lyonnais, midnight macaroni, or Seat Number One.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B04',
                                     'speaker': 'Narrator',
                                     'text': 'When the water-curtain collapses at 11:03 PM and Clorinde '
                                             'and I reach the dry central dais, Furina lies breathing '
                                             'peacefully on the marble -- her voice unharmed, the '
                                             'five-hundred-year pressure vented, and every private kitchen '
                                             'midnight we shared gone like sea foam.',
                                     'inner_thought': 'She survived... yet only her distant public '
                                                      "memories of Fontaine's blonde Traveler from the "
                                                      'prophecy trial remain.',
                                     'cg': 'ui_assets/story_quest_cgs/furina/ch4b_gate1_lockdown_base.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [{'default': True, 'next_node': 'N32_BAD2_2'}],
                          'ending_id': None},
           'N32_BAD2_2': {'node_id': 'N32_BAD2_2',
                          'chapter_id': 'CH4',
                          'title': 'Sun-Shower Stranger at Lucine',
                          'day_label': 'Day 12 - 03:30 PM (Erinnyes Island)',
                          'location': 'Fountain of Lucine - Sunlit Mist',
                          'beats': [{'beat_id': 'N32_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Three afternoons later, a fine sun-shower drifts across '
                                             'Erinnyes Island after the rescheduled Fontinalia matinee. '
                                             'Beside the tranquil Fountain of Lucine stands Furina -- '
                                             'healthy, clear-voiced, and wholly free of rime.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B02',
                                     'speaker': 'Furina',
                                     'text': 'Oh -- good afternoon, Honorable Traveler! Visiting the '
                                             'Fountain of Lucine before setting off on your next grand '
                                             "expedition? On behalf of Fontaine's arts community, allow me "
                                             'to thank you for attending the Gala!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                     'voice_emotion': 'greet_doorstep'},
                                    {'beat_id': 'N32_B03',
                                     'speaker': 'Narrator',
                                     'text': 'Her curtsy is immaculate, polite, and heartbreakingly formal '
                                             '-- the courteous smile one offers a famous dignitary met '
                                             'only across courtroom rails.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B04_RETURN_F07',
                                     'speaker': 'Narrator',
                                     'text': 'Looking at the two tiny empty pinholes on her navy hatband, '
                                             "I quietly draw 'L'Etoile d'Eau' from my pocket and hold it "
                                             "out with the gentlest lie I know: 'I found this pin near the "
                                             "Opera foyer on Gala night, Lady Furina.'",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                     'voice_emotion': '',
                                     'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                    {'beat_id': 'N32_B05_RETURN_F07',
                                     'speaker': 'Furina',
                                     'text': 'My sapphire star pin! Heavens, I have been turning my '
                                             'dressing room upside down wondering why my hat felt so '
                                             'light! How wonderfully lucky that you found it --',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_hand_chest_diff.jpg',
                                     'voice_emotion': '',
                                     'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                    {'beat_id': 'N32_E1',
                                     'speaker': 'Furina',
                                     'text': 'Miss Navia insisted on sending three boxes of strawberry '
                                             'macarons to my apartment this morning -- and imagine, they '
                                             'tasted sweeter than any pastry I remember all year!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_E2',
                                     'speaker': 'Aether',
                                     'text': 'I am glad the sweetness came back, Lady Furina. Truly glad.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_E3',
                                     'speaker': 'Furina',
                                     'text': "Eh? 'Came back'? What a poetic turn of phrase you outlanders "
                                             'use!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_E4',
                                     'speaker': 'Narrator',
                                     'text': 'Sunbeams break through light Erinnyes rain behind her '
                                             'shoulder, painting a faint rainbow across the Fountain of '
                                             'Lucine.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B06_RETURN_F07',
                                     'speaker': 'Narrator',
                                     'text': 'As she pins the star back onto her hatband, a single warm, '
                                             'unscripted tear spills abruptly down her cheek -- making her '
                                             'touch her fingertips to her eyelashes in bewildered '
                                             'surprise.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_hand_chest_diff.jpg',
                                     'voice_emotion': '',
                                     'when': {'all_flags': ['F07_SAPPHIRE_PIN']}}],
                          'choice': {'choice_id': 'C20_BAD2',
                                     'prompt': 'Sun-shower mist sparkles between you and the girl whose '
                                               'life was bought with every shared private memory:',
                                     'options': [{'opt_id': 'C20_A_RETURN_PLAYBILL',
                                                  'label': 'Hold out your gold-foiled Seat Number One '
                                                           'Playbill as an ordinary admirer, guarding her '
                                                           'hard-won peace in silence.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD2_PLAYBILL']},
                                                  'next_node': 'END_BAD_2',
                                                  'reaction_beats': [{'beat_id': 'N32_C20A_R1',
                                                                      'speaker': 'Aether',
                                                                      'text': 'Your Act Four Cadenza was '
                                                                              'unforgettable, Miss Furina. '
                                                                              'May an ordinary member of '
                                                                              'the audience ask the '
                                                                              'director to sign his Seat '
                                                                              'Number One program?',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N32_C20A_R2',
                                                                      'speaker': 'Furina',
                                                                      'text': 'Why, gladly! Though... how '
                                                                              "strange. Looking at 'Seat "
                                                                              "Number One' in gold leaf "
                                                                              'makes my chest ache as if I '
                                                                              'promised someone terribly '
                                                                              'dear to wait right there...',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_hand_chest_diff.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N32_C20A_R3',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'She hands back the signed '
                                                                              'playbill with a puzzled, '
                                                                              'wistful smile while the '
                                                                              'Fountain of Lucine murmurs '
                                                                              'softly behind us -- keeping '
                                                                              'our twelve days safe inside '
                                                                              'its waters forever.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_hand_chest_diff.jpg',
                                                                      'voice_emotion': ''}]},
                                                 {'opt_id': 'C20_B_RECALL_KITCHEN',
                                                  'label': 'Speak one quiet phrase from Quartier '
                                                           "Lyonnais's midnight kitchen before bidding her "
                                                           'farewell.',
                                                  'effects': {'bond': 0,
                                                              'insight': 0,
                                                              'add_flags': ['BAD2_KITCHEN_ECHO']},
                                                  'next_node': 'END_BAD_2',
                                                  'reaction_beats': [{'beat_id': 'N32_C20B_R1_F02',
                                                                      'speaker': 'Aether',
                                                                      'text': "'Savory first, sweet to "
                                                                              'close -- nobody leaves the '
                                                                              'table without sweetness on '
                                                                              "their tongue.' Remember to "
                                                                              'eat a strawberry macaron '
                                                                              'after dinner tonight, Miss '
                                                                              'Furina.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                                                      'voice_emotion': '',
                                                                      'when': {'all_flags': ['F02_MACARONI_RULE']}},
                                                                     {'beat_id': 'N32_C20B_R1_NO_F02',
                                                                      'speaker': 'Aether',
                                                                      'text': 'Even when late-night '
                                                                              'blocking notes run past '
                                                                              'midnight in Quartier '
                                                                              'Lyonnais, Miss Furina -- '
                                                                              'one spoonful of brown sugar '
                                                                              'is plenty now that the '
                                                                              'sweetness has come back.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_stranger_base.jpg',
                                                                      'voice_emotion': '',
                                                                      'when': {'forbid_flags': ['F02_MACARONI_RULE']}},
                                                                     {'beat_id': 'N32_C20B_R2',
                                                                      'speaker': 'Furina',
                                                                      'text': '...Wait, Traveler! Why does '
                                                                              'hearing you say that make '
                                                                              'my heart feel so warm it '
                                                                              'wants to cry -- as if I '
                                                                              'once sang an entire opera '
                                                                              'for an audience of one?!',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_hand_chest_diff.jpg',
                                                                      'voice_emotion': ''},
                                                                     {'beat_id': 'N32_C20B_R3',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'Pressing her bare hand '
                                                                              'softly over her ribboned '
                                                                              'chest, Furina watches me '
                                                                              'walk down the sunlit '
                                                                              'Erinnyes lane -- a single '
                                                                              'warm teardrop glistening on '
                                                                              'her cheek under a sky that '
                                                                              'finally remembers how to '
                                                                              'clear.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/furina/end_bad2_lucine_hand_chest_diff.jpg',
                                                                      'voice_emotion': ''}]}]},
                          'routing': [],
                          'ending_id': None},
           'N33_C3': {'node_id': 'N33_C3',
                      'chapter_id': 'CH4',
                      'title': 'Two-Thirty on the Villa Terrace',
                      'day_label': 'Day 9 - 02:30 AM',
                      'location': 'Serenitea Pot - Starlit Kitchen Terrace',
                      'beats': [{'beat_id': 'N33_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Inside the Realm Within, the night air never cools past a mild '
                                         'spring, yet my pocket watch on the nightstand ticks past '
                                         'two-thirty in the morning. Drawn out by the faint clink of a '
                                         'silver spoon, I find warm vanilla steam drifting across the '
                                         'quiet stone terrace.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N33_B02',
                                 'speaker': 'Furina',
                                 'text': 'Ahem! Caught in the middle of an unscheduled intermission, I '
                                         'see! Wipe that tragic third-act crease from your brow, my dear '
                                         'assistant -- a director of my stature requires midnight cocoa '
                                         'while drafting blocking notes, and I graciously brewed enough '
                                         'for two!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_startled_diff.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N33_E1',
                                 'speaker': 'Narrator',
                                 'text': 'By the dim terrace lamp, a half-open drawer reveals neatly '
                                         'addressed envelopes bearing blue wax seals for Monsieur '
                                         'Neuvillette, Demoiselle Navia, Champion Duelist Clorinde -- and '
                                         "one thicker envelope marked simply 'Aether'.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_startled_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N33_E2',
                                 'speaker': 'Aether',
                                 'text': 'Midnight blocking notes do not usually require sealing wax at '
                                         'two-thirty in the morning, Furina.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_startled_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N33_E3',
                                 'speaker': 'Furina',
                                 'text': 'Ceremonial Opening Night thank-you cards, naturally! A '
                                         'cultivated director seals her stationery properly before the '
                                         'rush!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_startled_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N33_E4',
                                 'speaker': 'Narrator',
                                 'text': 'Attempting to prove how steady she is, she reaches across the '
                                         'marble counter for the cocoa pot -- right before her numb wrist '
                                         'betrays her.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_startled_diff.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N33_B03',
                                 'speaker': 'Narrator',
                                 'text': 'Five empty Demerara wrappers already litter the marble beside '
                                         'her own mug, yet she sips it, frowns faintly, and stirs in one '
                                         'more heaping spoonful without blinking. When she lifts the '
                                         'second steaming cup toward me, her right wrist locks; scalding '
                                         'cocoa sloshes across her pale knuckles, raising an angry red '
                                         'flush -- and her eyelashes do not even twitch.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_spill_diff.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C17_C',
                                 'prompt': 'Scalding cocoa clings to her numb right knuckles, and those '
                                           'wax-sealed navy envelopes are still jutting from her pocket.',
                                 'options': [{'opt_id': 'C17_C1',
                                              'label': 'Take the hot cup from her numb hand at once and '
                                                       'ask directly about the sealed envelopes and the '
                                                       'sugar wrappers.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N34_C4_GATE2',
                                              'reaction_beats': [{'beat_id': 'N33_C17C1_R1',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Let go of the handle, Furina -- '
                                                                          'your skin is burning! And do '
                                                                          'not tell me those wax-sealed '
                                                                          'navy envelopes jutting out of '
                                                                          'your pocket for Navia, '
                                                                          "Clorinde, and me are 'blocking "
                                                                          "notes'!",
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N33_C17C1_R2',
                                                                  'speaker': 'Furina',
                                                                  'text': 'Th-those are merely thank-you '
                                                                          'letters in case my throat needs '
                                                                          'a quiet holiday after tonight! '
                                                                          'Stop looking at my pocket like '
                                                                          'that --',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N33_C17C1_B04_F02',
                                                                  'speaker': 'Aether',
                                                                  'text': 'On my third night in Quartier '
                                                                          'Lyonnais, you stood in your '
                                                                          'kitchen and declared a house '
                                                                          "rule. 'Savory first, sweet to "
                                                                          'close -- nobody leaves Furina '
                                                                          "de Fontaine's table without "
                                                                          "sweetness on their tongue.' "
                                                                          '...How long has it been since '
                                                                          'you tasted anything sweet at '
                                                                          'all, Furina?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                  'voice_emotion': '',
                                                                  'when': {'all_flags': ['F02_MACARONI_RULE']}},
                                                                 {'beat_id': 'N33_C17C1_B04_NO_F02',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Five empty sugar wrappers '
                                                                          'beside your mug tonight, just '
                                                                          'like the five empty packets in '
                                                                          'your kitchen in Quartier '
                                                                          'Lyonnais -- and your right hand '
                                                                          'did not even feel that burn. '
                                                                          'How long have you been hiding '
                                                                          'the numbness from me, Furina?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                  'voice_emotion': '',
                                                                  'when': {'forbid_flags': ['F02_MACARONI_RULE']}},
                                                                 {'beat_id': 'N33_C17C1_B05',
                                                                  'speaker': 'Furina',
                                                                  'text': '...Unfair. Truly unfair of my '
                                                                          'Seat Number One witness to '
                                                                          'catch every missed cue I try to '
                                                                          'hide. If the leading lady '
                                                                          'admits the sugar tastes like '
                                                                          'plain rainwater tonight... will '
                                                                          'you still stay until the '
                                                                          'curtain comes down?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C17_C2',
                                              'label': 'Set the cup aside and wrap both warm palms around '
                                                       'her freezing right wrist before saying a single '
                                                       'word.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N34_C4_GATE2',
                                              'reaction_beats': [{'beat_id': 'N33_C17C2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Without uttering a word of '
                                                                          'reproach, I lift the steaming '
                                                                          'mug safely onto the marble '
                                                                          'counter, soak a cool linen '
                                                                          'napkin against the red flush on '
                                                                          'her knuckles, and fold both '
                                                                          'warm palms gently around her '
                                                                          'ice-cold right wrist.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N33_C17C2_R2',
                                                                  'speaker': 'Furina',
                                                                  'text': '...Ah. Do not hold my wrist so '
                                                                          'warmly without scolding me '
                                                                          'first, Aether... How is a '
                                                                          'director supposed to stay in '
                                                                          'character when your hands shake '
                                                                          'like that?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N33_C17C2_B04_F02',
                                                                  'speaker': 'Aether',
                                                                  'text': 'On my third night in Quartier '
                                                                          'Lyonnais, you stood in your '
                                                                          'kitchen and declared a house '
                                                                          "rule. 'Savory first, sweet to "
                                                                          'close -- nobody leaves Furina '
                                                                          "de Fontaine's table without "
                                                                          "sweetness on their tongue.' "
                                                                          '...How long has it been since '
                                                                          'you tasted anything sweet at '
                                                                          'all, Furina?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                  'voice_emotion': '',
                                                                  'when': {'all_flags': ['F02_MACARONI_RULE']}},
                                                                 {'beat_id': 'N33_C17C2_B04_NO_F02',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Five empty sugar wrappers '
                                                                          'beside your mug tonight, just '
                                                                          'like the five empty packets in '
                                                                          'your kitchen in Quartier '
                                                                          'Lyonnais -- and your right hand '
                                                                          'did not even feel that burn. '
                                                                          'How long have you been hiding '
                                                                          'the numbness from me, Furina?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                  'voice_emotion': '',
                                                                  'when': {'forbid_flags': ['F02_MACARONI_RULE']}},
                                                                 {'beat_id': 'N33_C17C2_B05',
                                                                  'speaker': 'Furina',
                                                                  'text': '...Unfair. Truly unfair of my '
                                                                          'Seat Number One witness to '
                                                                          'catch every missed cue I try to '
                                                                          'hide. If the leading lady '
                                                                          'admits the sugar tastes like '
                                                                          'plain rainwater tonight... will '
                                                                          'you still stay until the '
                                                                          'curtain comes down?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N34_C4_GATE2': {'node_id': 'N34_C4_GATE2',
                            'chapter_id': 'CH4',
                            'title': '8:00 PM Day 9: Three Hours Before Curtain Up',
                            'day_label': 'Day 9 - 08:00 PM (Combination Gate #2)',
                            'location': 'Serenitea Pot - Courtyard Exit Waypoint',
                            'beats': [{'beat_id': 'N34_B01',
                                       'speaker': 'Narrator',
                                       'text': 'Dusk settles across Day Nine. At 8:00 PM -- three hours '
                                               "before the eleven-o'clock Winter Solstice Hydro-Tide peaks "
                                               'outside on Erinnyes Island -- soft footsteps cross the '
                                               "villa courtyard toward Tubby's exit chime.",
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N34_B02',
                                       'speaker': 'Narrator',
                                       'text': 'Dressed in full stage navy, Furina reaches out a trembling '
                                               'hand toward the realm boundary, intending to slip out onto '
                                               'Erinnyes Bluff and descend into the mirror cistern alone '
                                               'while I sleep.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N34_B03',
                                       'speaker': 'Aether',
                                       'text': "Three hours before eleven o'clock, Furina. Did you really "
                                               'think Seat Number One would let you walk out that gate '
                                               'alone?',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N34_B03B',
                                       'speaker': 'Narrator',
                                       'text': 'Startled under the realm starlight, Furina freezes with '
                                               'her fingertips an inch from the brass chime. Slowly, she '
                                               'turns around, clutching her navy capelet tight across her '
                                               'chest.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N34_B04',
                                       'speaker': 'Furina',
                                       'text': 'Let me pass, Aether, I beg you! Even with the Grand Organ '
                                               'dark tonight, the Solstice tide will burst the Lucine '
                                               "basin at eleven unless I sing Act Four's Cadenza down "
                                               'there -- and any Fontainian who follows me in will have '
                                               'five hundred years of sorrow poured into their Ley-Line '
                                               'memory!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N34_E1',
                                       'speaker': 'Aether',
                                       'text': 'Look at your right hand shaking on the hem of your '
                                               'capelet, Furina. If you step into that cistern alone at '
                                               "eleven o'clock, what happens to your voice -- and your "
                                               'memories?',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N34_E2',
                                       'speaker': 'Furina',
                                       'text': "Better a silent actress who saved her city's festival than "
                                               'dragging my dearest friend into five hundred years of '
                                               'drowning salt!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N34_E3',
                                       'speaker': 'Narrator',
                                       'text': 'Realm starlight glints off the unshed tears clinging to '
                                               "her lower lashes as Tubby's brass gate-chime hums softly "
                                               'between us.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N34_E4',
                                       'speaker': 'Aether',
                                       'text': 'Listen to me carefully before you take another step toward '
                                               'that chime, Furina.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N34_B05',
                                       'speaker': 'Furina',
                                       'text': 'I finally learned how it feels to cook dinner for someone, '
                                               'to laugh over silly contracts, to look forward to '
                                               'tomorrow! How could I bear dragging you into five '
                                               'centuries of my tears?!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                       'voice_emotion': ''}],
                            'choice': {'choice_id': 'C18_C_GATE2',
                                       'priority_unlock': True,
                                       'prompt': '8:00 PM at the Realm Gate -- three hours before the '
                                                 '11:00 PM Solstice peak on Erinnyes Island:',
                                       'options': [{'opt_id': 'C18_C_COMBO_UNLOCK',
                                                    'when': {'all_flags': ['F07_SAPPHIRE_PIN'],
                                                             'any_flags': ['F08_CRYSTAL_TEAR_SEEN',
                                                                           'F11_SUGAR_TIN_CLUE'],
                                                             'min_count_in': {'count': 2,
                                                                              'pool': ['F01_TEAR_RIME_CHILL',
                                                                                       'F02_MACARONI_RULE',
                                                                                       'F04_ROOFTOP_ENCORE',
                                                                                       'F05_LUTIST_SCORE',
                                                                                       'F06_HARMONICA_MERCY']},
                                                             'min_insight': 8},
                                                    'unlock_badge': '[COMBINATION GATE #2 UNLOCKED]',
                                                    'lock_hint': '[LOCKED: Needs Star Pin F07 + Rime/Sugar '
                                                                 'Proof (F08 OR F11) + Insight 8 + 2 '
                                                                 'Memory Anchors]',
                                                    'label': "Hold up 'L'Etoile d'Eau' and every clue she "
                                                             'hid: draw out the Twin-Witness Law and walk '
                                                             'into the cistern together at 10:45 PM!',
                                                    'effects': {'bond': 2,
                                                                'insight': 1,
                                                                'add_flags': ['COMBO2_CLEARED']},
                                                    'next_node': 'N36_CH5_CONVERGE',
                                                    'reaction_beats': [{'beat_id': 'N34_C18_UNLOCK_R1',
                                                                        'speaker': 'Aether',
                                                                        'text': "Look at 'L'Etoile d'Eau' "
                                                                                'shining in my palm, '
                                                                                'Furina! You hid the '
                                                                                'crystal tear-frost, the '
                                                                                'numb wrist, the lost '
                                                                                'sweetness, and Maitre '
                                                                                "Renaud's fate -- yet you "
                                                                                'forgot one truth from '
                                                                                'Night One!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N34_C18_UNLOCK_R2',
                                                                        'speaker': 'Furina',
                                                                        'text': '...Night One? Wait -- '
                                                                                "Maitre Renaud's score "
                                                                                'said the Cadenza only '
                                                                                'burns a solo singer '
                                                                                "because Teyvat's Ley "
                                                                                'Lines reflect the sorrow '
                                                                                'back... Unless a witness '
                                                                                'unbound to Irminsul '
                                                                                'grounds the bass chord! '
                                                                                'Aether -- you absorbed '
                                                                                'that geyser on Night One!',
                                                                        'inner_thought': 'Combination Gate '
                                                                                         '#2 Cleared '
                                                                                         '[Twin-Witness '
                                                                                         'Revelation]: '
                                                                                         "Furina's "
                                                                                         'Twin-Witness Law '
                                                                                         'meets the Fourth '
                                                                                         "Descender's "
                                                                                         'unlinked soul!',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N34_C18_UNLOCK_R3',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Tears of fierce relief '
                                                                                'break past her lashes as '
                                                                                'she catches both my '
                                                                                'hands. Exiting onto '
                                                                                'Erinnyes Bluff at 10:30 '
                                                                                'PM, we descend the quiet '
                                                                                'Lucine stair hand-in-hand '
                                                                                'and cross the inner '
                                                                                'mirror threshold at 10:45 '
                                                                                'PM -- ten full minutes '
                                                                                'before the 10:55 PM water '
                                                                                'curtain locks!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_base.jpg',
                                                                        'voice_emotion': ''}]},
                                                   {'opt_id': 'C18_C_GOOD_INTERMISSION',
                                                    'label': "Seal the Serenitea Pot's exit chime to save "
                                                             'her voice tonight and send an urgent flare '
                                                             'to Monsieur Neuvillette outside.',
                                                    'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                    'next_node': 'N35_GOOD_1',
                                                    'reaction_beats': [{'beat_id': 'N34_C18_GOOD_R1',
                                                                        'speaker': 'Aether',
                                                                        'text': 'Without knowing how to '
                                                                                'ground that rebound '
                                                                                'safely, I refuse to '
                                                                                'gamble your voice and '
                                                                                'life tonight! Tubby -- '
                                                                                'lock the realm gate while '
                                                                                'I send an emergency Realm '
                                                                                'Dispatch flare to '
                                                                                'Monsieur Neuvillette!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N34_C18_GOOD_R2',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'At 8:15 PM outside on '
                                                                                'Erinnyes Island, '
                                                                                'Neuvillette receives my '
                                                                                'flare, evacuates the '
                                                                                'Opera promenade, and '
                                                                                'drives a Ninety-Day '
                                                                                'Hydro-Stasis Seal deep '
                                                                                'through the Opera '
                                                                                "Epiclese's foundation -- "
                                                                                'buying us winter peace '
                                                                                'until the Spring Equinox.',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/furina/ch4c_terrace_close_avert_diff.jpg',
                                                                        'voice_emotion': ''}]}]},
                            'routing': [],
                            'ending_id': None},
           'N35_GOOD_1': {'node_id': 'N35_GOOD_1',
                          'chapter_id': 'CH4',
                          'title': 'Intermission Under Winter Glass',
                          'day_label': 'Day 10 - Snowy Noon (Borrowed Winter)',
                          'location': 'Quartier Lyonnais - Warm Living Room Sofa',
                          'beats': [{'beat_id': 'N35_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Outside the frosted parlor window in Quartier Lyonnais, soft '
                                             'December snow dusts the rooftops while across the water the '
                                             "Opera Epiclese sleeps safely beneath Neuvillette's "
                                             'ninety-day winter ice seal.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N35_B02',
                                     'speaker': 'Narrator',
                                     'text': 'Indoors beside the crackling hearth, hatless Furina sits '
                                             'curled under a thick plaid wool blanket next to me on the '
                                             'sofa, blowing steam off a shared porcelain bowl of fresh '
                                             'tomato-sauce macaroni.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N35_B02B',
                                     'speaker': 'Paimon',
                                     'text': 'Mmm, extra Marcotte cheese on top! See, Furina? Even with '
                                             'the Opera House taking a winter nap, Quartier Lyonnais still '
                                             'has the best dinner table in Fontaine!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N35_B03',
                                     'speaker': 'Furina',
                                     'text': 'Hmph... Ninety days of postponed rehearsals, and Charlotte '
                                             "already printed 'Director Takes Cozy Winter Sabbatical' on "
                                             'page three! Still... thank you for locking that gate last '
                                             'night, my stubborn assistant.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': 'vn_tender_love'},
                                    {'beat_id': 'N35_B03B',
                                     'speaker': 'Narrator',
                                     'text': 'Under the shared wool blanket, she nudges her still-cool '
                                             'right hand quietly against my warm palm beside the sofa '
                                             'cushion -- letting me warm her fingers while snow drifts '
                                             'past the glass.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N35_B04_F07',
                                     'speaker': 'Aether',
                                     'text': "Resting my fingertips over 'L'Etoile d'Eau' tucked safely "
                                             "inside my tunic pocket, I smile back at her: 'We have ninety "
                                             'warm winter mornings to research every note of that cistern '
                                             'together -- and when the Spring Equinox thaws the stage, I '
                                             "will pin your lucky star back onto your hat myself.'",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': '',
                                     'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                    {'beat_id': 'N35_B04_NO_F07',
                                     'speaker': 'Aether',
                                     'text': 'Glancing toward her star-pinned top hat resting dry and safe '
                                             'on the hall stand beside the hearth, I smile back at her: '
                                             "'We have ninety warm winter mornings to research every note "
                                             'of that cistern together -- so when the Spring Equinox thaws '
                                             "the stage, you will sing without losing a thing.'",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': '',
                                     'when': {'forbid_flags': ['F07_SAPPHIRE_PIN']}},
                                    {'beat_id': 'N35_E1',
                                     'speaker': 'Furina',
                                     'text': 'Monsieur Neuvillette stopped by with spring water from '
                                             'Sumeru this morning, you know. Even he admitted ninety days '
                                             'of winter quiet will give us plenty of time to carve a '
                                             'proper harmonic relief channel before April.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N35_E2',
                                     'speaker': 'Paimon',
                                     'text': 'Plus Paimon gets ninety bonus days of Quartier Lyonnais '
                                             'macaroni taste-testing before we ever pack for Natlan!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N35_E3',
                                     'speaker': 'Aether',
                                     'text': 'No more midnight farewell letters hidden in cardigan pockets '
                                             'while we research the thaw, agreed?',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N35_E4',
                                     'speaker': 'Furina',
                                     'text': 'A-Agreed! Burned every last envelope in the hearth before '
                                             'breakfast, I swear it!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': 'vn_shy_blush'},
                                    {'beat_id': 'N35_B05',
                                     'speaker': 'Furina',
                                     'text': '...Deal. Until the spring curtain rises, Seat Number One is '
                                             'officially requisitioned for daily kitchen duty right here '
                                             'beside me!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/furina/end_good_winter_sofa.jpg',
                                     'voice_emotion': 'vn_sweet_happy'}],
                          'choice': None,
                          'routing': [],
                          'ending_id': 'END_GOOD'},
           'N36_CH5_CONVERGE': {'node_id': 'N36_CH5_CONVERGE',
                                'chapter_id': 'CH5',
                                'title': 'Curtain Up on the Mirror-Stage',
                                'day_label': 'Day 9 - 10:59 PM to 11:00 PM',
                                'location': 'Sunken Erinnyes Cistern - Central Mirror Dais',
                                'beats': [{'beat_id': 'N36_B01_RA_TUNED',
                                           'speaker': 'Narrator',
                                           'text': 'At 10:59 PM on the sunken mirror dais, our newly '
                                                   'carved Twin-Witness Phase-Inversion Groove blazes gold '
                                                   'and sapphire along the central pillar just as the '
                                                   "eleven-o'clock Winter Solstice Hydro-Tide roars "
                                                   'upward!',
                                           'inner_thought': 'Our pre-tuned harmonic ward splits the '
                                                            'initial pressure spike cleanly into two '
                                                            'balanced streams!',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_A', 'TUNED_DUET_CHORD']}},
                                          {'beat_id': 'N36_B01_RA_RAW',
                                           'speaker': 'Narrator',
                                           'text': "When the eleven-o'clock Solstice shockwave detonates "
                                                   'upward without a carved relief groove, the raw blast '
                                                   'wrenches my dull blade sideways -- a razor shard of '
                                                   'rime-ice slicing a bright crimson line across my left '
                                                   'forearm before I plant my boots and hold the line '
                                                   'beside Furina!',
                                           'inner_thought': 'Only flesh and leather scratched -- my stance '
                                                            'holds firm, shielding her throat from the '
                                                            'opening surge!',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_A'],
                                                    'forbid_flags': ['TUNED_DUET_CHORD']}},
                                          {'beat_id': 'N36_B01_RB',
                                           'speaker': 'Narrator',
                                           'text': 'Vaulting straight through our breached Inner-Ring '
                                                   'Hydro-Curtain at 10:59 PM, I land squarely on the '
                                                   "central mirror dais and catch Furina's waist with one "
                                                   "arm at the exact second the eleven-o'clock Solstice "
                                                   'bell booms!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_B']}},
                                          {'beat_id': 'N36_B01_RC',
                                           'speaker': 'Narrator',
                                           'text': 'Having crossed the inner threshold hand-in-hand at '
                                                   '10:45 PM -- ten calm minutes before the 10:55 PM water '
                                                   'curtain sealed behind our backs -- Furina and I stand '
                                                   "ready at center stage as the eleven-o'clock Solstice "
                                                   'tide awakens!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_C']}},
                                          {'beat_id': 'N36_B02',
                                           'speaker': 'Furina',
                                           'text': 'You are really here on the stage with me... Good! '
                                                   'Ground the lowest bass note through your palm, Aether '
                                                   '-- Scene 182,377 begins right now!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_B02B',
                                           'speaker': 'Aether',
                                           'text': 'Every measure from start to finish -- sing with '
                                                   'everything in your heart, Furina! Not one drop of that '
                                                   'rebound gets past me!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_B02C',
                                           'speaker': 'Narrator',
                                           'text': 'Around the perimeter of the mirror dais, Mademoiselle '
                                                   'Crabaletta, Surintendante Chevalmarin, and Gentilhomme '
                                                   'Usher take gallant formation -- shimmering blue light '
                                                   'steadying the outer ripples.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_E1',
                                           'speaker': 'Narrator',
                                           'text': 'All around the sunken amphitheater, five centuries of '
                                                   'dormant Indemnitium veins ignite into a cathedral of '
                                                   'living sapphire water and golden star-dust!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_E2',
                                           'speaker': 'Furina',
                                           'text': 'My hands are not trembling anymore, Aether! Feel the '
                                                   'rhythm rising through the stone -- three-four time, '
                                                   "just like Maitre Renaud's clavecin!",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': 'outing_cruise'},
                                          {'beat_id': 'N36_E3',
                                           'speaker': 'Aether',
                                           'text': 'I have the bass root locked steady under my palm -- '
                                                   'lift your voice whenever you are ready!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_E4',
                                           'speaker': 'Narrator',
                                           'text': "Above us, the eleven-o'clock Solstice bell strikes its "
                                                   'deep bronze note, and Furina draws breath at the heart '
                                                   'of the mirror!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_B03',
                                           'speaker': 'Narrator',
                                           'text': 'Pressing my bare left palm against the central tuning '
                                                   'column while my right hand steadies hers, I open my '
                                                   'Fourth Descender channels wide as all three Spotlight '
                                                   'Meks converge in blinding silver-blue radiance!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                                           'voice_emotion': ''}],
                                'choice': None,
                                'routing': [{'default': True, 'next_node': 'N37'}],
                                'ending_id': None},
           'N37': {'node_id': 'N37',
                   'chapter_id': 'CH5',
                   'title': 'La Derniere Vaguelette & The Smile in the Foam',
                   'day_label': 'Day 9 - 11:02 PM',
                   'location': 'Sunken Mirror-Stage - Rising Sealight',
                   'beats': [{'beat_id': 'N37_B01',
                              'speaker': 'Narrator',
                              'text': 'Drawing a fearless breath, Furina lifts her pure mortal soprano '
                                      "into the wordless Act Four Cadenza of 'La Derniere Vaguelette' -- "
                                      'no longer singing as a false god on trial, but as the woman who '
                                      'endured every single night.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N37_B01B',
                              'speaker': 'Narrator',
                              'text': 'Down through our joined palms flows the crushing sub-bass weight of '
                                      'half a millennium -- lonely coronation mornings, rain-soaked '
                                      'prophecies, and midnight sobs muffled into velvet pillows -- all '
                                      'grounding harmlessly into golden starlight!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B02',
                              'speaker': 'Narrator',
                              'text': 'Around the vaulted gallery, all 182,375 crystal tear-masks lift off '
                                      'the stone walls like luminous blue butterflies, spiraling into a '
                                      "single soaring harmonic column straight up the Grand Organ's pipes!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B03_F06',
                              'speaker': 'Narrator',
                              'text': 'Woven gently beneath her soaring high note, a warm, unmistakable '
                                      'counter-phrase of brass harmonica breath echoes down from the '
                                      "acoustic vents -- as if fifty years of Maitre Renaud's devotion "
                                      'finally found its answer.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F06_HARMONICA_MERCY']}},
                             {'beat_id': 'N37_B04',
                              'speaker': 'Narrator',
                              'text': 'For three timeless heartbeats, shimmering sea-foam blurs the mirror '
                                      'water before us. Within the parting mist stands a tall, serene '
                                      'silhouette with twin cascading locks of pale blue light -- smiling '
                                      'at Furina with boundless, quiet pride before dissolving forever '
                                      'into warm morning spray.',
                              'inner_thought': 'Not a judge demanding another act -- only a final, loving '
                                               'curtain nod setting her human life completely free.',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B04B',
                              'speaker': 'Narrator',
                              'text': 'An illusory crown of ancient crystal splinters softly in the mist, '
                                      'drifting down as harmless warm rain across our shoulders.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_E1',
                              'speaker': 'Narrator',
                              'text': 'Measure by measure, the biting polar chill inside the cavern melts '
                                      'into warm sea-breeze smelling of sunlit Lumidouce Belles after '
                                      'summer rain.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_E2',
                              'speaker': 'Furina',
                              'text': 'Every tear I hid behind the velvet curtain... rise up the pipes and '
                                      'become music at last!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_E3',
                              'speaker': 'Aether',
                              'text': 'Keep soaring on the upper octave, Furina -- my golden channels are '
                                      'burning the whole undertow clean!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_E4',
                              'speaker': 'Narrator',
                              'text': 'Up through the sixty-foot acoustic shaft rolls a chord of pure, '
                                      'unburdened beauty such as Erinnyes Island has not heard in five '
                                      'hundred winters.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B05',
                              'speaker': 'Furina',
                              'text': '...Goodbye, mirror-stage. From this bar onward, my voice belongs to '
                                      'the living morning!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_mirror_cadenza_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N38_CURTAIN_GRASP'}],
                   'ending_id': None},
           'N38_CURTAIN_GRASP': {'node_id': 'N38_CURTAIN_GRASP',
                                 'chapter_id': 'CH5',
                                 'title': 'Piercing the Five-Hundred-Year Cascade',
                                 'day_label': 'Day 9 - 11:05 PM',
                                 'location': 'Sunken Mirror-Stage - Cresting Cascade',
                                 'beats': [{'beat_id': 'N38_B01',
                                            'speaker': 'Narrator',
                                            'text': 'As the final high note resolves, five centuries of '
                                                    'released Indemnitium pressure surge skyward in one '
                                                    'last blinding tidal curtain between our shoulders!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N38_B02_F07',
                                            'speaker': 'Narrator',
                                            'text': "Over my heart, 'L'Etoile d'Eau' flares like a living "
                                                    'sapphire compass star, cutting a crystalline path '
                                                    "straight toward Furina's outstretched fingers inside "
                                                    'the spray!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                            'voice_emotion': '',
                                            'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                           {'beat_id': 'N38_B02_NO_F07',
                                            'speaker': 'Narrator',
                                            'text': 'Flaring golden Fourth Descender starlight along my '
                                                    'bare arms, I lock onto the sapphire gleam of the star '
                                                    "pin on Furina's hat through the blinding spray!",
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                            'voice_emotion': '',
                                            'when': {'forbid_flags': ['F07_SAPPHIRE_PIN']}},
                                           {'beat_id': 'N38_E1',
                                            'speaker': 'Furina',
                                            'text': 'Aether -- the final pressure wave is cresting off the '
                                                    'mirror! Do not let the spray push us apart on the '
                                                    'last bar!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N38_E2',
                                            'speaker': 'Aether',
                                            'text': 'Not a chance in Teyvat -- reach your right hand '
                                                    'straight forward!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N38_E3',
                                            'speaker': 'Narrator',
                                            'text': 'Through dazzling prism-spray of blue and gold, her '
                                                    'ungloved fingers brush mine -- warm, alive, and '
                                                    'refusing to retreat!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N38_E4',
                                            'speaker': 'Narrator',
                                            'text': 'One decisive surge of willpower will seal this '
                                                    'five-hundred-year finale for good!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N38_B03',
                                            'speaker': 'Narrator',
                                            'text': 'Plunging both bare hands straight through the '
                                                    'five-hundred-year cascade, I feel the last crushing '
                                                    'psychic backlash strike my outlander meridians like '
                                                    'white-hot glass!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                            'voice_emotion': ''}],
                                 'choice': {'choice_id': 'C21_CH5',
                                            'prompt': 'Five centuries of parting tear-foam roar through '
                                                      'your channels as your fingers reach Furina:',
                                            'options': [{'opt_id': 'C21_A_COSTAR_CALL',
                                                         'label': 'Haul Furina fiercely against your chest '
                                                                  "and shout over the cascade: 'Come home "
                                                                  'to Quartier Lyonnais -- Scene 182,377 '
                                                                  "is ours!'",
                                                         'effects': {'bond': 2,
                                                                     'insight': 0,
                                                                     'add_flags': []},
                                                         'next_node': 'N39_LYONNAIS_WAKE',
                                                         'reaction_beats': [{'beat_id': 'N38_C21A_R1',
                                                                             'speaker': 'Aether',
                                                                             'text': 'Got you! Come home '
                                                                                     'to Quartier '
                                                                                     'Lyonnais, Furina -- '
                                                                                     'Scene 182,377 '
                                                                                     'belongs to the two '
                                                                                     'of us!',
                                                                             'inner_thought': '',
                                                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                                                             'voice_emotion': ''},
                                                                            {'beat_id': 'N38_C21A_R2',
                                                                             'speaker': 'Furina',
                                                                             'text': 'Aether!! Hold onto '
                                                                                     'me -- do not let go '
                                                                                     'even when the lights '
                                                                                     'go white!',
                                                                             'inner_thought': '',
                                                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                                                             'voice_emotion': 'vn_tender_love'},
                                                                            {'beat_id': 'N38_C21A_R3',
                                                                             'speaker': 'Narrator',
                                                                             'text': 'Wrapping both arms '
                                                                                     'around her trembling '
                                                                                     'shoulders as the '
                                                                                     'cascade turns to '
                                                                                     'warm, harmless '
                                                                                     'spring rain, a sharp '
                                                                                     'crimson trickle runs '
                                                                                     'down my left temple '
                                                                                     '-- and the '
                                                                                     'subterranean lights '
                                                                                     'dissolve into quiet '
                                                                                     'gold.',
                                                                             'inner_thought': '',
                                                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                                                             'voice_emotion': ''}]},
                                                        {'opt_id': 'C21_B_TEAR_SIPHON',
                                                         'label': 'Synchronize your Fourth Descender '
                                                                  "channels to Pneumousia's deepest bass "
                                                                  'root, transmuting every last drop of '
                                                                  'pressure into pure dew!',
                                                         'effects': {'bond': 1,
                                                                     'insight': 2,
                                                                     'add_flags': []},
                                                         'next_node': 'N39_LYONNAIS_WAKE',
                                                         'reaction_beats': [{'beat_id': 'N38_C21B_R1',
                                                                             'speaker': 'Narrator',
                                                                             'text': 'Locking my grip '
                                                                                     "around Furina's "
                                                                                     'right hand, I align '
                                                                                     'every outlander '
                                                                                     'meridian to the '
                                                                                     "Grand Organ's lowest "
                                                                                     'Pneumousia root -- '
                                                                                     'drinking the entire '
                                                                                     '500-year Indemnitium '
                                                                                     'rebound and burning '
                                                                                     'it clean into warm '
                                                                                     'morning mist!',
                                                                             'inner_thought': 'Not one '
                                                                                              'lingering '
                                                                                              'crystal of '
                                                                                              'frost '
                                                                                              'remains in '
                                                                                              'the basin '
                                                                                              '-- or in '
                                                                                              'her nerves!',
                                                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                                                             'voice_emotion': ''},
                                                                            {'beat_id': 'N38_C21B_R2',
                                                                             'speaker': 'Furina',
                                                                             'text': 'My right hand -- the '
                                                                                     'ice in my wrist just '
                                                                                     'vanished completely! '
                                                                                     'Aether?! Hey, lean '
                                                                                     'on me -- I have got '
                                                                                     'you!',
                                                                             'inner_thought': '',
                                                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                                                             'voice_emotion': 'outing_bump_rescue'},
                                                                            {'beat_id': 'N38_C21B_R3',
                                                                             'speaker': 'Narrator',
                                                                             'text': 'As the cistern '
                                                                                     'settles into a '
                                                                                     'crystal-clear, '
                                                                                     'peaceful pool, a '
                                                                                     'warm drop of blood '
                                                                                     'slips down my left '
                                                                                     'temple from neural '
                                                                                     'overload -- and I '
                                                                                     'sink safely against '
                                                                                     "Furina's shoulder.",
                                                                             'inner_thought': '',
                                                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_cascade_grasp_diff.jpg',
                                                                             'voice_emotion': ''}]}]},
                                 'routing': [],
                                 'ending_id': None},
           'N39_LYONNAIS_WAKE': {'node_id': 'N39_LYONNAIS_WAKE',
                                 'chapter_id': 'CH5',
                                 'title': 'Forty-Eight Hours in Quartier Lyonnais',
                                 'day_label': 'Day 12 - 07:00 AM',
                                 'location': "Quartier Lyonnais - Furina's Sunlit Bedroom",
                                 'beats': [{'beat_id': 'N39_B01',
                                            'speaker': 'Narrator',
                                            'text': 'Forty-eight hours drift past in muffled waves of cool '
                                                    'Romaritime compresses and quiet footsteps before '
                                                    'golden winter sunshine finally parts my eyelids.',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_B02',
                                            'speaker': 'Narrator',
                                            'text': 'A dull, cottony ring still lingers in my left ear '
                                                    'where the capillary burst at my temple, yet my chest '
                                                    'breathes easy under a soft quilted Fontaine duvet.',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_B02_SCAR',
                                            'speaker': 'Narrator',
                                            'text': 'Around my left forearm sits a neat roll of clean '
                                                    "white gauze dressed with Sigewinne's salve -- the "
                                                    "souvenir of taking Night Nine's unbuffered opening "
                                                    'rime-shard across my guard arm.',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': '',
                                            'when': {'all_flags': ['ROUTE_A'],
                                                     'forbid_flags': ['TUNED_DUET_CHORD']}},
                                           {'beat_id': 'N39_B03',
                                            'speaker': 'Sigewinne',
                                            'text': 'Good morning, patient! Keep your head low on the '
                                                    'pillow -- grounding five centuries of acoustic '
                                                    'pressure gave you a two-day neural fever, though your '
                                                    'left ear will clear completely by tonight!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_B04',
                                            'speaker': 'Narrator',
                                            'text': 'Turning my head slowly toward the sunlit window, my '
                                                    'breath catches. Folded asleep on her arms across the '
                                                    'edge of the mattress is hatless Furina -- clutching '
                                                    'my right hand inside BOTH of her bare palms.',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_B05',
                                            'speaker': 'Narrator',
                                            'text': 'Neither hand is icy anymore. From her fingertips to '
                                                    'her right pulse, her skin radiates steady, '
                                                    'unmistakable human warmth.',
                                            'inner_thought': 'Two sleepless nights keeping watch at my '
                                                             'bedside -- and every trace of tear-frost is '
                                                             'gone for good.',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_B06',
                                            'speaker': 'Aether',
                                            'text': 'Thank you, Head Nurse Sigewinne... Let me not wake '
                                                    'her for one more minute.',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_E1',
                                            'speaker': 'Sigewinne',
                                            'text': 'Honestly, you two gave Monsieur Neuvillette and '
                                                    'Clorinde ten new gray hairs when you walked up the '
                                                    'Lucine stairs leaning on each other at midnight!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_E2',
                                            'speaker': 'Aether',
                                            'text': 'Did the cistern seal hold cleanly after the Solstice '
                                                    'tide passed?',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_E3',
                                            'speaker': 'Sigewinne',
                                            'text': 'Clear as pure mountain spring water! Freminet dove '
                                                    'down yesterday afternoon and said not a single '
                                                    'crystal of rime remains under the Opera House!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_E4',
                                            'speaker': 'Narrator',
                                            'text': 'Beside my mattress, Furina murmurs my name softly in '
                                                    'her sleep, tightening her warm fingers around my hand '
                                                    'as if checking I am still real.',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''},
                                           {'beat_id': 'N39_B07',
                                            'speaker': 'Sigewinne',
                                            'text': 'Hehe, good luck with that! The moment your pulse sped '
                                                    'up just now, her eyelashes started fluttering -- I '
                                                    'will let your loud friends in the parlor know you are '
                                                    'conscious!',
                                            'inner_thought': '',
                                            'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_bedside_base.jpg',
                                            'voice_emotion': ''}],
                                 'choice': None,
                                 'routing': [{'default': True, 'next_node': 'N40'}],
                                 'ending_id': None},
           'N40': {'node_id': 'N40',
                   'chapter_id': 'CH5',
                   'title': 'The First Bite of Sweetness & The Phantom Overture',
                   'day_label': 'Day 12 - 09:30 AM to 04:30 PM',
                   'location': 'Quartier Lyonnais & Opera Epiclese Matinee',
                   'beats': [{'beat_id': 'N40_B01',
                              'speaker': 'Paimon',
                              'text': 'AETHER!! Waaah, you woke up!! Navia, Charlotte, Lyney, Lynette -- '
                                      'come quick, sleepyhead is finally opening his eyes!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B01B',
                              'speaker': 'Furina',
                              'text': 'Mmph -- wh-who authorized full-volume shouting in the recovery '
                                      'ward?! Oh -- Aether!! You reckless, insufferable co-star, do you '
                                      'know how many towels I wrung out for forty-eight hours?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': 'outing_bump_rescue'},
                             {'beat_id': 'N40_B01C',
                              'speaker': 'Lyney',
                              'text': 'She barely blinked for two straight nights, my friend -- Lynette '
                                      'and I practically had to conjure chamomile tea into her hands!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B01D',
                              'speaker': 'Lynette',
                              'text': 'Bedside devotion rating: ten out of ten.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B02',
                              'speaker': 'Charlotte',
                              'text': 'Do you have any idea what happened up in the Opera House at eleven '
                                      "o'clock on Night Nine?! Furina's Cadenza down in the cistern rang "
                                      "straight up the Grand Organ pipes like a 'Phantom Overture' -- half "
                                      'the audience was weeping before Monsieur Neuvillette calmly moved '
                                      'the main premiere to this afternoon!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B03',
                              'speaker': 'Navia',
                              'text': 'And wait till you taste the recovery pastry box Spina di Rosula '
                                      'brought! Go on, Furina -- Sigewinne says the bedside nurse has '
                                      'barely eaten a crumb since Night Nine!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B04',
                              'speaker': 'Narrator',
                              'text': 'Blinking awake with rosy cheeks, Furina hesitantly lifts a pink '
                                      "strawberry macaron from Navia's box and takes one small bite. "
                                      'Instantly, her heterochromatic eyes widen -- and crystal-clear, '
                                      'warm tears of pure joy spill over her lashes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B05',
                              'speaker': 'Furina',
                              'text': '...It is sweet. Aether -- I can taste the strawberries and the '
                                      'almond cream again!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N40_B06_F06',
                              'speaker': 'Narrator',
                              'text': 'That afternoon at the triumphant rescheduled Gala premiere, young '
                                      "Celine's soprano soars effortlessly alongside Furina's direction -- "
                                      'while in the very back row, silver-haired Maitre Renaud raises his '
                                      'brass ear-trumpet and applauds through proud tears.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F06_HARMONICA_MERCY']}},
                             {'beat_id': 'N40_E1',
                              'speaker': 'Paimon',
                              'text': 'Whoa -- Furina ate a second macaron AND the pistachio one too! '
                                      'Welcome back, reigning Dessert Queen of Quartier Lyonnais!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_E2',
                              'speaker': 'Furina',
                              'text': 'Sniff... I am NOT crying over almond meringue, Paimon, the sunlit '
                                      'window is simply glaring in my eyes! Here, Aether -- open wide, the '
                                      'nurse insists you test the raspberry filling too!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N40_E3',
                              'speaker': 'Aether',
                              'text': 'Sweetest pastry in all of Fontaine -- house rule honored in full.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_E4',
                              'speaker': 'Charlotte',
                              'text': 'Hold that smile right there, you two -- strictly for my personal '
                                      'scrapbook, not the newspaper, cross my heart!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B06_NO_F06',
                              'speaker': 'Narrator',
                              'text': 'That afternoon at the triumphant rescheduled Gala premiere, young '
                                      "Celine's soprano soars effortlessly under Furina's radiant "
                                      'direction as six curtain calls shake the chandeliers of the Opera '
                                      'Epiclese.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_lyonnais_macaron_joy_diff.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F06_HARMONICA_MERCY']}}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N41_ROYAL_BOX_DAWN'}],
                   'ending_id': None},
           'N41_ROYAL_BOX_DAWN': {'node_id': 'N41_ROYAL_BOX_DAWN',
                                  'chapter_id': 'CH5',
                                  'title': 'Twilight in the Empty Royal Box',
                                  'day_label': 'Day 12 - 06:15 PM (Golden Twilight)',
                                  'location': 'Opera Epiclese - Empty Royal Box',
                                  'beats': [{'beat_id': 'N41_B01_F07',
                                             'speaker': 'Narrator',
                                             'text': 'After the cheering crowds stream out into twilight, '
                                                     'Furina leads me up a private velvet stair into the '
                                                     'empty Royal Box overlooking the warm, golden stage '
                                                     '-- setting her top hat on the crimson rail with its '
                                                     'navy hatband still bare of its star pin.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_barehat_base.jpg',
                                             'voice_emotion': '',
                                             'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_B01_NO_F07',
                                             'speaker': 'Narrator',
                                             'text': 'After the cheering crowds stream out into twilight, '
                                                     'Furina leads me up a private velvet stair into the '
                                                     'empty Royal Box overlooking the warm, golden stage '
                                                     '-- setting her top hat on the crimson rail where its '
                                                     'sapphire-plume star pin glints softly.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                                             'voice_emotion': '',
                                             'when': {'forbid_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_B02_F07',
                                             'speaker': 'Narrator',
                                             'text': 'Before I can turn around, two slender bare hands '
                                                     'slip playfully from behind my shoulders to cover '
                                                     'both my eyes.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_barehat_base.jpg',
                                             'voice_emotion': '',
                                             'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_B02_NO_F07',
                                             'speaker': 'Narrator',
                                             'text': 'Before I can turn around, two slender bare hands '
                                                     'slip playfully from behind my shoulders to cover '
                                                     'both my eyes.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                                             'voice_emotion': '',
                                             'when': {'forbid_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_B03_F01_P',
                                             'speaker': 'Narrator',
                                             'text': 'Unlike that freezing right wrist I caught on our '
                                                     'very first morning in Quartier Lyonnais, BOTH of her '
                                                     'palms resting against my eyelids tonight are '
                                                     'gloriously, unmistakably warm.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_barehat_base.jpg',
                                             'voice_emotion': '',
                                             'when': {'all_flags': ['F01_TEAR_RIME_CHILL',
                                                                    'F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_B03_F01_NP',
                                             'speaker': 'Narrator',
                                             'text': 'Unlike that freezing right wrist I caught on our '
                                                     'very first morning in Quartier Lyonnais, BOTH of her '
                                                     'palms resting against my eyelids tonight are '
                                                     'gloriously, unmistakably warm.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                                             'voice_emotion': '',
                                             'when': {'all_flags': ['F01_TEAR_RIME_CHILL'],
                                                      'forbid_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_B04_P',
                                             'speaker': 'Furina',
                                             'text': 'Five hundred years of scripted tragedy finally took '
                                                     'their bow today, Aether... Now that Scene 182,377 '
                                                     'has an empty page waiting tomorrow morning, tell me '
                                                     'honestly: where do you intend to stand?',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_barehat_base.jpg',
                                             'voice_emotion': 'vn_tender_love',
                                             'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_E1',
                                             'speaker': 'Narrator',
                                             'text': 'Down on the empty stage below the Royal Box, dust '
                                                     'motes float lazily through amber sunset beams where '
                                                     'Celine and the chorus took six curtain bows an hour '
                                                     'ago.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                                             'voice_emotion': '',
                                             'when': {'forbid_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_E1_P',
                                             'speaker': 'Narrator',
                                             'text': 'Down on the empty stage below the Royal Box, dust '
                                                     'motes float lazily through amber sunset beams where '
                                                     'Celine and the chorus took six curtain bows an hour '
                                                     'ago.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_barehat_base.jpg',
                                             'voice_emotion': '',
                                             'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_E2',
                                             'speaker': 'Aether',
                                             'text': 'Six standing ovations, Director. Even Monsieur '
                                                     'Neuvillette clapped until his gloves wore thin.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                                             'voice_emotion': '',
                                             'when': {'forbid_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_E2_P',
                                             'speaker': 'Aether',
                                             'text': 'Six standing ovations, Director. Even Monsieur '
                                                     'Neuvillette clapped until his gloves wore thin.',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_barehat_base.jpg',
                                             'voice_emotion': '',
                                             'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                                            {'beat_id': 'N41_B04_NP',
                                             'speaker': 'Furina',
                                             'text': 'Five hundred years of scripted tragedy finally took '
                                                     'their bow today, Aether... Now that Scene 182,377 '
                                                     'has an empty page waiting tomorrow morning, tell me '
                                                     'honestly: where do you intend to stand?',
                                             'inner_thought': '',
                                             'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                                             'voice_emotion': 'vn_tender_love',
                                             'when': {'forbid_flags': ['F07_SAPPHIRE_PIN']}}],
                                  'choice': {'choice_id': 'C22_FINAL',
                                             'priority_unlock': True,
                                             'prompt': 'Amber twilight illuminates the velvet railing '
                                                       "between Seat Number One and Furina's upturned "
                                                       'eyes:',
                                             'options': [{'opt_id': 'C22_TRUE_CONFESS',
                                                          'when': {'all_flags': ['F07_SAPPHIRE_PIN'],
                                                                   'forbid_flags': ['DETACHED_SPECTATOR_NO_DUET'],
                                                                   'any_of': [{'min_bond': 16},
                                                                              {'min_bond': 14,
                                                                               'min_insight': 14}]},
                                                          'unlock_badge': '[UNSCRIPTED ENCORE UNLOCKED]',
                                                          'lock_hint': '[LOCKED: Needs Star Pin F07 + No '
                                                                       'Spectator Wall + (Bond 16 OR Bond '
                                                                       '14 & Insight 14)]',
                                                          'label': 'Step across the velvet railing out of '
                                                                   "Seat Number One forever, pin 'L'Etoile "
                                                                   "d'Eau' back onto her hat, and claim "
                                                                   'your place as her lifetime co-star.',
                                                          'effects': {'bond': 0,
                                                                      'insight': 0,
                                                                      'add_flags': ['TRUE_ENCORE_SEALED']},
                                                          'next_node': 'N42',
                                                          'reaction_beats': [{'beat_id': 'N41_C22T_R1',
                                                                              'speaker': 'Aether',
                                                                              'text': 'Seat Number One is '
                                                                                      'retired as of '
                                                                                      'tonight, Furina. '
                                                                                      'Wherever my '
                                                                                      'journeys go and '
                                                                                      'however many '
                                                                                      'mornings come '
                                                                                      'after, I am '
                                                                                      'returning to the '
                                                                                      'girl standing right '
                                                                                      'beside me on the '
                                                                                      'stage.',
                                                                              'inner_thought': '',
                                                                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                                                                              'voice_emotion': ''}]},
                                                         {'opt_id': 'C22_NEUTRAL_OVATION',
                                                          'label': 'Remain gently on the audience side of '
                                                                   'the velvet railing and offer your '
                                                                   'brightest standing ovation as her '
                                                                   'devoted Seat Number One.',
                                                          'effects': {'bond': 0,
                                                                      'insight': 0,
                                                                      'add_flags': []},
                                                          'next_node': 'N44',
                                                          'reaction_beats': [{'beat_id': 'N41_C22N_R1',
                                                                              'speaker': 'Aether',
                                                                              'text': 'Right where you can '
                                                                                      'always find me '
                                                                                      'whenever the '
                                                                                      'spotlight turns '
                                                                                      'bright, Furina -- '
                                                                                      'applauding louder '
                                                                                      'than anyone in '
                                                                                      'Fontaine from Seat '
                                                                                      'Number One.',
                                                                              'inner_thought': '',
                                                                              'cg': 'ui_assets/story_quest_cgs/furina/end_neutral_seat_one_bow.jpg',
                                                                              'voice_emotion': ''}]}]},
                                  'routing': [],
                                  'ending_id': None},
           'N42': {'node_id': 'N42',
                   'chapter_id': 'CH5',
                   'title': 'Twin Plumes Over a Living Heart',
                   'day_label': 'Day 12 - 06:30 PM',
                   'location': 'Opera Epiclese - Royal Box',
                   'beats': [{'beat_id': 'N42_B01',
                              'speaker': 'Narrator',
                              'text': "Stepping cleanly past the crimson velvet divider, I lift Furina's "
                                      "navy top hat from the railing and fasten 'L'Etoile d'Eau' home "
                                      'through its two familiar pinholes -- the sapphire star catching '
                                      'twilight like living water.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B02_F02',
                              'speaker': 'Aether',
                              'text': 'After all, house rules in Quartier Lyonnais are binding: savory '
                                      'first, sweet to close -- and we have a whole lifetime of sweet '
                                      'mornings to catch up on.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F02_MACARONI_RULE']}},
                             {'beat_id': 'N42_B02_F04',
                              'speaker': 'Aether',
                              'text': 'Besides, two lead actors shook hands on the Outer Seawall: neither '
                                      'of us ever takes a curtain bow while the other is left behind.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F04_ROOFTOP_ENCORE']}},
                             {'beat_id': 'N42_B03',
                              'speaker': 'Furina',
                              'text': 'W-wait a second -- you cannot just improvise a line like that '
                                      'before I deliver my cue! Hold completely still, Aether!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_twin_plumes_diff.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N42_B04',
                              'speaker': 'Narrator',
                              'text': 'Ears glowing crimson beneath her white-and-blue curls, Furina opens '
                                      'a small silk box from Chioriya Boutique and pins a delicate Twin '
                                      'Blue-and-Gold Plume Boutonniere directly onto my scarf above my '
                                      'beating heart.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_twin_plumes_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B05',
                              'speaker': 'Furina',
                              'text': '...I secretly asked Chiori to craft this twin plume on Day Seven in '
                                      'a moment of terrible cowardice. Originally, I meant to seal it '
                                      'inside a farewell envelope for you if I lost my voice... How '
                                      'infinitely happier I am to pin it onto your living heart myself!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_twin_plumes_diff.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N42_B06',
                              'speaker': 'Aether',
                              'text': 'So that was why Chiori measured my scarf lapel on Day Seven! No '
                                      'wonder she told me not to ask behind the screen.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_twin_plumes_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_E1',
                              'speaker': 'Narrator',
                              'text': 'In the hush of the golden auditorium, the sapphire plume on her '
                                      'hatband and the twin blue-and-gold plumes over my heart catch the '
                                      'exact same ray of twilight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_twin_plumes_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_E2',
                              'speaker': 'Aether',
                              'text': 'No wonder you guarded those navy envelopes so fiercely on the '
                                      "terrace -- half of your heart was already hidden inside Chiori's "
                                      'silk box.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_twin_plumes_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_E3',
                              'speaker': 'Furina',
                              'text': 'All of it, you dense co-star... Every last scene of it.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_twin_plumes_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_E4',
                              'speaker': 'Narrator',
                              'text': 'Resting her forehead lightly against my collarbone for a long, '
                                      'quiet breath, Furina listens to the steady beat beneath the twin '
                                      'plumes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_twin_plumes_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B07',
                              'speaker': 'Furina',
                              'text': 'H-Hush! Not another word about my secret commissions -- take my '
                                      'hand and escort your leading lady back to Erinnyes under the stars!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_twin_plumes_diff.jpg',
                              'voice_emotion': 'vn_shy_blush'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N43'}],
                   'ending_id': None},
           'N43': {'node_id': 'N43',
                   'chapter_id': 'CH5',
                   'title': 'Unscripted Encore for Two',
                   'day_label': 'Day 12 - 11:45 PM (Starry Midnight)',
                   'location': 'Erinnyes Island - Fountain of Lucine',
                   'beats': [{'beat_id': 'N43_B01',
                              'speaker': 'Narrator',
                              'text': 'Just before midnight on Night Twelve, we walk hand-in-hand back to '
                                      'where our twelve days began. Under a galaxy-clear winter sky, the '
                                      'Fountain of Lucine sings in gentle, untroubled silver arcs -- free '
                                      'of frost forever.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B02',
                              'speaker': 'Narrator',
                              'text': 'Ten paces down the marble walkway, Mademoiselle Crabaletta, '
                                      'Surintendante Chevalmarin, and Gentilhomme Usher puff out their '
                                      'chests and turn politely outward -- screening their director from '
                                      'every late-night passerby.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B02B',
                              'speaker': 'Aether',
                              'text': 'Twelve nights ago at this exact balustrade, you asked who went '
                                      'creeping across Erinnyes at a quarter to one.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B03',
                              'speaker': 'Furina',
                              'text': 'Listen, Aether... No organ rattle, no courtroom whispers -- only '
                                      'warm water under the stars. Stay close as you cross into Natlan and '
                                      'beyond, because your co-star will be waiting with hot macaroni and '
                                      'new scripts every time you come home!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N43_B03B',
                              'speaker': 'Aether',
                              'text': 'Every single encore, Furina. You will never stand on a dark stage '
                                      'alone again.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B04',
                              'speaker': 'Narrator',
                              'text': 'Rising onto tiptoe beside the starlit basin, Furina tilts the brim '
                                      'of her star-pinned top hat with one warm bare hand, catches my '
                                      'scarf over the twin plumes with the other, and presses her lips '
                                      'softly to mine.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_E1',
                              'speaker': 'Narrator',
                              'text': 'Silver spray from the Fountain of Lucine catches the winter '
                                      'constellations overhead, wrapping the quiet plaza in soft music.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_E2',
                              'speaker': 'Furina',
                              'text': 'Do not dare make me wait too long between letters when you travel '
                                      'west, Aether -- an unscripted encore requires both leads at '
                                      'rehearsals!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_E3',
                              'speaker': 'Aether',
                              'text': 'Every port, every waypoint, every festival sky -- my compass points '
                                      'straight back to Quartier Lyonnais.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_E4',
                              'speaker': 'Narrator',
                              'text': 'Her fingers interlace warmly with mine, neither hand hidden behind '
                                      'gloves or footlights ever again.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B05',
                              'speaker': 'Furina',
                              'text': '...Sweet. Strawberry-macaron sweet -- welcome to Scene 182,377, my '
                                      'beloved co-star.',
                              'inner_thought': 'TRUE ENDING -- Unscripted Encore for Two.',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_true_lucine_kiss.jpg',
                              'voice_emotion': 'vn_tender_love'}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_TRUE'},
           'N44': {'node_id': 'N44',
                   'chapter_id': 'CH5',
                   'title': 'Standing Ovation from Seat Number One',
                   'day_label': 'Day 12 - 06:30 PM',
                   'location': 'Opera Epiclese - Royal Box Velvet Rail',
                   'beats': [{'beat_id': 'N44_B01_RETURN_F07',
                              'speaker': 'Narrator',
                              'text': 'Keeping the promise I gave in Chioriya Boutique, I reach across the '
                                      'crimson velvet railing and open my palm -- formally returning '
                                      "'L'Etoile d'Eau' into Furina's warm bare hand now that her curtain "
                                      'call is safe.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_barehat_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                             {'beat_id': 'N44_B02_RETURN_F07',
                              'speaker': 'Narrator',
                              'text': 'Closing her fingers softly over the sapphire-plume star pin, Furina '
                                      'fastens it back onto her navy hatband before placing her hat on '
                                      'with a graceful tilt.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SAPPHIRE_PIN']}},
                             {'beat_id': 'N44_B01_NO_F07',
                              'speaker': 'Narrator',
                              'text': 'Lifting her navy top hat from the crimson railing, Furina lets her '
                                      'warm fingertips brush the sapphire-plume star pin gleaming on her '
                                      'hatband before placing her hat on with a graceful tilt.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/ch5_royal_box_with_pin_diff.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_SAPPHIRE_PIN']}},
                             {'beat_id': 'N44_E1',
                              'speaker': 'Aether',
                              'text': 'Watching you take the spotlight whole and unburdened this afternoon '
                                      'was worth every step across Fontaine, Furina.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_neutral_seat_one_bow.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N44_E2',
                              'speaker': 'Narrator',
                              'text': 'Golden dusk settles gently across the crimson velvet tiers of the '
                                      'Opera Epiclese as the chandeliers dim to warm amber.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_neutral_seat_one_bow.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N44_44A_B01',
                              'speaker': 'Furina',
                              'text': '...Still choosing Seat Number One tonight, are you? Hmph -- half a '
                                      'step of crimson velvet has never felt quite so wide, Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_neutral_seat_one_bow.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['DETACHED_SPECTATOR_NO_DUET'], 'min_bond': 14}},
                             {'beat_id': 'N44_44A_B02',
                              'speaker': 'Furina',
                              'text': "Keep that Seat Number One ticket warm through Natlan's fires for "
                                      "me, all right? Perhaps by next season's premiere... your director "
                                      'will be brave enough to write your name straight onto the stage.',
                              'inner_thought': 'NEUTRAL ENDING (44A) -- Half a Velvet Rail Between Two '
                                               'Hearts.',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_neutral_seat_one_bow.jpg',
                              'voice_emotion': 'vn_tender_love',
                              'when': {'forbid_flags': ['DETACHED_SPECTATOR_NO_DUET'], 'min_bond': 14}},
                             {'beat_id': 'N44_44B_B01',
                              'speaker': 'Furina',
                              'text': 'When the mirage rose at the footlights, you stayed on the audience '
                                      'side and shattered the glass with steady clarity. Perhaps a star '
                                      'truly needs one clear-eyed critic who never loses his head in the '
                                      'spotlights.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_neutral_seat_one_bow.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['DETACHED_SPECTATOR_NO_DUET']}},
                             {'beat_id': 'N44_44B_B02',
                              'speaker': 'Narrator',
                              'text': 'Sweeping a poised, radiant bow from the sunlit side of the rail '
                                      'while I applaud from the shadowed aisle, Furina honors the '
                                      'dignified glass boundary I chose to keep between us.',
                              'inner_thought': 'NEUTRAL ENDING (44B) -- The Clear-Eyed Witness in Seat '
                                               'Number One.',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_neutral_seat_one_bow.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['DETACHED_SPECTATOR_NO_DUET']}},
                             {'beat_id': 'N44_44C_B01',
                              'speaker': 'Furina',
                              'text': 'Bravo, my reliable Assistant Director! Thanks to you, both my voice '
                                      "and Fontaine's grandest Gala came through without a single dropped "
                                      'cue!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_neutral_seat_one_bow.jpg',
                              'voice_emotion': 'vn_sweet_happy',
                              'when': {'forbid_flags': ['DETACHED_SPECTATOR_NO_DUET'], 'max_bond': 13}},
                             {'beat_id': 'N44_44C_B02',
                              'speaker': 'Furina',
                              'text': 'Whenever your travels bring you back from Natlan, knock properly on '
                                      'my door in Quartier Lyonnais -- I will have a fresh pot of '
                                      'tomato-sauce macaroni and strawberry macarons waiting for my '
                                      'favorite friend!',
                              'inner_thought': 'NEUTRAL ENDING (44C) -- Standing Ovation Among Dear '
                                               'Friends.',
                              'cg': 'ui_assets/story_quest_cgs/furina/end_neutral_seat_one_bow.jpg',
                              'voice_emotion': 'outing_arrive_photo',
                              'when': {'forbid_flags': ['DETACHED_SPECTATOR_NO_DUET'], 'max_bond': 13}}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_NEUTRAL'}}}

STORY_QUEST_CAMPAIGNS: list[dict] = [STORY_QUEST_CAMPAIGN]
