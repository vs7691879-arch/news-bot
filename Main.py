from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import time
import requests

# Render के लिए डमी वेब सर्वर ताकि पोर्ट एरर न आए
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"MT5 Trading Bot is Live!")

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
    token = "905725890:AAG6RdS_7Sr..." 
    chat_id = "5999494758"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        response = requests.post(url, json=payload)
        print("Telegram Response:", response.text)
    except Exception as e:
        print("Error sending telegram message:", e)

def monitor_market():
    print("MT5 3m Timeframe S/R Rejection monitoring started...")
    
    # बॉट शुरू होने का टेस्ट मैसेज
    send_telegram_alert("🚀 Vikram, MT5 Trading Bot is now live and monitoring 3m S/R Rejections!")
    
    while True:
        try:
            # यहाँ MT5 के लाइव प्राइस एक्शन और 3m कैंडलस्टिक का डेटा प्रोसेस होगा
            for asset in ASSETS:
                # उदाहरण के लिए अपर रेजिस्टेंस रिजेक्शन लॉजिक (70-80% Sell Bias)
                # यदि MT5 डेटा में रेजिस्टेंस पर रिजेक्शन मिलता है:
                pass
                
        except Exception as e:
            print("Error in market monitoring loop:", e)
            
        time.sleep(180) # हर 3 मिनट पर नया कैंडल क्लोज होने पर स्कैन करेगा

if __name__ == "__main__":
    monitor_market()





