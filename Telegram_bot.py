from os import listdir
import telegram
import os
import random
from time import sleep


def main():
    sleep_time = 600
    chat_id = os.enivron["CHAT_ID"]
    token = os.environ["TG_TOKEN"]
    bot = telegram.Bot(token=token)
    while True:
        folder = "images"
        files = listdir(folder)
        random.shuffle(files)
        for file in files:
            path = os.path.join(folder, file)
            with open(path,"rb") as f:
                bot.send_document(chat_id=chat_id, document = f)
            sleep(time_sleep)


if __name__ == "__main__":
    main()
