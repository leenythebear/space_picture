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


def get_links_for_pictures_spacex(url):
    response = requests.get(url)
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


if __name__ == "__main__":
    links_for_picture_spacex = get_links_for_pictures_spacex(
        'https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a'
    )
    folder_name_spacex = 'spacex'
    create_folder(folder_name_spacex)
    for index, link in enumerate(links_for_picture_spacex):
        extension = get_picture_extension(link)
        save_picture(link, folder_name_spacex, extension)

    load_dotenv()
    nasa_token = os.environ['NASA_TOKEN']
    links_for_picture_nasa = get_links_for_picture_nasa(50, "https://api.nasa.gov/planetary/apod", nasa_token)
    folder_name_nasa = 'nasa'
    create_folder(folder_name_nasa)
    for index, link in enumerate(links_for_picture_nasa):
        extension = get_picture_extension(link)
        save_picture(link, folder_name_nasa, extension)
