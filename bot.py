import os
import threading
from flask import Flask
from pyrogram import Client, filters

app = Client(
    "RenameBot",
    api_id=24324625,
    api_hash="9d95e42aadb33ab0ef1ba72940e5cfc4",
    bot_token="7610831016:AAFF86BmlnyQCrntXpDta93QEtOcBV6gGGI"
)

web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is active!"

def run_web_server():
    web_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

@app.on_message(filters.document | filters.video)
async def rename_handler(client, message):
    await message.reply_text("আপনার ফাইলটি পেয়েছি! এখন নতুন নাম পাঠান:")

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_web_server)
    server_thread.daemon = True
    server_thread.start()

    app.run()
