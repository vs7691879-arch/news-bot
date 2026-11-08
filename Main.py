
# Main.py
import os
import requests
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from signals import analyze_market_and_generate_signal

app = FastAPI()

# टेलीग्राम क्रेडेंशियल्स जो आपने Render पर सेट किए हैं
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_alert(message: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram credentials missing!")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        print(f"Error sending telegram message: {e}")

# बैकग्राउंड जॉब जो हर 4 घंटे में ऑटोमैटिक सिग्नल भेजेगी
def scheduled_signal_job():
    signal_text = analyze_market_and_generate_signal()
    send_telegram_alert(signal_text)

scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_signal_job, 'interval', hours=4)
scheduler.start()

@app.get("/")
def home():
    return {"status": "Vikram Smart S/R Signal Bot is Live & Running smoothly!"}

@app.get("/trigger-signal")
def manual_trigger():
    """इस लिंक को ब्राउज़र में खोलकर आप तुरंत एक टेस्ट सिग्नल मंगा सकते हैं"""
    signal_text = analyze_market_and_generate_signal()
    send_telegram_alert(signal_text)
    return {"message": "Manual S/R Rejection Signal sent to Telegram successfully!"}
