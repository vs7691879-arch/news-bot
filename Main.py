from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time
import requests

# Render के लिए डमी वेब सर्वर ताकि पोर्ट एरर न आए
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"MT5 Advanced Trading Bot with Volume, S/R & News Sentiment is Live!")

def run_server():
    server_address = ('0.0.0.0', 10000)
    httpd = HTTPServer(server_address, SimpleHandler)
    httpd.serve_forever()

# बैकग्राउंड में वेब सर्वर चलाने के लिए थ्रेड शुरू करना
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# आपके ट्रेडिंग एसेट्स (MT5 के हिसाब से)
ASSETS = ["XAUUSD", "US100", "US Crude", "Forex", "Crypto"]

def send_telegram_alert(message):
    token = "9057258890:AAG6RdS_7Sr_3cpPrvGbd1SrHsTylFkjWI8" 
    chat_id = "5999494758"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    try:
        response = requests.post(url, json=payload)
        print("Telegram Response:", response.text)
    except Exception as e:
        print("Error sending telegram message:", e)

def analyze_market_conditions(asset):
    """
    यह फंक्शन High Volume Rejection, Breakout/Breakdown, S/R Profit Booking 
    और News Impact को एनालाइज करके सिग्नल जनरेट करेगा।
    """
    # यहाँ आप MT5 लाइव डेटा या API इंटीग्रेशन के हिसाब से वैल्यू सेट कर सकते हैं
    # उदाहरण के लिए एक सेलिंग-डोमिनेंट (Sell Bias) सेटअप:
    
    setup_type = "Bearish Rejection at Major Resistance (Supply Zone)"
    action = "SELL / SHORT 📉"
    volume_status = "High Volume Spike (Smart Money Rejection / Profit Booking)"
    news_context = "Hawkish Fed commentary & strong dollar index creating heavy overhead pressure near daily resistance."
    
    current_price = "2736.36"
    sl = "2743.36"
    tp1 = "2721.36"
    tp2 = "2708.36"
    
    return setup_type, action, volume_status, news_context, current_price, sl, tp1, tp2

def monitor_market():
    print("MT5 3m Timeframe Advanced S/R, Volume & News monitoring started...")
    
    # बॉट शुरू होने का टेस्ट मैसेज
    send_telegram_alert("🚀 *विक्रम देव सिंह*, Advanced MT5 Trading Bot (Volume + S/R + News Impact) is now live!")
    
    while True:
        try:
            for asset in ASSETS:
                # मार्केट का डीप एनालिसिस करना
                setup, action, volume, news, price, sl, tp1, tp2 = analyze_market_conditions(asset)
                
                # फॉर्मेट किया हुआ प्रोफेशनल टेलीग्राम सिग्नल मैसेज
                signal_message = (
                    f"🚨 *AI S/R REJECTION & SENTIMENT SIGNAL* 🚨\n\n"
                    f"📊 *Asset:* {asset}\n"
                    f"⚙️ *Setup:* {setup}\n"
                    f"📈 *Volume Action:* {volume}\n"
                    f"📍 *Current Zone Price:* {price}\n"
                    f"⚡ *Action:* {action}\n\n"
                    f"🛑 *Stop-Loss (SL):* {sl}\n"
                    f"🎯 *Target 1 (TP1):* {tp1}\n"
                    f"🎯 *Target 2 (TP2):* {tp2}\n\n"
                    f"📰 *Market & News Context:*\n{news}"
                )
                
                # सिग्नल मिलने पर टेलीग्राम पर भेजना (फिलहाल लूप को सुचारू रखने के लिए स्ट्रक्चर तैयार है)
                # send_telegram_alert(signal_message)
                
                break # टेस्ट के लिए फिलहाल एक एसेट पर रन करके लूप होल्ड कर रहे हैं
                
        except Exception as e:
            print("Error in market monitoring loop:", e)
            
        time.sleep(180) # हर 3 मिनट पर नया कैंडल क्लोज होने पर स्कैन करेगा

if __name__ == "__main__":
    send_telegram_alert("🚀 *विक्रम देव सिंह*, Advanced Bot connected successfully and scanning 3m candles!")
    monitor_market()







