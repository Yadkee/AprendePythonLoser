#! python3
import telegram.ext

TOKEN = "TU_TOKEN"


def echo(bot, update):
    text = update.message.text
    print(text)
    if text == "ping":
        bot.send_message(update.message.chat_id, "pong")

updater = telegram.ext.Updater(token=TOKEN)
handler = telegram.ext.MessageHandler(telegram.ext.Filters.text, echo)
updater.dispatcher.add_handler(handler)

updater.start_polling()
updater.idle()
