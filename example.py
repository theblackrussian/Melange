from poe_api_wrapper import PoeExample
import os
from dotenv import load_dotenv
load_dotenv(
    dotenv_path="/Users/tonda/Documents/Melange/.env"
)
cookie = os.getenv('COOKIE')
PoeExample(cookie).select_bot()