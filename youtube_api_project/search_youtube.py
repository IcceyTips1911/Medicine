import os 
from googleapiclient.discovery import build

API_KEY = "AIzaSyDCXFE_-WH2pERMNVNR9DXlEN6lyWHQkdw"

def youtube_search(query):
	youtube = build("youtube", "v3", developerKey=API_KEY)
	
	request = youtube.search().list(
		q=query,
		part="snippet",
		type="video",
		maxResults=3
	)

	response = request.execute()
	
	for item in response.get("items",[]):
		title = item["snippet"]["title"]
		video_id = item["id"]["videoId"]
		print(f"Title: {title}")
		print(f"URL: https://www.youtube.cxom/watch?v={video_id}\n")

if __name__ == "__main__":
	youtube_search("Soft sounds")
