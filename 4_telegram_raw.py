#! python3
import urllib.request
import urllib.parse
import json

TOKEN = "TU_TOKEN"
URL = "https://api.telegram.org/bot%s/" % TOKEN
TIMEOUT = 5


def send_message(chat_id, text):
    args = {"chat_id": chat_id,
            "text": text}
    data = urllib.parse.urlencode(args).encode()
    r = urllib.request.urlopen(URL + "sendMessage", data=data).read()
    return json.loads(r)


def get_updates(offset):
    args = {"timeout": TIMEOUT,
            "offset": offset}
    data = urllib.parse.urlencode(args).encode()
    r = urllib.request.urlopen(URL + "getUpdates", data=data).read()
    return json.loads(r)


offset = 0
while True:
    try:
        updates = get_updates(offset)["result"]
    except KeyboardInterrupt:
        break
    if not updates:
        continue
    offset = updates[-1]["update_id"] + 1
    for i in updates:
        text = i["message"]["text"]
        chat_id = i["message"]["chat"]["id"]
        print(i)
        if text == "ping":
            print(send_message(chat_id, "pong"))
