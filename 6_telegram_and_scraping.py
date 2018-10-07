#! python3
import telegram.ext
import urllib.request
import bs4

TOKEN = "TU_TOKEN"
URL = "https://www.etsisi.upm.es/estudios/secretaria-alumnos"


def noticias(bot, update):
    print("Recibido el comando")
    r = urllib.request.urlopen(URL)
    web = r.read()  # html binario
    print("Descargado la página web")

    soup = bs4.BeautifulSoup(web, "html.parser")
    print("Cargado en BeautifulSoup")
    tr = soup.findAll("tr")[2]  # Buscamos en la tercera row

    text = "\n\n".join(i.text for i in tr.findAll("li"))  # ACTUALIDAD
    text += "\n\n" + URL
    print("Parseado las noticias")

    bot.send_message(update.message.chat_id, text)

updater = telegram.ext.Updater(token=TOKEN)
handler = telegram.ext.CommandHandler("noticias", noticias)
updater.dispatcher.add_handler(handler)

updater.start_polling()
updater.idle()
