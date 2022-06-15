import telegram
import os
import random

from settings import CHAT_ID
from settings import BOT_TOKEN
from settings import IMAGES_FOLDER


def publish_image(images_paths):
    bot = telegram.Bot(token=BOT_TOKEN)
    image_path = random.choice(images_paths)
    bot.send_photo(chat_id=CHAT_ID, photo=open(image_path, 'rb'))
    return image_path


def take_files():
    files = list(os.walk(IMAGES_FOLDER))
    names = files[0][-1]
    images_paths = []
    for name in names:
        images_paths.append(files[0][0] + "/" + name)
    return images_paths


def del_image(image_path):
    os.remove(image_path)
    print(image_path)


if __name__ == '__main__':
    paths = take_files()
    path = publish_image(paths)
    del_image(path)
