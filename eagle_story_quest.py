"""
Story Quest Engine v2.0 (Multi-Campaign Branching Visual Novel Engine + 2D Causal Graph + 7-Slot Save/Load)
Target Runtime: C:\\Users\\LENOVO\\Desktop\\GTA\\Project Eagle\\gta sa gameplay-lab

Upgrades in v2.0 (100% Backward-Compatible with all v1.0 `eagle_story_quest_<char>.py` packs):
- Multi-Story-Quest per heroine (`campaigns_by_char: dict[char_id -> list[campaign]]`), reading both
  `STORY_QUEST_CAMPAIGNS: list[dict]` and `STORY_QUEST_CAMPAIGN: dict` from all `eagle_story_quest_*.py` modules.
- First-class Theatrical Movie-Poster Thumbnail (`poster_cg`), `title`, `subtitle`, and `synopsis` metadata
  displayed on the outer Story Quest Overview & Campaign List before starting a quest.
- Safe SQLite auto-migration (`(char_id, campaign_id)` keys across runs, checkpoints, unlocked endings) +
  new `story_quest_save_slots` table (`Slot 0 Auto-Save` + `Slots 1..6 Manual Save Slots` with `16:9` `cg_rel` preview).
- True 2D Causal Graph Layout (`build_causal_graph_2d`): computes non-overlapping `(col, lane)` coordinates
  and directed parent->child branch edges across `Ch.1 -> Ch.5 + 5 Endings`, distinguishing `Scene`, `Choice Gate [?]`,
  `Combination Gate [COMBO]`, `Current Node [NOW]`, `Locked [???]`, and `Ending Nodes` with click-to-inspect & Time-Jump.
"""
from __future__ import annotations

import datetime
import importlib
import importlib.util
import json
import sqlite3
import sys
import textwrap
import threading
from pathlib import Path
from typing import Any, Callable, Optional

FORBIDDEN_CFONT_CHARS: tuple[str, ...] = (
    "~",
    "|",
    "*",
    "\u2014",
    "\u2013",
    "\u2026",
    "\u201c",
    "\u201d",
    "\u2018",
    "\u2019",
)

HEROINE_VOICE_BUCKETS: tuple[str, ...] = (
    "greet_doorstep",
    "vn_sweet_happy",
    "vn_shy_blush",
    "vn_playful_tease",
    "vn_tender_love",
    "outing_cruise",
    "outing_bump_rescue",
    "outing_arrive_photo",
)

DEFAULT_THEME_COLORS: dict[str, tuple[int, int, int]] = {
    "hutao": (225, 49, 75),
    "furina": (56, 152, 248),
    "citlali": (192, 132, 252),
    "columbina": (244, 114, 182),
    "kirara": (52, 211, 153),
    "vesna": (251, 191, 36),
}

# Built-in fallback theatrical Movie-Poster thumbnails & synopses for packs created before v2.0
# (Any pack defining its own `poster_cg` and `synopsis` overrides these automatically!)
DEFAULT_CAMPAIGN_POSTERS_AND_SYNOPSES: dict[str, dict[str, str]] = {
    "hutao_papilio_5ch_v1": {
        "poster_cg": "ui_assets/story_quest_cgs/hutao/hutao_sq1_poster.jpg",
        "synopsis": (
            "Beneath Liyue's lantern glow, an unsealed Border flare drains the warmth from Wangsheng's 77th Director. "
            "Walk five nights beside Hu Tao through Wuwang mist, gather hidden karmic clues, and decide whether two "
            "mortal hands can rewrite an ancient law of parting."
        ),
    },
    "citlali_sq1_color_of_eternity": {
        "poster_cg": "ui_assets/story_quest_cgs/citlali/citlali_sq1_poster.jpg",
        "fallback_cg": "ui_assets/story_quest_cgs/citlali/ch1_01_doorstep_graffiti_base.jpg",
        "synopsis": (
            "Colorless frost creeps across Granny Itztli's cliffside sanctuary as a First-Era Night-Kingdom scroll "
            "threatens to bleach her memories white. Weave eleven hidden clues beside Citlali before the White Surge "
            "severs your shared Soul-Bridge forever."
        ),
    },
    "furina_sq1_unscripted_encore": {
        "poster_cg": "ui_assets/story_quest_cgs/furina/furina_sq1_poster.jpg",
        "fallback_cg": "ui_assets/story_quest_cgs/furina/ch1_01_lucine_midnight_base.jpg",
        "synopsis": (
            "Past midnight by the Fountain of Lucine, five centuries of crystal tear-rime chill Furina's wrist and "
            "steal her sense of sweetness. Cross the burning Indemnitium footlights as her mortal co-star before the "
            "Solstice tide seals the Opera Epiclese under winter ice."
        ),
    },
}


def sanitize_cfont_ascii(value: Any) -> str:
    """Defensive ASCII sanitizer for GTA SA RenderWare CFont HUD strings."""
    if value is None:
        return ""
    s = str(value)
    replacements = {
        "\u2014": "--",
        "\u2013": "-",
        "\u2026": "...",
        "\u201c": "'",
        "\u201d": "'",
        "\u2018": "'",
        "\u2019": "'",
        "~": "-",
        "|": "/",
        "*": "+",
        "\r": " ",
        "\n": " ",
        "\t": " ",
    }
    for bad, rep in replacements.items():
        if bad in s:
            s = s.replace(bad, rep)
    out_chars: list[str] = []
    for ch in s:
        code = ord(ch)
        if 32 <= code <= 126:
            out_chars.append(ch)
    return " ".join("".join(out_chars).split())


def check_strict_cfont_string(text: str, context_label: str) -> list[str]:
    """Returns a list of violations if `text` contains any forbidden CFont or non-ASCII character."""
    issues: list[str] = []
    for bad in FORBIDDEN_CFONT_CHARS:
        if bad in text:
            issues.append(f"{context_label}: contains forbidden char {repr(bad)}")
    for idx, ch in enumerate(text):
        code = ord(ch)
        if ch in ("\n",):
            continue
        if not (32 <= code <= 126):
            issues.append(f"{context_label}: non-ASCII char {repr(ch)} (U+{code:04X}) at index {idx}")
            break
    return issues


def evaluate_condition(cond: Optional[dict[str, Any]], state: dict[str, Any]) -> bool:
    """Safe declarative condition evaluator (zero `eval`)."""
    if not cond:
        return True
    if cond.get("default") is True and len(cond) == 1:
        return True

    bond = int(state.get("bond", 0))
    insight = int(state.get("insight", 0))
    raw_flags = state.get("flags") or ()
    flags = raw_flags if isinstance(raw_flags, set) else set(raw_flags)

    if "min_bond" in cond and bond < int(cond["min_bond"]):
        return False
    if "max_bond" in cond and bond > int(cond["max_bond"]):
        return False
    if "min_insight" in cond and insight < int(cond["min_insight"]):
        return False
    if "max_insight" in cond and insight > int(cond["max_insight"]):
        return False

    all_flags = cond.get("all_flags") or cond.get("requires_all") or []
    if all_flags and not all(f in flags for f in all_flags):
        return False

    forbid_flags = cond.get("forbid_flags") or cond.get("none_flags") or []
    if forbid_flags and any(f in flags for f in forbid_flags):
        return False

    any_flags = cond.get("any_flags") or cond.get("requires_any") or []
    if any_flags and not any(f in flags for f in any_flags):
        return False

    min_cnt_spec = cond.get("min_count_in") or cond.get("requires_at_least")
    if isinstance(min_cnt_spec, dict):
        pool = min_cnt_spec.get("flags") or min_cnt_spec.get("pool") or []
        req_n = int(min_cnt_spec.get("count", 1))
        if sum(1 for f in pool if f in flags) < req_n:
            return False

    all_of = cond.get("all_of")
    if isinstance(all_of, list) and not all(evaluate_condition(sub, state) for sub in all_of):
        return False

    any_of = cond.get("any_of")
    if isinstance(any_of, list) and any_of and not any(evaluate_condition(sub, state) for sub in any_of):
        return False

    return True


def _is_combination_condition(cond: Optional[dict[str, Any]]) -> bool:
    if not isinstance(cond, dict):
        return False
    if cond.get("all_of") or cond.get("any_of") or cond.get("min_count_in") or cond.get("requires_at_least"):
        return True
    af = cond.get("all_flags") or cond.get("requires_all") or []
    if len(af) >= 2:
        return True
    if len(af) >= 1 and ("min_bond" in cond or "min_insight" in cond):
        return True
    return False


def _collect_condition_flags(cond: Optional[dict[str, Any]], acc: set[str]) -> None:
    if not isinstance(cond, dict):
        return
    for key in ("all_flags", "requires_all", "any_flags", "requires_any", "forbid_flags", "none_flags"):
        for fl in cond.get(key) or []:
            acc.add(str(fl))
    mc = cond.get("min_count_in") or cond.get("requires_at_least")
    if isinstance(mc, dict):
        for fl in (mc.get("flags") or mc.get("pool") or []):
            acc.add(str(fl))
    for sub in cond.get("all_of") or []:
        _collect_condition_flags(sub, acc)
    for sub in cond.get("any_of") or []:
        _collect_condition_flags(sub, acc)


def apply_effects(state: dict[str, Any], effects: Optional[dict[str, Any]]) -> dict[str, Any]:
    """Returns an updated shallow state dict after applying bond/insight/add_flags/remove_flags."""
    next_flags = list(state.get("flags") or [])
    flag_set = set(next_flags)
    bond = int(state.get("bond", 0))
    insight = int(state.get("insight", 0))
    if effects:
        bond += int(effects.get("bond", 0))
        insight += int(effects.get("insight", 0))
        for rf in effects.get("remove_flags") or []:
            if rf in flag_set:
                flag_set.remove(rf)
                next_flags = [x for x in next_flags if x != rf]
        for af in effects.get("add_flags") or []:
            if af not in flag_set:
                flag_set.add(af)
                next_flags.append(af)
    return {
        "bond": bond,
        "insight": insight,
        "flags": next_flags,
    }


def validate_campaign_pack(
    campaign: dict[str, Any],
    base_dir: Optional[Path] = None,
    require_cgs_on_disk: bool = True,
) -> dict[str, Any]:
    """Comprehensive static + causal graph validator for any `STORY_QUEST_CAMPAIGN` pack."""
    errors: list[str] = []
    required_top = (
        "char_id",
        "campaign_id",
        "title",
        "subtitle",
        "version",
        "chapters",
        "initial_state",
        "flag_catalog",
        "endings",
        "nodes",
    )
    for rk in required_top:
        if rk not in campaign:
            errors.append(f"Missing top-level key: {rk}")
    if errors:
        return {"ok": False, "errors": errors}

    cfont_issues: list[str] = []
    for fld in ("title", "subtitle", "synopsis", "poster_cg"):
        if campaign.get(fld):
            cfont_issues.extend(check_strict_cfont_string(str(campaign.get(fld, "")), f"campaign.{fld}"))

    chapters = campaign["chapters"]
    nodes: dict[str, dict[str, Any]] = campaign["nodes"]
    endings: dict[str, dict[str, Any]] = campaign["endings"]
    flag_catalog: dict[str, dict[str, Any]] = campaign["flag_catalog"]

    for ch in chapters:
        cid = ch.get("chapter_id", "?")
        cfont_issues.extend(check_strict_cfont_string(str(ch.get("title", "")), f"chapter[{cid}].title"))
        en = ch.get("entry_node")
        if en not in nodes:
            errors.append(f"Chapter {cid} entry_node {en!r} not found in nodes")

    for fk, fmeta in flag_catalog.items():
        cfont_issues.extend(check_strict_cfont_string(str(fmeta.get("title", "")), f"flag[{fk}].title"))
        cfont_issues.extend(check_strict_cfont_string(str(fmeta.get("clue_hint", "")), f"flag[{fk}].clue_hint"))

    for ek, emeta in endings.items():
        cfont_issues.extend(check_strict_cfont_string(str(emeta.get("rank", "")), f"ending[{ek}].rank"))
        cfont_issues.extend(check_strict_cfont_string(str(emeta.get("title", "")), f"ending[{ek}].title"))
        if emeta.get("summary"):
            cfont_issues.extend(check_strict_cfont_string(str(emeta.get("summary", "")), f"ending[{ek}].summary"))

    planted_flags: set[str] = set(campaign["initial_state"].get("flags") or [])
    referenced_flags: set[str] = set()
    cg_paths: set[str] = set()
    if campaign.get("poster_cg"):
        cg_paths.add(str(campaign["poster_cg"]).strip())
    total_beats = 0

    def _inspect_beat(b: dict[str, Any], ctx: str) -> None:
        nonlocal total_beats
        total_beats += 1
        for tf in ("speaker", "text", "inner_thought"):
            val = str(b.get(tf, "") or "")
            if val:
                cfont_issues.extend(check_strict_cfont_string(val, f"{ctx}.{tf}"))
        cg_rel = str(b.get("cg", "") or "").strip()
        if not cg_rel:
            errors.append(f"{ctx}: empty cg path")
        else:
            cg_paths.add(cg_rel)
        ve = str(b.get("voice_emotion", "") or "").strip()
        if ve and ve not in HEROINE_VOICE_BUCKETS:
            errors.append(f"{ctx}: unknown voice_emotion {ve!r}")
        _collect_condition_flags(b.get("when"), referenced_flags)

    for nid, node in nodes.items():
        for nf in ("title", "day_label", "location"):
            cfont_issues.extend(check_strict_cfont_string(str(node.get(nf, "")), f"node[{nid}].{nf}"))

        for ev in node.get("pre_events") or []:
            _collect_condition_flags(ev.get("when"), referenced_flags)
            for af in (ev.get("effects") or {}).get("add_flags") or []:
                planted_flags.add(str(af))

        beats = node.get("beats") or []
        if not beats:
            errors.append(f"node[{nid}] has 0 beats")
        for bi, b in enumerate(beats):
            _inspect_beat(b, f"node[{nid}].beat[{bi}:{b.get('beat_id', '')}]")

        ch_obj = node.get("choice")
        rt_list = node.get("routing") or []
        end_id = node.get("ending_id")

        if ch_obj:
            cid = ch_obj.get("choice_id", nid)
            cfont_issues.extend(check_strict_cfont_string(str(ch_obj.get("prompt", "")), f"choice[{cid}].prompt"))
            opts = ch_obj.get("options") or []
            if not opts:
                errors.append(f"choice[{cid}] has 0 options")
            for opt in opts:
                oid = opt.get("opt_id", "?")
                cfont_issues.extend(check_strict_cfont_string(str(opt.get("label", "")), f"choice[{cid}].opt[{oid}].label"))
                if opt.get("lock_hint"):
                    cfont_issues.extend(check_strict_cfont_string(str(opt["lock_hint"]), f"choice[{cid}].opt[{oid}].lock_hint"))
                if opt.get("unlock_badge"):
                    cfont_issues.extend(check_strict_cfont_string(str(opt["unlock_badge"]), f"choice[{cid}].opt[{oid}].unlock_badge"))
                _collect_condition_flags(opt.get("when"), referenced_flags)
                for af in (opt.get("effects") or {}).get("add_flags") or []:
                    planted_flags.add(str(af))
                for rbi, rb in enumerate(opt.get("reaction_beats") or []):
                    _inspect_beat(rb, f"choice[{cid}].opt[{oid}].reaction[{rbi}]")
                nxt = opt.get("next_node")
                if nxt not in nodes and nxt not in endings:
                    errors.append(f"choice[{cid}].opt[{oid}] invalid next_node {nxt!r}")
        elif end_id:
            if end_id not in endings:
                errors.append(f"node[{nid}] invalid ending_id {end_id!r}")
        elif rt_list:
            for r_i, rule in enumerate(rt_list):
                _collect_condition_flags(rule.get("when"), referenced_flags)
                nxt = rule.get("next_node")
                if nxt not in nodes and nxt not in endings:
                    errors.append(f"node[{nid}].routing[{r_i}] invalid next_node {nxt!r}")
        else:
            errors.append(f"node[{nid}] has neither choice, routing, nor ending_id (dead-end node)")

    errors.extend(cfont_issues)

    for fk in flag_catalog:
        if fk not in planted_flags:
            errors.append(f"Catalog flag {fk!r} is never planted via add_flags")
        if fk not in referenced_flags:
            errors.append(f"Catalog flag {fk!r} is never referenced in any `when` condition")

    missing_cgs: list[str] = []
    if require_cgs_on_disk and base_dir is not None:
        for rel in sorted(cg_paths):
            full_p = Path(base_dir) / Path(rel)
            if not full_p.exists() or not full_p.is_file() or full_p.stat().st_size < 512:
                missing_cgs.append(rel)
        if missing_cgs:
            errors.append(f"Missing or empty CG files on disk ({len(missing_cgs)}): {missing_cgs[:8]}")

    entry_node = chapters[0]["entry_node"]
    init_st = campaign["initial_state"]
    init_sig = (entry_node, int(init_st.get("bond", 0)), int(init_st.get("insight", 0)), frozenset(init_st.get("flags") or []))

    visited_nodes: set[str] = set()
    reached_endings: set[str] = set()
    seen_sigs: set[tuple[str, int, int, frozenset[str]]] = set()

    def _walk(sig: tuple[str, int, int, frozenset[str]]) -> None:
        if sig in seen_sigs:
            return
        seen_sigs.add(sig)
        nid, b_val, i_val, f_set = sig
        if nid in endings:
            reached_endings.add(nid)
            return
        node = nodes[nid]
        visited_nodes.add(nid)

        st: dict[str, Any] = {"bond": b_val, "insight": i_val, "flags": list(f_set)}
        for ev in node.get("pre_events") or []:
            if evaluate_condition(ev.get("when"), st):
                st = apply_effects(st, ev.get("effects"))

        act_beats = [b for b in (node.get("beats") or []) if evaluate_condition(b.get("when"), st)]
        if not act_beats:
            errors.append(f"State at node[{nid}] yields 0 active beats for flags={sorted(st['flags'])}")
            return

        if node.get("ending_id"):
            reached_endings.add(str(node["ending_id"]))
            return

        ch_obj = node.get("choice")
        if ch_obj:
            cid = ch_obj.get("choice_id", nid)
            unlocked_opts = [opt for opt in ch_obj["options"] if evaluate_condition(opt.get("when"), st)]
            if not unlocked_opts:
                errors.append(
                    f"Deadlock at choice[{cid}] (node={nid}): 0 unlocked options for bond={st['bond']}, insight={st['insight']}, flags={sorted(st['flags'])}"
                )
                return
            if ch_obj.get("exclusive_rescue_gate") and len(unlocked_opts) > 1:
                unlocked_opts = [unlocked_opts[0]]
            for opt in unlocked_opts:
                st2 = apply_effects(st, opt.get("effects"))
                _walk((str(opt["next_node"]), int(st2["bond"]), int(st2["insight"]), frozenset(st2["flags"])))
            return

        matched_rt = None
        for rule in node.get("routing") or []:
            if rule.get("default") is True or evaluate_condition(rule.get("when"), st):
                matched_rt = rule.get("next_node")
                break
        if not matched_rt:
            errors.append(f"Deadlock in routing at node[{nid}] for bond={st['bond']}, insight={st['insight']}")
            return
        _walk((str(matched_rt), int(st["bond"]), int(st["insight"]), frozenset(st["flags"])))

    if not errors or (len(errors) == 1 and missing_cgs and not require_cgs_on_disk):
        _walk(init_sig)
        orphan_nodes = sorted(set(nodes.keys()) - visited_nodes)
        if orphan_nodes:
            errors.append(f"Orphan unreachable scene nodes ({len(orphan_nodes)}): {orphan_nodes}")
        unreached_endings = sorted(set(endings.keys()) - reached_endings)
        if unreached_endings:
            errors.append(f"Unreachable endings ({len(unreached_endings)}): {unreached_endings}")

    return {
        "ok": len(errors) == 0,
        "char_id": campaign.get("char_id"),
        "campaign_id": campaign.get("campaign_id"),
        "total_nodes": len(nodes),
        "visited_nodes": len(visited_nodes),
        "total_beats": total_beats,
        "unique_cgs": len(cg_paths),
        "missing_cgs": missing_cgs,
        "reached_endings": sorted(reached_endings),
        "distinct_state_signatures": len(seen_sigs),
        "errors": errors,
    }


class StoryQuestEngine:
    """
    StoryQuestEngine v2.0 — Multi-Campaign Pure Branching Visual Novel Runtime Manager
    with Movie-Poster Metadata, 2D Causal Graph Layout, and 7-Slot Save/Load System.
    """

    VERSION = "2.0.0"

    def __init__(
        self,
        base_dir: Path,
        db_path: Optional[Path] = None,
        voice_callback: Optional[Callable[[Any, str, str], None]] = None,
    ) -> None:
        self.base_dir = Path(base_dir)
        self.db_path = Path(db_path) if db_path is not None else (self.base_dir / "data" / "eagle_companion.db")
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._db_lock = threading.RLock()
        self._voice_callback = voice_callback

        # v2.0 multi-campaign registry + v1.0 primary alias (`self.campaigns[cid]`)
        self.campaigns_by_char: dict[str, list[dict[str, Any]]] = {}
        self.selected_campaign_by_char: dict[str, str] = {}
        self.campaigns: dict[str, dict[str, Any]] = {}

        self.active_session: Optional[dict[str, Any]] = None
        # UI submodes while active: "read" | "backlog" | "flowchart" | "saveload"
        self.submode: str = "read"
        self.saveload_mode_hint: str = "save"  # "save" or "load"
        self.saveload_slot_cursor: int = 1  # 0=Auto-Save, 1..6=Manual Slots
        self.hide_ui: bool = False
        self.choice_cursor: int = 0
        self.backlog_scroll: int = 0
        self.flowchart_cursor: int = 0
        self.flowchart_col_offset: int = 0
        self._graph_cache: dict[str, dict[str, Any]] = {}
        self._last_voiced_beat_token: str = ""
        self._last_engine_ref: Any = None

        self._init_db()
        self.discover_campaigns()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(str(self.db_path), timeout=15.0)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self) -> None:
        """Creates or safely migrates v1.0 tables to v2.0 `(char_id, campaign_id)` composite keys + Save Slots."""
        with self._db_lock:
            conn = self._connect()
            try:
                # 1. Inspect existing tables for v1.0 -> v2.0 composite PK migration
                def _pk_cols(table_name: str) -> list[str]:
                    rows = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
                    return [str(r["name"]) for r in sorted((r for r in rows if int(r["pk"]) > 0), key=lambda x: int(x["pk"]))]

                def _has_col(table_name: str, col_name: str) -> bool:
                    rows = conn.execute(f"PRAGMA table_info({table_name})").fetchall()
                    return any(str(r["name"]) == col_name for r in rows)

                # Migrate story_quest_runs -> PRIMARY KEY (char_id, campaign_id)
                runs_pk = _pk_cols("story_quest_runs")
                if runs_pk == ["char_id"]:
                    conn.executescript(
                        """
                        ALTER TABLE story_quest_runs RENAME TO _story_quest_runs_v1;
                        CREATE TABLE story_quest_runs (
                            char_id TEXT NOT NULL,
                            campaign_id TEXT NOT NULL,
                            node_id TEXT NOT NULL,
                            beat_idx INTEGER NOT NULL DEFAULT 0,
                            active_opt_id TEXT NOT NULL DEFAULT '',
                            bond INTEGER NOT NULL DEFAULT 0,
                            insight INTEGER NOT NULL DEFAULT 0,
                            flags_json TEXT NOT NULL DEFAULT '[]',
                            visited_nodes_json TEXT NOT NULL DEFAULT '[]',
                            backlog_json TEXT NOT NULL DEFAULT '[]',
                            finished INTEGER NOT NULL DEFAULT 0,
                            ending_id TEXT NOT NULL DEFAULT '',
                            updated_at TEXT NOT NULL,
                            PRIMARY KEY (char_id, campaign_id)
                        );
                        INSERT OR REPLACE INTO story_quest_runs
                        SELECT char_id, campaign_id, node_id, beat_idx, active_opt_id,
                               bond, insight, flags_json, visited_nodes_json, backlog_json,
                               finished, ending_id, updated_at
                        FROM _story_quest_runs_v1;
                        DROP TABLE _story_quest_runs_v1;
                        """
                    )

                # Migrate story_quest_checkpoints -> PRIMARY KEY (char_id, campaign_id, checkpoint_id)
                cp_pk = _pk_cols("story_quest_checkpoints")
                if cp_pk and "campaign_id" not in cp_pk:
                    has_camp_col = _has_col("story_quest_checkpoints", "campaign_id")
                    camp_expr = (
                        "COALESCE(NULLIF(c.campaign_id, ''), (SELECT r.campaign_id FROM story_quest_runs r WHERE r.char_id = c.char_id LIMIT 1), c.char_id || '_sq1')"
                        if has_camp_col
                        else "COALESCE((SELECT r.campaign_id FROM story_quest_runs r WHERE r.char_id = c.char_id LIMIT 1), "
                        "CASE c.char_id WHEN 'hutao' THEN 'hutao_papilio_5ch_v1' "
                        "WHEN 'citlali' THEN 'citlali_sq1_color_of_eternity' "
                        "WHEN 'furina' THEN 'furina_sq1_unscripted_encore' ELSE c.char_id || '_sq1' END)"
                    )
                    conn.executescript(
                        f"""
                        ALTER TABLE story_quest_checkpoints RENAME TO _story_quest_checkpoints_v1;
                        CREATE TABLE story_quest_checkpoints (
                            char_id TEXT NOT NULL,
                            campaign_id TEXT NOT NULL,
                            checkpoint_id TEXT NOT NULL,
                            sort_order INTEGER NOT NULL DEFAULT 0,
                            chapter_id TEXT NOT NULL,
                            node_id TEXT NOT NULL,
                            beat_idx INTEGER NOT NULL DEFAULT 0,
                            label TEXT NOT NULL,
                            day_label TEXT NOT NULL DEFAULT '',
                            is_gate INTEGER NOT NULL DEFAULT 0,
                            bond INTEGER NOT NULL DEFAULT 0,
                            insight INTEGER NOT NULL DEFAULT 0,
                            flags_json TEXT NOT NULL DEFAULT '[]',
                            updated_at TEXT NOT NULL,
                            PRIMARY KEY (char_id, campaign_id, checkpoint_id)
                        );
                        INSERT OR REPLACE INTO story_quest_checkpoints
                        SELECT c.char_id, {camp_expr}, c.checkpoint_id, c.sort_order, c.chapter_id,
                               c.node_id, c.beat_idx, c.label, c.day_label, c.is_gate,
                               c.bond, c.insight, c.flags_json, c.updated_at
                        FROM _story_quest_checkpoints_v1 c;
                        DROP TABLE _story_quest_checkpoints_v1;
                        """
                    )

                # Migrate story_quest_unlocked_endings -> PRIMARY KEY (char_id, campaign_id, ending_id)
                end_pk = _pk_cols("story_quest_unlocked_endings")
                if end_pk and "campaign_id" not in end_pk:
                    conn.executescript(
                        """
                        ALTER TABLE story_quest_unlocked_endings RENAME TO _story_quest_unlocked_endings_v1;
                        CREATE TABLE story_quest_unlocked_endings (
                            char_id TEXT NOT NULL,
                            campaign_id TEXT NOT NULL,
                            ending_id TEXT NOT NULL,
                            unlocked_at TEXT NOT NULL,
                            bond INTEGER NOT NULL DEFAULT 0,
                            insight INTEGER NOT NULL DEFAULT 0,
                            flags_json TEXT NOT NULL DEFAULT '[]',
                            PRIMARY KEY (char_id, campaign_id, ending_id)
                        );
                        INSERT OR REPLACE INTO story_quest_unlocked_endings
                        SELECT char_id, campaign_id, ending_id, unlocked_at, bond, insight, flags_json
                        FROM _story_quest_unlocked_endings_v1;
                        DROP TABLE _story_quest_unlocked_endings_v1;
                        """
                    )

                # Ensure all v2.0 tables exist cleanly on fresh databases
                conn.executescript(
                    """
                    CREATE TABLE IF NOT EXISTS story_quest_runs (
                        char_id TEXT NOT NULL,
                        campaign_id TEXT NOT NULL,
                        node_id TEXT NOT NULL,
                        beat_idx INTEGER NOT NULL DEFAULT 0,
                        active_opt_id TEXT NOT NULL DEFAULT '',
                        bond INTEGER NOT NULL DEFAULT 0,
                        insight INTEGER NOT NULL DEFAULT 0,
                        flags_json TEXT NOT NULL DEFAULT '[]',
                        visited_nodes_json TEXT NOT NULL DEFAULT '[]',
                        backlog_json TEXT NOT NULL DEFAULT '[]',
                        finished INTEGER NOT NULL DEFAULT 0,
                        ending_id TEXT NOT NULL DEFAULT '',
                        updated_at TEXT NOT NULL,
                        PRIMARY KEY (char_id, campaign_id)
                    );

                    CREATE TABLE IF NOT EXISTS story_quest_checkpoints (
                        char_id TEXT NOT NULL,
                        campaign_id TEXT NOT NULL,
                        checkpoint_id TEXT NOT NULL,
                        sort_order INTEGER NOT NULL DEFAULT 0,
                        chapter_id TEXT NOT NULL,
                        node_id TEXT NOT NULL,
                        beat_idx INTEGER NOT NULL DEFAULT 0,
                        label TEXT NOT NULL,
                        day_label TEXT NOT NULL DEFAULT '',
                        is_gate INTEGER NOT NULL DEFAULT 0,
                        bond INTEGER NOT NULL DEFAULT 0,
                        insight INTEGER NOT NULL DEFAULT 0,
                        flags_json TEXT NOT NULL DEFAULT '[]',
                        updated_at TEXT NOT NULL,
                        PRIMARY KEY (char_id, campaign_id, checkpoint_id)
                    );

                    CREATE TABLE IF NOT EXISTS story_quest_unlocked_endings (
                        char_id TEXT NOT NULL,
                        campaign_id TEXT NOT NULL,
                        ending_id TEXT NOT NULL,
                        unlocked_at TEXT NOT NULL,
                        bond INTEGER NOT NULL DEFAULT 0,
                        insight INTEGER NOT NULL DEFAULT 0,
                        flags_json TEXT NOT NULL DEFAULT '[]',
                        PRIMARY KEY (char_id, campaign_id, ending_id)
                    );

                    CREATE TABLE IF NOT EXISTS story_quest_unlocked_cgs (
                        char_id TEXT NOT NULL,
                        cg_rel TEXT NOT NULL,
                        unlocked_at TEXT NOT NULL,
                        PRIMARY KEY (char_id, cg_rel)
                    );

                    CREATE TABLE IF NOT EXISTS story_quest_save_slots (
                        char_id TEXT NOT NULL,
                        campaign_id TEXT NOT NULL,
                        slot_idx INTEGER NOT NULL,
                        node_id TEXT NOT NULL,
                        beat_idx INTEGER NOT NULL DEFAULT 0,
                        active_opt_id TEXT NOT NULL DEFAULT '',
                        chapter_id TEXT NOT NULL DEFAULT 'CH1',
                        scene_title TEXT NOT NULL DEFAULT '',
                        day_label TEXT NOT NULL DEFAULT '',
                        cg_rel TEXT NOT NULL DEFAULT '',
                        bond INTEGER NOT NULL DEFAULT 0,
                        insight INTEGER NOT NULL DEFAULT 0,
                        flags_json TEXT NOT NULL DEFAULT '[]',
                        visited_nodes_json TEXT NOT NULL DEFAULT '[]',
                        backlog_json TEXT NOT NULL DEFAULT '[]',
                        finished INTEGER NOT NULL DEFAULT 0,
                        ending_id TEXT NOT NULL DEFAULT '',
                        saved_at TEXT NOT NULL,
                        PRIMARY KEY (char_id, campaign_id, slot_idx)
                    );
                    """
                )
                conn.commit()
            finally:
                conn.close()

    # ==========================================================================
    # CAMPAIGN DISCOVERY, MOVIE-POSTER ENRICHMENT & MULTI-CAMPAIGN REGISTRY
    # ==========================================================================
    def _enrich_campaign_metadata(self, camp: dict[str, Any]) -> dict[str, Any]:
        """Ensures every campaign exposes clean `poster_cg`, `title`, `subtitle`, and `synopsis`."""
        camp_id = str(camp.get("campaign_id") or "")
        defaults = DEFAULT_CAMPAIGN_POSTERS_AND_SYNOPSES.get(camp_id, {})

        # Resolve best available 16:9 poster/cover CG on disk
        candidates: list[str] = []
        if camp.get("poster_cg"):
            candidates.append(str(camp["poster_cg"]).strip())
        if camp.get("thumbnail_rel"):
            candidates.append(str(camp["thumbnail_rel"]).strip())
        if defaults.get("poster_cg"):
            candidates.append(defaults["poster_cg"])
        if defaults.get("fallback_cg"):
            candidates.append(defaults["fallback_cg"])

        # First beat CG of Chapter 1 entry node as universal fallback
        try:
            en = str(camp["chapters"][0]["entry_node"])
            first_b = ((camp["nodes"].get(en) or {}).get("beats") or [{}])[0]
            if first_b.get("cg"):
                candidates.append(str(first_b["cg"]).strip())
        except Exception:
            pass

        chosen_poster = ""
        for rel in candidates:
            if not rel:
                continue
            p = self.base_dir / Path(rel)
            if p.exists() and p.is_file() and p.stat().st_size >= 512:
                chosen_poster = rel
                break
        if not chosen_poster and candidates:
            chosen_poster = candidates[0]

        if not camp.get("poster_cg") or not (self.base_dir / Path(str(camp["poster_cg"]))).exists():
            if chosen_poster:
                camp["poster_cg"] = chosen_poster

        if not camp.get("synopsis"):
            if defaults.get("synopsis"):
                camp["synopsis"] = defaults["synopsis"]
            else:
                ch1_title = ""
                if camp.get("chapters"):
                    ch1_title = str(camp["chapters"][0].get("title", ""))
                camp["synopsis"] = sanitize_cfont_ascii(
                    f"{camp.get('subtitle', '')}. Experience a 5-chapter branching visual novel campaign ({ch1_title}) "
                    f"with persistent choices, clues, and {len(camp.get('endings') or {})} distinct endings."
                )
        return camp

    def register_campaign_dict(self, camp: dict[str, Any]) -> None:
        """Programmatic campaign registration (also used by Part A multi-campaign unit tests)."""
        if not isinstance(camp, dict) or not camp.get("char_id") or not camp.get("campaign_id"):
            return
        cid = str(camp["char_id"]).strip().lower()
        camp_id = str(camp["campaign_id"]).strip()
        enriched = self._enrich_campaign_metadata(camp)
        bucket = self.campaigns_by_char.setdefault(cid, [])
        existing_idx = next((i for i, c in enumerate(bucket) if str(c.get("campaign_id")) == camp_id), None)
        if existing_idx is not None:
            bucket[existing_idx] = enriched
        else:
            bucket.append(enriched)
        sel_id = self.selected_campaign_by_char.get(cid)
        if not sel_id or not any(str(c.get("campaign_id")) == sel_id for c in bucket):
            self.selected_campaign_by_char[cid] = str(bucket[0]["campaign_id"])
        self._refresh_primary_campaigns_view()

    def _refresh_primary_campaigns_view(self) -> None:
        primary: dict[str, dict[str, Any]] = {}
        for cid, bucket in self.campaigns_by_char.items():
            if not bucket:
                continue
            sel_id = self.selected_campaign_by_char.get(cid, "")
            picked = next((c for c in bucket if str(c.get("campaign_id")) == sel_id), bucket[0])
            primary[cid] = picked
        self.campaigns = primary

    def discover_campaigns(self) -> dict[str, dict[str, Any]]:
        """Auto-discovers all `eagle_story_quest_*.py` modules (both single & multi-campaign packs)."""
        by_char: dict[str, list[dict[str, Any]]] = {}
        seen_pairs: set[tuple[str, str]] = set()
        base_str = str(self.base_dir.resolve())
        if base_str not in sys.path:
            sys.path.insert(0, base_str)

        for mod_path in sorted(self.base_dir.glob("eagle_story_quest_*.py")):
            stem = mod_path.stem
            suffix = stem.removeprefix("eagle_story_quest_").strip()
            if not suffix or suffix.startswith("_"):
                continue
            try:
                mod = None
                if stem in sys.modules:
                    mod_file = getattr(sys.modules[stem], "__file__", "") or ""
                    if mod_file and Path(mod_file).resolve() == mod_path.resolve():
                        mod = importlib.reload(sys.modules[stem])
                if mod is None:
                    if Path(base_str) == mod_path.parent.resolve():
                        try:
                            mod = importlib.import_module(stem)
                        except Exception:
                            mod = None
                    if mod is None:
                        spec = importlib.util.spec_from_file_location(f"_sq_pack_{suffix}", str(mod_path))
                        if spec and spec.loader:
                            mod = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(mod)
                if mod is None:
                    continue

                raw_list: list[dict[str, Any]] = []
                multi = getattr(mod, "STORY_QUEST_CAMPAIGNS", None)
                if isinstance(multi, (list, tuple)):
                    for item in multi:
                        if isinstance(item, dict):
                            raw_list.append(item)
                single = getattr(mod, "STORY_QUEST_CAMPAIGN", None)
                if isinstance(single, dict):
                    raw_list.append(single)

                for camp in raw_list:
                    cid = str(camp.get("char_id") or "").strip().lower()
                    camp_id = str(camp.get("campaign_id") or "").strip()
                    if not cid or not camp_id or (cid, camp_id) in seen_pairs:
                        continue
                    seen_pairs.add((cid, camp_id))
                    by_char.setdefault(cid, []).append(self._enrich_campaign_metadata(camp))
            except Exception as exc:
                print(f"[StoryQuestEngine v2.0] Failed loading {mod_path.name}: {exc}")

        self.campaigns_by_char = by_char
        for cid, bucket in by_char.items():
            cur_sel = self.selected_campaign_by_char.get(cid, "")
            if not cur_sel or not any(str(c.get("campaign_id")) == cur_sel for c in bucket):
                self.selected_campaign_by_char[cid] = str(bucket[0]["campaign_id"])
        self._refresh_primary_campaigns_view()
        self._graph_cache.clear()
        return self.campaigns

    def is_active(self) -> bool:
        return self.active_session is not None

    def has_campaign(self, char_id: str) -> bool:
        cid = (char_id or "").strip().lower()
        if cid not in self.campaigns_by_char:
            self.discover_campaigns()
        return bool(self.campaigns_by_char.get(cid))

    def list_char_campaigns(self, char_id: str) -> list[dict[str, Any]]:
        cid = (char_id or "").strip().lower()
        if cid not in self.campaigns_by_char:
            self.discover_campaigns()
        return list(self.campaigns_by_char.get(cid) or [])

    def select_char_campaign(self, char_id: str, campaign_id_or_idx: str | int) -> Optional[dict[str, Any]]:
        cid = (char_id or "").strip().lower()
        bucket = self.list_char_campaigns(cid)
        if not bucket:
            return None
        picked: Optional[dict[str, Any]] = None
        if isinstance(campaign_id_or_idx, int):
            picked = bucket[campaign_id_or_idx % len(bucket)]
        else:
            s = str(campaign_id_or_idx).strip()
            if s.isdigit():
                picked = bucket[int(s) % len(bucket)]
            else:
                picked = next((c for c in bucket if str(c.get("campaign_id")) == s), None)
        if picked is not None:
            self.selected_campaign_by_char[cid] = str(picked["campaign_id"])
            self._refresh_primary_campaigns_view()
        return picked

    def get_campaign(self, char_id: str, campaign_id: Optional[str] = None) -> Optional[dict[str, Any]]:
        cid = (char_id or "").strip().lower()
        bucket = self.list_char_campaigns(cid)
        if not bucket:
            return None
        target_id = (campaign_id or self.selected_campaign_by_char.get(cid) or "").strip()
        if target_id:
            found = next((c for c in bucket if str(c.get("campaign_id")) == target_id), None)
            if found is not None:
                return found
        return bucket[0]

    def _node_sort_order(self, campaign: dict[str, Any], node_id: str) -> int:
        keys = list((campaign.get("nodes") or {}).keys())
        try:
            return keys.index(node_id)
        except ValueError:
            return 999

    def _active_beats_for_node(
        self, campaign: dict[str, Any], node_id: str, state: dict[str, Any], active_opt_id: str = ""
    ) -> list[dict[str, Any]]:
        node = campaign["nodes"][node_id]
        if active_opt_id:
            ch_obj = node.get("choice") or {}
            for opt in ch_obj.get("options") or []:
                if str(opt.get("opt_id")) == active_opt_id:
                    r_beats = [b for b in (opt.get("reaction_beats") or []) if evaluate_condition(b.get("when"), state)]
                    if r_beats:
                        return r_beats
            return []
        return [b for b in (node.get("beats") or []) if evaluate_condition(b.get("when"), state)]

    def _evaluate_choice_options(self, node: dict[str, Any], state: dict[str, Any]) -> list[dict[str, Any]]:
        ch_obj = node.get("choice")
        if not ch_obj:
            return []
        raw_opts = ch_obj.get("options") or []
        evaluated: list[dict[str, Any]] = []
        any_rescue_unlocked = False
        if ch_obj.get("exclusive_rescue_gate") and raw_opts:
            any_rescue_unlocked = evaluate_condition(raw_opts[0].get("when"), state)

        for idx, opt in enumerate(raw_opts):
            if ch_obj.get("exclusive_rescue_gate") and idx > 0 and any_rescue_unlocked:
                continue
            unlocked = evaluate_condition(opt.get("when"), state)
            tag = ""
            if unlocked and opt.get("unlock_badge"):
                tag = str(opt["unlock_badge"])
            elif not unlocked:
                tag = str(opt.get("lock_hint") or "[LOCKED]")
            evaluated.append(
                {
                    "opt_id": str(opt["opt_id"]),
                    "label": str(opt["label"]),
                    "unlocked": bool(unlocked),
                    "tag": tag,
                    "effects": opt.get("effects") or {},
                    "next_node": str(opt["next_node"]),
                    "reaction_beats": opt.get("reaction_beats") or [],
                }
            )
        return evaluated

    def _record_cg_unlock(self, conn: sqlite3.Connection, char_id: str, cg_rel: str) -> None:
        if not cg_rel:
            return
        now_s = datetime.datetime.now().isoformat(timespec="seconds")
        conn.execute(
            """
            INSERT INTO story_quest_unlocked_cgs (char_id, cg_rel, unlocked_at)
            VALUES (?, ?, ?)
            ON CONFLICT(char_id, cg_rel) DO NOTHING
            """,
            (char_id, cg_rel, now_s),
        )

    def _record_checkpoint(
        self, conn: sqlite3.Connection, sess: dict[str, Any], campaign: dict[str, Any], is_gate_point: bool = False
    ) -> None:
        cid = str(sess["char_id"])
        camp_id = str(sess["campaign_id"])
        nid = str(sess["node_id"])
        node = campaign["nodes"].get(nid)
        if not node:
            return
        ch_id = str(node.get("chapter_id", "CH1"))
        has_choice = node.get("choice") is not None
        cp_id = f"GATE:{node['choice']['choice_id']}" if (is_gate_point and has_choice) else f"NODE:{nid}"
        sort_ord = self._node_sort_order(campaign, nid) * 10 + (5 if is_gate_point else 0)
        lbl_prefix = f"[{ch_id}] "
        if is_gate_point and has_choice:
            lbl = f"{lbl_prefix}Choice {node['choice']['choice_id']}: {node.get('title', nid)}"
        else:
            lbl = f"{lbl_prefix}{nid} - {node.get('title', nid)}"
        now_s = datetime.datetime.now().isoformat(timespec="seconds")
        conn.execute(
            """
            INSERT INTO story_quest_checkpoints (
                char_id, campaign_id, checkpoint_id, sort_order, chapter_id, node_id, beat_idx,
                label, day_label, is_gate, bond, insight, flags_json, updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(char_id, campaign_id, checkpoint_id) DO UPDATE SET
                beat_idx = excluded.beat_idx,
                bond = excluded.bond,
                insight = excluded.insight,
                flags_json = excluded.flags_json,
                updated_at = excluded.updated_at
            """,
            (
                cid,
                camp_id,
                cp_id,
                sort_ord,
                ch_id,
                nid,
                int(sess["beat_idx"]) if is_gate_point else 0,
                sanitize_cfont_ascii(lbl),
                sanitize_cfont_ascii(node.get("day_label", "")),
                1 if (is_gate_point or has_choice) else 0,
                int(sess["bond"]),
                int(sess["insight"]),
                json.dumps(list(sess["flags"])),
                now_s,
            ),
        )

    def _record_ending_unlock(self, conn: sqlite3.Connection, sess: dict[str, Any]) -> None:
        ending_id = str(sess.get("ending_id") or "")
        if not ending_id:
            return
        now_s = datetime.datetime.now().isoformat(timespec="seconds")
        conn.execute(
            """
            INSERT INTO story_quest_unlocked_endings (
                char_id, campaign_id, ending_id, unlocked_at, bond, insight, flags_json
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(char_id, campaign_id, ending_id) DO UPDATE SET
                unlocked_at = excluded.unlocked_at,
                bond = MAX(story_quest_unlocked_endings.bond, excluded.bond),
                insight = MAX(story_quest_unlocked_endings.insight, excluded.insight),
                flags_json = excluded.flags_json
            """,
            (
                str(sess["char_id"]),
                str(sess["campaign_id"]),
                ending_id,
                now_s,
                int(sess["bond"]),
                int(sess["insight"]),
                json.dumps(list(sess["flags"])),
            ),
        )

    def _write_slot_row(
        self, conn: sqlite3.Connection, sess: dict[str, Any], campaign: dict[str, Any], slot_idx: int
    ) -> None:
        nid = str(sess["node_id"])
        node = campaign["nodes"].get(nid) or {}
        cur_beat = self._current_beat_obj(sess, campaign) or {}
        cg_rel = str(cur_beat.get("cg") or campaign.get("poster_cg") or "")
        saved_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        conn.execute(
            """
            INSERT INTO story_quest_save_slots (
                char_id, campaign_id, slot_idx, node_id, beat_idx, active_opt_id,
                chapter_id, scene_title, day_label, cg_rel,
                bond, insight, flags_json, visited_nodes_json, backlog_json,
                finished, ending_id, saved_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(char_id, campaign_id, slot_idx) DO UPDATE SET
                node_id = excluded.node_id,
                beat_idx = excluded.beat_idx,
                active_opt_id = excluded.active_opt_id,
                chapter_id = excluded.chapter_id,
                scene_title = excluded.scene_title,
                day_label = excluded.day_label,
                cg_rel = excluded.cg_rel,
                bond = excluded.bond,
                insight = excluded.insight,
                flags_json = excluded.flags_json,
                visited_nodes_json = excluded.visited_nodes_json,
                backlog_json = excluded.backlog_json,
                finished = excluded.finished,
                ending_id = excluded.ending_id,
                saved_at = excluded.saved_at
            """,
            (
                str(sess["char_id"]),
                str(sess["campaign_id"]),
                int(slot_idx),
                nid,
                int(sess["beat_idx"]),
                str(sess.get("active_opt_id") or ""),
                sanitize_cfont_ascii(node.get("chapter_id", "CH1")),
                sanitize_cfont_ascii(node.get("title", nid)),
                sanitize_cfont_ascii(node.get("day_label", "")),
                cg_rel,
                int(sess["bond"]),
                int(sess["insight"]),
                json.dumps(list(sess["flags"])),
                json.dumps(list(sess["visited_nodes"])),
                json.dumps(list(sess.get("backlog") or [])[-120:]),
                1 if sess.get("finished") else 0,
                str(sess.get("ending_id") or ""),
                saved_at,
            ),
        )

    def _append_current_beat_to_backlog(self, sess: dict[str, Any], beat: dict[str, Any]) -> None:
        bid = str(beat.get("beat_id") or f"{sess['node_id']}_{sess['beat_idx']}")
        backlog: list[dict[str, Any]] = sess.setdefault("backlog", [])
        if backlog and backlog[-1].get("beat_id") == bid and not backlog[-1].get("is_choice"):
            return
        backlog.append(
            {
                "beat_id": bid,
                "node_id": str(sess["node_id"]),
                "speaker": sanitize_cfont_ascii(beat.get("speaker") or "Narrator"),
                "text": sanitize_cfont_ascii(beat.get("text") or ""),
                "inner_thought": sanitize_cfont_ascii(beat.get("inner_thought") or ""),
                "is_choice": False,
            }
        )
        if len(backlog) > 120:
            del backlog[:-120]

    def _persist_session(
        self, sess: dict[str, Any], record_node_cp: bool = False, record_gate_cp: bool = False
    ) -> None:
        camp = self.get_campaign(sess["char_id"], sess.get("campaign_id"))
        if not camp:
            return
        cur_beat = self._current_beat_obj(sess, camp)
        now_s = datetime.datetime.now().isoformat(timespec="seconds")
        with self._db_lock:
            conn = self._connect()
            try:
                if cur_beat and cur_beat.get("cg"):
                    self._record_cg_unlock(conn, str(sess["char_id"]), str(cur_beat["cg"]))
                if record_node_cp:
                    self._record_checkpoint(conn, sess, camp, is_gate_point=False)
                if record_gate_cp:
                    self._record_checkpoint(conn, sess, camp, is_gate_point=True)
                if sess.get("finished") and sess.get("ending_id"):
                    self._record_ending_unlock(conn, sess)

                conn.execute(
                    """
                    INSERT INTO story_quest_runs (
                        char_id, campaign_id, node_id, beat_idx, active_opt_id,
                        bond, insight, flags_json, visited_nodes_json, backlog_json,
                        finished, ending_id, updated_at
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(char_id, campaign_id) DO UPDATE SET
                        node_id = excluded.node_id,
                        beat_idx = excluded.beat_idx,
                        active_opt_id = excluded.active_opt_id,
                        bond = excluded.bond,
                        insight = excluded.insight,
                        flags_json = excluded.flags_json,
                        visited_nodes_json = excluded.visited_nodes_json,
                        backlog_json = excluded.backlog_json,
                        finished = excluded.finished,
                        ending_id = excluded.ending_id,
                        updated_at = excluded.updated_at
                    """,
                    (
                        str(sess["char_id"]),
                        str(sess["campaign_id"]),
                        str(sess["node_id"]),
                        int(sess["beat_idx"]),
                        str(sess.get("active_opt_id") or ""),
                        int(sess["bond"]),
                        int(sess["insight"]),
                        json.dumps(list(sess["flags"])),
                        json.dumps(list(sess["visited_nodes"])),
                        json.dumps(list(sess.get("backlog") or [])[-120:]),
                        1 if sess.get("finished") else 0,
                        str(sess.get("ending_id") or ""),
                        now_s,
                    ),
                )
                # Always keep Slot 0 (Auto-Save) synchronized with the latest beat!
                self._write_slot_row(conn, sess, camp, slot_idx=0)
                conn.commit()
            finally:
                conn.close()

    def _current_beat_obj(self, sess: dict[str, Any], campaign: dict[str, Any]) -> Optional[dict[str, Any]]:
        nid = str(sess["node_id"])
        if nid not in campaign["nodes"]:
            return None
        st = {"bond": sess["bond"], "insight": sess["insight"], "flags": sess["flags"]}
        beats = self._active_beats_for_node(campaign, nid, st, str(sess.get("active_opt_id") or ""))
        if not beats:
            beats = self._active_beats_for_node(campaign, nid, st, "")
        if not beats:
            return None
        b_idx = max(0, min(int(sess["beat_idx"]), len(beats) - 1))
        return beats[b_idx]

    def _maybe_trigger_beat_voice(self, engine: Any, sess: dict[str, Any], campaign: dict[str, Any]) -> None:
        if sess.get("finished"):
            return
        beat = self._current_beat_obj(sess, campaign)
        if not beat:
            return
        token = f"{sess['char_id']}:{sess['campaign_id']}:{sess['node_id']}:{sess.get('active_opt_id', '')}:{sess['beat_idx']}"
        if token == self._last_voiced_beat_token:
            return
        self._last_voiced_beat_token = token

        ve = str(beat.get("voice_emotion") or "").strip()
        if not ve:
            return
        cid = str(sess["char_id"])
        if self._voice_callback is not None:
            try:
                self._voice_callback(engine, cid, ve)
                return
            except Exception:
                pass
        ds = getattr(engine, "dating_sim", None) if engine is not None else None
        if ds is not None and hasattr(ds, "_play_voice_safe"):
            try:
                ds._play_voice_safe(engine, cid, ve, mood=ve, interrupt=True, force_cooldown=True)
            except Exception:
                pass

    def _sync_bgm_safe(self, engine: Any = None) -> None:
        eng = engine if engine is not None else self._last_engine_ref
        if eng is not None:
            self._last_engine_ref = eng
            ds = getattr(eng, "dating_sim", None)
            if ds is not None and hasattr(ds, "sync_bgm_with_engine"):
                try:
                    ds.sync_bgm_with_engine(eng)
                except Exception:
                    pass

    def _enter_node(self, sess: dict[str, Any], campaign: dict[str, Any], next_target: str, engine: Any = None) -> None:
        if next_target in campaign["endings"]:
            sess["active_opt_id"] = ""
            sess["finished"] = True
            sess["ending_id"] = next_target
            self._persist_session(sess)
            self._sync_bgm_safe(engine)
            return

        sess["node_id"] = next_target
        sess["beat_idx"] = 0
        sess["active_opt_id"] = ""
        sess["finished"] = False
        sess["ending_id"] = ""
        if next_target not in sess["visited_nodes"]:
            sess["visited_nodes"].append(next_target)

        node = campaign["nodes"][next_target]
        st = {"bond": sess["bond"], "insight": sess["insight"], "flags": list(sess["flags"])}
        for ev in node.get("pre_events") or []:
            if evaluate_condition(ev.get("when"), st):
                st = apply_effects(st, ev.get("effects"))
        sess["bond"] = int(st["bond"])
        sess["insight"] = int(st["insight"])
        sess["flags"] = list(st["flags"])

        cur_beat = self._current_beat_obj(sess, campaign)
        if cur_beat:
            self._append_current_beat_to_backlog(sess, cur_beat)

        beats = self._active_beats_for_node(campaign, next_target, st, "")
        at_choice_gate = (node.get("choice") is not None) and (len(beats) <= 1)
        self.choice_cursor = 0
        self._persist_session(sess, record_node_cp=True, record_gate_cp=at_choice_gate)
        self._sync_bgm_safe(engine)
        self._maybe_trigger_beat_voice(engine, sess, campaign)

    # ==========================================================================
    # CAMPAIGN STATUS, MULTI-CAMPAIGN SUMMARY & 7-SLOT SAVE/LOAD API
    # ==========================================================================
    def get_char_status(self, char_id: str, campaign_id: Optional[str] = None) -> dict[str, Any]:
        cid = (char_id or "").strip().lower()
        all_camps = self.list_char_campaigns(cid)
        camp = self.get_campaign(cid, campaign_id)
        if not camp:
            return {
                "available": False,
                "char_id": cid,
                "quest_count": 0,
                "has_save": False,
                "poster_cg": "",
                "title": "Story Quest Coming Soon",
                "subtitle": "Pure Branching Visual Novel Slot Ready",
                "synopsis": "A dedicated 5-chapter branching visual novel campaign for this heroine will arrive in a future pack.",
                "progress_pct": 0,
                "explored_nodes_count": 0,
                "total_nodes": 0,
                "discovered_clues_count": 0,
                "total_clues": 0,
                "unlocked_endings": [],
                "unlocked_endings_count": 0,
                "total_endings": 5,
                "ending_badges": [],
                "unlocked_cgs_count": 0,
            }

        camp_id = str(camp["campaign_id"])
        total_endings = len(camp.get("endings") or {})
        total_nodes = len(camp.get("nodes") or {})
        flag_cat = camp.get("flag_catalog") or {}
        total_clues = len(flag_cat)

        with self._db_lock:
            conn = self._connect()
            try:
                run_row = conn.execute(
                    "SELECT * FROM story_quest_runs WHERE char_id = ? AND campaign_id = ?",
                    (cid, camp_id),
                ).fetchone()
                end_rows = conn.execute(
                    "SELECT ending_id FROM story_quest_unlocked_endings WHERE char_id = ? AND campaign_id = ? ORDER BY ending_id",
                    (cid, camp_id),
                ).fetchall()
                cg_cnt = conn.execute(
                    "SELECT COUNT(*) AS cnt FROM story_quest_unlocked_cgs WHERE char_id = ?",
                    (cid,),
                ).fetchone()["cnt"]
                cp_rows = conn.execute(
                    "SELECT node_id, flags_json FROM story_quest_checkpoints WHERE char_id = ? AND campaign_id = ?",
                    (cid, camp_id),
                ).fetchall()
            finally:
                conn.close()

        explored_nodes: set[str] = set()
        discovered_clues: set[str] = set()
        for cr in cp_rows:
            explored_nodes.add(str(cr["node_id"]))
            for fl in json.loads(cr["flags_json"] or "[]"):
                if fl in flag_cat:
                    discovered_clues.add(str(fl))
        if run_row is not None:
            for vn in json.loads(run_row["visited_nodes_json"] or "[]"):
                if vn in (camp.get("nodes") or {}):
                    explored_nodes.add(str(vn))
            for fl in json.loads(run_row["flags_json"] or "[]"):
                if fl in flag_cat:
                    discovered_clues.add(str(fl))

        unlocked_end_set = {str(r["ending_id"]) for r in end_rows}
        ending_badges: list[dict[str, Any]] = []
        for eid, emeta in (camp.get("endings") or {}).items():
            is_unlk = eid in unlocked_end_set
            ending_badges.append(
                {
                    "ending_id": str(eid),
                    "rank": sanitize_cfont_ascii(emeta.get("rank", eid)),
                    "title": sanitize_cfont_ascii(emeta.get("title", eid)) if is_unlk else "[???]",
                    "unlocked": is_unlk,
                }
            )

        has_save = run_row is not None
        node_id = str(run_row["node_id"]) if has_save else str(camp["chapters"][0]["entry_node"])
        node_meta = camp["nodes"].get(node_id) or {}
        progress_pct = int(round((len(explored_nodes) * 100.0) / max(1, total_nodes)))

        return {
            "available": True,
            "char_id": cid,
            "quest_count": len(all_camps),
            "campaign_id": camp_id,
            "title": sanitize_cfont_ascii(camp["title"]),
            "subtitle": sanitize_cfont_ascii(camp.get("subtitle", "")),
            "poster_cg": str(camp.get("poster_cg") or ""),
            "synopsis": sanitize_cfont_ascii(camp.get("synopsis") or ""),
            "has_save": has_save,
            "finished": bool(run_row["finished"]) if has_save else False,
            "ending_id": str(run_row["ending_id"]) if has_save else "",
            "node_id": node_id,
            "chapter_id": str(node_meta.get("chapter_id", "CH1")),
            "node_title": sanitize_cfont_ascii(node_meta.get("title", "")),
            "day_label": sanitize_cfont_ascii(node_meta.get("day_label", "")),
            "beat_idx": int(run_row["beat_idx"]) if has_save else 0,
            "bond": int(run_row["bond"]) if has_save else 0,
            "insight": int(run_row["insight"]) if has_save else 0,
            "explored_nodes_count": len(explored_nodes),
            "total_nodes": total_nodes,
            "progress_pct": progress_pct,
            "discovered_clues_count": len(discovered_clues),
            "total_clues": total_clues,
            "unlocked_endings": sorted(unlocked_end_set),
            "unlocked_endings_count": len(unlocked_end_set),
            "total_endings": total_endings,
            "ending_badges": ending_badges,
            "unlocked_cgs_count": int(cg_cnt),
            "checkpoints_count": len(cp_rows),
        }

    def list_char_campaigns_status(self, char_id: str) -> list[dict[str, Any]]:
        cid = (char_id or "").strip().lower()
        return [self.get_char_status(cid, str(c["campaign_id"])) for c in self.list_char_campaigns(cid)]

    def list_campaigns_summary(self) -> list[dict[str, Any]]:
        self.discover_campaigns()
        out: list[dict[str, Any]] = []
        for cid in sorted(self.campaigns_by_char.keys()):
            for c in self.campaigns_by_char[cid]:
                out.append(self.get_char_status(cid, str(c["campaign_id"])))
        return out

    def list_save_slots(self, char_id: Optional[str] = None, campaign_id: Optional[str] = None) -> list[dict[str, Any]]:
        """Returns 7 Save Slot dicts (`slot_idx = 0` Auto-Save + `slot_idx = 1..6` Manual Slots)."""
        sess = self.active_session
        cid = (char_id or (sess["char_id"] if sess else "hutao")).strip().lower()
        camp = self.get_campaign(cid, campaign_id or (sess["campaign_id"] if sess and sess["char_id"] == cid else None))
        if not camp:
            return [
                {
                    "slot_idx": i,
                    "slot_label": "AUTO-SAVE" if i == 0 else f"SLOT {i}",
                    "occupied": False,
                }
                for i in range(7)
            ]
        camp_id = str(camp["campaign_id"])
        flag_cat = camp.get("flag_catalog") or {}
        with self._db_lock:
            conn = self._connect()
            try:
                rows = conn.execute(
                    "SELECT * FROM story_quest_save_slots WHERE char_id = ? AND campaign_id = ? ORDER BY slot_idx ASC",
                    (cid, camp_id),
                ).fetchall()
                run_row = conn.execute(
                    "SELECT * FROM story_quest_runs WHERE char_id = ? AND campaign_id = ?",
                    (cid, camp_id),
                ).fetchone()
            finally:
                conn.close()

        by_idx = {int(r["slot_idx"]): r for r in rows}
        # Backfill Slot 0 virtually if an older pre-v2.0 run exists before first v2.0 persist
        if 0 not in by_idx and run_row is not None:
            nid = str(run_row["node_id"])
            node = camp["nodes"].get(nid) or {}
            b0 = (node.get("beats") or [{}])[0]
            by_idx[0] = {
                "slot_idx": 0,
                "node_id": nid,
                "beat_idx": int(run_row["beat_idx"]),
                "active_opt_id": str(run_row["active_opt_id"] or ""),
                "chapter_id": str(node.get("chapter_id", "CH1")),
                "scene_title": str(node.get("title", nid)),
                "day_label": str(node.get("day_label", "")),
                "cg_rel": str(b0.get("cg") or camp.get("poster_cg") or ""),
                "bond": int(run_row["bond"]),
                "insight": int(run_row["insight"]),
                "flags_json": run_row["flags_json"],
                "finished": int(run_row["finished"]),
                "ending_id": str(run_row["ending_id"] or ""),
                "saved_at": str(run_row["updated_at"])[:16].replace("T", " "),
            }

        slots: list[dict[str, Any]] = []
        for idx in range(7):
            lbl = "AUTO-SAVE" if idx == 0 else f"SAVE SLOT {idx}"
            r = by_idx.get(idx)
            if r is None:
                slots.append(
                    {
                        "slot_idx": idx,
                        "slot_label": lbl,
                        "occupied": False,
                        "chapter_id": "--",
                        "scene_title": "[Empty Slot]",
                        "day_label": "",
                        "cg_rel": "",
                        "bond": 0,
                        "insight": 0,
                        "clues_count": 0,
                        "total_clues": len(flag_cat),
                        "saved_at": "--",
                    }
                )
            else:
                fls = json.loads(r["flags_json"] or "[]")
                clues_cnt = sum(1 for f in fls if f in flag_cat)
                slots.append(
                    {
                        "slot_idx": idx,
                        "slot_label": lbl,
                        "occupied": True,
                        "node_id": str(r["node_id"]),
                        "beat_idx": int(r["beat_idx"]),
                        "chapter_id": sanitize_cfont_ascii(r["chapter_id"]),
                        "scene_title": sanitize_cfont_ascii(r["scene_title"]),
                        "day_label": sanitize_cfont_ascii(r["day_label"]),
                        "cg_rel": str(r["cg_rel"] or ""),
                        "bond": int(r["bond"]),
                        "insight": int(r["insight"]),
                        "clues_count": clues_cnt,
                        "total_clues": len(flag_cat),
                        "finished": bool(r["finished"]),
                        "ending_id": str(r["ending_id"] or ""),
                        "saved_at": sanitize_cfont_ascii(r["saved_at"]),
                    }
                )
        return slots

    def save_to_slot(
        self,
        slot_idx: int,
        char_id: Optional[str] = None,
        campaign_id: Optional[str] = None,
        engine: Any = None,
    ) -> dict[str, Any]:
        """Saves either the live `active_session` or the persisted `story_quest_runs` row into Manual Slot `1..6`."""
        s_idx = int(slot_idx)
        if not (1 <= s_idx <= 6):
            return {"ok": False, "error": "Manual save requires slot_idx 1..6"}

        sess = self.active_session
        target_cid = (char_id or (sess["char_id"] if sess else "hutao")).strip().lower()
        camp = self.get_campaign(
            target_cid, campaign_id or (sess["campaign_id"] if sess and sess["char_id"] == target_cid else None)
        )
        if not camp:
            return {"ok": False, "error": f"No campaign found for {target_cid!r}"}

        camp_id = str(camp["campaign_id"])
        snap_sess: Optional[dict[str, Any]] = None
        if sess is not None and sess["char_id"] == target_cid and sess["campaign_id"] == camp_id:
            snap_sess = sess
        else:
            with self._db_lock:
                conn = self._connect()
                try:
                    run_row = conn.execute(
                        "SELECT * FROM story_quest_runs WHERE char_id = ? AND campaign_id = ?",
                        (target_cid, camp_id),
                    ).fetchone()
                finally:
                    conn.close()
            if run_row is not None:
                snap_sess = {
                    "char_id": target_cid,
                    "campaign_id": camp_id,
                    "node_id": str(run_row["node_id"]),
                    "beat_idx": int(run_row["beat_idx"]),
                    "active_opt_id": str(run_row["active_opt_id"] or ""),
                    "bond": int(run_row["bond"]),
                    "insight": int(run_row["insight"]),
                    "flags": json.loads(run_row["flags_json"] or "[]"),
                    "visited_nodes": json.loads(run_row["visited_nodes_json"] or "[]"),
                    "backlog": json.loads(run_row["backlog_json"] or "[]"),
                    "finished": bool(run_row["finished"]),
                    "ending_id": str(run_row["ending_id"] or ""),
                }

        if snap_sess is None:
            return {"ok": False, "error": "Start or play at least 1 scene before saving to a manual slot"}

        with self._db_lock:
            conn = self._connect()
            try:
                self._write_slot_row(conn, snap_sess, camp, s_idx)
                conn.commit()
            finally:
                conn.close()

        self.saveload_slot_cursor = s_idx
        if engine is not None and hasattr(engine, "last_toast"):
            engine.last_toast = f"Saved progress to Slot {s_idx}!"
        return {"ok": True, "saved_slot": s_idx, "slots": self.list_save_slots(target_cid, camp_id)}

    def load_from_slot(
        self,
        slot_idx: int,
        char_id: Optional[str] = None,
        campaign_id: Optional[str] = None,
        engine: Any = None,
    ) -> dict[str, Any]:
        """Loads exact beat & causal state from `slot_idx` (`0..6`) and enters active Story Quest VN."""
        s_idx = int(slot_idx)
        if not (0 <= s_idx <= 6):
            return {"ok": False, "error": "slot_idx must be 0..6"}

        sess_cur = self.active_session
        target_cid = (char_id or (sess_cur["char_id"] if sess_cur else "hutao")).strip().lower()
        camp = self.get_campaign(
            target_cid, campaign_id or (sess_cur["campaign_id"] if sess_cur and sess_cur["char_id"] == target_cid else None)
        )
        if not camp:
            return {"ok": False, "error": f"No campaign found for {target_cid!r}"}
        camp_id = str(camp["campaign_id"])
        self.selected_campaign_by_char[target_cid] = camp_id
        self._refresh_primary_campaigns_view()

        if s_idx == 0:
            with self._db_lock:
                conn = self._connect()
                try:
                    s0 = conn.execute(
                        "SELECT * FROM story_quest_save_slots WHERE char_id = ? AND campaign_id = ? AND slot_idx = 0",
                        (target_cid, camp_id),
                    ).fetchone()
                finally:
                    conn.close()
            if s0 is None:
                return self.start_or_continue(target_cid, restart=False, engine=engine, campaign_id=camp_id)

        with self._db_lock:
            conn = self._connect()
            try:
                row = conn.execute(
                    "SELECT * FROM story_quest_save_slots WHERE char_id = ? AND campaign_id = ? AND slot_idx = ?",
                    (target_cid, camp_id, s_idx),
                ).fetchone()
            finally:
                conn.close()

        if row is None:
            return {"ok": False, "error": f"Slot {s_idx} is empty"}

        nid = str(row["node_id"])
        if nid not in camp["nodes"]:
            return {"ok": False, "error": f"Saved node {nid!r} missing from campaign"}

        if engine is not None:
            ds = getattr(engine, "dating_sim", None)
            if ds is not None:
                ds.active_vn_session = None
                ds.active_house_menu = None
            engine.wl_typing_active = False
            engine.phone_open = 0
            if hasattr(engine, "_update_touch_capture"):
                try:
                    engine._update_touch_capture(bool(getattr(engine, "touch_mode", True)))
                except Exception:
                    pass

        sess = {
            "char_id": target_cid,
            "campaign_id": camp_id,
            "node_id": nid,
            "beat_idx": int(row["beat_idx"]),
            "active_opt_id": str(row["active_opt_id"] or ""),
            "bond": int(row["bond"]),
            "insight": int(row["insight"]),
            "flags": json.loads(row["flags_json"] or "[]"),
            "visited_nodes": json.loads(row["visited_nodes_json"] or "[]"),
            "backlog": json.loads(row["backlog_json"] or "[]"),
            "finished": bool(row["finished"]),
            "ending_id": str(row["ending_id"] or ""),
        }
        st = {"bond": sess["bond"], "insight": sess["insight"], "flags": sess["flags"]}
        beats = self._active_beats_for_node(camp, nid, st, sess["active_opt_id"])
        if not beats:
            sess["active_opt_id"] = ""
            beats = self._active_beats_for_node(camp, nid, st, "")
        sess["beat_idx"] = max(0, min(int(sess["beat_idx"]), max(0, len(beats) - 1)))

        self.active_session = sess
        self.submode = "read"
        self.hide_ui = False
        self.choice_cursor = 0
        self._last_voiced_beat_token = ""
        self._persist_session(sess)
        self._sync_bgm_safe(engine)
        self._maybe_trigger_beat_voice(engine, sess, camp)
        return {"ok": True, "loaded_slot": s_idx, "state": self.get_api_state(target_cid)}

    def delete_save_slot(
        self, slot_idx: int, char_id: Optional[str] = None, campaign_id: Optional[str] = None
    ) -> dict[str, Any]:
        s_idx = int(slot_idx)
        if not (1 <= s_idx <= 6):
            return {"ok": False, "error": "Only manual slots 1..6 can be deleted"}
        sess = self.active_session
        cid = (char_id or (sess["char_id"] if sess else "hutao")).strip().lower()
        camp = self.get_campaign(cid, campaign_id or (sess["campaign_id"] if sess and sess["char_id"] == cid else None))
        if not camp:
            return {"ok": False, "error": "No campaign"}
        camp_id = str(camp["campaign_id"])
        with self._db_lock:
            conn = self._connect()
            try:
                conn.execute(
                    "DELETE FROM story_quest_save_slots WHERE char_id = ? AND campaign_id = ? AND slot_idx = ?",
                    (cid, camp_id, s_idx),
                )
                conn.commit()
            finally:
                conn.close()
        return {"ok": True, "deleted_slot": s_idx, "slots": self.list_save_slots(cid, camp_id)}

    # ==========================================================================
    # 2D CAUSAL GRAPH BUILDER (`(col, lane)` + DIRECTED EDGES ACROSS CH.1 -> CH.5)
    # ==========================================================================
    def build_causal_graph_2d(
        self, char_id: Optional[str] = None, campaign_id: Optional[str] = None
    ) -> dict[str, Any]:
        """
        Builds a deterministic, zero-overlap 2D `(col, lane)` node-and-edge layout for any Story Quest pack,
        annotated with live unlock/checkpoint/ending telemetry from SQLite.
        """
        sess = self.active_session
        cid = (char_id or (sess["char_id"] if sess else "hutao")).strip().lower()
        camp = self.get_campaign(cid, campaign_id or (sess["campaign_id"] if sess and sess["char_id"] == cid else None))
        if not camp:
            return {"available": False, "columns": 0, "nodes": [], "edges": [], "chapter_start_cols": {}}

        camp_id = str(camp["campaign_id"])
        cache_key = f"{cid}:{camp_id}"
        static_layout = self._graph_cache.get(cache_key)
        if static_layout is None:
            static_layout = self._compute_static_2d_layout(camp)
            self._graph_cache[cache_key] = static_layout

        # Overlay live SQLite checkpoints, current node, and unlocked endings
        cps = self.list_checkpoints(cid, camp_id)
        cp_by_node: dict[str, dict[str, Any]] = {}
        for cp in cps:
            nid = cp["node_id"]
            # Prefer GATE checkpoint when available so Time-Jump lands right at the decision!
            if nid not in cp_by_node or cp["is_gate"]:
                cp_by_node[nid] = cp

        status = self.get_char_status(cid, camp_id)
        unlocked_endings = set(status.get("unlocked_endings") or [])
        cur_nid = ""
        if sess is not None and sess["char_id"] == cid and sess["campaign_id"] == camp_id:
            cur_nid = str(sess.get("ending_id") if sess.get("finished") else sess.get("node_id") or "")
        elif status.get("has_save"):
            cur_nid = str(status.get("ending_id") if status.get("finished") else status.get("node_id") or "")

        flag_cat = camp.get("flag_catalog") or {}
        live_nodes: list[dict[str, Any]] = []
        unlocked_ids: set[str] = set()

        for sn in static_layout["nodes"]:
            nid = sn["id"]
            ntype = sn["kind"]
            if ntype == "ending":
                is_unlk = nid in unlocked_endings
                if is_unlk:
                    unlocked_ids.add(nid)
                emeta = (camp.get("endings") or {}).get(nid) or {}
                live_nodes.append(
                    {
                        **sn,
                        "unlocked": is_unlk,
                        "is_current": (nid == cur_nid),
                        "can_jump": False,
                        "checkpoint_id": "",
                        "display_title": sanitize_cfont_ascii(emeta.get("title", nid)) if is_unlk else "[???] Locked Ending",
                        "badge": sanitize_cfont_ascii(emeta.get("rank", "END")),
                        "meta_line": sanitize_cfont_ascii(emeta.get("summary", ""))[:96] if is_unlk else "Explore causal branches to unlock this ending.",
                    }
                )
            else:
                cp = cp_by_node.get(nid)
                is_unlk = cp is not None or (nid == cur_nid)
                if is_unlk:
                    unlocked_ids.add(nid)
                clues_n = sum(1 for f in (cp["flags"] if cp else []) if f in flag_cat)
                badge = "[COMBO]" if ntype == "combo_gate" else ("[?]" if ntype == "choice_gate" else sn["chapter_id"])
                live_nodes.append(
                    {
                        **sn,
                        "unlocked": is_unlk,
                        "is_current": (nid == cur_nid),
                        "can_jump": cp is not None,
                        "checkpoint_id": str(cp["checkpoint_id"]) if cp else "",
                        "display_title": sn["short_title"] if is_unlk else "[???] Unexplored",
                        "full_title": sn["title"] if is_unlk else "[???] Unexplored Scene",
                        "badge": badge,
                        "bond": int(cp["bond"]) if cp else 0,
                        "insight": int(cp["insight"]) if cp else 0,
                        "clues": clues_n,
                        "day_label": sn["day_label"] if is_unlk else "???",
                        "meta_line": (
                            f"{sn['day_label']}  |  Bond {cp['bond']}  Insight {cp['insight']}  Clues {clues_n}/{len(flag_cat)}"
                            if cp
                            else "Reach this branch in Story Quest to unlock Time-Jump."
                        ),
                    }
                )

        live_edges: list[dict[str, Any]] = []
        for ed in static_layout["edges"]:
            live_edges.append(
                {
                    **ed,
                    "visited": (ed["src"] in unlocked_ids and ed["dst"] in unlocked_ids),
                }
            )

        return {
            "available": True,
            "char_id": cid,
            "campaign_id": camp_id,
            "columns": static_layout["columns"],
            "max_lanes": static_layout["max_lanes"],
            "chapter_start_cols": static_layout["chapter_start_cols"],
            "nodes": live_nodes,
            "edges": live_edges,
        }

    def _compute_static_2d_layout(self, camp: dict[str, Any]) -> dict[str, Any]:
        """Assigns every scene node & 5 endings to a unique `(col, lane)` cell (`0 <= lane < 5`) with zero overlap."""
        nodes_map: dict[str, dict[str, Any]] = camp["nodes"]
        endings_map: dict[str, dict[str, Any]] = camp["endings"]
        chapters: list[dict[str, Any]] = camp["chapters"]

        # Build outgoing adjacency & classify node types
        adj: dict[str, list[tuple[str, str]]] = {}  # src -> [(dst, edge_kind)]
        node_kind: dict[str, str] = {}
        for nid, node in nodes_map.items():
            outs: list[tuple[str, str]] = []
            ch_obj = node.get("choice")
            is_combo = False
            if ch_obj:
                if ch_obj.get("exclusive_rescue_gate"):
                    is_combo = True
                for opt in ch_obj.get("options") or []:
                    ek = "normal"
                    ub = str(opt.get("unlock_badge") or "").upper()
                    if _is_combination_condition(opt.get("when")) or any(
                        w in ub for w in ("COMBO", "RESCUE", "PRISM", "HARMONIC", "COUNTER", "CO-STAR", "TRUE")
                    ):
                        is_combo = True
                        ek = "combo"
                    nxt = str(opt["next_node"])
                    if not any(d == nxt for d, _ in outs):
                        outs.append((nxt, ek))
                node_kind[nid] = "combo_gate" if is_combo else "choice_gate"
            elif node.get("ending_id"):
                eid = str(node["ending_id"])
                outs.append((eid, "ending"))
                node_kind[nid] = "scene"
            else:
                for rule in node.get("routing") or []:
                    ek = "combo" if _is_combination_condition(rule.get("when")) else "normal"
                    if ek == "combo":
                        is_combo = True
                    nxt = str(rule["next_node"])
                    if not any(d == nxt for d, _ in outs):
                        outs.append((nxt, ek))
                node_kind[nid] = "combo_gate" if is_combo else "scene"
            adj[nid] = outs

        # Group scene nodes by chapter in authored order, then compute local topological depth per chapter
        ch_order = [str(ch["chapter_id"]) for ch in chapters]
        nodes_by_ch: dict[str, list[str]] = {c: [] for c in ch_order}
        for nid, node in nodes_map.items():
            c = str(node.get("chapter_id") or ch_order[0])
            nodes_by_ch.setdefault(c, []).append(nid)

        coords: dict[str, tuple[int, int]] = {}
        chapter_start_cols: dict[str, int] = {}
        cur_global_col = 0
        MAX_LANES = 5

        for c_id in ch_order:
            c_nodes = nodes_by_ch.get(c_id) or []
            if not c_nodes:
                continue
            chapter_start_cols[c_id] = cur_global_col
            c_set = set(c_nodes)
            local_depth: dict[str, int] = {nid: 0 for nid in c_nodes}
            # Relax longest DAG path within chapter (bounded iterations防止cycles)
            for _ in range(len(c_nodes) + 1):
                changed = False
                for u in c_nodes:
                    du = local_depth[u]
                    for v, _ in adj.get(u, ()):
                        if v in c_set and local_depth[v] < du + 1:
                            local_depth[v] = du + 1
                            changed = True
                if not changed:
                    break

            # Bucket by depth; if a depth bucket has > MAX_LANES nodes, spill smoothly to an extra column
            by_depth: dict[int, list[str]] = {}
            for nid in c_nodes:
                by_depth.setdefault(local_depth[nid], []).append(nid)

            for d_val in sorted(by_depth.keys()):
                bucket = by_depth[d_val]
                for chunk_start in range(0, len(bucket), MAX_LANES):
                    sub = bucket[chunk_start : chunk_start + MAX_LANES]
                    # Center-balance lanes nicely when 1..3 nodes are in a column
                    if len(sub) == 1:
                        lane_slots = [2]
                    elif len(sub) == 2:
                        lane_slots = [1, 3]
                    elif len(sub) == 3:
                        lane_slots = [1, 2, 3]
                    elif len(sub) == 4:
                        lane_slots = [0, 1, 3, 4]
                    else:
                        lane_slots = [0, 1, 2, 3, 4]
                    for i, nid in enumerate(sub):
                        coords[nid] = (cur_global_col, lane_slots[i])
                    cur_global_col += 1

        # Final column(s): 5 Ending Nodes stacked cleanly top-to-bottom (TRUE, GOOD, NEUTRAL, BAD I, BAD II)
        chapter_start_cols["END"] = cur_global_col
        end_keys = list(endings_map.keys())
        for chunk_start in range(0, len(end_keys), MAX_LANES):
            sub_e = end_keys[chunk_start : chunk_start + MAX_LANES]
            for i, eid in enumerate(sub_e):
                coords[eid] = (cur_global_col, i)
            cur_global_col += 1

        out_nodes: list[dict[str, Any]] = []
        for idx, (nid, node) in enumerate(nodes_map.items()):
            col, lane = coords[nid]
            t_clean = sanitize_cfont_ascii(node.get("title", nid))
            out_nodes.append(
                {
                    "idx": idx,
                    "id": nid,
                    "chapter_id": str(node.get("chapter_id", "CH1")),
                    "kind": node_kind.get(nid, "scene"),
                    "col": col,
                    "lane": lane,
                    "title": t_clean,
                    "short_title": textwrap.shorten(t_clean, width=22, placeholder=".."),
                    "day_label": sanitize_cfont_ascii(node.get("day_label", "")),
                }
            )
        base_idx = len(out_nodes)
        for e_i, (eid, emeta) in enumerate(endings_map.items()):
            col, lane = coords[eid]
            t_clean = sanitize_cfont_ascii(emeta.get("title", eid))
            out_nodes.append(
                {
                    "idx": base_idx + e_i,
                    "id": eid,
                    "chapter_id": "END",
                    "kind": "ending",
                    "col": col,
                    "lane": lane,
                    "title": t_clean,
                    "short_title": textwrap.shorten(t_clean, width=22, placeholder=".."),
                    "day_label": sanitize_cfont_ascii(emeta.get("rank", eid)),
                }
            )

        out_edges: list[dict[str, Any]] = []
        for src_id, outs in adj.items():
            if src_id not in coords:
                continue
            c1, l1 = coords[src_id]
            for dst_id, ek in outs:
                if dst_id not in coords:
                    continue
                c2, l2 = coords[dst_id]
                out_edges.append(
                    {
                        "src": src_id,
                        "dst": dst_id,
                        "c1": c1,
                        "l1": l1,
                        "c2": c2,
                        "l2": l2,
                        "kind": ek,
                    }
                )

        return {
            "columns": cur_global_col,
            "max_lanes": MAX_LANES,
            "chapter_start_cols": chapter_start_cols,
            "nodes": out_nodes,
            "edges": out_edges,
        }

    # ==========================================================================
    # CORE PLAYBACK, CHECKPOINTS, SUBMODES & TOUCH/HUD CONTRACTS
    # ==========================================================================
    def start_or_continue(
        self,
        char_id: str,
        restart: bool = False,
        engine: Any = None,
        campaign_id: Optional[str] = None,
    ) -> dict[str, Any]:
        cid = (char_id or "").strip().lower()
        camp = self.get_campaign(cid, campaign_id)
        if not camp:
            return {"ok": False, "error": f"No Story Quest campaign pack installed for {cid!r}"}

        camp_id = str(camp["campaign_id"])
        self.selected_campaign_by_char[cid] = camp_id
        self._refresh_primary_campaigns_view()

        if engine is not None:
            ds = getattr(engine, "dating_sim", None)
            if ds is not None:
                ds.active_vn_session = None
                ds.active_house_menu = None
            engine.wl_typing_active = False
            engine.phone_open = 0
            if hasattr(engine, "_update_touch_capture"):
                try:
                    engine._update_touch_capture(bool(getattr(engine, "touch_mode", True)))
                except Exception:
                    pass

        self.submode = "read"
        self.hide_ui = False
        self.choice_cursor = 0
        self.backlog_scroll = 0
        self._last_voiced_beat_token = ""

        saved_row = None
        if not restart:
            with self._db_lock:
                conn = self._connect()
                try:
                    saved_row = conn.execute(
                        "SELECT * FROM story_quest_runs WHERE char_id = ? AND campaign_id = ?",
                        (cid, camp_id),
                    ).fetchone()
                finally:
                    conn.close()

        if saved_row is not None and not restart and str(saved_row["node_id"]) in camp["nodes"]:
            sess = {
                "char_id": cid,
                "campaign_id": camp_id,
                "node_id": str(saved_row["node_id"]),
                "beat_idx": int(saved_row["beat_idx"]),
                "active_opt_id": str(saved_row["active_opt_id"] or ""),
                "bond": int(saved_row["bond"]),
                "insight": int(saved_row["insight"]),
                "flags": json.loads(saved_row["flags_json"] or "[]"),
                "visited_nodes": json.loads(saved_row["visited_nodes_json"] or "[]"),
                "backlog": json.loads(saved_row["backlog_json"] or "[]"),
                "finished": bool(saved_row["finished"]),
                "ending_id": str(saved_row["ending_id"] or ""),
            }
            self.active_session = sess
            cur_beat = self._current_beat_obj(sess, camp)
            if cur_beat:
                self._append_current_beat_to_backlog(sess, cur_beat)
            self._persist_session(sess)
            self._sync_bgm_safe(engine)
            self._maybe_trigger_beat_voice(engine, sess, camp)
            return {"ok": True, "resumed": True, "state": self.get_api_state(cid)}

        init_st = camp["initial_state"]
        entry_node = str(camp["chapters"][0]["entry_node"])
        sess = {
            "char_id": cid,
            "campaign_id": camp_id,
            "node_id": entry_node,
            "beat_idx": 0,
            "active_opt_id": "",
            "bond": int(init_st.get("bond", 0)),
            "insight": int(init_st.get("insight", 0)),
            "flags": list(init_st.get("flags") or []),
            "visited_nodes": [],
            "backlog": [],
            "finished": False,
            "ending_id": "",
        }
        self.active_session = sess
        self._enter_node(sess, camp, entry_node, engine=engine)
        return {"ok": True, "resumed": False, "state": self.get_api_state(cid)}

    def advance_beat(self, engine: Any = None, allow_choice_confirm: bool = False) -> dict[str, Any]:
        sess = self.active_session
        if sess is None:
            return {"ok": False, "error": "No active Story Quest session"}
        if self.hide_ui:
            self.hide_ui = False
            return {"ok": True, "unhid_ui": True}
        if self.submode != "read":
            self.submode = "read"
            return {"ok": True, "closed_submode": True}
        if sess.get("finished"):
            return {"ok": True, "finished": True, "ending_id": sess.get("ending_id")}

        camp = self.get_campaign(sess["char_id"], sess.get("campaign_id"))
        if not camp:
            return {"ok": False, "error": "Campaign missing"}

        nid = str(sess["node_id"])
        node = camp["nodes"][nid]
        st = {"bond": sess["bond"], "insight": sess["insight"], "flags": sess["flags"]}
        act_opt = str(sess.get("active_opt_id") or "")
        beats = self._active_beats_for_node(camp, nid, st, act_opt)
        b_idx = int(sess["beat_idx"])

        if b_idx + 1 < len(beats):
            sess["beat_idx"] = b_idx + 1
            cur_beat = beats[sess["beat_idx"]]
            self._append_current_beat_to_backlog(sess, cur_beat)
            on_final_choice = (not act_opt) and (node.get("choice") is not None) and (sess["beat_idx"] == len(beats) - 1)
            if on_final_choice:
                opts = self._evaluate_choice_options(node, st)
                first_unlk = next((i for i, o in enumerate(opts) if o["unlocked"]), 0)
                self.choice_cursor = first_unlk
            self._persist_session(sess, record_gate_cp=on_final_choice)
            self._maybe_trigger_beat_voice(engine, sess, camp)
            return {"ok": True, "advanced": True, "state": self.get_api_state()}

        if act_opt:
            ch_obj = node.get("choice") or {}
            chosen = next((o for o in (ch_obj.get("options") or []) if str(o.get("opt_id")) == act_opt), None)
            if chosen:
                self._enter_node(sess, camp, str(chosen["next_node"]), engine=engine)
                return {"ok": True, "transitioned": True, "state": self.get_api_state()}

        if node.get("choice") is not None:
            if allow_choice_confirm:
                return self.select_choice(self.choice_cursor, engine=engine)
            return {"ok": True, "awaiting_choice": True, "state": self.get_api_state()}

        if node.get("ending_id"):
            sess["finished"] = True
            sess["ending_id"] = str(node["ending_id"])
            self._persist_session(sess)
            return {"ok": True, "finished": True, "ending_id": sess["ending_id"], "state": self.get_api_state()}

        for rule in node.get("routing") or []:
            if rule.get("default") is True or evaluate_condition(rule.get("when"), st):
                self._enter_node(sess, camp, str(rule["next_node"]), engine=engine)
                return {"ok": True, "routed": True, "state": self.get_api_state()}

        return {"ok": False, "error": f"No valid outgoing route at {nid}"}

    def select_choice(self, opt_index_or_id: int | str, engine: Any = None) -> dict[str, Any]:
        sess = self.active_session
        if sess is None or sess.get("finished"):
            return {"ok": False, "error": "No active choice session"}
        if self.submode != "read":
            return {"ok": False, "error": "Not in read mode"}

        camp = self.get_campaign(sess["char_id"], sess.get("campaign_id"))
        if not camp:
            return {"ok": False, "error": "Campaign missing"}
        nid = str(sess["node_id"])
        node = camp["nodes"][nid]
        if node.get("choice") is None or sess.get("active_opt_id"):
            return {"ok": False, "error": "Current beat is not awaiting a choice"}

        st = {"bond": sess["bond"], "insight": sess["insight"], "flags": sess["flags"]}
        beats = self._active_beats_for_node(camp, nid, st, "")
        if int(sess["beat_idx"]) < len(beats) - 1:
            return {"ok": False, "error": "Not yet at final beat of node"}

        opts = self._evaluate_choice_options(node, st)
        picked: Optional[dict[str, Any]] = None
        if isinstance(opt_index_or_id, int):
            if 0 <= opt_index_or_id < len(opts):
                picked = opts[opt_index_or_id]
                self.choice_cursor = opt_index_or_id
        else:
            s_key = str(opt_index_or_id).strip()
            if s_key.isdigit():
                idx = int(s_key)
                if 0 <= idx < len(opts):
                    picked = opts[idx]
                    self.choice_cursor = idx
            else:
                for idx, o in enumerate(opts):
                    if o["opt_id"] == s_key:
                        picked = o
                        self.choice_cursor = idx
                        break

        if picked is None:
            return {"ok": False, "error": f"Choice {opt_index_or_id!r} out of range"}
        if not picked["unlocked"]:
            if engine is not None and hasattr(engine, "last_toast"):
                engine.last_toast = f"Locked Option: {picked['tag']}"
            return {"ok": False, "locked": True, "reason": picked["tag"]}

        self._persist_session(sess, record_gate_cp=True)

        sess.setdefault("backlog", []).append(
            {
                "beat_id": f"CHOICE:{picked['opt_id']}:{len(sess.get('backlog', []))}",
                "node_id": nid,
                "speaker": "Decision",
                "text": sanitize_cfont_ascii(picked["label"]),
                "inner_thought": "",
                "is_choice": True,
            }
        )
        if len(sess["backlog"]) > 120:
            del sess["backlog"][:-120]

        st_after = apply_effects(st, picked["effects"])
        sess["bond"] = int(st_after["bond"])
        sess["insight"] = int(st_after["insight"])
        sess["flags"] = list(st_after["flags"])

        r_beats = [b for b in (picked.get("reaction_beats") or []) if evaluate_condition(b.get("when"), st_after)]
        if r_beats:
            sess["active_opt_id"] = picked["opt_id"]
            sess["beat_idx"] = 0
            self._append_current_beat_to_backlog(sess, r_beats[0])
            self._persist_session(sess)
            self._maybe_trigger_beat_voice(engine, sess, camp)
            return {"ok": True, "picked": picked["opt_id"], "playing_reaction": True, "state": self.get_api_state()}

        self._enter_node(sess, camp, picked["next_node"], engine=engine)
        return {"ok": True, "picked": picked["opt_id"], "state": self.get_api_state()}

    def list_checkpoints(self, char_id: Optional[str] = None, campaign_id: Optional[str] = None) -> list[dict[str, Any]]:
        sess = self.active_session
        cid = (char_id or (sess["char_id"] if sess else "")).strip().lower()
        if not cid:
            return []
        camp = self.get_campaign(cid, campaign_id or (sess["campaign_id"] if sess and sess["char_id"] == cid else None))
        if not camp:
            return []
        camp_id = str(camp["campaign_id"])
        with self._db_lock:
            conn = self._connect()
            try:
                rows = conn.execute(
                    """
                    SELECT * FROM story_quest_checkpoints
                    WHERE char_id = ? AND campaign_id = ?
                    ORDER BY sort_order ASC, checkpoint_id ASC
                    """,
                    (cid, camp_id),
                ).fetchall()
            finally:
                conn.close()
        out: list[dict[str, Any]] = []
        for r in rows:
            fls = json.loads(r["flags_json"] or "[]")
            out.append(
                {
                    "checkpoint_id": str(r["checkpoint_id"]),
                    "campaign_id": camp_id,
                    "chapter_id": str(r["chapter_id"]),
                    "node_id": str(r["node_id"]),
                    "beat_idx": int(r["beat_idx"]),
                    "label": str(r["label"]),
                    "day_label": str(r["day_label"]),
                    "is_gate": bool(r["is_gate"]),
                    "bond": int(r["bond"]),
                    "insight": int(r["insight"]),
                    "flags": fls,
                }
            )
        return out

    def jump_to_checkpoint(
        self,
        checkpoint_id: str,
        char_id: Optional[str] = None,
        engine: Any = None,
        campaign_id: Optional[str] = None,
    ) -> dict[str, Any]:
        sess_cur = self.active_session
        cid = (char_id or (sess_cur["char_id"] if sess_cur else "")).strip().lower()
        camp = self.get_campaign(
            cid, campaign_id or (sess_cur["campaign_id"] if sess_cur and sess_cur["char_id"] == cid else None)
        )
        if not camp:
            return {"ok": False, "error": f"Unknown campaign {cid!r}"}
        camp_id = str(camp["campaign_id"])
        self.selected_campaign_by_char[cid] = camp_id
        self._refresh_primary_campaigns_view()

        raw_cp = str(checkpoint_id).strip()
        with self._db_lock:
            conn = self._connect()
            try:
                cp = conn.execute(
                    """
                    SELECT * FROM story_quest_checkpoints
                    WHERE char_id = ? AND campaign_id = ? AND (checkpoint_id IN (?, ?, ?) OR node_id = ?)
                    ORDER BY is_gate DESC, sort_order DESC
                    LIMIT 1
                    """,
                    (cid, camp_id, raw_cp, f"GATE:{raw_cp}", f"NODE:{raw_cp}", raw_cp),
                ).fetchone()
                prev_run = conn.execute(
                    "SELECT visited_nodes_json, backlog_json FROM story_quest_runs WHERE char_id = ? AND campaign_id = ?",
                    (cid, camp_id),
                ).fetchone()
            finally:
                conn.close()

        if cp is None:
            return {"ok": False, "error": f"Checkpoint {checkpoint_id!r} not unlocked yet"}

        nid = str(cp["node_id"])
        if nid not in camp["nodes"]:
            return {"ok": False, "error": f"Node {nid!r} missing from campaign"}

        if engine is not None:
            ds = getattr(engine, "dating_sim", None)
            if ds is not None:
                ds.active_vn_session = None
                ds.active_house_menu = None
            engine.wl_typing_active = False
            engine.phone_open = 0
            if hasattr(engine, "_update_touch_capture"):
                try:
                    engine._update_touch_capture(bool(getattr(engine, "touch_mode", True)))
                except Exception:
                    pass

        vis = json.loads(prev_run["visited_nodes_json"] or "[]") if prev_run else []
        if nid not in vis:
            vis.append(nid)
        bkl = json.loads(prev_run["backlog_json"] or "[]") if prev_run else []

        sess = {
            "char_id": cid,
            "campaign_id": camp_id,
            "node_id": nid,
            "beat_idx": int(cp["beat_idx"]),
            "active_opt_id": "",
            "bond": int(cp["bond"]),
            "insight": int(cp["insight"]),
            "flags": json.loads(cp["flags_json"] or "[]"),
            "visited_nodes": vis,
            "backlog": bkl,
            "finished": False,
            "ending_id": "",
        }
        self.active_session = sess
        self.submode = "read"
        self.hide_ui = False
        self.choice_cursor = 0
        self._last_voiced_beat_token = ""

        st = {"bond": sess["bond"], "insight": sess["insight"], "flags": sess["flags"]}
        beats = self._active_beats_for_node(camp, nid, st, "")
        sess["beat_idx"] = max(0, min(int(sess["beat_idx"]), max(0, len(beats) - 1)))
        cur_beat = self._current_beat_obj(sess, camp)
        if cur_beat:
            self._append_current_beat_to_backlog(sess, cur_beat)

        self._persist_session(sess)
        self._sync_bgm_safe(engine)
        self._maybe_trigger_beat_voice(engine, sess, camp)
        return {"ok": True, "jumped_to": checkpoint_id, "state": self.get_api_state(cid)}

    def toggle_backlog(self) -> str:
        if not self.active_session:
            return "read"
        self.hide_ui = False
        if self.submode == "backlog":
            self.submode = "read"
        else:
            self.submode = "backlog"
            self.backlog_scroll = 0
        return self.submode

    def toggle_flowchart(self) -> str:
        if not self.active_session:
            return "read"
        self.hide_ui = False
        if self.submode == "flowchart":
            self.submode = "read"
        else:
            self.submode = "flowchart"
            gr = self.build_causal_graph_2d(self.active_session["char_id"], self.active_session["campaign_id"])
            cur_nid = str(self.active_session["node_id"])
            sel_i = 0
            cur_col = 0
            for n in gr["nodes"]:
                if n["id"] == cur_nid:
                    sel_i = int(n["idx"])
                    cur_col = int(n["col"])
                    break
            self.flowchart_cursor = sel_i
            self.flowchart_col_offset = max(0, min(max(0, gr["columns"] - 4), cur_col - 1))
        return self.submode

    def toggle_saveload(self, mode_hint: str = "save") -> str:
        if not self.active_session:
            return "read"
        self.hide_ui = False
        if self.submode == "saveload" and self.saveload_mode_hint == mode_hint:
            self.submode = "read"
        else:
            self.submode = "saveload"
            self.saveload_mode_hint = mode_hint
            if mode_hint == "load" and self.saveload_slot_cursor == 0:
                self.saveload_slot_cursor = 0
            elif mode_hint == "save" and self.saveload_slot_cursor == 0:
                self.saveload_slot_cursor = 1
        return self.submode

    def toggle_hide_ui(self) -> bool:
        if not self.active_session:
            return False
        if self.submode != "read":
            self.submode = "read"
        self.hide_ui = not self.hide_ui
        return self.hide_ui

    def move_cursor(self, delta: int) -> None:
        sess = self.active_session
        if not sess:
            return
        if self.submode == "backlog":
            bkl = sess.get("backlog") or []
            max_sc = max(0, len(bkl) - 6)
            self.backlog_scroll = max(0, min(max_sc, self.backlog_scroll + (-delta * 2)))
            return
        if self.submode == "saveload":
            self.saveload_slot_cursor = (self.saveload_slot_cursor + delta) % 7
            return
        if self.submode == "flowchart":
            gr = self.build_causal_graph_2d(sess["char_id"], sess["campaign_id"])
            nodes = gr["nodes"]
            if nodes:
                self.flowchart_cursor = (self.flowchart_cursor + delta) % len(nodes)
                sel_col = int(nodes[self.flowchart_cursor]["col"])
                if sel_col < self.flowchart_col_offset:
                    self.flowchart_col_offset = sel_col
                elif sel_col >= self.flowchart_col_offset + 4:
                    self.flowchart_col_offset = max(0, sel_col - 3)
            return
        camp = self.get_campaign(sess["char_id"], sess.get("campaign_id"))
        if not camp:
            return
        node = camp["nodes"].get(sess["node_id"]) or {}
        st = {"bond": sess["bond"], "insight": sess["insight"], "flags": sess["flags"]}
        opts = self._evaluate_choice_options(node, st)
        if opts:
            self.choice_cursor = (self.choice_cursor + delta) % len(opts)

    def confirm_cursor(self, engine: Any = None) -> dict[str, Any]:
        sess = self.active_session
        if not sess:
            return {"ok": False}
        if self.submode == "backlog":
            self.submode = "read"
            return {"ok": True}
        if self.submode == "saveload":
            if self.saveload_mode_hint == "save" and 1 <= self.saveload_slot_cursor <= 6:
                return self.save_to_slot(self.saveload_slot_cursor, engine=engine)
            return self.load_from_slot(self.saveload_slot_cursor, engine=engine)
        if self.submode == "flowchart":
            gr = self.build_causal_graph_2d(sess["char_id"], sess["campaign_id"])
            nodes = gr["nodes"]
            if nodes and 0 <= self.flowchart_cursor < len(nodes):
                sel_n = nodes[self.flowchart_cursor]
                if sel_n.get("can_jump") and sel_n.get("checkpoint_id"):
                    return self.jump_to_checkpoint(sel_n["checkpoint_id"], engine=engine)
            return {"ok": False, "error": "Selected node is not unlocked for Time-Jump"}
        return self.advance_beat(engine=engine, allow_choice_confirm=True)

    def close_and_autosave(self, engine: Any = None) -> dict[str, Any]:
        if self.active_session is not None:
            self._persist_session(self.active_session)
        self.active_session = None
        self.submode = "read"
        self.hide_ui = False
        self._sync_bgm_safe(engine)
        return {"ok": True}

    def export_causal_graph_hud_kv(
        self,
        prefix: str,
        char_id: str,
        campaign_id: Optional[str],
        col_offset: int,
        selected_idx: int,
    ) -> tuple[dict[str, str], int, int]:
        """
        Serializes a 4-column x 5-lane 2D Causal Graph viewport + visible edges into compact HUD keys
        shared by BOTH `Card Hub -> PAGE_STORY_QUEST (Tab 2)` and in-VN `[J] Flowchart`!
        Returns `(kv_dict, clamped_col_offset, clamped_selected_idx)`.
        """
        kv: dict[str, str] = {}
        gr = self.build_causal_graph_2d(char_id, campaign_id)
        if not gr.get("available") or not gr["nodes"]:
            kv[f"{prefix}fc_avail"] = "0"
            return kv, 0, 0

        total_cols = int(gr["columns"])
        max_off = max(0, total_cols - 4)
        c_off = max(0, min(max_off, int(col_offset)))
        nodes = gr["nodes"]
        sel_i = max(0, min(len(nodes) - 1, int(selected_idx)))
        sel_node = nodes[sel_i]

        kv[f"{prefix}fc_avail"] = "1"
        kv[f"{prefix}fc_col_off"] = str(c_off)
        kv[f"{prefix}fc_col_tot"] = str(total_cols)
        kv[f"{prefix}fc_range"] = f"Columns {c_off + 1}-{min(total_cols, c_off + 4)} / {total_cols}"

        # Column headers (which Chapter each of the 4 visible columns belongs to)
        col_ch_map: dict[int, str] = {}
        for n in nodes:
            col_ch_map.setdefault(int(n["col"]), str(n["chapter_id"]))
        for vc in range(4):
            gc = c_off + vc
            kv[f"{prefix}fc_ch{vc + 1}"] = col_ch_map.get(gc, "") if gc < total_cols else ""

        # Visible nodes in [c_off .. c_off + 3] (at most 4 * 5 = 20 nodes)
        vis_nodes = [n for n in nodes if c_off <= int(n["col"]) < c_off + 4]
        kv[f"{prefix}fc_n_cnt"] = str(min(20, len(vis_nodes)))
        for i, vn in enumerate(vis_nodes[:20], start=1):
            vcol = int(vn["col"]) - c_off  # 0..3
            vlane = int(vn["lane"])  # 0..4
            state_flag = "2" if vn["is_current"] else ("1" if vn["unlocked"] else "0")
            is_sel = "1" if int(vn["idx"]) == sel_i else "0"
            # Compact pipe-free pack: vcol,vlane,kind,state,sel,idx
            kv[f"{prefix}fc_n{i}_pos"] = f"{vcol},{vlane},{vn['kind']},{state_flag},{is_sel},{vn['idx']}"
            kv[f"{prefix}fc_n{i}_lbl"] = sanitize_cfont_ascii(vn["display_title"])
            kv[f"{prefix}fc_n{i}_bdg"] = sanitize_cfont_ascii(vn["badge"])

        # Visible edges touching [c_off - 1 .. c_off + 4] clipped cleanly to viewport
        vis_edges = [
            e
            for e in gr["edges"]
            if (c_off <= e["c1"] < c_off + 4 or c_off <= e["c2"] < c_off + 4) and abs(e["c2"] - e["c1"]) <= 5
        ]
        kv[f"{prefix}fc_e_cnt"] = str(min(32, len(vis_edges)))
        for ei, ed in enumerate(vis_edges[:32], start=1):
            vc1 = int(ed["c1"]) - c_off
            vc2 = int(ed["c2"]) - c_off
            vis_flag = "1" if ed["visited"] else "0"
            kv[f"{prefix}fc_e{ei}"] = f"{vc1},{ed['l1']},{vc2},{ed['l2']},{ed['kind']},{vis_flag}"

        # Selected node inspector bar
        kv[f"{prefix}fc_sel_title"] = sanitize_cfont_ascii(
            f"[{sel_node['badge']}] {sel_node.get('full_title') or sel_node['display_title']}"
        )
        kv[f"{prefix}fc_sel_meta"] = sanitize_cfont_ascii(sel_node.get("meta_line", ""))
        kv[f"{prefix}fc_sel_can_jump"] = "1" if sel_node.get("can_jump") else "0"
        return kv, c_off, sel_i

    def export_saveload_hud_kv(
        self, prefix: str, char_id: str, campaign_id: Optional[str], slot_cursor: int
    ) -> tuple[dict[str, str], str]:
        """Serializes the 7 Save/Load slots (`0..6`) into HUD keys and returns `(kv, preview_cg_rel)`."""
        kv: dict[str, str] = {}
        slots = self.list_save_slots(char_id, campaign_id)
        sel = max(0, min(6, int(slot_cursor)))
        kv[f"{prefix}sl_cur"] = str(sel)
        for s in slots:
            si = int(s["slot_idx"])
            kv[f"{prefix}sl{si}_occ"] = "1" if s["occupied"] else "0"
            kv[f"{prefix}sl{si}_lbl"] = sanitize_cfont_ascii(s["slot_label"])
            if s["occupied"]:
                kv[f"{prefix}sl{si}_title"] = sanitize_cfont_ascii(f"[{s['chapter_id']}] {s['scene_title']}")
                kv[f"{prefix}sl{si}_meta"] = sanitize_cfont_ascii(
                    f"Bond {s['bond']}  Insight {s['insight']}  Clues {s['clues_count']}/{s['total_clues']}  -  {s['saved_at']}"
                )
            else:
                kv[f"{prefix}sl{si}_title"] = "[Empty Manual Save Slot]"
                kv[f"{prefix}sl{si}_meta"] = "Click [SAVE TO SLOT] to record exact beat & CG"

        sel_slot = slots[sel]
        kv[f"{prefix}sl_sel_occ"] = "1" if sel_slot["occupied"] else "0"
        kv[f"{prefix}sl_sel_lbl"] = sanitize_cfont_ascii(sel_slot["slot_label"])
        kv[f"{prefix}sl_sel_title"] = sanitize_cfont_ascii(
            f"[{sel_slot['chapter_id']}] {sel_slot['scene_title']}" if sel_slot["occupied"] else "Empty Save Slot"
        )
        kv[f"{prefix}sl_sel_day"] = sanitize_cfont_ascii(sel_slot.get("day_label") or "")
        kv[f"{prefix}sl_sel_stats"] = sanitize_cfont_ascii(
            f"Bond: {sel_slot['bond']}   -   Insight: {sel_slot['insight']}   -   Clues: {sel_slot['clues_count']}/{sel_slot['total_clues']}"
            if sel_slot["occupied"]
            else "No snapshot stored in this slot yet."
        )
        kv[f"{prefix}sl_sel_time"] = sanitize_cfont_ascii(sel_slot.get("saved_at") or "--")
        return kv, str(sel_slot.get("cg_rel") or "")

    def on_touch(self, code: int, arg: int, engine: Any = None) -> dict[str, Any]:
        """Handles DirectX 9 Touchscreen Mouse interactions (`code == 16`) inside `DrawStoryQuestVnHud`."""
        if code != 16 or self.active_session is None:
            return {"ok": False}
        sess = self.active_session
        cid = str(sess["char_id"])
        camp_id = str(sess["campaign_id"])

        if arg == 1:  # Next beat
            return self.advance_beat(engine=engine, allow_choice_confirm=False)
        if arg == 2:  # Toggle Backlog [B]
            self.toggle_backlog()
            return {"ok": True}
        if arg == 3:  # Toggle 2D Causal Flowchart [J]
            self.toggle_flowchart()
            return {"ok": True}
        if arg == 4:  # Toggle Hide UI [H]
            self.toggle_hide_ui()
            return {"ok": True}
        if arg == 5:  # Save & Exit [Backspace]
            return self.close_and_autosave(engine=engine)
        if arg == 6:  # Restart Campaign [R]
            return self.start_or_continue(cid, restart=True, engine=engine, campaign_id=camp_id)
        if arg == 7:  # Scroll Up / Pan Left
            if self.submode == "flowchart":
                self.flowchart_col_offset = max(0, self.flowchart_col_offset - 1)
            else:
                self.move_cursor(-1)
            return {"ok": True}
        if arg == 8:  # Scroll Down / Pan Right
            if self.submode == "flowchart":
                gr = self.build_causal_graph_2d(cid, camp_id)
                self.flowchart_col_offset = min(max(0, gr["columns"] - 4), self.flowchart_col_offset + 1)
            else:
                self.move_cursor(+1)
            return {"ok": True}
        if arg == 9:  # Confirm Flowchart Time-Jump / SaveLoad primary action
            return self.confirm_cursor(engine=engine)
        if arg == 10:  # Close submode modal ([X])
            self.submode = "read"
            return {"ok": True}
        if 11 <= arg <= 13:  # Choice Option 1..3
            return self.select_choice(arg - 11, engine=engine)
        if arg == 14:  # Toggle Save/Load Modal in SAVE mode [S]
            self.toggle_saveload("save")
            return {"ok": True}
        if arg == 15:  # Toggle Save/Load Modal in LOAD mode [L]
            self.toggle_saveload("load")
            return {"ok": True}
        if 30 <= arg <= 36:  # Select Save Slot 0..6
            self.saveload_slot_cursor = arg - 30
            return {"ok": True}
        if arg == 37:  # Explicit [SAVE CURRENT BEAT TO SLOT]
            if 1 <= self.saveload_slot_cursor <= 6:
                return self.save_to_slot(self.saveload_slot_cursor, cid, camp_id, engine=engine)
            return {"ok": False, "error": "Select Manual Slot 1..6 to overwrite"}
        if arg == 38:  # Explicit [LOAD SELECTED SLOT]
            return self.load_from_slot(self.saveload_slot_cursor, cid, camp_id, engine=engine)
        if arg == 39:  # Explicit [DELETE SELECTED SLOT]
            return self.delete_save_slot(self.saveload_slot_cursor, cid, camp_id)
        if 41 <= arg <= 45:  # Quick Chapter Jump Pill 1..5 in 2D Flowchart
            gr = self.build_causal_graph_2d(cid, camp_id)
            ch_key = "END" if arg == 45 and "CH5" not in gr["chapter_start_cols"] else f"CH{arg - 40}"
            if ch_key in gr["chapter_start_cols"]:
                self.flowchart_col_offset = max(
                    0, min(max(0, gr["columns"] - 4), int(gr["chapter_start_cols"][ch_key]))
                )
            return {"ok": True}
        if arg == 46:  # Jump camera to ENDings column
            gr = self.build_causal_graph_2d(cid, camp_id)
            self.flowchart_col_offset = max(0, gr["columns"] - 4)
            return {"ok": True}
        if 100 <= arg <= 260:  # Click 2D Flowchart node by `100 + node_idx`
            n_idx = arg - 100
            gr = self.build_causal_graph_2d(cid, camp_id)
            if 0 <= n_idx < len(gr["nodes"]):
                if self.flowchart_cursor == n_idx and gr["nodes"][n_idx].get("can_jump"):
                    return self.jump_to_checkpoint(gr["nodes"][n_idx]["checkpoint_id"], cid, engine=engine, campaign_id=camp_id)
                self.flowchart_cursor = n_idx
                return {"ok": True}
        return {"ok": False}

    def get_api_state(self, char_id: Optional[str] = None, campaign_id: Optional[str] = None) -> dict[str, Any]:
        sess = self.active_session
        target_cid = (char_id or (sess["char_id"] if sess else "hutao")).strip().lower()
        target_camp_id = campaign_id or (sess["campaign_id"] if sess and sess["char_id"] == target_cid else None)
        status = self.get_char_status(target_cid, target_camp_id)
        if sess is None or sess["char_id"] != target_cid:
            return {
                "active": False,
                "char_status": status,
                "char_campaigns": self.list_char_campaigns_status(target_cid),
                "campaigns": self.list_campaigns_summary(),
                "checkpoints": self.list_checkpoints(target_cid, target_camp_id),
                "save_slots": self.list_save_slots(target_cid, target_camp_id),
            }
        camp = self.get_campaign(target_cid, sess["campaign_id"]) or {}
        nid = str(sess["node_id"])
        node = (camp.get("nodes") or {}).get(nid) or {}
        st = {"bond": sess["bond"], "insight": sess["insight"], "flags": sess["flags"]}
        act_opt = str(sess.get("active_opt_id") or "")
        beats = self._active_beats_for_node(camp, nid, st, act_opt)
        cur_beat = self._current_beat_obj(sess, camp) or {}
        at_choice = (
            (not sess.get("finished"))
            and (not act_opt)
            and (node.get("choice") is not None)
            and (int(sess["beat_idx"]) == len(beats) - 1)
        )
        opts = self._evaluate_choice_options(node, st) if at_choice else []
        end_meta = (camp.get("endings") or {}).get(str(sess.get("ending_id") or "")) if sess.get("finished") else None

        return {
            "active": True,
            "submode": self.submode,
            "hide_ui": self.hide_ui,
            "char_id": target_cid,
            "campaign_id": sess["campaign_id"],
            "title": camp.get("title", ""),
            "poster_cg": camp.get("poster_cg", ""),
            "synopsis": camp.get("synopsis", ""),
            "node_id": nid,
            "chapter_id": node.get("chapter_id", ""),
            "node_title": node.get("title", ""),
            "day_label": node.get("day_label", ""),
            "location": node.get("location", ""),
            "beat_idx": int(sess["beat_idx"]),
            "beat_total": len(beats),
            "beat": cur_beat,
            "bond": int(sess["bond"]),
            "insight": int(sess["insight"]),
            "flags": list(sess["flags"]),
            "awaiting_choice": at_choice,
            "choice_prompt": (node.get("choice") or {}).get("prompt", "") if at_choice else "",
            "options": opts,
            "finished": bool(sess.get("finished")),
            "ending_id": str(sess.get("ending_id") or ""),
            "ending": end_meta,
            "char_status": status,
            "checkpoints": self.list_checkpoints(target_cid, sess["campaign_id"]),
            "save_slots": self.list_save_slots(target_cid, sess["campaign_id"]),
        }

    def build_hud_kv(self, engine: Any = None) -> dict[str, str]:
        """Builds ASCII-clean `sq_*` keys for `EaglePhoneHUD.dat` and drives `wl_active_cg_rel` when active."""
        kv: dict[str, str] = {}
        sel_cid = "hutao"
        if engine is not None and getattr(engine, "dating_sim", None) is not None:
            sel_cid = str(getattr(engine.dating_sim, "selected_char_id", "hutao") or "hutao")
        sel_st = self.get_char_status(sel_cid)
        kv["sq_avail"] = "1" if sel_st.get("available") else "0"
        kv["sq_has_save"] = "1" if sel_st.get("has_save") else "0"
        kv["sq_sel_title"] = sanitize_cfont_ascii(sel_st.get("title") or "Story Quest Coming Soon")
        kv["sq_sel_prog"] = sanitize_cfont_ascii(
            f"Quests: {sel_st.get('quest_count', 1)}  -  {sel_st.get('progress_pct', 0)}%  -  "
            f"Endings {sel_st.get('unlocked_endings_count', 0)}/{sel_st.get('total_endings', 5)}"
            if sel_st.get("available")
            else "Pack Slot Ready"
        )

        sess = self.active_session
        if sess is None:
            kv["sq_active"] = "0"
            return kv

        cid = str(sess["char_id"])
        camp_id = str(sess["campaign_id"])
        camp = self.get_campaign(cid, camp_id)
        if not camp:
            kv["sq_active"] = "0"
            return kv

        acc_r, acc_g, acc_b = DEFAULT_THEME_COLORS.get(cid, (225, 49, 75))
        if isinstance(camp.get("theme_rgb"), (list, tuple)) and len(camp["theme_rgb"]) == 3:
            acc_r, acc_g, acc_b = int(camp["theme_rgb"][0]), int(camp["theme_rgb"][1]), int(camp["theme_rgb"][2])

        nid = str(sess["node_id"])
        node = camp["nodes"].get(nid) or {}
        st = {"bond": sess["bond"], "insight": sess["insight"], "flags": sess["flags"]}
        act_opt = str(sess.get("active_opt_id") or "")
        beats = self._active_beats_for_node(camp, nid, st, act_opt)
        cur_beat = self._current_beat_obj(sess, camp) or {}
        ch_status = self.get_char_status(cid, camp_id)

        kv["sq_active"] = "1"
        kv["sq_char_id"] = cid
        kv["sq_submode"] = self.submode
        kv["sq_hide_ui"] = "1" if self.hide_ui else "0"
        kv["sq_acc_r"] = str(acc_r)
        kv["sq_acc_g"] = str(acc_g)
        kv["sq_acc_b"] = str(acc_b)
        kv["sq_title"] = sanitize_cfont_ascii(camp.get("title", "Story Quest"))

        ch_id = str(node.get("chapter_id", "CH1"))
        day_lbl = sanitize_cfont_ascii(node.get("day_label", ""))
        loc_lbl = sanitize_cfont_ascii(node.get("location", ""))
        kv["sq_ch_badge"] = sanitize_cfont_ascii(f"{ch_id}  -  {day_lbl}  -  {loc_lbl}")
        kv["sq_scene_title"] = sanitize_cfont_ascii(node.get("title", nid))
        kv["sq_bond"] = str(sess["bond"])
        kv["sq_insight"] = str(sess["insight"])

        cat_flags = [f for f in sess["flags"] if f in (camp.get("flag_catalog") or {})]
        kv["sq_flag_cnt"] = f"{len(cat_flags)}/{len(camp.get('flag_catalog') or {})}"
        kv["sq_endings_str"] = f"{ch_status['unlocked_endings_count']}/{ch_status['total_endings']}"
        kv["sq_cgs_str"] = str(ch_status["unlocked_cgs_count"])

        clue_titles = [sanitize_cfont_ascii(camp["flag_catalog"][f]["title"]) for f in cat_flags[-3:]]
        kv["sq_clues_short"] = ", ".join(clue_titles) if clue_titles else "None yet"

        cg_rel = str(cur_beat.get("cg") or "")
        if cg_rel:
            kv["wl_active_cg_rel"] = cg_rel
            kv["sq_cg_rel"] = cg_rel

        speaker = sanitize_cfont_ascii(cur_beat.get("speaker") or "Narrator")
        raw_txt = sanitize_cfont_ascii(cur_beat.get("text") or "")
        thought = sanitize_cfont_ascii(cur_beat.get("inner_thought") or "")
        wrapped = textwrap.wrap(raw_txt, width=120) if raw_txt else [""]
        if len(wrapped) > 4:
            wrapped = wrapped[:3] + [textwrap.shorten(" ".join(wrapped[3:]), width=120, placeholder="...")]
        kv["sq_speaker"] = speaker
        kv["sq_beat_pos"] = f"{min(int(sess['beat_idx']) + 1, max(1, len(beats)))}/{max(1, len(beats))}"
        for li in range(1, 5):
            kv[f"sq_l{li}"] = wrapped[li - 1] if (li - 1) < len(wrapped) else ""
        kv["sq_thought"] = textwrap.shorten(thought, width=140, placeholder="...") if thought else ""

        at_choice = (
            (not sess.get("finished"))
            and (not act_opt)
            and (node.get("choice") is not None)
            and (int(sess["beat_idx"]) == len(beats) - 1)
        )
        kv["sq_has_choice"] = "1" if at_choice else "0"
        if at_choice:
            ch_obj = node["choice"]
            kv["sq_choice_prompt"] = sanitize_cfont_ascii(ch_obj.get("prompt") or "")
            opts = self._evaluate_choice_options(node, st)
            kv["sq_opt_cnt"] = str(min(3, len(opts)))
            kv["sq_opt_cur"] = str(self.choice_cursor % max(1, len(opts)))
            for oi in range(1, 4):
                if (oi - 1) < len(opts):
                    o = opts[oi - 1]
                    o_lines = textwrap.wrap(sanitize_cfont_ascii(o["label"]), width=102) or [""]
                    kv[f"sq_opt{oi}_l1"] = o_lines[0]
                    kv[f"sq_opt{oi}_l2"] = (
                        textwrap.shorten(" ".join(o_lines[1:]), width=102, placeholder="...") if len(o_lines) > 1 else ""
                    )
                    kv[f"sq_opt{oi}_locked"] = "0" if o["unlocked"] else "1"
                    kv[f"sq_opt{oi}_tag"] = sanitize_cfont_ascii(o["tag"])
                else:
                    kv[f"sq_opt{oi}_l1"] = ""
                    kv[f"sq_opt{oi}_l2"] = ""
                    kv[f"sq_opt{oi}_locked"] = "0"
                    kv[f"sq_opt{oi}_tag"] = ""
        else:
            kv["sq_opt_cnt"] = "0"

        if sess.get("finished") and sess.get("ending_id"):
            eid = str(sess["ending_id"])
            emeta = (camp.get("endings") or {}).get(eid) or {}
            kv["sq_finished"] = "1"
            kv["sq_end_rank"] = sanitize_cfont_ascii(emeta.get("rank", eid))
            kv["sq_end_title"] = sanitize_cfont_ascii(emeta.get("title", ""))
            kv["sq_end_tone"] = sanitize_cfont_ascii(emeta.get("tone", "warm"))
            esum = sanitize_cfont_ascii(emeta.get("summary") or "")
            e_lns = textwrap.wrap(esum, width=82) if esum else []
            for eli in range(1, 4):
                kv[f"sq_end_l{eli}"] = e_lns[eli - 1] if (eli - 1) < len(e_lns) else ""
        else:
            kv["sq_finished"] = "0"

        if self.submode == "backlog":
            bkl = list(sess.get("backlog") or [])
            total_b = len(bkl)
            end_i = max(0, total_b - self.backlog_scroll)
            start_i = max(0, end_i - 6)
            vis_b = bkl[start_i:end_i]
            kv["sq_log_cnt"] = str(len(vis_b))
            kv["sq_log_range"] = f"{start_i + 1}-{end_i} of {total_b}" if total_b else "0/0"
            for bi in range(1, 7):
                if (bi - 1) < len(vis_b):
                    item = vis_b[bi - 1]
                    kv[f"sq_log{bi}_spk"] = sanitize_cfont_ascii(item.get("speaker", "Narrator"))
                    lns = textwrap.wrap(sanitize_cfont_ascii(item.get("text", "")), width=86) or [""]
                    kv[f"sq_log{bi}_l1"] = lns[0]
                    kv[f"sq_log{bi}_l2"] = (
                        textwrap.shorten(" ".join(lns[1:]), width=86, placeholder="...") if len(lns) > 1 else ""
                    )
                else:
                    kv[f"sq_log{bi}_spk"] = ""
                    kv[f"sq_log{bi}_l1"] = ""
                    kv[f"sq_log{bi}_l2"] = ""

        elif self.submode == "flowchart":
            fc_kv, self.flowchart_col_offset, self.flowchart_cursor = self.export_causal_graph_hud_kv(
                "sq_", cid, camp_id, self.flowchart_col_offset, self.flowchart_cursor
            )
            kv.update(fc_kv)

        elif self.submode == "saveload":
            kv["sq_sl_mode"] = self.saveload_mode_hint
            sl_kv, sl_cg = self.export_saveload_hud_kv("sq_", cid, camp_id, self.saveload_slot_cursor)
            kv.update(sl_kv)
            if sl_cg:
                kv["wl_active_cg_rel"] = sl_cg

        return {k: sanitize_cfont_ascii(v) for k, v in kv.items()}
