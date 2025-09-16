from telegram.ext import CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я бот для самоорганизации.')

def get_start_handler():
    return CommandHandler('start', start)