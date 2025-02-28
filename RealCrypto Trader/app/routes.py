from flask import Blueprint, render_template, jsonify
from binance.client import Client
import os
from dotenv import load_dotenv  

routes = Blueprint("routes", __name__)

# Load environment variables from .env file
load_dotenv()

# Fetch Binance API keys from environment
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

# Ensure API keys are available
if not BINANCE_API_KEY or not BINANCE_SECRET_KEY:
    raise ValueError("Missing Binance API keys. Please check your .env file.")

# Initialize Binance Client
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)

def fetch_prices():
    """Fetch current prices for BTC, ETH, BNB, ADA, SOL from Binance API."""
    symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "SOLUSDT"]
    prices = {}

    try:
        for symbol in symbols:
            ticker = client.get_symbol_ticker(symbol=symbol)
            prices[symbol] = ticker["price"]
    except Exception as e:
        print(f"Error fetching prices: {e}")

    return prices

@routes.route("/")
def home():
    """Render the main page with preloaded prices."""
    prices = fetch_prices()  
    return render_template("index.html", prices=prices) 

@routes.route("/get_prices")
def get_prices():
    """Fetch prices dynamically via API."""
    prices = fetch_prices()
    return jsonify(prices)
