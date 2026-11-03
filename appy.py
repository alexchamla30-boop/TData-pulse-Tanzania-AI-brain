# 🇹🇿 TDataPulse Day 4 - Streamlit Dashboard
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
st.caption("Built with ❤️ in Dar es Salaam | github.com/alexchamla30-boop/TData-pulse-Tanzania-AI-brain")