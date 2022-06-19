import os
from urllib.parse import urlparse

import requests


def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)


def save_picture(index, url, folder_name, filename, extension, token=None):
    params = {"api_key": f"{token}"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f"{folder_name}/{filename}{index}{extension}", "wb") as file:
        file.write(response.content)


def get_picture_extension(url):
    parsed_link = urlparse(url)
    parsed_path = os.path.splitext(parsed_link.path)
    return parsed_path[1]
