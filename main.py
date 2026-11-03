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
from datetime import datetime

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
    save_daily_report()