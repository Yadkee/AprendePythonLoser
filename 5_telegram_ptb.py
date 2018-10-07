#! python3
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "TU_TOKEN"


def echo(bot, update):
    text = update.message.text
    print(text)
    if text == "ping":
        bot.send_message(update.message.chat_id, "pong")

updater = Updater(token=TOKEN)
updater.start_polling()
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.idle()
