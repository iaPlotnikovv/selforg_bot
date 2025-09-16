import logging
from config.settings import BOT_TOKEN
from handlers.start import get_start_handler
from handlers.echo import get_echo_handler
from telegram.ext import Application

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(get_start_handler())
    app.add_handler(get_echo_handler())
    app.run_polling()

if __name__ == '__main__':
    main()