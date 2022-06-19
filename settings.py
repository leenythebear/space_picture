import os

from dotenv import load_dotenv

load_dotenv()

CHAT_ID = "@cosmicboybot2022"
BOT_TOKEN = os.environ["BOT_TOKEN"]
TIME_SLEEP = 14400

IMAGES_FOLDER = "images"

NASA_TOKEN = os.getenv("NASA_TOKEN")

ALL_LAUNCHES_URL = "https://api.spacexdata.com/v4/launches"
LATEST_LAUNCH_URL = "https://api.spacexdata.com/v4/launches/latest"
FILE_NAME_SPACEX = "spacex"

APOD_URL = "https://api.nasa.gov/planetary/apod"
FILE_NAME_APOD = "apod"

EPIC_URL = "https://api.nasa.gov/EPIC/api/natural/images"
FILE_NAME_EPIC = "epic"
