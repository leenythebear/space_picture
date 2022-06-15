import os

from dotenv import load_dotenv

load_dotenv()

CHAT_ID = "@cosmicboybot2022"
BOT_TOKEN = os.environ['BOT_TOKEN']

IMAGES_FOLDER = 'images'

NASA_TOKEN = os.getenv("NASA_TOKEN")

SPACEX_URL = 'https://api.spacexdata.com/v4/launches'
FILE_NAME_SPACEX = 'spacex'

APOD_URL = 'https://api.nasa.gov/planetary/apod'
FILE_NAME_APOD = 'apod'

EPIC_URL = 'https://api.nasa.gov/EPIC/api/natural/images'
FILE_NAME_EPIC = 'epic'
