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
