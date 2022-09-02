from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint as p
import os

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{date}"


# get top 100 songs from date into list
# URL = "https://www.billboard.com/charts/hot-100/2000-08-12"

response = requests.get(URL)

website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

song_title_tags = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")

songs_list = [song.getText().strip() for song in song_title_tags]



CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))

user = sp.current_user()
user_id = user["id"]



song_uris = []
year = 2000
# year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", description=f"Top 100 trending songs in {date}", public=False)

print(playlist)

sp.playlist_add_items(playlist['id'], song_uris, position=None)

