from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Put your NEW YouTube API key here
API_KEY = "AIzaSyDCXFE_-WH2pERMNVNR9DXlEN6lyWHQkdw"


def youtube_search(query):
    try:
        youtube = build(
            "youtube",
            "v3",
            developerKey=API_KEY
        )

        response = youtube.search().list(
            part="snippet",
            q=query,
            type="video",
            maxResults=3
        ).execute()

        videos = response.get("items", [])

        print(f"\nVideos found: {len(videos)}\n")

        if not videos:
            print("No videos found.")
            return

        for number, item in enumerate(videos, start=1):
            title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            url = f"https://www.youtube.com/watch?v={video_id}"

            print(f"{number}. {title}")
            print(f"   {url}")
            print("-" * 60)

    except HttpError as error:
        print("YouTube API error:")
        print(error)
