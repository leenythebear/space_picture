import requests

from helper import save_picture, create_folder, get_picture_extension

from settings import APOD_URL
from settings import IMAGES_FOLDER
from settings import FILE_NAME_APOD
from settings import NASA_TOKEN


def get_apod_nasa_links(count=30):
    params = {"api_key": f"{NASA_TOKEN}",
              "count": count
              }
    response = requests.get(APOD_URL, params=params)
    response.raise_for_status()
    links = []
    for picture in response.json():
        if picture['media_type'] == "image":
            links.append(picture["url"])
    return links


def fetch_apod_nasa_images(links):
    create_folder(IMAGES_FOLDER)
    for index, link in enumerate(links):
        extension = get_picture_extension(link)
        save_picture(index, link, IMAGES_FOLDER, FILE_NAME_APOD, extension, token=NASA_TOKEN)


if __name__ == "__main__":
    apod_nasa_links = get_apod_nasa_links()
    fetch_apod_nasa_images(apod_nasa_links)
