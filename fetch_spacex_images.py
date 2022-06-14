import argparse
from urllib.parse import urlparse

import requests

from helper import save_picture, create_folder, get_picture_extension


BASE_URL = 'https://api.spacexdata.com/v4/launches'
IMAGES_FOLDER = 'images'
FILE_NAME = 'spacex'


def get_spacex_images_links(link):
    response = requests.get(link)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def fetch_spacex_images(links):
    create_folder(IMAGES_FOLDER)
    for index, link in enumerate(links):
        extension = get_picture_extension(link)
        save_picture(index, link, IMAGES_FOLDER, FILE_NAME, extension)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Выгрузка фотографий запуска SpaceX')
    parser.add_argument('id', help='ID полета для выгрузки фотографий')
    args = parser.parse_args()
    flight_id = urlparse(args.id)
    url = BASE_URL + f'/{flight_id.path}'
    spacex_images_links = get_spacex_images_links(url)
    fetch_spacex_images(spacex_images_links)
