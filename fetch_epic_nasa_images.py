import datetime
import os

import requests

from helper import save_picture
from settings import EPIC_URL, FILE_NAME_EPIC, IMAGES_FOLDER, NASA_TOKEN


def get_epic_images_parameters():
    params = {"api_key": f"{NASA_TOKEN}"}
    response = requests.get(EPIC_URL, params=params)
    response.raise_for_status()
    parameters_of_picture = []
    for picture in response.json():
        parameters_of_picture.append([picture["date"], picture["image"]])
    return parameters_of_picture


def get_epic_images_links(parameters_of_picture):
    archive_url = "https://api.nasa.gov/EPIC/archive/natural"
    links = []
    for parameters in parameters_of_picture:
        image_datetime = parameters[0].split()[0]
        date = datetime.date.fromisoformat(image_datetime).strftime("%Y/%m/%d")
        name = parameters[1]
        url = archive_url + f"/{date}/png/{name}.png"
        links.append(url)
    return links


def fetch_epic_nasa_images(links):
    os.makedirs(IMAGES_FOLDER, exist_ok=True)
    for index, link in enumerate(links):
        save_picture(
            index,
            link,
            IMAGES_FOLDER,
            FILE_NAME_EPIC,
            extension=".png",
            token=NASA_TOKEN,
        )


if __name__ == "__main__":
    images_parameters = get_epic_images_parameters()
    epic_images_links = get_epic_images_links(images_parameters)
    fetch_epic_nasa_images(epic_images_links)
