import os
from dotenv import load_dotenv
from binance.client import Client

# Load environment variables from .env
load_dotenv()

# Fetch API keys (Corrected)
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")  
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY") 

# Check if API keys are loaded properly
if not BINANCE_API_KEY or not BINANCE_SECRET_KEY:
    raise ValueError("Missing Binance API keys. Please check your .env file.")

# Initialize Binance Client
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)
