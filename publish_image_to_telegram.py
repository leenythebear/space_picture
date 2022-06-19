import argparse
import os
import random
from urllib.parse import urlparse

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
    parser = argparse.ArgumentParser(
        description="Публикация фотографии в Telegram"
    )
    parser.add_argument(
        "--image",
        help="Наименование фотографии",
    )
    args = parser.parse_args()
    if args.image:
        image = urlparse(args.image)
        path = IMAGES_FOLDER + f"/{image.path}"
        if os.path.isfile(path):
            publish_image(path)
            del_image(path)
        else:
            print("Указанного файла не существует")
    else:
        paths = take_files()
        path = random.choice(paths)
        publish_image(path)
        del_image(path)
