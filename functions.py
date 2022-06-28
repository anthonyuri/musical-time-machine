import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "2fc3dca3c4f7427fb9c6f32de2a4be4f"
CLIENT_SECRET = "aa9720fb879f4ea8afba52ccd19c8e3f"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private"))

user = sp.current_user()
print(user)
user_id = user["id"]
print(user_id)





# sp.user_playlist_create(user=user_id, name=)

