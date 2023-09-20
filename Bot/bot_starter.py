from telegram import Update
from telegram.ext import Application, MessageHandler, filters, BaseHandler

import dotenv_values


def start_bot(callbacks: []):
    application = Application.builder().token(dotenv_values.telegram_bot_token).build()
    application.add_handlers(callbacks)
    application.run_polling(allowed_updates=Update.ALL_TYPES)
