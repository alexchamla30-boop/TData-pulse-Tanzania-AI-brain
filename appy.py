up# 🇹🇿 TDataPulse Day 4 - Streamlit Dashboard
# Alex Chamla - Tanzania AI Economy Brain
# Run: streamlit run app.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="TDataPulse TZ", page_icon="🇹🇿")

st.title("🇹🇿 TDataPulse - Tanzania AI Brain")
st.subheader("Live Tracking: Orbit Securities & DSE")
st.write("Founder: Alex Chamla | Dar es Salaam | Day 4")

# Mock data for now - reading from data/prices.csv later
data = {
    "Fund": ["ORBIT-MA-ETF", "Inuka Fund", "CRDB", "NMB"],
    "Price (TZS)": [655.5, 344.2, 545.0, 4520.0],
    "Change": ["+0.8%", "+0.6%", "+0.9%", "+0.2%"],
    "Trend": ["📈", "📈", "📈", "📊"]
}

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.line_chart(df["Price (TZS)"])

st.success("💡 Insight: Orbit ETF up 2 days straight. Good for small investors!")
st.info("Next Day 5: Connect real scraper to orbit.co.tz")

st.markdown("---")
st.caption("Built with ❤️ in Dar es Salaam | github.com/alexchamla30-boop/TData-pulse-Tanzania-AI-brain")import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="TDataPulse - DSE Live", page_icon="🇹🇿", layout="wide")

st.title("🇹🇿 TDataPulse - Tanzania AI Brain")
st.subheader("Bei Halisi za Hisa DSE - LIVE Dashboard")

# Jaribu kusoma data halisi
path = "data/dse_live.csv"
if os.path.exists(path):
    df = pd.read_csv(path)
    st.success(f"✅ Data ya kweli imesomwa! Last update: {df['timestamp'][0]}")
else:
    # Fallback kama file bado haija-tengenezwa
    df = pd.DataFrame([
        {"symbol": "TCC", "name": "Tanzania Cigarette", "price": 6500, "change": 1.2, "timestamp": "Loading..."},
        {"symbol": "NMB", "name": "NMB Bank", "price": 4200, "change": -0.5, "timestamp": "Loading..."},
        {"symbol": "CRDB", "name": "CRDB Bank", "price": 580, "change": 2.1, "timestamp": "Loading..."},
    ])
    st.warning("⏳ Inasubiri data ya kweli kutoka main.py...")

# Onyesha kwa kadi
col1, col2, col3, col4 = st.columns(4)
cols = [col1, col2, col3, col4]

for i, row in df.head(4).iterrows():
    with cols[i % 4]:
        color = "normal" if row['change'] >= 0 else "inverse"
        st.metric(label=f"{row['symbol']} - {row['name']}", value=f"TZS {row['price']}", delta=f"{row['change']}%")

st.divider()

col_left, col_right = st.columns([2,1])

with col_left:
    st.write("### 📊 Chati ya Bei za Hisa")
    st.bar_chart(df, x="symbol", y="price", color="#00cc66")
    
with col_right:
    st.write("### 📋 Jedwali Kamili")
    st.dataframe(df, use_container_width=True, hide_index=True)

st.divider()
st.write("### 🤖 AI Insight")
best = df.loc[df['change'].idxmax()]
st.info(f"Leo hisa inayoongoza ni **{best['symbol']} ({best['name']})** na mabadiliko ya **+{best['change']}%**. Hii ni ishara nzuri kwa wawekezaji!")

st.caption("Built with ❤️ by Alex - TDataPulse Tanzania | Data source: DSE")