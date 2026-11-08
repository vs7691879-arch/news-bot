from fastapi import FastAPI, Request
import requests

app = FastAPI()

# आपकी जानकारी (Telegram Bot Token और Chat ID)
TELEGRAM_BOT_TOKEN = "9057258890:AAG6RdS_7Sr_3cpPrvGbd1SrHsTylFkjWI8"
CHAT_ID = "5999494758"

def send_telegram_message(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def home():
    return {"status": "Vikram News Bot is running 24/7!"}

@app.post("/webhook")
async def receive_news(request: Request):
    data = await request.json()
    
    asset = data.get("asset", "US100 / Gold / Oil")
    news_title = data.get("title", "Breaking Market News")
    impact = data.get("impact", "High Volatility Expected")
    signal = data.get("signal", "Watch Support/Resistance Levels")
    
    message = (
        f"🚨 *TRADING ALERT: {asset}* 🚨\n\n"
        f"📰 *News:* {news_title}\n"
        f"⚡ *Impact:* {impact}\n"
        f"📊 *Action:* {signal}\n\n"
        f"_Generated via Vikratna Bot_"
    )
    
    send_telegram_message(message)
    return {"status": "Alert sent successfully to Vikram!"}
