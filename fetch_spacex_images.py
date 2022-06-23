import argparse
import os
from urllib.parse import urlparse

import requests

from helper import get_picture_extension, save_picture
from settings import ALL_LAUNCHES_URL, FILE_NAME_SPACEX, IMAGES_FOLDER


def get_launch_with_images():
    response = requests.get(ALL_LAUNCHES_URL)
    response.raise_for_status()
    for flight in response.json()[::-1]:
        flight_number = flight["id"]
        response = requests.get(f"{ALL_LAUNCHES_URL}/{flight_number}")
        response.raise_for_status()
        if len(response.json()["links"]["flickr"]["original"]) != 0:
            return flight_number


def get_spacex_images_links(link):
    response = requests.get(link)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def fetch_spacex_images(links):
    os.makedirs(IMAGES_FOLDER, exist_ok=True)
    for index, link in enumerate(links):
        extension = get_picture_extension(link)
        save_picture(index, link, IMAGES_FOLDER, FILE_NAME_SPACEX, extension)


if __name__ == "__main__":
    id_flight = get_launch_with_images()
    parser = argparse.ArgumentParser(
        description="Выгрузка фотографий запуска SpaceX"
    )
    parser.add_argument(
        "--id", help="ID полета для выгрузки фотографий", default=id_flight
    )
    args = parser.parse_args()
    flight_id = urlparse(args.id)
    if flight_id:
        url = ALL_LAUNCHES_URL + f"/{flight_id.path}"
    else:
        url = get_launch_with_images()
    spacex_images_links = get_spacex_images_links(url)
    fetch_spacex_images(spacex_images_links)
