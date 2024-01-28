from youtube_transcript_api import YouTubeTranscriptApi as yta
import re

def print_time(search_word, time):
    print(f"'{search_word}' was mentioned at:")
    # calculate the accurate time according to the video's duration
    for t in time:
        hours = int(t // 3600)
        minutes = int((t % 3600) // 60)
        seconds = int(t % 60)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

# Get the youtube video id form url after "?v="
video_id = "PJLWlmp8CDM"
# Change the language if needed, example: en, English
transcript = yta.get_transcript(video_id, languages=('en', 'en-US'))
data = [t['text'] for t in transcript]

# Removing non-alphanumeric characters and accepting Turkish Charact`ers
data = [re.sub(r"[^a-zA-Z0-9]", "", line) for line in data]
# Define the search word wanted
search_word = "AFL"

time = []
for i, line in enumerate(data):
    if search_word in line:
        start_time = transcript[i]['start']
        time.append(start_time)

print_time(search_word, time)