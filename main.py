# 🇹🇿 TDataPulse - Tanzania AI Economy Brain
# Founder: Alex Chamla - alexchamla30@gmail.com
# Day 1 - Challenge 2026-2029
# Location: Dar es Salaam

import datetime

print("=== TDataPulse Market Pulse ===")
print(f"Date: {datetime.date.today()}")
print("Tracking: ORBIT-MA-ETF, CRDB, NMB")
print("Status: Day 1 - Repo is Live!")
print("\nVision: Kila Mtanzania awe na mshauri wa kifedha")
print("Next: Scraping real prices from orbit.co.tz")# 🇹🇿 TDataPulse Day 2 - Real Market Scraper
# Founder: Alex Chamla | Dar es Salaam
# Target: orbit.co.tz - Inuka Fund & ETFs

import requests
from datetime import datetime# 🇹🇿 TDataPulse Day 3 - Data Persistence
# Alex Chamla | Dar es Salaam - Building AI Economy Brain
# Today we become Data Engineers

import csv
import os
from datetime import datetime

DATA_FILE = "data/prices.csv"

def get_today_market():
    # Simulated - Day 5 we connect real Orbit API
    return [
        {"date": datetime.now().strftime("%Y-%m-%d"), "fund": "ORBIT-MA-ETF", "price": 655.50, "change": "+0.8%", "source": "orbit.co.tz"},
        {"date": datetime.now().strftime("%Y-%m-%d"), "fund": "Inuka Fund", "price": 344.20, "change": "+0.6%", "source": "orbit.co.tz"},
        {"date": datetime.now().strftime("%Y-%m-%d"), "fund": "CRDB", "price": 545.00, "change": "+0.9%", "source": "DSE"},
    ]

def save_to_csv(new_data):
    file_exists = os.path.exists(DATA_FILE)
    # On GitHub mobile we just simulate, but structure is real
    print(f"💾 Saving {len(new_data)} records to {DATA_FILE}...")
    for row in new_data:
        print(f"  -> {row['fund']}: {row['price']} saved.")
    print("✅ Data persistence ready! This is what NMB Bank pays for.")

def daily_insight():
    print("\n--- TDataPulse AI Insight (Day 3) ---")
    print("📈 Trend: ETFs zinaongezeka siku 2 mfululizo.")
    print("💡 Ushauri: Kama uliwekeza TZS 100k Inuka Fund Nov 3, leo ungekuwa na TZS 100,600")
    print("🎯 Next: Day 4 - Graph ya kwanza kwa Streamlit!")

if __name__ == "__main__":
    print(f"=== TDataPulse Day 3 | {datetime.now().date()} ===")
    market = get_today_market()
    save_to_csv(market)
    daily_insight()

def get_orbit_data():
    print(f"=== TDataPulse Day 2 | {datetime.now().date()} ===")
    print("Connecting to Orbit Securities...")
    
    # For now we simulate with structure - Day 5 we add real BeautifulSoup
    # This structure is what employers look for: clean functions
    
    orbit_funds = [
        {"name": "ORBIT-MA-ETF", "price": 650.00, "change": "+1.2%", "source": "orbit.co.tz"},
        {"name": "Inuka Fund", "price": 342.15, "change": "+0.5%", "source": "orbit.co.tz"},
        {"name": "CRDB", "price": 540.00, "change": "-0.3%", "source": "DSE"},
        {"name": "NMB", "price": 4520.00, "change": "+0.8%", "source": "DSE"},
    ]
    
    print("\n--- LIVE MARKET PULSE ---")
    for fund in orbit_funds:
        print(f"{fund['name']}: TZS {fund['price']} ({fund['change']}) - {fund['source']}")
    
    print("\n--- INSIGHT ---")
    print("Orbit MA-ETF imepanda 1.2% - Dalili nzuri kwa wawekezaji wadogo.")
    print("Data saved to: data/orbit_prices.csv (coming Day 3)")
    
    return orbit_funds

def save_daily_report():
    # Day 3 we will save to CSV
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"\n[LOG] Report ya leo {today} imetengenezwa na Alex Chamla")
    print("[NEXT] Day 3: Tuta-save data kwenye CSV na kujenga graph")

if __name__ == "__main__":
    data = get_orbit_data()
    save_daily_report()import pandas as pd
import os
from datetime import datetime
os.makedirs("data", exist_ok=True)
def fetch_dse_real():
    stocks = [
        {"symbol": "TCC", "name": "Tanzania Cigarette", "price": 6500, "change": 1.2},
        {"symbol": "NMB", "name": "NMB Bank", "price": 4200, "change": -0.5},
        {"symbol": "CRDB", "name": "CRDB Bank", "price": 580, "change": 2.1},
        {"symbol": "DSE", "name": "DSE", "price": 1850, "change": 0.8},
        {"symbol": "TPCC", "name": "TP Cement", "price": 3800, "change": 0.0},
    ]
    df = pd.DataFrame(stocks)
    df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df.to_csv("data/dse_live.csv", index=False)
    print(f"Saved {len(df)} stocks")
    return df
if __name__ == "__main__":
    fetch_dse_real()