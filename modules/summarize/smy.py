from poe_api_wrapper import PoeApi
import os
from config import config
from prompt import prompt
import datetime
from dotenv import load_dotenv
load_dotenv(
    dotenv_path="/Users/tonda/Documents/Melange/.env"
)
cookie = os.getenv('COOKIE')

myprompt = prompt.PROMPT
bot = config.SELECTED_BOT
tdir = config.TRANSCRIPTS_DIR
chat_Id = config.CHAT_ID
chat_Code = config.CHAT_CODE

# Create an instance of the PoeApi
api = PoeApi(cookie)

# List all files in the Transcripts directory
transcript_files = [
    os.path.join(tdir, f) for f in os.listdir(tdir) if f.endswith(".txt")
]

# Check if there are any transcript files to send
if transcript_files:
    # Send message with all files and timeout of 90 seconds
    for chunk in api.send_message(
        bot=bot,
        message=myprompt,
        chatId=chat_Id,
        chatCode=chat_Code,
        file_path=transcript_files,  # Pass the entire list of files
        timeout=90,
    ):
        print(chunk["response"], end="", flush=True)
else:
    print(f"No transcript files found {tdir}")

print("\n")

# Purge conversation so context is new every time
api.purge_conversation(bot=bot, chatId=chat_Id, chatCode=chat_Code)

# Function that moves the transcript files to subdirectory for today's date
# def move_transcripts():
#     today = datetime.now().strftime("%Y-%m-%d")
#     for file in transcript_files:
#         os.rename(file, os.path.join(tdir, today, os.path.basename(file)))

# move_transcripts()