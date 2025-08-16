# 📈 AlgoTrade – Automated Stock Trading System  

## 🚀 Overview  
**AlgoTrade** is a Python-based trading bot that:  
- Fetches stock data from **Yahoo Finance**  
- Generates buy/sell signals using **technical indicators** (RSI, moving averages)  
- Runs a **backtesting engine** to evaluate strategies  
- Trains a simple **ML model (Decision Tree)** to predict price movement  
- Logs results into **Google Sheets**  
- Sends **real-time alerts via Telegram**  

This project is modular, making it easy to extend strategies, models, or integrations.  

---

## 📂 Project Structure  

algo_trade/
│── main.py # Entry point
│── requirements.txt # Dependencies
│── .gitignore # Ignore sensitive files
│
├── core/
│ ├── data_fetcher.py # Fetch stock data from Yahoo Finance
│ ├── strategy.py # Generate signals (RSI + Moving Averages)
│ ├── backtester.py # Backtesting engine
│ ├── ml_model.py # ML model for prediction
│ └── utils.py # Logging & helper functions
│
├── services/
│ ├── google_sheets_logger.py # Save trades + PnL to Google Sheets
│ └── telegram_alert.py # Send alerts to Telegram
│
├── config/
│ ├── config.json # Telegram bot config (chat_id, token)
│ └── your_credentials.json # Google API credentials (IGNORED via .gitignore)
│
└── tests/ # Unit tests (future expansion)

---

## ⚙️ Installation  

1. **Clone the repo**  
```bash
git clone https://github.com/yourusername/algo_trade.git
cd algo_trade

2. **Create a virtual environment (recommended)**
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3. **Install dependencies**
pip install -r requirements.txt
