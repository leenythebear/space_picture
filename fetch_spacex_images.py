import argparse
import random
from urllib.parse import urlparse

import requests

from helper import save_picture, create_folder, get_picture_extension

def get_launch_with_images():
    response = requests.get(LATEST_LAUNCH_URL)
    response.raise_for_status()
    if len(response.json()['links']['flickr']['original']) != 0:
        return "latest"

    response = requests.get(ALL_LAUNCHES_URL)
    response.raise_for_status()
    flights = [flight['id'] for flight in response.json()]
    flight_number = random.choice(flights)
    response = requests.get(f"{ALL_LAUNCHES_URL}/{flight_number}")
    response.raise_for_status()
    while len(response.json()['links']['flickr']['original']) == 0:
        flight_number = random.choice(flights)
        response = requests.get(f"{ALL_LAUNCHES_URL}/{flight_number}")
        response.raise_for_status()
    return flight_number


def get_spacex_images_links(link):
    response = requests.get(link)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def fetch_spacex_images(links):
    create_folder(IMAGES_FOLDER)
    for index, link in enumerate(links):
        extension = get_picture_extension(link)
        save_picture(index, link, IMAGES_FOLDER, FILE_NAME_SPACEX, extension)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Выгрузка фотографий запуска SpaceX')
    parser.add_argument("--id", help='ID полета для выгрузки фотографий', default=id_flight)
    args = parser.parse_args()
    flight_id = urlparse(args.id)
    url = SPACEX_URL + f'/{flight_id.path}'
    spacex_images_links = get_spacex_images_links(url)
    fetch_spacex_images(spacex_images_links)
