import streamlit as st
import requests

from api.backend_client import (
    fetch_summary,
    fetch_insights,
    fetch_merchants
)
from components.charts import render_charts
from components.insights import render_insights
from components.corrections import render_correction_ui
from config import BACKEND_URL


# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Personal Finance Analyzer",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

user_id = "shuvrajyoti"


# ===================== STYLING =====================
st.markdown("""
<style>
:root {
    --card: #111827;
    --border: #1f2937;
    --accent: #22d3ee;
    --muted: #9ca3af;
}

/* Page spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Header */
.header {
    background: linear-gradient(90deg, #020617, #0f172a);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 25px 50px;
    margin-bottom: 1.2rem;
    box-shadow: inset 0 -1px 0 rgba(34, 211, 238, 0.25);
}

.header-title {
    font-size: 1.65rem;
    font-weight: 700;
    line-height: 1.2;
}

.header-sub {
    font-size: 0.85rem;
    color: var(--muted);
}

/* Cards */
.card {
    background-color: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.2rem;
    margin-bottom: 1.2rem;
}

/* Titles */
.card-title {
    font-size: 0.95rem;
    font-weight: 600;
    margin-bottom: 0.8rem;
}

/* KPI */
.kpi {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--accent);
}

.muted {
    font-size: 0.8rem;
    color: var(--muted);
}

/* Centered uploader */
.uploader-wrapper {
    display: flex;
    justify-content: center;
}

.uploader-wrapper > div {
    width: 100%;
    max-width: 720px;
}

/* Dropzone */
[data-testid="stFileUploader"] {
    border-radius: 14px;
    border: 1px dashed #374151;
    padding: 1.2rem;
    background-color: #0b1220;
}
</style>
""", unsafe_allow_html=True)


# ===================== HEADER =====================
st.markdown("""
<div class="header">
    <div class="header-title">📈 Personal Finance Analyzer</div>
    <div class="header-sub">
        AI-assisted understanding of your Google Pay spending
    </div>
</div>
""", unsafe_allow_html=True)


# ===================== UPLOAD =====================
with st.container():
    st.markdown("<div class='card-title'>📤 Upload GPay Statement</div>", unsafe_allow_html=True)

    st.markdown('<div class="uploader-wrapper">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Drag & drop your GPay PDF here",
        type=["pdf"],
        label_visibility="collapsed"
    )

    st.markdown('</div>', unsafe_allow_html=True)


# ===================== PROCESS =====================
if uploaded_file:
    with st.spinner("Uploading & parsing transactions..."):
        resp = requests.post(
            f"{BACKEND_URL}/upload/gpay",
            files={"file": uploaded_file},
            params={"user_id": user_id},
        )

    if resp.status_code != 200:
        st.error(resp.text)
        st.stop()

    st.success(f"✅ {resp.json().get('inserted', 0)} transactions processed")

    # ===================== TABS =====================
    tab1, tab2, tab3 = st.tabs([
        "🏷️ Categorize",
        "📈 Overview",
        "🧠 Insights"
    ])

    # ---------- TAB 1 ----------
    with tab1:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        merchants = fetch_merchants(user_id)
        if merchants:
            render_correction_ui(user_id, merchants)
        else:
            st.info("No merchants available.")

        st.markdown('</div>', unsafe_allow_html=True)

    # ---------- TAB 2 ----------
    with tab2:
        summary = fetch_summary(user_id)

        if not summary:
            st.warning("Summary not available.")
        else:
            monthly_spend = summary.get("monthly_spend", {})
            category_spend = summary.get("category_spend", {})

            total_spend = sum(monthly_spend.values())
            months_tracked = len(monthly_spend)

            top_category = (
                max(category_spend, key=lambda k: category_spend[k]["amount"])
                if category_spend else "N/A"
            )

            c1, c2, c3 = st.columns(3)

            for col, label, value in [
                (c1, "Total Spend", f"₹ {total_spend:,.0f}"),
                (c2, "Top Category", top_category),
                (c3, "Months Tracked", months_tracked),
            ]:
                with col:
                    st.markdown('<div class="card">', unsafe_allow_html=True)
                    st.markdown(f"<div class='muted'>{label}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='kpi'>{value}</div>", unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("<div class='card-title'>Spending Breakdown</div>", unsafe_allow_html=True)
            render_charts(summary)
            st.markdown('</div>', unsafe_allow_html=True)

    # ---------- TAB 3 ----------
    with tab3:
        insights = fetch_insights(user_id)

        st.markdown('<div class="card">', unsafe_allow_html=True)

        if insights:
            render_insights(insights)
        else:
            st.info("Insights not available yet.")

        st.markdown('</div>', unsafe_allow_html=True)
