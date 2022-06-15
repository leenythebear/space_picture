import os
from dotenv import load_dotenv
import requests

from helper import save_picture, create_folder

from settings import EPIC_URL
from settings import IMAGES_FOLDER
from settings import NASA_TOKEN
from settings import FILE_NAME_EPIC


def get_epic_images_parameters():
    params = {"api_key": f"{NASA_TOKEN}"}
    response = requests.get(URL, params=params)
    response.raise_for_status()
    parameters_of_picture = []
    for picture in response.json():
        parameters_of_picture.append([picture['date'], picture['image']])
    return parameters_of_picture


def get_epic_images_links(parameters_of_picture):
    archive_url = 'https://api.nasa.gov/EPIC/archive/natural'
    links = []
    for parameters in parameters_of_picture:
        date = parameters[0].split()[0].replace("-", "/")
        name = parameters[1]
        url = archive_url + f"/{date}/png/{name}.png"
        links.append(url)
    return links


def fetch_epic_nasa_images(links):
    create_folder(IMAGES_FOLDER)
    for index, link in enumerate(links):
        save_picture(index, link, IMAGES_FOLDER, FILE_NAME, extension='.png', token=NASA_TOKEN)


if __name__ == "__main__":
    images_parameters = get_epic_images_parameters()
    epic_images_links = get_epic_images_links(images_parameters)
    fetch_epic_nasa_images(epic_images_links)


