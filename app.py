import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import base64

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SPK WP — Menu Sehat McDonald's India",
    page_icon="🥗",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CUSTOM CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.main .block-container {
    background: #0d0d12;
    padding-top: 1.5rem;
}
.stApp { background: #0d0d12; }

/* ── Hero Header ── */
.hero-header {
    position: relative;
    background: linear-gradient(135deg, #1a0a00 0%, #2d0f00 40%, #1a0a00 100%);
    border-radius: 20px;
    padding: 2.4rem 2.8rem;
    color: white;
    margin-bottom: 1.8rem;
    overflow: hidden;
    border: 1px solid rgba(218,41,28,0.3);
    box-shadow: 0 0 60px rgba(218,41,28,0.15), inset 0 1px 0 rgba(255,255,255,0.05);
}
.hero-header::before {
    content: '';
    position: absolute; top: -40%; right: -10%;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(255,199,44,0.12) 0%, transparent 65%);
    border-radius: 50%;
}
.hero-header::after {
    content: '';
    position: absolute; bottom: -50%; left: 20%;
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(218,41,28,0.18) 0%, transparent 65%);
    border-radius: 50%;
}
.hero-tag {
    display: inline-block;
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #ffc72c;
    background: rgba(255,199,44,0.1);
    border: 1px solid rgba(255,199,44,0.25);
    border-radius: 50px;
    padding: 0.25rem 0.85rem;
    margin-bottom: 0.85rem;
}
.hero-header h1 {
    font-family: 'Syne', sans-serif;
    font-size: 2.4rem; font-weight: 800;
    margin: 0 0 0.4rem;
    letter-spacing: -0.5px;
    background: linear-gradient(90deg, #ffffff 0%, #ffcb47 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-header p {
    font-size: 0.9rem; margin: 0;
    color: rgba(255,255,255,0.55); font-weight: 300;
}

/* ── Metric Cards ── */
.metric-card {
    background: linear-gradient(145deg, #161620, #1e1e2e);
    border-radius: 14px;
    padding: 1.3rem 1.5rem;
    border: 1px solid rgba(255,255,255,0.07);
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 1rem;
    position: relative; overflow: hidden;
}
.metric-card::before {
    content: '';
    position: absolute; top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(180deg, #da291c, #ffc72c);
    border-radius: 14px 0 0 14px;
}
.metric-card .label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem; color: rgba(255,255,255,0.4);
    font-weight: 500; text-transform: uppercase;
    letter-spacing: 0.1em; margin-bottom: 0.4rem;
}
.metric-card .value {
    font-family: 'Syne', sans-serif;
    font-size: 1.7rem; font-weight: 800;
    color: #ffffff; line-height: 1;
}

/* ── Step Boxes ── */
.step-box {
    background: linear-gradient(145deg, #131318, #1b1b26);
    border-radius: 12px;
    padding: 1.3rem 1.6rem;
    border: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 1.2rem;
}
.step-title {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem; color: #ffc72c;
    font-weight: 500; letter-spacing: 0.12em;
    margin-bottom: 0.6rem; text-transform: uppercase;
}
.step-box p, .step-box b { color: rgba(255,255,255,0.75); font-size: 0.9rem; }

/* ── Winner Card ── */
.winner-card {
    background: linear-gradient(135deg, #1a0600 0%, #2a0e00 50%, #1a0600 100%);
    border-radius: 20px;
    padding: 2.5rem 2rem; color: white;
    text-align: center;
    border: 1px solid rgba(218,41,28,0.4);
    box-shadow: 0 0 80px rgba(218,41,28,0.2), 0 20px 60px rgba(0,0,0,0.5);
    position: relative; overflow: hidden;
    margin-bottom: 1.5rem;
}
.winner-card::before {
    content: '';
    position: absolute; top: -30%; left: 50%;
    transform: translateX(-50%);
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(255,199,44,0.08) 0%, transparent 70%);
    border-radius: 50%;
}
.winner-card .rank1 {
    font-size: 3.5rem; margin-bottom: 0.5rem;
    filter: drop-shadow(0 0 20px rgba(255,199,44,0.6));
}
.winner-card h2 {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem; font-weight: 800;
    margin: 0.3rem 0 0.8rem;
    background: linear-gradient(90deg, #ffffff, #ffc72c);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.winner-card .score-badge {
    display: inline-block;
    background: linear-gradient(90deg, #da291c, #ff6b35);
    color: white;
    font-family: 'DM Mono', monospace;
    font-weight: 500; font-size: 1rem;
    border-radius: 50px;
    padding: 0.4rem 1.5rem; margin: 0.3rem 0;
    letter-spacing: 0.05em;
    box-shadow: 0 4px 20px rgba(218,41,28,0.4);
}
.winner-card .sub {
    color: rgba(255,255,255,0.45);
    font-size: 0.85rem; margin-top: 0.8rem; font-weight: 300;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: #0f0f18 !important;
    border-right: 1px solid rgba(255,255,255,0.06);
}
section[data-testid="stSidebar"] * { color: #d0d0e8 !important; }
section[data-testid="stSidebar"] .stSlider > div { color: white !important; }
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    font-family: 'Syne', sans-serif !important; color: #ffffff !important;
}

/* ── Tabs ── */
button[data-baseweb="tab"] {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    color: rgba(255,255,255,0.5) !important;
}
button[data-baseweb="tab"][aria-selected="true"] { color: #ffc72c !important; }

/* ── Section Labels ── */
.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem; font-weight: 700;
    color: #ffffff;
    margin: 1.5rem 0 0.8rem;
}

/* ── Footer ── */
.footer {
    text-align: center;
    color: rgba(255,255,255,0.25);
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem; letter-spacing: 0.05em;
    padding: 1.5rem 0 0.5rem;
    border-top: 1px solid rgba(255,255,255,0.06);
}

p, label, .stMarkdown p { color: rgba(255,255,255,0.8) !important; }
h1, h2, h3 { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# ─── LOAD DATA ──────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("IndiaMcDs_Menu.csv")
    df.columns = df.columns.str.strip()
    num_cols = ['Energy (kCal)', 'Protein (g)', 'Total fat (g)', 'Sat Fat (g)',
                'Trans fat (g)', 'Cholesterols (mg)', 'Total carbohydrate (g)',
                'Total Sugars (g)', 'Added Sugars (g)', 'Sodium (mg)']
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df.dropna(subset=num_cols, inplace=True)
    return df

df_all = load_data()

# ─── SIDEBAR ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Konfigurasi WP")
    st.markdown("---")

    st.markdown("### Filter Kategori")
    categories = ["Semua"] + sorted(df_all["Menu Category"].unique().tolist())
    selected_cat = st.selectbox("Kategori Menu", categories)

    st.markdown("### Jumlah Alternatif")
    top_n = st.slider("Tampilkan Top-N menu", min_value=5, max_value=30, value=10, step=1)

    st.markdown("---")
    st.markdown("### Bobot Kriteria")
    st.caption("Geser slider untuk mengatur bobot kepentingan (0.0 – 1.0)")

    w_energy  = st.slider(" Kalori (Cost)",         0.0, 1.0, 0.25, 0.05)
    w_protein = st.slider(" Protein (Benefit)",      0.0, 1.0, 0.30, 0.05)
    w_fat     = st.slider(" Total Lemak (Cost)",     0.0, 1.0, 0.20, 0.05)
    w_sugar   = st.slider(" Gula Tambahan (Cost)",   0.0, 1.0, 0.10, 0.05)
    w_sodium  = st.slider(" Sodium (Cost)",          0.0, 1.0, 0.15, 0.05)

    total_w = w_energy + w_protein + w_fat + w_sugar + w_sodium
    if abs(total_w - 1.0) > 0.001:
        st.warning(f" Total bobot = {total_w:.2f} (idealnya = 1.00)")
    else:
        st.success(f" Total bobot = {total_w:.2f}")

    st.markdown("---")
    st.markdown("### ℹ️ Info")
    st.markdown("""
    **Dataset:** McDonald's India Menu  
    **Metode:** Weighted Product (WP)  
    **Kriteria:** 5 variabel nutrisi              
    """)

# ─── HEADER ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <div class="hero-tag"> Praktikum SCPK — UPN Veteran Yogyakarta</div>
    <h1>🥗 SPK Pemilihan Menu Sehat</h1>
    <p>McDonald's India · Metode Weighted Product (WP) · 5 Kriteria Nutrisi</p>
</div>
""", unsafe_allow_html=True)

# ─── FILTER DATA ────────────────────────────────────────────────────────────────
if selected_cat == "Semua":
    df = df_all.copy()
else:
    df = df_all[df_all["Menu Category"] == selected_cat].copy()

CRITERIA = {
    'Energy (kCal)'   : {'type': 'cost',    'w': w_energy,  'label': 'Kalori (kCal)'},
    'Protein (g)'     : {'type': 'benefit', 'w': w_protein, 'label': 'Protein (g)'},
    'Total fat (g)'   : {'type': 'cost',    'w': w_fat,     'label': 'Total Lemak (g)'},
    'Added Sugars (g)': {'type': 'cost',    'w': w_sugar,   'label': 'Gula Tambahan (g)'},
    'Sodium (mg)'     : {'type': 'cost',    'w': w_sodium,  'label': 'Sodium (mg)'},
}

crit_cols = list(CRITERIA.keys())

# ─── SUMMARY METRICS ────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""<div class="metric-card">
        <div class="label">Total Menu</div>
        <div class="value">{len(df)}</div>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="metric-card">
        <div class="label">Kategori</div>
        <div class="value" style="font-size:1rem; padding-top:0.3rem">{selected_cat}</div>
    </div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="metric-card">
        <div class="label">Kriteria</div>
        <div class="value">5</div>
    </div>""", unsafe_allow_html=True)
with c4:
    st.markdown(f"""<div class="metric-card">
        <div class="label">Top N</div>
        <div class="value">{top_n}</div>
    </div>""", unsafe_allow_html=True)

# ─── TABS ───────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dataset", "🧮 Perhitungan WP", "🏆 Ranking", "📈 Visualisasi"])

# ═══ TAB 1 — DATASET ═══
with tab1:
    st.markdown('<div class="section-label"> Data Nutrisi Menu</div>', unsafe_allow_html=True)
    st.caption(f"Menampilkan {len(df)} item menu dari kategori: **{selected_cat}**")

    show_cols = ['Menu Category', 'Menu Items'] + crit_cols
    st.dataframe(df[show_cols].reset_index(drop=True), use_container_width=True, height=420)

    st.markdown('<div class="section-label"> Penjelasan Kriteria WP</div>', unsafe_allow_html=True)
    crit_info = pd.DataFrame([
        {"Kriteria": v['label'], "Kolom": k,
         "Tipe": "✅ Benefit" if v['type']=='benefit' else "❌ Cost",
         "Bobot": v['w']}
        for k, v in CRITERIA.items()
    ])
    st.dataframe(crit_info, use_container_width=True, hide_index=True)

# ═══ TAB 2 — PERHITUNGAN WP ═══
with tab2:
    total_w = sum(v['w'] for v in CRITERIA.values())
    if total_w == 0:
        st.error("Total bobot tidak boleh 0. Atur slider di sidebar.")
        st.stop()

    weights_norm = {k: v['w']/total_w for k, v in CRITERIA.items()}

    st.markdown("""
    <div class="step-box">
        <div class="step-title">LANGKAH 1 — NORMALISASI BOBOT</div>
        <p>Bobot ternormalisasi diperoleh dengan membagi tiap bobot dengan total bobot keseluruhan.</p>
    </div>
    """, unsafe_allow_html=True)

    w_df = pd.DataFrame([
        {"Kriteria": CRITERIA[k]['label'], "Tipe": CRITERIA[k]['type'].capitalize(),
         "Bobot Input": CRITERIA[k]['w'],
         "Bobot Ternormalisasi (Wj)": round(weights_norm[k], 4)}
        for k in CRITERIA
    ])
    st.dataframe(w_df, use_container_width=True, hide_index=True)

    st.markdown("""
    <div class="step-box">
        <div class="step-title">LANGKAH 2 — HITUNG VEKTOR S (NILAI PRODUK TERBOBOT)</div>
        <p>Formula: <b>Si = Π (Xij ^ Wj)</b><br>
        Pangkat positif (+Wj) untuk kriteria Benefit, pangkat negatif (-Wj) untuk kriteria Cost.</p>
    </div>
    """, unsafe_allow_html=True)

    df_wp = df[['Menu Category', 'Menu Items'] + crit_cols].copy().reset_index(drop=True)

    S_values = []
    for _, row in df_wp.iterrows():
        s = 1.0
        for col, meta in CRITERIA.items():
            val = row[col]
            if val <= 0:
                val = 1e-9
            exp = weights_norm[col] if meta['type'] == 'benefit' else -weights_norm[col]
            s *= (val ** exp)
        S_values.append(s)

    df_wp['Vektor S'] = S_values
    st.dataframe(
        df_wp[['Menu Items'] + crit_cols + ['Vektor S']].round(5).head(20),
        use_container_width=True, height=350
    )

    st.markdown("""
    <div class="step-box">
        <div class="step-title">LANGKAH 3 — HITUNG VEKTOR V (PREFERENSI AKHIR)</div>
        <p>Formula: <b>Vi = Si / Σ Si</b><br>
        Vektor V adalah nilai preferensi ternormalisasi; semakin besar V, semakin sehat menu tersebut.</p>
    </div>
    """, unsafe_allow_html=True)

    total_S = sum(S_values)
    df_wp['Vektor V'] = df_wp['Vektor S'] / total_S
    df_wp['Rank'] = df_wp['Vektor V'].rank(ascending=False).astype(int)
    df_wp_sorted = df_wp.sort_values('Rank')

    st.dataframe(
        df_wp_sorted[['Rank', 'Menu Items', 'Vektor S', 'Vektor V']].round(6).head(top_n),
        use_container_width=True, height=350
    )

# ═══ TAB 3 — RANKING ═══
with tab3:
    top_df = df_wp_sorted.head(top_n).copy()
    best = top_df.iloc[0]

    # ✅ Load gambar DULU di luar HTML
    try:
        with open("piala.png", "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
        trophy_html = f'<img src="data:image/png;base64,{img_b64}" style="width:80px; filter: drop-shadow(0 0 20px rgba(255,199,44,0.6));">'
    except FileNotFoundError:
        trophy_html = '<div style="font-size:3.5rem;">🏆</div>'  # fallback kalau file tidak ada

    # ✅ Baru masukkan variabel ke dalam HTML
    st.markdown(f"""
    <div class="winner-card">
        {trophy_html}
        <h2>{best['Menu Items']}</h2>
        <div class="score-badge">V = {best['Vektor V']:.6f}</div>
        <div class="sub">Menu paling sehat berdasarkan metode Weighted Product</div>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown(f'<div class="section-label">🏆 Top {top_n} Menu Paling Sehat</div>', unsafe_allow_html=True)
    rank_display = top_df[['Rank', 'Menu Items', 'Menu Category', 'Vektor V',
                            'Energy (kCal)', 'Protein (g)', 'Total fat (g)',
                            'Added Sugars (g)', 'Sodium (mg)']].copy()
    rank_display['Vektor V'] = rank_display['Vektor V'].map(lambda x: f"{x:.6f}")
    rank_display = rank_display.rename(columns={
        'Menu Items': 'Menu', 'Menu Category': 'Kategori',
        'Energy (kCal)': 'Kalori', 'Protein (g)': 'Protein',
        'Total fat (g)': 'Lemak', 'Added Sugars (g)': 'Gula Tambahan',
        'Sodium (mg)': 'Sodium'
    })
    st.dataframe(rank_display.reset_index(drop=True), use_container_width=True, height=420)

# ═══ TAB 4 — VISUALISASI ═══
with tab4:
    top_vis = df_wp_sorted.head(top_n).copy()

    DARK_BG = '#131318'
    FONT_CLR = 'rgba(255,255,255,0.8)'
    GRID_CLR = 'rgba(255,255,255,0.06)'

    # ── Bar chart ──
    st.markdown('<div class="section-label">📊 Nilai Preferensi (Vektor V) — Top Menu</div>', unsafe_allow_html=True)
    fig_bar = px.bar(
        top_vis, x='Vektor V', y='Menu Items', orientation='h',
        color='Vektor V',
        color_continuous_scale=['#ffc72c', '#ff6b35', '#da291c'],
        text=top_vis['Vektor V'].map(lambda x: f"{x:.5f}"),
        labels={'Menu Items': 'Menu', 'Vektor V': 'Nilai Preferensi (V)'},
    )
    fig_bar.update_layout(
        yaxis=dict(autorange='reversed', gridcolor=GRID_CLR),
        xaxis=dict(gridcolor=GRID_CLR),
        plot_bgcolor=DARK_BG, paper_bgcolor=DARK_BG,
        font=dict(family='DM Sans', color=FONT_CLR),
        coloraxis_showscale=False, height=440,
        margin=dict(l=10, r=20, t=20, b=20),
    )
    fig_bar.update_traces(textposition='outside', textfont_color=FONT_CLR)
    st.plotly_chart(fig_bar, use_container_width=True)

    col_l, col_r = st.columns(2)

    with col_l:
        st.markdown('<div class="section-label">🔵 Kalori vs Protein</div>', unsafe_allow_html=True)
        fig_sc = px.scatter(
            top_vis, x='Energy (kCal)', y='Protein (g)',
            size='Vektor V', color='Vektor V',
            color_continuous_scale=['#ffc72c', '#da291c'],
            hover_name='Menu Items',
            labels={'Energy (kCal)': 'Kalori (kCal)', 'Protein (g)': 'Protein (g)'},
            size_max=30,
        )
        fig_sc.update_layout(
            plot_bgcolor=DARK_BG, paper_bgcolor=DARK_BG,
            font=dict(family='DM Sans', color=FONT_CLR),
            height=360, coloraxis_showscale=False,
            xaxis=dict(gridcolor=GRID_CLR), yaxis=dict(gridcolor=GRID_CLR),
        )
        st.plotly_chart(fig_sc, use_container_width=True)

    with col_r:
        st.markdown('<div class="section-label">🕸️ Profil Nutrisi Top 5</div>', unsafe_allow_html=True)
        top5 = df_wp_sorted.head(5).copy()
        radar_cols   = ['Energy (kCal)', 'Protein (g)', 'Total fat (g)', 'Added Sugars (g)', 'Sodium (mg)']
        radar_labels = ['Kalori', 'Protein', 'Lemak', 'Gula', 'Sodium']

        fig_radar = go.Figure()
        colors = ['#da291c', '#ff6b35', '#ffc72c', '#27ae60', '#2980b9']

        for i, (_, row) in enumerate(top5.iterrows()):
            vals = []
            for c in radar_cols:
                col_max = df_wp[c].max()
                col_min = df_wp[c].min()
                norm = (row[c] - col_min) / (col_max - col_min + 1e-9)
                if CRITERIA[c]['type'] == 'cost':
                    norm = 1 - norm
                vals.append(round(norm, 3))

            fig_radar.add_trace(go.Scatterpolar(
                r=vals + [vals[0]],
                theta=radar_labels + [radar_labels[0]],
                fill='toself',
                name=row['Menu Items'][:25],
                line_color=colors[i],
                opacity=0.65,
            ))

        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 1],
                                gridcolor='rgba(255,255,255,0.08)',
                                color='rgba(255,255,255,0.4)'),
                angularaxis=dict(color='rgba(255,255,255,0.5)'),
                bgcolor=DARK_BG,
            ),
            showlegend=True,
            font=dict(family='DM Sans', color=FONT_CLR),
            height=360, paper_bgcolor=DARK_BG,
            legend=dict(font=dict(size=10), bgcolor='rgba(0,0,0,0)'),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown(f'<div class="section-label">🥧 Distribusi Kategori — Top {top_n} Menu Sehat</div>', unsafe_allow_html=True)
    cat_count = top_vis['Menu Category'].value_counts().reset_index()
    cat_count.columns = ['Kategori', 'Jumlah']
    fig_pie = px.pie(
        cat_count, values='Jumlah', names='Kategori', hole=0.45,
        color_discrete_sequence=['#da291c','#ff6b35','#ffc72c','#27ae60','#2980b9','#8e44ad','#e67e22'],
    )
    fig_pie.update_layout(
        font=dict(family='DM Sans', color=FONT_CLR),
        height=380, paper_bgcolor=DARK_BG,
        legend=dict(bgcolor='rgba(0,0,0,0)'),
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# ─── FOOTER ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div class="footer">
    🎓 PRAKTIKUM SISTEM CERDAS &amp; PENDUKUNG KEPUTUSAN &nbsp;·&nbsp; UPN VETERAN YOGYAKARTA
    &nbsp;·&nbsp; METODE WEIGHTED PRODUCT (WP) &nbsp;·&nbsp; DATASET: McDONALD'S INDIA MENU
</div>
""", unsafe_allow_html=True)