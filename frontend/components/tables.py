import streamlit as st
import pandas as pd

def render_tables(summary: dict):
    st.subheader("Top Merchants")
    df = pd.DataFrame(summary["top_merchants"]).T
    st.table(df)
