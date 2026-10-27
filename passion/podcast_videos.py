import os
import webbrowser

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY was not found in .env")


def get_best_video_url(query):
    try:
        youtube = build("youtube", "v3", developerKey=API_KEY)

        response = youtube.search().list(
            q=query,
            part="snippet",
            maxResults=1,
            type="video"
        ).execute()

        items = response.get("items", [])

        if not items:
            print("No videos found.")
            return None

        video_id = items[0]["id"]["videoId"]
        video_title = items[0]["snippet"]["title"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"

        print(f"Best match found: {video_title}")
        print(f"Video URL: {video_url}")

        return video_url

    except HttpError as error:
        print("YouTube API error:")
        print(error)
        return None


def play_video(url):
    if not url:
        return

    print("Opening YouTube in your browser...")
    webbrowser.open(url)

def tech_podcast():
    search_query = "tech podcast"
    video_url = get_best_video_url(search_query)
    play_video(video_url)

def bible_sermon():
    search_query = "bible sermon"
    video_url = get_best_video_url(search_query)
    play_video(video_url)