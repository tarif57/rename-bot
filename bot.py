import os
import threading
from flask import Flask
from pyrogram import Client, filters

# বট ক্লায়েন্ট ইনিশিয়ালাইজেশন
app = Client(
    "RenameBot",
    api_id=24324625,
    api_hash="9d95e42aadb33ab0ef1ba72940e5cfc4",
    bot_token="7610831016:AAFF86BmlnyQCrntXpDta93QEtOcBV6gGGI"
)

# রেন্ডার যেন সজাগ থাকে, তার জন্য ছোট ওয়েব সার্ভার
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is active!"

def run_web_server():
    web_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# ফাইল বা ভিডিও মেসেজ আসলে হ্যান্ডেল করার কাজ
@app.on_message(filters.document | filters.video)
async def rename_handler(client, message):
    await message.reply_text("আপনার ফাইলটি পেয়েছি! এখন নতুন নাম পাঠান:")

if __name__ == "__main__":
    # ব্যাকগ্রাউন্ডে ফ্লাস্ক সার্ভার চালু রাখা
    server_thread = threading.Thread(target=run_web_server)
    server_thread.daemon = True
    server_thread.start()

    # পাইথনের নতুন ভার্সনের জন্য সঠিক নিয়মে বট স্টার্ট করা
    app.run()
