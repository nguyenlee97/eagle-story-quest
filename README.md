# eagle-story-quest

> **Project Eagle** | Visual Novel Story Quest System | v2.0

A plug-and-play Visual Novel engine for GTA San Andreas modding, built for Project Eagle. Add new character campaigns by dropping a single Python file — no core edits required.

## Architecture

```
eagle_story_quest.py          ← Core engine (do not modify)
eagle_story_quest_hutao.py    ← Hu Tao campaign (420KB, 44 nodes, 42 CG)
eagle_story_quest_citlali.py  ← Citlali campaign (496KB, 44 nodes, 42 CG)
eagle_story_quest_furina.py   ← Furina campaign (517KB, 44 nodes, 44 CG)
README-story-quest-engine.md  ← Full engine documentation
```

## Zero-Core-Edit Pattern

```python
# 1. Create eagle_story_quest_<char>.py with:
STORY_QUEST_CAMPAIGN = {
    "campaign_id": "hutao_sq1_papilio_rests",
    "char_id": "hutao",
    "ped_id": 49428,
    "theme_rgb": [220, 50, 50],
    "chapters": [...],  # 44 scene nodes
    "flags": {...},     # causal flags
    "endings": [...],   # 5 endings
}
STORY_QUEST_CAMPAIGNS = [STORY_QUEST_CAMPAIGN]

# 2. Drop 42 CGs into ui_assets/story_quest_cgs/<char>/
# 3. Engine auto-discovers — done.
```

## Campaigns

| Character | Campaign ID | Nodes | Beats | Paths | CG | Endings | Status |
|-----------|-------------|-------|-------|-------|-----|---------|--------|
| Hu Tao | `hutao_sq1_papilio_rests` | 44 | 501 | 6,311 | 42/42 | 5 | ✅ PASS |
| Citlali | `citlali_sq1_color_of_eternity` | 44 | 569 | 6,355 | 42/42 | 5 | ✅ PASS |
| Furina | `furina_sq1_unscripted_encore` | 44 | 573 | 5,467 | 38/44 | 5 | ✅ PASS |

## Engine Features (v2.0)

- **Multi-campaign** auto-discovery: drop file → engine finds it
- **SQLite state machine**: auto-save every beat (`waifulink.sqlite3`)
- **7 save slots**: Slot 0 Auto-Save + Slots 1–6 Manual with CG preview
- **2D Causal Graph** `[J]`: Ch.1→Ch.5 columns, Time-Jump with full snapshot
- **DirectX 9 fullscreen** via Ping-Pong `WLCG0/1.TXD` (1024×512)
- **JP Voice** auto-triggered by `voice_emotion` field
- **Mouse 144Hz** via `CPad::UpdateMouse` auto-patch
- **Backlog** `[Backspace]`, **Gallery** `[H]`, **Save/Load** `[S]/[L]`

## QA Results

| Campaign | DAG Check | DX9 Screenshots | eagle_doctor |
|----------|-----------|-----------------|--------------|
| Hu Tao | 0 deadlock, 0 orphan | 11/11 PASS | 11/11 |
| Citlali | 44/44 reachable | 12/12 PASS | 11/11 |
| Furina | 5/5 endings verified | 11/11 PASS | 11/11 |

## Jira
- [SCRUM-170](https://nguyennguyenle997.atlassian.net/browse/SCRUM-170) — Engine v1.0 + Hu Tao
- [SCRUM-178](https://nguyennguyenle997.atlassian.net/browse/SCRUM-178) — Citlali SQ1
- [SCRUM-174](https://nguyennguyenle997.atlassian.net/browse/SCRUM-174) — Furina SQ1

## Related
- [eagle-waifulink](https://github.com/nguyenlee97/eagle-waifulink) — Dating sim + BGM
- [project-eagle-tools](https://github.com/nguyenlee97/project-eagle-tools) — Infrastructure
