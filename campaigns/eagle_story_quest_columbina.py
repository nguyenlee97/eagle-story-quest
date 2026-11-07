r"""
Columbina Hyposelenia 5-Chapter Pure Branching Visual Novel Campaign Pack ("Somnias a Luna: Lullaby of the Fallen Moon")
Subtitle: "Five-Chapter Branching Visual Novel -- Silvermoon Hall & Zapolyarny Conservatory"
Character: Columbina (`char_id = "columbina"`, `ped_id = 49431`)
Target Runtime: C:\Users\LENOVO\Desktop\GTA\Project Eagle\gta sa gameplay-lab
Plug-and-Play Contract: exports `STORY_QUEST_CAMPAIGN` and `STORY_QUEST_CAMPAIGNS` for `StoryQuestEngine` v2.0.
"""
from __future__ import annotations

STORY_QUEST_CAMPAIGN: dict = {'char_id': 'columbina',
 'ped_id': 49431,
 'display_name': 'Columbina',
 'campaign_id': 'columbina_sq1_lullaby_of_the_fallen_moon',
 'title': 'Somnias a Luna: Lullaby of the Fallen Moon',
 'subtitle': 'Five-Chapter Branching Visual Novel -- Silvermoon Hall & Zapolyarny Conservatory',
 'poster_cg': 'ui_assets/story_quest_cgs/columbina/columbina_sq1_poster.jpg',
 'synopsis': "Beneath Nod-Krai's frost moon, Columbina's lullaby fractures under the ancient Seelie curse: "
             'an Angel who loves one chosen soul alone crumbles into a hollow husk -- unless the Fourth '
             "Descender rewrites heaven's law before the lunar eclipse.",
 'version': '2.1.0',
 'theme_rgb': [244, 114, 182],
 'chapters': [{'chapter_id': 'CH1',
               'index': 1,
               'title': 'Chapter 1 -- Where the Moonfall Silver Pales',
               'entry_node': 'N01'},
              {'chapter_id': 'CH2',
               'index': 2,
               'title': 'Chapter 2 -- Tea Beneath the Frost-Glass Dome',
               'entry_node': 'N09'},
              {'chapter_id': 'CH3',
               'index': 3,
               'title': 'Chapter 3 -- Thorns of the Crimson & Pale Moons',
               'entry_node': 'N18'},
              {'chapter_id': 'CH4',
               'index': 4,
               'title': 'Chapter 4 -- Zapolyarny Glass Winter & Sanctum Crisis',
               'entry_node': 'N28'},
              {'chapter_id': 'CH5',
               'index': 5,
               'title': 'Chapter 5 -- Somnias a Luna: Beyond the False Sky',
               'entry_node': 'N36'}],
 'initial_state': {'bond': 0, 'insight': 0, 'flags': []},
 'flag_catalog': {'F01_HEARD_SILENT_NOTE': {'title': 'The Unsung Rest Between Bars',
                                            'clue_hint': 'Listened in stillness to the silent breath '
                                                         "between phrases of Columbina's lullaby inside "
                                                         'Silvermoon Hall.'},
                  'F02_FALSE_SKY_CONFIDANT': {'title': 'Witness Beyond the Painted Firmament',
                                              'clue_hint': 'Confided outlander memories of the true cosmos '
                                                           "beyond Teyvat's False Sky, echoing why she "
                                                           'veiled her eyes.'},
                  'F03_CHILDE_INSTINCT_HEEDED': {'title': "Tartaglia's Pier Warning",
                                                 'clue_hint': "Heeded Childe's warning about No. 3's eerie "
                                                              'serenity at Nasha Pier while refusing to '
                                                              'treat Columbina as a monster.'},
                  'F04_KUUHENKI_LULLABY_SHARED': {'title': 'Outlander Counter-Melody for Luonnotar',
                                                  'clue_hint': 'Hummed a quiet star-traveler '
                                                               'counter-melody beside Columbina to lull '
                                                               'Luonnotar and the Kuuhenki after midnight '
                                                               'rain.'},
                  'F05_BRUSHED_MORNING_PLAITS': {'title': 'Morning Plaits & First-Frost Berries',
                                                 'clue_hint': "Unknotted Columbina's tangled morning hair "
                                                              'by hand and shared warm hearth-bread with '
                                                              'sweet northern berries.'},
                  'F06_VESNA_SEELIE_CODEX': {'title': "Koitar's Hyperborean Seelie Codex",
                                             'clue_hint': 'Decoded the Snowland Fae mural with Vesna '
                                                          'Strivozha, revealing how exclusive devotion '
                                                          "triggers an Angel's inner soul-seal."},
                  'F07_MOONWEAVE_RIBBON_CHIME': {'title': 'Moonweave Ribbon & Luonnotar Chime',
                                                 'clue_hint': "Entrusted with Columbina's moon-spun hair "
                                                              'ribbon and silver Luonnotar pulse-chime '
                                                              'attuned directly to her heartbeat.'},
                  'F08_SANDRONE_TEA_FORMULA': {'title': "Sandrone's Differential Decay Curve",
                                               'clue_hint': "Memorized Sandrone's World-Formula harmonic "
                                                            "constants mapping Columbina's midnight Day 12 "
                                                            'calcification asymptote.'},
                  'F09_DESCENDER_HARMONIC_PACT': {'title': 'Fourth Descender Grounding Pact',
                                                  'clue_hint': 'Forged an extra-cosmic Descender harmonic '
                                                               'pact in Zapolyarny to drain the Angel '
                                                               "Curse beyond Irminsul's closed loop."},
                  'F10_KOITAR_COUNTERPOINT_SCORE': {'title': "First Angel's Unfinished Counterpoint",
                                                    'clue_hint': "Transcribed Koitar's unfinished "
                                                                 'Hyperborean duet score inside the '
                                                                 'crystalline vault of the Deep Gallery.'},
                  'F11_COLD_PROTOCOL': {'title': 'Hairline Frost of Harbinger Distance',
                                        'clue_hint': 'Drew back before the porcelain crack at her throat '
                                                     "or invoked No. 3's protocol, leaving hairline "
                                                     'fractures across her veil.'},
                  'F12_CRIMSON_MARROW_TUNING': {'title': 'Crimson Moon Phase-Dampener',
                                                'clue_hint': "Calibrated Arlecchino's Crimson Moon "
                                                             "harmonic dampener with Sandrone's astrolabe "
                                                             'prism down in the Deep Gallery.'}},
 'endings': {'END_TRUE': {'rank': 'TRUE ENDING',
                          'title': 'Somnias a Luna: Home Beneath Both Skies',
                          'tone': 'radiant',
                          'summary': 'Draining the Seelie curse past the False Sky through their Moonweave '
                                     "conduit, Columbina unties her X-veil forever -- gazing into Aether's "
                                     "eyes with luminous lotus-pink irises at Silvermoon Hall's open "
                                     'hearth.',
                          'epilogue_cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg'},
             'END_GOOD': {'rank': 'GOOD ENDING',
                          'title': "Winter's Lullaby Behind Frosted Glass",
                          'tone': 'warm',
                          'summary': "While Sandrone's valves and Vesna's pylons shield Hiisi Island, the "
                                     "Tsaritsa seals Columbina in gentle camellia stasis beside Sandrone's "
                                     'wax-cylinder phonograph -- preserving every memory until spring '
                                     'thaw.',
                          'epilogue_cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg'},
             'END_NEUTRAL': {'rank': 'NEUTRAL ENDING',
                             'title': 'Through the Moonlight Veil',
                             'tone': 'bittersweet',
                             'summary': 'Keeping her X-lattice veil tied across the eclipse apex spares '
                                        "Columbina's mind from shattering, leaving her veiled in quiet "
                                        'moonlight until another lunar cycle -- or parted behind mist.',
                             'epilogue_cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg'},
             'END_BAD_1': {'rank': 'BAD ENDING I',
                           'title': 'Elogia Cinerosa: Mercy of No. 3',
                           'tone': 'tragic',
                           'summary': "Atop Hiisi's ruined cliff-altar, Columbina answers Aether's "
                                      'hesitation by freezing her newborn mortal heart into the Third '
                                      "Harbinger's calm ice -- walking barefoot into the blizzard humming "
                                      'Elogia Cinerosa.',
                           'epilogue_cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg'},
             'END_BAD_2': {'rank': 'BAD ENDING II',
                           'title': 'Porcelain Seelie of Silvermoon Hall',
                           'tone': 'tragic',
                           'summary': 'Shattering the Eclipse Prism halts calcification without an '
                                      "outlander drain, scrubbing every memory of Aether from Columbina's "
                                      'soul -- leaving a serene stranger asking why the kneeling traveler '
                                      'weeps.',
                           'epilogue_cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg'}},
 'nodes': {'N01': {'node_id': 'N01',
                   'chapter_id': 'CH1',
                   'title': 'Echoes in Silvermoon Hall',
                   'day_label': 'Day 1 - Dusk, 18:30',
                   'location': 'Hiisi Island - Silvermoon Hall Cavern',
                   'bgm_bucket': 'vn_daily_sweet',
                   'flowchart_pos': [0, 2],
                   'beats': [{'beat_id': 'N01_B01',
                              'speaker': 'Narrator',
                              'text': "Twelve nights before Nod-Krai's decennial frost-moon eclipse, a "
                                      'tiny lunar spirit shaped like a silver hare leads Paimon and me '
                                      'beneath the mossy stone arch of Silvermoon Hall.',
                              'inner_thought': 'Even the coastal wind hushes at the threshold, as if '
                                               'afraid of waking a five-hundred-year dream.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B02',
                              'speaker': 'Narrator',
                              'text': 'Inside the subterranean grotto, pale-blue Kuuvahki mist curls '
                                      'across mirrored water and carpets of luminous Moonfall Silver '
                                      'blossoms.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B03',
                              'speaker': 'Paimon',
                              'text': 'Whoa... keep your voice down, Aether! Look up on that moss-draped '
                                      'stone arch above the pool -- Luonnotar flew straight to her sleeve!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B04',
                              'speaker': 'Narrator',
                              'text': 'Seated barefoot upon the carved limestone rib is Columbina. Six '
                                      'snow-white dove wings crown her dark, magenta-tipped hair while a '
                                      'delicate white X-lattice veil rests across her closed eyes.',
                              'inner_thought': 'Neither Archon throne nor Harbinger banner surrounds her '
                                               'here -- only blue flowers and quiet water.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B05',
                              'speaker': 'Narrator',
                              'text': 'Unaware -- or wholly unbothered -- by our steps on the wet shingle, '
                                      'she sways her bare ankles above the tide and hums a slow, wordless '
                                      'lullaby in three-quarter time.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B06',
                              'speaker': 'Columbina',
                              'text': 'Mm... la-la, sleep beneath the silver bough, little tide... where '
                                      'no star asks your name...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_base.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N01_B07',
                              'speaker': 'Narrator',
                              'text': 'Every Moonfall Silver corolla along the bank tilts toward her '
                                      'melody like a compass needle, drinking the cool lunar resonance '
                                      'drifting from her fingertips.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B08',
                              'speaker': 'Narrator',
                              'text': 'Yet right at the turn of the eighth bar, her voice drops out for '
                                      'half a measure. In that deliberate rest, a faint, solitary sigh '
                                      'slips past her lips -- almost too soft for mortal ears.',
                              'inner_thought': 'That pause was not written for serenity; it sounded like '
                                               'an echo waiting in vain for a second voice.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B09',
                              'speaker': 'Paimon',
                              'text': "Wait -- did she stop singing because she sensed us, or is Paimon's "
                                      'stomach rumbling over the honey-bread in our pack?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B10',
                              'speaker': 'Narrator',
                              'text': 'Above the water, Columbina rests her chin lightly against her knee. '
                                      'Beneath the X-woven gauze of the Seelie Court seal, her lips curve '
                                      'in a tranquil, expectant smile.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_diff_smile.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B11',
                              'speaker': 'Columbina',
                              'text': 'Two heartbeats at my doorway... one small and fluttering like a '
                                      'finch near warm crust, and one steady as gold forged beyond the '
                                      'painted sky.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_diff_smile.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B12',
                              'speaker': 'Aether',
                              'text': 'We followed Luonnotar in from the frost-ridge when the evening tide '
                                      'rose. We did not mean to intrude on your song, Columbina.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_diff_smile.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B13',
                              'speaker': 'Columbina',
                              'text': 'Intrude? A lullaby sung to stone and water belongs to no one, '
                                      'Aether... not even to the singer. Tell me, then, what brought you '
                                      'to halt at the edge of the pool?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_diff_smile.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B14',
                              'speaker': 'Narrator',
                              'text': 'Little Luonnotar peers down from the folds of her pearl-white '
                                      "sleeve as the cavern's silver-blue acoustics wait upon my answer.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_diff_smile.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C01',
                              'prompt': 'Columbina tilts her veiled face toward the water, awaiting how '
                                        'you answer her lullaby.',
                              'options': [{'opt_id': 'C01_A',
                                           'label': 'Remain still and tell her you heard the lonely '
                                                    'half-measure rest sighing between her verses.',
                                           'effects': {'bond': 2,
                                                       'insight': 1,
                                                       'add_flags': ['F01_HEARD_SILENT_NOTE']},
                                           'next_node': 'N02',
                                           'reaction_beats': [{'beat_id': 'N01_R_A1',
                                                               'speaker': 'Aether',
                                                               'text': 'It was not the notes themselves '
                                                                       'that stopped me, Columbina. It was '
                                                                       'that silent half-beat between the '
                                                                       'bars -- as if the song left room '
                                                                       'for an answer that never came.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_diff_smile.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N01_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': '...Oh. Five hundred winters of '
                                                                       'petitioners have praised my voice, '
                                                                       'yet not one ever listened to the '
                                                                       'breath where I stopped singing.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_diff_smile.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C01_B',
                                           'label': 'Greet her warmly and offer to share fresh '
                                                    'honey-glazed hearth bread with her and Paimon.',
                                           'effects': {'bond': 2, 'insight': 0},
                                           'next_node': 'N02',
                                           'reaction_beats': [{'beat_id': 'N01_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'The wind off Nasha Sound is '
                                                                       'freezing tonight. We brought warm '
                                                                       'honey-bread from town, and it '
                                                                       'tastes far better shared than '
                                                                       'eaten on the road.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_diff_smile.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N01_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Hehe... warm bread carried all the '
                                                                       'way to a damp cavern, with no '
                                                                       'prayer attached to the crust? What '
                                                                       'a rare and gentle offering.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n01_diff_smile.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N02': {'node_id': 'N02',
                   'chapter_id': 'CH1',
                   'title': 'Blue Flowers of Hiisi',
                   'day_label': 'Day 1 - Evening, 20:00',
                   'location': 'Silvermoon Hall - Subterranean Waterside',
                   'bgm_bucket': 'vn_daily_sweet',
                   'flowchart_pos': [1, 2],
                   'beats': [{'beat_id': 'N02_B01',
                              'speaker': 'Narrator',
                              'text': 'While Paimon drifts back toward the warm lantern niche by the '
                                      'entrance to count our remaining honey-loaves, I walk beside '
                                      'Columbina along the subterranean waterside.',
                              'inner_thought': 'Leaving Paimon by the warm brazier lets our footsteps keep '
                                               "the grotto's unhurried hush.",
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B02',
                              'speaker': 'Narrator',
                              'text': 'Bare heels skimming silent as mist over smooth slate, Columbina '
                                      'stoops beside a cluster of glowing blue Moonfall Silver lilies '
                                      'where tiny Kuuhenki sprites bob like glass lanterns.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B03_F01',
                              'speaker': 'Columbina',
                              'text': 'You noticed my silent measure earlier, Aether. Long ago, whoever '
                                      'sang that cradle-song to me before I woke left the very same gap -- '
                                      'though I have never recalled her face.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F01_HEARD_SILENT_NOTE']}},
                             {'beat_id': 'N02_B03_NOF01',
                              'speaker': 'Columbina',
                              'text': 'A drop of clover honey from your bread lingered on my thumb... the '
                                      'Kuuhenki have been circling my sleeve ever since, begging for a '
                                      'taste of mortal warmth.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F01_HEARD_SILENT_NOTE']}},
                             {'beat_id': 'N02_B04',
                              'speaker': 'Aether',
                              'text': 'These blue blossoms brighten whenever your hem brushes past them. '
                                      "Is the island's Kuuvahki tide always this high?",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B05',
                              'speaker': 'Columbina',
                              'text': 'Eleven nights from tomorrow midnight marks the decennial perigee '
                                      "eclipse, when the Frost Moon's remnant draws closest to Hiisi's "
                                      'veins. Until that hour passes, the underground current swells.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B06',
                              'speaker': 'Narrator',
                              'text': 'She cradles a bashful Kuuhenki in both palms, letting its cool '
                                      'azure luminescence wash across the sheer white ribbons at her '
                                      'wrists.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B07',
                              'speaker': 'Columbina',
                              'text': 'When I first stepped out of the silver spring five centuries ago, '
                                      'the elders of the Frostmoon Scions knelt in rows along this very '
                                      'bank. Their eyes burned so fiercely through my veil.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B08',
                              'speaker': 'Aether',
                              'text': 'They wanted miracles from a newborn goddess before asking whether '
                                      'she even knew how to walk on stone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B09',
                              'speaker': 'Columbina',
                              'text': 'Oracles, victories, eternal shelter... and centuries later in '
                                      'Snezhnaya, the Fatui asked to borrow my lullaby as a winter '
                                      'deterrent. Between altar and palace, I felt like rootless grass '
                                      'drifting on water.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B10',
                              'speaker': 'Columbina',
                              'text': 'Yet when you stand beside me here, Aether, your Kuuvahki signature '
                                      'asks for nothing at all. It simply hums -- warm, steady, and '
                                      'strange as summer starlight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N02_B11',
                              'speaker': 'Narrator',
                              'text': 'The little Kuuhenki hops from her palm toward my sleeve, chiming '
                                      'twice before gliding back into the glowing reeds.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B12',
                              'speaker': 'Aether',
                              'text': 'Come on. The night air is growing sharper near the upper shaft -- '
                                      'let us walk up toward the skylight gallery.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N03'}],
                   'ending_id': None},
           'N03': {'node_id': 'N03',
                   'chapter_id': 'CH1',
                   'title': 'An Eye Mask Woven of Moonlight',
                   'day_label': 'Day 1 - Late Night, 22:15',
                   'location': 'Silvermoon Hall - Upper Skylight Oculi',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'flowchart_pos': [2, 2],
                   'beats': [{'beat_id': 'N03_B01',
                              'speaker': 'Narrator',
                              'text': 'Past ten at night, we climb a spiral stair of weathered frost-stone '
                                      'to an open circular oculus where pale aurora ribbons trail across '
                                      "Nod-Krai's sky.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B02',
                              'speaker': 'Paimon',
                              'text': 'Brrr! Even indoors, the wind coming straight down through that '
                                      "ceiling ring nips right through Paimon's scarf!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B03',
                              'speaker': 'Narrator',
                              'text': 'Columbina stands directly beneath the shaft of silver moonlight, '
                                      'tilting her face upward as fine snow-dust catches on the six white '
                                      'wings crowning her hair.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B04',
                              'speaker': 'Narrator',
                              'text': 'Up close, the translucent white X-lattice covering her eyes gleams '
                                      'with tiny geometric diamond knots -- the unmistakable emblem of an '
                                      'ancient Seelie Court.',
                              'inner_thought': 'That filigree predates the Seven Archons; it matches the '
                                               'ruined Seelie pillars scattered across Teyvat.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B05',
                              'speaker': 'Columbina',
                              'text': 'You are staring at my eye mask, Traveler. Do you wonder, like young '
                                      'Childe once did, whether I keep some dreadful abyssal glare locked '
                                      'behind the lace?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N03_B06',
                              'speaker': 'Aether',
                              'text': 'No. Here on Hiisi Island, you navigate every step through Kuuvahki '
                                      'clearer than sight. Which means the veil is a choice -- not '
                                      'blindness.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B07',
                              'speaker': 'Narrator',
                              'text': 'Her slender fingers rise to brush the crossed moon-silk over her '
                                      'bridge, hesitating for a heartbeat as the aurora shifts overhead.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B08',
                              'speaker': 'Columbina',
                              'text': 'On the night I was born from the spring, I looked up once through '
                                      'this very oculus... and saw a firmament painted onto glass, cold '
                                      'and counterfeit as stage scenery.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B09',
                              'speaker': 'Columbina',
                              'text': "Why open one's eyes to revere an inverted lie? So I wove moonlight "
                                      'over my lashes... though if I am wholly honest, another nameless '
                                      'tremor stayed my hand.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B10',
                              'speaker': 'Aether',
                              'text': 'A tremor?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B11',
                              'speaker': 'Columbina',
                              'text': 'Whenever I imagine lifting this gauze to look upon one person -- '
                                      'truly look, so that no other face in all the world matters -- '
                                      'something deep inside my chest shivers like thin porcelain over '
                                      'ice.',
                              'inner_thought': 'She does not know the written words of the law, yet her '
                                               "soul remembers the executioner's blade.",
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B12',
                              'speaker': 'Paimon',
                              'text': 'Huh? Just from looking at somebody?! That sounds super lonely, '
                                      'Columbina...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B13',
                              'speaker': 'Narrator',
                              'text': 'Snowflakes drift between us in the shaft of pale moonlight as '
                                      'Columbina lowers her hand from the X-lattice veil, listening '
                                      'quietly to my pulse.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C02',
                              'prompt': 'Beneath the open oculus, Columbina confides both her rejection of '
                                        "Teyvat's sky and her nameless dread.",
                              'options': [{'opt_id': 'C02_A',
                                           'label': "Confide your outlander truth: Teyvat's sky is indeed "
                                                    'a false shell, and you have sailed the real sea of '
                                                    'stars beyond it.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F02_FALSE_SKY_CONFIDANT']},
                                           'next_node': 'N04',
                                           'reaction_beats': [{'beat_id': 'N03_R_A1',
                                                               'speaker': 'Aether',
                                                               'text': 'Your instinct was never madness, '
                                                                       'Columbina. Before this world '
                                                                       'snared my wings, I crossed the '
                                                                       'true cosmos beyond that dome -- '
                                                                       'where stars burn unbound by any '
                                                                       "throne's ledger.",
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N03_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': "...Unbound by Teyvat's ledger. No "
                                                                       'wonder your footsteps ring like a '
                                                                       'note written outside the staff. '
                                                                       'Tell me more of that sky someday, '
                                                                       'Outlander.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C02_B',
                                           'label': 'Take her chilled fingers gently and promise to '
                                                    'describe every honest color on earth until she never '
                                                    'feels alone behind the veil.',
                                           'effects': {'bond': 2, 'insight': 1},
                                           'next_node': 'N04',
                                           'reaction_beats': [{'beat_id': 'N03_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Then keep the painted sky shut out '
                                                                       'as long as you wish. Give me your '
                                                                       'hand -- whenever we walk below it, '
                                                                       'I will tell you every real color '
                                                                       'worth keeping.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N03_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Your palm is almost fever-warm '
                                                                       'against mine... Careful, Aether, '
                                                                       'or I may grow spoiled borrowing '
                                                                       'your eyes.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n03_skylight_mask.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N04': {'node_id': 'N04',
                   'chapter_id': 'CH1',
                   'title': 'Footsteps on Starsand Frost',
                   'day_label': 'Day 2 - Noon, 12:30',
                   'location': 'Starsand Shoal - Sunlit Frost Trail',
                   'bgm_bucket': 'vn_daily_sweet',
                   'flowchart_pos': [3, 2],
                   'beats': [{'beat_id': 'N04_B01',
                              'speaker': 'Narrator',
                              'text': 'Crisp noon sun glitters across the frozen shingle of Starsand Shoal '
                                      'the next day as Columbina, Paimon, and I follow the coastal path '
                                      "toward Nasha Town's outer pier.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B02',
                              'speaker': 'Paimon',
                              'text': 'Paimon still cannot believe a baby Kuuhenki snapped two harp '
                                      'strings trying to imitate your morning trill! Good thing Nasha '
                                      "Pier's tinker stocks silver wire.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B03',
                              'speaker': 'Narrator',
                              'text': 'Despite the sub-zero sea breeze, Columbina walks barefoot across '
                                      'the sparkling frost-crust without leaving a single melted print, '
                                      'frost-mist swirling softly around her white ankle ribbons.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B04_F02',
                              'speaker': 'Columbina',
                              'text': 'Under this bright noon glare, Aether... are the true stars you '
                                      'crossed beyond the shell cold white like snow, or warm gold like '
                                      'the braid on your shoulder?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F02_FALSE_SKY_CONFIDANT']}},
                             {'beat_id': 'N04_B04_NOF02',
                              'speaker': 'Columbina',
                              'text': 'You promised last night to lend me earthly colors, Aether. Tell me '
                                      '-- what shade does the noon frost wear where my shadow meets yours?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F02_FALSE_SKY_CONFIDANT']}},
                             {'beat_id': 'N04_B05',
                              'speaker': 'Aether',
                              'text': 'Right where the sunlight hits the rime beside your heels, it '
                                      'scatters pale rose and sea-blue -- almost the exact gradient of '
                                      'your hair and cloak.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B06',
                              'speaker': 'Columbina',
                              'text': 'Mm... rose and sea-blue. In Zapolyarny Palace, winter wore only '
                                      'iron gray and ceremonial silver.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N04_B07',
                              'speaker': 'Narrator',
                              'text': 'Halfway down the causeway, I spot three snapped wooden boundary '
                                      'stakes half-buried in the drift -- scorched cleanly in half by twin '
                                      'Hydro blades.',
                              'inner_thought': 'Fresh Fatui boot-treads in the slush... someone '
                                               'intercepted a patrol here less than an hour ago.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B08',
                              'speaker': 'Paimon',
                              'text': 'Uh-oh! Those charred insignias belong to rogue Fatui skirmishers! '
                                      'Why would soldiers be sneaking toward Hiisi Island?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B09',
                              'speaker': 'Columbina',
                              'text': 'Old echoes travel slowly across frozen seas. When the Tsaritsa '
                                      'first issued the Palestar Edict to retrieve me, certain garrisons '
                                      'never learned when to lower their spears.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B10',
                              'speaker': 'Aether',
                              'text': 'Stay half a pace behind me as we round the headland. Whoever cut '
                                      'those stakes used Foul Legacy-grade Hydro.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B11',
                              'speaker': 'Columbina',
                              'text': 'Oh, there is no danger in that scent of ozone and whale-spray. You '
                                      'know that noisy eleventh seat far better than I do, Traveler.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B12',
                              'speaker': 'Narrator',
                              'text': 'As the salt-wind carries the clang of a slung polar bow from the '
                                      'sunlit pier ahead, we descend the final snow-stair toward the '
                                      'harbor.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n04_starsand_noon.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N05'}],
                   'ending_id': None},
           'N05': {'node_id': 'N05',
                   'chapter_id': 'CH1',
                   'title': "Tartaglia's Warning at Nasha Pier",
                   'day_label': 'Day 2 - Sunset, 17:15',
                   'location': 'Nasha Outer Pier - Icebreaker Mooring',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [4, 2],
                   'beats': [{'beat_id': 'N05_B01',
                              'speaker': 'Narrator',
                              'text': 'By the time we finish trading for silver harp-wire and reach the '
                                      'outer pier, low crimson sunset bleeds across the pack ice -- where '
                                      'Tartaglia sits atop a bound stack of confiscated Fatui rifles.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B02',
                              'speaker': 'Tartaglia',
                              'text': 'Well, well! Look who comes strolling out of the frost-mist! Hey '
                                      'there, comrade -- and... ah.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B03',
                              'speaker': 'Narrator',
                              'text': "The easy grin freezes half-formed on Childe's face the instant his "
                                      'gaze lands on Columbina standing serenely beside the mooring '
                                      'bollard. Instinctively, his right hand drops two inches toward his '
                                      'Hydro Vision.',
                              'inner_thought': 'Even the Eleventh Harbinger, who begs to spar with abyssal '
                                               'beasts, stiffens in her quiet shadow.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B04',
                              'speaker': 'Columbina',
                              'text': 'Good evening, Tartaglia. You swept away those noisy deserters along '
                                      'the shoal so my little Kuuhenki could sleep... how thoughtful of '
                                      'the Eleventh.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B05',
                              'speaker': 'Tartaglia',
                              'text': 'Ha... haha, do not mention it, Lady Damselette. Just clearing out '
                                      "hotheads who missed Lady Sandrone's dispatch that the Palestar "
                                      'Edict is under review.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B06',
                              'speaker': 'Narrator',
                              'text': 'While Columbina steps softly to the pier rail with Paimon to feed '
                                      'breadcrumbs to the ice-gulls, Childe catches my elbow and draws me '
                                      'behind a frosted crane mast.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B07',
                              'speaker': 'Tartaglia',
                              'text': 'Listen to me closely, comrade -- and keep your voice low. What in '
                                      "the Tsaritsa's name are you doing walking unguarded beside Number "
                                      'Three?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B08',
                              'speaker': 'Aether',
                              'text': 'She left her Harbinger seat behind, Childe. On Hiisi Island she has '
                                      'done nothing more dangerous than mend harp strings and hum to '
                                      'moon-sprites.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B09',
                              'speaker': 'Tartaglia',
                              'text': 'That is the exact part that raises every hair on my neck! I will '
                                      'gladly cross blades with The Captain or The Knave, because I can '
                                      'read their killing intent.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B10',
                              'speaker': 'Tartaglia',
                              'text': 'With Columbina, there is zero malice -- just bottomless, singing '
                                      'stillness. Even the Wanderer told me once: if you ever recoil from '
                                      'her or push her heart into a corner, she will freeze herself hollow '
                                      'with a smile and break your conscience.',
                              'inner_thought': "Childe's warning rings dead-serious; beneath his "
                                               'battle-lust, his survival instincts never lie.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B11',
                              'speaker': 'Narrator',
                              'text': "At the pier's edge, sunset light glints across Columbina's six "
                                      'white hair-wings as she turns her veiled face unerringly toward our '
                                      'hushed corner.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B12',
                              'speaker': 'Tartaglia',
                              'text': 'Storm clouds are rolling in hard off the sound. Whatever happens '
                                      "before next week's eclipse, Aether -- do not say your comrade never "
                                      'warned you.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B13',
                              'speaker': 'Aether',
                              'text': 'What about your unit?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B14',
                              'speaker': 'Tartaglia',
                              'text': "Holding the outer fjord perimeter with Vesna's frost-birch scouts "
                                      'so no more rogue squads bother Hiisi. Now go -- she is already '
                                      'waiting for your step.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C03',
                              'prompt': 'Tartaglia watches grimly as you turn back toward Columbina on the '
                                        'darkening pier.',
                              'options': [{'opt_id': 'C03_A',
                                           'label': "Take Childe's warning to heart -- never recoil from "
                                                    'her nature, yet vow to judge Columbina with your own '
                                                    'eyes.',
                                           'effects': {'bond': 1,
                                                       'insight': 2,
                                                       'add_flags': ['F03_CHILDE_INSTINCT_HEEDED']},
                                           'next_node': 'N06',
                                           'reaction_beats': [{'beat_id': 'N05_R_A1',
                                                               'speaker': 'Aether',
                                                               'text': 'I hear you, Childe, and I will '
                                                                       'remember what both you and '
                                                                       'Wanderer saw. If fear or '
                                                                       'hesitation is what pushes her over '
                                                                       'the edge, then I will make sure my '
                                                                       'hand never flinches.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N05_R_A2',
                                                               'speaker': 'Tartaglia',
                                                               'text': 'Hah... spoken like the crazy '
                                                                       'outlander I know. Watch your '
                                                                       'footing out there, partner.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C03_B',
                                           'label': 'Brush the Harbinger rumors aside and walk straight '
                                                    'back to shield Columbina from the rising sea-squall.',
                                           'effects': {'bond': 2, 'insight': 0},
                                           'next_node': 'N06',
                                           'reaction_beats': [{'beat_id': 'N05_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Ranks in Zapolyarny mean nothing '
                                                                       'out here, Childe. Right now she is '
                                                                       'just someone waiting in a cold '
                                                                       'wind with a spool of harp wire.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N05_R_B2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Without glancing back at the '
                                                                       'stacked rifles, I stride across '
                                                                       'the planks and drape my travel '
                                                                       'cloak between Columbina and the '
                                                                       'freezing spray.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n05_tartaglia_pier.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N06': {'node_id': 'N06',
                   'chapter_id': 'CH1',
                   'title': 'Shelter Beneath Vaulted Rain',
                   'day_label': 'Day 2 - Night Rain, 20:30',
                   'location': 'Hiisi Ruined Causeway - Vaulted Stone Colonnade',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'flowchart_pos': [5, 2],
                   'beats': [{'beat_id': 'N06_B01',
                              'speaker': 'Narrator',
                              'text': 'Halfway back across the island causeway, icy sleet-rain bursts from '
                                      'low slate clouds, driving us beneath a vaulted colonnade of ancient '
                                      'moon-carved stone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B02',
                              'speaker': 'Paimon',
                              'text': "Achoo!! Brrr, Paimon's boots are soaked! Good thing this covered "
                                      'gallery still has dry flagstones inside!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B03',
                              'speaker': 'Narrator',
                              'text': 'While Paimon curls inside my dry outer pack near a warm Pyro-lit '
                                      "brazier stone, Columbina lingers at the colonnade's dripping arch, "
                                      'extending one pale palm into the silver curtain of rain.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B04_F03',
                              'speaker': 'Columbina',
                              'text': 'Young Tartaglia warned you to guard your conscience around me at '
                                      'the pier, did he not? His pulse always races like a trapped hare '
                                      'whenever I hum.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F03_CHILDE_INSTINCT_HEEDED']}},
                             {'beat_id': 'N06_B04_NOF03',
                              'speaker': 'Columbina',
                              'text': 'Listen to the rain striking the arches, Aether... so many hurried '
                                      'little notes tumbling home to the sea.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F03_CHILDE_INSTINCT_HEEDED']}},
                             {'beat_id': 'N06_B05',
                              'speaker': 'Aether',
                              'text': 'Your fingertips are turning ice-cold. Step half a pace back under '
                                      'the vault with me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B06',
                              'speaker': 'Columbina',
                              'text': 'I enjoy listening to rain, Traveler. Mortals hurry under roofs '
                                      'because someone waits inside with a dry towel and soup... they call '
                                      "that 'shelter,' and 'home.'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N06_B07',
                              'speaker': 'Columbina',
                              'text': 'For five hundred years, rain only meant water returning to '
                                      'Kuuvahki. Whether it fell on stone or on my hair made no difference '
                                      'at all.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B08',
                              'speaker': 'Narrator',
                              'text': 'Unfolding a clean linen cloth from my satchel, I gently blot the '
                                      'gleaming rain-beads from the magenta curls resting over her '
                                      'collarbone.',
                              'inner_thought': 'She goes utterly still beneath the cloth -- not pulling '
                                               'away by even a breadth.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B09',
                              'speaker': 'Columbina',
                              'text': '...Oh. So this is why mortals hurry under stone arches when clouds '
                                      'gather.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B10',
                              'speaker': 'Aether',
                              'text': 'Because catching a chill just to study raindrops makes whoever '
                                      'walks beside you worry.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B11',
                              'speaker': 'Columbina',
                              'text': 'Worry... for me, rather than for what my power might cost the tide. '
                                      'Do not say such warm things carelessly, Aether, or this rain may '
                                      'linger in my chest.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B12',
                              'speaker': 'Narrator',
                              'text': 'As the downpour softens to a fine silver mist past nine, we carry '
                                      'the sleeping Paimon back down the lantern path into Silvermoon '
                                      'Hall.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n06_rain_colonnade.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N07'}],
                   'ending_id': None},
           'N07': {'node_id': 'N07',
                   'chapter_id': 'CH1',
                   'title': 'Lullaby for Luonnotar',
                   'day_label': 'Day 2 - Late Night, 23:30',
                   'location': 'Silvermoon Hall - Inner Basin Alcove',
                   'bgm_bucket': 'vn_daily_sweet',
                   'flowchart_pos': [6, 2],
                   'beats': [{'beat_id': 'N07_B01',
                              'speaker': 'Narrator',
                              'text': 'Half an hour before midnight, the inner alcove of Silvermoon Hall '
                                      'glows like blue mother-of-pearl while Paimon snores softly under a '
                                      'fleece blanket in the dry side-niche.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B02',
                              'speaker': 'Narrator',
                              'text': "Beside the basin's mossy rim, however, Luonnotar and half a dozen "
                                      'young Kuuhenki dart restlessly above the Moonfall Silver stems, '
                                      'agitated by distant storm-barometric tremors.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B03',
                              'speaker': 'Columbina',
                              'text': 'Hush now, little ones... the sleet cannot reach you down here, and '
                                      'your harp has new silver strings.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B04',
                              'speaker': 'Narrator',
                              'text': 'Sitting cross-legged on the smooth stone ledge beside me, Columbina '
                                      "cradles sleepy Luonnotar in her lap, stroking the spirit's "
                                      'translucent ears as glowing blue petals brush her hem.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B05',
                              'speaker': 'Aether',
                              'text': 'Even the water-rings look tighter tonight. Is the approaching '
                                      'eclipse already tugging at them?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B06',
                              'speaker': 'Columbina',
                              'text': "Yes. Every ten years, when the pale moon's shadow crosses the "
                                      "perigee, my voice must steady the subterranean tide so Hiisi's "
                                      'springs do not surge.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B07',
                              'speaker': 'Columbina',
                              'text': 'Usually my solo lullaby settles Luonnotar within three breaths... '
                                      'yet tonight she keeps turning toward your shoulder, listening for a '
                                      'second note.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N07_B08',
                              'speaker': 'Narrator',
                              'text': 'True to her word, the little silver spirit peeks up from '
                                      "Columbina's white sleeve, twitching one luminous ear toward me.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B09',
                              'speaker': 'Aether',
                              'text': 'Looks like your choir conductor wants a guest performer before '
                                      'midnight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B10',
                              'speaker': 'Columbina',
                              'text': 'Will you oblige her, Traveler? A melody from beyond this sky -- or '
                                      'a bedtime tale where small souls choose their own names -- might '
                                      'soothe what my voice alone cannot.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B11',
                              'speaker': 'Narrator',
                              'text': 'In the quiet grotto, our shoulders rest scarce an inch apart above '
                                      'the mirror-still basin.',
                              'inner_thought': 'Her breathing has slowed to match the exact cadence of my '
                                               'own chest.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B12',
                              'speaker': 'Columbina',
                              'text': "Come closer to the water's edge, Aether. The cavern carries low "
                                      'whispers clearest right here.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B13',
                              'speaker': 'Narrator',
                              'text': 'One by one, the small Kuuhenki gather like floating sapphires '
                                      'around our knees, waiting for me to join her night-watch.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B14',
                              'speaker': 'Columbina',
                              'text': 'Whenever you are ready... I am listening.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C04',
                              'prompt': 'Beside the midnight basin, Luonnotar and Columbina lean close to '
                                        'hear how you answer the night vigil.',
                              'options': [{'opt_id': 'C04_A',
                                           'label': 'Hum a gentle outlander star-melody in counterpoint '
                                                    "with Columbina's lullaby until Luonnotar drifts to "
                                                    'sleep.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F04_KUUHENKI_LULLABY_SHARED']},
                                           'next_node': 'N08',
                                           'reaction_beats': [{'beat_id': 'N07_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Lowering my voice to a soft '
                                                                       'baritone hum, I weave an old '
                                                                       "star-voyager's cradle tune "
                                                                       'directly across the empty '
                                                                       "half-beat of Columbina's lullaby.",
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N07_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': '...Ah. How effortlessly your fifth '
                                                                       'interval fills the rest I left '
                                                                       'empty for five hundred years.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C04_B',
                                           'label': "Tell a quiet traveler's tale of wandering spirits who "
                                                    'cast off imposed titles to claim names of their own.',
                                           'effects': {'bond': 1, 'insight': 2},
                                           'next_node': 'N08',
                                           'reaction_beats': [{'beat_id': 'N07_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Out among older worlds, I once met '
                                                                       'tiny drift-lights born solely to '
                                                                       'guide royal fleets -- until one '
                                                                       'chose its own name and stayed '
                                                                       'beside a quiet harbor fire '
                                                                       'instead.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N07_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'A name chosen for warmth rather '
                                                                       'than duty... Luonnotar likes that '
                                                                       'ending, Aether. And so do I.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N08': {'node_id': 'N08',
                   'chapter_id': 'CH1',
                   'title': 'The First White Petal',
                   'day_label': 'Day 3 - Deep Night, 01:15',
                   'location': 'Silvermoon Hall - Inner Basin Midnight',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [7, 2],
                   'beats': [{'beat_id': 'N08_B01',
                              'speaker': 'Narrator',
                              'text': 'Midnight slips past unnoticed into the small hours of Day Three. By '
                                      'a quarter past one, every Kuuhenki along the bank floats fast '
                                      'asleep like dimmed blue glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B02_F04',
                              'speaker': 'Columbina',
                              'text': 'Your star-melody is still lingering under the vault, Aether... my '
                                      'chest feels as warm as sunlit snow.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F04_KUUHENKI_LULLABY_SHARED']}},
                             {'beat_id': 'N08_B02_NOF04',
                              'speaker': 'Columbina',
                              'text': 'Your story of chosen names is still lingering under the vault, '
                                      'Aether... my chest feels strangely light tonight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F04_KUUHENKI_LULLABY_SHARED']}},
                             {'beat_id': 'N08_B03',
                              'speaker': 'Narrator',
                              'text': 'Half-drowsy in the silver hush, Columbina lets her temple tip '
                                      'sideways until the soft dark crown of her hair rests directly '
                                      'against my shoulder.',
                              'inner_thought': 'For the first time since we met, her Kuuvahki aura stops '
                                               'dispersing into the cavern -- locking solely onto me.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B04',
                              'speaker': 'Columbina',
                              'text': 'If I hummed only for one listener tomorrow... just one, instead of '
                                      'the whole island... would that be terribly selfish of a Moon '
                                      'Maiden?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B05',
                              'speaker': 'Aether',
                              'text': 'Even the moon deserves one place where she does not have to shine '
                                      'for everyone at once.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B06',
                              'speaker': 'Narrator',
                              'text': 'At that quiet confession, her heartbeat and Kuuvahki phase-lock '
                                      'completely onto mine -- and deep inside the ancient seed of her '
                                      'soul, a dormant law snaps awake!',
                              'inner_thought': 'Something razor-cold just rang from inside her chest -- '
                                               'like crystal stressed past its breaking point!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B07',
                              'speaker': 'Columbina',
                              'text': '...Ngh--!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B08',
                              'speaker': 'Narrator',
                              'text': 'Columbina inhales sharply, pressing slim fingers just below her '
                                      'throat. Across the pale skin of her left collarbone, a hairline '
                                      'seam glints dead, chalky porcelain-white!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B09',
                              'speaker': 'Narrator',
                              'text': 'Down beside her bare heel, the brightest blue Moonfall Silver lily '
                                      'shudders -- draining of every drop of azure glow until its petals '
                                      'bleach white as ash-bone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B10',
                              'speaker': 'Aether',
                              'text': 'Columbina?! Your collarbone -- your skin went freezing cold in a '
                                      'split second! Stay still, let me see!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B11',
                              'speaker': 'Columbina',
                              'text': 'Ah... strange. That sting felt just like the nameless chill from my '
                                      'cradle-song... yet there is no Abyssal taint anywhere in the hall.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B12',
                              'speaker': 'Narrator',
                              'text': 'As soon as she draws half a breath back to compose herself, the '
                                      'eerie porcelain seam dims beneath her skin -- leaving the single '
                                      'bone-white flower trembling at her ankle.',
                              'inner_thought': 'That was not an outside attack. It ignited from within the '
                                               'very instant her heart leaned toward me alone.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B13',
                              'speaker': 'Columbina',
                              'text': 'Forgive me, Aether... perhaps the perigee tide merely startled my '
                                      'pulse. Let us rest until morning light reaches the courtyard.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n08_omen_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N09'}],
                   'ending_id': None},
           'N09': {'node_id': 'N09',
                   'chapter_id': 'CH2',
                   'title': 'Tangled Plaits & Wild Berries',
                   'day_label': 'Day 3 - Morning, 08:30',
                   'location': 'Silvermoon Hall - Sunlit Stone Courtyard',
                   'bgm_bucket': 'vn_daily_sweet',
                   'flowchart_pos': [8, 2],
                   'beats': [{'beat_id': 'N09_B01',
                              'speaker': 'Narrator',
                              'text': "Pale morning sun filters into Silvermoon Hall's open courtyard, "
                                      'warming the frost off the stone bench where Paimon sets out toasted '
                                      'rye slices and a wooden bowl of glistening northern cloudberries.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B02',
                              'speaker': 'Paimon',
                              'text': 'Wake up, sleepyheads! Paimon traded two pinecones with the Kuuhenki '
                                      'for the sweetest first-frost berries on Hiisi Island!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B03',
                              'speaker': 'Narrator',
                              'text': 'Columbina emerges barefoot from the arched gallery, rubbing one '
                                      'veiled temple lightly. Two of her magenta-tipped side curls have '
                                      'tangled around the silver clasp at her shoulder during her restless '
                                      'sleep.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B04',
                              'speaker': 'Columbina',
                              'text': 'Good morning, Aether... Paimon. Mm, forgive my hair -- the damp '
                                      'cavern breeze tied knots in my plaits while I dreamed, and my '
                                      'fingers feel oddly clumsy this morning.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N09_B05',
                              'speaker': 'Narrator',
                              'text': 'When the collar of her white capelet shifts in the morning light, I '
                                      "catch a glimpse of last night's chalk-white hairline mark resting "
                                      'silent beneath her left collarbone.',
                              'inner_thought': 'In daylight it looks like glazed bone -- motionless while '
                                               'she greets both of us at once.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B06',
                              'speaker': 'Aether',
                              'text': "Does your shoulder still ache from last night's chill, Columbina?",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B07',
                              'speaker': 'Columbina',
                              'text': 'No... it does not hurt, though the skin there feels cool, like '
                                      'winter porcelain. How strange -- in five centuries, even fierce '
                                      'battles never left frost on my pulse.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B08',
                              'speaker': 'Paimon',
                              'text': 'Sit down on the warm stone bench right now! Empty stomachs make '
                                      'strange chills ten times worse!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B09',
                              'speaker': 'Narrator',
                              'text': 'Obediently folding her ankles onto the sunlit bench, Columbina '
                                      'holds out a small silver comb with a shy tilt of her head.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B10',
                              'speaker': 'Columbina',
                              'text': "Sandrone's mechanical butler usually loses patience with knots and "
                                      'tugs... Would you mind helping me untangle this ribbon before the '
                                      'bread cools, Aether?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B11',
                              'speaker': 'Narrator',
                              'text': 'Up close, her dark locks smell faintly of cold spring water and '
                                      'crushed silver-lily petals.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B12',
                              'speaker': 'Columbina',
                              'text': 'Take your time... the morning sun on my neck feels remarkably '
                                      'gentle.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B13',
                              'speaker': 'Narrator',
                              'text': 'Holding the silver comb behind her shoulder, I weigh whether to '
                                      'focus on the everyday tenderness she craves or study the dormant '
                                      'seam along her collarbone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C05',
                              'prompt': 'Sunlight warms the courtyard bench as Columbina entrusts her '
                                        'tangled morning curls to your hands.',
                              'options': [{'opt_id': 'C05_A',
                                           'label': 'Patiently comb every knot from her dark-magenta locks '
                                                    'by hand and offer her the ripest frost-sweetened '
                                                    'berry.',
                                           'effects': {'bond': 2,
                                                       'insight': 1,
                                                       'add_flags': ['F05_BRUSHED_MORNING_PLAITS']},
                                           'next_node': 'N10',
                                           'reaction_beats': [{'beat_id': 'N09_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Parting each tangled lock '
                                                                       'carefully between my fingers so '
                                                                       'the comb never pulls, I retie her '
                                                                       'white ribbon neatly and hold a '
                                                                       'tart-sweet cloudberry to her lips.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N09_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Mm... sweet, with a little winter '
                                                                       'sun inside. So this is how '
                                                                       'ordinary mornings feel when '
                                                                       'someone stays for breakfast.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C05_B',
                                           'label': 'Smooth her hair gently while attuning your elemental '
                                                    'sight to read the dormant harmonic frequency of her '
                                                    'collarbone mark.',
                                           'effects': {'bond': 0, 'insight': 2},
                                           'next_node': 'N10',
                                           'reaction_beats': [{'beat_id': 'N09_R_B1',
                                                               'speaker': 'Narrator',
                                                               'text': 'As I draw the comb smoothly down '
                                                                       'her hair, I focus my elemental '
                                                                       'sight: the white seam carries the '
                                                                       'exact geometric resonance as the '
                                                                       'Seelie Court knots woven into her '
                                                                       'eye mask.',
                                                               'inner_thought': 'Whatever woke last night '
                                                                                'is part of her own '
                                                                                'angelic lineage -- not a '
                                                                                'curse cast from outside.',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N09_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Your fingertips paused right '
                                                                       'behind my shoulder, Aether. Did '
                                                                       'your outlander eyes catch a stray '
                                                                       'winter spirit hiding there?',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n09_morning_plaits.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N10': {'node_id': 'N10',
                   'chapter_id': 'CH2',
                   'title': 'Glass Arches Over Frozen Tide',
                   'day_label': 'Day 3 - Evening, 19:45',
                   'location': 'Hiisi High Bluff - Abandoned Frost-Glass Conservatory',
                   'bgm_bucket': 'vn_daily_sweet',
                   'flowchart_pos': [9, 2],
                   'beats': [{'beat_id': 'N10_B01',
                              'speaker': 'Narrator',
                              'text': 'As violet evening settles over Day Three, Columbina guides Paimon '
                                      'and me up a cliffside stair to an abandoned frost-glass '
                                      "conservatory overlooking Hiisi's frozen bay.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B02',
                              'speaker': 'Paimon',
                              'text': 'Ooh, look at those tall arched crystal panes! Even with snow piled '
                                      'along the ribs outside, the air inside smells like dried mint and '
                                      'winter camellias!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B03',
                              'speaker': 'Columbina',
                              'text': 'Sandrone repaired the cracked panes for me two autumns ago so our '
                                      'tea leaves would stop freezing. Whenever Silvermoon Hall feels too '
                                      'deep underground, I sit beneath this dome.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B04_F05',
                              'speaker': 'Narrator',
                              'text': 'As she turns beneath the lantern-lit glass ribs, the neat '
                                      'side-plait I combed for her this morning sways silkily past her '
                                      'cheek -- kept untouched all day.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F05_BRUSHED_MORNING_PLAITS']}},
                             {'beat_id': 'N10_B04_NOF05',
                              'speaker': 'Narrator',
                              'text': 'As she turns beneath the lantern-lit glass ribs, frost-light '
                                      'catches the geometric weave of her veil -- echoing the faint '
                                      'frequency I sensed at breakfast.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F05_BRUSHED_MORNING_PLAITS']}},
                             {'beat_id': 'N10_B05',
                              'speaker': 'Narrator',
                              'text': 'I kindle a small smokeless stove beneath a porcelain kettle while '
                                      'Paimon eagerly arranges honey biscuits on a silver tray.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B06',
                              'speaker': 'Aether',
                              'text': "Vesna's Druzhna border watch sent a flare from the birch ridge at "
                                      'dusk. Will she let visitors inspect the old Snowland Fae shrine '
                                      'tomorrow?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B07',
                              'speaker': 'Columbina',
                              'text': 'Vesna owes her fairy wings to the old Hyperborean court. If anyone '
                                      'in Nod-Krai keeps records older than the Frostmoon Scions, it is '
                                      'her border archive.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B08',
                              'speaker': 'Paimon',
                              'text': 'Yaaawn... warm tea steam plus snow tapping on glass is unfair... '
                                      'Paimon is just gonna rest her eyes on this velvet cushion for five '
                                      'minutes...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B09',
                              'speaker': 'Narrator',
                              'text': 'Within two minutes, Paimon is curled fast asleep beside the warm '
                                      'tea-caddy, leaving only the whisper of snow sliding down the arched '
                                      'glass dome.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B10',
                              'speaker': 'Columbina',
                              'text': 'Hehe... she falls asleep faster than the Kuuhenki.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N10_B11',
                              'speaker': 'Aether',
                              'text': 'Let her rest. I will pour a fresh cup for you before the kettle '
                                      'cools.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B12',
                              'speaker': 'Narrator',
                              'text': 'Across the small round table, fragrant white steam rises between us '
                                      'as midnight approaches.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N11'}],
                   'ending_id': None},
           'N11': {'node_id': 'N11',
                   'chapter_id': 'CH2',
                   'title': 'The Moonweave Ribbon Chime',
                   'day_label': 'Day 3 - Midnight, 23:45',
                   'location': 'Frost-Glass Conservatory - Center Tea Table',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [10, 2],
                   'beats': [{'beat_id': 'N11_B01',
                              'speaker': 'Narrator',
                              'text': 'At a quarter to midnight, the frost-moon hangs directly above the '
                                      "conservatory's central glass rib, bathing Columbina's porcelain "
                                      'hands and steaming teacup in silver-rose light.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B02',
                              'speaker': 'Columbina',
                              'text': 'Aether... may I confess a small malfunction in my singing tonight?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B03',
                              'speaker': 'Aether',
                              'text': 'Tell me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B04',
                              'speaker': 'Columbina',
                              'text': "Whenever I hum to steady the island's veins now, the melody refuses "
                                      'to spread evenly across the water. Every phrase bends -- like a '
                                      'compass needle drawn back toward your chair.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B05',
                              'speaker': 'Narrator',
                              'text': 'Setting down her cup, she reaches up behind her left ear and unties '
                                      'a slender ribbon spun of pale silver moon-silk, tipped with a tiny '
                                      'hollow Luonnotar bell.',
                              'inner_thought': 'Even without wind, the miniature silver chime rings in '
                                               'exact unison with the pulse at her wrist.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B06',
                              'speaker': 'Columbina',
                              'text': 'I wove this Moonweave Ribbon Chime from the first thread of '
                                      'Kuuvahki that cradled me at birth. Its little bell does not ring '
                                      'for wind -- it rings only to the rhythm of my own soul.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B07',
                              'speaker': 'Narrator',
                              'text': 'Across the narrow tea table, she extends both hands, offering the '
                                      'shimmering silver ribbon and bell above my open palm.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B08',
                              'speaker': 'Columbina',
                              'text': "If we travel beyond Hiisi's waters -- or if the eclipse mist ever "
                                      'grows too loud for my veiled sight -- a chime tied to your wrist '
                                      'would let my song find you without faltering.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N11_B09',
                              'speaker': 'Aether',
                              'text': 'Columbina... if this ribbon carries your birth-thread of Kuuvahki, '
                                      'parting with it leaves half your own anchor in my keeping.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B10',
                              'speaker': 'Columbina',
                              'text': 'Perhaps I am tired of keeping every thread tucked safely inside '
                                      'myself.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B11',
                              'speaker': 'Narrator',
                              'text': 'Beneath the X-lattice veil, a faint rose flush warms her cheeks, '
                                      'though a tiny shiver passes down her wrists as the bell chiming '
                                      'between us brightens.',
                              'inner_thought': 'Accepting it binds my pulse directly to hers; returning it '
                                               'spares her from giving away her birth-charm.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B12',
                              'speaker': 'Columbina',
                              'text': "Still... if carrying a Moon Maiden's tether feels too heavy for a "
                                      'wandering star, you may fold it back into my hair, and I will not '
                                      'mind.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B13',
                              'speaker': 'Narrator',
                              'text': 'Moonlight pools across the silver Luonnotar bell suspended between '
                                      'our fingertips.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B14',
                              'speaker': 'Columbina',
                              'text': 'Tell me truly, Aether -- where shall this chime rest tonight?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B15',
                              'speaker': 'Narrator',
                              'text': 'Outside the frost-glass dome, the midnight tide murmurs against the '
                                      'cliff below as I make my choice.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C06',
                              'prompt': 'Columbina holds out her Moonweave Ribbon Chime across the '
                                        'midnight tea table.',
                              'options': [{'opt_id': 'C06_A',
                                           'label': 'Accept the Moonweave Ribbon Chime and let Columbina '
                                                    'tie it fast around your wrist so her song can always '
                                                    'find your heartbeat.',
                                           'effects': {'bond': 2,
                                                       'insight': 1,
                                                       'add_flags': ['F07_MOONWEAVE_RIBBON_CHIME']},
                                           'next_node': 'N12',
                                           'reaction_beats': [{'beat_id': 'N11_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Turning my wrist upward across the '
                                                                       'table, I let Columbina loop the '
                                                                       'cool moon-silk twice around my '
                                                                       'pulse and knot it fast; the tiny '
                                                                       'silver bell chimes one clear, '
                                                                       'resonant C-sharp.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N11_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': '...It settled into your golden '
                                                                       'pulse without a single tremor. '
                                                                       'Keep it safe for me, Aether -- now '
                                                                       'even in a blizzard, I will know '
                                                                       'the exact shape of your step.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C06_B',
                                           'label': 'Gently braid the Moonweave Ribbon Chime back into her '
                                                    'hair so she keeps its protection, and warm her hands '
                                                    'in yours instead.',
                                           'effects': {'bond': 2, 'insight': 0},
                                           'next_node': 'N12',
                                           'reaction_beats': [{'beat_id': 'N11_R_B1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Cradling the ribbon carefully, I '
                                                                       'tie it back behind her left ear so '
                                                                       'her birth-anchor stays whole, then '
                                                                       'fold both of my warm palms around '
                                                                       'her chilled hands.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N11_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Always guarding me from spending '
                                                                       'too much of myself... very well, I '
                                                                       'shall wear it in my hair a little '
                                                                       'longer while your hands stay near.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n11_conservatory_diff.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N12': {'node_id': 'N12',
                   'chapter_id': 'CH2',
                   'title': 'Vesna of the Frost-Birch Watch',
                   'day_label': 'Day 4 - Afternoon, 14:00',
                   'location': 'Northern Hiisi Ridge - Frost-Birch Border Outpost',
                   'bgm_bucket': 'vn_daily_sweet',
                   'flowchart_pos': [11, 2],
                   'beats': [{'beat_id': 'N12_B01',
                              'speaker': 'Narrator',
                              'text': 'Early on the fourth afternoon, pale sunlight slants through white '
                                      'birch trunks as Columbina, Paimon, and I reach the Druzhna border '
                                      'watchpost guarding the northern strait.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B02',
                              'speaker': 'Narrator',
                              'text': 'Waiting beside a rune-etched resonance pylon is Commander Vesna '
                                      'Strivozha -- four translucent, rose-gold-framed fairy wings '
                                      'shimmering behind her teal-and-white fur mantle.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B03',
                              'speaker': 'Vesna',
                              'text': 'Peace of the Pale Star upon you, Traveler -- and upon you, Moon '
                                      'Maiden. My Vila wings began humming ten minutes before your feet '
                                      'touched the birch trail.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B04_F07',
                              'speaker': 'Vesna',
                              'text': "Oh? That Moonweave pulse-chime tied around Aether's wrist... "
                                      'Merciful Koitar, you have already bound a birth-thread to a single '
                                      'bearer, Lady Columbina?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N12_B04_NOF07',
                              'speaker': 'Vesna',
                              'text': 'Wait -- listen to the Moonweave chime braided behind your ear, Lady '
                                      "Columbina! Its silver pitch is leaning wholly toward the Traveler's "
                                      'heartbeat!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N12_B05',
                              'speaker': 'Paimon',
                              'text': 'Whoa, Vesna, why did your face go pale all of a sudden?! Is a '
                                      'ringing bell bad luck for Snowland Fae?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B06',
                              'speaker': 'Columbina',
                              'text': 'Two nights ago, a seam of cold porcelain woke beneath my collarbone '
                                      "when I leaned on Aether's shoulder, Commander Vesna. Even the "
                                      'Frostmoon elders left no scroll explaining it.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B07',
                              'speaker': 'Narrator',
                              'text': 'Vesna lowers her butterfly-tipped crystal wand, her aqua-teal eyes '
                                      'widening as she traces the six white dove wings crowning '
                                      "Columbina's hair and the X-lattice seal over her eyes.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B08',
                              'speaker': 'Vesna',
                              'text': 'Of course the Frostmoon Scions left no record -- they worshipped '
                                      'you only as a newborn Moon Goddess and never recognized the older '
                                      'choir singing inside your soul-seed!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B09',
                              'speaker': 'Aether',
                              'text': 'An older choir? You mean the Seelie -- the Angels of Hyperborea?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B10',
                              'speaker': 'Vesna',
                              'text': 'My Vila ancestors served the First Angel Koitar before the heavens '
                                      'nailed Hyperborea into frost. Come -- our subterranean vault lies '
                                      'directly beneath these birches. You must read the stone before '
                                      'dusk!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B11',
                              'speaker': 'Columbina',
                              'text': 'Lead the way, child of the Snowland Fae. Five hundred years is '
                                      'quite long enough to fear a shadow without knowing its name.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': 'outing_cruise'},
                             {'beat_id': 'N12_B12',
                              'speaker': 'Narrator',
                              'text': 'Touching her wand to a frost-sealed root cellar beneath the ancient '
                                      'white birch, Vesna parts the rime to reveal steps descending into '
                                      'pre-Archon stone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n12_vesna_birch.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N13'}],
                   'ending_id': None},
           'N13': {'node_id': 'N13',
                   'chapter_id': 'CH2',
                   'title': "Mural of the First Angel's Fall",
                   'day_label': 'Day 4 - Dusk, 17:30',
                   'location': 'Beneath Frost-Birch Ridge - Hyperborean Fae Vault',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [12, 2],
                   'beats': [{'beat_id': 'N13_B01',
                              'speaker': 'Narrator',
                              'text': 'Thirty paces underground, Vesna raises a cryo-phosphor lamp against '
                                      'a towering bas-relief of silver-inlaid obsidian older than any '
                                      'statue of the Seven.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B02',
                              'speaker': 'Narrator',
                              'text': 'Carved across the frieze is a six-winged Angel in a broken crown '
                                      'gazing into the eyes of a youth from beyond the stars -- while '
                                      'behind them, rows of winged choir-sisters crumble into hollow, '
                                      'faceless Seelie wisps.',
                              'inner_thought': "The X-shaped seal carved above the Angel's brow is "
                                               "identical stroke-for-stroke to Columbina's eye mask.",
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B03',
                              'speaker': 'Paimon',
                              'text': 'Look at the crown and the six wings on that mural... and the '
                                      "X-pattern! It matches Columbina's veil!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B04',
                              'speaker': 'Vesna',
                              'text': "Listen to the Hyperborean inscription beneath Koitar's feet: "
                                      "'Created to love all things equally, an Angel carries heaven's "
                                      "shackle woven straight into the core of her soul.'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B05',
                              'speaker': 'Vesna',
                              'text': "'If ever she dares gaze upon one person alone and yield to one "
                                      'individual the devotion meant for all creation, her divine form '
                                      'shall calcify into dust, and her mind shall hollow into a mute '
                                      "Seelie.'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B06',
                              'speaker': 'Narrator',
                              'text': "Beside me, Columbina's breath catches completely. Her hand rises to "
                                      'the white X-lattice over her eyes as five centuries of nameless '
                                      'instinct snap into terrifying clarity.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B07',
                              'speaker': 'Columbina',
                              'text': "...'Sleep, sleep now, my dear little dove, keep both eyes shut "
                                      "against the sky.' That lullaby I heard before my birth... it was a "
                                      "surviving Angel's warning woven into my Kuuvahki seed.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B08',
                              'speaker': 'Aether',
                              'text': 'Wait, Vesna -- why did the curse still destroy Koitar if the '
                                      'Voyager she loved came from outside Teyvat?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B09',
                              'speaker': 'Vesna',
                              'text': 'Look at the second tablet! The shackle does not consult Irminsul '
                                      "before firing -- it detonates autonomously inside the Angel's own "
                                      'soul the instant her resonance phase-locks onto one beloved!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B10',
                              'speaker': 'Vesna',
                              'text': 'When the Voyager met Koitar, she wore a borrowed mortal body born '
                                      "inside Teyvat's Ley Lines -- a closed circuit! With nowhere outside "
                                      'the world to vent the execution surge, it rebounded and burned both '
                                      'their memories to ash!',
                              'inner_thought': 'A borrowed native body trapped the surge inside '
                                               'Irminsul... whereas I walk Teyvat in my original Descender '
                                               'vessel!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B11',
                              'speaker': 'Vesna',
                              'text': 'That is why kindness toward Sandrone or your Kuuhenki never woke '
                                      'the seal, Lady Columbina -- fellowship is shared, whereas your '
                                      'heart has begun singing for one soul alone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B12',
                              'speaker': 'Columbina',
                              'text': 'So every warm beat my chest learns beside you... turns another '
                                      'thread of my mind into white stone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B13',
                              'speaker': 'Narrator',
                              'text': "Under the flickering blue lamp, Columbina's fingertips tremble "
                                      'almost imperceptibly against her sleeve.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B14',
                              'speaker': 'Vesna',
                              'text': 'There is half a schematic of an extra-cosmic grounding duet etched '
                                      'at the bottom edge, Traveler -- decide quickly before the damp '
                                      'frost obscures the runes!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C07',
                              'prompt': "Before Koitar's ancient mural, Columbina stands shaken by the "
                                        'truth of her Angelic bloodline.',
                              'options': [{'opt_id': 'C07_A',
                                           'label': "Transcribe every rune of Vesna's Seelie Codex -- "
                                                    'mapping how an original Descender body can vent an '
                                                    'autonomous soul-curse outside Irminsul.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F06_VESNA_SEELIE_CODEX']},
                                           'next_node': 'N14',
                                           'reaction_beats': [{'beat_id': 'N13_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Working shoulder-to-shoulder with '
                                                                       'Vesna, I copy every glyph of '
                                                                       "Koitar's grounding theorem: a "
                                                                       'physical pulse-bridge bound to an '
                                                                       'original Descender core can siphon '
                                                                       'the backlash straight past the '
                                                                       'False Sky.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N13_R_A2',
                                                               'speaker': 'Vesna',
                                                               'text': 'You have the entire circuit '
                                                                       'recorded, Aether! Guard those '
                                                                       'notes with your life!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C07_B',
                                           'label': "Clasp Columbina's trembling icy hands before the "
                                                    "mural and swear she will never share Koitar's hollow "
                                                    'fate.',
                                           'effects': {'bond': 2, 'insight': 1},
                                           'next_node': 'N14',
                                           'reaction_beats': [{'beat_id': 'N13_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Listen to me, Columbina -- I am '
                                                                       'not walking in a borrowed Teyvat '
                                                                       'shell like the Voyager did. Hold '
                                                                       'onto me, and I swear no law on '
                                                                       'that wall will turn you into a '
                                                                       'hollow wisp.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N13_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': '...Foolish star. Even after '
                                                                       "reading heaven's sentence aloud, "
                                                                       'you grip my hand tighter instead '
                                                                       'of letting go.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n13_koitar_mural.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N14': {'node_id': 'N14',
                   'chapter_id': 'CH2',
                   'title': 'Porcelain Beneath the Collarbone',
                   'day_label': 'Day 4 - Night, 21:00',
                   'location': 'Silvermoon Hall - Outer Snow-Dusted Archway',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'flowchart_pos': [13, 2],
                   'beats': [{'beat_id': 'N14_B01',
                              'speaker': 'Narrator',
                              'text': 'Dry night snow swirls across the carved stone archway of Silvermoon '
                                      'Hall as we return from the birch ridge at nine.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B02_F06',
                              'speaker': 'Aether',
                              'text': "According to Vesna's codex transcription, keeping your pulse steady "
                                      "until we assemble a full harmonic drain should slow the seal's "
                                      'progression.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F06_VESNA_SEELIE_CODEX']}},
                             {'beat_id': 'N14_B02_NOF06',
                              'speaker': 'Aether',
                              'text': "Vesna promised to send her Vila scouts down to check the island's "
                                      'outer resonance pylons first thing tomorrow.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F06_VESNA_SEELIE_CODEX']}},
                             {'beat_id': 'N14_B03',
                              'speaker': 'Narrator',
                              'text': 'Two steps beneath the stone arch, Columbina abruptly stops walking. '
                                      'One slender hand presses against the frosted pillar as her knees '
                                      'sway.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B04',
                              'speaker': 'Columbina',
                              'text': 'Ah... wait a moment. Getting dizzy...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B05',
                              'speaker': 'Narrator',
                              'text': 'With a tiny chime like snapping icicles, a single white feather '
                                      'detaches from the lowest wing-ornament in her hair -- hardening '
                                      'mid-fall into brittle translucent crystal before shattering across '
                                      'the snow!',
                              'inner_thought': 'My chest tightens -- the calcification is already climbing '
                                               'from her collarbone toward her crown.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B06',
                              'speaker': 'Paimon',
                              'text': 'Columbina!! Aether, catch her elbow -- a feather from her hair just '
                                      'turned to glass and broke!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B07',
                              'speaker': 'Narrator',
                              'text': 'Steadying her shoulders through her white capelet, I feel a tremor '
                                      'run down her frame as she turns her veiled face uncertainly toward '
                                      "Paimon's voice.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B08',
                              'speaker': 'Columbina',
                              'text': 'I am still standing, little finch... Only -- remind me for a '
                                      'second. Yesterday noon on the shoal, did Aether tell me your scarf '
                                      'was winter-white... or midnight-blue?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B09',
                              'speaker': 'Paimon',
                              'text': "W-What?! You asked Aether about Paimon's starry navy scarf three "
                                      'times while we ate berries yesterday!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B10',
                              'speaker': 'Columbina',
                              'text': '...Starry navy. Yes -- forgive me, it came back just now. For three '
                                      'heartbeats, that corner of yesterday looked like blank snow.',
                              'inner_thought': 'Three seconds of erased memory today... how much will '
                                               'vanish when the eclipse tide peaks?',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B11',
                              'speaker': 'Aether',
                              'text': 'Lean on my arm and do not hum tonight. Tomorrow evening Sandrone '
                                      'arrives at the conservatory -- if anyone can measure the exact rate '
                                      'of that backlash, it is her.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B12',
                              'speaker': 'Narrator',
                              'text': 'Beneath the silent snowfall of the stone archway, Columbina nods '
                                      'wordlessly, letting me guide her inside to the warm hearth.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N15'}],
                   'ending_id': None},
           'N15': {'node_id': 'N15',
                   'chapter_id': 'CH2',
                   'title': "Sandrone's Portable Tea Table",
                   'day_label': 'Day 5 - Evening, 20:00',
                   'location': "Frost-Glass Conservatory - Marionette's Salon",
                   'bgm_bucket': 'vn_daily_sweet',
                   'flowchart_pos': [14, 2],
                   'beats': [{'beat_id': 'N15_B01',
                              'speaker': 'Narrator',
                              'text': 'Promptly at eight on the fifth evening, heavy brass footsteps clank '
                                      'outside the frost-glass conservatory as the towering automaton '
                                      'Pulonia sets down a lace-draped tea table.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B02',
                              'speaker': 'Sandrone',
                              'text': 'Honestly, Columbina! Must you always nest on a damp rock in the '
                                      'middle of frozen nowhere? Pulonia nearly frosted an ankle-gear '
                                      'hauling fresh Fontinalia mille-feuille up your cliff!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B03',
                              'speaker': 'Narrator',
                              'text': 'Dressed in her immaculate ruffled gown with the golden clockwork '
                                      'wind-up key turning smoothly at her back, Seventh Harbinger '
                                      'Sandrone huffs -- yet carefully places the warmest berry tart '
                                      'directly in front of Columbina.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B04',
                              'speaker': 'Columbina',
                              'text': 'Welcome back, Sandrone. You brought three spoons of wild-berry '
                                      'preserve just as I like... and heavy hydro-pneumatic oil on '
                                      "Pulonia's gauntlets.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N15_B05',
                              'speaker': 'Sandrone',
                              'text': 'Hmph! Do not think I spent all afternoon bolted into coastal '
                                      'bedrock out of sentimentality! With the perigee eclipse seven '
                                      "nights away, leaving an entire town's safety tied to one girl's "
                                      'vocal cords was atrocious engineering!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B06',
                              'speaker': 'Aether',
                              'text': "Wait -- you built a mechanical bypass for Hiisi Island's "
                                      'subterranean Kuuvahki tide?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B07',
                              'speaker': 'Sandrone',
                              'text': 'Six Pulonia-class hydro-pneumatic tide-relief valves, phase-linked '
                                      "directly to Commander Vesna's Vila pylons along the shoal! Even if "
                                      'Columbina stops singing tomorrow -- or leaves Nod-Krai altogether '
                                      '-- Nasha Town and the Frostmoon Enclave will not suffer a single '
                                      'flooded cellar!',
                              'inner_thought': "Sandrone just took the entire island's hostage-weight off "
                                               "Columbina's throat!",
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B08',
                              'speaker': 'Paimon',
                              'text': 'Whoa!! For somebody who complains nonstop, Sandrone actually saved '
                                      'the whole town behind the scenes!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B09',
                              'speaker': 'Sandrone',
                              'text': 'Quiet, floating nuisance, and eat your pastry! Now hold still, '
                                      "Columbina -- let Pulonia's optic lens scan why your vocal pitch "
                                      'dropped four hertz just now.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B10',
                              'speaker': 'Narrator',
                              'text': "Pulonia's monocle projects a pale-gold harmonic grid across "
                                      "Columbina's collarbone. Instantly, the wind-up key behind "
                                      "Sandrone's waist screeches and spins twice as fast -- her porcelain "
                                      'expression dropping into cold dread!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B11',
                              'speaker': 'Sandrone',
                              'text': '...What is this crystalline impedance curve?! Columbina -- your '
                                      'soul-lattice is calcifying from the inside out!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B12',
                              'speaker': 'Narrator',
                              'text': 'Glowing brass-blue differential equations erupt in midair above the '
                                      'teacups as Sandrone slams both palms onto the tablecloth, eyes '
                                      'darting between Columbina and me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B13',
                              'speaker': 'Sandrone',
                              'text': 'Pulonia, seal the conservatory doors at once! Nobody leaves this '
                                      'table until I run the full World-Formula projection!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N16'}],
                   'ending_id': None},
           'N16': {'node_id': 'N16',
                   'chapter_id': 'CH2',
                   'title': 'Differential Analysis of a Dying Song',
                   'day_label': 'Day 5 - Late Night, 22:30',
                   'location': 'Frost-Glass Conservatory - World-Formula Projection',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [15, 2],
                   'beats': [{'beat_id': 'N16_B01',
                              'speaker': 'Narrator',
                              'text': "Two hours later, untouched tea has gone stone-cold while Sandrone's "
                                      'brass astrolabe projects a razor-steep exponential curve above the '
                                      'lace cloth.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B02',
                              'speaker': 'Sandrone',
                              'text': "Look at the asymptote! My tide-valves protect Nasha Town's bedrock, "
                                      "yes -- but decoupling the island's outer loop also removes the "
                                      "external shock-absorber that was slowing Columbina's internal "
                                      'backlash!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B03',
                              'speaker': 'Aether',
                              'text': 'Where does that vertical spike intersect the timeline?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B04',
                              'speaker': 'Sandrone',
                              'text': 'Zero-zero-hundred hours opening Day Twelve -- the exact midnight '
                                      'apex of the Frostmoon Perigee Syzygy! At that minute, gravitational '
                                      'resonance forces her Angelic soul-seal past critical threshold!',
                              'inner_thought': 'Midnight opening Day Twelve... fewer than seven days '
                                               'before her mind hollows completely.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B05',
                              'speaker': 'Columbina',
                              'text': 'How neat and tidy your numbers are, Sandrone... like sheet music '
                                      'marking the final bar.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B06',
                              'speaker': 'Sandrone',
                              'text': 'Do NOT smile at me like that, you infuriating girl! Who gave you '
                                      'permission to fall in love with one person and trigger a '
                                      'prehistoric Hyperborean execution seal without consulting me?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B07',
                              'speaker': 'Narrator',
                              'text': "Sandrone's voice cracks for a fraction of a second before she "
                                      'angrily adjusts her cuff, tapping two glowing variables on the '
                                      'floating World-Formula chart.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B08',
                              'speaker': 'Sandrone',
                              'text': 'Listen carefully, Fourth Descender! No power registered inside '
                                      'Irminsul -- not Pulonia, not The Knave, not even Her Majesty the '
                                      'Tsaritsa -- can permanently annihilate that surge. At best, '
                                      'Snezhnayan Cryo stasis could freeze her through winter.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B09',
                              'speaker': 'Sandrone',
                              'text': 'To shatter the seal permanently at midnight on Day Twelve, your '
                                      'outlander body must act as an active phase-inverted grounding sink '
                                      '-- matching a `13.7` kilohertz counter-harmonic across a physical '
                                      'Kuuvahki bridge!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B10',
                              'speaker': 'Paimon',
                              'text': 'Thirteen-point-seven kilo-whatsit?! Aether, tell Paimon you are '
                                      'writing those glowing numbers down!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B11',
                              'speaker': 'Sandrone',
                              'text': 'I am sending Pulonia down to check the Derelict Deep Gallery shaft '
                                      'tomorrow, and I have already wired Zapolyarny to suspend the '
                                      'Palestar Edict. What you do with this math tonight is up to you!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B12',
                              'speaker': 'Columbina',
                              'text': 'Thank you, Sandrone... truly. Even when you scold me, your tea '
                                      'table is always warm.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B13',
                              'speaker': 'Sandrone',
                              'text': "Hmph! Save your gratitude until you show up to next month's tea "
                                      'party with all your memories intact!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B14',
                              'speaker': 'Narrator',
                              'text': 'Before Pulonia folds the brass projector away, the shimmering '
                                      'World-Formula constants hover one last moment before my eyes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C08',
                              'prompt': "Sandrone's World-Formula decay projection hovers above the table "
                                        'before Pulonia packs the astrolabe.',
                              'options': [{'opt_id': 'C08_A',
                                           'label': 'Commit every differential constant and the 13.7 kHz '
                                                    "phase-inversion curve of Sandrone's World-Formula to "
                                                    'memory.',
                                           'effects': {'bond': 1,
                                                       'insight': 2,
                                                       'add_flags': ['F08_SANDRONE_TEA_FORMULA']},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_R_A1',
                                                               'speaker': 'Aether',
                                                               'text': 'Phase-inverted counter-harmonic at '
                                                                       '13.7 kilohertz, timed to the '
                                                                       'twelve-minute syzygy window at '
                                                                       '00:00 on Day Twelve. I have every '
                                                                       'constant locked in memory, '
                                                                       'Sandrone.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_R_A2',
                                                               'speaker': 'Sandrone',
                                                               'text': 'Hmph... at least your brain is '
                                                                       "less decorative than Childe's. Use "
                                                                       'those numbers properly, Outlander.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C08_B',
                                           'label': 'Thank Sandrone sincerely for shielding Hiisi Island '
                                                    'and swear to bring Columbina back whole to their next '
                                                    'tea party.',
                                           'effects': {'bond': 2, 'insight': 0},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Thank you for building those '
                                                                       'tide-valves and standing by her, '
                                                                       'Sandrone. Keep two chairs open '
                                                                       'next month -- I will make sure she '
                                                                       'remembers every tart on the tray.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_R_B2',
                                                               'speaker': 'Sandrone',
                                                               'text': 'W-Well, see that you do! Good '
                                                                       'grief, Pulonia, pick up the kettle '
                                                                       'before these two make me drop a '
                                                                       'gear!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n15_sandrone_tea_diff.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N17': {'node_id': 'N17',
                   'chapter_id': 'CH2',
                   'title': 'Vigil at the Silvermoon Archway',
                   'day_label': 'Day 5 - Midnight Snow, 23:55',
                   'location': 'Silvermoon Hall - Snowy Stone Archway',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [16, 2],
                   'pre_events': [{'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                            'min_bond': 12,
                                            'min_insight': 8},
                                   'effects': {'add_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                             'F07_SECOND_CHANCE_N17']}}],
                   'beats': [{'beat_id': 'N17_B01',
                              'speaker': 'Narrator',
                              'text': 'Five minutes before midnight on Day Five, thick snow falls straight '
                                      'and windless past the stone archway of Silvermoon Hall while Paimon '
                                      'hurries ahead to stoke the hearth.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B02',
                              'speaker': 'Narrator',
                              'text': 'Columbina pauses beneath the carved lintel, listening to the '
                                      "distant, rhythmic thrum of Sandrone's new coastal relief valves "
                                      'echoing faintly through the cliff.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B03_F08',
                              'speaker': 'Columbina',
                              'text': "You memorized every cruel decimal of Sandrone's decay curve "
                                      'tonight, Aether... six nights and a handful of hours look terribly '
                                      'small when drawn in brass light.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F08_SANDRONE_TEA_FORMULA']}},
                             {'beat_id': 'N17_B03_NOF08',
                              'speaker': 'Columbina',
                              'text': 'Hearing Sandrone scold me until her voice shook... I never knew how '
                                      "fiercely a friend could resent heaven's arithmetic on my behalf.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F08_SANDRONE_TEA_FORMULA']}},
                             {'beat_id': 'N17_B04',
                              'speaker': 'Aether',
                              'text': 'Nasha Town and the Enclave are safe behind her valves now. That '
                                      'means for the next six nights, my only duty on this island is you.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B05_HAS_EARLY',
                              'speaker': 'Columbina',
                              'text': 'Hold still a moment in the snow, Aether... let me listen to the '
                                      'chime you have carried since Night Three.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B06_HAS_EARLY',
                              'speaker': 'Narrator',
                              'text': 'Stepping close beneath the snowy arch, Columbina brushes her cool '
                                      'fingertips over the Moonweave Ribbon Chime at my wrist, tightening '
                                      'its silver silk knot against my pulse.',
                              'inner_thought': 'Even through rising frost, the little Luonnotar bell '
                                               'answers my heartbeat without a single waver.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B07_HAS_EARLY',
                              'speaker': 'Columbina',
                              'text': 'Sandrone called for a physical Kuuvahki bridge... How fortunate '
                                      'that you accepted my selfish little ribbon before either of us knew '
                                      'its price.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': 'vn_tender_love',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B05_SECOND_CHANCE',
                              'speaker': 'Columbina',
                              'text': 'Wait beneath the arch, Aether -- do not step inside yet. Two '
                                      'midnights ago you braided my Moonweave Ribbon Chime back into my '
                                      "hair to keep me safe... tonight, I refuse to take 'no' for an "
                                      'answer.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B06_SECOND_CHANCE',
                              'speaker': 'Narrator',
                              'text': 'Reaching behind her ear in the falling snow, Columbina unties the '
                                      'luminous Moonweave Ribbon and silver Luonnotar bell, drawing my '
                                      'hand gently toward her chest to knot it fast around my wrist!',
                              'inner_thought': 'Everything we shared and uncovered over five days just '
                                               'earned back the physical bridge we need!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B07_SECOND_CHANCE',
                              'speaker': 'Columbina',
                              'text': "Both Vesna's mural and Sandrone's math demand a physical Kuuvahki "
                                      'conduit... Wear my birth-chime now, my stubborn star, so you can '
                                      'haul me back if the snow grows white.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': 'vn_tender_love',
                              'when': {'requires_all': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B05_NO_F07',
                              'speaker': 'Columbina',
                              'text': 'Sandrone spoke of needing a physical Kuuvahki bridge... yet when I '
                                      'reach toward the chime braided behind my ear tonight, my fingers '
                                      'tremble too coldly to untie the knot.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N17_B06_NO_F07',
                              'speaker': 'Narrator',
                              'text': 'In the quiet snowfall beneath the arch, the silver Luonnotar bell '
                                      "remains braided in Columbina's dark-magenta hair, ringing a faint, "
                                      'solitary note as she folds her hands inside her sleeves.',
                              'inner_thought': 'Without enough shared understanding yet, she is still '
                                               'afraid to burden my wrist with her soul-thread.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N17_B07_NO_F07',
                              'speaker': 'Columbina',
                              'text': 'Perhaps keeping this ribbon on my own temple is safer for you after '
                                      'all, Traveler... even if the road ahead grows narrower.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N17_B08',
                              'speaker': 'Narrator',
                              'text': 'Far down the northern cliff-face, a faint crimson ember flickers '
                                      'once against the snow -- not Pyro from a torch, nor blue Kuuvahki, '
                                      'but the baleful scarlet of an older moon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B09',
                              'speaker': 'Aether',
                              'text': 'Did you sense that ash-scent on the wind just now?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B10',
                              'speaker': 'Columbina',
                              'text': "Mm... crimson cinders that never freeze. So 'Father' has come north "
                                      'from Fontaine to inspect the Deep Gallery shaft herself.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B11',
                              'speaker': 'Aether',
                              'text': 'Arlecchino? If the Fourth Harbinger is here on Hiisi Island, '
                                      'tomorrow twilight will bring more than tea.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B12',
                              'speaker': 'Columbina',
                              'text': 'Do not fear Peruere, Aether. Her fire burns away falsehoods -- and '
                                      'tomorrow, she will ask us both which truth we intend to keep.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B13',
                              'speaker': 'Narrator',
                              'text': 'Side by side beneath the snow-laden archway, we step inside '
                                      'Silvermoon Hall as Chapter Two closes six days before the eclipse.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N18'}],
                   'ending_id': None},
           'N18': {'node_id': 'N18',
                   'chapter_id': 'CH3',
                   'title': 'Crimson Moon at the Threshold',
                   'day_label': 'Day 6 - Twilight, 18:00',
                   'location': 'Hiisi Northern Gorge - Derelict Deep Gallery Entrance',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [17, 2],
                   'beats': [{'beat_id': 'N18_B01',
                              'speaker': 'Narrator',
                              'text': 'At twilight on Day Six, high barometric pressure from the unsealed '
                                      'Deep Gallery shaft presses heavily across Silvermoon Hall, making '
                                      'poor Paimon sway dizzily beside the hearth.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B02',
                              'speaker': 'Aether',
                              'text': 'Stay inside the warm alcove with Luonnotar and watch over the young '
                                      'Kuuhenki until we get back, Paimon. The raw ley-pressure outside '
                                      'that shaft is too dense for you.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B03',
                              'speaker': 'Narrator',
                              'text': "Leaving Paimon tucked safely beside Luonnotar's warm brazier, "
                                      'Columbina and I ascend the snowy gorge to the cracked Hyperborean '
                                      'archway of the Derelict Deep Gallery.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B04',
                              'speaker': 'Narrator',
                              'text': 'Every Moonfall Silver blossom lining the threshold has flushed a '
                                      'startling, arterial crimson -- and standing between Sandrone and '
                                      'the sunken gate is Fourth Harbinger Arlecchino.',
                              'inner_thought': "Red X-pupils calm as banked embers -- 'The Knave' measures "
                                               'both of us in a single glance.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B05',
                              'speaker': 'Arlecchino',
                              'text': "Good evening, Aether. And Columbina... Sandrone's dispatch did not "
                                      'exaggerate. Even from ten paces, the frost-seam climbing your '
                                      'collarbone smells of old celestia-wrought bone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B06',
                              'speaker': 'Columbina',
                              'text': 'Even the blue lilies blushed red to welcome you, Peruere. Have you '
                                      'come to plant your Crimson Moon stakes along the outer gorge?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B07',
                              'speaker': 'Arlecchino',
                              'text': "Already driven into the ridge to reinforce Sandrone's valves and "
                                      "Tartaglia's perimeter. Hiisi's townsfolk will sleep undisturbed "
                                      'through the eclipse.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B08',
                              'speaker': 'Narrator',
                              'text': 'Resting one black-clawed gauntlet over the pommel of her '
                                      'scythe-cane, Arlecchino steps forward until crimson cinder-light '
                                      "reflects across Columbina's white X-veil.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B09',
                              'speaker': 'Arlecchino',
                              'text': 'Which leaves only the lethal contradiction standing before me. My '
                                      "bloodline descends from the Crimson Moon's shadow; I know what "
                                      'happens when an ancient lunar vessel fractures halfway.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B10',
                              'speaker': 'Sandrone',
                              'text': 'Pulonia just cleared the upper ice-plug of the Deep Gallery vault '
                                      'below us. Pre-Archon angelic counterpoint tablets AND ancient '
                                      'moon-marrow dampeners are still intact down there -- alongside our '
                                      'armored Bore-Rail shaft to Zapolyarny.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B11',
                              'speaker': 'Aether',
                              'text': 'If Columbina descends into that sub-zero Hyperborean shaft in her '
                                      'current state, the raw ley-draft will accelerate the crack at her '
                                      'throat.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B12',
                              'speaker': 'Arlecchino',
                              'text': 'Precisely why half-measures will kill her before Day Twelve, '
                                      'Aether. Night is falling fast over the gorge.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N18_B13',
                              'speaker': 'Narrator',
                              'text': 'Cold wind whips scarlet petals between the four of us as the '
                                      "porcelain seam below Columbina's throat pulses with a sharp white "
                                      'glint.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N19'}],
                   'ending_id': None},
           'N19': {'node_id': 'N19',
                   'chapter_id': 'CH3',
                   'title': 'Three Mirrors in the Snow',
                   'day_label': 'Day 6 - Night, 20:00',
                   'location': 'Deep Gallery Threshold - Three-Way Crossroads',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [18, 2],
                   'beats': [{'beat_id': 'N19_B01',
                              'speaker': 'Narrator',
                              'text': 'By eight at night, darkness locks the gorge in iron blue while '
                                      'crimson blossoms smolder around our boots like fallen stars.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B02',
                              'speaker': 'Arlecchino',
                              'text': 'Six nights remain until the syzygy, Outlander. Stand before the '
                                      'fire without flinching and choose which road you will stake her '
                                      'survival upon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B03',
                              'speaker': 'Arlecchino',
                              'text': 'First: refuse to leave her side. Shelter with her inside Silvermoon '
                                      "Hall's warm cavern and tune your Descender pulse directly to her "
                                      'breath -- betting that intimacy can outpace decay.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B04',
                              'speaker': 'Sandrone',
                              'text': "Second: station Pulonia at the cavern gate to guard Columbina's "
                                      'rest while you descend into the Deep Gallery vault with Peruere and '
                                      "me -- recovering Koitar's counterpoint or calibrating a Crimson "
                                      'Moon dampener before riding the Bore-Rail to my Zapolyarny '
                                      'astrolabe!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B05',
                              'speaker': 'Arlecchino',
                              'text': 'Or third... if seeing that porcelain death-seam climb toward her '
                                      'jaw makes your mortal nerve recoil, speak plainly now and command '
                                      'Number Three to seal her emotions under Harbinger frost before both '
                                      'of you break.',
                              'inner_thought': 'Three diverging roads -- heart-to-heart attunement, deep '
                                               'Hyperborean scholarship, or cold Harbinger distance.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B06',
                              'speaker': 'Narrator',
                              'text': 'Columbina stands quiet in the snow between us. Slowly, she lifts '
                                      'her bare right hand a few inches toward mine -- waiting to feel '
                                      'whether my fingers close around hers, step toward the vault, or '
                                      'draw back.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B07',
                              'speaker': 'Columbina',
                              'text': 'Do not let their titles rush your heart, Aether. Whichever mirror '
                                      'you hold up to me tonight... I will abide by what you choose.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B08',
                              'speaker': 'Narrator',
                              'text': 'Right as my hand moves toward hers, a sudden gust parts her white '
                                      'collar -- revealing tiny spiderwebbing frost-filaments creeping '
                                      'half an inch higher toward her throat!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B09',
                              'speaker': 'Sandrone',
                              'text': 'Tch -- her impedance just spiked two percent in the draft! Decide '
                                      'right now, Traveler!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B10',
                              'speaker': 'Aether',
                              'text': 'Columbina...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B11',
                              'speaker': 'Arlecchino',
                              'text': 'Look closely at that white seam on her neck, Aether. Devotion, '
                                      'knowledge, or protocol -- choose!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B12',
                              'speaker': 'Narrator',
                              'text': "Pulonia's optical lamp hums beside the dark subterranean stair "
                                      'while storm-clouds gather overhead.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B13',
                              'speaker': 'Columbina',
                              'text': 'Your hand is hovering in the cold, Traveler...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N19_B14',
                              'speaker': 'Narrator',
                              'text': 'In the hush before the coming storm, I commit to our path.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C09_DIVERGE',
                              'prompt': 'At the crimson threshold of Chapter Three, choose which path you '
                                        'take before the lunar eclipse.',
                              'options': [{'opt_id': 'C09_ROUTE_A',
                                           'label': "[Route A - Intimate Vigil] Clasp Columbina's hand "
                                                    'without hesitation and shelter with her in Silvermoon '
                                                    'Hall to attune your Descender pulse directly to hers.',
                                           'effects': {'bond': 2, 'insight': 0},
                                           'next_node': 'N20',
                                           'reaction_beats': [{'beat_id': 'N19_R_A1',
                                                               'speaker': 'Aether',
                                                               'text': 'I am not leaving her alone while '
                                                                       'her pulse is trembling, '
                                                                       'Arlecchino. Guard the shaft above '
                                                                       '-- I am taking Columbina back '
                                                                       'inside Silvermoon Hall and '
                                                                       'anchoring her breath myself.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N19_R_A2',
                                                               'speaker': 'Arlecchino',
                                                               'text': 'Very well. Then we shall meet you '
                                                                       "at Zapolyarny's glass conservatory "
                                                                       'on Day Nine -- see that your nerve '
                                                                       'holds when the storm breaks '
                                                                       'tonight.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C09_ROUTE_B',
                                           'label': "[Route B - Deep Gallery Lore] Entrust Columbina's "
                                                    "rest to Pulonia's warm barrier and descend into the "
                                                    'Deep Gallery vault with Arlecchino and Sandrone.',
                                           'effects': {'bond': 0, 'insight': 2},
                                           'next_node': 'N23',
                                           'reaction_beats': [{'beat_id': 'N19_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Rest inside the warm pavilion '
                                                                       "behind Pulonia's shield until "
                                                                       'dawn, Columbina. I am going down '
                                                                       'into that Hyperborean vault with '
                                                                       'Arlecchino and Sandrone to bring '
                                                                       'back the exact key that breaks '
                                                                       'this seal.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N19_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Walk carefully in the deep ice, '
                                                                       'Aether... I will keep my breath '
                                                                       'slow and listen for your return at '
                                                                       'dawn.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C09_ROUTE_C',
                                           'label': '[Route C - Harbinger Distance] Draw your hand back '
                                                    'from the spreading porcelain crack at her throat and '
                                                    'urge No. 3 to freeze her emotions behind protocol.',
                                           'effects': {'bond': 0,
                                                       'insight': 1,
                                                       'add_flags': ['F11_COLD_PROTOCOL']},
                                           'next_node': 'N25',
                                           'reaction_beats': [{'beat_id': 'N19_R_C1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Staring at the bone-white '
                                                                       'filaments creeping toward her '
                                                                       'throat, dread seizes my wrist -- '
                                                                       'and I pull my hand half a step '
                                                                       'back from her reach.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N19_R_C2',
                                                               'speaker': 'Columbina',
                                                               'text': '...Ah. Your hand drew back. Do not '
                                                                       'look troubled, Traveler -- the '
                                                                       'Third Harbinger remembers where '
                                                                       'the high frost-altar stands.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n18_crimson_threshold.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N20': {'node_id': 'N20',
                   'chapter_id': 'CH3',
                   'title': 'When Thunder Strikes Without Lightning',
                   'day_label': 'Day 6 - Stormy Night, 22:00',
                   'location': 'Silvermoon Hall - Darkened Inner Grotto',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'flowchart_pos': [19, 1],
                   'beats': [{'beat_id': 'N20_B01',
                              'speaker': 'Narrator',
                              'text': 'By ten at night, a dry polar thunderstorm rolls directly across '
                                      "Hiisi's limestone roof while Paimon and Luonnotar sleep behind the "
                                      'curtained hearth-niche.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B02',
                              'speaker': 'Narrator',
                              'text': 'Without warning, a deafening clap of dry winter thunder booms down '
                                      'the cavern shaft -- zero lightning flash to herald it, only raw '
                                      'concussive shock!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B03',
                              'speaker': 'Columbina',
                              'text': '--!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B04',
                              'speaker': 'Narrator',
                              'text': 'The fearless former Third Harbinger gasps sharply, both hands '
                                      'flying to cover her ears as she flinches straight against my side '
                                      'in the blue gloom!',
                              'inner_thought': 'With her eyes veiled, sudden thunder without preceding '
                                               'rain or Kuuvahki static strikes her blindside!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B05',
                              'speaker': 'Aether',
                              'text': 'Easy -- I am right here, Columbina. It was only dry winter thunder '
                                      'above the bluff.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B06',
                              'speaker': 'Columbina',
                              'text': 'Ah... how embarrassing. Rain announces itself across a hundred '
                                      'yards of mist, so I never mind rain... yet thunder crashes out of '
                                      'silence before I can brace my chest.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N20_B07',
                              'speaker': 'Narrator',
                              'text': 'A second rolling peal shakes loose silver rime from the ceiling '
                                      'vault. Beneath my palm, the six small wings in her hair quiver like '
                                      "a startled dove's plumage.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B08',
                              'speaker': 'Columbina',
                              'text': 'Do not tell Tartaglia or Peruere that Kuutar jumped at sky-noise, '
                                      'please... It would ruin three centuries of dreadful mystique.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B09',
                              'speaker': 'Aether',
                              'text': 'Your dreadful mystique was already ruined over wild berries two '
                                      'mornings ago.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B10',
                              'speaker': 'Narrator',
                              'text': 'Yet beneath our light banter, I feel the porcelain seam under her '
                                      'collar thrumming erratically from the startle-reflex.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B11',
                              'speaker': 'Columbina',
                              'text': 'Another peal is gathering in the clouds above... my pulse is racing '
                                      'out of time, Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B12',
                              'speaker': 'Narrator',
                              'text': 'In the dim azure glow of the cavern water, she leans into the '
                                      'shelter of my cloak, waiting for me to anchor the next crash.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N20_B13',
                              'speaker': 'Columbina',
                              'text': 'Stay close until the storm passes over the strait...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C10_A',
                              'prompt': 'Another dry thunderclap gathers overhead while Columbina trembles '
                                        'against your cloak.',
                              'options': [{'opt_id': 'C10_A1',
                                           'label': 'Gather her into a warm embrace and press her palm '
                                                    'over your chest so she counts your steady heartbeat '
                                                    'instead of the thunder.',
                                           'effects': {'bond': 2, 'insight': 0},
                                           'next_node': 'N21',
                                           'reaction_beats': [{'beat_id': 'N20_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Drawing her into my arms beneath '
                                                                       'my cloak, I guide her cool palm '
                                                                       'flat over my sternum just as the '
                                                                       'third thunderclap rolls harmlessly '
                                                                       'above the stone.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N20_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': 'One... two... three... Your '
                                                                       'heartbeat drowns out the whole sky '
                                                                       'from this close, Aether.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C10_A2',
                                           'label': 'Cradle both her hands and guide her breathing in slow '
                                                    "four-count acoustic intervals to dampen the seal's "
                                                    'spike.',
                                           'effects': {'bond': 0, 'insight': 2},
                                           'next_node': 'N21',
                                           'reaction_beats': [{'beat_id': 'N20_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Breathe in with me for four counts '
                                                                       'before the air-pressure drops -- '
                                                                       'there, now exhale across the '
                                                                       "thunder's tail so the shockwave "
                                                                       'cannot jar your collarbone.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N20_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Ah... the sting faded right on the '
                                                                       'fourth count. You read '
                                                                       'wave-interference almost like a '
                                                                       'choir-master.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n20_thunder_embrace.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N21': {'node_id': 'N21',
                   'chapter_id': 'CH3',
                   'title': 'Pulse Through the Lattice Veil',
                   'day_label': 'Day 7 - Deep Night, 00:30',
                   'location': 'Silvermoon Hall - Moonlit Stone Ledge',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [20, 1],
                   'beats': [{'beat_id': 'N21_B01',
                              'speaker': 'Narrator',
                              'text': 'Half an hour past midnight opening Day Seven, the dry storm clears, '
                                      'letting a single blade of silver moonlight fall through the upper '
                                      'fissure onto our quiet ledge.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B02',
                              'speaker': 'Columbina',
                              'text': 'The thunder has gone out to sea... yet you have still not let go of '
                                      'my hands, Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B03',
                              'speaker': 'Aether',
                              'text': 'Your fingers only just stopped being cold. Five more minutes will '
                                      'not hurt.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B04',
                              'speaker': 'Narrator',
                              'text': 'Sitting scarce a breath away in the silver hush, Columbina lifts '
                                      'one hand to touch my cheek -- tracing the line of my jaw with '
                                      'feather-light curiosity.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B05',
                              'speaker': 'Columbina',
                              'text': 'Through Kuuvahki, I know the warm gold of your aura by heart. Yet '
                                      'tonight... a wicked little wish keeps whispering inside me: what do '
                                      'your eyes truly look like when they watch me?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B06',
                              'speaker': 'Aether',
                              'text': 'Columbina, wait -- do not test the seal before our grounding duet '
                                      'is ready!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B07',
                              'speaker': 'Columbina',
                              'text': 'Just the tiniest sliver behind the lace... surely heaven will not '
                                      'begrudge half a lash...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B08',
                              'speaker': 'Narrator',
                              'text': 'Behind the translucent white X-lattice, her dark lashes part by a '
                                      "hair's breadth -- and for one breathless instant, a luminous "
                                      'lotus-pink gleam catches the moonlight!',
                              'inner_thought': 'Lotus-pink clear as dawn over snow -- and instantly a '
                                               'gold-white curse spark arcs straight across her temple!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B09',
                              'speaker': 'Columbina',
                              'text': 'Ngh -- ahh!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B10',
                              'speaker': 'Narrator',
                              'text': 'She snaps her eyelids shut with a sharp gasp as a hairline '
                                      'frost-crack races an inch higher from her collarbone toward the '
                                      'base of her throat, radiating an eerie, glacial angelic pressure!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B11',
                              'speaker': 'Columbina',
                              'text': 'Haa... haa... forgive me. Even through the gauze, half a second '
                                      'burned like staring into white iron.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B12',
                              'speaker': 'Narrator',
                              'text': 'Frost-vapor curls off the porcelain seam at her neck, stinging my '
                                      'knuckles with sub-zero static.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B13',
                              'speaker': 'Columbina',
                              'text': 'Does this cold porcelain on my throat frighten you now, Aether...?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N21_B14',
                              'speaker': 'Narrator',
                              'text': 'Her veiled face tilts toward me in fragile silence as my hands '
                                      'hover inches from the glowing crack.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C11_A',
                              'prompt': "A sharp curse-spark stings Columbina's temple and throat after "
                                        'her stolen half-glance behind the veil.',
                              'options': [{'opt_id': 'C11_A1',
                                           'label': 'Cup your warm palm gently over her X-lattice veil and '
                                                    'beg her to wait five more nights until you shatter '
                                                    'the curse completely.',
                                           'effects': {'bond': 2, 'insight': 0},
                                           'next_node': 'N22',
                                           'reaction_beats': [{'beat_id': 'N21_R_A1',
                                                               'speaker': 'Aether',
                                                               'text': 'Keep your eyes closed behind my '
                                                                       'palm just a few nights longer, '
                                                                       'Columbina. On eclipse midnight, I '
                                                                       'want you looking at me without a '
                                                                       'single spark of pain.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N21_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': '...I promise. Still... even for '
                                                                       'half a heartbeat, the gold I '
                                                                       'glimpsed was worth the sting.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]},
                                          {'opt_id': 'C11_A2',
                                           'label': 'Hold her shoulders steady while tracing the exact '
                                                    'discharge vector of that spark to map where the seal '
                                                    'vents from her temple.',
                                           'effects': {'bond': 0, 'insight': 2},
                                           'next_node': 'N22',
                                           'reaction_beats': [{'beat_id': 'N21_R_B1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Bracing her shoulders without '
                                                                       'flinching, I read the fading '
                                                                       'golden arc: the seal routes '
                                                                       'straight from the temple knots of '
                                                                       'her X-veil down the left '
                                                                       'pulse-artery toward her wrist!',
                                                               'inner_thought': 'Left temple straight down '
                                                                                'the left wrist -- the '
                                                                                'exact meridian where a '
                                                                                'wrist-bound ribbon can '
                                                                                'intercept it!',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N21_R_B2',
                                                               'speaker': 'Aether',
                                                               'text': 'Stay still against me, Columbina. '
                                                                       'That spark just showed me the '
                                                                       'exact meridian we need to ground.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C11_A3_RECOIL',
                                           'label': 'Jerk your hand back in alarm from the glacial angelic '
                                                    'aura and spreading porcelain crack at her neck.',
                                           'effects': {'bond': 0,
                                                       'insight': 0,
                                                       'add_flags': ['F11_COLD_PROTOCOL']},
                                           'next_node': 'N25',
                                           'reaction_beats': [{'beat_id': 'N21_R_C1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Stung by the sub-zero angelic '
                                                                       'backlash radiating off her cracked '
                                                                       'throat, my hand jerks backward '
                                                                       'before I can stop myself -- '
                                                                       'leaving empty cold air between us.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N21_R_C2',
                                                               'speaker': 'Columbina',
                                                               'text': '...Ah. Even you drew your hand '
                                                                       'back. Rest here, Traveler -- I '
                                                                       'need a little high cliff air '
                                                                       'before dawn.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n21_peek_diff.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N22': {'node_id': 'N22',
                   'chapter_id': 'CH3',
                   'title': 'Harmonic Sync Beneath Falling Rime',
                   'day_label': 'Day 7 - Dusk, 18:00',
                   'location': 'Silvermoon Hall - Subterranean Waterside',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [21, 1],
                   'beats': [{'beat_id': 'N22_B01',
                              'speaker': 'Narrator',
                              'text': "At dusk on Day Seven, an hour before Sandrone's Bore-Rail car "
                                      "departs for Zapolyarny's conservatory, Columbina and I stand alone "
                                      "beside Silvermoon Hall's glowing blue waterside.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B02',
                              'speaker': 'Narrator',
                              'text': 'Tiny Kuuhenki hover in a hushed ring over the Moonfall Silver '
                                      'lilies while Paimon packs winter rations back inside the warm '
                                      'hearth-room.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B03',
                              'speaker': 'Columbina',
                              'text': 'Once we board the rail north into Snezhnaya proper, the ambient '
                                      "Kuuvahki thins to a whisper under Her Majesty's winter. If we wish "
                                      'to test a trial duet, we must try it beside these waters first.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B04',
                              'speaker': 'Aether',
                              'text': 'Just one quiet phrase to test phase-alignment. The second your '
                                      'collarbone stings, we stop.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B05',
                              'speaker': 'Narrator',
                              'text': 'Standing palm-to-palm above the mirrored tide, Columbina begins '
                                      'humming the opening bar of her lullaby -- reaching toward that '
                                      'silent eighth-measure rest.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B06',
                              'speaker': 'Columbina',
                              'text': 'La-la... drift beneath the frost-white bough...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N22_B07',
                              'speaker': 'Narrator',
                              'text': 'Silver ripples expand in concentric rings from her bare ankles, '
                                      'pressing against my Descender aura as the eighth bar approaches.',
                              'inner_thought': 'Matching her silent rest cleanly takes deep attunement; '
                                               'pushing blindly could strain her cracked collar.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B08',
                              'speaker': 'Columbina',
                              'text': 'The measure is opening now, Aether... can your voice step inside it '
                                      'without forcing my breath?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B09',
                              'speaker': 'Narrator',
                              'text': 'The Kuuhenki hold motionless above the blue blossoms as our joined '
                                      'palms hum with rising lunar static.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B10',
                              'speaker': 'Aether',
                              'text': 'Steady... right on the downbeat...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B11',
                              'speaker': 'Narrator',
                              'text': 'Feeling the delicate tension along her wrist, I decide whether our '
                                      'shared cadence is strong enough to lock full resonance now or ease '
                                      'back safely.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N22_B12',
                              'speaker': 'Columbina',
                              'text': 'Guide the bar, my star.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C12_A_SYNC',
                              'prompt': "At the subterranean waterside, Columbina's trial lullaby opens "
                                        'its silent measure for your harmonic lock.',
                              'options': [{'opt_id': 'C12_SYNC_PASS',
                                           'label': 'Step into her silent eighth-measure rest and lock a '
                                                    'full Descender harmonic duet across the glowing '
                                                    'waterside.',
                                           'unlock_badge': '[HARMONIC SYNC]',
                                           'lock_hint': '[Needs Silent Note + Shared Lullaby (Bond>=12, '
                                                        'Insight>=8) OR Bond>=16, Insight>=10]',
                                           'when': {'any_of': [{'requires_all': ['F01_HEARD_SILENT_NOTE',
                                                                                 'F04_KUUHENKI_LULLABY_SHARED'],
                                                                'min_bond': 12,
                                                                'min_insight': 8},
                                                               {'min_bond': 16, 'min_insight': 10}]},
                                           'effects': {'bond': 1, 'insight': 1},
                                           'next_node': 'N28',
                                           'reaction_beats': [{'beat_id': 'N22_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Slipping seamlessly into her '
                                                                       'unsung rest, my star-counterpoint '
                                                                       'locks phase with her lullaby -- '
                                                                       'sending a warm gold-and-blue wave '
                                                                       'across the pool that cools the '
                                                                       'white seam on her neck!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N22_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': '...Not a single tremor. With this '
                                                                       'harmony steady between us, we are '
                                                                       "ready for Zapolyarny's winter "
                                                                       'glass.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C12_SYNC_WAVERING',
                                           'label': 'Ease off the resonance early so you do not strain her '
                                                    'fractured collarbone before reaching Zapolyarny.',
                                           'effects': {'bond': 0, 'insight': 1},
                                           'next_node': 'N29',
                                           'reaction_beats': [{'beat_id': 'N22_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Hold there -- your pulse fluttered '
                                                                       'half a beat on the bridge. Let us '
                                                                       'step down gently now and finish '
                                                                       "tuning with Sandrone's instruments "
                                                                       'in Zapolyarny.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N22_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Thank you for catching me before '
                                                                       'the note frayed, Aether. Let us '
                                                                       'board the northern car while the '
                                                                       'dusk holds.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c1_n02_waterside.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N23': {'node_id': 'N23',
                   'chapter_id': 'CH3',
                   'title': 'Vault of the Rebellious Envoy',
                   'day_label': 'Day 7 - Deep Night, 01:00',
                   'location': 'Derelict Deep Gallery - Crystalline Abyssal-Frost Vault',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [19, 2],
                   'beats': [{'beat_id': 'N23_B01',
                              'speaker': 'Narrator',
                              'text': 'Five hours of descending frost-choked Hyperborean stairs bring '
                                      'Arlecchino, Sandrone, and me into the cavernous crystal heart of '
                                      'the Deep Gallery at one in the morning.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B02',
                              'speaker': 'Narrator',
                              'text': 'Shattered pillars of star-silver ice arch over two intact relics '
                                      'resting at opposite ends of a cracked celestial dais, lit by '
                                      "Arlecchino's crimson flame and Sandrone's brass lamp.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B03',
                              'speaker': 'Sandrone',
                              'text': 'Mind the floor fissures! The permafrost seal down here is shifting '
                                      '-- once we disturb either pedestal, we will only have time to '
                                      'extract and calibrate ONE relic before sealing the lower bulkhead!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B04',
                              'speaker': 'Arlecchino',
                              'text': 'Examine both clearly before you reach, Aether. Neither is '
                                      'trinketry.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B05',
                              'speaker': 'Narrator',
                              'text': 'Upon the left lectern of white quartz rests a thin tablet of '
                                      'musical neumes etched in silver feather-strokes -- titled in '
                                      "Hyperborean script: 'Duet for the Unbound Star.'",
                              'inner_thought': "Koitar's own unfinished counterpoint -- written to vent an "
                                               "Angel's soul-seal into an extra-cosmic vessel!",
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B06',
                              'speaker': 'Sandrone',
                              'text': "That left tablet is the First Angel Koitar's mathematical "
                                      'counterpoint! Combined with my World-Formula decay constants and '
                                      'your outlander astronomy, my Zapolyarny astrolabe could derive a '
                                      'clean fourth-star theorem!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B07',
                              'speaker': 'Narrator',
                              'text': 'Upon the right altar smolders a dark-red octahedral prism of '
                                      'ancient Crimson Moon marrow, humming in sympathetic contrast with '
                                      "Arlecchino's gauntlets.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B08',
                              'speaker': 'Arlecchino',
                              'text': 'And on the right rests a Crimson Moon harmonic dampener from the '
                                      "Khaenri'ahn dynasty's oldest vault. Attuned by my blood-fire and "
                                      "Sandrone's lens, it can cushion Columbina's pulse so a shared "
                                      'lullaby grounds the surge safely.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B09',
                              'speaker': 'Aether',
                              'text': 'Pure theoretical counterpoint on the left, or harmonic marrow '
                                      "stabilization on the right... both lead into Sandrone's astrolabe "
                                      'in Zapolyarny.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B10',
                              'speaker': 'Sandrone',
                              'text': 'Ceiling rime is cracking above the east arch -- sixty seconds '
                                      'before the frost-pressure drops! Pick your instrument, Descender!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B11',
                              'speaker': 'Arlecchino',
                              'text': 'My flame will hold the vault roof until your hands finish. Move.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B12',
                              'speaker': 'Narrator',
                              'text': 'Ice dust rains between the twin pedestals as I step onto the '
                                      'Hyperborean dais.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B13',
                              'speaker': 'Sandrone',
                              'text': "Left for Koitar's score, right for the Crimson Marrow dampener -- "
                                      'now!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N23_B14',
                              'speaker': 'Narrator',
                              'text': 'Evaluating the clues I have gathered since Day One, I claim the '
                                      'relic that completes our chain.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C13_B',
                              'prompt': 'Inside the shifting Deep Gallery vault, choose which ancient '
                                        'Hyperborean relic to secure before dawn.',
                              'options': [{'opt_id': 'C13_B_KOITAR',
                                           'label': "Transcribe and lift the First Angel Koitar's "
                                                    'Unfinished Counterpoint Score from the white quartz '
                                                    'lectern.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F10_KOITAR_COUNTERPOINT_SCORE']},
                                           'next_node': 'N24',
                                           'reaction_beats': [{'beat_id': 'N23_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Lifting the quartz score-tablet '
                                                                       "cleanly into Sandrone's insulated "
                                                                       'case, I verify every Hyperborean '
                                                                       'interval written for an unbound '
                                                                       "star beyond Teyvat's sky.",
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N23_R_A2',
                                                               'speaker': 'Sandrone',
                                                               'text': 'Got it without chipping a single '
                                                                       'neume! Up to the Bore-Rail '
                                                                       'platform -- move!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C13_B_MARROW',
                                           'label': "Attune Arlecchino's Crimson Moon Harmonic Dampener "
                                                    "with Sandrone's prism so it cushions Columbina's "
                                                    'living song.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F12_CRIMSON_MARROW_TUNING']},
                                           'next_node': 'N24',
                                           'reaction_beats': [{'beat_id': 'N23_R_B1',
                                                               'speaker': 'Narrator',
                                                               'text': "Bracing Sandrone's brass ring "
                                                                       'around the octahedron while '
                                                                       'Arlecchino tempers its edge with '
                                                                       'crimson fire, I lock the dampener '
                                                                       'to gentle lunar resonance.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N23_R_B2',
                                                               'speaker': 'Arlecchino',
                                                               'text': 'Cleanly tempered. Its warmth will '
                                                                       'steady her chest when the '
                                                                       'astrolabe engages. To the upper '
                                                                       'rail!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N24': {'node_id': 'N24',
                   'chapter_id': 'CH3',
                   'title': 'Ashes of Hyperborea',
                   'day_label': 'Day 8 - Dawn Bore-Rail, 07:00',
                   'location': 'Subterranean Fatui Bore-Rail -> Zapolyarny Conservatory Annex',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'flowchart_pos': [20, 2],
                   'beats': [{'beat_id': 'N24_B01',
                              'speaker': 'Narrator',
                              'text': 'At seven on the morning of Day Eight, we ascend the upper crystal '
                                      'gallery of the Deep Vault to the pressurized Fatui Bore-Rail siding '
                                      'where Pulonia escorts a rested, cloak-wrapped Columbina aboard.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B02',
                              'speaker': 'Columbina',
                              'text': 'Welcome back from the deep ice, Aether... Even through three stone '
                                      'bulkheads, I heard your footsteps climbing back toward me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N24_B03',
                              'speaker': 'Aether',
                              'text': 'Paimon and Luonnotar are safe by the cavern hearth?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B04',
                              'speaker': 'Sandrone',
                              'text': 'Stuffed with toasted brioche and guarded by two Druzhna Vila '
                                      'sentries! Now strap in -- the armored Zapolyarny Bore-Rail Express '
                                      'clears the under-ice strait in twelve hours flat.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B05',
                              'speaker': 'Narrator',
                              'text': 'As the steam-driven subterranean railcar glides away from the '
                                      'crystalline Hyperborean vault, Columbina sits beside me against the '
                                      'velvet bulkhead while blue cavern light gives way to dark tunnel '
                                      'rime.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B06',
                              'speaker': 'Arlecchino',
                              'text': 'Once we reach Zapolyarny tonight, Commander Vesna will join us at '
                                      "Sandrone's astrolabe annex by military courier, while Tartaglia "
                                      'holds the Hiisi strait.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B07',
                              'speaker': 'Columbina',
                              'text': "How strange... leaving Nod-Krai's waters behind makes the air "
                                      'around my veil feel thin and quiet, like diving beneath heavy wool.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B08',
                              'speaker': 'Aether',
                              'text': 'Lean against my arm and sleep through the tunnel crossing, '
                                      "Columbina. We did not climb into Hyperborea's ashes empty-handed.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B09',
                              'speaker': 'Narrator',
                              'text': 'Across the long under-sea bore-tunnel, her breathing steadies '
                                      'against my sleeve while Sandrone polishes lenses across the aisle.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n23_deep_gallery.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B10',
                              'speaker': 'Narrator',
                              'text': "By early evening on Day Nine's eve-approach, the armored car brakes "
                                      'smoothly inside the frosted glass annex beneath Zapolyarny Palace, '
                                      'where brass astrolabe rings gleam overhead.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B11',
                              'speaker': 'Sandrone',
                              'text': 'End of the line -- Zapolyarny Astrolabe Annex! Give Pulonia until '
                                      'tomorrow evening to align the primary prisms while Columbina rests '
                                      'in the heated camellia wing!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N24_B12',
                              'speaker': 'Narrator',
                              'text': 'Guiding Columbina carefully across the unfamiliar Snezhnayan marble '
                                      "where Kuuvahki runs thin, we prepare for tomorrow evening's first "
                                      'Combination Gate.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N30'}],
                   'ending_id': None},
           'N25': {'node_id': 'N25',
                   'chapter_id': 'CH3',
                   'title': 'Altar of the Unfeeling Damselette',
                   'day_label': 'Day 7 - Pre-Dawn Frost, 02:00',
                   'location': 'Hiisi High Sea-Cliff - Ruined Frostmoon Plinth',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [21, 3],
                   'beats': [{'beat_id': 'N25_B01',
                              'speaker': 'Narrator',
                              'text': 'Snow drifts through the shattered stone ribs of the ancient '
                                      "frost-altar overlooking Hiisi's frozen cliffs. Columbina sits "
                                      'barefoot atop the ice plinth, ankles crossed, white ankle-ribbons '
                                      'trailing motionless in the bitter draft as my footsteps halt below '
                                      'her.',
                              'inner_thought': 'Wanderer warned me once -- stay away from her if you still '
                                               'possess a conscience.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B02',
                              'speaker': 'Columbina',
                              'text': 'You drew your hand back when the porcelain crack reached my throat, '
                                      'Traveler. Prudence is a gentle virtue... after all, a frost-forged '
                                      'weapon belongs inside its sheath until its master has need of a '
                                      'winter dirge.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B03',
                              'speaker': 'Narrator',
                              'text': 'Not a single azure blossom survives around the plinth tonight. '
                                      'Every petal at her bare heels has bleached to the dead, immaculate '
                                      'white of snow-buried bone, yet her lips curve in a gentle, '
                                      'untroubled smile beneath the X-woven gauze.',
                              'inner_thought': 'Not a trace of anger touches her voice -- and that '
                                               'serenity turns my blood to ice.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B04',
                              'speaker': 'Columbina',
                              'text': 'How fortunate for us both. Removing an inconvenient heart is much '
                                      'simpler than enduring its ache. Tell me honestly -- would your '
                                      'conscience sleep sweeter tonight if Kuutar granted your wish from '
                                      'afar, or if The Damselette forgot how to tremble at your name?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B05',
                              'speaker': 'Aether',
                              'text': 'Columbina, step down from that cliff-plinth! The wind up here is '
                                      'forty below zero -- you are letting the Harbinger frost swallow '
                                      'your own chest on purpose!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B06',
                              'speaker': 'Columbina',
                              'text': 'Why raise your voice, Aether? When your fingers pulled back from my '
                                      'neck, I understood everything clearly.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B07',
                              'speaker': 'Columbina',
                              'text': 'Mortals cherish pure songs from a safe distance, yet recoil when '
                                      'the singer begins cracking into something monstrous for their sake. '
                                      'Truly, I hold zero grievance against you.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B08',
                              'speaker': 'Narrator',
                              'text': 'Around the ruined cliff-altar, pale-blue cryo-mist spirals upward '
                                      'from the sea-crags, glazing the lower hem of her gown in razor-thin '
                                      'ice.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B09',
                              'speaker': 'Columbina',
                              'text': "Sandrone's valves already guard Nasha Town below. If I simply "
                                      "freeze this foolish mortal pulse back into the Third Harbinger's "
                                      "stillness tonight, heaven's curse loses its fuel -- and you walk "
                                      'free without blood on your hands.',
                              'inner_thought': 'She is offering to lobotomize her own heart out of polite, '
                                               'terrifying mercy for my hesitation!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B10',
                              'speaker': 'Aether',
                              'text': 'Freezing every feeling inside yourself so I do not feel guilty is '
                                      'not salvation -- that is suicide dressed as courtesy!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B11',
                              'speaker': 'Columbina',
                              'text': 'Courtesy was all Number Three ever needed in Zapolyarny Palace. '
                                      'Look -- even the porcelain crack on my collarbone stops stinging '
                                      'when I stop wishing for your warmth.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B12',
                              'speaker': 'Narrator',
                              'text': 'Far down the northern ridge, signal flares from rogue Fatui '
                                      'remnants still prowling outside the fjord blink red through the '
                                      'rising blizzard.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B13',
                              'speaker': 'Columbina',
                              'text': 'One word from you, Traveler, and I shall wrap myself in Her '
                                      "Majesty's winter and walk back to my third seat forever.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B14',
                              'speaker': 'Narrator',
                              'text': 'Rime creeps across her bare ankles on the freezing stone plinth -- '
                                      'seconds away from sealing her heart shut.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N25_B15',
                              'speaker': 'Columbina',
                              'text': 'Speak softly now... what does your conscience ask of me?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C14_C_BAD1_GATE',
                              'prompt': 'Frost creeps past her collarbone as she awaits your verdict with '
                                        'chilling, porcelain obedience.',
                              'options': [{'opt_id': 'C14_C_CONSCIENCE_WAKE',
                                           'label': 'Vault onto the frozen plinth, seize her ice-rimmed '
                                                    'hands, and call Columbina Hyposelenia back from '
                                                    'Harbinger stillness!',
                                           'unlock_badge': '[CONSCIENCE RESCUE]',
                                           'lock_hint': "[Needs Childe's Warning (Bond>=9) OR Bond>=11, "
                                                        'Insight>=8]',
                                           'when': {'any_of': [{'requires_all': ['F03_CHILDE_INSTINCT_HEEDED'],
                                                                'min_bond': 9},
                                                               {'min_bond': 11, 'min_insight': 8}]},
                                           'effects': {'bond': 1, 'insight': 1},
                                           'next_node': 'N27',
                                           'reaction_beats': [{'beat_id': 'N25_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Vaulting straight up onto the '
                                                                       'ice-glazed plinth, I seize both of '
                                                                       'her freezing hands in mine -- '
                                                                       'shattering the creeping rime with '
                                                                       'raw Descender warmth!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N25_R_A2',
                                                               'speaker': 'Aether',
                                                               'text': 'Damn my hesitation back at the '
                                                                       'gorge! You are not Number Three '
                                                                       'and you are not an altar idol -- '
                                                                       'come back to me, Columbina '
                                                                       'Hyposelenia!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N25_R_A3',
                                                               'speaker': 'Columbina',
                                                               'text': '...! Ah... your hands are burning '
                                                                       'through the frost... Why come back '
                                                                       'onto the ice after seeing what I '
                                                                       'am...?',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C14_C_DAMSELETTE_SEVER',
                                           'label': "Lower your gaze before the Third Harbinger's mercy "
                                                    'and let her seal the mortal fracture in eternal ice.',
                                           'effects': {'bond': 0, 'insight': 0},
                                           'next_node': 'N26',
                                           'reaction_beats': [{'beat_id': 'N25_R_B1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Frozen by the unearthly stillness '
                                                                       'in her smile and the fear of '
                                                                       'watching her mind shatter on Day '
                                                                       'Twelve, my boots stay rooted below '
                                                                       'the plinth as I lower my gaze.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N25_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': '...Thank you for your honesty, '
                                                                       'Traveler. Sleep peacefully -- I '
                                                                       'shall take care of the rest.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n25_damselette_altar.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N26': {'node_id': 'N26',
                   'chapter_id': 'CH3',
                   'title': 'Elogia Cinerosa: Mercy of No. 3',
                   'day_label': 'Day 7 - Blizzard Zero Hour, 03:00',
                   'location': 'Hiisi Sea-Cliff Blizzard - Fatui Extraction Ridge',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'flowchart_pos': [22, 4],
                   'beats': [{'beat_id': 'N26_B01',
                              'speaker': 'Narrator',
                              'text': 'At three in the morning, a whiteout gale roars off the polar sea, '
                                      'burying the ruined cliff-altar in driving horizontal snow.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B02',
                              'speaker': 'Narrator',
                              'text': 'Rising weightlessly from the frozen plinth, Columbina drifts down '
                                      'beside me and presses one winter-pale forefinger lightly against my '
                                      'lips.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B03',
                              'speaker': 'Columbina',
                              'text': 'Shh... do not apologize, Aether. A mortal heart was only a borrowed '
                                      'coat I wore for six foolish days, and winter suits me far better.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B04',
                              'speaker': 'Narrator',
                              'text': 'Deep inside her chest, a sound like a Cathedral ice-gate locking '
                                      'shut reverberates through the storm. Instantly, the porcelain crack '
                                      'on her neck stops spreading -- frozen beneath a glaze of absolute, '
                                      'unfeeling Harbinger frost.',
                              'inner_thought': 'She saved her own mind from shattering -- by entombing '
                                               'every warm feeling we ever shared in dead ice.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B05_F07',
                              'speaker': 'Narrator',
                              'text': 'At my wrist, the silver Luonnotar bell on the Moonweave Ribbon '
                                      'Chime glazes white with hoarfrost -- and cracks cleanly in two '
                                      'without a sound, its severed pulse-link going mute forever.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N26_B05_NOF07',
                              'speaker': 'Narrator',
                              'text': 'Behind her left ear, the silver Luonnotar bell braided into her '
                                      'hair glazes solid white with hoarfrost -- freezing its tiny clapper '
                                      'mute forever.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N26_B06',
                              'speaker': 'Aether',
                              'text': 'Columbina... wait--!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B07',
                              'speaker': 'Narrator',
                              'text': 'When I reach belatedly toward her sleeve, the glacial pressure '
                                      'rolling off the Third of the Eleven Fatui Harbingers numbs my arm '
                                      'to the shoulder, halting my step in deep drift-snow.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B08',
                              'speaker': 'Columbina',
                              'text': 'Give the little flying fairy waiting by my old hearth the rest of '
                                      'the berry jam, Traveler. Tell her the Hall has no owner anymore.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B09',
                              'speaker': 'Narrator',
                              'text': 'Down along the ice-locked ridge below, masked Fatui honor-guards '
                                      'kneel in two silent ranks beside black Palestar banners as she '
                                      'walks barefoot into the blizzard.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B10',
                              'speaker': 'Columbina',
                              'text': "Dormi, cinis albus... sleep beneath the pale star's ash...",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B11',
                              'speaker': 'Narrator',
                              'text': 'Her soprano rises through the howling whiteout in the solemn, '
                                      'funeral Latin of Elogia Cinerosa -- flawless, untrembling, and '
                                      'devoid of the lonely half-beat rest that once waited for me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B12',
                              'speaker': 'Narrator',
                              'text': 'Back inside Silvermoon Hall, Paimon will wake beside a cold brazier '
                                      'asking where Columbina went -- while every flower around the '
                                      'subterranean pool stands frozen in colorless ice.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N26_B13',
                              'speaker': 'Narrator',
                              'text': 'Long after the black banners vanish toward Snezhnaya, her ash-white '
                                      'lullaby echoes across the cliff -- sparing my life while haunting '
                                      'my conscience forever.',
                              'inner_thought': 'BAD ENDING I -- Elogia Cinerosa: Mercy of No. 3.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n26_bad1_elogia.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_BAD_1'},
           'N27': {'node_id': 'N27',
                   'chapter_id': 'CH3',
                   'title': 'Sleigh Through the Palestar Blizzard',
                   'day_label': 'Day 8 - Blizzard Pass, 15:00',
                   'location': 'Northern Border Fjord - Armored Icebreaker Sleigh',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'flowchart_pos': [22, 3],
                   'beats': [{'beat_id': 'N27_B01',
                              'speaker': 'Narrator',
                              'text': 'After carrying an exhausted Columbina down from the cliff-altar and '
                                      "sheltering through Day Seven's gale, Tartaglia and Commander Vesna "
                                      'meet us at the northern fjord pass on the afternoon of Day Eight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N27_B02',
                              'speaker': 'Tartaglia',
                              'text': 'Hold onto the iron rail back there, comrade! My armored courier '
                                      "sleigh eats six-foot snowdrifts for breakfast, and Zapolyarny's "
                                      'outer gate is straight ahead!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N27_B03',
                              'speaker': 'Vesna',
                              'text': 'Do not worry about Hiisi Island or little Paimon, Traveler! Two of '
                                      "my trusted Vila sisters are tending Silvermoon Hall's hearth with "
                                      "Luonnotar while Sandrone's valves and my pylons hold the tide!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N27_B04',
                              'speaker': 'Narrator',
                              'text': 'Bundled deep in white wolf-fur blankets inside the enclosed rear '
                                      'cab, Columbina leans quietly against my chest. Though I stopped her '
                                      'from freezing her heart, a thin frost-line from my earlier recoil '
                                      'still lingers on her X-lattice veil.',
                              'inner_thought': 'Only direct clemency and harmonic grace at Zapolyarny '
                                               'Palace can mend the hairline frost my hesitation left.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N27_B05',
                              'speaker': 'Columbina',
                              'text': 'You actually climbed onto that freezing plinth and shouted my '
                                      'chosen name into the wind, Aether... Tartaglia must think we have '
                                      'both lost our wits.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': 'outing_bump_rescue'},
                             {'beat_id': 'N27_B06',
                              'speaker': 'Aether',
                              'text': 'If I ever pull my hand back again, you have full permission to drop '
                                      'a snowbank on my head. Right now, why are we heading straight to '
                                      "the Tsaritsa's glass garden?",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N27_B07',
                              'speaker': 'Vesna',
                              'text': "Because the frost-fracture on Lady Columbina's veil resonated with "
                                      "Her Majesty's old Palestar authority when she nearly sealed her "
                                      'heart on the cliff!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N27_B08',
                              'speaker': 'Tartaglia',
                              'text': 'Her Majesty Anastasya agreed to grant a private audience in the '
                                      'Imperial Camellia Conservatory tomorrow night! Once I drop you at '
                                      "the palace Postern, I am racing straight back to guard Hiisi's "
                                      'outer ice!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N27_B09',
                              'speaker': 'Columbina',
                              'text': "Her Majesty's camellia dome... Even among the Eleven, few have "
                                      'heard the Cryo Archon speak of love without winter in her voice.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N27_B10',
                              'speaker': 'Aether',
                              'text': 'Rest against me until the runners reach palace stone, Columbina. '
                                      'Tomorrow night, I will answer Her Majesty myself.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N27_B11',
                              'speaker': 'Narrator',
                              'text': "As Childe's ice-runners carve twin silver arcs across the border "
                                      'pass, the towering crystal spires of Zapolyarny Palace rise out of '
                                      'the northern dusk.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c3_n27_blizzard_sleigh.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N31'}],
                   'ending_id': None},
           'N28': {'node_id': 'N28',
                   'chapter_id': 'CH4',
                   'title': 'Camellias Under Zapolyarny Glass',
                   'day_label': 'Day 9 - Afternoon, 15:30',
                   'location': 'Zapolyarny Palace - Imperial Camellia Conservatory',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [23, 0],
                   'beats': [{'beat_id': 'N28_B01',
                              'speaker': 'Narrator',
                              'text': 'Afternoon snow glitters across the soaring iron-and-crystal ribs of '
                                      "Zapolyarny Palace's outer conservatory, where white winter "
                                      'camellias bloom inside heated glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B02',
                              'speaker': 'Narrator',
                              'text': "Far from Hiisi Island's dense subterranean springs, Snezhnaya's "
                                      "ambient Kuuvahki runs thin beneath the Cryo Archon's winter -- "
                                      "shrinking Columbina's veiled spatial sense to arm's reach.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B03_F07',
                              'speaker': 'Columbina',
                              'text': 'Everything outside this path sounds muffled under palace frost, '
                                      'Aether... Keep your wrist close so I can follow the little silver '
                                      'bell you wear for me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N28_B03_NOF07',
                              'speaker': 'Columbina',
                              'text': 'Everything outside this path sounds muffled under palace frost, '
                                      'Aether... Let me hold your sleeve and listen to your boots while '
                                      'the chime in my hair keeps time.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N28_B04',
                              'speaker': 'Narrator',
                              'text': 'Her fingers curl lightly into my cuff as Sandrone briskly '
                                      'approaches down the marble aisle, holding up a silver-sealed '
                                      'imperial parchment.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B05',
                              'speaker': 'Sandrone',
                              'text': "There you two are! Catch -- fresh from Her Majesty's chancellery: "
                                      'the formal Palestar Suspension Writ! Not a single Fatui regiment '
                                      'may lay a finger on Columbina or Hiisi Island!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B06',
                              'speaker': 'Aether',
                              'text': 'And the perimeter back on Hiisi while we are here?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B07',
                              'speaker': 'Sandrone',
                              'text': "Tighter than a bank vault! Tartaglia's vanguard, Peruere's Crimson "
                                      "Moon stakes, and Commander Vesna's Vila choir are all stationed "
                                      'around my six Pulonia tide-valves -- and Paimon just wired that '
                                      'Luonnotar ate two whole berry scones!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B08',
                              'speaker': 'Columbina',
                              'text': 'Hehe... so everyone is guarding my little hall while I borrow Her '
                                      "Majesty's camellias.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N28_B09',
                              'speaker': 'Sandrone',
                              'text': "Do not get complacent! Pulonia's scan shows your Waterside harmonic "
                                      'sync held admirably during the rail crossing, which leaves sixty '
                                      'minutes before the return express to lock your final Descender '
                                      'grounding vow!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B10',
                              'speaker': 'Narrator',
                              'text': 'Leaving us beneath an arch of snow-white camellias, Sandrone '
                                      'marches back to prime the return car.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B11',
                              'speaker': 'Columbina',
                              'text': 'Without Kuuvahki mist around us here, Aether, I can feel the '
                                      "boundary between Teyvat's air and your star-born core sharper than "
                                      'ever.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B12',
                              'speaker': 'Aether',
                              'text': 'Three nights remain before the syzygy opens above Silvermoon Hall.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N28_B13',
                              'speaker': 'Narrator',
                              'text': 'Among silent white blossoms under frosted glass, Columbina rests '
                                      'both hands in mine.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C15_A_PACT',
                              'prompt': "Beneath Zapolyarny's white camellias, seal how your Descender "
                                        'vessel prepares for the eclipse return.',
                              'options': [{'opt_id': 'C15_A1',
                                           'label': 'Press her hand over your star-born core and swear the '
                                                    "Fourth Descender's Harmonic Pact -- opening an active "
                                                    'conduit past Irminsul.',
                                           'effects': {'bond': 0,
                                                       'insight': 1,
                                                       'add_flags': ['F09_DESCENDER_HARMONIC_PACT']},
                                           'next_node': 'N32',
                                           'reaction_beats': [{'beat_id': 'N28_R_A1',
                                                               'speaker': 'Aether',
                                                               'text': 'Feel this pulse beneath my ribs, '
                                                                       'Columbina -- no thread of it '
                                                                       'belongs to Irminsul. At midnight '
                                                                       'on Day Twelve, pour every ounce of '
                                                                       "heaven's backlash straight through "
                                                                       'me into the stars beyond.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N28_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': '...The circuit answered in clean '
                                                                       'golden fourths. Now let us go home '
                                                                       'to Silvermoon Hall.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C15_A2',
                                           'label': 'Wrap your warm cloak around her shoulders among the '
                                                    'camellias and pour steady affection into calming her '
                                                    'pulse for the journey home.',
                                           'effects': {'bond': 2, 'insight': 0},
                                           'next_node': 'N32',
                                           'reaction_beats': [{'beat_id': 'N28_R_B1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Fastening my warm travel cloak '
                                                                       'over her white capelet, I hold her '
                                                                       'close among the camellia petals '
                                                                       'until the Snezhnayan chill leaves '
                                                                       'her wrists completely.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N28_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': "Even in the Tsaritsa's winter, you "
                                                                       'smell of warm sun and silver '
                                                                       'lilies... Let us hurry home, '
                                                                       'Aether.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n28_camellia_glass.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N29': {'node_id': 'N29',
                   'chapter_id': 'CH4',
                   'title': 'Clockwork Key & Trembling Feathers',
                   'day_label': 'Day 9 - Afternoon, 16:00',
                   'location': 'Zapolyarny Conservatory - Outer Clockwork Colonnade',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [23, 1],
                   'beats': [{'beat_id': 'N29_B01',
                              'speaker': 'Narrator',
                              'text': "Inside the marble colonnade adjoining Zapolyarny's conservatory on "
                                      'Day Nine, thin Kuuvahki leaves Columbina holding tightly to my '
                                      'forearm as brass steam-pipes hum along the glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B02_F07',
                              'speaker': 'Narrator',
                              'text': 'At my wrist, the silver Luonnotar bell on the Moonweave Ribbon '
                                      'Chime rings in uneven, stuttering triplets -- betraying the '
                                      'unfinished Waterside sync we halted on Day Seven.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N29_B02_NOF07',
                              'speaker': 'Narrator',
                              'text': 'Behind her ear, the silver Luonnotar bell braided in her hair rings '
                                      'in uneven, stuttering triplets -- betraying the unfinished '
                                      'Waterside sync we halted on Day Seven.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N29_B03',
                              'speaker': 'Sandrone',
                              'text': "Hold still right there! First, take Her Majesty's sealed Palestar "
                                      "Suspension Writ -- Tartaglia, Peruere, and Vesna's Vila are all "
                                      'holding the Hiisi valve-ring with Paimon safe inside the Hall!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B04',
                              'speaker': 'Sandrone',
                              'text': 'Second -- what is this sloppy four-hertz phase wobble on '
                                      "Columbina's collarbone?! You stopped the Waterside trial halfway!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B05',
                              'speaker': 'Aether',
                              'text': 'Pushing harder on Day Seven without instruments would have cracked '
                                      'the seam wider.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B06',
                              'speaker': 'Sandrone',
                              'text': 'Prudent, yes -- but if you ride back to Hiisi with an unsteadied '
                                      "carrier wave, tomorrow night's pre-eclipse foreshock in the Sanctum "
                                      'will hit her like a battering ram!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B07',
                              'speaker': 'Narrator',
                              'text': "Flipping open a portable brass tuning fork calibrated to Pulonia's "
                                      'core, Sandrone strikes a pure reference tone that shimmers down the '
                                      'glass corridor.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B08',
                              'speaker': 'Columbina',
                              'text': 'My feathers are trembling a little in this thin palace air, '
                                      "Aether... Can your breath catch Sandrone's reference pitch for me?",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B09',
                              'speaker': 'Sandrone',
                              'text': 'You have one clean attempt before the return Bore-Rail departs! '
                                      'Either lock the carrier wave cleanly right now, or brace yourself '
                                      'for a rough landing at the Sanctum!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B10',
                              'speaker': 'Narrator',
                              'text': "Taking Columbina's cool wrists in both hands, I match my breathing "
                                      'to the ringing brass fork.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B11',
                              'speaker': 'Aether',
                              'text': 'Listen to my chest, Columbina -- one measure at a time.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N29_B12',
                              'speaker': 'Narrator',
                              'text': 'As the tuning fork reaches peak resonance, I choose whether we have '
                                      'the depth to lock the wave cleanly or shield her gently.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C16_A_RECOVER',
                              'prompt': "Sandrone's brass tuning fork rings down the glass corridor before "
                                        'the return rail departs.',
                              'options': [{'opt_id': 'C16_REC_STEADY',
                                           'label': "Anchor her pulse to Sandrone's brass tuning fork and "
                                                    'iron out every harmonic tremor before the return '
                                                    'express.',
                                           'unlock_badge': '[PULSE STEADIED]',
                                           'lock_hint': '[Requires Bond >= 13 and Insight >= 9]',
                                           'when': {'min_bond': 13, 'min_insight': 9},
                                           'effects': {'bond': 1, 'insight': 1},
                                           'next_node': 'N32',
                                           'reaction_beats': [{'beat_id': 'N29_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Anchoring both her hands against '
                                                                       'my sternum while aligning my '
                                                                       "elemental pitch to Sandrone's "
                                                                       'fork, I iron every tremor out of '
                                                                       'her collarbone seam in three clean '
                                                                       'breaths!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N29_R_A2',
                                                               'speaker': 'Sandrone',
                                                               'text': 'Zero-point-zero drift! Hmph -- '
                                                                       'acceptable work, Outlander! Now '
                                                                       'get her aboard the express back to '
                                                                       'Silvermoon Hall!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C16_REC_SLIP',
                                           'label': 'Keep your resonance gentle and focus on shielding her '
                                                    'body during the return journey to Hiisi.',
                                           'effects': {'bond': 1, 'insight': 0},
                                           'next_node': 'N33',
                                           'reaction_beats': [{'beat_id': 'N29_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Forcing a full lock in thin '
                                                                       'Kuuvahki is stinging her throat, '
                                                                       'Sandrone -- I will cushion her '
                                                                       'pulse manually on the train and '
                                                                       'meet the surge at the Sanctum.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N29_R_B2',
                                                               'speaker': 'Sandrone',
                                                               'text': 'Tch... then guard your hands '
                                                                       'tomorrow night, Traveler, because '
                                                                       'the Sanctum prism will not pull '
                                                                       'its punch!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n29_clockwork_corridor.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N30': {'node_id': 'N30',
                   'chapter_id': 'CH4',
                   'title': 'Combination Gate I: Theorem of the Fourth Star',
                   'day_label': 'Day 9 - Evening, 19:00',
                   'location': "Zapolyarny Palace - Sandrone's Astrolabe Annex",
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [23, 2],
                   'beats': [{'beat_id': 'N30_B01',
                              'speaker': 'Narrator',
                              'text': 'At seven on the ninth evening, concentric brass astrolabe rings '
                                      "spin beneath the frosted dome of Sandrone's Zapolyarny annex as "
                                      'Arlecchino and newly arrived Commander Vesna stand watch.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B02',
                              'speaker': 'Narrator',
                              'text': "Pinned beside the central lens is the Cryo Archon's newly stamped "
                                      "Palestar Suspension Writ, alongside Tartaglia's heliograph "
                                      "confirming that Hiisi's outer strait and Pulonia's six tide-valves "
                                      'stand secure.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B03_F07',
                              'speaker': 'Columbina',
                              'text': 'The palace air is so thin against my veil tonight... Stay beside '
                                      'the lectern, Aether, so the Moonweave chime on your wrist keeps my '
                                      'bearings clear.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N30_B03_NOF07',
                              'speaker': 'Columbina',
                              'text': 'The palace air is so thin against my veil tonight... Stay beside '
                                      'the lectern, Aether, while the chime braided in my hair listens for '
                                      'your voice.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N30_B04',
                              'speaker': 'Sandrone',
                              'text': 'Attention, everyone! Pulonia has mounted the Deep Gallery relic at '
                                      "the astrolabe's focal point -- now we synthesize the complete "
                                      'Fourth-Star Grounding Theorem!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B05',
                              'speaker': 'Vesna',
                              'text': 'Remember what the Hyperborean mural taught us: because the Angel '
                                      'Curse fires autonomously inside the soul, an ordinary Teyvat '
                                      'circuit rebounds and destroys the mind.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B06',
                              'speaker': 'Arlecchino',
                              'text': 'Which means your synthesis must prove one of two complete chains '
                                      'without a single missing link, Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B07',
                              'speaker': 'Sandrone',
                              'text': 'Chain One -- Pure Celestial Mathematics: combine your outlander '
                                      "False-Sky astronomy, Koitar's Unfinished Counterpoint Score, and my "
                                      '13.7-kilohertz World-Formula decay curve!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B08',
                              'speaker': 'Vesna',
                              'text': 'Or Chain Two -- Living Harmonic Cushion: weave your shared '
                                      'Luonnotar star-lullaby, the Crimson Moon Marrow dampener, and my '
                                      'Snowland Fae Seelie Codex into one resonant shield!',
                              'inner_thought': 'Every clue from Silvermoon Hall, the birch vault, '
                                               "Sandrone's tea table, and the Deep Gallery converges right "
                                               'here!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B09',
                              'speaker': 'Narrator',
                              'text': 'Golden-blue light pours from the spinning brass rings onto '
                                      "Columbina's veiled face as the porcelain seam at her collarbone "
                                      'begins humming in anticipation.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B10',
                              'speaker': 'Columbina',
                              'text': 'Do not force the rings if a piece is missing, Aether... an '
                                      'incomplete chord here would rattle straight into my chest.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B11',
                              'speaker': 'Sandrone',
                              'text': 'Main prism reaching alignment -- step to the console and feed in '
                                      'your proof, Fourth Descender!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B12',
                              'speaker': 'Arlecchino',
                              'text': 'Show us whether five days of gathering truth were enough.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B13',
                              'speaker': 'Aether',
                              'text': 'Stand with me by the focal ring, Columbina.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N30_B14',
                              'speaker': 'Narrator',
                              'text': "My hands settle on the astrolabe's twin vernier dials at "
                                      'Combination Gate One.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C17_B_COMBO_GATE1',
                              'combination_gate': True,
                              'prompt': 'COMBINATION GATE I -- Synthesize your multi-chapter clues inside '
                                        "Sandrone's Zapolyarny astrolabe.",
                              'options': [{'opt_id': 'C17_GATE1_UNLOCK',
                                           'label': "Synthesize your multi-chapter clues inside Sandrone's "
                                                    'astrolabe to prove the complete Fourth-Star Grounding '
                                                    'Theorem!',
                                           'unlock_badge': '[COMBO GATE I]',
                                           'lock_hint': '[Needs (F02+F10+F08 & Insight>=12) OR '
                                                        '(F04+F12+F06 & Bond>=11)]',
                                           'when': {'any_of': [{'requires_all': ['F02_FALSE_SKY_CONFIDANT',
                                                                                 'F10_KOITAR_COUNTERPOINT_SCORE',
                                                                                 'F08_SANDRONE_TEA_FORMULA'],
                                                                'min_insight': 12},
                                                               {'requires_all': ['F04_KUUHENKI_LULLABY_SHARED',
                                                                                 'F12_CRIMSON_MARROW_TUNING',
                                                                                 'F06_VESNA_SEELIE_CODEX'],
                                                                'min_bond': 11}]},
                                           'effects': {'bond': 2,
                                                       'insight': 1,
                                                       'add_flags': ['F09_DESCENDER_HARMONIC_PACT']},
                                           'next_node': 'N32',
                                           'reaction_beats': [{'beat_id': 'N30_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Locking every gathered clue into '
                                                                       "the astrolabe's vernier, the brass "
                                                                       'rings chime a triumphant golden '
                                                                       'chord -- projecting a flawless '
                                                                       'extra-cosmic grounding vector from '
                                                                       "Columbina's soul through my "
                                                                       'Descender core!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N30_R_A2',
                                                               'speaker': 'Sandrone',
                                                               'text': 'Ha!! Zero residual impedance '
                                                                       'across the boundary! We have the '
                                                                       'Theorem of the Fourth Star -- '
                                                                       'Pulonia, clear the Bore-Rail back '
                                                                       'to Silvermoon Hall!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C17_GATE1_FALLBACK',
                                           'label': 'Halt the astrolabe projection early to spare '
                                                    "Columbina's trembling pulse and escort her back to "
                                                    'Silvermoon Hall.',
                                           'effects': {'bond': 1, 'insight': 1},
                                           'next_node': 'N33',
                                           'reaction_beats': [{'beat_id': 'N30_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Cut the beam, Sandrone! Without '
                                                                       'the missing link in that triad, '
                                                                       'the harmonic feedback is biting '
                                                                       'straight into her collarbone!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N30_R_B2',
                                                               'speaker': 'Arlecchino',
                                                               'text': 'Wise to disengage before the prism '
                                                                       'spiked -- yet without a completed '
                                                                       'theorem, prepare to weather a '
                                                                       'fierce foreshock at the Sanctum '
                                                                       'tomorrow night.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n30_combo_gate1.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N31': {'node_id': 'N31',
                   'chapter_id': 'CH4',
                   'title': 'Combination Gate II: Audience With the Cryo Archon',
                   'day_label': 'Day 9 - Night, 21:30',
                   'location': 'Zapolyarny Palace - Sovereign Cryo Conservatory',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [23, 3],
                   'beats': [{'beat_id': 'N31_B01',
                              'speaker': 'Narrator',
                              'text': 'At half past nine on the ninth night, towering doors of rime-etched '
                                      'crystal swing silently shut behind us inside the sovereign '
                                      'conservatory of Zapolyarny Palace.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B02',
                              'speaker': 'Narrator',
                              'text': 'Standing beneath a vault of frozen starlight and sapphire '
                                      'ice-pillars is Her Majesty the Tsaritsa -- silver hair crowned in '
                                      'crystalline frost, pale eyes holding five centuries of winter grief '
                                      'as her hand rests upon an ice scepter.',
                              'inner_thought': "Even motionless, the Cryo Archon's presence stills every "
                                               'molecule of air in the conservatory.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B03_F07',
                              'speaker': 'Narrator',
                              'text': 'Beside me in the thin Snezhnayan Kuuvahki, Columbina keeps two '
                                      'fingers brushed lightly against the Moonweave Ribbon Chime on my '
                                      'wrist -- where the hairline frost-fracture of my earlier recoil '
                                      'still clouds her X-veil.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N31_B03_NOF07',
                              'speaker': 'Narrator',
                              'text': 'Beside me in the thin Snezhnayan Kuuvahki, Columbina holds the edge '
                                      'of my sleeve while the chime in her hair stays hushed -- the '
                                      'hairline frost-fracture of my earlier recoil still clouding her '
                                      'X-veil.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N31_B04',
                              'speaker': 'The Tsaritsa',
                              'text': 'Step no nearer the dais, Fourth Descender... and lift your head, my '
                                      "little Moon Maiden. I have already signed Sandrone's writ "
                                      "suspending the Palestar Edict, while my Harbingers and Vesna's Fae "
                                      "guard Hiisi's waters.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B05',
                              'speaker': 'Columbina',
                              'text': 'Your Majesty... Even after I left my third seat empty, your winter '
                                      'glass still remembers the temperature of my wings.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B06',
                              'speaker': 'The Tsaritsa',
                              'text': 'How could the Archon who once loved too fiercely fail to recognize '
                                      "heaven's cruelest shackle? Look at the hairline frost marring her "
                                      'veil, Outlander -- born the instant your mortal hand flinched from '
                                      'her throat.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B07',
                              'speaker': 'Aether',
                              'text': 'I climbed that freezing cliff-altar to pull her back, Your Majesty, '
                                      'and I am not letting go again.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B08',
                              'speaker': 'The Tsaritsa',
                              'text': 'Courage on a cliff rescues a night; it does not mend a fractured '
                                      "Seelie seal before Day Twelve's syzygy. Hear the three judgments my "
                                      'throne permits tonight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B09',
                              'speaker': 'The Tsaritsa',
                              'text': 'First: if she already bound her Moonweave birth-chime to your '
                                      'wrist, and you prove both tender devotion and true knowledge of the '
                                      "False Sky's math, my Cryo authority shall melt that frost-fracture "
                                      'clean and bless your Descender pact.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B10',
                              'speaker': 'The Tsaritsa',
                              'text': 'Second: if you lack the full chain to gamble her mind against '
                                      "heaven's eclipse, yet love her deeply enough to wait out the "
                                      'winter, I will cradle Columbina in gentle camellia Cryo-stasis '
                                      "beside Sandrone's memory-phonograph until spring thaw.",
                              'inner_thought': "Because Sandrone's valves already protect Nasha Town, "
                                               'winter stasis here can shelter Columbina safely without '
                                               'harming a soul!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B11',
                              'speaker': 'The Tsaritsa',
                              'text': 'Or third: refuse both my blessing and my glass sanctuary, and carry '
                                      'her back to Silvermoon Hall on your mortal stubbornness alone.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B12',
                              'speaker': 'Columbina',
                              'text': 'Whichever path you ask of Her Majesty tonight, Aether... I trust '
                                      'the hand that climbed the cliff for me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B13',
                              'speaker': 'Narrator',
                              'text': 'Pale snow-crystals hang suspended in midair around the Cryo '
                                      "Archon's scepter as she awaits my plea.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B14',
                              'speaker': 'The Tsaritsa',
                              'text': 'Answer before the winter stars, Traveler. How shall you love an '
                                      'Angel whom heaven forbade to be loved?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N31_B15',
                              'speaker': 'Narrator',
                              'text': 'Stepping half a pace forward on the frosted marble, I offer my '
                                      'answer at Combination Gate Two.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C18_C_COMBO_GATE2',
                              'combination_gate': True,
                              'prompt': 'COMBINATION GATE II -- Stand before The Tsaritsa and answer for '
                                        "Columbina's fractured veil.",
                              'options': [{'opt_id': 'C18_GATE2_REDEEM',
                                           'label': 'Present your Moonweave bond and celestial proofs '
                                                    'before The Tsaritsa to melt the frost-fracture from '
                                                    "Columbina's veil!",
                                           'unlock_badge': '[COMBO GATE II]',
                                           'lock_hint': '[Needs Ribbon F07 + ((F01+F05, B>=13, I>=9) OR '
                                                        '(F02+F08, B>=11, I>=10))]',
                                           'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                                    'any_of': [{'requires_all': ['F01_HEARD_SILENT_NOTE',
                                                                                 'F05_BRUSHED_MORNING_PLAITS'],
                                                                'min_bond': 13,
                                                                'min_insight': 9},
                                                               {'requires_all': ['F02_FALSE_SKY_CONFIDANT',
                                                                                 'F08_SANDRONE_TEA_FORMULA'],
                                                                'min_bond': 11,
                                                                'min_insight': 10}]},
                                           'effects': {'bond': 2,
                                                       'insight': 2,
                                                       'remove_flags': ['F11_COLD_PROTOCOL'],
                                                       'add_flags': ['F09_DESCENDER_HARMONIC_PACT']},
                                           'next_node': 'N32',
                                           'reaction_beats': [{'beat_id': 'N31_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'As I raise our Moonweave bond '
                                                                       'alongside every quiet truth we '
                                                                       "shared, the Tsaritsa's crystalline "
                                                                       'lashes lower in rare, solemn grace '
                                                                       '-- extending one gloved hand in '
                                                                       'royal benediction.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N31_R_A2',
                                                               'speaker': 'The Tsaritsa',
                                                               'text': 'A warm pulse that heard her unsung '
                                                                       "rest and mapped the sky's "
                                                                       'rebellion... Very well. Let my '
                                                                       'frost lift every fracture of fear '
                                                                       'from her veil -- go, and tear '
                                                                       "heaven's shackle down at "
                                                                       'Silvermoon Hall.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C18_TSARITSA_STASIS_GOOD',
                                           'label': "Entrust Columbina to The Tsaritsa's camellia "
                                                    'Cryo-stasis sanctuary until spring thaw so her '
                                                    'memories stay whole.',
                                           'unlock_badge': '[WINTER SANCTUARY]',
                                           'lock_hint': '[Requires Bond >= 12 and Insight >= 9]',
                                           'when': {'min_bond': 12, 'min_insight': 9},
                                           'effects': {'bond': 0, 'insight': 0},
                                           'next_node': 'N34',
                                           'reaction_beats': [{'beat_id': 'N31_R_B1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Knowing a fractured veil could '
                                                                       'shatter her mind if forced through '
                                                                       "Day Twelve's syzygy unprepared, I "
                                                                       'bow deeply -- and the Tsaritsa '
                                                                       'lowers her lashes gently, lifting '
                                                                       'one gloved hand to summon a warm '
                                                                       'camellia frost-cradle.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N31_R_B2',
                                                               'speaker': 'The Tsaritsa',
                                                               'text': 'A tender restraint is rarer than '
                                                                       'reckless valor, Outlander. Come -- '
                                                                       'my winter glass shall hold her '
                                                                       'memories whole until you open the '
                                                                       'spring.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C18_SOLEMN_RETURN',
                                           'label': 'Decline eternal frost and carry Columbina back to '
                                                    'Silvermoon Hall to face the eclipse together.',
                                           'effects': {'bond': 1, 'insight': 1},
                                           'next_node': 'N33',
                                           'reaction_beats': [{'beat_id': 'N31_R_C1',
                                                               'speaker': 'Aether',
                                                               'text': 'Thank you for suspending the '
                                                                       'Edict, Your Majesty, but '
                                                                       'Silvermoon Hall is her home. Even '
                                                                       'if I have to shield her veil with '
                                                                       'my own two hands, we are going '
                                                                       'back to face the tide together.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N31_R_C2',
                                                               'speaker': 'The Tsaritsa',
                                                               'text': 'Then guard your palms well '
                                                                       'tomorrow night, Fourth Descender. '
                                                                       'My Bore-Rail awaits you at the '
                                                                       'lower gate.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n31_tsaritsa_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N32': {'node_id': 'N32',
                   'chapter_id': 'CH4',
                   'title': 'Rocking Chair Under Returning Snow',
                   'day_label': 'Day 10 - Clear Night, 22:00',
                   'location': 'Silvermoon Hall - Open Courtyard Under Stars',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [24, 1],
                   'beats': [{'beat_id': 'N32_B01',
                              'speaker': 'Narrator',
                              'text': "Returning swiftly via the express bore-rail and Hiisi's coastal "
                                      "waypoint on Day Ten, we step back into Silvermoon Hall's "
                                      'lantern-lit courtyard under a crystal-clear night sky.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B02',
                              'speaker': 'Paimon',
                              'text': 'Aether!! Columbina!! You are back!! Paimon and Luonnotar kept the '
                                      'brazier burning every single night AND saved you the biggest jar of '
                                      'cloudberry jam!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B03',
                              'speaker': 'Narrator',
                              'text': 'After a joyful supper where Sandrone, Arlecchino, Commander Vesna, '
                                      'and Childe report by beacon that all six coastal tide-valves stand '
                                      "ready for tomorrow's eve, quiet settles over the courtyard.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B04',
                              'speaker': 'Narrator',
                              'text': "Back inside Hiisi's rich Kuuvahki embrace, Columbina breathes "
                                      'effortlessly again. Beside the carved stone parapet sits a wide '
                                      'wooden rocking chair draped in a thick wool quilt.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B05',
                              'speaker': 'Columbina',
                              'text': 'Paimon and Luonnotar have already curled up by the warm bricks... '
                                      'Come here, Aether. This rocking chair was built wide enough for two '
                                      'if we share the quilt.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N32_B06',
                              'speaker': 'Narrator',
                              'text': 'Sitting down beside her and drawing the soft wool blanket across '
                                      'both our laps, I feel the wooden runners sway in a slow, lulling '
                                      'arc as she rests her head against my shoulder.',
                              'inner_thought': 'Unfractured, grounded, and home -- twenty-six hours before '
                                               'the syzygy opens.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B07',
                              'speaker': 'Columbina',
                              'text': 'Do you like moongazing like this, Aether? Up on the palace spires, '
                                      'the moon always looked like a cold silver coin... yet from this '
                                      'chair beside you, even its frost feels gentle.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B08',
                              'speaker': 'Aether',
                              'text': 'How does the seam beneath your collarbone feel tonight?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B09',
                              'speaker': 'Columbina',
                              'text': 'Quiet as sleeping water. It knows our grounding pact is waiting for '
                                      'tomorrow midnight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B10',
                              'speaker': 'Columbina',
                              'text': 'When all of this is behind us... promise we will bring this rocking '
                                      'chair up onto the cliff in summer too, with berry tarts on the '
                                      'armrest.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B11',
                              'speaker': 'Aether',
                              'text': 'Every season you want, Columbina.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B12',
                              'speaker': 'Narrator',
                              'text': 'Fine silver snow-crystals drift past the courtyard lanterns as the '
                                      'chair rocks softly beneath the rising frost-moon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N32_B13',
                              'speaker': 'Columbina',
                              'text': 'Stay awake with me a little longer under the quilt... how shall we '
                                      'spend this quiet hour?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C19_ROCKING_CHAIR',
                              'prompt': 'Sharing the quilted rocking chair on Night Ten, choose how you '
                                        'spend this peaceful vigil with Columbina.',
                              'options': [{'opt_id': 'C19_RC_HUM',
                                           'label': 'Rest your forehead lightly against hers and hum the '
                                                    "quiet modulation bridge of tomorrow night's duet "
                                                    'together.',
                                           'effects': {'bond': 2, 'insight': 0},
                                           'next_node': 'N36',
                                           'reaction_beats': [{'beat_id': 'N32_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Resting my brow gently against her '
                                                                       'veiled temple, we hum the soft '
                                                                       'rising bridge in unison until the '
                                                                       'Moonfall Silver lilies around the '
                                                                       'chair glow warm sapphire.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N32_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Mm... my heart did not skip a '
                                                                       'single beat. Tomorrow night, this '
                                                                       'song will carry us all the way '
                                                                       'through.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]},
                                          {'opt_id': 'C19_RC_STARS',
                                           'label': 'Describe the true golden nebulae beyond the False Sky '
                                                    'so her mind holds a clear extra-cosmic anchor for '
                                                    'midnight.',
                                           'effects': {'bond': 0, 'insight': 2},
                                           'next_node': 'N36',
                                           'reaction_beats': [{'beat_id': 'N32_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': "Past Teyvat's glass dome, "
                                                                       'star-nurseries bloom in amber and '
                                                                       'rose clouds ten thousand leagues '
                                                                       'wide -- where no law ever forbade '
                                                                       'an angel to choose one home.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N32_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Amber and rose clouds... I have '
                                                                       'mapped that horizon inside my '
                                                                       'chest, Aether. Tomorrow night, '
                                                                       'show it to my own eyes.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n32_rocking_chair.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N33': {'node_id': 'N33',
                   'chapter_id': 'CH4',
                   'title': 'Fracture in the Sanctum of the Oathbearer',
                   'day_label': 'Day 10 - Late Night, 23:40',
                   'location': 'Hiisi Island - Sanctum of the Oathbearer Altar',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [24, 2],
                   'beats': [{'beat_id': 'N33_B01',
                              'speaker': 'Narrator',
                              'text': 'Twenty minutes before midnight on Day Ten, our return to Hiisi '
                                      'Island is met by a violent pre-eclipse foreshock rumbling beneath '
                                      'the ancient Sanctum of the Oathbearer!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B02',
                              'speaker': 'Narrator',
                              'text': "While Sandrone's coastal valves vent the sea-pressure harmlessly "
                                      'away from Nasha Town, the ungrounded Eclipse Prism hovering above '
                                      "Columbina's birth-spring locks directly onto her unshielded "
                                      'collarbone!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B03',
                              'speaker': 'Columbina',
                              'text': 'Agh --!! Aether, stand back from the basin -- the prism is pulling '
                                      'the seal outward prematurely!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B04',
                              'speaker': 'Narrator',
                              'text': 'Blinding white-gold Seelie lightning arcs from the floating crystal '
                                      'prism straight into the X-lattice veil over her eyes! Two feathers '
                                      'on her hair-wings turn to chalky stone and snap in midair!',
                              'inner_thought': 'Without a completed Zapolyarny theorem, the foreshock is '
                                               'trying to hollow her mind twenty-four hours early!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B05',
                              'speaker': 'Aether',
                              'text': 'Hold onto me, Columbina -- do not let the light drag your focus '
                                      'under!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B06',
                              'speaker': 'Columbina',
                              'text': 'My memories... the afternoon on the shoal... the taste of the '
                                      'berries... it is bleaching white around the edges! Aether -- '
                                      'shatter the Eclipse Prism with your blade!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B07',
                              'speaker': 'Aether',
                              'text': 'What?! If I shatter your birth-prism abruptly without a grounding '
                                      'sink, what happens to the rebound inside your soul?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B08',
                              'speaker': 'Columbina',
                              'text': 'It will sever the calcification before my body crumbles... even '
                                      'if... even if the rebound washes away the name of the one I loved! '
                                      'Cut it down before I turn to dust in front of you!',
                              'inner_thought': 'Shattering the prism saves her physical shell at the cost '
                                               'of every memory of us -- unless my bare hands take the '
                                               'surge!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B09',
                              'speaker': 'Narrator',
                              'text': 'Behind us at the Sanctum arch, Paimon and Commander Vesna sprint in '
                                      'with emergency frost-salve just as the white lightning roars toward '
                                      "Columbina's temples!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B10',
                              'speaker': 'Vesna',
                              'text': 'Do NOT cleave the prism, Traveler!! Cutting the outer crystal makes '
                                      'the Angel Seal scrub every private memory clean into a porcelain '
                                      'Seelie!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B11',
                              'speaker': 'Paimon',
                              'text': 'Aether!! The white crack is touching her chin!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B12',
                              'speaker': 'Narrator',
                              'text': 'White-hot cryo-celestial voltage crackles across the X-lattice veil '
                                      "an arm's length before my dull blade.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B13',
                              'speaker': 'Columbina',
                              'text': 'Please, Aether... strike the crystal and save yourself the burn...!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N33_B14',
                              'speaker': 'Narrator',
                              'text': "In a split second between blade and bare palms, her soul's survival "
                                      'hangs on my move.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C20_BAD2_GATE',
                              'prompt': 'White-gold Seelie lightning arcs from the Sanctum prism toward '
                                        "Columbina's mind -- act at once!",
                              'options': [{'opt_id': 'C20_ABSORB_VEIL',
                                           'label': 'Cast your blade aside and shield her burning '
                                                    'X-lattice veil with your bare Descender hands to take '
                                                    'the frost-bolt yourself!',
                                           'unlock_badge': '[VEIL SHIELD]',
                                           'lock_hint': '[Needs (Ribbon F07 + Vesna Codex, Insight>=10) OR '
                                                        '(Childe Warning, Bond>=12)]',
                                           'when': {'any_of': [{'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                                                 'F06_VESNA_SEELIE_CODEX'],
                                                                'min_insight': 10},
                                                               {'requires_all': ['F03_CHILDE_INSTINCT_HEEDED'],
                                                                'min_bond': 12}]},
                                           'effects': {'bond': 2, 'insight': 1},
                                           'next_node': 'N37',
                                           'reaction_beats': [{'beat_id': 'N33_R_A1_F07',
                                                               'speaker': 'Narrator',
                                                               'text': 'Casting my sword aside, I wrap the '
                                                                       'Moonweave Ribbon Chime tight '
                                                                       'across my bare palms and clamp '
                                                                       'both hands directly over the '
                                                                       'burning X-veil -- driving the '
                                                                       'blistering frost-bolt straight '
                                                                       'into my own Descender arms!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                                                               'voice_emotion': '',
                                                               'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                                                              {'beat_id': 'N33_R_A1_NOF07',
                                                               'speaker': 'Narrator',
                                                               'text': 'Casting my sword aside, I plunge '
                                                                       'both bare hands directly onto the '
                                                                       'burning X-veil -- intercepting the '
                                                                       'blistering frost-bolt through my '
                                                                       'own Descender palms before it can '
                                                                       'touch her mind!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                                                               'voice_emotion': '',
                                                               'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                                                              {'beat_id': 'N33_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Aether -- NO! Your hands -- the '
                                                                       'frost-lightning is searing your '
                                                                       'palms white!!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C20_SHATTER_ALTAR',
                                           'label': 'Strike down the Eclipse Prism to sever the external '
                                                    'surge before calcification reaches her heart.',
                                           'effects': {'bond': 0, 'insight': 0},
                                           'next_node': 'N35',
                                           'reaction_beats': [{'beat_id': 'N33_R_B1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Terrified that another second of '
                                                                       'voltage will crumble her chest to '
                                                                       'stone, I swing my blade cleanly '
                                                                       'through the floating Eclipse Prism '
                                                                       '-- shattering it into a thousand '
                                                                       'silent shards!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N33_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': '...Ah. How quiet... Aether... keep '
                                                                       'holding my name...',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n33_sanctum_fracture.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N34': {'node_id': 'N34',
                   'chapter_id': 'CH4',
                   'title': "Winter's Lullaby Behind Frosted Glass",
                   'day_label': 'Day 10 - Deep Night, 00:15',
                   'location': 'Zapolyarny Palace - Camellia Cryo-Stasis Sanctuary',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [24, 3],
                   'beats': [{'beat_id': 'N34_B01',
                              'speaker': 'Narrator',
                              'text': 'Midnight passes peacefully into fifteen minutes past twelve on Day '
                                      "Ten inside the Tsaritsa's sovereign camellia sanctuary, where "
                                      'luminous blue frost-petals swirl around a tall pavilion of '
                                      'diamond-clear Cryo glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N34_B02',
                              'speaker': 'Sandrone',
                              'text': 'Telegraph from Commander Vesna and Tartaglia on Hiisi Island just '
                                      'printed clean! All six Pulonia hydro-pneumatic valves and Vila '
                                      'pylons are holding steady -- Nasha Town and the Enclave will sail '
                                      "through Day Twelve's eclipse without a ripple!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N34_B03',
                              'speaker': 'Narrator',
                              'text': 'Sandrone sets a finely machined brass wax-cylinder phonograph '
                                      'beside the crystal stasis chamber, alongside a folded crayon-drawn '
                                      'goodnight card couriered north from Paimon and Luonnotar.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N34_B04',
                              'speaker': 'Sandrone',
                              'text': 'Every lullaby variation you hummed this week is etched onto three '
                                      'pure platinum-wax cylinders, Columbina. When we thaw this glass at '
                                      'the spring equinox after the syzygy tide ebbs, not a single note '
                                      'will be missing!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N34_B05',
                              'speaker': 'Columbina',
                              'text': 'Thank you, Sandrone... and tell little Paimon I will bake '
                                      'honey-berry tarts for her the morning the ice melts.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N34_B06',
                              'speaker': 'Narrator',
                              'text': 'Stepping inside the blooming ring of frost-camellias as the '
                                      "Tsaritsa's gentle Cryo veil rises like silver snow, Columbina turns "
                                      'back and presses her bare palm flat against the inner glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N34_B07',
                              'speaker': 'Narrator',
                              'text': 'Immediately, I press my own warm palm directly opposite hers on the '
                                      'outer pane.',
                              'inner_thought': 'Ninety winter days of quiet sleep -- trading haste for '
                                               'certainty so her mind stays 100% whole.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N34_B08_F07',
                              'speaker': 'Narrator',
                              'text': 'Unlooping one end of the Moonweave Ribbon Chime at my wrist, I tie '
                                      'its silver bow onto the crystal latch directly beside our joined '
                                      'palms, where its tiny Luonnotar bell chimes once through the pane.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N34_B08_NOF07',
                              'speaker': 'Narrator',
                              'text': 'Inside the rising camellia frost, the Moonweave Ribbon Chime '
                                      "braided behind Columbina's left ear glints softly like a silver "
                                      'star preserved intact beneath clear glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N34_B09',
                              'speaker': 'Aether',
                              'text': 'Rest easy through the eclipse winter, Columbina. By the time the '
                                      'first snowdrop opens on Hiisi Island, Sandrone and I will have the '
                                      'full Descender counterpoint waiting at your door.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N34_B10',
                              'speaker': 'Columbina',
                              'text': 'Mm... ninety mornings is scarcely a nap for the moon, Aether. Keep '
                                      'knocking on the glass whenever you visit -- even in dreams, my '
                                      'pulse knows the warmth of your hand.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N34_B11',
                              'speaker': 'Narrator',
                              'text': 'Beneath her white X-lattice veil, her lips curve in a serene, '
                                      'trusting smile as crystalline camellias close gently around the '
                                      'chamber, halting the porcelain seam completely.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N34_B12',
                              'speaker': 'Narrator',
                              'text': 'Outside in the quiet conservatory, Sandrone starts the brass '
                                      "phonograph -- letting Columbina's soft lullaby fill the winter "
                                      'night while I keep watch until spring.',
                              'inner_thought': "GOOD ENDING -- Winter's Lullaby Behind Frosted Glass.",
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n34_good_stasis.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_GOOD'},
           'N35': {'node_id': 'N35',
                   'chapter_id': 'CH4',
                   'title': 'Porcelain Seelie of Silvermoon Hall',
                   'day_label': 'Day 11 - Midnight Ruin, 00:15',
                   'location': 'Hiisi Island - Bleached Sanctum Waters',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [25, 4],
                   'beats': [{'beat_id': 'N35_B01',
                              'speaker': 'Narrator',
                              'text': 'Thirty-five minutes after my blade clove the Eclipse Prism -- '
                                      'fifteen minutes into Day Eleven -- dead, windless silence hangs '
                                      'over the shattered basin.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B02',
                              'speaker': 'Narrator',
                              'text': 'Without an extra-cosmic sink to carry the severed surge out of '
                                      'Teyvat, the autonomous Angel Seal rebounded straight across '
                                      "Columbina's memory-threads before extinguishing itself.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B03',
                              'speaker': 'Narrator',
                              'text': 'Every blue Moonfall Silver flower around the water has turned '
                                      'chalk-white, while dozens of tiny, faceless pale-blue Seelie wisps '
                                      'drift mutely above the broken crystal shards.',
                              'inner_thought': 'Her body stopped calcifying -- at the cost of every '
                                               'personal memory her soul ever held.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B04_F07',
                              'speaker': 'Narrator',
                              'text': 'Around my trembling wrist, the Moonweave Ribbon Chime unravels into '
                                      'weightless pale-blue Seelie dust, slipping silently between my '
                                      'fingers into the dark water.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N35_B04_NOF07',
                              'speaker': 'Narrator',
                              'text': "Behind Columbina's ear, the Moonweave Ribbon Chime unravels into "
                                      'weightless pale-blue Seelie dust, drifting away across the '
                                      'colorless petals.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N35_B05',
                              'speaker': 'Paimon',
                              'text': 'C-Columbina...? Hey, look at Paimon -- remember the cloudberries '
                                      "and the honey-bread?! Don't look past us like that... sniff...",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B06',
                              'speaker': 'Narrator',
                              'text': 'On the stone steps behind me, Paimon presses both tiny hands over '
                                      "her mouth, sobbing quietly against Vesna's shoulder as I drop to my "
                                      'knees beside the water.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B07',
                              'speaker': 'Narrator',
                              'text': 'Seated unharmed upon the white stone ledge, Columbina looks '
                                      'immaculate as carved alabaster -- the crack on her collarbone gone, '
                                      'her X-lattice veil spotless and still.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B08',
                              'speaker': 'Aether',
                              'text': 'Columbina... it is me. Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B09',
                              'speaker': 'Columbina',
                              'text': 'Peace be upon your road, golden-haired traveler. Have you come to '
                                      "this shrine seeking the pale moon's guidance across the snow?",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B10',
                              'speaker': 'Narrator',
                              'text': 'Her voice is gentle, luminous, and boundlessly kind to all living '
                                      'things -- yet there is zero recognition of my name, my voice, or '
                                      'the resting measure we once shared.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B11',
                              'speaker': 'Columbina',
                              'text': '...How curious. When I turn toward your voice, a single warm drop '
                                      'falls from beneath my veil, though this spirit recalls no sorrow.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B12',
                              'speaker': 'Columbina',
                              'text': 'Tell me, stranger... why are you crying?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B13',
                              'speaker': 'Narrator',
                              'text': 'Above the bleached white lilies of Silvermoon Hall, she begins '
                                      'humming a hollow, seamless hymn with no silent rest left between '
                                      'the bars -- forever whole in body, and forever lost to us.',
                              'inner_thought': 'BAD ENDING II -- Porcelain Seelie of Silvermoon Hall.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c4_n35_bad2_seelie.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_BAD_2'},
           'N36': {'node_id': 'N36',
                   'chapter_id': 'CH5',
                   'title': 'Barefoot Across Glowing Kuuvahki',
                   'day_label': 'Day 11 - Twilight Eve, 19:30',
                   'location': 'Silvermoon Hall - Luminous Tidal Shallows',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [26, 1],
                   'beats': [{'beat_id': 'N36_B01',
                              'speaker': 'Narrator',
                              'text': 'Four and a half hours before the decennial lunar eclipse opens Day '
                                      "Twelve, Silvermoon Hall's inner lagoon shimmers like liquid "
                                      'starlight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B02',
                              'speaker': 'Paimon',
                              'text': 'Sandrone and Vesna just flashed three green lantern signals from '
                                      'the bluff! Every tide-valve and perimeter stake around Hiisi Island '
                                      'is locked at 100 percent!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B03',
                              'speaker': 'Narrator',
                              'text': 'Perched atop a mossy boulder beside Paimon, little Luonnotar taps a '
                                      'tiny silver-wire tambourine in gentle three-quarter time as '
                                      'Columbina steps into the ankle-deep glowing shallows.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B04',
                              'speaker': 'Columbina',
                              'text': 'Unlace your heavy travel boots for a little while, Aether... On the '
                                      "eve of syzygy, Kuuvahki carries a singer's pulse clearest through "
                                      'bare soles.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': 'outing_arrive_photo'},
                             {'beat_id': 'N36_B05',
                              'speaker': 'Narrator',
                              'text': "Setting my boots beside Paimon's basket, I wade barefoot across the "
                                      "surprisingly warm, bioluminescent shallows to take Columbina's "
                                      'outstretched hands.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B06',
                              'speaker': 'Narrator',
                              'text': 'Where our steps meet, blue-silver ripples twine with threads of '
                                      'pale outlander gold, lifting weightless droplets into the cavern '
                                      'air like reverse rain.',
                              'inner_thought': 'Four hours to midnight -- every breath we align now builds '
                                               'the runway for Somnias Duetto.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B07',
                              'speaker': 'Columbina',
                              'text': "Five hundred years ago, I stepped out of this pool knowing nobody's "
                                      'name... Tonight, every drop under my heels knows yours.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B08',
                              'speaker': 'Aether',
                              'text': 'Are you afraid of what happens when we untie the veil at midnight?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B09',
                              'speaker': 'Columbina',
                              'text': 'A little... my eyelashes have forgotten how heavy real light feels. '
                                      "Yet if your hands hold the bridge, even heaven's thunder looks "
                                      'small.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B10',
                              'speaker': 'Paimon',
                              'text': 'Go on, you two! Luonnotar is holding the tempo for your final '
                                      'warm-up!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B11',
                              'speaker': 'Narrator',
                              'text': 'Rings of azure light spiral outward from our bare ankles as the '
                                      "water's harmonic tension rises toward its pre-midnight crest.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B12',
                              'speaker': 'Columbina',
                              'text': 'Lead this last rehearsal across the tide, Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N36_B13',
                              'speaker': 'Narrator',
                              'text': 'Clasping both her hands over the glowing lagoon, I choose how we '
                                      'tune the final hours before midnight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C21_EVE_MAIN',
                              'prompt': 'Standing barefoot in the glowing Kuuvahki tide on Eclipse Eve, '
                                        'align your final preparation.',
                              'options': [{'opt_id': 'C21_PACT_HARMONY',
                                           'label': 'Weave your intimate trust and celestial '
                                                    'counter-harmony into one effortless pre-midnight '
                                                    'chord across the glowing tide.',
                                           'unlock_badge': '[HARMONIC PACT]',
                                           'lock_hint': '[Needs (Descender Pact F09 + Morning Plaits F05) '
                                                        'OR (Tea Formula F08 + Shared Lullaby F04)]',
                                           'when': {'any_of': [{'requires_all': ['F09_DESCENDER_HARMONIC_PACT',
                                                                                 'F05_BRUSHED_MORNING_PLAITS']},
                                                               {'requires_all': ['F08_SANDRONE_TEA_FORMULA',
                                                                                 'F04_KUUHENKI_LULLABY_SHARED']}]},
                                           'effects': {'bond': 2, 'insight': 2},
                                           'next_node': 'N38',
                                           'reaction_beats': [{'beat_id': 'N36_R_A1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Weaving our intimate morning trust '
                                                                       'and mathematical counter-harmony '
                                                                       'into one effortless phrase, a '
                                                                       'pillar of gentle gold-and-azure '
                                                                       'mist rises from our joined hands '
                                                                       'without a trace of strain!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N36_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': '...Flawless. Every note between '
                                                                       'your stars and my tide is ready '
                                                                       'for midnight.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]},
                                          {'opt_id': 'C21_QUIET_PRAYER',
                                           'label': 'Hold her hands in quiet stillness so she saves every '
                                                    'breath for midnight.',
                                           'effects': {'bond': 0, 'insight': 1},
                                           'next_node': 'N38',
                                           'reaction_beats': [{'beat_id': 'N36_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Save your voice until the eclipse '
                                                                       'opens, Columbina. Just stand in '
                                                                       'the warm current with me and let '
                                                                       'my pulse steady yours.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N36_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Always so careful with me... Very '
                                                                       'well, let us listen to the rising '
                                                                       'tide together.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n36_barefoot_tide.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N37': {'node_id': 'N37',
                   'chapter_id': 'CH5',
                   'title': 'Singed Palms & Whispered Apology',
                   'day_label': 'Day 11 - Night, 21:00',
                   'location': 'Silvermoon Hall - Warm Waterside Alcove',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'flowchart_pos': [26, 2],
                   'pre_events': [{'when': {'requires_all': ['F11_COLD_PROTOCOL',
                                                             'F07_MOONWEAVE_RIBBON_CHIME',
                                                             'F03_CHILDE_INSTINCT_HEEDED',
                                                             'F06_VESNA_SEELIE_CODEX'],
                                            'min_bond': 15,
                                            'min_insight': 11},
                                   'effects': {'remove_flags': ['F11_COLD_PROTOCOL'],
                                               'add_flags': ['F11_REDEEMED_N37']}}],
                   'beats': [{'beat_id': 'N37_B01',
                              'speaker': 'Narrator',
                              'text': 'Three hours before the midnight syzygy on Day Eleven, Commander '
                                      'Vesna and Paimon finish wrapping clean linen steeped in Snowland '
                                      'Fae herb-salve around both of my frost-singed palms.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B02',
                              'speaker': 'Paimon',
                              'text': 'Ouch, ouch... even looking at those white frost-blisters makes '
                                      'Paimon wince! Thank goodness your outlander constitution kept the '
                                      'lightning out of your bones, Aether!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B03',
                              'speaker': 'Vesna',
                              'text': "Your bare hands saved Lady Columbina's memories from being wiped "
                                      'clean at the Sanctum last night, Traveler. I must return to my Vila '
                                      "pylons on the bluff now -- Sandrone's valves are holding Nasha Town "
                                      'safe!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B04',
                              'speaker': 'Narrator',
                              'text': 'Once Vesna departs and Paimon hurries to brew warm ginger tea by '
                                      'the brazier, Columbina kneels silently beside me on the mossy '
                                      'stone, lifting my bandaged hands with trembling reverence.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B05_F07',
                              'speaker': 'Narrator',
                              'text': 'Wound over the white linen at my right wrist, the silver Moonweave '
                                      'Ribbon Chime bears a faint scorch-frost patina from channeling half '
                                      "of last night's bolt -- yet its little Luonnotar bell still rings "
                                      'clear.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N37_B05_NOF07',
                              'speaker': 'Narrator',
                              'text': 'Without the Moonweave Ribbon Chime on my wrist to diffuse last '
                                      "night's bolt, my linen wraps took the full raw bite -- while the "
                                      'silver bell in her hair chimes softly above my knuckles.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N37_B06',
                              'speaker': 'Columbina',
                              'text': 'Look what protecting a cursed Angel did to your hands, Aether... I '
                                      "begged you to cut the prism down, yet you took heaven's white iron "
                                      'straight across your skin.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B07',
                              'speaker': 'Aether',
                              'text': 'Blisters heal in a week, Columbina. Watching you forget my name '
                                      'across that pool would never have healed.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B08',
                              'speaker': 'Narrator',
                              'text': 'Pressing her cheek gently against the back of my bandaged knuckles, '
                                      'Columbina lets a single hot tear slip from beneath the lower edge '
                                      'of her white X-veil onto the gauze.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B09_PENANCE',
                              'speaker': 'Narrator',
                              'text': 'Where her warm tear meets my scorched Moonweave ribbon and '
                                      'Fae-salved gauze, a soft golden-silver glow blooms -- melting away '
                                      'the last hairline frost-fracture that my earlier recoil had left '
                                      'upon her X-veil!',
                              'inner_thought': 'Blood-Frost Penance -- shielding her veil with my bare '
                                               'hands just healed every trace of past hesitation!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_REDEEMED_N37']}},
                             {'beat_id': 'N37_B09_STILL_F11',
                              'speaker': 'Narrator',
                              'text': 'Yet even as her warm tear darkens my bandage, I see the thin '
                                      'hairline frost-fracture from my earlier recoil still spiderwebbing '
                                      'across the temple-knot of her X-veil -- dangerously close to its '
                                      'limit.',
                              'inner_thought': "Even after last night's rescue, that unhealed hairline "
                                               'crack makes untying her veil tonight lethal.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N37_B09_CLEAN',
                              'speaker': 'Narrator',
                              'text': "Beneath the cavern's soft azure glow, her X-lattice veil holds "
                                      'unbroken above my bandaged fingers as our heartbeats settle into '
                                      'quiet alignment.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F11_COLD_PROTOCOL', 'F11_REDEEMED_N37']}},
                             {'beat_id': 'N37_B10',
                              'speaker': 'Columbina',
                              'text': 'Even through linen, your palms are still warmer than any hearth I '
                                      'have ever known...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N37_B11',
                              'speaker': 'Aether',
                              'text': 'Midnight is less than three hours away. Lean on me while the tide '
                                      'rises to the central platform.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N37_B12',
                              'speaker': 'Narrator',
                              'text': 'Fingers intertwined carefully around my bandages, we walk together '
                                      'toward the center of Silvermoon Hall to meet the eclipse.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n37_singed_palms.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N38'}],
                   'ending_id': None},
           'N38': {'node_id': 'N38',
                   'chapter_id': 'CH5',
                   'title': 'The False Sky Ripples at Midnight',
                   'day_label': 'Day 11 - Eclipse Vigil, 23:50',
                   'location': 'Silvermoon Hall - Central Oculus Tide-Ring',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [27, 2],
                   'beats': [{'beat_id': 'N38_B01',
                              'speaker': 'Narrator',
                              'text': 'At ten minutes before midnight on Day Eleven, every wind across '
                                      "Hiisi Island drops dead still. Through Silvermoon Hall's open "
                                      'ceiling oculus, the shadow of the decennial eclipse creeps across '
                                      'the Frost Moon!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B02',
                              'speaker': 'Narrator',
                              'text': "High above the clouds, Teyvat's painted firmament shivers -- "
                                      'concentric translucent ripples spreading across the False Sky like '
                                      'a struck mirror of dark glass!',
                              'inner_thought': 'The perigee syzygy is pulling directly at the seam between '
                                               "Teyvat's shell and the abyss of real stars!",
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B03',
                              'speaker': 'Paimon',
                              'text': 'W-Whoa!! Look straight up through the ceiling ring, Aether -- the '
                                      'stars look like they are rippling on water! Paimon and Luonnotar '
                                      'will hold the lantern barrier back by the arch!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B04',
                              'speaker': 'Narrator',
                              'text': 'Out in the center of the flooded hall, luminous blue Kuuvahki rises '
                                      'into a zero-gravity ring of floating silver droplets around '
                                      'Columbina and me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B05',
                              'speaker': 'Narrator',
                              'text': 'As the eclipse shadow nears totality, a blinding geometric halo of '
                                      'gold-and-alabaster runes -- the primordial Seal of the Seelie Court '
                                      "-- ignites across Columbina's white X-lattice veil!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B06',
                              'speaker': 'Columbina',
                              'text': "Ngh... there it is. Heaven's final audit has arrived right on "
                                      "Sandrone's minute-hand, Aether.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B07',
                              'speaker': 'Aether',
                              'text': 'I have you, Columbina! Keep your feet inside my gravity ring -- do '
                                      'not let the updraft pull you back!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B08',
                              'speaker': 'Narrator',
                              'text': 'Six radiant translucent moon-wings flare half-open behind her '
                                      'shoulders, straining against golden chains of celestial static that '
                                      'hiss whenever her heartbeat calls my name.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B09',
                              'speaker': 'Columbina',
                              'text': 'Feel how fiercely the seal pulls at my temples... Because my heart '
                                      "already chose you alone, twelve o'clock will force one of two fates "
                                      'upon this veil.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B10',
                              'speaker': 'Columbina',
                              'text': 'If our Moonweave conduit, unfractured trust, and harmonic truth are '
                                      'complete, untying this veil will pour the entire execution surge '
                                      'out past that rippling sky...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B11',
                              'speaker': 'Columbina',
                              'text': 'Otherwise, we must hold the X-lattice tied fast and weather the '
                                      'surge half-blind until dawn -- surviving behind gauze rather than '
                                      'gambling my mind.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B12',
                              'speaker': 'Narrator',
                              'text': "Far along the outer cliffs, Sandrone's valves boom once in deep "
                                      'bass unison as the eclipse shadow swallows the final silver '
                                      'crescent overhead.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B13',
                              'speaker': 'Narrator',
                              'text': 'Clock-chimes of ancient ice toll midnight across Nod-Krai as Day '
                                      'Twelve begins.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N39'}],
                   'ending_id': None},
           'N39': {'node_id': 'N39',
                   'chapter_id': 'CH5',
                   'title': 'Final Gate: Gaze Beneath the Moonweave Veil',
                   'day_label': 'Day 12 - Eclipse Apex, 00:00',
                   'location': 'Silvermoon Hall - Zero-Hour Syzygy Epicenter',
                   'bgm_bucket': 'vn_mystic_tension',
                   'flowchart_pos': [28, 2],
                   'beats': [{'beat_id': 'N39_B01',
                              'speaker': 'Narrator',
                              'text': 'Zero-zero-hundred hours, Day Twelve. Totality locks the Frost Moon '
                                      'into a corona of pale rose-silver directly above the oculus!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B02',
                              'speaker': 'Narrator',
                              'text': 'Every droplet of water inside Silvermoon Hall hangs motionless in '
                                      'midair around us as the golden Seelie seal blazes to critical '
                                      "asymptote across Columbina's brow!",
                              'inner_thought': "Sandrone's midnight asymptote is here -- twelve seconds to "
                                               'commit our entire twelve-day journey!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B03',
                              'speaker': 'Columbina',
                              'text': 'Aether... my fingers are on the knot of my veil!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B04',
                              'speaker': 'Narrator',
                              'text': 'Standing ankle-to-ankle on the mirrored surface of the pool, '
                                      'Columbina lifts one trembling hand to the silk knot behind her '
                                      'temple while extending her other hand straight into mine.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B05',
                              'speaker': 'Columbina',
                              'text': 'Tell me what your outlander eyes see in our bond right now, my '
                                      'star!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B06',
                              'speaker': 'Aether',
                              'text': 'I am right in front of you, Columbina -- feel my core!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B07',
                              'speaker': 'Columbina',
                              'text': 'If my Moonweave Ribbon Chime binds our wrists without a single cold '
                                      'fracture left on my veil -- and our harmony holds -- sing Somnias '
                                      'Duetto with me and let me open my eyes for you alone!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B08',
                              'speaker': 'Columbina',
                              'text': 'Or if even one link is missing, hold my veil shut against your '
                                      'chest and let us ride out the storm alive!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B09',
                              'speaker': 'Narrator',
                              'text': 'Above the oculus, the False Sky ripples thin as gossamer -- '
                                      "exposing a pinhole of real, untamed starlight beyond Teyvat's "
                                      'shell!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B10',
                              'speaker': 'Paimon',
                              'text': 'Whatever you choose, Aether -- do it right on the downbeat!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B11',
                              'speaker': 'Narrator',
                              'text': "Golden celestial static roars down the shaft as Columbina's pulse "
                                      'pounds through my palm.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B12',
                              'speaker': 'Columbina',
                              'text': 'Now, Aether -- guide my hands!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N39_B13',
                              'speaker': 'Narrator',
                              'text': 'At the final causal gate of Somnias a Luna, I make our ultimate '
                                      'choice.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C22_FINAL',
                              'combination_gate': True,
                              'prompt': 'FINAL ECLIPSE GATE (00:00) -- Untie the Seelie veil in Somnias '
                                        'Duetto, or hold it fast against the storm?',
                              'options': [{'opt_id': 'C22_UNVEIL_TRUE_DUET',
                                           'label': 'Bind your Moonweave conduit, sing Somnias Duetto past '
                                                    'the False Sky, and let Columbina untie her veil for '
                                                    'you alone!',
                                           'unlock_badge': '[TRUE DUET]',
                                           'lock_hint': '[Needs Ribbon F07, No Cold Fracture F11, & '
                                                        '(B>=18,I>=11 or B>=15,I>=15 or Pact '
                                                        'F09+B>=13,I>=13)]',
                                           'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                                    'forbid_flags': ['F11_COLD_PROTOCOL'],
                                                    'any_of': [{'min_bond': 18, 'min_insight': 11},
                                                               {'min_bond': 15, 'min_insight': 15},
                                                               {'requires_all': ['F09_DESCENDER_HARMONIC_PACT'],
                                                                'min_bond': 13,
                                                                'min_insight': 13}]},
                                           'effects': {'bond': 0, 'insight': 0},
                                           'next_node': 'N40',
                                           'reaction_beats': [{'beat_id': 'N39_R_A1',
                                                               'speaker': 'Aether',
                                                               'text': 'Our Moonweave bridge is whole and '
                                                                       'not a trace of fear stands between '
                                                                       'us! Untie the knot on my count, '
                                                                       'Columbina -- we are singing '
                                                                       'Somnias Duetto straight past the '
                                                                       'False Sky!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N39_R_A2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Yes -- take every note of my soul, '
                                                                       'my Fourth Star!!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C22_KEEP_VEIL_TIED',
                                           'label': 'Keep the X-lattice veil tied tight and weather the '
                                                    'midnight surge without risking her mind.',
                                           'effects': {'bond': 0, 'insight': 0},
                                           'next_node': 'N44',
                                           'reaction_beats': [{'beat_id': 'N39_R_B1',
                                                               'speaker': 'Aether',
                                                               'text': 'Keep the knot tied fast tonight, '
                                                                       'Columbina! Lean straight into my '
                                                                       'arms -- I will never gamble your '
                                                                       'mind before every link is ready!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N39_R_B2',
                                                               'speaker': 'Columbina',
                                                               'text': 'Hold me tight through the surge, '
                                                                       'Aether -- here it comes!!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N40': {'node_id': 'N40',
                   'chapter_id': 'CH5',
                   'title': 'Somnias Duetto: Unrecorded Star',
                   'day_label': 'Day 12 - Syzygy Duet, 00:05',
                   'location': 'Silvermoon Hall - Mirrored Gravity Ring',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [29, 1],
                   'beats': [{'beat_id': 'N40_B01',
                              'speaker': 'Narrator',
                              'text': 'Stepping boldly onto the unyielding mirror of the lagoon, I loop '
                                      'the trailing end of the Moonweave Ribbon Chime from my wrist '
                                      "straight around Columbina's left pulse -- binding our arteries with "
                                      'luminous moon-silk!',
                              'inner_thought': 'Physical Kuuvahki conduit locked; unfractured devotion '
                                               'steady; original Fourth Descender core wide open!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B02',
                              'speaker': 'Columbina',
                              'text': 'Somnias a luna... hear the dove whom winter could not cage...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B03',
                              'speaker': 'Narrator',
                              'text': 'As her soaring soprano opens the forbidden solo dedication -- '
                                      'singing openly, unmistakably for one chosen soul alone -- the '
                                      'ancient Angel Seal inside her chest detonates with ten thousand '
                                      'winters of white calcification!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B04',
                              'speaker': 'Narrator',
                              'text': "Where Koitar's surge once hit a borrowed mortal shell and rebounded "
                                      'into ash, the lethal wave races across our Moonweave Ribbon Chime '
                                      'straight into my original Fourth Descender vessel!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B05',
                              'speaker': 'Aether',
                              'text': 'Out beyond the painted glass -- GO!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B06',
                              'speaker': 'Narrator',
                              'text': 'Entering right on her eighth-measure silent rest at 13.7 kilohertz, '
                                      'my outlander counterpoint phase-inverts the execution bolt -- '
                                      'siphoning every shred of white porcelain frost out of her '
                                      'collarbone and through my star-lit chest!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B07',
                              'speaker': 'Narrator',
                              'text': 'A spiral column of intertwined azure Kuuvahki and golden Descender '
                                      'starlight erupts straight upward through the ceiling oculus, '
                                      "piercing the rippling False Sky and venting heaven's entire curse "
                                      'harmlessly into the boundless cosmos beyond!',
                              'inner_thought': 'With no closed Irminsul loop to rebound off, five '
                                               'millennia of celestial punishment disperse into starlight!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B08',
                              'speaker': 'Paimon',
                              'text': 'LOOK AT HER COLLARBONE, LUONNOTAR!! The white porcelain crack just '
                                      'vanished completely!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B09',
                              'speaker': 'Narrator',
                              'text': 'With a crystalline chime heard across every shoal of Hiisi Island, '
                                      "the golden chains around Columbina's six radiant moon-wings shatter "
                                      'into warm, harmless motes of falling gold!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B10',
                              'speaker': 'Columbina',
                              'text': 'Ah... my chest... the frost is gone, Aether! Every memory -- every '
                                      'berry, every raindrop, every word you ever whispered -- is warm and '
                                      'crystal-clear!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N40_B11',
                              'speaker': 'Narrator',
                              'text': 'All around our bare ankles, thousands of Moonfall Silver lilies '
                                      'burst into triumphant, luminous sapphire bloom as the floating '
                                      'water droplets rain gently back into the pool.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B12',
                              'speaker': 'Aether',
                              'text': 'The shackle is gone forever, Columbina. Not a fragment of it '
                                      'remains inside your soul.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B13',
                              'speaker': 'Narrator',
                              'text': 'Breathing softly in the silver stillness of the cleansed hall, '
                                      'Columbina raises both unblemished hands to the knot of her eye '
                                      'mask.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n40_somnias_duetto.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N41'}],
                   'ending_id': None},
           'N41': {'node_id': 'N41',
                   'chapter_id': 'CH5',
                   'title': 'Lotus-Pink Eyes of the New Moon',
                   'day_label': 'Day 12 - Unveiling, 00:12',
                   'location': 'Silvermoon Hall - Heart of the Cleansed Lagoon',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [30, 1],
                   'beats': [{'beat_id': 'N41_B01',
                              'speaker': 'Narrator',
                              'text': 'Bound between our joined wrists, the Moonweave Ribbon Chime rings '
                                      'one last crystalline note across the hushed waters of Silvermoon '
                                      'Hall. With fingers that no longer flake into porcelain dust, '
                                      'Columbina reaches up and unties the white X-lattice veil from her '
                                      'temples.',
                              'inner_thought': 'The golden Seelie seal has dissolved into starlight -- '
                                               'nothing stands above us now.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_closed_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B02',
                              'speaker': 'Columbina',
                              'text': "For five hundred winters, I veiled my sight from Teyvat's painted "
                                      'sky, guided only by a nameless dread... never knowing until this '
                                      'week that heaven swore to burn my mind to ash the instant I opened '
                                      'my eyes for one beloved soul.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_closed_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B03',
                              'speaker': 'Narrator',
                              'text': 'I catch the unbound white veil gently as it drifts from her '
                                      'temples, holding her steady on the mirrored tide without looking '
                                      'away.',
                              'inner_thought': "Light as a shed dove's feather, the moon-woven gauze "
                                               'settles across my open palm.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_closed_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B04',
                              'speaker': 'Aether',
                              'text': 'Heaven has no ledger for a traveler from beyond the stars, '
                                      'Columbina. Look at me -- nothing in this world or beyond it can '
                                      'take your name or your memories tonight.',
                              'inner_thought': 'No law etched into Irminsul can claim what belongs beyond '
                                               'the stars.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_closed_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B05',
                              'speaker': 'Narrator',
                              'text': 'Slowly, tremulously, her long dark lashes lift. Beneath them awaken '
                                      'irises of translucent lotus-pink, cradling soft pale-blue crescent '
                                      'highlights clearer than the sea of Kuuvahki -- gazing straight into '
                                      'my eyes without a single crack, shadow, or veil between us.',
                              'inner_thought': 'For the space of a single heartbeat, even the tide of '
                                               'Silvermoon Hall forgets to breathe.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_open_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B06',
                              'speaker': 'Columbina',
                              'text': '...Ah. So this is the exact shade of gold your eyes hold when you '
                                      'smile at me, Aether. Stay close a little longer, please -- I have '
                                      'five hundred winters of unseen light to gather in your gaze, and I '
                                      'refuse to blink.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_open_diff.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N41_B07',
                              'speaker': 'Narrator',
                              'text': 'Luminous lotus-pink eyes shimmering with unshed silver dew, she '
                                      'lifts one warm palm to trace my brow, my nose, and the golden lock '
                                      'beside my cheek -- marveling like a painter seeing color for the '
                                      'first time.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_open_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B08',
                              'speaker': 'Aether',
                              'text': 'Five hundred winters was a long wait... Welcome to the light, '
                                      'Columbina.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_open_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B09',
                              'speaker': 'Columbina',
                              'text': 'Even the blue flowers look softer than Kuuvahki ever told me... yet '
                                      'I cannot seem to look at anything except you.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_open_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B10',
                              'speaker': 'Paimon',
                              'text': "Waaah!! Columbina's eyes are the prettiest lotus-pink Paimon has "
                                      "ever seen!! Luonnotar, stop spinning loops around Paimon's head or "
                                      'Paimon is gonna cry happy tears!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_open_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B11',
                              'speaker': 'Columbina',
                              'text': 'Hehe... so the starry navy scarf really is midnight-blue, little '
                                      'finch. I will never misplace its color again.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_open_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B12',
                              'speaker': 'Columbina',
                              'text': 'Hold my hand, Aether -- while the syzygy updraft still lingers '
                                      "above the oculus, let me carry you somewhere higher than Teyvat's "
                                      'clouds before dawn.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_open_diff.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B13',
                              'speaker': 'Narrator',
                              'text': 'Six radiant white wings unfurl behind her in clean, unburdened '
                                      'splendor, lifting us effortlessly through the open stone ring into '
                                      'the night sky.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n41_eyes_open_diff.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N42'}],
                   'ending_id': None},
           'N42': {'node_id': 'N42',
                   'chapter_id': 'CH5',
                   'title': 'Cleansed Feathers Over Hiisi Dawn',
                   'day_label': 'Day 12 - Pre-Dawn, 04:30',
                   'location': 'High Lunar Cloud-Sea Above Nod-Krai',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [31, 1],
                   'beats': [{'beat_id': 'N42_B01',
                              'speaker': 'Narrator',
                              'text': "High above Nod-Krai's coastal storm-deck in the tranquil silver "
                                      'cloud-sea of her Lunar Domain, the first faint rose of pre-dawn '
                                      'tints the eastern horizon at half past four.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B02',
                              'speaker': 'Narrator',
                              'text': 'Floating weightlessly amid drifting ribbons of pearl-white cloud, '
                                      'Columbina gazes out across the curvature of the sleeping world with '
                                      'wide, unveiled lotus-pink eyes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B03',
                              'speaker': 'Columbina',
                              'text': "Look down there, Aether... Nasha Town's harbor lamps are waking one "
                                      'by one, and the tide around Hiisi is calm as glass.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B04',
                              'speaker': 'Aether',
                              'text': 'No altar petitions below, and no Harbinger decree behind you. What '
                                      'name does the New Moon choose for herself this morning?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B05',
                              'speaker': 'Columbina',
                              'text': 'Not Number Three, and not an idol bound to stone... Call me '
                                      'Columbina Hyposelenia -- the little dove who belongs beneath the '
                                      'moon and beside her wandering star.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N42_B06',
                              'speaker': 'Narrator',
                              'text': 'Turning back toward me in the silver-rose glow, she cradles both '
                                      'sides of my face in palms that are no longer cold porcelain, but '
                                      'living, gentle warmth.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B07',
                              'speaker': 'Columbina',
                              'text': 'You filled the silent half-measure of my cradle-song, Aether. May I '
                                      'claim one quiet beat of my own before sunrise?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B08',
                              'speaker': 'Aether',
                              'text': 'Every measure is yours, Columbina.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B09',
                              'speaker': 'Narrator',
                              'text': 'Rising half an inch on her luminous wings while the Moonweave '
                                      'Ribbon Chime sings softly between our wrists, Columbina leans in '
                                      'and presses a tender, breathless first kiss to my lips beneath the '
                                      'fading frost-moon.',
                              'inner_thought': 'Soft as winter camellias and warm as dawn -- five '
                                               'centuries of solitude melting away in a single breath.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B10',
                              'speaker': 'Narrator',
                              'text': 'When we part by a whisper, her lotus-pink eyes shine brighter than '
                                      'the morning star, cheeks flushed the exact rose of early sunrise.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B11',
                              'speaker': 'Columbina',
                              'text': 'Come... Sandrone and the others will be marching up to Silvermoon '
                                      'Hall with tea kettles by evening, and it is time I rolled that '
                                      'front boulder aside for good.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B12',
                              'speaker': 'Narrator',
                              'text': 'Hand in hand through golden-pink daybreak, we glide down from the '
                                      'cloud-sea toward home.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n42_moon_kiss_dawn.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N43'}],
                   'ending_id': None},
           'N43': {'node_id': 'N43',
                   'chapter_id': 'CH5',
                   'title': 'Somnias a Luna: Home Beneath Both Skies',
                   'day_label': 'Day 12 - Moonlit Evening, 19:30',
                   'location': 'Silvermoon Hall - Open Lantern Courtyard',
                   'bgm_bucket': 'vn_tender_romance',
                   'flowchart_pos': [32, 1],
                   'beats': [{'beat_id': 'N43_B01',
                              'speaker': 'Narrator',
                              'text': 'That evening on Day Twelve, the heavy moss-stone boulder that once '
                                      "sealed Silvermoon Hall's outer threshold stands rolled wide open to "
                                      'the sea-breeze for the first time in centuries.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B02',
                              'speaker': 'Narrator',
                              'text': 'Under strings of warm courtyard lanterns surrounded by thriving '
                                      "azure Moonfall Silver lilies, Sandrone's grand tea table overflows "
                                      'with cloudberry mille-feuille, honey-bread, and steaming samovars.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B03',
                              'speaker': 'Sandrone',
                              'text': 'Careful with that third tier of pastry plates, Tartaglia! Honestly '
                                      '-- I calibrate six flawless coastal valves and still end up '
                                      'catering for half of Snezhnaya!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B04',
                              'speaker': 'Tartaglia',
                              'text': 'Hahaha! Come on, Lady Sandrone, even The Knave brought Fontinalia '
                                      'black tea! Besides, seeing Columbina look people straight in the '
                                      'eye without freezing the pier is worth celebrating!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B05',
                              'speaker': 'Arlecchino',
                              'text': 'A clean victory over an archaic celestial law deserves decent tea '
                                      'leaves. Keep her cup warm, Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B06',
                              'speaker': 'Vesna',
                              'text': 'May the Snowland Fae remember tonight in golden ink -- the first '
                                      "Angel since Koitar's age to love freely with open eyes and unbroken "
                                      'wings!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B07',
                              'speaker': 'Paimon',
                              'text': 'Hey!! Save two berry tarts for Paimon before Luonnotar and the '
                                      'Kuuhenki spirit them off the platter!!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B08',
                              'speaker': 'Narrator',
                              'text': 'At the head of the warm stone bench beside me sits Columbina -- her '
                                      'X-veil gone forever, lotus-pink eyes sparkling with soft laughter '
                                      'while her Moonweave Ribbon Chime is braided together with a strand '
                                      'of my golden scarf-silk in her hair.',
                              'inner_thought': 'Rootless grass no longer -- she has a name, open eyes, '
                                               'friends at her table, and a home beside me.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B09',
                              'speaker': 'Columbina',
                              'text': 'Here, Aether -- I saved the sweetest frost-berry on the plate for '
                                      'you.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N43_B10',
                              'speaker': 'Aether',
                              'text': 'No lonely rest between the bars anymore?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N43_B11',
                              'speaker': 'Columbina',
                              'text': 'Never again. Wherever your road leads beneath this painted sky or '
                                      'out among your true stars... my lullaby walks beside its second '
                                      'voice forever.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N43_B12',
                              'speaker': 'Narrator',
                              'text': 'Leaning her head warmly against my shoulder beneath the open '
                                      'moonlit arch, Columbina hums a joyous new duet as silver '
                                      "bell-chimes and laughter carry far across Hiisi's peaceful sea.",
                              'inner_thought': 'TRUE ENDING -- Somnias a Luna: Home Beneath Both Skies.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n43_true_tea_party.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_TRUE'},
           'N44': {'node_id': 'N44',
                   'chapter_id': 'CH5',
                   'title': 'Through the Moonlight Veil',
                   'day_label': 'Day 12 - Quiet Dawn, 05:30',
                   'location': 'Silvermoon Hall - Post-Eclipse Dawn',
                   'bgm_bucket': 'vn_melancholy_memory',
                   'flowchart_pos': [29, 3],
                   'beats': [{'beat_id': 'N44_44A_B01',
                              'speaker': 'Narrator',
                              'text': "At 00:00 totality, I wrap both arms firmly around Columbina's "
                                      'shoulders over her tied X-lattice veil while the Moonweave Ribbon '
                                      'Chime on my wrist blazes silver-gold against the eclipse surge!',
                              'inner_thought': 'Without risking an unveiling yet, the Moonweave bridge '
                                               'still lets me siphon half the midnight pressure!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B02',
                              'speaker': 'Columbina',
                              'text': 'Ngh... hold my wrist steady, Aether! Keep the knot closed until the '
                                      'moon clears the shadow!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B03',
                              'speaker': 'Narrator',
                              'text': "Outside along the shoals, Sandrone's six Pulonia tide-valves and "
                                      "Vesna's pylons vent the oceanic Kuuvahki safely away from Nasha "
                                      'Town while my Descender palm grounds the excess sparks off her '
                                      'ribbon!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B04',
                              'speaker': 'Narrator',
                              'text': 'Twelve tense minutes past midnight, the False Sky stops rippling. '
                                      'Though the Seelie seal remains unbroken beneath her veil, its '
                                      'lethal asymptote subsides into dormancy as totality passes!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B05',
                              'speaker': 'Narrator',
                              'text': 'By half past five in the quiet blue dawn, pale morning light '
                                      "filters across Silvermoon Hall's courtyard where Paimon and "
                                      'Luonnotar sleep curled beside a warm teapot.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B06',
                              'speaker': 'Narrator',
                              'text': 'Seated beside me on the wooden rocking chair beneath a shared wool '
                                      'blanket, Columbina breathes peacefully -- the white X-lattice veil '
                                      'still tied securely across her closed eyes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B07',
                              'speaker': 'Narrator',
                              'text': 'Carefully unknotting the slightly frost-singed Moonweave Ribbon '
                                      'Chime from my wrist, I braid it back behind her left ear so its '
                                      'silver Luonnotar bell rests warm against her curls.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B08',
                              'speaker': 'Columbina',
                              'text': 'My little bell smells of your starlight now, Aether... Even with '
                                      'this gauze still between us, not a single memory of our week was '
                                      'lost.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B09',
                              'speaker': 'Aether',
                              'text': 'I am sorry we had to keep the veil tied tonight, Columbina. Another '
                                      'step closer, and we could have broken the seal for good.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B10',
                              'speaker': 'Columbina',
                              'text': 'Do not look wistful, foolish star. Because you refused to gamble my '
                                      "mind recklessly, I am still right here to taste Paimon's morning "
                                      'berries.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': 'vn_tender_love',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B11',
                              'speaker': 'Columbina',
                              'text': 'When the next lunar cycle comes round and every chord of our '
                                      'harmony is complete... come back to this rocking chair and untie my '
                                      'ribbon properly.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44A_B12',
                              'speaker': 'Narrator',
                              'text': 'Fingers interlaced beneath the blanket as quiet dawn gilds her '
                                      'veiled smile, we listen to the silver bell chime softly between two '
                                      'hearts waiting for their next moon.',
                              'inner_thought': 'NEUTRAL ENDING (44A) -- Through the Moonlight Veil: '
                                               'Promise of the Next Moon.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F07_MOONWEAVE_RIBBON_CHIME'],
                                       'forbid_flags': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B01',
                              'speaker': 'Narrator',
                              'text': 'At 00:00 totality, without the Moonweave Ribbon Chime bound to my '
                                      'wrist as a direct wire, I hold Columbina fast against my chest over '
                                      'her tied X-veil as the eclipse surge crashes down!',
                              'inner_thought': 'With no physical ribbon-bridge between our wrists, she has '
                                               'to vent half her own lunar power downward!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B02',
                              'speaker': 'Columbina',
                              'text': 'Hold my shoulders steady, Aether -- I am releasing half of my '
                                      'stored Kuuvahki down into the deep bedrock valves!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B03',
                              'speaker': 'Narrator',
                              'text': "Sandrone's six coastal relief valves and Vesna's pylons roar at "
                                      'full capacity, swallowing the shed divine current safely into the '
                                      'polar sea while I shield her trembling back!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B04',
                              'speaker': 'Narrator',
                              'text': 'Quarter past midnight, the False Sky stills. Shedding half her '
                                      "lunar reserve drops her resonance safely below the Seelie seal's "
                                      'threshold -- leaving her exhausted, veiled, yet wholly herself!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B05',
                              'speaker': 'Narrator',
                              'text': 'At half past five in the pale dawn, soft mist curls through '
                                      "Silvermoon Hall's courtyard while Paimon tiptoes over with warm "
                                      'honey-water before curling up beside Luonnotar.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B06',
                              'speaker': 'Narrator',
                              'text': 'Resting deeply in the quilted rocking chair beside me, Columbina '
                                      'leans her veiled head onto my shoulder -- the Moonweave Ribbon '
                                      'Chime in her hair ringing faintly in the dawn breeze.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B07',
                              'speaker': 'Aether',
                              'text': 'Your voice sounds softer than whispers after venting half your '
                                      'Kuuvahki into the sea, Columbina. Does your throat ache?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B08',
                              'speaker': 'Columbina',
                              'text': 'Only a pleasant tiredness... I cannot float across the cavern '
                                      'ceiling for a few seasons, yet every memory of your kindness stayed '
                                      'safe inside my chest.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B09',
                              'speaker': 'Columbina',
                              'text': 'Perhaps keeping this X-lattice veil tied is a fair bargain for an '
                                      'Angel who was not quite ready to part with her birth-ribbon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': 'vn_sweet_happy',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B10',
                              'speaker': 'Aether',
                              'text': 'As long as you are alive and smiling beside me, the veil can wait '
                                      'as many winters as it takes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B11',
                              'speaker': 'Columbina',
                              'text': "Mm... hum that traveler's tune for me once more before I nap, "
                                      'Aether. Even unseen, morning sounds warm beside you.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44B_B12',
                              'speaker': 'Narrator',
                              'text': 'Rocking gently beneath the pale Nod-Krai sunrise while the bell in '
                                      'her hair answers my hum, we keep a quiet, veiled peace beyond the '
                                      'storm.',
                              'inner_thought': 'NEUTRAL ENDING (44B) -- Through the Moonlight Veil: Gentle '
                                               'Slumber of the Diminished Tide.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n44_neutral_veil.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME',
                                                        'F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B01',
                              'speaker': 'Narrator',
                              'text': "At 00:00 totality, I shield Columbina's tied X-lattice veil in my "
                                      'bandaged hands as the eclipse surge hammers down -- while '
                                      "Sandrone's coastal valves keep Nasha Town safe below!",
                              'inner_thought': 'Even with the veil tied fast, the unhealed hairline crack '
                                               'from my earlier recoil groans near breaking!',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B02',
                              'speaker': 'Columbina',
                              'text': 'Ngh... hold fast just ten seconds more, Aether -- do not let the '
                                      'temple-knot snap!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B03',
                              'speaker': 'Narrator',
                              'text': 'Sparks of white frost hiss along the fractured edge of her gauze, '
                                      'stopping half a millimeter short of shattering her mind only as the '
                                      'eclipse corona begins to wane!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B04',
                              'speaker': 'Narrator',
                              'text': 'We survive midnight with her memories intact -- yet the hairline '
                                      'fracture across her X-veil remains paper-thin, vibrating '
                                      'dangerously whenever my heartbeat nears hers.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c5_n38_eclipse_syzygy.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B05',
                              'speaker': 'Narrator',
                              'text': 'At half past five in the misty dawn, Columbina walks Paimon and me '
                                      'out beneath the snow-dusted stone archway of Silvermoon Hall -- '
                                      'halting on the inner side of the threshold.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B06',
                              'speaker': 'Paimon',
                              'text': "Huh? Columbina, why did you pack Paimon's travel snacks by the "
                                      'outer gate? The eclipse is already over!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B07',
                              'speaker': 'Columbina',
                              'text': 'Because the hairline crack on my veil only survived midnight by a '
                                      'breath, little finch... If Aether stays beside me another week '
                                      'while my heart leans toward him, the gauze will split and force him '
                                      'to watch me crumble.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B08',
                              'speaker': 'Aether',
                              'text': "Columbina, don't do this -- you do not have to lock yourself behind "
                                      'Moon Maiden protocol to spare me!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B09_WITH_F07',
                              'speaker': 'Narrator',
                              'text': 'A silent tear dampens the lower hem of her white X-veil. Reaching '
                                      'out tenderly, she unties the scorched Moonweave Ribbon Chime from '
                                      'my bandaged wrist and presses its silver bell over the crack on her '
                                      'collarbone to hold her own seal together.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL',
                                                        'F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N44_44C_B09_NO_F07',
                              'speaker': 'Narrator',
                              'text': 'A silent tear dampens the lower hem of her white X-veil. Brushing '
                                      'my bandaged knuckles one last time, she draws the Moonweave Ribbon '
                                      'Chime from her hair and presses its silver bell over her cracked '
                                      'collarbone to hold her seal together.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL'],
                                       'forbid_flags': ['F07_MOONWEAVE_RIBBON_CHIME']}},
                             {'beat_id': 'N44_44C_B10',
                              'speaker': 'Columbina',
                              'text': 'You already burned both your hands saving my memories, Aether... '
                                      'Let the Moon Maiden invoke sacred quarantine while I still remember '
                                      'the warmth of your name.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B11',
                              'speaker': 'Columbina',
                              'text': 'Farewell for now, my wandering star. Do not look back when the mist '
                                      'closes -- if you hear a lullaby across the strait, know that its '
                                      'silent rest still belongs to you.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}},
                             {'beat_id': 'N44_44C_B12',
                              'speaker': 'Narrator',
                              'text': 'Stepping backward into dense silver Kuuvahki mist beneath the stone '
                                      'archway, Columbina seals the sanctuary behind pale fog -- alive, '
                                      'remembering us, yet quarantined behind a veil our past hesitation '
                                      'left too fragile to untie.',
                              'inner_thought': 'NEUTRAL ENDING (44C) -- Through the Moonlight Veil: '
                                               'Self-Quarantine Behind the Mist.',
                              'cg': 'ui_assets/story_quest_cgs/columbina/col_c2_n17_archway_vigil.jpg',
                              'voice_emotion': '',
                              'when': {'requires_all': ['F11_COLD_PROTOCOL']}}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_NEUTRAL'}}}

STORY_QUEST_CAMPAIGNS: list[dict] = [STORY_QUEST_CAMPAIGN]
