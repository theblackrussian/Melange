from poe_api_wrapper import PoeApi
import os
from config_yt import config
from dotenv import load_dotenv
load_dotenv(
    dotenv_path="/Users/tonda/Documents/Melange/.env"
)
cookie = os.getenv('COOKIE')

userq = input("Question: ")

# Take input text as argument
input_text = f"""
You must answer a question.
Your answer must be understood by a 10th grade student.
The question is: {userq}
"""

# Create an instance of the PoeApi
api = PoeApi(cookie)

# Hardcoded bot to work with
selected_bot = "Ahmes"

transcript_files = [
    os.path.join(config.TRANSCRIPTS_DIR, f)
    for f in os.listdir(config.TRANSCRIPTS_DIR)
    if f.endswith(".txt")
]

if transcript_files:
    # Send message with file and timeout of 90 seconds
    for chunk in api.send_message(
        bot=selected_bot,
        message=input_text,
        chatId=config.CHAT_ID,
        chatCode=config.CHAT_CODE,
        file_path=transcript_files,
        timeout=90,
    ):

        print(chunk["response"], end="", flush=True)
else:
    print(f"No transcripts found in {config.TRANSCRIPTS_DIR} directory.")

print("\n")

# Purge conversation so context is new every time
api.purge_conversation(
    bot=selected_bot, chatId=config.CHAT_ID, chatCode=config.CHAT_CODE
)

# Delete all files in the Transcripts directory
for f in transcript_files:
    os.remove(f)
