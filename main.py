from pprint import pprint

import requests
import os


if not os.path.exists("images"):
    os.makedirs("images")


def save_picture(url, path, filename='hubble.jpeg'):
    response = requests.get(url)
    response.raise_for_status()
    with open(f'images/{filename}', 'wb') as file:
        file.write(response.content)


def get_links_for_picture(latest_launch='https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a'):
    response = requests.get(latest_launch)
    response.raise_for_status()
    return response.json()


# pprint(get_links_for_picture())

