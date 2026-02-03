import streamlit as st
import requests
from config import BACKEND_URL


def render_correction_ui(user_id: str, merchants: list[str]):
    st.subheader("Correct Merchant Category")

    merchant = st.selectbox("Merchant", merchants)
    category = st.selectbox(
        "Correct Category",
        ["Food", "Shopping", "Transport", "Bills", "Entertainment", "Others"]
    )
    subcategory = st.text_input("Subcategory (optional)")

    if st.button("Apply Correction"):
        resp = requests.post(
            f"{BACKEND_URL}/correct",
            json={
                "user_id": user_id,
                "merchant": merchant,
                "category": category,
                "subcategory": subcategory or None,
            },
        )

        if resp.status_code == 200:
            st.success("Correction saved. Future transactions will be updated.")
        else:
            st.error(resp.text)
