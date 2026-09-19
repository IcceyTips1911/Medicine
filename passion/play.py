import os
import subprocess

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise RuntimeError("API_KEY was not found in .env")


SEARCH_QUERY = "rap music"


def get_best_video_url(query):
    try:
        youtube = build(
            "youtube",
            "v3",
            developerKey=API_KEY
        )

        request = youtube.search().list(
            q=query,
            part="snippet",
            maxResults=1,
            type="video"
        )

        response = request.execute()

        items = response.get("items", [])

        if not items:
            print("No videos found.")
            return None

        video_id = items[0]["id"]["videoId"]
        video_title = items[0]["snippet"]["title"]

        print(f"Best match found: {video_title}")
        print(f"Video URL: https://www.youtube.com/watch?v={video_id}")

        return f"https://www.youtube.com/watch?v={video_id}"

    except HttpError as error:
        print("YouTube API error:")
        print(error)
        return None


def play_video(url):
    if not url:
        return

    print("Opening media player...")

    try:
        subprocess.run(
            [
                "mpv",
                "--no-video",
                url
            ],
            check=True
        )

    except FileNotFoundError:
        print("MPV was not found.")
        print("Install MPV with:")
        print("sudo apt install mpv")

    except subprocess.CalledProcessError as error:
        print(f"MPV exited with an error: {error}")


if __name__ == "__main__":
    video_url = get_best_video_url(SEARCH_QUERY)
    play_video(video_url)
