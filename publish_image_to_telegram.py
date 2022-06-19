import os
import random

import telegram

from settings import BOT_TOKEN, CHAT_ID, IMAGES_FOLDER


def publish_image(image_path):
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_photo(chat_id=CHAT_ID, photo=open(image_path, "rb"))


def take_files():
    files = list(os.walk(IMAGES_FOLDER))
    names = files[0][-1]
    images_paths = []
    for name in names:
        images_paths.append(files[0][0] + "/" + name)
    return images_paths


def del_image(image_path):
    os.remove(image_path)


if __name__ == "__main__":
    paths = take_files()
    path = random.choice(paths)
    publish_image(path)
    del_image(path)
