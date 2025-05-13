# Streamlit dashboard
API_URL = "https://5f9a9c15-180a-4bd3-9144-10df2bb2f2e1-00-2pvifywhn69hg.worf.replit.dev/"

try:
    response = requests.get(f"{API_URL}/latest-trade", headers=HEADERS)
    response.raise_for_status()
    data = response.json()

    st.subheader("Latest Signal")
    st.markdown(f"""
    **Action:** `{data.get('action', 'N/A')}`  
    **Symbol:** `{data.get('symbol', 'N/A')}`  
    **Price:** `${data.get('price', 'N/A')}`  
    **Time:** `{data.get('time', 'N/A')}`
    """)
except requests.exceptions.RequestException as e:
    st.error("API not reachable or unauthorized.")

import streamlit as st
import requests

# === CONFIG ===
API_URL = "https://5f9a9c15-180a-4bd3-9144-10df2bb2f2e1-00-2pvifywhn69hg.worf.replit.dev/"

# === PAGE SETTINGS ===
st.set_page_config(
    page_title="Crypto Bot Dashboard",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Crypto Bot Dashboard")

# === API CALL ===
try:
    response = requests.get(f"{API_URL}/latest-trade", headers=HEADERS)
    response.raise_for_status()
    data = response.json()

    # === DISPLAY SIGNAL ===
    st.subheader("Latest Trade Signal")
    st.markdown(f"""
    **Action:** `{data.get('action', 'N/A')}`  
    **Symbol:** `{data.get('symbol', 'N/A')}`  
    **Price:** `${data.get('price', 'N/A')}`  
    **Time:** `{data.get('time', 'N/A')}`
    """)

except requests.exceptions.RequestException as e:
    st.error("API not reachable or unauthorized.")
    st.text(str(e))

# === FOOTER ===
st.markdown("---")
st.caption("Built by Mychael Gray | Streamlit Dashboard connected to Flask API")
