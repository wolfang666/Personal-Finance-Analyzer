import streamlit as st
import pandas as pd

def render_charts(summary: dict):
    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
      st.subheader("Monthly Spend")
      st.line_chart(summary["monthly_spend"], height=220)

    with col2:
      st.subheader("Category Breakdown")
      cat_df = pd.DataFrame(summary["category_spend"]).T
      st.bar_chart(cat_df["percentage"], height=220)

    with col3:
      st.subheader("Top Merchants")
      merch_df = pd.DataFrame(summary["top_merchants"]).T
      st.dataframe(merch_df, height=220)

