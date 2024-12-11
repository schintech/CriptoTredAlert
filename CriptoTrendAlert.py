import time
import requests
from datetime import datetime
import hmac
import hashlib
import json

# Your Binance and Telegram credentials
BINANCE_API_KEY = "YOUR_BINANCE_API_KEY"
BINANCE_SECRET_KEY = "YOUR_BINANCE_SECRET_KEY"
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# Binance API endpoints
BASE_URL = "https://api.binance.com/api/v3"
KLINES_ENDPOINT = "/klines"

# Telegram send message function
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=payload)

# Fetch kline data (price history)
def fetch_klines(symbol, interval="1m", limit=50):
    url = f"{BASE_URL}{KLINES_ENDPOINT}?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return [float(k[4]) for k in response.json()]  # Closing prices
    return []

# Calculate RSI
def calculate_rsi(prices, period=14):
    if len(prices) < period + 1:
        return None
    gains, losses = 0, 0
    for i in range(1, period + 1):
        diff = prices[-i] - prices[-i - 1]
        if diff > 0:
            gains += diff
        else:
            losses -= diff
    avg_gain = gains / period
    avg_loss = losses / period
    rs = avg_gain / avg_loss if avg_loss != 0 else 0
    return 100 - (100 / (1 + rs))

# Calculate SMA
def calculate_sma(prices, period):
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period

# Monitor and analyze the market
def monitor_market():
    # Initial conditions
    btc_sell_price = 95555
    eth_sell_price = "YOUR_ETH_SELL_PRICE"  # Replace with your ETH sell price
    btc_buy_back_price = 90000
    eth_buy_back_price = "YOUR_ETH_BUY_BACK_PRICE"  # Replace with your ETH buy-back price
    
    symbols = {
        "BTCUSDT": {"sell_price": btc_sell_price, "buy_back_price": btc_buy_back_price},
        "ETHUSDT": {"sell_price": eth_sell_price, "buy_back_price": eth_buy_back_price}
    }

    while True:
        for symbol, levels in symbols.items():
            prices = fetch_klines(symbol)
            if not prices:
                continue

            current_price = prices[-1]
            rsi = calculate_rsi(prices)
            sma = calculate_sma(prices, period=20)  # Example: 20-period SMA

            # Conditions to rebuy or take action
            if current_price <= levels["buy_back_price"]:
                message = f"ALERT: {symbol} has reached the buy-back price (${current_price}). Recommended to rebuy now."
                send_telegram_message(message)

            elif current_price > levels["sell_price"] and rsi > 70:
                message = f"ALERT: {symbol} RSI is {rsi} (Overbought). Consider exiting the short position."
                send_telegram_message(message)

            else:
                print(f"{datetime.now()} - {symbol} | Price: {current_price} | RSI: {rsi} | SMA: {sma}")
        
        # Pause for 1 minute
        time.sleep(60)

if __name__ == "__main__":
    try:
        send_telegram_message("Trading Bot Started: Monitoring BTC and ETH positions.")
        monitor_market()
    except Exception as e:
        send_telegram_message(f"Bot Error: {str(e)}")
