import streamlit as st
from pathlib import Path
import os
import time

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FileForge",
    page_icon="🗂️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;500;700;800&display=swap');

/* ── Root Variables ── */
:root {
    --bg:        #0d0f14;
    --surface:   #13161e;
    --border:    #1f2433;
    --accent1:   #4fffb0;
    --accent2:   #ff4f8b;
    --accent3:   #4fbfff;
    --text:      #e8eaf0;
    --muted:     #6b7280;
    --danger:    #ff4f4f;
}

/* ── Global Reset ── */
html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}
.stApp { background-color: var(--bg) !important; }

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 1.5rem 4rem !important; max-width: 780px !important; }

/* ── Hero Header ── */
.hero {
    text-align: center;
    padding: 3.5rem 1rem 2.5rem;
    position: relative;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 70% 60% at 50% 0%, rgba(79,255,176,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.hero-badge {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent1);
    border: 1px solid rgba(79,255,176,0.3);
    padding: 0.25rem 0.75rem;
    border-radius: 2px;
    margin-bottom: 1.2rem;
}
.hero-title {
    font-size: clamp(2.8rem, 8vw, 4.5rem);
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1;
    background: linear-gradient(135deg, #e8eaf0 30%, var(--accent1) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.6rem;
}
.hero-sub {
    font-family: 'Space Mono', monospace;
    font-size: 0.8rem;
    color: var(--muted);
    letter-spacing: 0.05em;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 0 !important;
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 6px !important;
    padding: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    color: var(--muted) !important;
    padding: 0.55rem 1.2rem !important;
    border-radius: 4px !important;
    border: none !important;
    background: transparent !important;
    transition: all 0.2s !important;
}
.stTabs [aria-selected="true"] {
    color: var(--bg) !important;
    background: var(--accent1) !important;
    font-weight: 700 !important;
}
.stTabs [data-baseweb="tab-panel"] {
    padding-top: 1.8rem !important;
}

/* ── Cards ── */
.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1.8rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
}
.card-create::before  { background: linear-gradient(90deg, var(--accent1), transparent); }
.card-read::before    { background: linear-gradient(90deg, var(--accent3), transparent); }
.card-update::before  { background: linear-gradient(90deg, #a78bfa, transparent); }
.card-delete::before  { background: linear-gradient(90deg, var(--danger), transparent); }

.card-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 1rem;
}

/* ── Inputs ── */
.stTextInput input, .stTextArea textarea {
    background: #0d0f14 !important;
    border: 1px solid var(--border) !important;
    border-radius: 6px !important;
    color: var(--text) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.82rem !important;
    transition: border-color 0.2s !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: var(--accent1) !important;
    box-shadow: 0 0 0 2px rgba(79,255,176,0.1) !important;
}
.stTextInput label, .stTextArea label {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.7rem !important;
    letter-spacing: 0.08em !important;
    color: var(--muted) !important;
    text-transform: uppercase !important;
}

/* ── Buttons ── */
.stButton > button {
    font-family: 'Space Mono', monospace !important;
    font-size: 0.72rem !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    font-weight: 700 !important;
    border-radius: 6px !important;
    padding: 0.6rem 1.5rem !important;
    transition: all 0.2s !important;
    border: none !important;
    width: 100% !important;
}
.btn-create .stButton > button { background: var(--accent1) !important; color: #0d0f14 !important; }
.btn-read   .stButton > button { background: var(--accent3) !important; color: #0d0f14 !important; }
.btn-update .stButton > button { background: #a78bfa !important;         color: #0d0f14 !important; }
.btn-delete .stButton > button { background: var(--danger) !important;   color: #fff !important; }

.stButton > button:hover { transform: translateY(-1px); box-shadow: 0 6px 20px rgba(0,0,0,0.4) !important; }
.stButton > button:active { transform: translateY(0); }

/* ── Radio / Select ── */
.stRadio > div { gap: 0.5rem !important; }
.stRadio label { color: var(--text) !important; font-size: 0.85rem !important; }
.stSelectbox [data-baseweb="select"] > div {
    background: #0d0f14 !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.8rem !important;
}

/* ── Alerts ── */
.stSuccess, .stError, .stInfo, .stWarning {
    border-radius: 6px !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 0.78rem !important;
}

/* ── File content box ── */
.file-content-box {
    background: #0a0c10;
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent3);
    border-radius: 6px;
    padding: 1.2rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.78rem;
    line-height: 1.7;
    white-space: pre-wrap;
    color: #c8d0e0;
    max-height: 320px;
    overflow-y: auto;
    margin-top: 1rem;
}

/* ── Stats bar ── */
.stats-row {
    display: flex;
    gap: 1rem;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
}
.stat-chip {
    flex: 1;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
}
.stat-value {
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--accent1);
    display: block;
    line-height: 1;
    margin-bottom: 0.3rem;
}
.stat-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--muted);
}

/* ── File list ── */
.file-list-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.65rem 0.9rem;
    background: #0a0c10;
    border: 1px solid var(--border);
    border-radius: 6px;
    margin-bottom: 0.4rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    color: var(--muted);
}
.file-list-item .fname { color: var(--text); flex: 1; }
.file-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--accent1); flex-shrink: 0; }

/* ── Divider ── */
hr { border-color: var(--border) !important; margin: 1.5rem 0 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }
</style>
""", unsafe_allow_html=True)

# ─── Helpers ──────────────────────────────────────────────────────────────────
WORK_DIR = Path("fileforge_files")
WORK_DIR.mkdir(exist_ok=True)

def safe_path(name: str) -> Path:
    """Resolve path safely inside WORK_DIR."""
    p = (WORK_DIR / name).resolve()
    if not str(p).startswith(str(WORK_DIR.resolve())):
        raise ValueError("Path traversal not allowed.")
    return p

def list_files():
    return sorted([f for f in WORK_DIR.iterdir() if f.is_file()])

def human_size(path: Path) -> str:
    b = path.stat().st_size
    for unit in ["B","KB","MB"]:
        if b < 1024: return f"{b:.0f} {unit}"
        b /= 1024
    return f"{b:.1f} GB"

# ─── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">✦ File Management System</div>
  <div class="hero-title">FileForge</div>
  <div class="hero-sub">create · read · update · delete — done right</div>
</div>
""", unsafe_allow_html=True)

# ─── Stats Bar ────────────────────────────────────────────────────────────────
all_files = list_files()
total_size = sum(f.stat().st_size for f in all_files)
total_kb = f"{total_size/1024:.1f}" if total_size >= 1024 else f"{total_size}"
size_unit = "KB" if total_size >= 1024 else "B"

st.markdown(f"""
<div class="stats-row">
  <div class="stat-chip">
    <span class="stat-value">{len(all_files)}</span>
    <span class="stat-label">Files</span>
  </div>
  <div class="stat-chip">
    <span class="stat-value">{total_kb}</span>
    <span class="stat-label">Total {size_unit}</span>
  </div>
  <div class="stat-chip">
    <span class="stat-value">4</span>
    <span class="stat-label">Operations</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Tabs ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs(["✦ Create", "◈ Read", "◉ Update", "✕ Delete", "⊞ Files"])

# ══════════════════════════════════════════════════════════
# TAB 1 — CREATE
# ══════════════════════════════════════════════════════════
with tab1:
    st.markdown('<div class="card card-create">', unsafe_allow_html=True)
    st.markdown('<div class="card-label">01 — Create New File</div>', unsafe_allow_html=True)
    filename = st.text_input("File Name", placeholder="notes.txt", key="c_name")
    content  = st.text_area("File Content", placeholder="Start writing here...", height=160, key="c_content")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="btn-create">', unsafe_allow_html=True)
    if st.button("⊕ Create File", key="create_btn"):
        if not filename.strip():
            st.error("Filename cannot be empty.")
        else:
            try:
                p = safe_path(filename.strip())
                if p.exists():
                    st.error(f"**{filename}** already exists. Choose a different name.")
                else:
                    p.write_text(content)
                    st.success(f"✓ **{filename}** created successfully!")
                    st.balloons()
                    time.sleep(0.3)
                    st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# TAB 2 — READ
# ══════════════════════════════════════════════════════════
with tab2:
    st.markdown('<div class="card card-read">', unsafe_allow_html=True)
    st.markdown('<div class="card-label">02 — Read File Contents</div>', unsafe_allow_html=True)
    files_now = list_files()
    if files_now:
        chosen = st.selectbox("Choose a file", [f.name for f in files_now], key="r_sel")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="btn-read">', unsafe_allow_html=True)
        if st.button("◈ Read File", key="read_btn"):
            try:
                p = safe_path(chosen)
                text = p.read_text()
                sz = human_size(p)
                st.info(f"📄  **{chosen}**  ·  {sz}  ·  {len(text.splitlines())} lines")
                st.markdown(f'<div class="file-content-box">{text if text else "<em>— empty file —</em>"}</div>',
                            unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No files yet. Create one first.")
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# TAB 3 — UPDATE
# ══════════════════════════════════════════════════════════
with tab3:
    st.markdown('<div class="card card-update">', unsafe_allow_html=True)
    st.markdown('<div class="card-label">03 — Update Existing File</div>', unsafe_allow_html=True)
    files_now = list_files()
    if files_now:
        chosen_u = st.selectbox("Choose a file", [f.name for f in files_now], key="u_sel")
        operation = st.radio(
            "Operation",
            ["Rename", "Append Content", "Overwrite Content"],
            horizontal=True,
            key="u_op"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        if operation == "Rename":
            new_name = st.text_input("New Filename", placeholder="new_name.txt", key="u_newname")
            st.markdown('<div class="btn-update">', unsafe_allow_html=True)
            if st.button("◉ Rename File", key="rename_btn"):
                if not new_name.strip():
                    st.error("New filename cannot be empty.")
                else:
                    try:
                        src = safe_path(chosen_u)
                        dst = safe_path(new_name.strip())
                        if dst.exists():
                            st.error(f"**{new_name}** already exists.")
                        else:
                            src.rename(dst)
                            st.success(f"✓ Renamed **{chosen_u}** → **{new_name}**")
                            time.sleep(0.3)
                            st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")
            st.markdown('</div>', unsafe_allow_html=True)

        elif operation == "Append Content":
            append_data = st.text_area("Content to Append", height=120, key="u_append")
            st.markdown('<div class="btn-update">', unsafe_allow_html=True)
            if st.button("◉ Append to File", key="append_btn"):
                try:
                    p = safe_path(chosen_u)
                    with open(p, "a") as f:
                        f.write("\n" + append_data)
                    st.success(f"✓ Content appended to **{chosen_u}**")
                except Exception as e:
                    st.error(f"Error: {e}")
            st.markdown('</div>', unsafe_allow_html=True)

        else:  # Overwrite
            overwrite_data = st.text_area("New Content (replaces everything)", height=120, key="u_over")
            st.markdown('<div class="btn-update">', unsafe_allow_html=True)
            if st.button("◉ Overwrite File", key="overwrite_btn"):
                try:
                    p = safe_path(chosen_u)
                    p.write_text(overwrite_data)
                    st.success(f"✓ **{chosen_u}** overwritten successfully")
                except Exception as e:
                    st.error(f"Error: {e}")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No files yet. Create one first.")
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# TAB 4 — DELETE
# ══════════════════════════════════════════════════════════
with tab4:
    st.markdown('<div class="card card-delete">', unsafe_allow_html=True)
    st.markdown('<div class="card-label">04 — Delete File</div>', unsafe_allow_html=True)
    files_now = list_files()
    if files_now:
        chosen_d = st.selectbox("Choose a file to delete", [f.name for f in files_now], key="d_sel")
        st.markdown(f"""
        <div style="background:#1a0a0a;border:1px solid #3d1111;border-radius:6px;padding:0.9rem 1rem;
                    font-family:'Space Mono',monospace;font-size:0.75rem;color:#ff8080;margin-bottom:1rem;">
          ⚠ This action is permanent. <strong>{chosen_d}</strong> will be deleted.
        </div>
        """, unsafe_allow_html=True)
        confirm = st.checkbox(f'I confirm I want to delete "{chosen_d}"', key="d_confirm")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="btn-delete">', unsafe_allow_html=True)
        if st.button("✕ Delete File", key="delete_btn", disabled=not confirm):
            try:
                p = safe_path(chosen_d)
                p.unlink()
                st.success(f"✓ **{chosen_d}** deleted successfully.")
                time.sleep(0.3)
                st.rerun()
            except Exception as e:
                st.error(f"Error: {e}")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("No files to delete.")
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# TAB 5 — FILE BROWSER
# ══════════════════════════════════════════════════════════
with tab5:
    st.markdown('<div class="card-label" style="font-family:\'Space Mono\',monospace;font-size:0.62rem;letter-spacing:.18em;text-transform:uppercase;color:#6b7280;margin-bottom:1rem;">All Files in Workspace</div>', unsafe_allow_html=True)
    files_now = list_files()
    if files_now:
        for f in files_now:
            sz = human_size(f)
            st.markdown(f"""
            <div class="file-list-item">
              <div class="file-dot"></div>
              <span class="fname">{f.name}</span>
              <span>{sz}</span>
            </div>
            """, unsafe_allow_html=True)
        if st.button("↻ Refresh", key="refresh_btn"):
            st.rerun()
    else:
        st.markdown("""
        <div style="text-align:center;padding:3rem 1rem;font-family:'Space Mono',monospace;font-size:0.78rem;color:#6b7280;">
            No files yet.<br><span style="color:#4fffb0">Create your first file →</span>
        </div>
        """, unsafe_allow_html=True)

# ─── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<hr>
<div style="text-align:center;font-family:'Space Mono',monospace;font-size:0.62rem;
            letter-spacing:0.12em;text-transform:uppercase;color:#3d4150;padding-bottom:1rem;">
  FileForge · Built with Python & Streamlit
</div>
""", unsafe_allow_html=True)