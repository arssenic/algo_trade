import requests
import json

with open("config.json") as f:
    config = json.load(f)

def send_telegram_alert(msg):
    url = f"https://api.telegram.org/bot{config['bot_token']}/sendMessage"
    payload = {
        "chat_id": config['chat_id'],
        "text": msg
    }
    r = requests.post(url, data=payload)
    print("Status:", r.status_code)
    print("Response:", r.text)

send_telegram_alert("Telegram bot is working!")
