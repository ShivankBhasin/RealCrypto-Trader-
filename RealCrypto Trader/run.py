from flask import Flask, render_template
from app import create_app

app = create_app()

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

if __name__ == "__main__":
    print("Flask app is running on http://127.0.0.1:5000")
    app.run(debug=True)
