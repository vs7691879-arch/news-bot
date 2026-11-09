import requests
import time

# --- 1. CONFIGURATION & API KEYS ---
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

# News / Geopolitical Sentiment API (Example using a financial news API endpoint)
NEWS_API_URL = "https://newsapi.org/v2/everything?q=geopolitics+gold+nasdaq&apiKey=YOUR_NEWS_API_KEY"

# Trading Parameters for Scalping
TIMEFRAME = "1m"  # 1m/3m fast reaction timeframe
GOLD_ZONE = 4117.0
US100_ZONE = 27107.0
BUFFER = 2.0  # Tolerance buffer to avoid missing near-touches

def get_news_sentiment():
    """फिल्टर करता है कि क्या मार्केट पर इस वक्त कोई बड़ा जियोपॉलिटिकल या ट्रेड इम्पैक्ट है"""
    try:
        response = requests.get(NEWS_API_URL, timeout=5).json()
        articles = response.get("articles", [])
        # यदि हालिया खबरों में युद्ध, टैरिफ, या फेडरल रिजर्व का जिक्र है तो हाई इम्पैक्ट मानेंगे
        high_impact_keywords = ["tariff", "war", "conflict", "fed", "inflation", "trump"]
        
        for article in articles[:3]: # शुरुआती 3 ताजा खबरें चेक करें
            title = article.get("title", "").lower()
            if any(keyword in title for keyword in high_impact_keywords):
                return True, article.get("title")
    except Exception as e:
        print("News API Error:", e)
    return False, "Normal Flow"

def evaluate_bot_signal(symbol, current_price, zone_level, volume_spike):
    """तकनीकी रिजेक्शन, वॉल्यूम और जियोपॉलिटिकल न्यूज को मिलाकर फाइनल ट्रिगर तय करता है"""
    
    # स्टेप 1: ज़ोन टॉलरेंस और प्राइस चेक
    is_at_zone = abs(current_price - zone_level) <= BUFFER
    
    # स्टेप 2: वॉल्यूम स्पाइक चेक (नॉर्मल से 1.5 गुना ज्यादा)
    has_volume = volume_spike >= 1.5 
    
    # स्टेप 3: न्यूज और जियोपॉलिटिकल इम्पैक्ट चेक
    news_active, headline = get_news_sentiment()
    
    # यदि मार्केट जियोपॉलिटिकल जोन में है और वॉल्यूम आ रहा है, तो तुरंत ट्रिगर होगा
    if is_at_zone and has_volume:
        send_telegram_alert(symbol, current_price, headline, "High-Accuracy Setup")
        return True
    elif news_active and is_at_zone:
        # अगर बड़ी खबर है और प्राइस ज़ोन पर है, तो बिना वॉल्यूम के भी हल्का अलर्ट दे देगा
        send_telegram_alert(symbol, current_price, headline, "Geopolitical Driven Setup")
        return True
        
    return False

def send_telegram_alert(symbol, price, headline, setup_type):
    message = f"🚨 **HIGH ACCURACY ALERT!** 🚨\n\n" \
              f"Symbol: {symbol}\n" \
              f"Price: {price}\n" \
              f"Setup: {setup_type}\n" \
              f"News Catalyst: {headline}\n" \
              f"Timeframe: {TIMEFRAME} (Scalping Mode)"
              
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Telegram Error:", e)
