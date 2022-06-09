import telegram
from dotenv import load_dotenv
import requests
import os
from urllib.parse import urlparse


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def save_picture(url, folder_name, extension, token=None):
    params = {"api_key": f"{token}"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(f'{folder_name}/{folder_name}{index}{extension}', 'wb') as file:
        file.write(response.content)


def get_picture_extension(url):
    parsed_link = urlparse(url)
    parsed_path = os.path.splitext(parsed_link.path)
    return parsed_path[1]


def get_links_for_pictures_spacex(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def get_links_for_picture_nasa(count, url, token):
    params = {"api_key": f"{token}",
              "count": count
              }
    response = requests.get(url, params=params)
    response.raise_for_status()
    links = []
    for picture in response.json():
        if picture['media_type'] == "image":
            links.append(picture["url"])
    return links


def get_earth_picture_parameters(url, token):
    params = {"api_key": f"{token}"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    parameters_of_picture = []
    for picture in response.json():
        parameters_of_picture.append([picture['date'], picture['image']])
    return parameters_of_picture


def get_links_for_earth_picture(parameters_of_picture):
    archive_url = 'https://api.nasa.gov/EPIC/archive/natural'
    links = []
    for parameters in parameters_of_picture:
        date = parameters[0].split()[0].replace("-", "/")
        name = parameters[1]
        url = archive_url + f"/{date}/png/{name}.png"
        links.append(url)
    return links[:1]


if __name__ == "__main__":
    load_dotenv()
    bot_token = os.environ['BOT_TOKEN']
    bot = telegram.Bot(token=bot_token)
    updates = bot.get_updates()
    chat_id = "@cosmicboybot2022"
    # bot.send_message(text="HI", chat_id=chat_id)
    bot.send_photo(chat_id=chat_id, photo=open('nasa_earth/nasa_earth0.png', 'rb'))

    links_for_picture_spacex = get_links_for_pictures_spacex(
        'https://api.spacexdata.com/v4/launches/5eb87d47ffd86e000604b38a'
    )
    folder_name_spacex = 'spacex'
    create_folder(folder_name_spacex)
    for index, link in enumerate(links_for_picture_spacex):
        picture_extension = get_picture_extension(link)
        save_picture(link, folder_name_spacex, picture_extension)

    nasa_token = os.environ['NASA_TOKEN']
    links_for_picture_nasa = get_links_for_picture_nasa(50, "https://api.nasa.gov/planetary/apod", nasa_token)
    folder_name_nasa = 'nasa'
    create_folder(folder_name_nasa)
    for index, link in enumerate(links_for_picture_nasa):
        picture_extension = get_picture_extension(link)
        save_picture(link, folder_name_nasa, picture_extension)

    picture_parameters = get_earth_picture_parameters('https://api.nasa.gov/EPIC/api/natural/images', nasa_token)
    folder_name_earth = "nasa_earth"
    create_folder(folder_name_earth)
    links_for_picture_earth = get_links_for_earth_picture(picture_parameters)
    for index, link in enumerate(links_for_picture_earth):
        save_picture(link, folder_name_earth, extension='.png', token=nasa_token)
