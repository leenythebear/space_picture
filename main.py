import argparse
import os
import random
import time
from urllib.parse import urlparse

from dotenv import load_dotenv

from fetch_apod_nasa_images import fetch_apod_nasa_images, get_apod_nasa_links
from fetch_epic_nasa_images import (fetch_epic_nasa_images,
                                    get_epic_images_links,
                                    get_epic_images_parameters)
from fetch_spacex_images import (fetch_spacex_images, get_launch_with_images,
                                 get_spacex_images_links)
from publish_image_to_telegram import del_image, publish_image, take_files
from settings import ALL_LAUNCHES_URL, IMAGES_FOLDER, TIME_SLEEP

load_dotenv()

if __name__ == "__main__":
    while True:
        paths = list(os.walk(IMAGES_FOLDER))
        if not paths:
            id_flight = get_launch_with_images()
            parser = argparse.ArgumentParser(
                description="Выгрузка фотографий запуска SpaceX"
            )
            parser.add_argument(
                "--id",
                help="ID полета для выгрузки фотографий",
                default=id_flight,
            )
            args = parser.parse_args()
            flight_id = urlparse(args.id)
            url = ALL_LAUNCHES_URL + f"/{flight_id.path}"
            spacex_images_links = get_spacex_images_links(url)
            fetch_spacex_images(spacex_images_links)

            apod_nasa_links = get_apod_nasa_links()
            fetch_apod_nasa_images(apod_nasa_links)

            images_parameters = get_epic_images_parameters()
            epic_images_links = get_epic_images_links(images_parameters)
            fetch_epic_nasa_images(epic_images_links)
        else:
            time.sleep(TIME_SLEEP)
            images_path = take_files()
            image_path = random.choice(images_path)
            publish_image_path = publish_image(image_path)
            del_image(image_path)
