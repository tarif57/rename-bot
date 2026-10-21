import os
import asyncio
from aiohttp import web
from pyrogram import Client, filters

# টেলিগ্রাম বট ক্লায়েন্ট
app = Client(
    "RenameBot",
    api_id=24324625,
    api_hash="9d95e42aadb33ab0ef1ba72940e5cfc4",
    bot_token="7610831016:AAFF86BmlnyQCrntXpDta93QEtOcBV6gGGI"
)

# রেন্ডার ফ্রি টিয়ার সজাগ রাখার জন্য aiohttp ওয়েব সার্ভার
async def handle(request):
    return web.Response(text="Bot is active and running!")

async def start_web_server():
    server = web.Application()
    server.router.add_get("/", handle)
    runner = web.AppRunner(server)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"Web server started on port {port}")

# ফাইল বা ভিডিও আসলে রিনেমের হ্যান্ডলার
@app.on_message(filters.document | filters.video)
async def rename_handler(client, message):
    await message.reply_text("আপনার ফাইলটি পেয়েছি! এখন নতুন ফাইলের নাম পাঠান:")

async def main():
    # প্রথমে ওয়েব সার্ভার এবং পরে বট স্টার্ট করা হবে
    await start_web_server()
    await app.start()
    print("Telegram Bot Started Successfully!")
    
    # বট যেন বন্ধ না হয়ে ব্যাকগ্রাউন্ডে সচল থাকে
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
