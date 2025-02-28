# RealCrypto-Trader-
RealCrypto Trader is a real-time cryptocurrency trading platform that fetches live price updates from the Binance WebSocket API and allows users to track cryptocurrency prices dynamically. The platform also features a portfolio management system, allowing users to monitor their crypto holdings.

🚀 Features

- Live Price Updates: Uses WebSocket API to stream real-time cryptocurrency prices.

- REST API Integration: Fetches current prices via Binance REST API.

- Portfolio Management: Users can add cryptocurrencies to their portfolio and track them.

- Modern UI: Interactive and visually appealing trading dashboard.

- Dynamic Updates: Prices update instantly without refreshing the page.
  
📌 Tech Stack

- Backend: Flask, Flask-SocketIO

- Frontend: HTML, CSS, JavaScript

- APIs: Binance WebSocket API, Binance REST API

🔧 Installation & Setup

1️⃣ Clone the Repository

 git clone https://github.com/ShivankBhasin/RealCrypto-Trader.git
 cd RealCrypto-Trader

2️⃣ Create a Virtual Environment

 python -m venv venv
 source venv/bin/activate  # For macOS/Linux
 venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies

 pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a .env file in the project root and add your Binance API keys:

BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key

5️⃣ Run the Application

 python run.py

🏗️ Project Structure:
   RealCrypto-Trader/
    │── app/
    │   │── __init__.py  # Initializes Flask app
    │   │── routes.py  # API routes for price fetching
    │   │── websocket.py  # WebSocket for live prices
    │   │── config.py  # Loads API keys & config
    │── static/
    │   │── style.css  # Stylesheet
    │── templates/
    │   │── index.html  # Frontend UI
    │── run.py  # Starts the Flask server
    │── requirements.txt  # Project dependencies
    │── .env  # API keys (ignored in .gitignore)
    │── README.md  # Project documentation
