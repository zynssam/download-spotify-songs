import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getspotipysongs(playlistid):
    client_id = '34d8782d5d5f41afae8ced9ff432cfbc'
    client_secret = '755d95dfc54a4b758d2a319e700fb836'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    playlist_id = playlistid

    playlist = sp.playlist_tracks(playlist_id)

    track_names = [item['track']['name'] for item in playlist['items']]

    return(track_names)







