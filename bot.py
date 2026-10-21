import os
from aiohttp import web
from pyrogram import Client, filters

# বট ক্লায়েন্ট ইনিশিয়ালাইজেশন
app = Client(
    "RenameBot",
    api_id=24324625,
    api_hash="9d95e42aadb33ab0ef1ba72940e5cfc4",
    bot_token="7610831016:AAFF86BmlnyQCrntXpDta93QEtOcBV6gGGI"
)

# রেন্ডারকে সজাগ রাখার জন্য aiohttp দিয়ে হালকা ওয়েব সার্ভার (থ্রেডিং ঝামেলা মুক্ত)
async def handle(request):
    return web.Response(text="Bot is active!")

async def web_server():
    server = web.Application()
    server.router.add_get("/", handle)
    runner = web.AppRunner(server)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

# ফাইল বা ভিডিও মেসেজ আসলে হ্যান্ডেল করার কাজ
@app.on_message(filters.document | filters.video)
async def rename_handler(client, message):
    await message.reply_text("আপনার ফাইলটি পেয়েছি! এখন নতুন নাম পাঠান:")

async def main():
    # ওয়েব সার্ভার এবং টেলিগ্রাম বট একসাথে স্টার্ট করা
    await web_server()
    await app.start()
    print("Bot and Web Server Started Successfully!")
    # বট যেন বন্ধ না হয়ে সচল থাকে
    await asyncio.Event().wait()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
