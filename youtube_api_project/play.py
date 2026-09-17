import subprocess
from googleapiclient.discovery import build

API_KEY = "AIzaSyDCXFE_-WH2pERMNVNR9DXlEN6lyWHQkdw"
SEARCH_QUERY = "rap music to listen to in the background"

def get_best_video_url(query):
	youtube = build('youtube', 'v3', developerKey=API_KEY)
	request = youtube.search().list(
		q=query,
		part='snippet',
		maxResults=1,
		type='video'
	)
	response = request.execute()
	
	items = response.get('items',[])
	if not items:
		print ("No Videos Found.")
		return None

	video_id = items[0]['id']['videoId']
	video_title = items[0]['snippet']['title']
	print(f"Best Match Found: {video_title}")
	
	return f"https://youtube.com/watch?v={video_id}"

def play_video(url):
    if not url:
        return

    print("Opening media player...")
    subprocess.run([
        "mpv",
        "--hwdec=no",
        url
    ])
if __name__ == '__main__':
	video_url = get_best_video_url(SEARCH_QUERY)
	play_video(video_url)
