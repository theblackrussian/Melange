#!/usr/bin/env python3
import sys
from youtube_transcript_api import YouTubeTranscriptApi
import os


class YouTubeTranscriptFetcher:
    def __init__(self):
        self.filepath = "/Users/tonda/Documents/Melange/modules/youtube/transcripts/"

    def fetch_transcripts(self, video_ids):
        try:
            transcripts, _ = YouTubeTranscriptApi.get_transcripts(
                video_ids, languages=["en", "en-US"]
            )
            return transcripts
        except Exception as e:
            print(f"Failed to fetch transcripts: {e}")
            return {}

    def save_transcripts(self, transcripts):
        for index, (video_id, transcript) in enumerate(transcripts.items(), start=1):
            filename = f"{video_id}.txt"
            with open(
                os.path.join(self.filepath, filename), "w", encoding="utf-8"
            ) as f:
                for line in transcript:
                    f.write(line["text"] + "\n")
            print(f"Transcript for video ID {video_id} saved as {filename}")


if __name__ == "__main__":
    # Check if there is piped input
    if not sys.stdin.isatty():
        clipboard_content = sys.stdin.read().strip()
        video_urls = clipboard_content.split(",")
        video_ids = [url.split("watch?v=")[-1] for url in video_urls]

        # Create an instance of the fetcher and use it
        fetcher = YouTubeTranscriptFetcher()
        transcripts = fetcher.fetch_transcripts(video_ids)

        if transcripts:
            fetcher.save_transcripts(transcripts)
        else:
            print("No transcripts were fetched.")
    else:
        print("No input provided.")
