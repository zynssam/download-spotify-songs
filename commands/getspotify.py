import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getspotipysongs(playlistid):
    client_id = '' #Enter The Client Id
    client_secret = '' #Enter The Client Secret
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    playlist_id = playlistid

    playlist = sp.playlist_tracks(playlist_id)

    track_names = [item['track']['name'] for item in playlist['items']]

    return(track_names)







