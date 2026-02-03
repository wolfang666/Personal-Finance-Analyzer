import requests
import streamlit as st
from config import BACKEND_URL

@st.cache_data(ttl=300)
def fetch_summary(user_id: str) -> dict:
    resp = requests.get(f"{BACKEND_URL}/summary/{user_id}")
    resp.raise_for_status()
    return resp.json()

@st.cache_data(ttl=300)
def fetch_insights(user_id: str) -> str:
    resp = requests.get(f"{BACKEND_URL}/insights/{user_id}")
    resp.raise_for_status()
    return resp.json()["insights"]

@st.cache_data(ttl=300)
def fetch_merchants(user_id: str) -> list[str]:
    resp = requests.get(f"{BACKEND_URL}/merchants/{user_id}")
    return resp.json()

