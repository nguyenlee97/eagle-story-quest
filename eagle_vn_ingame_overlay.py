"""
eagle_vn_ingame_overlay.py — Native Topmost 16:9 High-Res CG Visual Novel & House Visit Overlay
for Project Eagle (gta sa gameplay-lab).

Automatically pops up over the game window whenever a Girlfriend House Visit Menu (`active_house_menu`)
or 4-Scene Visual Novel Scenario (`active_vn_session`) is active, rendering the actual 16:9
Couple & Genshin Cameo CG `.jpg` files, 5-Stage Relationship HUD, 4-Scene Filmstrip, Spoken Dialogue,
3 Pre-Generated Choices, and Custom Free-Text Input Box, and auto-hides itself 4.5s after Scene 4/4 ends
or immediately when pressing Backspace / walking away from the doorstep / pausing / Alt-Tabbing.
"""

from __future__ import annotations

import ctypes
import ctypes.wintypes as wt
import os
import threading
import time
from pathlib import Path
from typing import Any


HWND_TOPMOST = -1
SWP_NOSIZE = 0x0001
SWP_NOMOVE = 0x0002
SWP_NOACTIVATE = 0x0010
SWP_SHOWWINDOW = 0x0040


class _POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


class _RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]


def _find_process_main_hwnd(target_pid: int) -> int:
    if not target_pid:
        return 0
    u32 = ctypes.windll.user32
    found = [0]

    @ctypes.WINFUNCTYPE(wt.BOOL, wt.HWND, wt.LPARAM)
    def _enum_cb(hwnd, _lparam):
        if not u32.IsWindowVisible(hwnd):
            return True
        pid = wt.DWORD(0)
        u32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        if pid.value == target_pid:
            rc = _RECT()
            if u32.GetClientRect(hwnd, ctypes.byref(rc)) and (rc.right - rc.left) >= 320:
                found[0] = int(hwnd)
                return False
        return True

    try:
        u32.EnumWindows(_enum_cb, 0)
    except Exception:
        pass
    return found[0]


class WaifuLinkIngameOverlay:
    def __init__(self, engine_getter):
        self.engine_getter = engine_getter
        self.thread: threading.Thread | None = None
        self.running = False
        self._last_sig = "HIDDEN"
        self._photo_ref = None
        self._gta_hwnd_cache = 0
        self._gta_pid_cache = 0

    def start(self):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self._ui_loop, name="WaifuLinkIngameOverlay", daemon=True)
        self.thread.start()

    def _get_gta_hwnd(self, gta_pid: int) -> int:
        if not gta_pid:
            return 0
        u32 = ctypes.windll.user32
        if self._gta_pid_cache == gta_pid and self._gta_hwnd_cache and u32.IsWindow(self._gta_hwnd_cache):
            return self._gta_hwnd_cache
        hwnd = _find_process_main_hwnd(gta_pid)
        if hwnd:
            self._gta_pid_cache = gta_pid
            self._gta_hwnd_cache = hwnd
        return hwnd

    def _ui_loop(self):
        try:
            import tkinter as tk
            from PIL import Image, ImageTk
        except Exception:
            return

        try:
            root = tk.Tk()
        except Exception:
            return

        u32 = ctypes.windll.user32
        self_pid = os.getpid()

        root.title("WaifuLink v4.0 — In-Game Visual Novel Overlay")
        root.overrideredirect(True)
        root.attributes("-topmost", True)
        root.configure(bg="#090714")
        root.withdraw()

        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        win_w = min(980, max(760, int(sw * 0.62)))
        win_h = min(650, max(540, int(sh * 0.72)))
        win_x = (sw - win_w) // 2
        win_y = max(18, (sh - win_h) // 2)
        root.geometry(f"{win_w}x{win_h}+{win_x}+{win_y}")

        def set_typing_mode(active: bool):
            eng = self.engine_getter()
            if eng is not None:
                eng.vn_overlay_typing = bool(active)

        def return_focus_to_gta():
            set_typing_mode(False)
            eng = self.engine_getter()
            if eng is not None and getattr(eng, "bridge", None) is not None and eng.bridge.pid:
                ghwnd = self._get_gta_hwnd(int(eng.bridge.pid))
                if ghwnd:
                    try:
                        u32.SetForegroundWindow(ghwnd)
                    except Exception:
                        pass

        def show_overlay_noactivate(eng: Any):
            wx, wy = win_x, win_y
            if eng is not None and getattr(eng, "bridge", None) is not None and eng.bridge.pid:
                ghwnd = self._get_gta_hwnd(int(eng.bridge.pid))
                if ghwnd and not u32.IsIconic(ghwnd):
                    rc = _RECT()
                    pt = _POINT(0, 0)
                    if u32.GetClientRect(ghwnd, ctypes.byref(rc)) and u32.ClientToScreen(ghwnd, ctypes.byref(pt)):
                        cw = max(1, rc.right - rc.left)
                        ch = max(1, rc.bottom - rc.top)
                        wx = pt.x + (cw - win_w) // 2
                        wy = pt.y + max(10, (ch - win_h) // 2)
            was_withdrawn = (root.state() == "withdrawn")
            if was_withdrawn:
                fg_before = u32.GetForegroundWindow()
                root.geometry(f"{win_w}x{win_h}+{wx}+{wy}")
                root.deiconify()
                root.update_idletasks()
                try:
                    ov_hwnd = int(root.winfo_id())
                    top_ov = u32.GetParent(ov_hwnd) or ov_hwnd
                    u32.SetWindowPos(
                        top_ov,
                        HWND_TOPMOST,
                        wx,
                        wy,
                        win_w,
                        win_h,
                        SWP_NOACTIVATE | SWP_SHOWWINDOW,
                    )
                except Exception:
                    pass
                if fg_before and not getattr(eng, "vn_overlay_typing", False):
                    try:
                        u32.SetForegroundWindow(fg_before)
                    except Exception:
                        pass
            else:
                try:
                    ov_hwnd = int(root.winfo_id())
                    top_ov = u32.GetParent(ov_hwnd) or ov_hwnd
                    u32.SetWindowPos(
                        top_ov,
                        HWND_TOPMOST,
                        wx,
                        wy,
                        win_w,
                        win_h,
                        SWP_NOACTIVATE | SWP_SHOWWINDOW,
                    )
                except Exception:
                    pass

        def hide_overlay():
            set_typing_mode(False)
            if self._last_sig != "HIDDEN":
                self._last_sig = "HIDDEN"
                root.withdraw()
                return_focus_to_gta()

        # Outer border frame
        outer = tk.Frame(root, bg="#e11d48", bd=0, highlightthickness=2, highlightbackground="#f43f5e")
        outer.pack(fill="both", expand=True)

        inner = tk.Frame(outer, bg="#0b0918", padx=12, pady=8)
        inner.pack(fill="both", expand=True)

        # 1. Top Relationship & 3-Pillar Progress Bar
        top_bar = tk.Frame(inner, bg="#161129", padx=10, pady=6)
        top_bar.pack(fill="x", pady=(0, 6))

        lbl_rel_title = tk.Label(
            top_bar,
            text="HU TAO • STAGE 1/5 • 80/1000 AFFECTION",
            fg="#fde047",
            bg="#161129",
            font=("Segoe UI", 11, "bold"),
            anchor="w",
        )
        lbl_rel_title.pack(fill="x")

        lbl_rel_pillars = tk.Label(
            top_bar,
            text="Chat: 0/45 | Outing: 0/75 | Stage Gate: 0/3 | Milestone CGs: 1/15",
            fg="#a7f3d0",
            bg="#161129",
            font=("Segoe UI", 9, "bold"),
            anchor="w",
        )
        lbl_rel_pillars.pack(fill="x")

        # 2. 4-Scene Filmstrip Header
        strip_bar = tk.Frame(inner, bg="#0b0918")
        strip_bar.pack(fill="x", pady=(0, 6))
        scene_pills = []
        for idx in range(4):
            lbl_s = tk.Label(
                strip_bar,
                text=f"Scene {idx+1}/4",
                fg="#ffffff",
                bg="#1e293b",
                font=("Segoe UI", 8, "bold"),
                padx=8,
                pady=3,
            )
            lbl_s.pack(side="left", expand=True, fill="x", padx=2)
            scene_pills.append(lbl_s)

        # 3. 16:9 High-Res Couple / Cameo CG Canvas
        cg_h = max(230, int(win_h * 0.42))
        cg_w = int(cg_h * 16 / 9)
        cg_container = tk.Frame(inner, bg="#05040c", height=cg_h)
        cg_container.pack(fill="x", pady=(0, 6))
        cg_label = tk.Label(cg_container, bg="#05040c", text="", fg="#f472b6", font=("Segoe UI", 10, "bold"))
        cg_label.pack(anchor="center")

        # 4. Scenario Title + Cameo Cast + Thought Box
        dlg_frame = tk.Frame(inner, bg="#130f24", padx=12, pady=8)
        dlg_frame.pack(fill="both", expand=True)

        hdr_row = tk.Frame(dlg_frame, bg="#130f24")
        hdr_row.pack(fill="x")
        lbl_sc_title = tk.Label(
            hdr_row,
            text="",
            fg="#fef08a",
            bg="#130f24",
            font=("Segoe UI", 10, "bold"),
            anchor="w",
        )
        lbl_sc_title.pack(side="left")
        lbl_cameo_badge = tk.Label(
            hdr_row,
            text="",
            fg="#f472b6",
            bg="#2d122b",
            font=("Segoe UI", 9, "bold"),
            padx=8,
            pady=2,
        )
        lbl_cameo_badge.pack(side="right")

        lbl_narration = tk.Label(
            dlg_frame,
            text="",
            fg="#cbd5e1",
            bg="#130f24",
            font=("Segoe UI", 9, "italic"),
            wraplength=win_w - 56,
            justify="left",
            anchor="w",
        )
        lbl_narration.pack(fill="x", pady=(3, 2))

        lbl_thought = tk.Label(
            dlg_frame,
            text="",
            fg="#f9a8d4",
            bg="#1f1333",
            font=("Segoe UI", 9),
            wraplength=win_w - 56,
            justify="left",
            anchor="w",
            padx=6,
            pady=3,
        )
        lbl_thought.pack(fill="x", pady=(0, 4))

        lbl_spoken = tk.Label(
            dlg_frame,
            text="",
            fg="#ffffff",
            bg="#130f24",
            font=("Segoe UI", 10, "bold"),
            wraplength=win_w - 56,
            justify="left",
            anchor="w",
        )
        lbl_spoken.pack(fill="x", pady=(0, 6))

        # 5. Interactive Choice Buttons (Supports up to 5 options for House Menu or 3 for VN)
        btns_frame = tk.Frame(dlg_frame, bg="#130f24")
        btns_frame.pack(fill="x")
        option_btns: list[tk.Button] = []

        def on_option_click(idx: int):
            eng = self.engine_getter()
            if not eng:
                return
            with eng.lock:
                if eng.dating_sim.active_vn_session is not None:
                    vn = eng.dating_sim.active_vn_session
                    if vn.get("finished"):
                        eng.dating_sim.close_vn_scenario()
                    else:
                        cnode = vn.get("current_node") or {}
                        choices = cnode.get("choices") or []
                        if 0 <= idx < len(choices):
                            eng.dating_sim.vn_cursor_idx = idx
                            eng.dating_sim.choose_vn_option(eng, choice_id=str(choices[idx]["id"]))
                elif eng.dating_sim.active_house_menu is not None:
                    eng.dating_sim.select_house_visit_option(eng, idx)
                eng._write_hud_dat(force=True)
            return_focus_to_gta()

        for b_idx in range(6):
            btn = tk.Button(
                btns_frame,
                text="",
                fg="#fef08a",
                bg="#27173a",
                activebackground="#be185d",
                activeforeground="#ffffff",
                font=("Segoe UI", 9, "bold"),
                anchor="w",
                padx=10,
                pady=3,
                relief="flat",
                cursor="hand2",
                command=lambda i=b_idx: on_option_click(i),
            )
            option_btns.append(btn)

        # 6. Custom Free-Text Input Row + Close Button
        input_row = tk.Frame(dlg_frame, bg="#130f24")
        input_row.pack(fill="x", pady=(6, 0))

        entry_var = tk.StringVar()
        entry_box = tk.Entry(
            input_row,
            textvariable=entry_var,
            bg="#090714",
            fg="#f8fafc",
            insertbackground="#f43f5e",
            font=("Segoe UI", 9),
            relief="flat",
        )
        entry_box.pack(side="left", fill="x", expand=True, ipady=4, padx=(0, 6))

        def on_entry_click(_event=None):
            set_typing_mode(True)
            try:
                ov_hwnd = int(root.winfo_id())
                top_ov = u32.GetParent(ov_hwnd) or ov_hwnd
                u32.SetForegroundWindow(top_ov)
                entry_box.focus_force()
            except Exception:
                pass

        entry_box.bind("<Button-1>", on_entry_click)
        entry_box.bind("<FocusIn>", lambda _e: set_typing_mode(True))
        entry_box.bind("<FocusOut>", lambda _e: set_typing_mode(False))
        entry_box.bind("<Escape>", lambda _e: (root.focus_set(), return_focus_to_gta()))

        def on_send_free_text(*_args):
            txt = entry_var.get().strip()
            if not txt:
                return
            entry_var.set("")
            eng = self.engine_getter()
            if not eng:
                return
            with eng.lock:
                if eng.dating_sim.active_vn_session is not None and not eng.dating_sim.active_vn_session.get("finished"):
                    eng.dating_sim.choose_vn_option(eng, choice_id="", free_text=txt)
                    eng._write_hud_dat(force=True)
            root.focus_set()
            return_focus_to_gta()

        entry_box.bind("<Return>", on_send_free_text)

        btn_send = tk.Button(
            input_row,
            text="💬 Send Custom Reply",
            fg="#ffffff",
            bg="#be185d",
            font=("Segoe UI", 9, "bold"),
            padx=10,
            pady=2,
            relief="flat",
            cursor="hand2",
            command=on_send_free_text,
        )
        btn_send.pack(side="left", padx=(0, 6))

        def on_close_overlay(*_args):
            eng = self.engine_getter()
            if not eng:
                return
            with eng.lock:
                if eng.dating_sim.active_vn_session is not None:
                    eng.dating_sim.close_vn_scenario()
                if eng.dating_sim.active_house_menu is not None:
                    eng.dating_sim.close_house_visit_menu()
                eng._write_hud_dat(force=True)
            hide_overlay()

        btn_close = tk.Button(
            input_row,
            text="✖ Close [Backspace]",
            fg="#fca5a5",
            bg="#311024",
            font=("Segoe UI", 9, "bold"),
            padx=10,
            pady=2,
            relief="flat",
            cursor="hand2",
            command=on_close_overlay,
        )
        btn_close.pack(side="right")

        def on_root_backspace(event):
            if event.widget is entry_box:
                return
            on_close_overlay()

        root.bind("<BackSpace>", on_root_backspace)
        root.bind("<Escape>", lambda e: on_close_overlay() if e.widget is not entry_box else None)

        def load_cg_image(media_dir: Path, filename: str):
            if not filename:
                return None
            img_path = media_dir / filename
            if not img_path.exists():
                return None
            try:
                im = Image.open(img_path).convert("RGB")
                im = im.resize((cg_w, cg_h), Image.Resampling.LANCZOS)
                return ImageTk.PhotoImage(im)
            except Exception:
                return None

        def should_show_over_game(eng: Any) -> bool:
            # Native DirectX9 rendering in hud.lua handles 100% of 16:9 Couple CGs, 4-Scene Filmstrip,
            # House Visit Menu, and [F6] Custom Text Input without stealing D3D9 Exclusive Fullscreen focus!
            # Only show external Tk overlay if explicitly opted-in AND D3D9 is in Windowed mode (0x00C9C060 != 0).
            if os.environ.get("WAIFULINK_TK_OVERLAY", "0") != "1":
                return False
            br = getattr(eng, "bridge", None)
            if br is None or not br.pid or not br.handle:
                return False
            d3d_windowed = br.read_u32(0x00C9C060)
            if not d3d_windowed:
                return False
            menu_act = br.read_u8(0x00BA67A4)
            if menu_act is not None and menu_act != 0:
                return False
            ghwnd = self._get_gta_hwnd(int(br.pid))
            if ghwnd and u32.IsIconic(ghwnd):
                return False
            fg_hwnd = u32.GetForegroundWindow()
            if fg_hwnd:
                fg_pid = wt.DWORD(0)
                u32.GetWindowThreadProcessId(fg_hwnd, ctypes.byref(fg_pid))
                if fg_pid.value and fg_pid.value not in (int(br.pid), self_pid):
                    return False
            return True

        def poll_state():
            if not self.running:
                return
            eng = self.engine_getter()
            if eng is not None:
                ds = eng.dating_sim
                vn = ds.active_vn_session
                hm = ds.active_house_menu
                if (vn is None and hm is None) or not should_show_over_game(eng):
                    hide_overlay()
                else:
                    proj = ds.build_projection(eng)
                    sel = proj["selected"]
                    st_num = int(sel["stage"])
                    hearts = "❤️" * st_num + "🤍" * (5 - st_num)
                    lbl_rel_title.config(
                        text=f"{sel['name']}  •  {hearts}  STAGE {st_num}/5: {sel['stage_title'].upper()}  ({sel['affection']}/1000 Affection)"
                    )
                    lbl_rel_pillars.config(
                        text=(
                            f"Chat Cap: {sel['stage_chat_pts']}/{sel['stage_chat_cap']}  |  "
                            f"Outing Cap: {sel['stage_freeroam_pts']}/{sel['stage_freeroam_cap']}  |  "
                            f"Stage Gate: {sel['stage_scenarios_passed']}/{sel['stage_scenarios_req']}  |  "
                            f"Milestone CGs: {len(sel.get('sent_milestones', []))}/15"
                        )
                    )

                    if vn is not None:
                        cnode = vn.get("current_node") or {}
                        scene_num = int(vn.get("scene_num", 1))
                        cg_seq = vn.get("cg_sequence") or []
                        finished = bool(vn.get("finished"))
                        rem_s = max(0.0, float(vn.get("auto_close_at", 0.0)) - time.time()) if finished else 0.0
                        active_cg_url = (
                            vn.get("ending_cg_url") or (cg_seq[-1].get("url", "") if cg_seq else "")
                            if finished
                            else (cg_seq[scene_num - 1].get("url", "") if 0 < scene_num <= len(cg_seq) else "")
                        )
                        active_cg_file = Path(str(active_cg_url)).name if active_cg_url else ""
                        reask_cnt = int(vn.get("node_retry_count", 0))
                        vn_cur = int(getattr(ds, "vn_cursor_idx", 0))
                        sig = f"VN|{vn.get('scenario_id')}|{scene_num}|{finished}|{int(rem_s*2)}|{reask_cnt}|{vn_cur}"
                        if sig != self._last_sig:
                            self._last_sig = sig
                            show_overlay_noactivate(eng)
                            for s_i in range(4):
                                s_lbl = cg_seq[s_i]["label"] if s_i < len(cg_seq) else f"Scene {s_i+1}/4"
                                is_cur = (s_i + 1 == scene_num) and not finished
                                is_done = (s_i + 1 < scene_num) or finished
                                scene_pills[s_i].config(
                                    text=s_lbl[:28],
                                    bg="#e11d48" if is_cur else ("#059669" if is_done else "#1e293b"),
                                )
                            photo = load_cg_image(ds.media_dir, active_cg_file)
                            if photo is not None:
                                self._photo_ref = photo
                                cg_label.config(image=photo, text="")
                            else:
                                cg_label.config(image="", text=f"[16:9 Couple/Cameo CG: {active_cg_file}]")

                            cameo_cast = vn.get("cameo_cast") or []
                            vn_short = vn.get("short_name", sel["short_name"])
                            lbl_sc_title.config(
                                text=f"🎬 {vn.get('title')}  •  📍 {vn.get('location')}  •  Score: {vn.get('total_score')}/45"
                            )
                            lbl_cameo_badge.config(
                                text=f"✨ Cameo: {', '.join(cameo_cast)}" if cameo_cast else f"💑 Couple CG: Aether + {vn_short}"
                            )

                            for b in option_btns:
                                b.pack_forget()

                            if finished:
                                last_r = vn.get("last_reaction") or {}
                                status_txt = "🎉 SCENARIO PASSED!" if vn.get("passed") else "🔄 RETRY AVAILABLE"
                                lbl_narration.config(
                                    text=f"{status_txt} (+{vn.get('effective_affection_gain', 0)} Affection){vn.get('cap_note', '')}"
                                )
                                lbl_thought.config(text=f"💭 {last_r.get('reaction_thought', '')}")
                                lbl_spoken.config(text=f"🗣️ {vn_short}: \"{last_r.get('reaction_reply', '')}\"")
                                option_btns[0].config(
                                    text=f"✅ [F9 / Enter / Click] Return to GTA SA Now (Auto-closing overlay in {rem_s:.1f}s...)",
                                    bg="#065f46",
                                )
                                option_btns[0].pack(fill="x", pady=2)
                            else:
                                last_r = vn.get("last_reaction") or {}
                                if reask_cnt > 0 and last_r.get("off_topic_action") == "REASK_CURRENT_NODE":
                                    lbl_narration.config(
                                        text=f"⚠️ [Off-Topic Re-Ask {reask_cnt}/1] {last_r.get('reaction_reply', '')}"
                                    )
                                else:
                                    lbl_narration.config(text=cnode.get("narration", ""))
                                lbl_thought.config(text=f"💭 {cnode.get('inner_thought', '')}")
                                lbl_spoken.config(text=f"🗣️ {vn_short}: \"{cnode.get('speaker_line', '')}\"")
                                choices = cnode.get("choices") or []
                                for c_i, ch in enumerate(choices[:3]):
                                    is_sel = (c_i == (vn_cur % max(1, len(choices[:3]))))
                                    option_btns[c_i].config(
                                        text=f"[{c_i+1}] {ch['label']} — \"{ch.get('player_text', '')[:86]}\"",
                                        bg="#be185d" if is_sel else "#27173a",
                                    )
                                    option_btns[c_i].pack(fill="x", pady=2)

                    elif hm is not None:
                        opts = hm.get("options") or []
                        cur_idx = int(hm.get("cursor_idx", 0))
                        hm_short = hm.get("short_name", sel["short_name"])
                        sig = f"HM|{hm.get('char_id')}|{cur_idx}|{len(opts)}"
                        if sig != self._last_sig:
                            self._last_sig = sig
                            show_overlay_noactivate(eng)
                            for s_i in range(4):
                                scene_pills[s_i].config(text=f"Scene {s_i+1}/4 Ready", bg="#1e293b")
                            preview_file = f"{hm.get('char_id', 'hutao')}_s{st_num}_sc1_cg1.jpg"
                            photo = load_cg_image(ds.media_dir, preview_file)
                            if photo is not None:
                                self._photo_ref = photo
                                cg_label.config(image=photo, text="")
                            lbl_sc_title.config(text=f"🏠 HOUSE VISIT EVENT TRIGGER: {hm.get('char_name')} ({hm.get('home_label')})")
                            lbl_cameo_badge.config(text="Press [1-5] or [I/K + F9] to Start")
                            lbl_narration.config(
                                text="Select a Core Couple VN Scenario, an Extra Genshin Cameo VN Scenario, Carryover VN, or Free-Roam Outing:"
                            )
                            lbl_thought.config(
                                text=f"💭 {hm_short} smiles warmly at {hm.get('home_label')}, waiting for Aether's choice."
                            )
                            lbl_spoken.config(
                                text=f"🗣️ {hm_short}: \"Aether! You made it to my doorstep~ What kind of adventure are we starting today?\""
                            )
                            for b in option_btns:
                                b.pack_forget()
                            for o_i, opt in enumerate(opts[:6]):
                                is_sel = (o_i == cur_idx)
                                option_btns[o_i].config(
                                    text=f"[{o_i+1}] {opt.get('label', '')}",
                                    bg="#be185d" if is_sel else "#27173a",
                                )
                                option_btns[o_i].pack(fill="x", pady=2)

            root.after(100, poll_state)

        root.after(120, poll_state)
        try:
            root.mainloop()
        except Exception:
            pass
