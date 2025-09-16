from telegram.ext import MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Ты написал: {update.message.text}")

def get_echo_handler():
    return MessageHandler(filters.TEXT & ~filters.COMMAND, echo)