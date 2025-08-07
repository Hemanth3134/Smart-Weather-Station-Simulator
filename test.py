
# test.py
import asyncio
from telegram import Bot

TOKEN = "7258863421:AAEcl92GoU2xS9cXyNBFvOILp8kqK0pGehY"
CHAT_ID = "7258863421"

async def send_message():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="✅ Test from weather station!")

if __name__ == "__main__":
    asyncio.run(send_message())
