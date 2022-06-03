from pprint import pprint

import requests
import os


if not os.path.exists("images"):
    os.makedirs("images")


def fetch_spacex_last_launch(links):
    for index, link in enumerate(links):
        response = requests.get(link)
        response.raise_for_status()
        with open(f'images/{index}.jpeg', 'wb') as file:
            file.write(response.content)


def get_picture_extension(link):
    parsed_link = urlparse(link)
    parsed_path = os.path.splitext(parsed_link.path)
    return parsed_path[1]


def get_links_for_pictures(latest_launch='https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a'):
    response = requests.get(latest_launch)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


# pprint(get_links_for_picture())

