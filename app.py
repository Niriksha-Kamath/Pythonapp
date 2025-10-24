from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1")
APP_MESSAGE = os.getenv("APP_MESSAGE", "Hello from Flask in a container!")

@app.route("/")
def home():
    return jsonify({
        "message": APP_MESSAGE,
        "version": APP_VERSION,
        "time": time.time()
    })

@app.route("/healthz")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
