import sys
import xbmcgui
import xbmcplugin
import requests
from urllib.parse import parse_qs

# সেটিংস
HANDLE = int(sys.argv[1])
# আপনার গিটহাবের RAW জেসন লিঙ্ক এখানে দিন
JSON_URL = "https://raw.githubusercontent.com/Habib4326/hdhub4u/main/movies.json"

def get_remote_data():
    """গিটহাব থেকে মুভি লিস্ট ডাউনলোড করা"""
    try:
        response = requests.get(JSON_URL)
        return response.json()
    except:
        return []

def add_directory_item(movie):
    """জেসন ডাটা থেকে মেনু আইটেম তৈরি"""
    name = movie.get('name')
    url = f"{sys.argv[0]}?action=play&video_url={movie.get('url')}"
    
    list_item = xbmcgui.ListItem(label=name)
    list_item.setArt({
        'thumb': movie.get('thumbnail'),
        'icon': movie.get('thumbnail'),
        'fanart': movie.get('fanart')
    })
    list_item.setInfo('video', {'title': name})
    list_item.setProperty('IsPlayable', 'true')
    
    xbmcplugin.addDirectoryItem(HANDLE, url, list_item, isFolder=False)

def play_video(video_url):
    """ভিডিও প্লে করা"""
    play_item = xbmcgui.ListItem(path=video_url)
    xbmcplugin.setResolvedUrl(HANDLE, True, listitem=play_item)

# মেইন লজিক (Router)
params = parse_qs(sys.argv[2][1:])
action = params.get('action', [None])[0]

if action is None:
    # গিটহাব থেকে ডাটা এনে লিস্ট দেখানো
    movies = get_remote_data()
    for movie in movies:
        add_directory_item(movie)
    xbmcplugin.endOfDirectory(HANDLE)

elif action == 'play':
    video_url = params.get('video_url', [None])[0]
    play_video(video_url)