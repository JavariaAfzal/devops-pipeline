from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "DevOps Pipeline Application is Running!")
    return message

@app.route("/health")
def health():
    return "Healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))