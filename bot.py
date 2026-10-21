import os
import threading
from flask import Flask
from pyrogram import Client, filters

# সরাসরি আপনার আসল তথ্যগুলো এখানে বসিয়ে দিন:
app = Client(
    "RenameBot",
    api_id=24324625,
    api_hash="9d95e42aadb33ab0ef1ba72940e5cfc4",
    bot_token="7610831016:AAFF86BmlnyQCrntXpDta93QEtOcBV6gGGI"
)

# রেন্ডার যেন বটকে ঘুম পাড়াতে না পারে, সেজন্য ছোট একটি ওয়েব সার্ভার
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot is active!"

def run_web_server():
    web_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# বটের ফাইল রিনেম করার কাজ
@app.on_message(filters.document | filters.video)
async def rename_handler(client, message):
    await message.reply_text("আপনার ফাইলটি পেয়েছি! এখন নতুন নাম পাঠান:")

if __name__ == "__main__":
    # ওয়েব সার্ভার ব্যাকগ্রাউন্ডে চালু করা
    t = threading.Thread(target=run_web_server)
    t.start()

    # বট চালু করা
    app.run()
