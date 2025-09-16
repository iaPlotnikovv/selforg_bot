from telegram.ext import Application, MessageHandler, CommandHandler, filters
import logging

# Включи логи для отладки (покажет ошибки)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Токен из файла
with open('token.txt', 'r') as f:
    TOKEN = f.read().strip()

async def start(update, context):
    await update.message.reply_text("Привет! Я бот, который отвечает на твои сообщения.")
# Функция, которая отвечает на любое сообщение
async def echo(update, context):
    # Ответ на любое другое сообщение    
    await update.message.reply_text(f"Ты написал: {update.message.text}")
    

# Запуск бота
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    app.add_handler(CommandHandler("start", start))
    
    app.run_polling()

if __name__ == '__main__':
    main()