# keep_alive.py
import os
import threading
import time
import requests
from flask import Flask

app = Flask(__name__)

RENDER_URL = os.getenv("RENDER_URL","https://silukkuchat-wf4n.onrender.com")

@app.route('/')
def home():
    return "✅ Bot is alive and running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

def self_ping():
    """Continuously ping the Render URL every 5 minutes."""
    while True:
        try:
            url = os.getenv("RENDER_URL")
            if url:
                requests.get(url)
                print(f"[KeepAlive] Pinged {url}")
            else:
                print("[KeepAlive] RENDER_URL not set.")
        except Exception as e:
            print(f"[KeepAlive] Error: {e}")
        time.sleep(300)

def keep_alive():
    """Start both Flask and self-ping in background threads."""
    threading.Thread(target=run_flask, daemon=True).start()
    threading.Thread(target=self_ping, daemon=True).start()
