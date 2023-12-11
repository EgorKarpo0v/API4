from os import listdir
import telegram
import os
import random
from time import sleep

chat_id = "@SpaceImages11"
bot = telegram.Bot(token='6571182137:AAG6ZCJRwEF00pUTaXFlu9ay37duginxM5g')
print(bot.get_me())
# bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")
# bot.send_document(chat_id=chat_id, document=open('cat.png', "rb"))
while True:
    folder = "images"
    files = listdir(folder)
    random.shuffle(files)
    for file in files:
        path = os.path.join(folder, file)
        with open(path,"rb") as f:
            bot.send_document(chat_id=chat_id, document = f)
        sleep(600)
