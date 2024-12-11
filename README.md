


---
Real-Time Crypto Trading Monitor and Alert Bot

This project is a real-time cryptocurrency trading monitor and alert bot designed to help you track and manage your short positions on Bitcoin (BTC) and Ethereum (ETH). The bot continuously analyzes market data using indicators such as RSI (Relative Strength Index) and SMA (Simple Moving Average). It sends alerts to your Telegram when predefined conditions are met, such as reaching a buy-back price or encountering overbought/oversold conditions.


---

Features

1. Real-Time Monitoring:

Continuously tracks BTC and ETH market prices using Binance API.

Calculates RSI and SMA indicators for analysis.



2. Alert System:

Sends actionable alerts to your Telegram account when specific trading conditions are met:

Reaching the buy-back price.

Overbought conditions (RSI > 70).




3. Continuous Operation:

Runs continuously and evaluates market conditions every minute.



4. Customizable:

Configure sell prices, buy-back prices, and other parameters as per your trading strategy.





---

How It Works

1. Market Data Fetching:

The bot fetches real-time price data for BTC/USDT and ETH/USDT pairs from the Binance API.



2. Indicator Calculation:

RSI: Used to detect overbought (>70) or oversold (<30) conditions.

SMA: Used to identify short-term market trends.



3. Decision Making:

Sends a buy-back alert if the price drops to your predefined buy-back level.

Sends an exit alert if the price rises above your sell price and RSI > 70.



4. Alerts:

Alerts are sent to your Telegram chat using the Telegram Bot API.





---

Prerequisites

Python 3.7+

Binance account with API key and secret.

Telegram account with a bot set up for messaging.



---

Setup Instructions

1. Clone the Repository

git clone https://github.com/schintech/CriptoTredAlert/tree/main
cd crypto-trading-monitor

2. Install Dependencies

Install required Python libraries using pip:

pip install requests

3. Set Up API Keys

Binance API:

Log in to your Binance account.

Navigate to the API Management section and create an API key and secret.

Replace YOUR_BINANCE_API_KEY and YOUR_BINANCE_SECRET_KEY in the code with your credentials.


Telegram Bot:

Create a bot using BotFather on Telegram.

Note down your bot token and replace YOUR_TELEGRAM_BOT_TOKEN in the code.

Find your Telegram chat ID using a bot like IDBot and replace YOUR_TELEGRAM_CHAT_ID.



4. Configure Price Levels

Edit the monitor_market function in the script to set your desired:

Sell Price: Price at which you sold BTC/ETH (e.g., btc_sell_price = 95555).

Buy-Back Price: Price at which you want to rebuy BTC/ETH (e.g., btc_buy_back_price = 90000).


5. Run the Bot

Execute the script using Python:

python trading_bot.py


---

Alerts

Buy-Back Alert: Triggered when the price drops to or below the predefined buy-back price.

Exit Alert: Triggered when the price exceeds the sell price and RSI > 70.


Example Telegram messages:

ALERT: BTCUSDT has reached the buy-back price ($90000). Recommended to rebuy now.

ALERT: ETHUSDT RSI is 72.5 (Overbought). Consider exiting the short position.



---

Customization

Add New Indicators

You can enhance the bot with additional technical indicators such as:

Bollinger Bands

MACD (Moving Average Convergence Divergence)


Monitor Additional Pairs

To monitor more trading pairs:

Add them to the symbols dictionary in the monitor_market function.

Set appropriate sell and buy-back prices for each pair.



---

Example Output

Console Output:

2024-12-11 10:01:00 - BTCUSDT | Price: 94500 | RSI: 55.2 | SMA: 95000
2024-12-11 10:02:00 - ETHUSDT | Price: 3700 | RSI: 65.0 | SMA: 3650

Telegram Alerts:

ALERT: BTCUSDT has reached the buy-back price ($90000). Recommended to rebuy now.


---

Troubleshooting

No Alerts:

Ensure your Binance API key has read permissions.

Verify your Telegram bot token and chat ID are correct.


Rate Limits:

Binance API has rate limits. Avoid spamming requests in short intervals.


Errors:

Check the error message in the Telegram alert if the bot stops working.




---

Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes.


---

License

This project is licensed under the MIT License.


---

