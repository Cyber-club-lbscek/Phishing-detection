from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Define phishing indicators
RED_FLAGS = [
    "login", "verify", "update", "secure", "account",
    "paypal", "bank", "@", "bit.ly", "tinyurl"
]

@app.route("/api/detect_phishing", methods=["POST"])
def detect_phishing():
    data = request.get_json()
    url = data.get("url", "").lower()

    is_phishing = any(flag in url for flag in RED_FLAGS) or not url.startswith("https://")

    return jsonify({"phishing": is_phishing})

if __name__ == "__main__":
    app.run(debug=True)
