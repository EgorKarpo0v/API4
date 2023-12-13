from os import listdir
import telegram
import os
import random
from time import sleep


chat_id = "@SpaceImages11"
bot = telegram.Bot(token='6571182137:AAG6ZCJRwEF00pUTaXFlu9ay37duginxM5g')
while True:
    folder = "images"
    files = listdir(folder)
    random.shuffle(files)
    for file in files:
        path = os.path.join(folder, file)
        with open(path,"rb") as f:
            bot.send_document(chat_id=chat_id, document = f)
        sleep(600)
