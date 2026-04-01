import asyncio
import os
from pyrogram import Client, idle
from flask import Flask
from threading import Thread
from config import Config

# خادم ويب بسيط لإيهام Railway أن الخدمة نشطة
app = Flask(__name__)
@app.route('/')
def index(): return "UserBot is Alive!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

class HunterBot(Client):
    def __init__(self):
        super().__init__(
            name="my_hunter",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            session_string=Config.SESSION,
            plugins={"root": "plugins"} # سيبحث عن الأوامر داخل مجلد plugins
        )

    async def start_bot(self):
        await self.start()
        print("✅ تم تشغيل يوزر بوت الصيد بنجاح!")
        await idle()

if __name__ == "__main__":
    Thread(target=run_web, daemon=True).start()
    bot = HunterBot()
    asyncio.run(bot.start_bot())
