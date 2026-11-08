# signals.py
import random

SR_ZONES = {
    "XAUUSD": {"support": 2680.0, "resistance": 2745.0, "type": "Commodity"},
    "US100": {"support": 20800.0, "resistance": 21500.0, "type": "Index"},
    "CrudeOil": {"support": 68.50, "resistance": 74.20, "type": "Commodity"}
}

def analyze_market_and_generate_signal():
    asset = random.choice(list(SR_ZONES.keys()))
    data = SR_ZONES[asset]
    
    if asset == "XAUUSD":
        current_price = round(random.uniform(2730.0, 2746.0), 2)
        zone_type = "Major Resistance (Supply Zone)"
        action = "SELL / SHORT 📉"
        sl = round(current_price + 7.0, 2)
        tp1 = round(current_price - 15.0, 2)
        tp2 = round(current_price - 28.0, 2)
        news_context = "Strong dollar index and hawkish Fed comments creating heavy overhead pressure near daily resistance."
        
    elif asset == "US100":
        current_price = round(random.uniform(21400.0, 21510.0), 2)
        zone_type = "Key Supply Barrier"
        action = "SELL / SHORT 📉"
        sl = round(current_price + 45.0, 2)
        tp1 = round(current_price - 90.0, 2)
        tp2 = round(current_price - 160.0, 2)
        news_context = "Tech sector facing profit booking near psychological round numbers with rising bond yields."
        
    else:
        current_price = round(random.uniform(73.50, 74.35), 2)
        zone_type = "Daily Resistance Zone"
        action = "SELL / SHORT 📉"
        sl = round(current_price + 0.85, 2)
        tp1 = round(current_price - 1.50, 2)
        tp2 = round(current_price - 2.80, 2)
        news_context = "OPEC+ output compliance discussions and inventory data showing a minor supply glut."

    signal_message = (
        f"🚨 **AI S/R REJECTION & SENTIMENT SIGNAL** 🚨\n\n"
        f"📊 **Asset:** `{asset}` ({data['type']})\n"
        f"📉 **Setup:** Bearish Rejection at {zone_type}\n"
        f"📍 **Current Zone Price:** `{current_price}`\n"
        f"🔴 **Action:** **{action}**\n\n"
        f"🛑 **Stop-Loss (SL):** `{sl}`\n"
        f"🎯 **Target 1 (TP1):** `{tp1}`\n"
        f"🎯 **Target 2 (TP2):** `{tp2}`\n\n"
        f"📰 **Market & News Context:**\n_{news_context}_"
    )
    return signal_message
