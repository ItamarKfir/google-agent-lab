from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Lab Test APP"

@app.route("/chat")
def chat():
    return "Wellcome to the chat 2"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)