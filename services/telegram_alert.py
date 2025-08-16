import requests
import json

with open('config.json') as f:
    config = json.load(f)

def send_telegram_alert(msg):
    url = f"https://api.telegram.org/bot{config['bot_token']}/sendMessage"
    payload = {
        'chat_id': config['chat_id'],
        'text': msg
    }
    requests.post(url, data=payload)
