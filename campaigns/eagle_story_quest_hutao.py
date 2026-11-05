"""
Hu Tao 5-Chapter Pure Branching Visual Novel Campaign Pack ("Where the Papilio Rests")
Target Runtime: C:\\Users\\LENOVO\\Desktop\\GTA\\Project Eagle\\gta sa gameplay-lab
Plug-and-Play Contract: exports `STORY_QUEST_CAMPAIGN` for `StoryQuestEngine` v1.0.
"""
from __future__ import annotations

STORY_QUEST_CAMPAIGN: dict = {'char_id': 'hutao',
 'ped_id': 49429,
 'display_name': 'Hu Tao',
 'campaign_id': 'hutao_papilio_5ch_v1',
 'title': 'Where the Papilio Rests',
 'subtitle': 'Where the Plum Blossom Crosses the Mist',
 'poster_cg': 'ui_assets/story_quest_cgs/hutao/hutao_sq1_poster.jpg',
 'synopsis': "Beneath Liyue's lantern glow, an unsealed Border flare drains the warmth from Wangsheng's 77th Director. Walk five nights beside Hu Tao through Wuwang mist, gather hidden karmic clues, and decide whether two mortal hands can rewrite an ancient law of parting.",
 'version': '2.2.0',
 'theme_rgb': [225, 49, 75],
 'chapters': [{'chapter_id': 'CH1',
               'index': 1,
               'title': 'Chapter 1 -- Red Pine & Hidden Frost',
               'entry_node': 'N01'},
              {'chapter_id': 'CH2',
               'index': 2,
               'title': 'Chapter 2 -- The Unsent Plum Branch',
               'entry_node': 'N09'},
              {'chapter_id': 'CH3',
               'index': 3,
               'title': 'Chapter 3 -- Divergence Across the Mist',
               'entry_node': 'N18_A1'},
              {'chapter_id': 'CH4',
               'index': 4,
               'title': 'Chapter 4 -- Three Gates Before Midnight',
               'entry_node': 'N21_A4'},
              {'chapter_id': 'CH5',
               'index': 5,
               'title': 'Chapter 5 -- Matching Plum Blossoms',
               'entry_node': 'N34_CH5_CONVERGE'}],
 'initial_state': {'bond': 0, 'insight': 0, 'flags': []},
 'flag_catalog': {'F01_COLD_PULSE': {'title': 'Cold Wrist Pulse',
                                     'clue_hint': "Noticed subterranean yin-frost chilling only Hu Tao's "
                                                  'Homa-casting right wrist.'},
                  'F02_SHARED_BOWL': {'title': 'Shared Osmanthus Bowl',
                                      'clue_hint': "Kept Wangsheng's midnight rule: bitter first, sweet "
                                                   'last -- never part on bitterness.'},
                  'F03_WUWANG_LORE': {'title': 'Tao Dou & Ley Line Lore',
                                      'clue_hint': "Learned from Zhongli how Tao Dou's Eight Gates exact "
                                                   'Ley Line Obfuscation on mortals.'},
                  'F04_ROOF_PROMISE': {'title': 'Rooftop Lantern Vow',
                                       'clue_hint': "Promised on Wangsheng's curved roof to meet every "
                                                    'Lantern Rite sky side by side.'},
                  'F05_CARPENTER_LEDGER': {'title': "Old Lin's Farewell Tin",
                                           'clue_hint': 'Recognized how Liyue souls hide farewell gifts in '
                                                        'plain sight when preparing to cross.'},
                  'F06_MERCY_LANTERN': {'title': 'Swallow Lantern Mercy',
                                        'clue_hint': "Delivered Old Lin's carved swallow secret without "
                                                     "breaking Wangsheng's oath."},
                  'F07_PLUM_BRANCH': {'title': 'Living Crimson Plum Branch',
                                      'clue_hint': 'Carries the living plum branch Old Hu grafted -- Hu '
                                                   "Tao's personal anchor to the living shore."},
                  'F08_ASH_COUGH_SEEN': {'title': 'Smoldering Yin-Ash Cloth',
                                         'clue_hint': "Witnessed the black yin-ash coughed onto Hu Tao's "
                                                      'white silk handkerchief.'},
                  'F09_MORTAL_VOW': {'title': 'Ten-Finger Mortal Vow',
                                     'clue_hint': "Chose one finite lifetime holding Hu Tao's living hand "
                                                  'over a painless eternity.'},
                  'F10_UNLINKED_RATTAN': {'title': 'Unlinked Rattan Figure',
                                          'clue_hint': "Kept Lan Yan's blank Chenyu rattan doll unbound to "
                                                       "Teyvat's Ley Lines as a spatial medium."},
                  'F11_BUBU_HERBS': {'title': 'Bubu Marrow-Frost Slip',
                                     'clue_hint': "Read Doctor Baizhu's secret prescription for late-stage "
                                                  'marrow-frost in the lungs.'}},
 'endings': {'END_TRUE': {'rank': 'TRUE ENDING',
                          'title': 'Twin Plum Blossoms on the Living Shore',
                          'summary': 'Crossing the Gate of Death together and anchoring Hu Tao back from '
                                     'erasure, Aether pins a matching crimson plum branch to his scarf '
                                     "beside hers under Liyue's New Year lanterns."},
             'END_GOOD': {'rank': 'GOOD ENDING',
                          'title': 'A Slumber Beneath Borrowed Eaves',
                          'summary': "Sealing the Serenitea Pot three hours before midnight saves Hu Tao's "
                                     'life while Zhongli freezes Wuwang for sixty days until Qingming -- '
                                     'buying warm borrowed spring to find another cure together.'},
             'END_NEUTRAL': {'rank': 'NEUTRAL ENDING',
                             'title': 'Lanterns Across Half a Step',
                             'summary': "Wuwang's border crisis is cleansed and Hu Tao lives whole in the "
                                        'sunlit harbor, yet half a step of unspoken distance leaves Aether '
                                        'departing for the next horizon as cherished friends.'},
             'END_BAD_1': {'rank': 'BAD ENDING I',
                           'title': 'Polite Strangers Under a Black Umbrella',
                           'summary': 'Flinching before the phantom thousand-year headstone shatters their '
                                      'resonance; Zhongli quarantines northern Wuwang by force, and Hu Tao '
                                      'bids Aether farewell behind an impenetrable professional smile.'},
             'END_BAD_2': {'rank': 'BAD ENDING II',
                           'title': 'Butterflies Over Forgotten Ash',
                           'summary': 'Lacking the living plum anchor and Descender rift at Boar Hour, '
                                      "Aether reaches Wuwang's altar thirty minutes too late -- alone "
                                      "remembering the 77th Director whom Liyue's Ley Lines erased."}},
 'nodes': {'N01': {'node_id': 'N01',
                   'chapter_id': 'CH1',
                   'title': 'Fetor in the Bamboo Mist',
                   'day_label': 'Day 1 - Midnight',
                   'location': 'Wuwang Hill - Northern Bamboo Slope',
                   'beats': [{'beat_id': 'N01_B01',
                              'speaker': 'Narrator',
                              'text': "Cold mountain fog clings to the culms above Qingce's northern "
                                      'ridge, thick enough to swallow the torchlight of the young '
                                      'Millelith patrol behind me.',
                              'inner_thought': "Twelve days before Lantern Rite, the earth above Wuwang's "
                                               'roots should never hum like a drawn bowstring.',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B02',
                              'speaker': 'Narrator',
                              'text': 'Beneath a split limestone boulder, a hairline fissure breathes '
                                      'black vapor that smells of wet grave-ash and rusted iron -- an '
                                      "early pocket of Tao Dou's border fetor.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B03',
                              'speaker': 'Aether',
                              'text': 'Get back behind the stone marker! Hold your breath and do not let '
                                      'that black mist touch your skin!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B04',
                              'speaker': 'Narrator',
                              'text': 'Before the youngest spearman can stumble backward, the pocket '
                                      'ruptures. A whip of ink-black miasma lashes straight toward his '
                                      'throat.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B05',
                              'speaker': 'Narrator',
                              'text': 'Instinct moves faster than thought. I plant my boots between the '
                                      'fissure and the squad, thrusting my bare right palm directly into '
                                      'the erupting plume.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B06',
                              'speaker': 'Narrator',
                              'text': "The fetor expects mortal lungs bound to Liyue's Ley Lines. Instead "
                                      'it hits a vessel from beyond the sky -- the same abyssal-filtering '
                                      "constitution that once drank Dvalin's poisoned tears.",
                              'inner_thought': 'My meridians flare white-gold, dragging every thread of '
                                               "black vapor inward and incinerating it outside Teyvat's "
                                               'root network.',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B07',
                              'speaker': 'Narrator',
                              'text': 'In two violent heartbeats the bamboo clearing turns crystal clear. '
                                      'Not a single speck of Ley Line rot reaches my organs, yet the '
                                      'sudden elemental draw empties my stamina like a shattered cup.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B08',
                              'speaker': 'Narrator',
                              'text': 'My knees hit the damp moss. Through the ringing in my ears, the '
                                      'Millelith sergeant shouts for a stretcher down the trail, while a '
                                      'very different sound drifts down from the higher mist.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B09',
                              'speaker': 'Narrator',
                              'text': 'Crisp brass bells chime in unhurried three-beat cadence. A solitary '
                                      'crimson Pyro butterfly parts the gray fog, shedding warm embers '
                                      'that smell faintly of snow-plum incense.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B10',
                              'speaker': 'Hu Tao',
                              'text': 'Oya? Oyaoya... Fancy meeting my favorite regular sprawled across '
                                      "Wuwang's front porch at midnight!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N01_B11',
                              'speaker': 'Narrator',
                              'text': 'Polished dark shoes stop inches from my fingers. Beneath the dark '
                                      'brim of her Harmony Hexagram Hat -- a fresh crimson plum branch '
                                      'tucked neatly beside its gold talisman -- Hu Tao tilts her head '
                                      'down at me.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_close.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B12',
                              'speaker': 'Hu Tao',
                              'text': 'Tell the Millelith boys they can head down the hill. This one '
                                      "didn't inhale a drop of border rot -- he just burned his own "
                                      'lantern oil dry showing off.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_close.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N01_B13',
                              'speaker': 'Aether',
                              'text': 'Hu Tao... What are you doing up near the border this late?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_close.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B14',
                              'speaker': 'Hu Tao',
                              'text': 'Hehe, routine boundary bookkeeping, what else? Honestly, Aether, '
                                      "after all the years we've walked Liyue together, you could just "
                                      "knock on Wangsheng's door for tea instead of fainting in my "
                                      'jurisdiction.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_close.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N01_B15',
                              'speaker': 'Narrator',
                              'text': 'She crouches beside me, sliding my left arm across her narrow '
                                      'shoulders with startling practiced strength while her right sleeve '
                                      'stays tucked slightly back from the sealed rock.',
                              'inner_thought': 'Even half-conscious, I notice the faint scent of singed '
                                               'silk clinging to her cuffs.',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_close.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N01_B16',
                              'speaker': 'Hu Tao',
                              'text': "Close your eyes for a bit, Traveler. Seventy-seventh Director's "
                                      'personal escort service -- free of charge until noon tomorrow.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_bamboo_mist_close.jpg',
                              'voice_emotion': 'vn_tender_love'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N02'}],
                   'ending_id': None},
           'N02': {'node_id': 'N02',
                   'chapter_id': 'CH1',
                   'title': 'Red Pine & Hidden Frost',
                   'day_label': 'Day 2 - Noon',
                   'location': 'Wangsheng Funeral Parlor - Inner Courtyard Guest Room',
                   'beats': [{'beat_id': 'N02_B01',
                              'speaker': 'Narrator',
                              'text': 'Warm winter-end sunlight filters through lattice paper windows, '
                                      'carrying the clean, resinous scent of red pine shavings and roasted '
                                      'Songluo tea.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B02',
                              'speaker': 'Narrator',
                              'text': 'Pinned under a porcelain teacup on the bedside stand sits a '
                                      'round-hand note from Paimon, complete with a crooked doodle of a '
                                      'Mora pouch.',
                              'inner_thought': "'Aether! Baizhu checked you at dawn and said you just "
                                               "needed sleep! Uncle Mao and Xiangling hired me as Wanmin's "
                                               'daytime Lantern Rite Menu Taster -- all-you-can-eat pay! '
                                               "See you after my shifts!'",
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B03',
                              'speaker': 'Hu Tao',
                              'text': "Awake at last! Two more hours and I would've started drafting your "
                                      'elegy in seven-character verse.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N02_B04',
                              'speaker': 'Narrator',
                              'text': 'Hu Tao sits perched side-saddle on a rosewood stool beside the bed, '
                                      "swinging her legs while unrolling a carpenter's wooden measuring "
                                      'tape with theatrical solemnity. The crimson plum branch on her hat '
                                      'catches the noon sun.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B05',
                              'speaker': 'Aether',
                              'text': 'Let me guess. A seasonal discount on red-pine coffins for repeat '
                                      'reckless rescues?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B06',
                              'speaker': 'Hu Tao',
                              'text': 'Oyaoya, slander! Friends of the parlor get bespoke sizing before we '
                                      'ever talk Mora. Hold still -- let your physician-in-acting check '
                                      'that pulse first.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N02_B07',
                              'speaker': 'Narrator',
                              'text': 'Setting a warm teacup down with her left hand, she reaches out '
                                      'absently with her right, pressing two slender fingertips against '
                                      'the radial pulse of my wrist.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B08',
                              'speaker': 'Narrator',
                              'text': 'For a fraction of a breath, the playful curve of her lips stills. '
                                      'Even Baizhu had been baffled at dawn: any Liyue native who '
                                      'swallowed Wuwang fetor should carry gray Ley Line rot in their '
                                      'lungs, yet my pulse beats clean and steady.',
                              'inner_thought': 'Something flickers behind her scarlet plum-blossom pupils '
                                               '-- half relief, half troubled calculation -- and her right '
                                               'fingertips feel shockingly cold against my skin.',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B09',
                              'speaker': 'Hu Tao',
                              'text': 'Hmph. Clean as spring water, just like Doctor Baizhu said. You '
                                      'outlanders really are built out of stubbornness and stardust.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N02_B10',
                              'speaker': 'Narrator',
                              'text': 'She moves to tuck her right hand swiftly back into her wide dark '
                                      'cuff while waving the wooden measuring tape in her left.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N02_B11',
                              'speaker': 'Hu Tao',
                              'text': "Still, Wangsheng's finest guest mattress and Songluo leaves aren't "
                                      "charity! Until your qi tops back up, I'm drafting you for four days "
                                      'as my resident parlor assistant. What do you say?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': 'vn_playful_tease'}],
                   'choice': {'choice_id': 'C01',
                              'prompt': 'Her right fingers slip back toward her dark cuff even as the noon '
                                        'sun warms the room.',
                              'options': [{'opt_id': 'C01_A',
                                           'label': 'Catch her right wrist gently before she pulls back: '
                                                    "'Your hand is colder than mine, Hu Tao.'",
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F01_COLD_PULSE']},
                                           'next_node': 'N03',
                                           'reaction_beats': [{'beat_id': 'N02_C01A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Before she can retreat, my fingers '
                                                                       'close lightly around her right '
                                                                       'wrist. Beneath the sunlit window, '
                                                                       'her pulse feels like meltwater '
                                                                       'trapped beneath black river ice -- '
                                                                       'utterly unlike her warm left hand.',
                                                               'inner_thought': 'Clue Recorded [Cold Wrist '
                                                                                'Pulse]: Only her '
                                                                                'Homa-casting right arm '
                                                                                'carries subterranean '
                                                                                'frost.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_wrist.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N02_C01A_R2',
                                                               'speaker': 'Hu Tao',
                                                               'text': 'Oya... quick reflexes for an '
                                                                       "invalid! Hands off the Director's "
                                                                       'merchandise, assistant -- funeral '
                                                                       'parlor folk naturally run cool in '
                                                                       'winter.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_wrist.jpg',
                                                               'voice_emotion': 'vn_shy_blush'},
                                                              {'beat_id': 'N02_C01A_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'She slips her wrist free with a '
                                                                       'practiced twirl and hides it '
                                                                       'behind her back, erecting a bright '
                                                                       'professional grin a heartbeat too '
                                                                       'fast.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_wrist.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C01_B',
                                           'label': 'Play along with her measuring tape and request '
                                                    'starlight lacquer on the lid to make her laugh.',
                                           'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N03',
                                           'reaction_beats': [{'beat_id': 'N02_C01B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Four days of assistant labor '
                                                                       'sounds fair, provided my reserved '
                                                                       'lid comes inlaid with gold leaf '
                                                                       'and windwheel asters.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N02_C01B_R2',
                                                               'speaker': 'Hu Tao',
                                                               'text': 'Hahaha! Gold leaf AND Mondstadt '
                                                                       "imports? Now you're speaking "
                                                                       "Wangsheng's language! Deal sealed "
                                                                       '-- no backing out when the incense '
                                                                       'ash piles up!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'},
                                                              {'beat_id': 'N02_C01B_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'The tension left over from last '
                                                                       'night melts cleanly out of her '
                                                                       'shoulders as her bright laughter '
                                                                       'fills the sunny courtyard.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N03': {'node_id': 'N03',
                   'chapter_id': 'CH1',
                   'title': 'Seventy-Six Generations Before Her',
                   'day_label': 'Day 2 Afternoon - Day 3 Dusk',
                   'location': 'Wangsheng Funeral Parlor - Courtyard & Ancestral Hall',
                   'beats': [{'beat_id': 'N03_B01',
                              'speaker': 'Narrator',
                              'text': 'Living under the same curved eaves for two full days strips away '
                                      "the last thin formality between 'honored Traveler' and '77th "
                                      "Director'.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B02',
                              'speaker': 'Narrator',
                              'text': "We have known each other for years -- through the mist of Wuwang's "
                                      'border where she once searched for Old Hu, and across noisy Lantern '
                                      'Rite banquet tables beside Zhongli, Venti, and Xiao.',
                              'inner_thought': 'Yet sharing morning chores in a quiet courtyard belongs to '
                                               'an intimacy neither of us has ever named aloud.',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B03',
                              'speaker': 'Narrator',
                              'text': 'On the afternoon of Day 2, I lay sheets of sandalwood paper across '
                                      'bamboo racks in the sun while Hu Tao haggles cheerfully with two '
                                      'elderly Harbor guildmasters over ceremonial silk.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B04',
                              'speaker': 'Hu Tao',
                              'text': 'Assistant Aether! Tell Master Sun here that crimson silk around the '
                                      'doorway wards off gloom ten times better than dreary gray hemp!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N03_B05',
                              'speaker': 'Aether',
                              'text': "She's right, Master Sun. Even the adepti in Jueyun Karst prefer "
                                      'warm lantern colors when sending off old friends.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B06',
                              'speaker': 'Narrator',
                              'text': 'When the guildmasters leave chuckling and shaking their heads, Hu '
                                      'Tao flashes me a conspiratorial thumbs-up behind a ledger stack.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_bedside_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B07',
                              'speaker': 'Narrator',
                              'text': 'Yet by dusk of the third day, the courtyard grows hushed. Follow '
                                      'the scent of aged aloeswood past the inner moon-gate, and I find '
                                      "the door of Wangsheng's private ancestral hall standing ajar.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B08',
                              'speaker': 'Narrator',
                              'text': 'Rows upon rows of dark rosewood spirit tablets rise along the '
                                      'tiered altar -- seventy-six predecessors stretching back to the '
                                      'devastation after the Archon War.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B09',
                              'speaker': 'Narrator',
                              'text': 'Having set her hat aside on the threshold table, Hu Tao stands '
                                      "alone before the seventy-sixth tablet -- her grandfather Old Hu's "
                                      '-- wiping each carved character with a clean linen cloth.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B10',
                              'speaker': 'Hu Tao',
                              'text': "Don't hover at the threshold like a stray wisp, Aether. Come light "
                                      'the third stick if you want.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N03_B11',
                              'speaker': 'Aether',
                              'text': 'Seventy-six Directors before you... Seeing them all in one room '
                                      'makes thirteen sound terribly young to have picked up that staff.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B12',
                              'speaker': 'Hu Tao',
                              'text': 'Thirteen was plenty old enough to know Grandpa left without a '
                                      'single regret. None of the Hu family live to snowy eyebrows, you '
                                      'know -- border work eats the candle from both ends.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N03_B13',
                              'speaker': 'Hu Tao',
                              'text': "That's why our house motto isn't mournful at all. Live brightly "
                                      'while the wick holds, cross cleanly when the bell rings. Simple, '
                                      'right?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N03_B14',
                              'speaker': 'Narrator',
                              'text': 'She says it with effortless lightness, yet in the amber taper glow, '
                                      'her nineteen-year-old shoulders look unbearably slender beneath '
                                      'seventy-six generations of silent wood.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N04'}],
                   'ending_id': None},
           'N04': {'node_id': 'N04',
                   'chapter_id': 'CH1',
                   'title': 'Bitter Tonic, Sweet Tangyuan',
                   'day_label': 'Day 3 - Late Night',
                   'location': 'Wangsheng Funeral Parlor - Lantern-Lit Guest Room',
                   'beats': [{'beat_id': 'N04_B01',
                              'speaker': 'Narrator',
                              'text': 'Rain patters softly against the courtyard banana leaves late on the '
                                      'third night when three rhythmic taps sound against my door frame.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B02',
                              'speaker': 'Hu Tao',
                              'text': "Special night delivery! Doctor Baizhu's qi-restoring decoction, "
                                      'plus an unauthorized kitchen bonus from yours truly.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N04_B03',
                              'speaker': 'Narrator',
                              'text': 'Hatless in a loose dark-crimson indoor cardigan, twin-tails draped '
                                      'softly over her collarbone, Hu Tao sets a lacquered tray onto my '
                                      'low table.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B04',
                              'speaker': 'Narrator',
                              'text': 'Beside the dark bowl of bitter medicinal broth steams a '
                                      'blue-and-white porcelain bowl of glutinous rice tangyuan floating '
                                      'in golden osmanthus syrup -- slightly uneven in size, unmistakably '
                                      'rolled by hand.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B05',
                              'speaker': 'Aether',
                              'text': "Wait. After the suspicious dishes you've served Xiangling over the "
                                      'years, should I ask Baizhu for an antidote first?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B06',
                              'speaker': 'Hu Tao',
                              'text': 'Hey! Sweet tangyuan has zero room for creative error! Drink the '
                                      "bitter bowl while it's hot -- I'll rinse the teapot on the side "
                                      'stand.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N04_X1',
                              'speaker': 'Hu Tao',
                              'text': 'Grandpa used to roll sweet rice balls like this whenever winter '
                                      'rain kept me stuck indoors memorizing parlor liturgy.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N04_X2',
                              'speaker': 'Aether',
                              'text': 'Let me guess -- yours always came out shaped like little ghosts?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_X3',
                              'speaker': 'Hu Tao',
                              'text': 'Spherical ghosts are still round! Besides, syrup tastes sweeter '
                                      'when someone stays up past midnight to stir the pot.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N04_B07',
                              'speaker': 'Narrator',
                              'text': 'As she turns her back toward the washstand, the corner of a folded '
                                      'white silk cloth on the outer edge of her lacquer tray slips '
                                      'sideways in the draft.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N04_B08',
                              'speaker': 'Narrator',
                              'text': 'Tucked underneath that silk is a second, tightly tied Bubu Pharmacy '
                                      'herb packet stained with frost-repelling cinnabar seal ink -- '
                                      'completely different from the mild qi tonic in my hands.',
                              'inner_thought': 'In two seconds she will turn back around with the kettle, '
                                               'while a single osmanthus tangyuan floats at the bottom of '
                                               'the sweet bowl.',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C02',
                              'prompt': 'Hu Tao hums softly at the side stand while steam rises from the '
                                        'sweet osmanthus bowl and the half-covered herb packet.',
                              'options': [{'opt_id': 'C02_A',
                                           'label': 'Drink the bitter tonic in one go, then split the last '
                                                    'osmanthus tangyuan with her.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F02_SHARED_BOWL']},
                                           'next_node': 'N05',
                                           'reaction_beats': [{'beat_id': 'N04_C02A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'I drain the bitter tonic without '
                                                                       'wincing, eat the first sweet rice '
                                                                       'ball, and lift the second '
                                                                       'porcelain spoon with half of the '
                                                                       'last osmanthus tangyuan as she '
                                                                       'turns back.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_blush.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02A_R2',
                                                               'speaker': 'Aether',
                                                               'text': 'The cook ought to verify her own '
                                                                       'batch. Fair split for my four-day '
                                                                       'supervisor?',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_blush.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02A_R3',
                                                               'speaker': 'Hu Tao',
                                                               'text': 'O-oya... Well, waste is a sin! Mmm '
                                                                       '-- see, flawless! Remember our new '
                                                                       'house rule, Aether: bitter first, '
                                                                       'sweet last -- nobody leaves '
                                                                       "Wangsheng's table with bitterness "
                                                                       'on their tongue.',
                                                               'inner_thought': 'Memory Kept [Shared '
                                                                                'Osmanthus Bowl]: Her '
                                                                                'quiet blush lingers '
                                                                                'warmer than the ginger '
                                                                                'syrup.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_blush.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C02_B',
                                           'label': 'Glance beneath the silk cloth while her back is '
                                                    'turned to read the second Bubu prescription slip.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F11_BUBU_HERBS']},
                                           'next_node': 'N05',
                                           'reaction_beats': [{'beat_id': 'N04_C02B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Without rustling the cloth, I tilt '
                                                                       'my head just far enough to read '
                                                                       "Baizhu's cramped brush script "
                                                                       'along the cinnabar strip before '
                                                                       'smoothing the silk back in place.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02B_R2',
                                                               'speaker': 'Narrator',
                                                               'text': "'Confidential -- Wangsheng Inner "
                                                                       'Residence. Diagnosis: Severe '
                                                                       'Marrow-Frost Entering the Lungs. '
                                                                       'Boil over high flame twice '
                                                                       'nightly; suppresses yin-meridian '
                                                                       "numbness only.'",
                                                               'inner_thought': 'Clue Recorded [Bubu Frost '
                                                                                'Prescription]: Someone '
                                                                                'inside Wangsheng is '
                                                                                'hiding late-stage '
                                                                                'Yin-frost in their lungs.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N04_C02B_R3',
                                                               'speaker': 'Hu Tao',
                                                               'text': 'All rinsed! Oya, you drank the '
                                                                       'bitter bowl already? Good '
                                                                       'assistant -- eat the sweet '
                                                                       'tangyuan before it cools!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_parlor_tea_night_blush.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N05': {'node_id': 'N05',
                   'chapter_id': 'CH1',
                   'title': 'Lantern Patrol Along Chihu Rock',
                   'day_label': 'Day 4 - Late Afternoon',
                   'location': 'Liyue Harbor - Chihu Rock Market',
                   'beats': [{'beat_id': 'N05_B01',
                              'speaker': 'Narrator',
                              'text': 'By the fourth afternoon my strength has returned in full, just in '
                                      "time for Paimon to swoop through Wangsheng's courtyard waving a "
                                      'paper bag of steamingjade parcels.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B02',
                              'speaker': 'Paimon',
                              'text': "Aether! Hu Tao! Xiangling's testing five new sweet-and-numbing "
                                      'sauces for the festival rush, and Paimon is officially Chief '
                                      "Quality Inspector until New Year's Eve!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B03',
                              'speaker': 'Hu Tao',
                              'text': 'Work hard, little inspector! Tell Chef Xiangling to save two '
                                      'portions of golden shrimp balls for my assistant when his shift '
                                      'ends!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N05_B04',
                              'speaker': 'Narrator',
                              'text': "Once Paimon darts happily back toward Wanmin's dinner prep, Hu Tao "
                                      'settles her Harmony Hexagram Hat -- crimson plum branch bright '
                                      'against its dark felt -- onto her head and beckons me toward the '
                                      'street.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B05',
                              'speaker': 'Narrator',
                              'text': 'Together we walk the stone steps of Chihu Rock, inspecting the '
                                      'traditional wayfinding lanterns hung at street corners so wandering '
                                      'spirits do not lose their bearings amid festival crowds.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B06',
                              'speaker': 'Hu Tao',
                              'text': 'Look up on the third-story railing, Aether. Speak of timeless '
                                      "fossils and there sits our parlor's most expensive tea connoisseur.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N05_X1',
                              'speaker': 'Narrator',
                              'text': "Halfway past Granny Shan's pinwheel stall, Hu Tao snaps her left "
                                      'fingers -- kindling a tiny gold-red spark to relight a wind-snuffed '
                                      'street lantern.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_X2',
                              'speaker': 'Hu Tao',
                              'text': 'People think Wangsheng only tends the dead, yet street lanterns are '
                                      'really for the living, Aether. Walk home under warm light, and '
                                      'grief loses half its teeth.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N05_X3',
                              'speaker': 'Aether',
                              'text': 'No wonder Granny Shan slipped two candied hawthorns into your '
                                      "pocket when she thought I wasn't looking.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_X4',
                              'speaker': 'Hu Tao',
                              'text': 'Hehe, professional perks! One stick for the Director, one for her '
                                      'star-ranked assistant!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N05_B07',
                              'speaker': 'Zhongli',
                              'text': 'Ah, Traveler. And the Director as well. The harbor breeze carries '
                                      'an unusually crisp edge this evening.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N05_B08',
                              'speaker': 'Hu Tao',
                              'text': "Put the tab on Wangsheng's slate as usual, Mister Zhongli -- I spot "
                                      'fresh sugar-roasted chestnuts across the bridge! Back in five '
                                      'minutes!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N06'}],
                   'ending_id': None},
           'N06': {'node_id': 'N06',
                   'chapter_id': 'CH1',
                   'title': "The Consultant's Amber Gaze",
                   'day_label': 'Day 4 - Dusk',
                   'location': 'Chihu Rock - Upper Teahouse Balcony',
                   'beats': [{'beat_id': 'N06_B01',
                              'speaker': 'Narrator',
                              'text': 'Down by the bridge brazier, Hu Tao bounces lightly on her heels '
                                      'beside the chestnut vendor, crimson coat vivid against the '
                                      'dusk-blue tide.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B02',
                              'speaker': 'Narrator',
                              'text': 'Across the carved cedar table, Zhongli does not lift his teacup. '
                                      'His amber eyes follow that small crimson silhouette with the quiet '
                                      'gravity of bedrock remembering an ancient fault line.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B03',
                              'speaker': 'Zhongli',
                              'text': 'I heard from Baizhu of your encounter above Qingce on the first '
                                      "night. Few beings could draw a pocket of Tao Dou's fetor into their "
                                      'own palm and walk away unscathed.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B04',
                              'speaker': 'Aether',
                              'text': "Tao Dou... That's more than ordinary Archon War residue beneath "
                                      "Wuwang Hill, isn't it, Zhongli?",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_X1',
                              'speaker': 'Zhongli',
                              'text': 'When Director Hu was thirteen, she packed three days of dry rations '
                                      "and sat stubbornly at Wuwang's border stone waiting to say goodbye "
                                      'to Old Master Hu.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_X2',
                              'speaker': 'Zhongli',
                              'text': 'Only when she found the border empty did she realize how thoroughly '
                                      'her grandfather lived without regret. Since that morning, she has '
                                      "guarded others' farewells with fierce pride.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_X3',
                              'speaker': 'Aether',
                              'text': 'Yet she never lets anyone guard hers.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_X4',
                              'speaker': 'Zhongli',
                              'text': 'Perhaps because no one before you ever lingered at Wangsheng long '
                                      'enough to try, Traveler.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B05',
                              'speaker': 'Zhongli',
                              'text': 'An ancient deity of life and death felled in antiquity, whose '
                                      'shattered corpus became the very seam between yin and yang in '
                                      'northern Liyue.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N06_B06',
                              'speaker': 'Narrator',
                              'text': 'Across the street, the chestnut vendor scoops glossy hot nuts into '
                                      'a brown paper cone. Hu Tao waves up at me with her left hand, '
                                      'inviting me down into the sea breeze.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C03',
                              'prompt': "Zhongli's gaze lingers on the northern hills while Hu Tao waves "
                                        'from the warm chestnut brazier below.',
                              'options': [{'opt_id': 'C03_A',
                                           'label': 'Ask Zhongli quietly why the border beneath Wuwang '
                                                    'demands heavier tolls from Wangsheng Directors near '
                                                    'the New Year.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F03_WUWANG_LORE']},
                                           'next_node': 'N07',
                                           'reaction_beats': [{'beat_id': 'N06_C03A_R1',
                                                               'speaker': 'Zhongli',
                                                               'text': 'Because divine geo spears would '
                                                                       "detonate Tao Dou's resentment "
                                                                       'along every Ley Line in Liyue. '
                                                                       'Only a mortal written into this '
                                                                       "land's roots, wielding Homa's "
                                                                       'flame, can anchor the seam.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03A_R2',
                                                               'speaker': 'Zhongli',
                                                               'text': 'Seventy-six Directors paid years '
                                                                       'of their lifespans to keep that '
                                                                       'pact. And this winter, Traveler... '
                                                                       'the subterranean tremor runs '
                                                                       'deeper than any cycle in living '
                                                                       'memory.',
                                                               'inner_thought': 'Clue Recorded [Tao Dou & '
                                                                                'Mortal Anchor]: Divine '
                                                                                'Geo would detonate the '
                                                                                'Ley Lines; only a mortal '
                                                                                'Homa bearer anchors the '
                                                                                'border.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C03_B',
                                           'label': 'Excuse yourself from the solemn lore to join Hu Tao '
                                                    'by the roasting-chestnut brazier and shield her from '
                                                    'the sea wind.',
                                           'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N07',
                                           'reaction_beats': [{'beat_id': 'N06_C03B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'With a respectful nod to Zhongli, '
                                                                       'I hurry down the stone steps and '
                                                                       "step onto Hu Tao's windward side "
                                                                       'right as an icy harbor gust sweeps '
                                                                       'off the bay.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N06_C03B_R2',
                                                               'speaker': 'Hu Tao',
                                                               'text': 'Hehe, rescued from one of Mister '
                                                                       "Zhongli's three-hour history "
                                                                       'lectures! Here -- cup both hands '
                                                                       'with mine while the shells are '
                                                                       'piping hot!',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_chihu_zhongli_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N07': {'node_id': 'N07',
                   'chapter_id': 'CH1',
                   'title': 'Chestnuts Under Early Frost',
                   'day_label': 'Day 4 - Night',
                   'location': 'Wangsheng Funeral Parlor - Curved Clay Rooftop',
                   'beats': [{'beat_id': 'N07_B01',
                              'speaker': 'Narrator',
                              'text': "By the fourth night my official 'assistant debt' is nearly settled, "
                                      'yet neither of us moves to say goodnight at the courtyard door.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B02',
                              'speaker': 'Narrator',
                              'text': 'With one light Anemo leap and a practiced scramble of dark boots, '
                                      "we settle side by side along the curved ridge tiles of Wangsheng's "
                                      'main roof, sharing the paper cone of roasted chestnuts.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B03',
                              'speaker': 'Narrator',
                              'text': 'Down by the docks, artisans release the first dozen test Xiao '
                                      'Lanterns of the season. Golden specks drift upward against the '
                                      'indigo sea sky like reverse snowfall.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_B04',
                              'speaker': 'Hu Tao',
                              'text': "Funny, isn't it? Every year we sit at some crowded banquet table "
                                      "trading awful rhymes, yet we've never once watched the test "
                                      'lanterns from my own roof.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N07_B05',
                              'speaker': 'Aether',
                              'text': 'You never invited me up here before. I figured the roof tiles were '
                                      'strictly reserved for composing questionable street flyers.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_X1',
                              'speaker': 'Narrator',
                              'text': 'A sharp gust sweeps down from Mt. Tianheng. Without thinking, I '
                                      'unwind half of my long white scarf and drape its warm fold across '
                                      "the back of Hu Tao's neck.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_X2',
                              'speaker': 'Hu Tao',
                              'text': 'Oya? Trying to wrap your employer up like a spring roll now?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N07_X3',
                              'speaker': 'Aether',
                              'text': 'If the 77th Director catches a cold on her own roof, Paimon will '
                                      'blame my assistant skills for a month.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_X4',
                              'speaker': 'Hu Tao',
                              'text': 'Hmph... smells like sun-warmed windwheel asters and glaze lilies. '
                                      'Remember two Lantern Rites ago when Venti talked Mister Zhongli '
                                      'into pouring him three jugs of dandelion wine at Xinyue Kiosk?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N07_X5',
                              'speaker': 'Aether',
                              'text': 'And Conqueror of Demons Xiao stood out on the balcony pretending he '
                                      "wasn't listening to your terrible lotus-head poem.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N07_X6',
                              'speaker': 'Hu Tao',
                              'text': 'Terrible?! Even Xiao cracked half a smile! ...Every single year '
                                      'since we met, my favorite memories have you sitting right across '
                                      'the table.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N07_B06',
                              'speaker': 'Hu Tao',
                              'text': "Hey, my flyers are literary milestones! ...Besides, up here it's "
                                      'quiet enough to hear the whole harbor breathing.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N07_B07',
                              'speaker': 'Narrator',
                              'text': 'I crack a warm chestnut shell cleanly in half and pass the golden '
                                      'kernel into her palm. Our knuckles brush; her twin-tails lift in '
                                      'the night wind beside the crimson plum branch on her hat.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N08'}],
                   'ending_id': None},
           'N08': {'node_id': 'N08',
                   'chapter_id': 'CH1',
                   'title': 'Fireworks & Ten Thousand Years',
                   'day_label': 'Day 4 - Late Night',
                   'location': 'Wangsheng Funeral Parlor - Curved Clay Rooftop',
                   'beats': [{'beat_id': 'N08_B01',
                              'speaker': 'Narrator',
                              'text': "A test firework blooms over Guyun's horizon, painting Hu Tao's "
                                      'profile in fleeting rose and gold before fading back into '
                                      'starlight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B02',
                              'speaker': 'Narrator',
                              'text': 'She rests her chin on her knees, watching the golden profile of the '
                                      'outlander beside her with an expression stripped of every parlor '
                                      'theatric.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B03',
                              'speaker': 'Hu Tao',
                              'text': "A thousand Lantern Rites from tonight, you'll still look just like "
                                      "this under some other sky, won't you, Aether?",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N08_B04',
                              'speaker': 'Aether',
                              'text': 'Hu Tao...',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_X1',
                              'speaker': 'Aether',
                              'text': 'Fireworks vanish fast only if nobody remembers the warmth they left '
                                      'behind, Hu Tao.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_X2',
                              'speaker': 'Hu Tao',
                              'text': 'Careful, Traveler. Say pretty things like that under moonlight, and '
                                      'a mortal girl might get greedy for seventy-seven more winters.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N08_X3',
                              'speaker': 'Narrator',
                              'text': 'She laughs softly into the fold of my scarf, yet her fingers '
                                      'tighten imperceptibly against the cold clay ridge tile.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B05',
                              'speaker': 'Hu Tao',
                              'text': "Don't make that face -- I'm not complaining! Mortals like us are "
                                      'closer to fireworks. One bright, noisy burst against the dark, and '
                                      'poof -- back into clean smoke.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N08_B06',
                              'speaker': 'Narrator',
                              'text': 'Even as she speaks, faint translucent spirit-moths above the eaves '
                                      'abandon the southward sea breeze, pulled in an unnatural straight '
                                      'line toward the dark silhouette of Wuwang Hill in the north.',
                              'inner_thought': 'My old immortal instinct whispers to keep a safe, painless '
                                               'distance -- yet my hand is already inches from hers on the '
                                               'cold tile.',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C04',
                              'prompt': 'Her fingers rest still on the cold ridge tile while pale '
                                        'spirit-moths drift against the wind toward northern Wuwang.',
                              'options': [{'opt_id': 'C04_A',
                                           'label': "Cover the back of her hand on the cold tiles: 'Stop "
                                                    "talking like I'm passing weather, Hu Tao. Promise you "
                                                    "won't shut me out.'",
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F04_ROOF_PROMISE']},
                                           'next_node': 'N09',
                                           'reaction_beats': [{'beat_id': 'N08_C04A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'I place my warm palm squarely over '
                                                                       'the back of her hand on the '
                                                                       'frost-cooled tile. Her dark '
                                                                       'eyelashes tremble once in the '
                                                                       'lantern glow.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_vow.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N08_C04A_R2',
                                                               'speaker': 'Hu Tao',
                                                               'text': "...Passing weather doesn't stay "
                                                                       'four days folding incense paper '
                                                                       'for me, huh. Fine, Assistant '
                                                                       'Aether. If the sky really starts '
                                                                       "falling, I'll leave one clue only "
                                                                       "you're sharp enough to catch.",
                                                               'inner_thought': 'Memory Kept [Rooftop '
                                                                                'Promise]: Her pinky hooks '
                                                                                'briefly, warmly around '
                                                                                'mine beneath the stars.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_vow.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C04_B',
                                           'label': 'Follow the strange northward drift of the '
                                                    'spirit-moths above the eaves and ask what is pulling '
                                                    'them toward Wuwang Hill.',
                                           'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                           'next_node': 'N09',
                                           'reaction_beats': [{'beat_id': 'N08_C04B_R1',
                                                               'speaker': 'Aether',
                                                               'text': "Those spirit-moths aren't drifting "
                                                                       'with the sea wind, Hu Tao. '
                                                                       'Something beneath northern Wuwang '
                                                                       'is drawing them upstream like a '
                                                                       'whirlpool.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N08_C04B_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Hu Tao falls silent for two full '
                                                                       'beats before clapping her hands to '
                                                                       'brush away chestnut crumbs. That '
                                                                       'fleeting silence confirms '
                                                                       'everything: the epicenter lies '
                                                                       "directly beneath Wuwang's main "
                                                                       'root.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch1_rooftop_lanterns_base.jpg',
                                                               'voice_emotion': ''}]}]},
                   'routing': [],
                   'ending_id': None},
           'N09': {'node_id': 'N09',
                   'chapter_id': 'CH2',
                   'title': 'Sawdust & Silent Cedar',
                   'day_label': 'Day 5 - Morning',
                   'location': "Southern Wharf Lane - Old Lin's Carpentry Shop",
                   'beats': [{'beat_id': 'N09_B01',
                              'speaker': 'Narrator',
                              'text': "Dawn of the fifth day brings a quiet commission to Wangsheng's "
                                      'front desk -- no weeping cortege, no brass gongs, only a pre-paid '
                                      'rosewood token delivered by a night watchman.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B02',
                              'speaker': 'Narrator',
                              'text': 'Old Lin, a sixty-year-old master joiner down by the southern wharf, '
                                      'passed away peacefully beside his planing bench before sunrise.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B03',
                              'speaker': 'Narrator',
                              'text': 'Inside his narrow workshop, pale winter sunbeams slant through '
                                      'cedar dust. Every tool hangs oiled in neat rows, as though the old '
                                      'craftsman merely stepped out for morning tea.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B04',
                              'speaker': 'Hu Tao',
                              'text': 'Look at his contract clause, Aether. Paid down to the last copper '
                                      'Mora three months ago, with one strict non-disclosure condition.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B05',
                              'speaker': 'Aether',
                              'text': "'Deliver the finished Xiao Lantern on my bench to Lin Wan's "
                                      'embroidery shop on Feiyun Slope. Do not speak my name, and do not '
                                      "tell her I have died.'",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_X1',
                              'speaker': 'Narrator',
                              'text': 'Along the highest dusty rafter above the saws sit nine smaller Xiao '
                                      'Lanterns from nine previous winters -- none of them ever flown, '
                                      'lined up like silent calendar marks.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_X2',
                              'speaker': 'Aether',
                              'text': 'He built one for her every single Lantern Rite after driving her '
                                      'away... and only paid Wangsheng to deliver the tenth when he knew '
                                      "he wouldn't wake up for an eleventh.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_X3',
                              'speaker': 'Hu Tao',
                              'text': 'Stubborn old Liyue men, huh? Carve ten years of longing into red '
                                      'plum wood rather than say three honest words over dinner.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_X4',
                              'speaker': 'Narrator',
                              'text': "Though she teases the old joiner's stubbornness, her left hand "
                                      "brushes the tenth lantern's rim with extraordinary gentleness.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B06',
                              'speaker': 'Hu Tao',
                              'text': 'Neighbors say Old Lin drove his daughter out of this house ten '
                                      "years ago in a furious shouting match over nothing. She hasn't set "
                                      'foot across his threshold since.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N09_B07',
                              'speaker': 'Narrator',
                              'text': 'Resting at the center of the workbench is a delicate Xiao Lantern '
                                      'framed not in cheap bamboo, but in hand-steamed red plum wood.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N10'}],
                   'ending_id': None},
           'N10': {'node_id': 'N10',
                   'chapter_id': 'CH2',
                   'title': 'The Staged Quarrel',
                   'day_label': 'Day 5 - Noon',
                   'location': "Southern Wharf Lane - Old Lin's Carpentry Shop",
                   'beats': [{'beat_id': 'N10_B01',
                              'speaker': 'Narrator',
                              'text': 'Hu Tao sets three sticks of guiding incense at the head of the '
                                      'bench, her crimson plum-trimmed hat bowed in quiet professional '
                                      'reverence.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B02',
                              'speaker': 'Hu Tao',
                              'text': "Wangsheng never judges a client's final arrangement. Still... ten "
                                      'years of silence is a heavy stone to carry to the border.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N10_X1',
                              'speaker': 'Aether',
                              'text': 'Look at the callus along his right thumb, Hu Tao. Even when his '
                                      'breathing failed, he sanded every inner rib smooth so silk sleeves '
                                      "wouldn't snag on splinters.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_X2',
                              'speaker': 'Hu Tao',
                              'text': 'When people know their candle is down to the last inch of tallow, '
                                      'every small detail becomes their whole world.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_X3',
                              'speaker': 'Narrator',
                              'text': "Outside in the lane, a vendor's festive drum echoes bright against "
                                      'the quiet cedar walls.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B03',
                              'speaker': 'Narrator',
                              'text': 'Near the mortise joint of the plum-wood lantern frame, a faint '
                                      'rust-brown stain catches the light -- and wedged beneath the loose '
                                      "floorboard under Old Lin's stool sits a tin ledger box.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N10_B04',
                              'speaker': 'Narrator',
                              'text': 'Beside the bier, Hu Tao unfolds clean warm linen to wash the cedar '
                                      "resin from the old carpenter's calloused knuckles before the "
                                      'undertakers arrive.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C05',
                              'prompt': "Old Lin's tin box glints beneath the workbench while Hu Tao "
                                        'prepares the warm cleansing water.',
                              'options': [{'opt_id': 'C05_A',
                                           'label': 'Inspect the dried blood inside the plum-wood lantern '
                                                    "joint and the unsent draft letter beneath Old Lin's "
                                                    'workbench.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F05_CARPENTER_LEDGER']},
                                           'next_node': 'N11',
                                           'reaction_beats': [{'beat_id': 'N10_C05A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Inside the tin box lie ten years '
                                                                       'of anonymous pawnshop remittance '
                                                                       "slips funding Lin Wan's embroidery "
                                                                       'shop -- and a crumpled, '
                                                                       'blood-flecked letter Old Lin never '
                                                                       'mailed.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_letter.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05A_R2',
                                                               'speaker': 'Aether',
                                                               'text': "'When Baizhu told me stone-dust "
                                                                       'chill had settled in my lungs, '
                                                                       'Wan-er was only eighteen. Better '
                                                                       'she hate a heartless old man and '
                                                                       'live free than waste her youth '
                                                                       "beside a dying stove...'",
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_letter.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05A_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'I look up from the page -- and '
                                                                       'freeze. Hu Tao is staring at that '
                                                                       'unsent confession with parted lips '
                                                                       'and stricken scarlet pupils, as if '
                                                                       'someone had just read her own '
                                                                       'secret ledger aloud.',
                                                               'inner_thought': "Clue Recorded [Old Lin's "
                                                                                'Unsent Ledger]: Picking a '
                                                                                'cold, cruel goodbye to '
                                                                                'spare someone you love '
                                                                                'from watching you fade.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_letter.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C05_B',
                                           'label': 'Stay beside Hu Tao to wash the cedar sawdust from Old '
                                                    "Lin's calloused hands and light the guiding incense "
                                                    'together.',
                                           'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N11',
                                           'reaction_beats': [{'beat_id': 'N10_C05B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Leaving the private box '
                                                                       'undisturbed, I kneel opposite Hu '
                                                                       'Tao, wringing out a warm cloth to '
                                                                       'wipe sixty years of cedar dust '
                                                                       "from the craftsman's fingers "
                                                                       'without hesitation.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N10_C05B_R2',
                                                               'speaker': 'Hu Tao',
                                                               'text': '...Most warriors flinch around the '
                                                                       'newly departed, you know. Having '
                                                                       'you steady the lantern beside me '
                                                                       'makes the room feel awfully '
                                                                       'gentle, Aether.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_carpenter_shop_base.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N11': {'node_id': 'N11',
                   'chapter_id': 'CH2',
                   'title': 'Embroidery & Red Coals',
                   'day_label': 'Day 6 - Late Afternoon',
                   'location': "Feiyun Slope - Lin Wan's Silk Shop",
                   'beats': [{'beat_id': 'N11_B01',
                              'speaker': 'Narrator',
                              'text': 'On the sixth afternoon, bolts of embroidered brocade flutter '
                                      "outside Lin Wan's shopfront as merchants hurry home for festival "
                                      'prep.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B02',
                              'speaker': 'Narrator',
                              'text': 'Hu Tao carries the plum-wood Xiao Lantern wrapped in plain white '
                                      "paper, stepping inside with her crisp, courteous Director's bow.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B03',
                              'speaker': 'Hu Tao',
                              'text': 'Good afternoon, Miss Lin. An anonymous patron commissioned us to '
                                      "deliver one custom lantern to your counter before tomorrow's eve.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N11_B04',
                              'speaker': 'Narrator',
                              'text': 'The young seamstress barely glances at the Wangsheng lapel before '
                                      'her eyes drop to the bevelled dovetail joint of the plum-wood '
                                      'frame. Her knuckles turn chalk-white.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B05',
                              'speaker': 'Lin Wan',
                              'text': 'Only one stubborn old joiner in Liyue bevels eight-sided mortises '
                                      'without glue! Ten years he throws me out into the rain, and now he '
                                      'sends funeral parlor messengers with mute wood?!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_X1',
                              'speaker': 'Narrator',
                              'text': "Behind Lin Wan's counter hangs a faded sampler stitched in uneven "
                                      "teenage thread -- two swallows perched on a carpenter's square, "
                                      'saved from her childhood room.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_X2',
                              'speaker': 'Lin Wan',
                              'text': "Every winter I left the back latch unlocked on New Year's Eve, "
                                      "thinking he'd swallow that iron temper and walk up Feiyun Slope for "
                                      'one bowl of soup!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_X3',
                              'speaker': 'Lin Wan',
                              'text': 'If he wants to say something after ten winters, tell him to climb '
                                      'these stone stairs himself instead of hiring Wangsheng couriers!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_X4',
                              'speaker': 'Narrator',
                              'text': "Tears of wounded pride spill down the young seamstress's cheeks -- "
                                      'completely unaware that the old joiner she waits for has already '
                                      'crossed the border.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B06',
                              'speaker': 'Narrator',
                              'text': 'Trembling with old heartbreak, Lin Wan snatches the lantern and '
                                      'swings it straight toward the open iron charcoal brazier heating '
                                      'her shop!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N11_B07',
                              'speaker': 'Narrator',
                              'text': "Bound by Wangsheng's sacred non-disclosure seal, Hu Tao's lips "
                                      'press into a tight, pained line -- forbidden by oath from speaking '
                                      "Old Lin's name or revealing his death.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N12'}],
                   'ending_id': None},
           'N12': {'node_id': 'N12',
                   'chapter_id': 'CH2',
                   'title': 'Three Breaths in the Twilight Alley',
                   'day_label': 'Day 6 - Dusk',
                   'location': 'Feiyun Back Alley - Canal Steps',
                   'beats': [{'beat_id': 'N12_X1',
                              'speaker': 'Narrator',
                              'text': 'Time slows in the warm glow of the silk shop: one word too many '
                                      "breaks Wangsheng's sacred contract, while total silence lets ten "
                                      'years of hidden devotion burn to ash.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_X2',
                              'speaker': 'Hu Tao',
                              'text': 'Miss Lin, wait -- please look closely at the woodwork before the '
                                      'flame catches--!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_X3',
                              'speaker': 'Narrator',
                              'text': 'Hu Tao cannot legally utter why Old Lin cannot climb the stairs '
                                      'himself -- leaving only my unsworn hands free to act.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B01',
                              'speaker': 'Narrator',
                              'text': 'Orange sparks curl up from the iron brazier inches beneath the '
                                      "oiled paper of Old Lin's final handiwork.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N12_B02',
                              'speaker': 'Narrator',
                              'text': "On the underside of the lantern's wooden crosspiece, visible only "
                                      'from my angle, sits a tiny thumb-worn carving of a fledgling '
                                      "swallow -- the emblem stitched onto Lin Wan's own shop banner.",
                              'inner_thought': "I took no blood oath with Wangsheng's ledger, yet Old Lin "
                                               'paid everything to spare his daughter funeral grief.',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C06',
                              'prompt': "Lin Wan's wrist wavers above the red coals while Hu Tao's "
                                        'professional vow holds her tongue.',
                              'options': [{'opt_id': 'C06_A',
                                           'label': "Bend Wangsheng's non-interference rule: catch the "
                                                    'frame above the brazier and point silently to the '
                                                    'swallow carved beneath its base.',
                                           'effects': {'bond': 2,
                                                       'insight': 0,
                                                       'add_flags': ['F06_MERCY_LANTERN']},
                                           'next_node': 'N13',
                                           'reaction_beats': [{'beat_id': 'N12_C06A_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Before you burn it, Miss Lin, turn '
                                                                       'the base over. The hands that '
                                                                       "carved that little swallow won't "
                                                                       'trouble your doorway again -- they '
                                                                       'only wished one warm light into '
                                                                       'your sky.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06A_R2',
                                                               'speaker': 'Narrator',
                                                               'text': "Lin Wan's breath catches as her "
                                                                       'thumb finds the worn wooden '
                                                                       'swallow. Without another word, she '
                                                                       'sinks behind her counter hugging '
                                                                       'the unharmed lantern to her chest '
                                                                       'in silent tears.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06A_R3',
                                                               'speaker': 'Narrator',
                                                               'text': 'Halfway down the quiet twilight '
                                                                       'alley outside, Hu Tao abruptly '
                                                                       'stops walking and leans her temple '
                                                                       'lightly against my shoulder for '
                                                                       'one, two, three slow breaths.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_lean.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06A_R4',
                                                               'speaker': 'Hu Tao',
                                                               'text': 'You break rules far too gently, '
                                                                       "Aether... Promise me you won't go "
                                                                       'prying open stubborn farewells if '
                                                                       'this Director ever has to slip '
                                                                       'away.',
                                                               'inner_thought': 'Memory Kept [Swallow '
                                                                                'Mercy Lantern]: Her '
                                                                                'forehead against my '
                                                                                'shoulder feels fragile as '
                                                                                'paper ash.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_lean.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]},
                                          {'opt_id': 'C06_B',
                                           'label': "Honor Old Lin's fierce pride and Wangsheng's strict "
                                                    'vow: catch the lantern back gently and release it for '
                                                    'him ourselves at dusk.',
                                           'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                           'next_node': 'N13',
                                           'reaction_beats': [{'beat_id': 'N12_C06B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'Accepting her refusal without '
                                                                       "breaking Old Lin's shield, Hu Tao "
                                                                       'and I retrieve the unburned '
                                                                       'lantern and carry it down to the '
                                                                       'quiet canal steps as dusk settles.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N12_C06B_R2',
                                                               'speaker': 'Hu Tao',
                                                               'text': 'Watch how straight it climbs, '
                                                                       'Aether... Sometimes pushing '
                                                                       'someone away is the very last '
                                                                       'kindness a dying person has left '
                                                                       'to give.',
                                                               'inner_thought': 'Insight Gained: She '
                                                                                "wasn't talking about Old "
                                                                                'Lin alone -- she is '
                                                                                'rehearsing her own '
                                                                                'farewell.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_alley_dusk_base.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N13': {'node_id': 'N13',
                   'chapter_id': 'CH2',
                   'title': 'Snow-Plum Crimson at Sunset',
                   'day_label': 'Day 7 - Sunset',
                   'location': 'Liyue Harbor - Southern Stone Pier',
                   'beats': [{'beat_id': 'N13_B01',
                              'speaker': 'Narrator',
                              'text': 'Two days remain before the grand Mingxiao Lantern rises. Sunset on '
                                      'the seventh evening pours molten vermilion across the harbor waves.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B02',
                              'speaker': 'Hu Tao',
                              'text': 'Ta-da! Keep your eyes front and center, Traveler -- Chef Xiangling '
                                      'stayed up till rooster-crow finishing my New Year coat!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N13_B03',
                              'speaker': 'Narrator',
                              'text': 'Hands clasped neatly behind her back, Hu Tao executes a crisp, '
                                      'buoyant spin on the sunlit flagstones in crisp snow-laden crimson '
                                      'and ivory festive tailoring.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_X1',
                              'speaker': 'Aether',
                              'text': 'Wait -- let me guess first. Guoba tried helping Xiangling iron the '
                                      'sleeves and nearly toasted the cuffs?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_X2',
                              'speaker': 'Hu Tao',
                              'text': 'Hahaha! Close -- Xiangling had to bribe Guoba with three plates of '
                                      'almond-crusted Mora meat just to guard the sewing basket!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N13_X3',
                              'speaker': 'Narrator',
                              'text': 'Orange harbor light catches the gold filigree along her festive '
                                      'collar and the curiously smooth, unadorned dark curve of her hat '
                                      'brim above her bright eyes.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_X4',
                              'speaker': 'Hu Tao',
                              'text': 'Look closer than the tailoring, silly! Every single day since we '
                                      'met in Wuwang woods, one signature piece has never left its perch '
                                      '-- until five minutes ago!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N13_B04',
                              'speaker': 'Narrator',
                              'text': 'Before calling me over to the pier, she had already fussed with her '
                                      'Harmony Hexagram Hat in private. Beneath the golden sunset, its '
                                      'dark hexagonal brim carries only the gold paper talisman and black '
                                      'ribbon -- completely bare of its signature crimson plum branch.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N13_B05',
                              'speaker': 'Hu Tao',
                              'text': 'Well, Assistant Aether? Four days under my roof ought to have '
                                      'sharpened your eyes! Tell me -- what looks different about your '
                                      'Director this evening?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': 'vn_playful_tease'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N14'}],
                   'ending_id': None},
           'N14': {'node_id': 'N14',
                   'chapter_id': 'CH2',
                   'title': 'What Was Missing From Her Brim',
                   'day_label': 'Day 7 - Sunset',
                   'location': 'Liyue Harbor - Southern Stone Pier',
                   'beats': [{'beat_id': 'N14_X1',
                              'speaker': 'Narrator',
                              'text': 'Behind us on the wharf, dockworkers hoist strings of red silk '
                                      "lanterns up the masts of Beidou's anchored fleet.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_X2',
                              'speaker': 'Hu Tao',
                              'text': 'Tick-tock, Assistant Aether -- sundown waits for no traveler! Tell '
                                      'me what your sharp golden eyes see, or forfeit your chestnut '
                                      'ration!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N14_X3',
                              'speaker': 'Narrator',
                              'text': 'Beneath the playful challenge, a quiet vulnerability shimmers in '
                                      'her gaze -- hoping without asking that I know every detail of her '
                                      'heart by sight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B01',
                              'speaker': 'Narrator',
                              'text': 'Sea gulls wheel past anchored merchant junks as Hu Tao rocks onto '
                                      'her tiptoes, eyes sparkling with half-teasing, half-breathless '
                                      'expectation.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N14_B02',
                              'speaker': 'Narrator',
                              'text': 'Her wide festive right sleeve hangs heavier than usual behind her '
                                      'waist, shielding something slender from the salt breeze while the '
                                      'dark brim of her hat sits unusually empty.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C07',
                              'prompt': 'Sunset gilds her new snow-crimson coat and the bare dark brim of '
                                        'her Harmony Hexagram Hat.',
                              'options': [{'opt_id': 'C07_A',
                                           'label': 'Look past the new crimson silk toward the bare dark '
                                                    "brim of her Harmony Hexagram Hat: 'Your crimson plum "
                                                    "branch... where did it go?'",
                                           'effects': {'bond': 1,
                                                       'insight': 1,
                                                       'add_flags': ['F07_PLUM_BRANCH']},
                                           'next_node': 'N15',
                                           'reaction_beats': [{'beat_id': 'N14_C07A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'The playful banter freezes on Hu '
                                                                       "Tao's lips. Slowly, color rises "
                                                                       'across the bridge of her nose '
                                                                       'brighter than the harbor dusk.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_plum_gift.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07A_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Drawing her hand from her wide '
                                                                       'sleeve, she reveals the living '
                                                                       'crimson plum branch grafted from '
                                                                       'her own courtyard tree -- warm '
                                                                       'with a quiet pulse of her own Pyro '
                                                                       'life-spark -- and presses it into '
                                                                       'my palm.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_plum_gift.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07A_R3',
                                                               'speaker': 'Hu Tao',
                                                               'text': 'Nothing gets past you, huh... Keep '
                                                                       'it safe over your heart for me, '
                                                                       'Aether. Everyone in Liyue gives '
                                                                       'you lucky coins, so I wanted you '
                                                                       'carrying the one thing nobody else '
                                                                       'in this world has.',
                                                               'inner_thought': 'Keepsake Entrusted '
                                                                                '[Crimson Plum Branch]: '
                                                                                'Her hat stays bare as its '
                                                                                'living warmth beats '
                                                                                'against my palm.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_plum_gift.jpg',
                                                               'voice_emotion': 'vn_shy_blush'}]},
                                          {'opt_id': 'C07_B',
                                           'label': 'Smile warmly at her spin and tell her how bright the '
                                                    'snow-plum crimson looks compared to her usual dark '
                                                    'parlor coat.',
                                           'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N15',
                                           'reaction_beats': [{'beat_id': 'N14_C07B_R1',
                                                               'speaker': 'Aether',
                                                               'text': 'Xiangling outdid herself. Seeing '
                                                                       'you in bright snow-crimson makes '
                                                                       'the whole pier look like spring '
                                                                       'arrived early.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N14_C07B_R2',
                                                               'speaker': 'Hu Tao',
                                                               'text': 'Hehe! Flattery earns you ten bonus '
                                                                       'points on your performance review! '
                                                                       "Come on -- let's walk back before "
                                                                       'the evening chill sets in!',
                                                               'inner_thought': 'Hidden behind her back, '
                                                                                'her fingers curl '
                                                                                'wistfully around the '
                                                                                'ungiven branch inside her '
                                                                                'bare-hatted silhouette.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_barehat_base.jpg',
                                                               'voice_emotion': 'vn_sweet_happy'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N15': {'node_id': 'N15',
                   'chapter_id': 'CH2',
                   'title': 'Cracked Cedar & Legal Seals',
                   'day_label': 'Day 7 - Early Dusk',
                   'location': 'Wangsheng Funeral Parlor - Front Courtyard',
                   'beats': [{'beat_id': 'N15_B01',
                              'speaker': 'Narrator',
                              'text': "We barely reach Wangsheng's red gates at dusk when a deep, "
                                      'sub-audible groan rolls southward beneath the flagstones straight '
                                      'from Wuwang Hill.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B02',
                              'speaker': 'Narrator',
                              'text': "CRACK! Overhead, the seasoned cedar tie-beam supporting Wangsheng's "
                                      'main hall porch splits lengthwise, raining three gray roof tiles '
                                      'onto the courtyard stones!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B03',
                              'speaker': 'Aether',
                              'text': 'Watch out above you, Hu Tao!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B04',
                              'speaker': 'Narrator',
                              'text': 'I sweep her clear of the falling slate just as rapid footsteps '
                                      'clatter around the street corner -- Yanfei, thick festival '
                                      'building-code codex tucked under her arm, skidding to a halt at the '
                                      'gate.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B05',
                              'speaker': 'Yanfei',
                              'text': 'Whoa, I felt that ground-shift from two blocks away! Nobody step '
                                      'under that load-bearing beam -- under Liyue Municipal Safety '
                                      'Statute Article Twelve, a split ridge timber is an immediate '
                                      'hazard!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_X1',
                              'speaker': 'Yanfei',
                              'text': 'Look at the fracture grain along that cedar tie-beam, Aether -- '
                                      'split clean from underneath by a northward subterranean shockwave, '
                                      'not dry rot!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_X2',
                              'speaker': 'Aether',
                              'text': 'Is the rest of Chihu Rock damaged, Yanfei?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_X3',
                              'speaker': 'Yanfei',
                              'text': 'Only foundations sitting directly along the old northern root vein! '
                                      'Ningguang already has Ministry engineers checking the upper wards, '
                                      'so nobody enters this hall until the carpenters brace it!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_X4',
                              'speaker': 'Narrator',
                              'text': 'While Yanfei measures the split timber with practiced precision, Hu '
                                      'Tao quietly shifts half a step into the dusk shadow of the side '
                                      'colonnade.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B06',
                              'speaker': 'Yanfei',
                              'text': "Sorry, Director Hu! Until the Ministry's master carpenters shore "
                                      "that beam up, I'm issuing a mandatory forty-eight-hour structural "
                                      "seal on Wangsheng's main residence -- effective until New Year's "
                                      'Night!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N15_B07',
                              'speaker': 'Hu Tao',
                              'text': 'Oya, forty-eight hours?! Well, the law is the law, Miss Legal '
                                      'Adviser -- paste the seal straight so it looks festive!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': 'vn_playful_tease'}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N16'}],
                   'ending_id': None},
           'N16': {'node_id': 'N16',
                   'chapter_id': 'CH2',
                   'title': 'Embers on White Silk',
                   'day_label': 'Day 7 - Dusk',
                   'location': 'Wangsheng Side Corridor - Lantern Shadow',
                   'beats': [{'beat_id': 'N16_B01',
                              'speaker': 'Narrator',
                              'text': 'The instant Yanfei turns toward the front pillar to stamp her '
                                      "vermilion forty-eight-hour repair notice, Hu Tao's bright posture "
                                      'falters.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B02',
                              'speaker': 'Narrator',
                              'text': 'Beneath her bare-brimmed Hexagram Hat, she slips swiftly behind the '
                                      "shadow of the side corridor's paper lantern, pressing a folded "
                                      'white silk handkerchief hard against her lips to muffle a dry, '
                                      'rattling cough.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_X1',
                              'speaker': 'Narrator',
                              'text': 'Another muted cough catches behind her sleeve -- quiet, dry, and '
                                      'accompanied by a faint hiss like frost hitting hot iron.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_X2',
                              'speaker': 'Aether',
                              'text': 'Hu Tao, your voice sounded strained just now. Let me take a look.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_X3',
                              'speaker': 'Hu Tao',
                              'text': 'Nuh-uh, stay right by that stone lion! Since when does an assistant '
                                      "barge in while a lady's fixing her ribbon?!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N16_B03',
                              'speaker': 'Hu Tao',
                              'text': 'Stay out by the courtyard gate a second, Aether! Just tile dust in '
                                      'my throat -- and my collar ribbon came undone when you pulled me '
                                      'back!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N16_B04',
                              'speaker': 'Narrator',
                              'text': 'No tile dust fell anywhere near her face. Even from five paces '
                                      'away, the air around that shadowy corridor pillar drops three '
                                      'degrees colder.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C08',
                              'prompt': 'Hu Tao turns into the dark lantern alcove, shielding her '
                                        'trembling right hand from view.',
                              'options': [{'opt_id': 'C08_A',
                                           'label': 'Cross into the lantern shadow despite her request and '
                                                    'catch sight of the handkerchief before she balls it '
                                                    'up.',
                                           'effects': {'bond': 0,
                                                       'insight': 2,
                                                       'add_flags': ['F08_ASH_COUGH_SEEN']},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_C08A_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'I step silently past the pillar '
                                                                       'before she can fold the cloth '
                                                                       'away. Hu Tao stiffens, whirling '
                                                                       'half around with wide, betrayed '
                                                                       'eyes.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_ash_cough_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08A_R2',
                                                               'speaker': 'Narrator',
                                                               'text': 'Staining the snow-white silk is '
                                                                       'not red blood, but a streak of '
                                                                       'jet-black smoldering ash whose '
                                                                       'cold yin-sparks eat tiny pinholes '
                                                                       'straight through the weave!',
                                                               'inner_thought': 'Clue Recorded [Smoldering '
                                                                                'Yin-Ash Cough]: Border '
                                                                                'fetor is burning her '
                                                                                'lungs into ash from the '
                                                                                'inside.',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_ash_cough_diff.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08A_R3',
                                                               'speaker': 'Hu Tao',
                                                               'text': '...I told you not to look, Aether. '
                                                                       'Just residual soot from sealing '
                                                                       "Tuesday's incense brazier -- don't "
                                                                       'breathe a word to Yanfei.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_ash_cough_diff.jpg',
                                                               'voice_emotion': ''}]},
                                          {'opt_id': 'C08_B',
                                           'label': 'Respect her boundary: stand guard facing the '
                                                    'courtyard to block the cold draft and hand her a '
                                                    'flask of warm tea when she steps out.',
                                           'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                           'next_node': 'N17',
                                           'reaction_beats': [{'beat_id': 'N16_C08B_R1',
                                                               'speaker': 'Narrator',
                                                               'text': 'I halt at the edge of the light, '
                                                                       'turning my back to shield the '
                                                                       "alcove from Yanfei's view and "
                                                                       'unscrewing my warm bamboo tea '
                                                                       'flask.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                                                               'voice_emotion': ''},
                                                              {'beat_id': 'N16_C08B_R2',
                                                               'speaker': 'Hu Tao',
                                                               'text': '...Thanks, Assistant Aether. You '
                                                                       'always know right where to stand '
                                                                       'so a girl keeps her dignity '
                                                                       'intact.',
                                                               'inner_thought': '',
                                                               'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                                                               'voice_emotion': 'vn_tender_love'}]}]},
                   'routing': [],
                   'ending_id': None},
           'N17': {'node_id': 'N17',
                   'chapter_id': 'CH2',
                   'title': 'First Watch Bell & Three Diverging Roads',
                   'day_label': 'Day 7 - Night (First Watch)',
                   'location': 'Wangsheng Gate - Crossroads Under Lantern Fog',
                   'pre_events': [{'when': {'forbid_flags': ['F07_PLUM_BRANCH'],
                                            'min_bond': 10,
                                            'min_insight': 6},
                                   'effects': {'add_flags': ['F07_PLUM_BRANCH', 'F07_SECOND_CHANCE_N17']}}],
                   'beats': [{'beat_id': 'N17_B01',
                              'speaker': 'Narrator',
                              'text': 'By the time Yanfei finishes affixing her forty-eight-hour safety '
                                      "seal across Wangsheng's main doors and hurries back toward Yujing "
                                      'Terrace, the first-watch bell tolls across the misty harbor.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B02',
                              'speaker': 'Hu Tao',
                              'text': "Well, there goes our roof until New Year's Night! Take your "
                                      'well-earned leave back at your inn or the Serenitea Pot, Aether.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': 'greet_doorstep'},
                             {'beat_id': 'N17_B03',
                              'speaker': 'Aether',
                              'text': 'And where exactly is the 77th Director sleeping tonight with the '
                                      'parlor sealed?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B04',
                              'speaker': 'Hu Tao',
                              'text': 'Me? Wangsheng keeps a dry storehouse halfway up Wuwang Hill! Gotta '
                                      'count the last crates of ceremonial beeswax candles before New '
                                      "Year's Eve anyway.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N17_B05',
                              'speaker': 'Narrator',
                              'text': 'Her tone is light as spun sugar, yet her bare-brimmed Hexagram Hat '
                                      'tilts slightly against the cold northern wind and her boots are '
                                      'already angled toward the mountain road.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_B06_SC1',
                              'speaker': 'Narrator',
                              'text': 'She takes two brisk steps into the mist -- then stops dead. Her '
                                      'small shoulders tighten before she whirls right back around, ears '
                                      'burning scarlet beneath her bare hat brim.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_plum_gift.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B07_SC2',
                              'speaker': 'Hu Tao',
                              'text': "Ugh, I can't just leave it in my sleeve! Here, dummy -- you were so "
                                      "busy praising Xiangling's tailoring on the pier that you didn't "
                                      'even notice my hat was bare!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_plum_gift.jpg',
                              'voice_emotion': 'vn_shy_blush',
                              'when': {'all_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_B08_SC3',
                              'speaker': 'Narrator',
                              'text': 'She thrusts the warm, living crimson plum branch straight into my '
                                      'palm, closing my fingers over its stem for one fierce second before '
                                      'stepping back.',
                              'inner_thought': 'Second-Chance Keepsake [Crimson Plum Branch]: Deep bond '
                                               'and keen eyes moved her to entrust her life-spark branch '
                                               'after all!',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_harbor_sunset_plum_gift.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F07_SECOND_CHANCE_N17']}},
                             {'beat_id': 'N17_X1',
                              'speaker': 'Aether',
                              'text': 'Beeswax inventory on Wuwang Hill right after a subterranean tremor '
                                      "cracked your main beam? Even Paimon wouldn't buy that cover story.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N17_X2',
                              'speaker': 'Hu Tao',
                              'text': "Hehe, Paimon's busy grading sweet-and-sour pork right now, so her "
                                      "vote is absent! Don't look at me like I'm marching off to war, "
                                      "Aether -- borders are Wangsheng's everyday backyard.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N17_B09_REPIN',
                              'speaker': 'Narrator',
                              'text': 'Before turning toward the fog, Hu Tao quietly slips the ungiven '
                                      'crimson plum branch out of her wide sleeve and pins it back onto '
                                      'the dark brim of her hat with a faint, rueful exhale.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': '',
                              'when': {'forbid_flags': ['F07_PLUM_BRANCH']}},
                             {'beat_id': 'N17_B10',
                              'speaker': 'Narrator',
                              'text': "Forty-eight hours remain until New Year's Eve midnight. Whatever "
                                      'crisis is gathering beneath Wuwang Hill, my next move right here at '
                                      'the parlor gate will decide which road we walk.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                              'voice_emotion': ''}],
                   'choice': {'choice_id': 'C09',
                              'prompt': 'Hu Tao turns toward the foggy northern stone steps. Choose how '
                                        'you answer her excuse:',
                              'options': [{'opt_id': 'C09_ROUTE_A',
                                           'label': '[Route A - Wuwang Veil] Catch her cold sleeve right '
                                                    "now: 'Stop hiding behind candle inventories. Wherever "
                                                    "the border is cracking, I walk beside you.'",
                                           'effects': {'bond': 1, 'insight': 0, 'add_flags': ['ROUTE_A']},
                                           'next_node': 'N18_A1'},
                                          {'opt_id': 'C09_ROUTE_B',
                                           'label': "[Route B - Seven Gates] Hold back so she doesn't hide "
                                                    'deeper, then investigate Yujing Terrace and '
                                                    "Wangsheng's study to uncover the whole array.",
                                           'effects': {'bond': 0, 'insight': 1, 'add_flags': ['ROUTE_B']},
                                           'next_node': 'N22_B1'},
                                          {'opt_id': 'C09_ROUTE_C',
                                           'label': "[Route C - Borrowed Spring] Hold up Yanfei's 48-hour "
                                                    "repair notice and the Serenitea Pot: 'Mandatory rest "
                                                    "under warm spring eaves until New Year's Eve!'",
                                           'effects': {'bond': 1, 'insight': 0, 'add_flags': ['ROUTE_C']},
                                           'next_node': 'N26_C1'}]},
                   'routing': [],
                   'ending_id': None},
           'N18_A1': {'node_id': 'N18_A1',
                      'chapter_id': 'CH3',
                      'title': "Chongyun's Outer Ward",
                      'day_label': 'Day 7 - Late Night',
                      'location': 'Wuwang Hill - Outer Talisman Perimeter',
                      'beats': [{'beat_id': 'N18_B01',
                                 'speaker': 'Narrator',
                                 'text': 'My fingers close gently but immovably around the cold silk of Hu '
                                         "Tao's sleeve before she can take another step into the harbor "
                                         'fog.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B02',
                                 'speaker': 'Aether',
                                 'text': 'Stop hiding behind beeswax candle counts, Hu Tao. Wherever the '
                                         "border is cracking tonight, I'm walking beside you.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B03',
                                 'speaker': 'Hu Tao',
                                 'text': "...Stubborn as stone, aren't you? Even if I ordered you back as "
                                         "Director, you'd just trail fifty paces behind in the dark.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                                 'voice_emotion': 'vn_tender_love'},
                                {'beat_id': 'N18_B04',
                                 'speaker': 'Hu Tao',
                                 'text': "Fine. One non-negotiable rule: once we pass Chongyun's outer "
                                         'ward, do not let go of my coat hem -- not for a single breath.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B05',
                                 'speaker': 'Narrator',
                                 'text': "Halfway up Wuwang's pine ridge, paper exorcism sigils snap "
                                         'violently in a freezing gale. Chongyun steps from behind a '
                                         'frost-rimed torii, greatsword drawn against stray yin-wisps.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_X1',
                                 'speaker': 'Narrator',
                                 'text': 'Side by side we climb the steep, moss-slick steps above Qingce '
                                         'while harbor lights shrink into a distant amber ribbon behind '
                                         'us.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_X2',
                                 'speaker': 'Hu Tao',
                                 'text': 'Keep your left fingers hooked in my sash, okay? Grandpa taught '
                                         "me that Wuwang's deep fog loves separating people who think "
                                         "they're strong enough to walk two paces apart.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_X3',
                                 'speaker': 'Chongyun',
                                 'text': 'Even my congenital positivity barely keeps the frost off my hilt '
                                         "tonight, Director Hu! Whatever woke up under the summit isn't "
                                         'ordinary spirit static!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_X4',
                                 'speaker': 'Aether',
                                 'text': 'Fall back to the village perimeter and guard the evacuees, '
                                         'Chongyun -- Hu Tao and I will handle the inner arch!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B06',
                                 'speaker': 'Chongyun',
                                 'text': 'Director Hu! Traveler! My yang-spirit talismans are burning '
                                         'through at triple speed -- the fog beyond the stone arch is '
                                         'warping space itself!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N18_B07',
                                 'speaker': 'Narrator',
                                 'text': 'Before Hu Tao can answer, the ground beneath the torii buckles '
                                         '-- no, drops upward into a silent tide of colorless ash! Wind '
                                         "tears Hu Tao's hat loose onto its neck cord behind her shoulders "
                                         'as we plunge together into the rift!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N19_A2'}],
                      'ending_id': None},
           'N19_A2': {'node_id': 'N19_A2',
                      'chapter_id': 'CH3',
                      'title': 'The Monochrome Border',
                      'day_label': 'Day 8 - Time-Dilated Mist',
                      'location': 'Wuwang Seam - Monochrome Spirit Border',
                      'beats': [{'beat_id': 'N19_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Sound dies first; color follows. When we regain our footing on '
                                         'cracked gray slate, pine needles, clouds, and stone alike have '
                                         'bleached into the silver-gray of old charcoal.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Only two things in this silent world still hold living hue: the '
                                         'golden starlight along my scarf, and the scarlet Pyro '
                                         "butterflies circling Hu Tao's bare, wind-tossed twin-tails.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_X1',
                                 'speaker': 'Hu Tao',
                                 'text': 'Silly churl, billy churl, silly-billy hilichurl... Hum the beat '
                                         'back to me if the gray fog tries muffling your ears, Aether!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N19_X2',
                                 'speaker': 'Aether',
                                 'text': 'Using your infamous hilichurl nursery rhyme as an anti-miasma '
                                         'mantra? Strangely enough, it actually works.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_X3',
                                 'speaker': 'Narrator',
                                 'text': 'Every time her brass bells ring three beats, crimson Pyro '
                                         'butterflies burn a narrow path across the colorless stone -- yet '
                                         'each step costs her cold right wrist a sharper tremor.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_X4',
                                 'speaker': 'Hu Tao',
                                 'text': 'Almost to the upper seam... Whatever phantom the border throws '
                                         "in front of your eyes next, remember it's only feeding on "
                                         'unspoken fear!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B03',
                                 'speaker': 'Hu Tao',
                                 'text': 'Stay close! We fell into a time-dilated fold of the border -- '
                                         'one slow watch down here costs an entire day and night up in '
                                         'Liyue!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N19_B04',
                                 'speaker': 'Narrator',
                                 'text': 'Every breath inside the gray fog pulls freezing needles across '
                                         "her lungs. Even while weaving Homa's crimson seals with her "
                                         'stiff right hand, she keeps positioning herself half a step '
                                         'ahead of me.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C10_A',
                                 'prompt': "Whispers curl through the monochrome fog as Hu Tao's right "
                                           'wrist trembles around Staff of Homa.',
                                 'options': [{'opt_id': 'C10_A1',
                                              'label': "Match your breathing to Hu Tao's brass bell "
                                                       'cadence and decipher the ley-memory pulse of the '
                                                       'border mist.',
                                              'effects': {'bond': 1, 'insight': 1, 'add_flags': []},
                                              'next_node': 'N20_A3',
                                              'reaction_beats': [{'beat_id': 'N19_C10A1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Syncing my inhale to the '
                                                                          'three-beat chime at her waist, '
                                                                          'I spot the pattern: the mist '
                                                                          "isn't attacking flesh -- it is "
                                                                          'hunting unhealed fears in '
                                                                          'memory.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C10_A2',
                                              'label': "Drape your warm elemental aura across Hu Tao's "
                                                       'shivering shoulders so she can weave her Homa '
                                                       'seals unhindered.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N20_A3',
                                              'reaction_beats': [{'beat_id': 'N19_C10A2_R1',
                                                                  'speaker': 'Hu Tao',
                                                                  'text': '...Show-off. Your starlight '
                                                                          'feels like standing beside '
                                                                          "Wanmin's stove in midwinter. "
                                                                          'Keep holding on, okay?',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                                                  'voice_emotion': 'vn_tender_love'}]}]},
                      'routing': [],
                      'ending_id': None},
           'N20_A3': {'node_id': 'N20_A3',
                      'chapter_id': 'CH3',
                      'title': 'A Headstone One Thousand Years Away',
                      'day_label': 'Day 8 Night - Inside the Seam',
                      'location': 'Monochrome Border - Mirage of Future Liyue',
                      'beats': [{'beat_id': 'N20_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Without warning, the gray slate ahead ripples like disturbed '
                                         'water -- and shapes itself into the single terror I have never '
                                         'confessed to a living soul in Teyvat.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Towering unfamiliar pagodas of a Liyue Harbor one thousand years '
                                         'in the future loom through ash. Behind a ruined courtyard wall '
                                         'stands a gnarled, petrified plum tree -- and beneath it, a '
                                         'weather-worn granite headstone.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B03',
                                 'speaker': 'Narrator',
                                 'text': 'Half-erased by centuries of rain, the carved inscription reads: '
                                         "'Here rests Hu Tao -- Seventy-Seventh Director of Wangsheng.' "
                                         'Around it stretches ten thousand years of empty starlight where '
                                         'only I remain.',
                                 'inner_thought': 'Every world I have outlived claws at my throat at once. '
                                                  'This is why immortals never tie their hearts to '
                                                  'fireworks.',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B04',
                                 'speaker': 'Narrator',
                                 'text': 'Right in front of that phantom grave, warm crimson butterflies '
                                         'cleave the gray mirage! Hair streaming unbound in the wind, the '
                                         'real nineteen-year-old Hu Tao thrusts her bare left hand back '
                                         'toward me.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_X1',
                                 'speaker': 'Narrator',
                                 'text': 'Whispers rise out of the phantom stone in my own voice -- '
                                         'reminding me of fallen stars, of worlds turned to ash while only '
                                         'the traveler walked on unchanged.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_X2',
                                 'speaker': 'Hu Tao',
                                 'text': "You've carried that quiet, polite wall inside your chest every "
                                         "year I've known you! Always ready to block a blade for me, "
                                         'always terrified to stay for breakfast!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B05',
                                 'speaker': 'Hu Tao',
                                 'text': 'Aether, look at me! Stop staring at a cold stone from a thousand '
                                         'years away -- look at the girl standing alive right in front of '
                                         'you!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N20_B06',
                                 'speaker': 'Hu Tao',
                                 'text': "So what if mortals don't last ten thousand years?! Take my hand "
                                         "and let's hold a proper Wangsheng funeral to bury that lonely "
                                         'dread of yours right here!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                 'voice_emotion': 'vn_tender_love'}],
                      'choice': {'choice_id': 'C11_A',
                                 'prompt': "Between the phantom thousand-year headstone and Hu Tao's "
                                           'living outstretched hand, the border demands your answer:',
                                 'options': [{'opt_id': 'C11_A1_MORTAL_VOW',
                                              'label': 'Step past the phantom headstone and lace all ten '
                                                       'fingers through hers: choose one finite lifetime '
                                                       'beside her over a painless eternity.',
                                              'effects': {'bond': 2,
                                                          'insight': 1,
                                                          'add_flags': ['F09_MORTAL_VOW']},
                                              'next_node': 'N21_A4',
                                              'reaction_beats': [{'beat_id': 'N20_C11A1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'I crush the mirage stone '
                                                                          'underfoot and lock all ten '
                                                                          'fingers through hers. Her palm '
                                                                          'is fierce and trembling and '
                                                                          'unmistakably real.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_vow_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A1_R2',
                                                                  'speaker': 'Aether',
                                                                  'text': 'Let a thousand years wait their '
                                                                          "turn, Hu Tao. Right now, I'm "
                                                                          'not trading a single morning '
                                                                          "you're in!",
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_vow_diff.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A1_R3',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Golden starlight and crimson '
                                                                          'Homa flame erupt from our '
                                                                          'joined hands, shattering the '
                                                                          'monochrome sky like stained '
                                                                          'glass!',
                                                                  'inner_thought': 'Vow Sealed [Mortal '
                                                                                   'Vow]: The dread of '
                                                                                   'outliving her no '
                                                                                   'longer stands between '
                                                                                   'our hands.',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_vow_diff.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C11_A2_STOIC_SEVER',
                                              'when': {'min_insight': 6},
                                              'unlock_badge': '[INSIGHT 6]',
                                              'lock_hint': '[LOCKED: Needs Insight 6]',
                                              'label': 'Leave her hand untaken to guard your heart, but '
                                                       "read the mist's ley-structure and cleave the "
                                                       'mirage apart with cold Descender willpower.',
                                              'effects': {'bond': 0,
                                                          'insight': 2,
                                                          'add_flags': ['STOIC_BYPASS_NO_VOW']},
                                              'next_node': 'N21_A4',
                                              'reaction_beats': [{'beat_id': 'N20_C11A2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Unable to promise my heart '
                                                                          'against that future stone, I '
                                                                          'draw my blade instead and slice '
                                                                          'the ley-projection cleanly down '
                                                                          'its seam with clinical '
                                                                          'precision.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N20_C11A2_R2',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'The fog parts -- saving us both '
                                                                          '-- yet Hu Tao slowly lowers her '
                                                                          'unclasped hand to her side with '
                                                                          'a quiet, understanding shadow '
                                                                          'behind her eyes.',
                                                                  'inner_thought': 'Note: We escaped '
                                                                                   'unscathed, yet the '
                                                                                   'unspoken wall of '
                                                                                   'eternity remains '
                                                                                   'between us.',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C11_A3_HESITATE_FALL',
                                              'label': 'Flinch half a step back from her outstretched hand '
                                                       "in terror of outliving her: 'Let me shield you "
                                                       "from a safe distance, Hu Tao...'",
                                              'effects': {'bond': -1, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N30_BAD1_1',
                                              'reaction_beats': [{'beat_id': 'N20_C11A3_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'For half a fatal heartbeat, my '
                                                                          'boots flinch backward before '
                                                                          'the phantom grave. Shock '
                                                                          "flashes across Hu Tao's face -- "
                                                                          'and our Homa resonance snaps in '
                                                                          'two!',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3a_monochrome_mist_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N21_A4': {'node_id': 'N21_A4',
                      'chapter_id': 'CH4',
                      'title': "Fireside Vigil Beneath Tao Dou's Root",
                      'day_label': "Day 9 - New Year's Eve Dusk to Late Night",
                      'location': 'Wuwang Summit - Ancient Petrified Root',
                      'beats': [{'beat_id': 'N21_B01',
                                 'speaker': 'Narrator',
                                 'text': 'When we tear free of the monochrome fold, crimson dusk is '
                                         "already spilling across Wuwang's highest ridge -- an entire day "
                                         "and night spent crossing the dilated seam. Tonight is New Year's "
                                         'Eve.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Before us coils the colossal petrified root of Tao Dou, ringed '
                                         "by eight ancient stone pillars awaiting midnight's Qimen "
                                         'alignment.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B03_F05',
                                 'speaker': 'Aether',
                                 'text': 'Back at the parlor gate two nights ago, you were trying to pull '
                                         "Old Lin's carpenter trick on me -- sending me away cold so you "
                                         'could walk into this circle alone.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F05_CARPENTER_LEDGER']}},
                                {'beat_id': 'N21_B04',
                                 'speaker': 'Hu Tao',
                                 'text': '...No point hiding the ledger anymore. At Boar Hour midnight, '
                                         'Ningguang and the adepti open the Seven-and-Eight-Gates array '
                                         'across Liyue, and the 77th Director must stand here at the Gate '
                                         'of Death.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B05',
                                 'speaker': 'Hu Tao',
                                 'text': 'Listen carefully, Aether: you cannot take my place when the '
                                         "array opens. Only a mortal whose life is recorded in Liyue's Ley "
                                         'Lines can draw the scattered fetor inward -- otherwise the '
                                         'miasma scatters and drowns the harbor.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B06',
                                 'speaker': 'Hu Tao',
                                 'text': 'Once the fetor converges, the Gate exacts Ley Line Obfuscation '
                                         "-- erasing any mortal bound to Teyvat's roots into ash and "
                                         'wiping their name from memory.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B07',
                                 'speaker': 'Narrator',
                                 'text': "Hearing her words, memories from Sumeru's Irminsul and Natlan's "
                                         'Night Kingdom snap together in my mind like flint against steel.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_B08',
                                 'speaker': 'Aether',
                                 'text': "Wait -- 'recorded in Teyvat's roots'! Hu Tao, I was never "
                                         "written into this world's Ley Lines! You can open the "
                                         'convergence as the mortal anchor, and the instant erasure '
                                         'begins, I can reach across the rim and siphon the fetor out '
                                         'through me!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_X1',
                                 'speaker': 'Hu Tao',
                                 'text': 'Look how tiny the harbor docks look from up here, Aether. Every '
                                         'single warm gold speck down there is a family setting out extra '
                                         "chopsticks for tomorrow's reunion.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': 'vn_tender_love'},
                                {'beat_id': 'N21_X2',
                                 'speaker': 'Aether',
                                 'text': "Including Wangsheng's courtyard tomorrow noon -- once we walk "
                                         'back down this mountain together.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N21_X3',
                                 'speaker': 'Hu Tao',
                                 'text': "Hehe... bold promise in front of an ancient stone root! Don't "
                                         'let your campfire tea go cold before Boar Hour, Partner.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': 'vn_sweet_happy'},
                                {'beat_id': 'N21_B09',
                                 'speaker': 'Hu Tao',
                                 'text': "What...?! That's why your pulse stayed clean after Qingce! "
                                         "Still, pulling an entire deity's resentment through bare "
                                         'meridians without a proper ward could shred your arm to bone!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': 'vn_shy_blush'},
                                {'beat_id': 'N21_B10',
                                 'speaker': 'Narrator',
                                 'text': "Two quiet hours remain before midnight's signal lantern rises "
                                         'over distant Liyue Harbor. Beside a small shielded campfire on '
                                         'the cliff edge, Hu Tao sits close beside me, hat resting on the '
                                         'rock.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C12_A',
                                 'prompt': "Distant harbor lanterns glimmer below Wuwang's cliff as "
                                           'midnight approaches:',
                                 'options': [{'opt_id': 'C12_A1_SIPHON_WARD',
                                              'when': {'all_flags': ['F09_MORTAL_VOW', 'F03_WUWANG_LORE'],
                                                       'min_insight': 7},
                                              'unlock_badge': '[SIPHON WARD UNLOCKED]',
                                              'lock_hint': '[LOCKED: Needs Mortal Vow + Tao Dou Lore + '
                                                           'Insight 7]',
                                              'label': "Combine Zhongli's Tao Dou lore with your vow to "
                                                       'carve a Descender Siphon Ward onto your sword '
                                                       'hilt, easing her fear completely.',
                                              'effects': {'bond': 3,
                                                          'insight': 1,
                                                          'add_flags': ['SIPHON_WARD_CARVED']},
                                              'next_node': 'N34_CH5_CONVERGE',
                                              'reaction_beats': [{'beat_id': 'N21_C12A1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Channeling Geo and Anemo along '
                                                                          'my hilt in inverse Qimen order, '
                                                                          'I test-draw a wisp of root '
                                                                          'vapor cleanly into harmless '
                                                                          'golden sparks before her eyes.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_lean.jpg',
                                                                  'voice_emotion': ''},
                                                                 {'beat_id': 'N21_C12A1_R2',
                                                                  'speaker': 'Hu Tao',
                                                                  'text': '...Show-off assistant. Wake me '
                                                                          'ten minutes before midnight, '
                                                                          'okay? For the first time all '
                                                                          "winter... I'm not scared to "
                                                                          'close my eyes.',
                                                                  'inner_thought': 'Her head settles warm '
                                                                                   'and trusting against '
                                                                                   'my shoulder beside the '
                                                                                   'crackling fire.',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_lean.jpg',
                                                                  'voice_emotion': 'vn_tender_love'}]},
                                             {'opt_id': 'C12_A2_VIGIL_WARMTH',
                                              'label': 'Feed dry pine into the campfire and stand quiet '
                                                       'watch over the stone perimeter while she meditates '
                                                       "on Homa's incantation.",
                                              'effects': {'bond': 0, 'insight': 1, 'add_flags': []},
                                              'next_node': 'N34_CH5_CONVERGE',
                                              'reaction_beats': [{'beat_id': 'N21_C12A2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Side by side in steady silence, '
                                                                          'we watch the festival lights '
                                                                          'brighten across the sea until '
                                                                          'the final hour arrives.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4a_taodou_campfire_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N30_BAD1_1': {'node_id': 'N30_BAD1_1',
                          'chapter_id': 'CH4',
                          'title': 'Shattered Resonance & Falling Stone',
                          'day_label': 'Day 8 Dusk - Day 9 Night',
                          'location': 'Wuwang Border -> Sealed Northern Ridge',
                          'beats': [{'beat_id': 'N30_B01',
                                     'speaker': 'Narrator',
                                     'text': 'As chains of freezing gray mist coil around our ankles after '
                                             'my half-step retreat, a blinding pillar of archaic amber Geo '
                                             'pierces the outer fog from above!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B02',
                                     'speaker': 'Narrator',
                                     'text': "Because midnight's array has not yet opened, Zhongli's "
                                             'sky-stone shatters the outer boundary veil without '
                                             'detonating the Ley Lines, dragging both of us out onto '
                                             "Wuwang's wet grass alive -- but spiritually concussed.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_X1',
                                     'speaker': 'Narrator',
                                     'text': "Back in Bubu Pharmacy's quiet ward that evening, Zhongli "
                                             'stands in silence outside the bamboo screen while Baizhu '
                                             "stabilizes Hu Tao's bruised meridians.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_X2',
                                     'speaker': 'Zhongli',
                                     'text': 'A single half-step of hesitation inside a spirit-resonance '
                                             'array cuts deeper than iron, Traveler. Give her tonight to '
                                             'breathe; we will seal the northern ridge by force.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_X3',
                                     'speaker': 'Narrator',
                                     'text': "All through Day 9's muted Lantern Rite, golden adeptal "
                                             'pillars lock northern Wuwang behind a jagged stone '
                                             "quarantine -- saving Liyue's streets at the price of a "
                                             'permanent wound.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_X4',
                                     'speaker': 'Narrator',
                                     'text': "Not once during the fireworks does Hu Tao appear at Wanmin's "
                                             'table or Chihu Rock.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B03',
                                     'speaker': 'Narrator',
                                     'text': "With Hu Tao's Homa meridian bruised from the broken link, "
                                             "Ningguang and the adepti are forced throughout New Year's "
                                             'Eve night to drop a heavy, scarred quarantine seal across '
                                             'all of northern Wuwang Hill.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N30_B04',
                                     'speaker': 'Narrator',
                                     'text': 'Liyue survives the holiday without casualties, yet the '
                                             'border remains a festering wound -- and Hu Tao has not sent '
                                             'a single word since Zhongli carried her home.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [{'default': True, 'next_node': 'N31_BAD1_2'}],
                          'ending_id': None},
           'N31_BAD1_2': {'node_id': 'N31_BAD1_2',
                          'chapter_id': 'CH4',
                          'title': "The Director's Black Umbrella",
                          'day_label': "Day 10 - New Year's Morning Drizzle",
                          'location': 'Wangsheng Funeral Parlor - Rain-Wet Threshold',
                          'beats': [{'beat_id': 'N31_B01',
                                     'speaker': 'Narrator',
                                     'text': "On New Year's morning -- hours after Yanfei's "
                                             'forty-eight-hour beam-repair notice finally expires -- cold '
                                             'spring drizzle washes red firecracker scraps along '
                                             "Wangsheng's stone steps.",
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B02',
                                     'speaker': 'Narrator',
                                     'text': 'Before my knuckles even touch the freshly repaired red door, '
                                             'it swings smoothly inward. Hu Tao does not hide inside.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B03',
                                     'speaker': 'Narrator',
                                     'text': 'Dressed in immaculate dark parlor attire, she steps onto the '
                                             'threshold holding a black oil-paper umbrella edged in '
                                             'painted plum blossoms, its dark canopy tilted to shadow her '
                                             'hat and brow.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B04',
                                     'speaker': 'Narrator',
                                     'text': 'On her lips sits the flawless, courteous smile she reserves '
                                             'for unfamiliar clients -- polished porcelain without a '
                                             'single crack for me to reach through.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_X1',
                                     'speaker': 'Aether',
                                     'text': "Hu Tao, let me explain what I saw in that fog -- I wasn't "
                                             'pulling away from you, I was terrified of losing--',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_X2',
                                     'speaker': 'Hu Tao',
                                     'text': 'Please, Traveler. A Wangsheng Director knows every face of '
                                             'grief by heart. Spare us both an awkward postscript on the '
                                             'doorstep.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_X3',
                                     'speaker': 'Narrator',
                                     'text': 'Rain patters steadily across the oiled black paper of her '
                                             'umbrella -- a fortress of impeccable grace built out of my '
                                             'own hesitation.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B05',
                                     'speaker': 'Hu Tao',
                                     'text': 'Good morning, Honorable Traveler. Wangsheng Funeral Parlor '
                                             'is closed to outside visitors for internal rites throughout '
                                             'the first month.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N31_B06',
                                     'speaker': 'Hu Tao',
                                     'text': "Someone blessed with ten thousand tomorrows shouldn't linger "
                                             'under eaves steeped in mortal parting. You taught me that '
                                             'yourself in the mist. May your next road be clear, Traveler.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_base.jpg',
                                     'voice_emotion': ''}],
                          'choice': {'choice_id': 'C19_BAD1',
                                     'prompt': 'Cold New Year rain beads off the rim of her black '
                                               'oil-paper umbrella between you:',
                                     'options': [{'opt_id': 'C19_A_LEAVE_TALISMAN',
                                                  'label': 'Set your protective talisman quietly upon the '
                                                           'rain-wet stone step and bow back without '
                                                           'forcing her mask to crack.',
                                                  'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                  'next_node': 'END_BAD_1',
                                                  'reaction_beats': [{'beat_id': 'N31_C19A_R1',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'I place the warm talisman '
                                                                              'on the dry edge of the '
                                                                              'threshold and step back '
                                                                              'into the drizzle. Only as '
                                                                              'the red doors close does '
                                                                              'the black umbrella tremble '
                                                                              'once.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_tilt.jpg',
                                                                      'voice_emotion': ''}]},
                                                 {'opt_id': 'C19_B_CALL_HER_NAME',
                                                  'label': "Call out 'Hu Tao' -- not 'Director' -- one "
                                                           'last time across the falling rain as her black '
                                                           'umbrella tilts down to hide her eyes.',
                                                  'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                  'next_node': 'END_BAD_1',
                                                  'reaction_beats': [{'beat_id': 'N31_C19B_R1',
                                                                      'speaker': 'Narrator',
                                                                      'text': 'At the sound of her name, '
                                                                              'her knuckles whiten on the '
                                                                              'bamboo handle -- and the '
                                                                              'black umbrella tilts '
                                                                              'sharply downward, hiding '
                                                                              'her eyes completely until '
                                                                              'the parlor latch clicks '
                                                                              'shut.',
                                                                      'inner_thought': '',
                                                                      'cg': 'ui_assets/story_quest_cgs/hutao/end_bad1_black_umbrella_tilt.jpg',
                                                                      'voice_emotion': ''}]}]},
                          'routing': [],
                          'ending_id': None},
           'N22_B1': {'node_id': 'N22_B1',
                      'chapter_id': 'CH3',
                      'title': 'Secret Council on Yujing Terrace',
                      'day_label': 'Day 8 - Morning',
                      'location': 'Liyue Harbor - Yujing Terrace Pavilion',
                      'beats': [{'beat_id': 'N22_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Letting Hu Tao vanish up the fog-wrapped road without spooking '
                                         'her into deeper secrecy, I rendezvous with Paimon at dawn and '
                                         'climb straight to Yujing Terrace.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Inside a warded pavilion overlooking the docks, Ningguang, '
                                         'Keqing, and Chenyu Vale rattan master Lan Yan stand around a '
                                         'bronze map of eight glowing Ley Line nodes.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B03',
                                 'speaker': 'Keqing',
                                 'text': 'Traveler, Paimon -- good timing. Paimon, could you help our '
                                         'logistics clerks distribute calming incense sachets along the '
                                         'southern pier while we brief Aether?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B04',
                                 'speaker': 'Paimon',
                                 'text': "Leave the pier to Chief Inspector Paimon! Don't hide anything "
                                         "important from Aether while I'm gone!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_X1',
                                 'speaker': 'Aether',
                                 'text': "Wait -- 'stands alone at the Gate of Death'?! Ningguang, what "
                                         'happens to the anchor standing inside the eighth gate when the '
                                         'fetor converges?!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_X2',
                                 'speaker': 'Narrator',
                                 'text': "Silence drops like lead across Yujing Terrace. Keqing's gloved "
                                         'hand tightens around her sword hilt; Ningguang lowers her jade '
                                         'pipe.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_X3',
                                 'speaker': 'Ningguang',
                                 'text': 'Director Hu forbade us from telling you before midnight. She '
                                         'argued -- rightly by Qimen law -- that only a mortal Wangsheng '
                                         'heir can anchor the convergence without scattering plague across '
                                         'the harbor.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_X4',
                                 'speaker': 'Keqing',
                                 'text': "None of us accepted that sitting down, Aether! That's why we "
                                         'summoned Lan Yan from Chenyu Vale at dawn to weave a Ley Line '
                                         'life-sharing tether!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B05',
                                 'speaker': 'Ningguang',
                                 'text': "Once tomorrow's Boar Hour strikes on New Year's Eve, we activate "
                                         "the Seven-and-Eight-Gates Qimen Array to purge Tao Dou's "
                                         'erupting fetor once and for all.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N22_B06',
                                 'speaker': 'Ningguang',
                                 'text': 'Keqing, Ganyu, Shenhe, Conqueror of Demons Xiao, Doctor Baizhu, '
                                         'Captain Beidou, and Yelan hold the seven outer gates. Director '
                                         'Hu Tao stands alone at the eighth -- the Gate of Death.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N23_B2'}],
                      'ending_id': None},
           'N23_B2': {'node_id': 'N23_B2',
                      'chapter_id': 'CH3',
                      'title': 'The Thread That Passed Through Glass',
                      'day_label': 'Day 8 - Afternoon',
                      'location': 'Yujing Terrace - Rattan Spirit Table',
                      'beats': [{'beat_id': 'N23_B01',
                                 'speaker': 'Lan Yan',
                                 'text': "To keep the Gate of Death from crushing Director Hu's life-force "
                                         'immediately, I wove eight Chenyu spirit-grass rattan figures '
                                         "linked through Liyue's Ley Lines to share the strain!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B02',
                                 'speaker': 'Aether',
                                 'text': "Link mine first, Lan Yan. Pull as much of the eighth gate's load "
                                         'onto me as the weave can carry!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B03',
                                 'speaker': 'Narrator',
                                 'text': 'Lan Yan pinches a silver swallow charm and flicks a glowing cyan '
                                         'Ley Line thread straight at my sternum -- and gasps aloud.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B04',
                                 'speaker': 'Narrator',
                                 'text': 'The cyan Ley Line thread passes cleanly through my chest like '
                                         'moonlight through empty air, leaving the eighth rattan doll '
                                         'lying inert and unlit upon the stone table!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_X1',
                                 'speaker': 'Narrator',
                                 'text': 'Staring down at the unlit eighth rattan figure on the stone '
                                         'table, my pulse races faster than combat.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_X2',
                                 'speaker': 'Narrator',
                                 'text': 'To Ningguang and Lan Yan, a Ley Line thread missing my chest is '
                                         'a frustrating technical failure. To someone who stood before '
                                         "Nahida in Sumeru's Sanctuary of Surasthana, it is a lightning "
                                         'bolt of revelation!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_X3',
                                 'speaker': 'Keqing',
                                 'text': 'We move out in twenty minutes to fortify the seven outer gates '
                                         'before nightfall. Where can you help us most, Aether?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B05',
                                 'speaker': 'Lan Yan',
                                 'text': "Huh?! It didn't catch at all! Ah... forgive me, Traveler -- "
                                         'Chenyu spirit-grass must only recognize bloodlines born upon Rex '
                                         "Lapis's soil!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N23_B06',
                                 'speaker': 'Ningguang',
                                 'text': 'A pity, though understandable for a guest from afar. We will '
                                         "reassign that slot to the Millelith's auxiliary jade talisman "
                                         'instead.',
                                 'inner_thought': 'Neither Lan Yan nor Ningguang knows what Irminsul or a '
                                                  "Descender is -- only I realize why Teyvat's Ley Line "
                                                  'thread found zero record inside my chest!',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C13_B',
                                 'prompt': "The unlinked rattan figure lies untouched beside Lan Yan's "
                                           'basket while Keqing prepares sub-gate wards:',
                                 'options': [{'opt_id': 'C13_B_RATTAN',
                                              'label': "Ask Lan Yan if you may keep the 'defective' "
                                                       'unlinked rattan figure anyway to study how its '
                                                       'spirit-weave responds to non-native energy.',
                                              'effects': {'bond': 0,
                                                          'insight': 2,
                                                          'add_flags': ['F10_UNLINKED_RATTAN']},
                                              'next_node': 'N24A_B3',
                                              'reaction_beats': [{'beat_id': 'N23_C13B1_R1',
                                                                  'speaker': 'Lan Yan',
                                                                  'text': "Of course! It hasn't absorbed a "
                                                                          'single drop of Ley Line '
                                                                          "signature yet, so it's "
                                                                          'completely blank -- keep it as '
                                                                          'a lucky charm, Traveler!',
                                                                  'inner_thought': 'Item Acquired '
                                                                                   '[Unlinked Rattan '
                                                                                   'Figure]: A blank '
                                                                                   'spirit-compass '
                                                                                   'completely unbound to '
                                                                                   "Teyvat's Ley Lines.",
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C13_B_SUBGATES',
                                              'label': 'Offer your multi-elemental resonance to reinforce '
                                                       "Keqing and Xiao's seven sub-gates so less fetor "
                                                       'overflows toward Hu Tao.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N24A_B3',
                                              'reaction_beats': [{'beat_id': 'N23_C13B2_R1',
                                                                  'speaker': 'Keqing',
                                                                  'text': 'Having your elemental infusion '
                                                                          'on the outer anchors will '
                                                                          "lighten Director Hu's burden "
                                                                          'considerably. Thank you, Aether '
                                                                          "-- she'll feel that support.",
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_yujing_rattan_base.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N24A_B3': {'node_id': 'N24A_B3',
                       'chapter_id': 'CH3',
                       'title': 'Half-Burned Verse in an Empty Study',
                       'day_label': 'Day 8 Night - Day 9 Afternoon',
                       'location': 'Wangsheng Funeral Parlor - Inner Study',
                       'beats': [{'beat_id': 'N24A_B01',
                                  'speaker': 'Narrator',
                                  'text': 'Late on the eighth night, using the inner courtyard key Hu Tao '
                                          'gave me as her assistant, I slip quietly past the shored-up '
                                          'front porch into her empty study.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B02',
                                  'speaker': 'Narrator',
                                  'text': 'A single tallow candle flickers beside a cold Songluo teacup. '
                                          'Without her mischievous voice filling the corridors, '
                                          'seventy-six generations of dark timber feel intolerably vast.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B03_F11',
                                  'speaker': 'Narrator',
                                  'text': 'Hidden behind the lowest bamboo shelf sits a scorched clay '
                                          'medicine pot -- crusted black with the exact Marrow-Frost lung '
                                          "herbs from Baizhu's confidential slip.",
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': '',
                                  'when': {'all_flags': ['F11_BUBU_HERBS']}},
                                 {'beat_id': 'N24A_B04',
                                  'speaker': 'Narrator',
                                  'text': 'Beneath the brass paperweight of her inkstone, a half-charred '
                                          'scrap of Xuan rice paper catches the candle glow -- saved from '
                                          'the brazier only because her hand snuffed the flame halfway.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B05',
                                  'speaker': 'Narrator',
                                  'text': "Written in Hu Tao's unmistakable slanted calligraphy are five "
                                          'short couplets tracing her own constellation, addressed at the '
                                          "top margin simply: 'For the star that paused under my eaves.'",
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B06',
                                  'speaker': 'Narrator',
                                  'text': 'Right where the sixth and final line was burned away into black '
                                          'ash, a single round water stain has dried crinkled into the '
                                          'paper.',
                                  'inner_thought': "Even while preparing to vanish from Liyue's memory, "
                                                   "the girl who laughs at death couldn't bear to finish "
                                                   'writing goodbye.',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_X1',
                                  'speaker': 'Narrator',
                                  'text': 'Resting neatly inside her top desk drawer are sealed red New '
                                          'Year stipend packets for every Wangsheng ferryman and street '
                                          'sweeper -- signed and dated three days in advance.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_X2',
                                  'speaker': 'Narrator',
                                  'text': 'Even her favorite snow-plum hair ribbon lies folded beside Old '
                                          "Hu's portrait, leaving nothing messy behind for whoever "
                                          'inherits the seventy-eighth ledger.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_X3',
                                  'speaker': 'Aether',
                                  'text': "Not on my watch, seventy-seventh Director. Wangsheng isn't "
                                          'opening applications for a seventy-eighth.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24A_B07_F05',
                                  'speaker': 'Aether',
                                  'text': "Just like Old Lin's unsent letter under the workbench... You "
                                          'really thought burning the sixth line would spare me when '
                                          "tomorrow night ends, didn't you, Hu Tao?",
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': '',
                                  'when': {'all_flags': ['F05_CARPENTER_LEDGER']}},
                                 {'beat_id': 'N24A_B08',
                                  'speaker': 'Narrator',
                                  'text': 'Folding the scorched poem carefully over my heart, I spend the '
                                          'daylight hours of Day 9 searching every northern trail -- '
                                          'blocked at every pass by ancient Qimen mist arrays until dusk '
                                          'calls me back to the harbor bridge.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3b_study_burned_poem_base.jpg',
                                  'voice_emotion': ''}],
                       'choice': None,
                       'routing': [{'default': True, 'next_node': 'N24B_B4'}],
                       'ending_id': None},
           'N24B_B4': {'node_id': 'N24B_B4',
                       'chapter_id': 'CH4',
                       'title': 'The Rex Coin on the Lantern Bridge',
                       'day_label': "Day 9 - New Year's Eve Night",
                       'location': 'Liyue Harbor - Quiet Canal Stone Bridge',
                       'beats': [{'beat_id': 'N24B_B01',
                                  'speaker': 'Narrator',
                                  'text': 'Lantern Rite night blazes across Liyue Harbor. Distant opera '
                                          "drums carry Yun Jin's clear aria over thousands of cheering "
                                          'citizens, yet on the arched stone bridge behind Chihu Rock, one '
                                          'figure stands waiting alone.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B02',
                                  'speaker': 'Zhongli',
                                  'text': 'You found the unfinished scroll in her study, I take it. Before '
                                          'ascending Wuwang Hill at dusk, Director Hu asked me to place '
                                          'this in your palm.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B03',
                                  'speaker': 'Narrator',
                                  'text': 'Zhongli extends an ancient, square-holed bronze Rex Coin -- an '
                                          "heirloom talisman of fortune warmed by Hu Tao's own hands.",
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B04',
                                  'speaker': 'Aether',
                                  'text': 'Zhongli, why let a nineteen-year-old walk into that gate '
                                          "alone?! Can't your power shatter Tao Dou's core right now?!",
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B05',
                                  'speaker': 'Zhongli',
                                  'text': 'Once the Eight Gates array is primed, Traveler, my divine Geo '
                                          'authority is the very flint that slew Tao Dou in antiquity. '
                                          'Were I to step inside the active Gate of Death, the backlash '
                                          'would detonate every Ley Line beneath Liyue Harbor.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_X1',
                                  'speaker': 'Narrator',
                                  'text': "Across the lantern-lit canal, Yun Jin's crystalline opera "
                                          'falsetto rises over silk strings -- singing of an ancient '
                                          'maiden walking fearless into mountain mist so spring may return '
                                          'to the valley.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_X2',
                                  'speaker': 'Zhongli',
                                  'text': 'That child smiled when she handed me this Rex Coin at sunset. '
                                          "Not a forced smile -- the clear, settled gaze of Old Hu's "
                                          'granddaughter.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_X3',
                                  'speaker': 'Zhongli',
                                  'text': 'Yet even the bravest nineteen-year-old heart leaves a trail of '
                                          'breadcrumbs when there is one person she wishes would find her.',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B06',
                                  'speaker': 'Zhongli',
                                  'text': 'Nor could a temporary adeptal freeze cure the rot -- it would '
                                          'merely delay the eruption until Qingming. Yet listen to the '
                                          "sixth verse she left unspoken: 'The lone butterfly left, but "
                                          "not without a trace... A fragrance remained, her Butterfly's "
                                          "Embrace.'",
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''},
                                 {'beat_id': 'N24B_B07',
                                  'speaker': 'Zhongli',
                                  'text': "The Gate of Death erases only what Liyue's Ley Lines record. "
                                          'Knowing what passed through your chest on Yujing Terrace... '
                                          'what door remains unlocked to you alone?',
                                  'inner_thought': '',
                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                  'voice_emotion': ''}],
                       'choice': {'choice_id': 'C14_B',
                                  'prompt': "Zhongli's amber eyes hold steady as the countdown drums "
                                            'toward Boar Hour echo across the water:',
                                  'options': [{'opt_id': 'C14_B1',
                                               'label': "Connect Zhongli's hint to Irminsul and Yujing's "
                                                        'cyan thread: Ley Line erasure cannot touch a '
                                                        "Descender never written into Teyvat's roots!",
                                               'effects': {'bond': 1, 'insight': 2, 'add_flags': []},
                                               'next_node': 'N25_B5_GATE1',
                                               'reaction_beats': [{'beat_id': 'N24B_C14B1_R1',
                                                                   'speaker': 'Zhongli',
                                                                   'text': 'Precisely. You cannot open the '
                                                                           'Gate as its mortal anchor -- '
                                                                           'yet the instant convergence '
                                                                           'completes, your hand can cross '
                                                                           'a threshold that turns native '
                                                                           'gods and mortals alike to ash.',
                                                                   'inner_thought': '',
                                                                   'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                                                   'voice_emotion': ''}]},
                                              {'opt_id': 'C14_B2',
                                               'label': 'Clench the still-warm Rex Coin hard against your '
                                                        'palm and swear to reach her altar before the last '
                                                        'stick of incense burns down.',
                                               'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                               'next_node': 'N25_B5_GATE1',
                                               'reaction_beats': [{'beat_id': 'N24B_C14B2_R1',
                                                                   'speaker': 'Zhongli',
                                                                   'text': 'Hold fast to that resolve, '
                                                                           'Traveler -- look to the sky! '
                                                                           'The hour has struck!',
                                                                   'inner_thought': '',
                                                                   'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                                                   'voice_emotion': ''}]}]},
                       'routing': [],
                       'ending_id': None},
           'N25_B5_GATE1': {'node_id': 'N25_B5_GATE1',
                            'chapter_id': 'CH4',
                            'title': 'Combination Gate #1 -- When the Mingxiao Burns',
                            'day_label': 'Day 9 - Boar Hour Midnight',
                            'location': 'Liyue Harbor Bridge -> Spatial Seam',
                            'beats': [{'beat_id': 'N25_B01',
                                       'speaker': 'Narrator',
                                       'text': 'BOAR HOUR! Above the harbor docks, the colossal Mingxiao '
                                               'Lantern surges into the heavens in a tide of molten gold '
                                               'as ten thousand voices roar New Year blessings!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_X1',
                                       'speaker': 'Narrator',
                                       'text': 'Down on the docks below us, children cheer and point at '
                                               'golden fireworks while Paimon waves two candied apples -- '
                                               'blissfully unaware that high in the northern dark, the '
                                               'Gate of Death has just closed its jaws!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_X2',
                                       'speaker': 'Zhongli',
                                       'text': 'Now, Traveler! If you hold both her living spark and an '
                                               "unrecorded vessel -- strike before Liyue's Ley Lines seal "
                                               'her name behind the shroud!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_X3',
                                       'speaker': 'Narrator',
                                       'text': 'Every clue gathered across nine days converges onto the '
                                               'palm of my right hand in a single breath!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_B02',
                                       'speaker': 'Narrator',
                                       'text': 'At that exact second, dark shockwaves shudder silently '
                                               "down from northern Wuwang. Along Yujing's eaves, all seven "
                                               "auxiliary rattan dolls splinter in unison -- and Hu Tao's "
                                               'distant Pyro signature drops off a cliff!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N25_B03',
                                       'speaker': 'Narrator',
                                       'text': 'Running on foot up the sealed mountain road will take '
                                               'forty minutes -- thirty-nine minutes too late. Only an '
                                               'unlinked spirit medium bound to her living life-spark can '
                                               'cleave a direct Descender rift from this bridge!',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                       'voice_emotion': ''}],
                            'choice': {'choice_id': 'C15_B_GATE1',
                                       'exclusive_rescue_gate': True,
                                       'prompt': "Hu Tao's life-flame is winking out behind Wuwang's "
                                                 'sealed veil right now:',
                                       'options': [{'opt_id': 'C15_B_COMBO_UNLOCK',
                                                    'when': {'all_flags': ['F07_PLUM_BRANCH',
                                                                           'F10_UNLINKED_RATTAN'],
                                                             'any_flags': ['F03_WUWANG_LORE',
                                                                           'F05_CARPENTER_LEDGER',
                                                                           'F08_ASH_COUGH_SEEN'],
                                                             'min_insight': 10},
                                                    'unlock_badge': '[COMBINATION UNLOCKED]',
                                                    'lock_hint': '[LOCKED: Needs Plum Branch + Unlinked '
                                                                 'Rattan + Origin Clue + Insight 10]',
                                                    'label': "Press Hu Tao's living crimson plum branch "
                                                             'into the unlinked rattan figure and cleave a '
                                                             "Descender rift straight to Tao Dou's root!",
                                                    'effects': {'bond': 3,
                                                                'insight': 1,
                                                                'add_flags': ['COMBO1_CLEARED']},
                                                    'next_node': 'N34_CH5_CONVERGE',
                                                    'reaction_beats': [{'beat_id': 'N25_C15_OK_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'I drive the living '
                                                                                'crimson plum branch '
                                                                                'straight into the chest '
                                                                                "of Lan Yan's unlinked "
                                                                                'rattan doll! Unbound by '
                                                                                "Teyvat's Ley Lines, its "
                                                                                'blank weave drinks Hu '
                                                                                "Tao's Pyro spark and "
                                                                                'blazes scarlet-gold!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_rift_combo_diff.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N25_C15_OK_R2',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'With one swing of my '
                                                                                'Descender blade, the air '
                                                                                'above the stone bridge '
                                                                                'tears open directly onto '
                                                                                "Wuwang's summit! Zhongli "
                                                                                'steps back with a faint, '
                                                                                'approving nod as I vault '
                                                                                'straight into the fire!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_rift_combo_diff.jpg',
                                                                        'voice_emotion': ''}]},
                                                   {'opt_id': 'C15_B_FAIL_SPRINT',
                                                    'label': 'Without a complete spatial medium to lock '
                                                             'onto her soul, sprint full-speed against the '
                                                             'cheering festival crowd toward Wuwang Hill!',
                                                    'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                    'next_node': 'N32_BAD2_1',
                                                    'reaction_beats': [{'beat_id': 'N25_C15_FAIL_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Shouldering blindly '
                                                                                'against waves of laughing '
                                                                                'festival-goers under '
                                                                                'falling fireworks, I tear '
                                                                                'my lungs raw racing '
                                                                                'toward the northern gate '
                                                                                'on foot...',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch4b_bridge_zhongli_coin_base.jpg',
                                                                        'voice_emotion': ''}]}]},
                            'routing': [],
                            'ending_id': None},
           'N32_BAD2_1': {'node_id': 'N32_BAD2_1',
                          'chapter_id': 'CH4',
                          'title': 'The Harbor That Forgot Her Name',
                          'day_label': 'Day 10 - Pre-Dawn After Midnight',
                          'location': 'Wangsheng Gate -> Barren Wuwang Summit',
                          'beats': [{'beat_id': 'N32_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Halfway past Chihu Rock toward the mountain road, a wave of '
                                             'purified, sweet-smelling air sweeps down from the hills -- '
                                             'curing every coughing elder in the street at once.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B02',
                                     'speaker': 'Narrator',
                                     'text': 'Then an ice-cold horror grips my spine. Right outside '
                                             'Wangsheng Funeral Parlor, two longtime undertakers hanging '
                                             'New Year lanterns laugh cheerfully to one another.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B03',
                                     'speaker': 'Parlor Ferryman',
                                     'text': "Strange, isn't it? Ever since Old Master Hu the 76th passed "
                                             "six years back, our parlor's run on autopilot without ever "
                                             'naming a 77th Director!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B04',
                                     'speaker': 'Narrator',
                                     'text': "Tao Dou's Gate of Death backlash has woven a local Wuwang "
                                             'Yin-Mist cognitive shroud across every mortal mind bound to '
                                             "Liyue's Ley Lines -- unlike global Irminsul erasure, leaving "
                                             "only Zhongli's ancient contract carved in divine Geo bedrock "
                                             'and my outlander soul untouched!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_X1',
                                     'speaker': 'Aether',
                                     'text': 'What are you talking about?! Director Hu Tao -- nineteen '
                                             'years old, twin-tails, plum-blossom hat -- she stood right '
                                             'under this plaque two nights ago!!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_X2',
                                     'speaker': 'Parlor Ferryman',
                                     'text': 'Whoa, easy there, Traveler! Too much festive wine? If our '
                                             'parlor had a lively young Director like that, how could we '
                                             'possibly forget her?',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_X3',
                                     'speaker': 'Narrator',
                                     'text': "Even the calligraphy on Wangsheng's noticeboard blurs and "
                                             'rewrites itself before mortal eyes under the local Yin-Mist '
                                             'shroud -- wiping every trace that she ever laughed along '
                                             'these stones.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B05',
                                     'speaker': 'Narrator',
                                     'text': "By the time my bleeding boots crest Wuwang's summit under a "
                                             'pale gray dawn, the Qimen circle lies silent and cold.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N32_B06',
                                     'speaker': 'Narrator',
                                     'text': 'Planted upright at the center of gray ash stands the Staff '
                                             'of Homa alone. No footprints lead out of the ring.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                     'voice_emotion': ''}],
                          'choice': None,
                          'routing': [{'default': True, 'next_node': 'N32B_BAD2_2'}],
                          'ending_id': None},
           'N32B_BAD2_2': {'node_id': 'N32B_BAD2_2',
                           'chapter_id': 'CH4',
                           'title': "Next Year's Crimson Butterfly",
                           'day_label': 'Day 10 - Cold Gray Dawn',
                           'location': 'Wuwang Summit - Solitary Staff of Homa',
                           'beats': [{'beat_id': 'N32B_B01',
                                      'speaker': 'Narrator',
                                      'text': 'Far down by the harbor bridge, Zhongli tips a solitary cup '
                                              'of clear rice wine onto the flagstones for a friend nobody '
                                              'beside him can name anymore.',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_X1',
                                      'speaker': 'Narrator',
                                      'text': 'Cold mountain wind scatters gray ash across my knees. Down '
                                              'in the valley, Liyue Harbor wakes healthy, whole, and '
                                              'bright -- bought at a price it can no longer remember '
                                              'paying.',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_homa_ash_base.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_X2',
                                      'speaker': 'Aether',
                                      'text': 'I was thirty minutes too late, Hu Tao... Wait just one more '
                                              "second -- don't fade yet--!",
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_crimson_butterfly_diff.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_X3',
                                      'speaker': 'Hu Tao',
                                      'text': 'Bitter first, sweet last, remember? Keep smiling for both '
                                              'of us under all those stars, Assistant Aether...',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_crimson_butterfly_diff.jpg',
                                      'voice_emotion': 'vn_tender_love'},
                                     {'beat_id': 'N32B_B02',
                                      'speaker': 'Narrator',
                                      'text': 'As I drop to my knees before the cold shaft of Homa, one '
                                              'last translucent crimson Pyro butterfly rises out of the '
                                              'gray ash and settles weightlessly upon my trembling '
                                              'fingertips.',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_crimson_butterfly_diff.jpg',
                                      'voice_emotion': ''},
                                     {'beat_id': 'N32B_B03',
                                      'speaker': 'Hu Tao',
                                      'text': "Oya... don't pull such a tragic face on New Year's Day, "
                                              'Aether. Next Lantern Rite, if a crimson butterfly drifts '
                                              "past your window... that's just your Director dropping by, "
                                              'okay?',
                                      'inner_thought': '',
                                      'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_crimson_butterfly_diff.jpg',
                                      'voice_emotion': 'vn_tender_love'}],
                           'choice': {'choice_id': 'C20_BAD2',
                                      'prompt': 'The last warm crimson spark flickers faint against the '
                                                'cold mountain wind:',
                                      'options': [{'opt_id': 'C20_A_CUP_BUTTERFLY',
                                                   'label': 'Cup both hands gently around the fading '
                                                            'crimson butterfly until its last warm spark '
                                                            'dissolves into your skin, swearing to '
                                                            'remember her across every star.',
                                                   'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                   'next_node': 'END_BAD_2',
                                                   'reaction_beats': [{'beat_id': 'N32B_C20A_R1',
                                                                       'speaker': 'Narrator',
                                                                       'text': 'Warmth kisses my palms one '
                                                                               'final time before '
                                                                               'scattering into morning '
                                                                               'wind, leaving me sole '
                                                                               'keeper of the 77th '
                                                                               "Director's laughter.",
                                                                       'inner_thought': '',
                                                                       'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_crimson_butterfly_diff.jpg',
                                                                       'voice_emotion': ''}]},
                                                  {'opt_id': 'C20_B_CARVE_STONE_NAME',
                                                   'label': "Draw your Descender blade and carve 'Hu Tao "
                                                            "-- 77th Director' deep into the altar rock "
                                                            "where Liyue's Ley Lines can never shroud it.",
                                                   'effects': {'bond': 0, 'insight': 0, 'add_flags': []},
                                                   'next_node': 'END_BAD_2',
                                                   'reaction_beats': [{'beat_id': 'N32B_C20B_R1',
                                                                       'speaker': 'Narrator',
                                                                       'text': 'Golden outlander script '
                                                                               'burns permanently into the '
                                                                               'cold granite beside Staff '
                                                                               'of Homa -- an un-erasable '
                                                                               'monument beneath an '
                                                                               'unremembering sky.',
                                                                       'inner_thought': '',
                                                                       'cg': 'ui_assets/story_quest_cgs/hutao/end_bad2_crimson_butterfly_diff.jpg',
                                                                       'voice_emotion': ''}]}]},
                           'routing': [],
                           'ending_id': None},
           'N26_C1': {'node_id': 'N26_C1',
                      'chapter_id': 'CH3',
                      'title': 'Forty-Eight Hours Under Peach Blossoms',
                      'day_label': 'Day 7 Night - Day 8 Morning',
                      'location': 'Serenitea Pot - Emerald Peak Spring Courtyard',
                      'beats': [{'beat_id': 'N26_B01',
                                 'speaker': 'Aether',
                                 'text': "Yanfei's municipal seal legally condemns Wangsheng's roof for "
                                         "forty-eight hours, Director -- and midnight's ceremony isn't "
                                         'until tomorrow night. Until then, mandatory rest inside the '
                                         'Serenitea Pot.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B02',
                                 'speaker': 'Hu Tao',
                                 'text': 'Oya?! Pulling legal statutes on me now, Assistant Aether? '
                                         'Well... Mister Zhongli DID nag me to conserve my strength before '
                                         "New Year's Eve. Lead the way, landlord!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch2_parlor_beam_crack_base.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N26_B03',
                                 'speaker': 'Narrator',
                                 'text': "Stepping through the teapot's golden chime trades Liyue's "
                                         'late-winter chill for an endless, frostless spring courtyard '
                                         'where out-of-season peach petals drift across warm flagstones.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_X1',
                                 'speaker': 'Hu Tao',
                                 'text': 'Whoa, Tubby! Your courtyard has Mondstadt windwheel asters '
                                         'planted right next to Inazuman sakura and Natlan '
                                         'ember-marigolds!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': 'vn_sweet_happy'},
                                {'beat_id': 'N26_X2',
                                 'speaker': 'Aether',
                                 'text': "One corner left open by the veranda pond if Wangsheng's Director "
                                         'ever wants to graft a red plum sapling.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_X3',
                                 'speaker': 'Hu Tao',
                                 'text': 'Oyaoya, offering long-term real estate leases already? Careful, '
                                         'Landlord -- plum roots dig deep once you invite them in!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N26_X4',
                                 'speaker': 'Narrator',
                                 'text': 'She jokes lightly beside the pond, yet whenever she thinks my '
                                         'back is turned, she warms her stiff right fingers quietly '
                                         'against her teacup.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B04',
                                 'speaker': 'Narrator',
                                 'text': 'Setting her hat aside in the guest wing, Hu Tao slips into a '
                                         'soft crimson indoor cardigan, humming cheerfully as Tubby sets '
                                         'out fresh almond tofu and warm blankets.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N26_B05',
                                 'speaker': 'Narrator',
                                 'text': 'For one peaceful night and sunlit morning, no Millelith alarm '
                                         'sounds -- because the Qimen array outside is not scheduled to '
                                         "open until tomorrow's Boar Hour.",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': None,
                      'routing': [{'default': True, 'next_node': 'N27_C2'}],
                      'ending_id': None},
           'N27_C2': {'node_id': 'N27_C2',
                      'chapter_id': 'CH3',
                      'title': 'The Seventy-Seven-Year Tea Contract',
                      'day_label': 'Day 8 - Noon',
                      'location': 'Serenitea Pot - Garden Stone Table',
                      'beats': [{'beat_id': 'N27_B01',
                                 'speaker': 'Narrator',
                                 'text': 'At noon on the eighth day, Xiangling, Paimon, and Yanfei pop '
                                         'into the courtyard via their realm pass carrying a steaming '
                                         'bamboo steamer of festival lunch.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B02',
                                 'speaker': 'Paimon',
                                 'text': "Paimon brought Wanmin's test batch of eight-treasure duck! Whoa, "
                                         "Hu Tao's cheeks actually have color again!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B03',
                                 'speaker': 'Hu Tao',
                                 'text': "Just in time! Since Liyue's sharpest legal mind is sitting right "
                                         "at our table, I move to notarize Wangsheng's 'Seventy-Seven-Year "
                                         "Tea-Friend Covenant' with Traveler Aether!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': 'vn_sweet_happy'},
                                {'beat_id': 'N27_B04',
                                 'speaker': 'Yanfei',
                                 'text': 'Six whole pages of brush calligraphy?! Let me read Clause Four '
                                         "-- 'Every spring when plum blossoms open, Party B shall brew one "
                                         'pot of Songluo tea and remember the 77th Director at least three '
                                         "times aloud'?!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_X1',
                                 'speaker': 'Hu Tao',
                                 'text': 'Order in the courtyard! Clause Seven clearly states that if '
                                         'Party B travels to Snezhnayan snowfields without a warm scarf, '
                                         'Party A reserves posthumous -- ahem, executive lecturing rights!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N27_X2',
                                 'speaker': 'Paimon',
                                 'text': "Hey, Hu Tao just slipped and almost said 'posthumous'!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_X3',
                                 'speaker': 'Hu Tao',
                                 'text': 'Occupational habit, Bailiff Paimon! Stuff another shrimp '
                                         'dumpling in your cheeks and pass the inkstone!',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': 'vn_sweet_happy'},
                                {'beat_id': 'N27_B05',
                                 'speaker': 'Xiangling',
                                 'text': "Hahaha, why does 'remember her aloud' sound like Hu Tao's "
                                         "planning to skip town without paying Wanmin's tab?!",
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N27_B06',
                                 'speaker': 'Narrator',
                                 'text': 'Everyone laughs around the sunlit stone table -- yet as Hu Tao '
                                         'signs her name at the bottom with a vermilion brush, her right '
                                         'index finger stiffens slightly, hooking the final stroke '
                                         'downward.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                 'voice_emotion': ''}],
                      'choice': {'choice_id': 'C16_C',
                                 'prompt': 'Hu Tao slides the freshly inked six-page scroll across the '
                                           'stone table toward you:',
                                 'options': [{'opt_id': 'C16_C1',
                                              'label': "Notice how the final stroke of Hu Tao's brush "
                                                       'signature hooks and blurs because her right index '
                                                       'finger has gone stiff.',
                                              'effects': {'bond': 0, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N28_C3',
                                              'reaction_beats': [{'beat_id': 'N27_C16C1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Even inside perpetual spring '
                                                                          'warmth, her right hand cannot '
                                                                          'grip a thin bamboo brush '
                                                                          'steady. And every single clause '
                                                                          'on that scroll asks me to '
                                                                          "'remember' her rather than meet "
                                                                          'her.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C16_C2',
                                              'label': 'Sign beside her name immediately, adding a rider '
                                                       'clause requiring the 77th Director to collect the '
                                                       'tea fee in person every spring.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N28_C3',
                                              'reaction_beats': [{'beat_id': 'N27_C16C2_R1',
                                                                  'speaker': 'Hu Tao',
                                                                  'text': "...'Collect in person every "
                                                                          "spring,' huh? Oyaoya, look at "
                                                                          'Party B sneaking sharp '
                                                                          "amendments past Yanfei! Deal's "
                                                                          'a deal!',
                                                                  'inner_thought': 'Her eyes blink once '
                                                                                   'too fast at the words '
                                                                                   "'in person' before her "
                                                                                   'grin covers the crack.',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch3c_teapot_court_base.jpg',
                                                                  'voice_emotion': 'vn_shy_blush'}]}]},
                      'routing': [],
                      'ending_id': None},
           'N28_C3': {'node_id': 'N28_C3',
                      'chapter_id': 'CH4',
                      'title': 'Three in the Morning on the Veranda',
                      'day_label': 'Day 9 - 03:00 AM',
                      'location': 'Serenitea Pot - Lantern-Lit Outdoor Kitchen',
                      'beats': [{'beat_id': 'N28_B01',
                                 'speaker': 'Narrator',
                                 'text': 'Sub-space realms keep perpetual spring, yet my Fontainian pocket '
                                         'watch on the nightstand still ticks past three in the morning. '
                                         'When a soft clink of porcelain wakes me, the courtyard outside '
                                         'lies still and warm beneath the peach blossoms, and sweet ginger '
                                         'steam is curling from the outdoor hearth.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B02',
                                 'speaker': 'Narrator',
                                 'text': 'Resting on a low cedar tea stand well clear of the stove sits a '
                                         'neat stack of thick red envelopes sealed in crimson wax -- '
                                         'addressed one by one to Zhongli, Xiangling, Xingqiu, Chongyun, '
                                         'and me.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B03',
                                 'speaker': 'Narrator',
                                 'text': 'At the creak of my sandal, Hu Tao spins halfway around, her wide '
                                         'right sleeve sweeping the entire stack of wax-sealed red '
                                         'envelopes off the tea stand and deep into her pocket before '
                                         'flashing a crooked grin.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_base.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B04',
                                 'speaker': 'Hu Tao',
                                 'text': 'Oyaoya, caught red-handed! Wipe that courtroom scowl off your '
                                         'face, Aether. A certain host barely touched dinner after '
                                         "Yanfei's six-page ambush, so yours truly took pity on your "
                                         'rumbling stomach.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_base.jpg',
                                 'voice_emotion': 'vn_playful_tease'},
                                {'beat_id': 'N28_B05',
                                 'speaker': 'Narrator',
                                 'text': 'She lifts the blue-and-white porcelain bowl with her usual '
                                         'theatrical flourish. Halfway across the counter, the tendons in '
                                         'her right wrist lock. Scalding amber syrup sloshes over the rim, '
                                         'raising an angry crimson welt across her pale knuckles -- and '
                                         'her eyelashes do not even twitch.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tremor.jpg',
                                 'voice_emotion': ''},
                                {'beat_id': 'N28_B06_F02',
                                 'speaker': 'Aether',
                                 'text': 'Back on my third night at the parlor, you made up a house rule '
                                         "over a bowl just like this. 'Bitter first, sweet last -- nobody "
                                         "leaves Wangsheng's table with bitterness on their tongue.' "
                                         '...Who are you saying goodbye to at three in the morning, Hu '
                                         'Tao?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tremor.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F02_SHARED_BOWL']}},
                                {'beat_id': 'N28_B07_F05',
                                 'speaker': 'Aether',
                                 'text': "Those wax-sealed envelopes in your sleeve are Old Lin's tin box "
                                         "all over again. You looked at that old carpenter's unsent letter "
                                         'like a mirror because you were already writing yours.',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tremor.jpg',
                                 'voice_emotion': '',
                                 'when': {'all_flags': ['F05_CARPENTER_LEDGER']}},
                                {'beat_id': 'N28_B08',
                                 'speaker': 'Hu Tao',
                                 'text': '...You have a wicked habit of hoarding every throwaway line I '
                                         "drop. Can't a girl steal a midnight bowl of sweet tangyuan "
                                         'without facing an inquest?',
                                 'inner_thought': '',
                                 'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tremor.jpg',
                                 'voice_emotion': 'vn_shy_blush'}],
                      'choice': {'choice_id': 'C17_C',
                                 'prompt': 'Boiling ginger syrup glistens across her unfeeling right '
                                           'knuckles under the warm veranda lantern:',
                                 'options': [{'opt_id': 'C17_C1',
                                              'label': 'Set the scalding bowl down, hold her numb right '
                                                       'wrist, and ask directly whom those wax-sealed red '
                                                       'envelopes in her sleeve are addressed to.',
                                              'effects': {'bond': 1, 'insight': 2, 'add_flags': []},
                                              'next_node': 'N29_C4_GATE2',
                                              'reaction_beats': [{'beat_id': 'N28_C17C1_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'Unable to feel either the burn '
                                                                          'or my grip on her right hand, '
                                                                          'Hu Tao lowers her bangs over '
                                                                          'her eyes, silently letting me '
                                                                          'rinse the scalding syrup away '
                                                                          'with cool spring water.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                                                  'voice_emotion': ''}]},
                                             {'opt_id': 'C17_C2',
                                              'label': 'Press a cool damp cloth gently over her burned '
                                                       'knuckles without forcing a confession yet, pulling '
                                                       'her shivering frame against your chest.',
                                              'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                              'next_node': 'N29_C4_GATE2',
                                              'reaction_beats': [{'beat_id': 'N28_C17C2_R1',
                                                                  'speaker': 'Narrator',
                                                                  'text': 'For five wordless minutes '
                                                                          'before dawn, her forehead rests '
                                                                          'silent and unmoving against my '
                                                                          'collarbone while the kitchen '
                                                                          'fire crackles low.',
                                                                  'inner_thought': '',
                                                                  'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                                                  'voice_emotion': ''}]}]},
                      'routing': [],
                      'ending_id': None},
           'N29_C4_GATE2': {'node_id': 'N29_C4_GATE2',
                            'chapter_id': 'CH4',
                            'title': 'Combination Gate #2 -- Rooster Hour Summons',
                            'day_label': 'Day 9 - Dusk (3 Hours Before Midnight)',
                            'location': 'Serenitea Pot - Courtyard Exit Gate',
                            'beats': [{'beat_id': 'N29_B01',
                                       'speaker': 'Narrator',
                                       'text': 'Rooster Hour strikes -- three full hours before Boar Hour '
                                               "opens the Eight Gates array outside. Inside Hu Tao's "
                                               'sleeve, an ancient jade Wangsheng tally begins vibrating '
                                               'with low, mournful resonance.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_X1',
                                       'speaker': 'Aether',
                                       'text': 'If you step through that realm gate alone right now, you '
                                               'have zero intention of ever walking back down Wuwang Hill, '
                                               'do you?',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_X2',
                                       'speaker': 'Hu Tao',
                                       'text': "...Don't make this harder than it already is, Aether. Two "
                                               'days of borrowed spring under these peach blossoms gave me '
                                               'more than I ever hoped to carry with me.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                       'voice_emotion': 'vn_tender_love'},
                                      {'beat_id': 'N29_X3',
                                       'speaker': 'Narrator',
                                       'text': 'Pink peach petals drift across the stone between our boots '
                                               'as her trembling left hand reaches for the exit rune.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B02',
                                       'speaker': 'Narrator',
                                       'text': "Every trace of mischief vanishes from Hu Tao's face. "
                                               'Stepping toward the realm boundary, she raises two fingers '
                                               'to unseal her exit back to Wuwang Hill alone.',
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                       'voice_emotion': ''},
                                      {'beat_id': 'N29_B03',
                                       'speaker': 'Hu Tao',
                                       'text': 'Forty-eight hours are almost up, Landlord Aether. Stay '
                                               'inside and watch the fireworks with Paimon tonight -- '
                                               "Director's final request.",
                                       'inner_thought': '',
                                       'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                       'voice_emotion': ''}],
                            'choice': {'choice_id': 'C18_C_GATE2',
                                       'prompt': "Three hours remain before midnight's array opens. Hu "
                                                 "Tao's hand is already on the realm exit seal:",
                                       'options': [{'opt_id': 'C18_C_COMBO_UNLOCK',
                                                    'when': {'all_flags': ['F07_PLUM_BRANCH'],
                                                             'any_flags': ['F08_ASH_COUGH_SEEN',
                                                                           'F11_BUBU_HERBS'],
                                                             'min_count_in': {'count': 2,
                                                                              'pool': ['F01_COLD_PULSE',
                                                                                       'F02_SHARED_BOWL',
                                                                                       'F04_ROOF_PROMISE',
                                                                                       'F05_CARPENTER_LEDGER',
                                                                                       'F06_MERCY_LANTERN']},
                                                             'min_insight': 6},
                                                    'unlock_badge': '[COMBINATION UNLOCKED]',
                                                    'lock_hint': '[LOCKED: Needs Plum Branch + Lung-Frost '
                                                                 'Proof + 2 Memories + Insight 6]',
                                                    'label': 'Set her crimson plum branch beside the proof '
                                                             'of her marrow-frost lungs and every promise '
                                                             'between you -- shattering her farewell mask.',
                                                    'effects': {'bond': 2,
                                                                'insight': 1,
                                                                'add_flags': ['COMBO2_CLEARED']},
                                                    'next_node': 'N34_CH5_CONVERGE',
                                                    'reaction_beats': [{'beat_id': 'N29_C18_OK_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Confronted with her own '
                                                                                'living plum branch and '
                                                                                'every symptom she hid, Hu '
                                                                                "Tao's composure finally "
                                                                                'breaks. Tears spill hot '
                                                                                'down her cheeks as she '
                                                                                'buries her face against '
                                                                                'my chest.',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N29_C18_OK_R2',
                                                                        'speaker': 'Hu Tao',
                                                                        'text': "I don't WANT to leave you "
                                                                                "either, dummy! It's the "
                                                                                'Gate of Death -- anyone '
                                                                                "written into Liyue's Ley "
                                                                                'Lines who steps inside in '
                                                                                'my place turns to ash '
                                                                                'while the array still '
                                                                                'shatters!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                                                        'voice_emotion': 'vn_tender_love'},
                                                                       {'beat_id': 'N29_C18_OK_R3',
                                                                        'speaker': 'Aether',
                                                                        'text': "'Written into Liyue's Ley "
                                                                                "Lines'... Look at me, Hu "
                                                                                "Tao! Teyvat's Ley Lines "
                                                                                'have no record of me! '
                                                                                'Open the anchor as '
                                                                                'Director, and the second '
                                                                                'erasure starts, my hand '
                                                                                'pulls you back and burns '
                                                                                'the fetor outside the '
                                                                                'roots!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                                                        'voice_emotion': ''},
                                                                       {'beat_id': 'N29_C18_OK_R4',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Wiping her eyes fiercely '
                                                                                'on her crimson cuff, Hu '
                                                                                'Tao laces her fingers '
                                                                                'tight through mine -- and '
                                                                                'together we step straight '
                                                                                'out of the teapot toward '
                                                                                "Wuwang's midnight altar!",
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                                                        'voice_emotion': ''}]},
                                                   {'opt_id': 'C18_C_GOOD_SHELTER',
                                                    'label': "Lock the Serenitea Pot's realm seal to keep "
                                                             'Hu Tao safe inside before the array opens, '
                                                             'calling Zhongli and the adepti to freeze '
                                                             'Wuwang from outside!',
                                                    'effects': {'bond': 2, 'insight': 0, 'add_flags': []},
                                                    'next_node': 'N33_GOOD_1',
                                                    'reaction_beats': [{'beat_id': 'N29_C18_GD_R1',
                                                                        'speaker': 'Narrator',
                                                                        'text': 'Unwilling to gamble her '
                                                                                'life against an unknown '
                                                                                'law, I invert my adeptal '
                                                                                'realm key -- sealing the '
                                                                                'courtyard doors shut and '
                                                                                'firing an emergency '
                                                                                'golden flare straight to '
                                                                                'Zhongli and Xianyun!',
                                                                        'inner_thought': '',
                                                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch4c_veranda_3am_tears.jpg',
                                                                        'voice_emotion': ''}]}]},
                            'routing': [],
                            'ending_id': None},
           'N33_GOOD_1': {'node_id': 'N33_GOOD_1',
                          'chapter_id': 'CH4',
                          'title': 'A Slumber Beneath Borrowed Eaves',
                          'day_label': "Day 10 - New Year's Morning (60 Days Before Qingming)",
                          'location': 'Serenitea Pot - Peach-Blossom Hotpot Veranda',
                          'beats': [{'beat_id': 'N33_B01',
                                     'speaker': 'Narrator',
                                     'text': 'Because my flare reached Zhongli three hours before Boar '
                                             'Hour, the Seven-and-Eight-Gates array never ignited -- '
                                             'sparing all seven sub-gate guardians from backlash.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B02',
                                     'speaker': 'Narrator',
                                     'text': "Yet an external adeptal seal cannot purify Tao Dou's fetor. "
                                             'Working through midnight alongside Xianyun, Mountain Shaper, '
                                             'and Moon Carver, Zhongli could only freeze the northern '
                                             'fissure under six layers of amber stone -- buying Liyue '
                                             'exactly sixty days until Qingming.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B03',
                                     'speaker': 'Narrator',
                                     'text': 'Northern Wuwang stands cordoned off behind Millelith '
                                             'banners, and no crimson butterflies danced over the harbor '
                                             'last night -- yet across the steaming New Year hotpot table '
                                             'inside our spring courtyard, Hu Tao is alive and rapping my '
                                             'forehead with bamboo chopsticks.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B04',
                                     'speaker': 'Hu Tao',
                                     'text': 'Unbelievable! Locking your own employer inside an adeptal '
                                             'teapot -- Yanfei, how many years of dishwashing does '
                                             'unlawful detention carry?!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': 'vn_playful_tease'},
                                    {'beat_id': 'N33_B05',
                                     'speaker': 'Yanfei',
                                     'text': 'Hmm, citing emergency life-preservation before midnight... '
                                             'Court sentences Party B to sixty consecutive days of brewing '
                                             'warm ginger tea!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_X1',
                                     'speaker': 'Xiangling',
                                     'text': 'Eat up, Hu Tao! Doctor Baizhu sent warming chili-ginger '
                                             "broth rules specifically so you don't sneak out into cold "
                                             'mountain drafts!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_X2',
                                     'speaker': 'Paimon',
                                     'text': 'Yeah! Paimon nearly cried when Aether locked the teapot last '
                                             'night -- you owe Paimon three bowls of sweet rice balls for '
                                             'the scare!',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_X3',
                                     'speaker': 'Narrator',
                                     'text': "Outside in Liyue, Zhongli's six-layered amber seal holds the "
                                             'silent mountain fast -- not a victory yet, only a precious '
                                             'sixty-day reprieve before spring rain tests the stone again.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B06',
                                     'speaker': 'Narrator',
                                     'text': 'Beneath the noisy tablecloth while Xiangling and Paimon '
                                             'fight over lotus root slices, my fingers lace quietly around '
                                             "Hu Tao's right hand -- where a thin, cold thread of unpurged "
                                             'yin-frost still slumbers beneath her skin.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': ''},
                                    {'beat_id': 'N33_B07',
                                     'speaker': 'Hu Tao',
                                     'text': 'Sixty days of borrowed spring before Qingming thaws the '
                                             "seal, huh? ...Then don't let go of my hand, Assistant "
                                             'Aether. Help me find a real answer before spring rain falls.',
                                     'inner_thought': '',
                                     'cg': 'ui_assets/story_quest_cgs/hutao/end_good_teapot_hotpot_base.jpg',
                                     'voice_emotion': 'vn_tender_love'}],
                          'choice': None,
                          'routing': [],
                          'ending_id': 'END_GOOD'},
           'N34_CH5_CONVERGE': {'node_id': 'N34_CH5_CONVERGE',
                                'chapter_id': 'CH5',
                                'title': 'The Duty of Wangsheng',
                                'day_label': 'Day 9 - Midnight at the Gate of Death',
                                'location': 'Wuwang Summit - Eight Gates Altar',
                                'beats': [{'beat_id': 'N34_B01_RA',
                                           'speaker': 'Narrator',
                                           'text': 'Standing inches outside the eighth stone pillar where '
                                                   'we kept vigil together, I grip my hilt and exchange '
                                                   "one steady, fearless nod with Hu Tao as midnight's "
                                                   'golden lantern crests the southern horizon.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_A']}},
                                          {'beat_id': 'N34_B01_RB',
                                           'speaker': 'Narrator',
                                           'text': "Atop Wuwang's lonely summit, Hu Tao raises Staff of "
                                                   'Homa believing not a soul in Liyue knows her sacrifice '
                                                   '-- until a blazing golden-crimson spatial rift tears '
                                                   'open directly above the outer stone ring and I drop '
                                                   'onto the rim calling her name!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_B']}},
                                          {'beat_id': 'N34_B01_RC',
                                           'speaker': 'Narrator',
                                           'text': "Golden teapot light deposits both of us onto Wuwang's "
                                                   'summit seconds before Boar Hour; our ten fingers part '
                                                   'only at the chalk rim of the eighth stone pillar as we '
                                                   'take our agreed stations.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['ROUTE_C']}},
                                          {'beat_id': 'N34_B02',
                                           'speaker': 'Narrator',
                                           'text': 'Across Liyue below, seven pillars of elemental light '
                                                   'lance skyward from Keqing, Ganyu, Shenhe, Xiao, '
                                                   'Baizhu, Beidou, and Yelan -- driving every black vein '
                                                   "of Tao Dou's fetor roaring toward Wuwang's center!",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_B03',
                                           'speaker': 'Hu Tao',
                                           'text': 'Spirits drift across the sea of suffering! Flickering '
                                                   'out from sight, return quickly to the night!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_X1',
                                           'speaker': 'Narrator',
                                           'text': 'Far across Mt. Tianheng, Xiao plunges his jade spear '
                                                   'into karmic shadow; on the northern crags, Shenhe and '
                                                   'Ganyu freeze whole torrents of black vapor; offshore, '
                                                   "Beidou's fleet fires Electro-warded flares while Yelan "
                                                   'and Keqing sever stray tendrils!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_X2',
                                           'speaker': 'Narrator',
                                           'text': 'Down in the harbor, Doctor Baizhu and Changsheng brace '
                                                   'the seventh seal as every ounce of converged fetor '
                                                   'funnels straight into the eighth stone circle under Hu '
                                                   "Tao's boots!",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_X3',
                                           'speaker': 'Hu Tao',
                                           'text': 'Count three heartbeats after the butterflies rise, '
                                                   'Aether -- not one second sooner, or the convergence '
                                                   'breaks!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_X4',
                                           'speaker': 'Aether',
                                           'text': 'Three heartbeats -- and then my hand brings you home!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_B04',
                                           'speaker': 'Hu Tao',
                                           'text': 'There is no avoiding death, nor predicting its time -- '
                                                   'the duty of Wangsheng, I now fulfill!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N34_B05',
                                           'speaker': 'Narrator',
                                           'text': 'Hatless hair whipping like dark silk in the gale, Hu '
                                                   'Tao drives the blazing Staff of Homa straight into Tao '
                                                   "Dou's heart! Ten thousand crimson Pyro butterflies "
                                                   'erupt into the heavens, incinerating the plague clouds '
                                                   'across Liyue -- even as black erasure mist swallows '
                                                   'her feet!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_gate_of_death_ritual_base.jpg',
                                           'voice_emotion': ''}],
                                'choice': None,
                                'routing': [{'default': True, 'next_node': 'N35'}],
                                'ending_id': None},
           'N35': {'node_id': 'N35',
                   'chapter_id': 'CH5',
                   'title': "Mirror-Black Water & Old Hu's Farewell",
                   'day_label': 'Day 9 - Beyond Time in the Border',
                   'location': 'Underworld Threshold - The Painted Scroll Gate',
                   'beats': [{'beat_id': 'N35_B01',
                              'speaker': 'Narrator',
                              'text': "Beneath the triumphant crimson sky, Hu Tao's consciousness sinks "
                                      'into mirror-black water that stretches to every horizon without a '
                                      'ripple.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B02',
                              'speaker': 'Narrator',
                              'text': 'Ley Line Obfuscation washes over her senses like warm gray snow -- '
                                      'muffling every sound from above, blurring minutes into years until '
                                      'even the direction of the outer stone ring dissolves in the dark.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B03_F06',
                              'speaker': 'Narrator',
                              'text': 'Just as her boot nears a bottomless drop in the black tide, a small '
                                      'plum-wood lantern bearing a carved swallow drifts brightly across '
                                      "the water -- Old Lin's grateful wish steadying her path toward the "
                                      'glowing scroll ahead.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F06_MERCY_LANTERN']}},
                             {'beat_id': 'N35_B04',
                              'speaker': 'Narrator',
                              'text': 'Towering out of the silver mist stands the colossal Chinese '
                                      'ink-scroll Gate of the Afterlife. Waiting gently before its '
                                      'threshold stand two warm, familiar silhouettes -- her late father, '
                                      'and the seventy-sixth Director, Old Hu.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B05',
                              'speaker': 'Old Hu',
                              'text': 'Look how tall our little girl grew. Seventy-seven generations of '
                                      'Wangsheng, and not once has our house stood prouder than tonight.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_X1',
                              'speaker': 'Hu Tao',
                              'text': 'When I was thirteen, Grandpa... I sat at this border for three days '
                                      "with crumbled sesame cakes in my pocket, angry I didn't even get "
                                      'one last wave.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N35_X2',
                              'speaker': 'Old Hu',
                              'text': 'Hahaha, silly child! Had I lingered at the gate back then, you '
                                      'never would have stepped forward into the sunlight on your own two '
                                      'feet.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_X3',
                              'speaker': 'Old Hu',
                              'text': 'And look what wondrous company you found along the living road. '
                                      "Don't keep that golden-haired boy waiting -- his arm is burning "
                                      'bright enough to blind our whole scroll!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N35_B06',
                              'speaker': 'Hu Tao',
                              'text': 'Grandpa... Dad... Did all the lanterns down in the harbor stay lit?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N35_B07',
                              'speaker': 'Old Hu',
                              'text': 'Every single one, child. Live in life, and die in death -- yet your '
                                      'time has not yet come. Look up above the dark water, Hu Tao. '
                                      'Someone refused to let the Ley Lines forget your name.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_water_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N36_BORDER_GRASP'}],
                   'ending_id': None},
           'N36_BORDER_GRASP': {'node_id': 'N36_BORDER_GRASP',
                                'chapter_id': 'CH5',
                                'title': 'The Hand That Crossed Erasure',
                                'day_label': 'Day 9 - Boar Hour Climax',
                                'location': 'Seam of Life and Death',
                                'beats': [{'beat_id': 'N36_B01_PLUM',
                                           'speaker': 'Narrator',
                                           'text': 'Through a hairline crack of golden light high above '
                                                   'the black water, a single living crimson plum petal -- '
                                                   'warm with the pulse she entrusted to my chest -- '
                                                   "flutters straight down into Hu Tao's open palm!",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N36_B01_STAR',
                                           'speaker': 'Narrator',
                                           'text': 'Through a hairline crack high above the black water, a '
                                                   'bright mote of golden Descender starlight drops '
                                                   'through the dark, chiming clear as brass bells in '
                                                   "front of Hu Tao's eyes!",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                           'voice_emotion': '',
                                           'when': {'forbid_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N36_B02',
                                           'speaker': 'Narrator',
                                           'text': 'The instant Hu Tao looks up, my right arm -- blazing '
                                                   'white-gold with unrecorded outlander light -- punches '
                                                   'straight down through the erasure veil and locks '
                                                   'around her cold wrist!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_X1',
                                           'speaker': 'Narrator',
                                           'text': 'Above on the altar rim, cracks of absolute zero race '
                                                   'up my right bracer as the Gate of Death tries and '
                                                   "fails to locate my name in Teyvat's Ley Lines!",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_X2',
                                           'speaker': 'Hu Tao',
                                           'text': "Your arm -- Aether, the fetor's freezing your veins "
                                                   "black! Let go or it'll tear your meridians apart!",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_X3',
                                           'speaker': 'Aether',
                                           'text': "Let it freeze! No rule carved under Teyvat's soil gets "
                                                   'to take you while my hand has reach!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                           'voice_emotion': ''},
                                          {'beat_id': 'N36_B03',
                                           'speaker': 'Hu Tao',
                                           'text': 'Aether--?!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                           'voice_emotion': 'vn_shy_blush'},
                                          {'beat_id': 'N36_B04',
                                           'speaker': 'Narrator',
                                           'text': 'Finding zero Ley Line record to erase inside me, the '
                                                   "furious black whirlpool of Tao Dou's remaining fetor "
                                                   "reverses course -- pouring out of Hu Tao's lungs and "
                                                   'roaring straight up my right arm to be incinerated in '
                                                   'golden starlight!',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                           'voice_emotion': ''}],
                                'choice': {'choice_id': 'C21_CH5',
                                           'prompt': 'Freezing black fetor sears up your right meridians '
                                                     'as you haul Hu Tao upward toward the living sky:',
                                           'options': [{'opt_id': 'C21_A_HEART_CALL',
                                                        'label': "'Don't look back at the scroll, Hu Tao! "
                                                                 'Everyone in Liyue is waiting for you -- '
                                                                 "and so am I!'",
                                                        'effects': {'bond': 2,
                                                                    'insight': 0,
                                                                    'add_flags': []},
                                                        'next_node': 'N37_BUBU_WAKE',
                                                        'reaction_beats': [{'beat_id': 'N36_C21A_R1',
                                                                            'speaker': 'Hu Tao',
                                                                            'text': '...You reckless, '
                                                                                    'impossible dummy! '
                                                                                    "Don't you dare let go "
                                                                                    'of me now!',
                                                                            'inner_thought': '',
                                                                            'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                                                            'voice_emotion': 'vn_tender_love'}]},
                                                       {'opt_id': 'C21_B_SIPHON_ANCHOR',
                                                        'label': "'Hold tight to my wrist! Let every last "
                                                                 'drop of marrow-frost pour into my arm '
                                                                 "before the Gate seals shut!'",
                                                        'effects': {'bond': 1,
                                                                    'insight': 1,
                                                                    'add_flags': []},
                                                        'next_node': 'N37_BUBU_WAKE',
                                                        'reaction_beats': [{'beat_id': 'N36_C21B_R1',
                                                                            'speaker': 'Narrator',
                                                                            'text': 'Her fingers clamp '
                                                                                    'fiercely around my '
                                                                                    'forearm as the last '
                                                                                    'ribbon of Yin-frost '
                                                                                    'tears out of her '
                                                                                    'chest and shatters '
                                                                                    'into white-gold '
                                                                                    'sparks!',
                                                                            'inner_thought': '',
                                                                            'cg': 'ui_assets/story_quest_cgs/hutao/ch5_underworld_grasp_diff.jpg',
                                                                            'voice_emotion': ''}]}]},
                                'routing': [],
                                'ending_id': None},
           'N37_BUBU_WAKE': {'node_id': 'N37_BUBU_WAKE',
                             'chapter_id': 'CH5',
                             'title': 'White Blossoms & Moonlit Steps',
                             'day_label': 'Day 10 - Pre-Dawn Moonlight',
                             'location': 'Wuwang Hill Stone Trail -> Liyue Harbor',
                             'beats': [{'beat_id': 'N37_B01',
                                        'speaker': 'Narrator',
                                        'text': 'We burst upward onto grass together right as the '
                                                'petrified wood of Tao Dou splits open into thousands of '
                                                'pure white blossoms under the New Year moon!',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': ''},
                                       {'beat_id': 'N37_B02',
                                        'speaker': 'Narrator',
                                        'text': "Color and warmth flood back into Hu Tao's cheeks at once "
                                                '-- while steam as cold as dry ice hisses off my right '
                                                'sleeve. Dark-gray meridian cold-burn veins spiderweb from '
                                                'my right wrist all the way to my collarbone!',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': ''},
                                       {'beat_id': 'N37_B03_WARD',
                                        'speaker': 'Narrator',
                                        'text': 'Thanks to the Descender Siphon Ward carved on my hilt, '
                                                'the blast stops short of my heart, yet the sheer volume '
                                                'of incinerated deity-fetor drags my knees straight into '
                                                'the grass.',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': '',
                                        'when': {'all_flags': ['SIPHON_WARD_CARVED']}},
                                       {'beat_id': 'N37_B03_RAW',
                                        'speaker': 'Narrator',
                                        'text': "Taking an ancient deity's entire backlash through "
                                                'unwarded flesh spares my organs from Ley Line rot, yet '
                                                'the violent meridian cold-burn sends freezing fever '
                                                'straight through my nervous system.',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': '',
                                        'when': {'forbid_flags': ['SIPHON_WARD_CARVED']}},
                                       {'beat_id': 'N37_X1',
                                        'speaker': 'Narrator',
                                        'text': 'Halfway down the stone mountain trail, Chongyun and '
                                                'Millelith sentries rush forward with a bamboo litter -- '
                                                'only for Hu Tao to wave them fiercely aside without '
                                                'surrendering my weight.',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': ''},
                                       {'beat_id': 'N37_X2',
                                        'speaker': 'Hu Tao',
                                        'text': 'Clear the stairs to Bubu Pharmacy and tell Doctor Baizhu '
                                                "to heat silver needles! He carried Wangsheng's burden in "
                                                "his bare right arm -- I'm carrying him through that door "
                                                'myself!',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': ''},
                                       {'beat_id': 'N37_X3',
                                        'speaker': 'Narrator',
                                        'text': 'Through half-delirious fever, I feel warm tears splash '
                                                'onto the back of my bandaged wrist with every steady, '
                                                'stubborn step her small boots take under the waning moon.',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': ''},
                                       {'beat_id': 'N37_X4',
                                        'speaker': 'Narrator',
                                        'text': "Not until lantern light from Bubu Pharmacy's green eaves "
                                                'washes over us does darkness finally claim my sight.',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': ''},
                                       {'beat_id': 'N37_B04',
                                        'speaker': 'Narrator',
                                        'text': 'Refusing to wait for stretchers, nineteen-year-old Hu Tao '
                                                'drops to one knee, hoists my heavier frame stubbornly '
                                                'onto her slender back just as she did on Night 1, and '
                                                "starts down the long moonlit stone steps toward Liyue's "
                                                'distant lanterns.',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': ''},
                                       {'beat_id': 'N37_B05',
                                        'speaker': 'Hu Tao',
                                        'text': "Hey... stay awake back there, you hear me? Don't you dare "
                                                'fall asleep for good on my shoulders, idiot... Wangsheng '
                                                'rejects your registration -- permanently!',
                                        'inner_thought': '',
                                        'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                                        'voice_emotion': 'vn_tender_love'}],
                             'choice': None,
                             'routing': [{'default': True, 'next_node': 'N38'}],
                             'ending_id': None},
           'N38': {'node_id': 'N38',
                   'chapter_id': 'CH5',
                   'title': 'Forty-Eight Hours Beside Your Cot',
                   'day_label': 'Day 11 - Late Night',
                   'location': 'Bubu Pharmacy - Inner Acupuncture Ward',
                   'beats': [{'beat_id': 'N38_B01',
                              'speaker': 'Narrator',
                              'text': 'Forty-eight hours pass in warm waves of silver acupuncture needles '
                                      'and bitter qingxin poultices before my eyelids finally lift to the '
                                      'quiet green lanterns of Bubu Pharmacy.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B02',
                              'speaker': 'Narrator',
                              'text': 'Thick white herbal bandages wrap my right arm from palm to '
                                      'shoulder, tingling with restorative warmth rather than decay.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B03',
                              'speaker': 'Paimon',
                              'text': "AETHER!! Waaah, you're finally awake! Baizhu and Qiqi said any "
                                      "mortal arm would've turned to dust, so forty-eight hours of "
                                      'meridian fever is a miracle!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_X1',
                              'speaker': 'Narrator',
                              'text': 'Stepping quietly around the bamboo screen, Qiqi sets a porcelain '
                                      'cup of warm honey-lotus water beside my pillow with solemn '
                                      'precision.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_X2',
                              'speaker': 'Qiqi',
                              'text': 'Qiqi... usually dislikes warm, noisy Hu Tao. ...Still, Hu Tao held '
                                      "Traveler's left hand for forty-eight hours without sleeping. Qiqi "
                                      'wrote in notebook: do not chase Hu Tao away.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_X3',
                              'speaker': 'Baizhu',
                              'text': "Your outlander meridians burned away every trace of Tao Dou's "
                                      'resentment without suffering Ley Line necrosis, Aether. Keep that '
                                      'salve wrapped three more days and your sword-arm will recover in '
                                      'full.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_X4',
                              'speaker': 'Aether',
                              'text': "Thank you, Baizhu -- Qiqi, Paimon. Don't worry, I won't swing a "
                                      'blade this morning. Only going out to the balcony.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B04',
                              'speaker': 'Paimon',
                              'text': 'Xiangling, Keqing, Ningguang, and Mister Zhongli all came by to '
                                      'check on you -- only Hu Tao refused to budge from that wooden stool '
                                      'for two whole days and nights!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N38_B05',
                              'speaker': 'Paimon',
                              'text': 'Qiqi barely chased her out onto the balcony ten minutes ago to wash '
                                      "her face before sunrise! Go let her know you're up before she "
                                      'worries herself sick again!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_moonlight_piggyback_base.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N39_BALCONY_DAWN'}],
                   'ending_id': None},
           'N39_BALCONY_DAWN': {'node_id': 'N39_BALCONY_DAWN',
                                'chapter_id': 'CH5',
                                'title': 'Sunrise Over Living Harbor',
                                'day_label': 'Day 12 - Golden Dawn',
                                'location': 'High Wooden Balcony Overlooking Liyue Harbor',
                                'beats': [{'beat_id': 'N39_B01',
                                           'speaker': 'Narrator',
                                           'text': 'Draping my coat over my bandaged right arm, I step out '
                                                   "onto the high cedar balcony just as Day 12's first "
                                                   'golden sunbeam crests the sea horizon.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_barehat_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B01_NP',
                                           'speaker': 'Narrator',
                                           'text': 'Draping my coat over my bandaged right arm, I step out '
                                                   "onto the high cedar balcony just as Day 12's first "
                                                   'golden sunbeam crests the sea horizon.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_with_plum_diff.jpg',
                                           'voice_emotion': '',
                                           'when': {'forbid_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B02',
                                           'speaker': 'Narrator',
                                           'text': 'Soft footsteps pad silently behind me -- and suddenly '
                                                   'two slender hands slip from behind my shoulders to '
                                                   'cover both my eyes.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_barehat_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B02_NP',
                                           'speaker': 'Narrator',
                                           'text': 'Soft footsteps pad silently behind me -- and suddenly '
                                                   'two slender hands slip from behind my shoulders to '
                                                   'cover both my eyes.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_with_plum_diff.jpg',
                                           'voice_emotion': '',
                                           'when': {'forbid_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B03_F01',
                                           'speaker': 'Narrator',
                                           'text': 'My breath catches. Unlike that icy right wrist I '
                                                   'caught on my very first noon at Wangsheng, BOTH of her '
                                                   'palms resting against my cheeks this morning are '
                                                   'gloriously, unmistakably warm with living blood.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_barehat_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['F01_COLD_PULSE', 'F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B03_F01_NP',
                                           'speaker': 'Narrator',
                                           'text': 'My breath catches. Unlike that icy right wrist I '
                                                   'caught on my very first noon at Wangsheng, BOTH of her '
                                                   'palms resting against my cheeks this morning are '
                                                   'gloriously, unmistakably warm with living blood.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_with_plum_diff.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['F01_COLD_PULSE'],
                                                    'forbid_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B04',
                                           'speaker': 'Hu Tao',
                                           'text': 'One more time... guess who?',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_barehat_base.jpg',
                                           'voice_emotion': 'vn_playful_tease',
                                           'when': {'all_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B04_NP',
                                           'speaker': 'Hu Tao',
                                           'text': 'One more time... guess who?',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_with_plum_diff.jpg',
                                           'voice_emotion': 'vn_playful_tease',
                                           'when': {'forbid_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B05',
                                           'speaker': 'Narrator',
                                           'text': 'Laughing softly as I lower her hands, Hu Tao spins to '
                                                   'lean beside me against the sunlit railing -- her '
                                                   'Harmony Hexagram Hat still completely bare of its '
                                                   'crimson plum branch, waiting openly in the morning '
                                                   'light.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_barehat_base.jpg',
                                           'voice_emotion': '',
                                           'when': {'all_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B05_NP',
                                           'speaker': 'Narrator',
                                           'text': 'Laughing softly as I lower her hands, Hu Tao spins to '
                                                   'lean beside me against the sunlit railing, morning sun '
                                                   'glinting across the crimson plum branch on her Harmony '
                                                   'Hexagram Hat.',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_with_plum_diff.jpg',
                                           'voice_emotion': '',
                                           'when': {'forbid_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B06',
                                           'speaker': 'Hu Tao',
                                           'text': "'Butterflies cross the mist at dawn, plum blossoms "
                                                   'wake where ash has gone -- how sweet to open living '
                                                   "eyes, beneath the same familiar skies.'",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_barehat_base.jpg',
                                           'voice_emotion': 'vn_sweet_happy',
                                           'when': {'all_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B06_NP',
                                           'speaker': 'Hu Tao',
                                           'text': "'Butterflies cross the mist at dawn, plum blossoms "
                                                   'wake where ash has gone -- how sweet to open living '
                                                   "eyes, beneath the same familiar skies.'",
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_with_plum_diff.jpg',
                                           'voice_emotion': 'vn_sweet_happy',
                                           'when': {'forbid_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B07',
                                           'speaker': 'Hu Tao',
                                           'text': "You dragged Wangsheng's 77th Director all the way back "
                                                   'from the scroll gate, Aether. So tell me honestly... '
                                                   'what are you planning to do with the lifetime you just '
                                                   'saved?',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_barehat_base.jpg',
                                           'voice_emotion': 'vn_tender_love',
                                           'when': {'all_flags': ['F07_PLUM_BRANCH']}},
                                          {'beat_id': 'N39_B07_NP',
                                           'speaker': 'Hu Tao',
                                           'text': "You dragged Wangsheng's 77th Director all the way back "
                                                   'from the scroll gate, Aether. So tell me honestly... '
                                                   'what are you planning to do with the lifetime you just '
                                                   'saved?',
                                           'inner_thought': '',
                                           'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_with_plum_diff.jpg',
                                           'voice_emotion': 'vn_tender_love',
                                           'when': {'forbid_flags': ['F07_PLUM_BRANCH']}}],
                                'choice': {'choice_id': 'C22_FINAL',
                                           'prompt': "Golden dawn spills across Hu Tao's upturned scarlet "
                                                     'eyes on the harbor balcony:',
                                           'options': [{'opt_id': 'C22_TRUE_CONFESS',
                                                        'when': {'all_flags': ['F07_PLUM_BRANCH'],
                                                                 'forbid_flags': ['STOIC_BYPASS_NO_VOW'],
                                                                 'min_bond': 14},
                                                        'unlock_badge': '[TRUE VOW UNLOCKED]',
                                                        'lock_hint': '[LOCKED: Needs Crimson Plum Branch + '
                                                                     'Mortal Vow + Bond 14]',
                                                        'label': 'Catch her warm fingers, draw the living '
                                                                 'crimson plum branch from over your '
                                                                 'heart, and pin it home onto the bare '
                                                                 'brim of her hat.',
                                                        'effects': {'bond': 3,
                                                                    'insight': 0,
                                                                    'add_flags': ['TRUE_BOND_SEALED']},
                                                        'next_node': 'N40',
                                                        'reaction_beats': [{'beat_id': 'N39_C22T_R1',
                                                                            'speaker': 'Aether',
                                                                            'text': "I'm returning what I "
                                                                                    'promised to keep safe '
                                                                                    '-- and claiming every '
                                                                                    'morning that comes '
                                                                                    'with its owner.',
                                                                            'inner_thought': '',
                                                                            'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                                                                            'voice_emotion': ''}]},
                                                       {'opt_id': 'C22_NEUTRAL_PARTING',
                                                        'label': 'Smile gently in the dawn breeze and '
                                                                 'answer as her steadfast companion before '
                                                                 'the road calls again.',
                                                        'effects': {'bond': 0,
                                                                    'insight': 0,
                                                                    'add_flags': []},
                                                        'next_node': 'N42'}]},
                                'routing': [],
                                'ending_id': None},
           'N40': {'node_id': 'N40',
                   'chapter_id': 'CH5',
                   'title': 'Twin Branches & Chenyu Banquet',
                   'day_label': 'Day 12 - Morning to Lantern Dusk',
                   'location': 'Harbor Balcony -> Chenyu Vale Feast Table',
                   'beats': [{'beat_id': 'N40_B01',
                              'speaker': 'Narrator',
                              'text': 'As my left hand slides the living crimson plum branch back into its '
                                      "rightful clasp on her Harmony Hexagram Hat, Hu Tao's eyes curve "
                                      'into radiant crescents.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B02',
                              'speaker': 'Hu Tao',
                              'text': "Hehe... I had a hunch you wouldn't hand that back without making a "
                                      'bold claim! Hold completely still, Assistant -- no, Partner Aether!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N40_B03',
                              'speaker': 'Narrator',
                              'text': 'Producing a second freshly cut crimson plum branch she hid behind '
                                      'her waist at dawn -- snipped from the very same courtyard bough -- '
                                      'she rises onto her toes and pins it straight onto the white scarf '
                                      'over my heart!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B04',
                              'speaker': 'Hu Tao',
                              'text': 'One on my brim, one over your heart! Now wherever my Traveler '
                                      "wanders across Teyvat, Wangsheng's 77th Director holds an ironclad "
                                      'claim on his lapel!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': 'vn_shy_blush'},
                             {'beat_id': 'N40_X1',
                              'speaker': 'Xingqiu',
                              'text': 'A toast to our Traveler and the 77th Director! Though I must ask -- '
                                      'since when do matching crimson plum branches count as standard '
                                      'Wangsheng uniform?',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_X2',
                              'speaker': 'Chongyun',
                              'text': 'Wait -- matching branches?! Oh! Uh, congratulations to you both!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_X3',
                              'speaker': 'Lan Yan',
                              'text': 'Hehe, Chenyu elders say twin plum sprigs cut from the same winter '
                                      'bough tie two roads back to the same courtyard no matter how far '
                                      'the wind blows!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_X4',
                              'speaker': 'Hu Tao',
                              'text': 'Hear that, Partner Aether? Even Chenyu folklore backs up '
                                      "Wangsheng's paperwork -- zero loopholes left!",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N40_B05',
                              'speaker': 'Narrator',
                              'text': 'That evening in Chenyu Vale, lanterns hang from every jade pavilion '
                                      'as Xiangling, Xingqiu, Chongyun, Lan Yan, and Paimon crowd our '
                                      "celebratory banquet table while Yun Jin's clear song drifts across "
                                      'the water.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N40_B06_F02',
                              'speaker': 'Narrator',
                              'text': 'When dessert arrives, Hu Tao nudges my knee under the table and '
                                      'drops half an osmanthus tangyuan into my spoon with a wink -- '
                                      "'sweet last,' kept in full.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': '',
                              'when': {'all_flags': ['F02_SHARED_BOWL']}}],
                   'choice': None,
                   'routing': [{'default': True, 'next_node': 'N41'}],
                   'ending_id': None},
           'N41': {'node_id': 'N41',
                   'chapter_id': 'CH5',
                   'title': 'Matching Plum Blossoms Beneath a Living Sky',
                   'day_label': 'Day 12 - Final Lantern Night',
                   'location': 'Bishui River - Floating Lantern Dock',
                   'beats': [{'beat_id': 'N41_B01',
                              'speaker': 'Narrator',
                              'text': 'Slipping away from the cheerful clamor of the banquet, Hu Tao and I '
                                      'walk out to the quiet wooden pier above Bishui River where hundreds '
                                      'of lotus lanterns drift toward the sea.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B02_F04',
                              'speaker': 'Hu Tao',
                              'text': "Remember what you told me up on Wangsheng's cold roof tiles on "
                                      "Night Four? 'Stop talking like I'm passing weather, Hu Tao.' ...I "
                                      'held onto that line all the way down in the dark water.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': 'vn_tender_love',
                              'when': {'all_flags': ['F04_ROOF_PROMISE']}},
                             {'beat_id': 'N41_B03',
                              'speaker': 'Narrator',
                              'text': 'Lifting her plum-crowned hat into one hand so the river lanterns '
                                      'catch every warm highlight in her eyes, Hu Tao catches my scarf '
                                      'with her right hand -- steady, warm, and strong -- and rises onto '
                                      'tiptoe.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B04',
                              'speaker': 'Narrator',
                              'text': 'Her lips press soft and warm against the corner of mine, tasting '
                                      'faintly of sweet osmanthus and spring wind before her forehead '
                                      'rests lightly against my chin.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_X1',
                              'speaker': 'Narrator',
                              'text': 'River mist curls warm around the cedar pilings of the dock as '
                                      "golden lotus lanterns mirror themselves across Bishui's gentle "
                                      'current.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_X2',
                              'speaker': 'Aether',
                              'text': 'Before Qingce that first night, I spent years telling myself it was '
                                      'kinder never to anchor an immortal life to someone mortal.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_X3',
                              'speaker': 'Aether',
                              'text': 'Standing over that black water taught me the opposite. Ten thousand '
                                      "empty years aren't worth a single morning if Liyue forgets your "
                                      'laugh.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_X4',
                              'speaker': 'Narrator',
                              'text': "Hu Tao's breath catches softly in the lantern glow; for once, not a "
                                      'single teasing rhyme comes to her rescue as her warm fingers slide '
                                      'up my lapel.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N41_B05',
                              'speaker': 'Hu Tao',
                              'text': "I don't need ten thousand years like the stars, Aether. So long as "
                                      'the first person I get to pester every morning of this lifetime is '
                                      "you... Wangsheng's 77th Director calls that the bargain of the "
                                      'millennium.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': 'vn_tender_love'},
                             {'beat_id': 'N41_B06',
                              'speaker': 'Aether',
                              'text': 'Deal sealed, Hu Tao -- every spring, every morning, in person.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_true_twin_plums_kiss.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_TRUE'},
           'N42': {'node_id': 'N42',
                   'chapter_id': 'CH5',
                   'title': 'One Lantern for the Unspoken',
                   'day_label': 'Day 12 - Dawn Balcony -> Moonlit Wangsheng Roof',
                   'location': 'Liyue Harbor -> Wangsheng Rooftop From Afar',
                   'beats': [{'beat_id': 'N42_B01_VA1',
                              'speaker': 'Narrator',
                              'text': 'Heart pounding in the dawn sun, I step half a pace closer to ask to '
                                      'stay beside her -- and my fingers brush an empty lapel where no '
                                      'keepsake plum branch rests to bridge the words.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_with_plum_diff.jpg',
                              'voice_emotion': '',
                              'when': {'min_bond': 14, 'forbid_flags': ['F07_PLUM_BRANCH']}},
                             {'beat_id': 'N42_B02_VA2',
                              'speaker': 'Narrator',
                              'text': 'That half-second pause while I search for words is all it takes. '
                                      'Terrified of becoming an anchor dragging a star-traveler down, Hu '
                                      'Tao pulls her hat brim low and slaps a gilded wooden token into my '
                                      'palm with a bright laugh before I can speak!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_with_plum_diff.jpg',
                              'voice_emotion': '',
                              'when': {'min_bond': 14, 'forbid_flags': ['F07_PLUM_BRANCH']}},
                             {'beat_id': 'N42_B01_VB',
                              'speaker': 'Narrator',
                              'text': 'Unable to cross that final threshold between ten thousand years and '
                                      'one mortal spring, I smile gently and answer that any honorary '
                                      'Wangsheng assistant would have pulled his Director home.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_barehat_base.jpg',
                              'voice_emotion': '',
                              'when': {'any_of': [{'max_bond': 13},
                                                  {'all_flags': ['STOIC_BYPASS_NO_VOW']}]}},
                             {'beat_id': 'N42_B02_VB',
                              'speaker': 'Narrator',
                              'text': "For the briefest flicker, Hu Tao's scarlet pupils dim -- before her "
                                      'bright grin snaps cleanly back into place and she slaps a gilded '
                                      'wooden token into my palm.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/ch5_balcony_dawn_barehat_base.jpg',
                              'voice_emotion': '',
                              'when': {'any_of': [{'max_bond': 13},
                                                  {'all_flags': ['STOIC_BYPASS_NO_VOW']}]}},
                             {'beat_id': 'N42_B03',
                              'speaker': 'Hu Tao',
                              'text': "Ta-da! Lifetime Fifty-Percent VIP Parlor Pass for Wangsheng's MVP "
                                      'Assistant! Whenever your road loops back through Liyue Harbor, '
                                      'Songluo tea is on the house!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_neutral_solo_lantern.jpg',
                              'voice_emotion': 'vn_sweet_happy'},
                             {'beat_id': 'N42_X1',
                              'speaker': 'Aether',
                              'text': 'Wait, Hu Tao -- before you turn this into another parlor coupon--',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_neutral_solo_lantern.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_X2',
                              'speaker': 'Hu Tao',
                              'text': 'Nope, no refunds and no heavy faces on Day Twelve! Look down at the '
                                      "wharf -- Paimon's already waving two big bags of Wanmin travel buns "
                                      'for your next horizon!',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_neutral_solo_lantern.jpg',
                              'voice_emotion': 'vn_playful_tease'},
                             {'beat_id': 'N42_X3',
                              'speaker': 'Narrator',
                              'text': 'She steps back with a crisp, buoyant salute that hides her '
                                      "fingertips behind her sleeve, leaving a hair's-breadth of warm "
                                      'morning air neither of us quite dares cross.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_neutral_solo_lantern.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B04',
                              'speaker': 'Narrator',
                              'text': 'Late that twelfth night, pausing down in the quiet lane before '
                                      "setting out toward the harbor gate, I glance back up at Wangsheng's "
                                      'curved clay roof under the silver moon.',
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_neutral_solo_lantern.jpg',
                              'voice_emotion': ''},
                             {'beat_id': 'N42_B05',
                              'speaker': 'Narrator',
                              'text': 'Sitting alone along the ridge tiles where we once shared roasted '
                                      'chestnuts, Hu Tao releases a single nameless Xiao Lantern -- '
                                      'watching its unspoken wish climb silently into the stars, just like '
                                      "Old Lin's.",
                              'inner_thought': '',
                              'cg': 'ui_assets/story_quest_cgs/hutao/end_neutral_solo_lantern.jpg',
                              'voice_emotion': ''}],
                   'choice': None,
                   'routing': [],
                   'ending_id': 'END_NEUTRAL'}}}

STORY_QUEST_CAMPAIGNS: list[dict] = [STORY_QUEST_CAMPAIGN]
