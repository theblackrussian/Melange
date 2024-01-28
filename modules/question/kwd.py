from youtube_transcript_api import YouTubeTranscriptApi as yta
import re
import sys

class YouTubeTranscriptProcessor:
    def __init__(self, video_id, language=('en', 'en-US')):
        self.video_id = video_id
        self.language = language
        self.transcript = self._fetch_transcript()
        self.cleaned_data = self._clean_data()

    def _fetch_transcript(self):
        return yta.get_transcript(self.video_id, languages=self.language)

    def _clean_data(self):
        return [re.sub(r"[^a-zA-Z0-9]", "", t['text']) for t in self.transcript]

    def search_word(self, search_word):
        time_mentions = []
        for i, line in enumerate(self.cleaned_data):
            if search_word.lower() in line.lower():
                start_time = self.transcript[i]['start']
                time_mentions.append(start_time)
        return time_mentions

    def print_time(self, search_word, time_mentions):
        print(f"'{search_word}' was mentioned at:")
        for t in time_mentions:
            hours, minutes, seconds = self._convert_time(t)
            print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    def _convert_time(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return hours, minutes, seconds

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    video_id = video_url.split("watch?v=")[-1]

    # Now that we've handled the video URL, we can proceed with the rest
    transcript_processor = YouTubeTranscriptProcessor(video_id)
    search_word = input("Search keyword: ")
    time_mentions = transcript_processor.search_word(search_word)
    transcript_processor.print_time(search_word, time_mentions)