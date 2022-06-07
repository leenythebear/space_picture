from pprint import pprint

import requests
import os


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def save_picture(link, folder_name, extension):
    response = requests.get(link)
    response.raise_for_status()
    with open(f'{folder_name}/{folder_name}{index}{extension}', 'wb') as file:
        file.write(response.content)


def get_picture_extension(link):
    parsed_link = urlparse(link)
    parsed_path = os.path.splitext(parsed_link.path)
    return parsed_path[1]


def get_links_for_pictures(latest_launch='https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a'):
    response = requests.get(latest_launch)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def get_links_for_picture_nasa(count, url, token):
    params = {"api_key": f"{nasa_token}",
              "count": count
              }
    response = requests.get(url, params=params)
    response.raise_for_status()
    links = []
    for picture in response.json():
        if picture['media_type'] == "image":
            links.append(picture["hdurl"])
    return links


