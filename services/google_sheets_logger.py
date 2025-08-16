import gspread
from oauth2client.service_account import ServiceAccountCredentials

def log_to_sheets(result, symbol):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("your_credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("AlgoTrade_Log").worksheet("Trades")
    summary = client.open("AlgoTrade_Log").worksheet("Summary")

    # Log trades if there are any
    if result["log"]:
        for entry in result["log"]:
            sheet.append_row([
                symbol,
                entry['Date'].strftime("%Y-%m-%d"),
                entry['Action'],
                entry['Price']
            ])
    else:
        print(f"[INFO] No trades found for {symbol}")

    # Always log P&L to Summary (even if 0)
    summary.append_row([symbol, result["final_pnl"]])
