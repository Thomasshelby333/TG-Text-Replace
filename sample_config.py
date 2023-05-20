import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6067529074:AAFGTov_CV1JbuE0rEdg1BOg0whPWdk_ghs")

    APP_ID = int(os.environ.get("APP_ID", 9321645))

    API_HASH = os.environ.get("API_HASH", "6a1b5084e59012093525c2443880a09a")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "HI")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5102746389").split())
