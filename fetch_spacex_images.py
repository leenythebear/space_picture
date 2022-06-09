import requests

from helper import save_picture, create_folder, get_picture_extension


URL = 'https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a'
IMAGES_FOLDER = 'spacex'


def get_spacex_images_links():
    response = requests.get(URL)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def fetch_spacex_images(links):
    create_folder(IMAGES_FOLDER)
    for index, link in enumerate(links):
        extension = get_picture_extension(link)
        save_picture(index, link, IMAGES_FOLDER, extension)


if __name__ == '__main__':
    spacex_images_links = get_spacex_images_links()
    fetch_spacex_images(spacex_images_links)
