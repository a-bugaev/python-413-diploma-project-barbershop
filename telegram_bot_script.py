"""
sends message by signal from django
"""

import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_message(text):
    """
    sends given massage to your chat
    """
    asyncio.run(Bot(token=BOT_TOKEN).send_message(CHAT_ID, text))
