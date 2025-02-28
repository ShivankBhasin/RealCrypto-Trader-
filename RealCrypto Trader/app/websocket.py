from flask_socketio import SocketIO
from binance import ThreadedWebsocketManager
import os

socketio = SocketIO()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

twm = ThreadedWebsocketManager(api_key=BINANCE_API_KEY, api_secret=BINANCE_SECRET_KEY)

def handle_message(msg):
    """Handles incoming messages from Binance WebSocket."""
    if msg['e'] == '24hrTicker':
        socketio.emit("price_update", {msg["s"]: msg["c"]}) 

@socketio.on("connect")
def start_socket():
    """Starts the WebSocket connection on client connect."""
    twm.start()
    twm.start_symbol_ticker_socket(callback=handle_message, symbol="BTCUSDT")
    twm.start_symbol_ticker_socket(callback=handle_message, symbol="ETHUSDT")
    twm.start_symbol_ticker_socket(callback=handle_message, symbol="BNBUSDT")
    twm.start_symbol_ticker_socket(callback=handle_message, symbol="ADAUSDT")
    twm.start_symbol_ticker_socket(callback=handle_message, symbol="SOLUSDT")
