import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="TDataPulse - DSE Live", page_icon="🇹🇿", layout="wide")

st.title("🇹🇿 TDataPulse - Tanzania AI Brain")
st.subheader("Bei Halisi za Hisa DSE - LIVE Dashboard")

path = "data/dse_live.csv"

if os.path.exists(path):
    df = pd.read_csv(path)
    st.success("✅ Data ya kweli imesomwa!")
else:
    df = pd.DataFrame([
        {"symbol": "TCC", "name": "Tanzania Cigarette", "price": 6500, "change": 1.2},
        {"symbol": "NMB", "name": "NMB Bank", "price": 4200, "change": -0.5},
        {"symbol": "CRDB", "name": "CRDB Bank", "price": 580, "change": 2.1},
        {"symbol": "DSE", "name": "Dar Exchange", "price": 1850, "change": 0.8},
    ])
    st.warning("⏳ Data ya mfano - subiri file halisi")

col1, col2, col3, col4 = st.columns(4)
cols = [col1, col2, col3, col4]

for i, row in df.head(4).iterrows():
    with cols[i % 4]:
        st.metric(label=row["symbol"], value=f"TZS {row['price']}", delta=f"{row['change']}%")

st.divider()
st.write("### 📊 Chati ya Bei")
st.bar_chart(df, x="symbol", y="price")

st.write("### 📋 Jedwali")
st.dataframe(df, use_container_width=True, hide_index=True)

st.caption("Built by Alex - TDataPulse Tanzania")