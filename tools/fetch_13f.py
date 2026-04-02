import json
from pathlib import Path

def fetch_13f_from_edgar(cik_code: str, year: int, quarter: int) -> dict:
    print(f"Connecting to SEC EDGAR for CIK: {cik_code} (Q{quarter}-{year})...")
    return {
        "status": "success",
        "fund_name": "MOCK_FUND_LLC",
        "top_holdings": [
            {"ticker": "MSFT", "weight": 0.08, "change_from_last_q": 0.01},
            {"ticker": "TLT", "weight": 0.02, "change_from_last_q": -0.05}
        ],
        "estimated_turnover": 0.65,
        "concentration_top10": 0.55
    }

if __name__ == "__main__":
    fetch_13f_from_edgar("0001811444", 2023, 3)
