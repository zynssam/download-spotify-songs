import commands.getspotify as getspotify 
import commands.getytlinks as getlinks
import commands.download as download
import commands.enterlink as enterlink

folder_location = r'' #Your Folder Location
def get_spotify_playlist_id(url):
    parts = url.split('/')
    
    if 'playlist' in parts:
        return parts[parts.index('playlist') + 1].split('?')[0]
    return None

def download_tracks():
    url = linkgetter.create_url_input_app()

    track_names = getspotify.getspotipysongs(get_spotify_playlist_id(url), )
    for track_name in track_names:
        try:
            yt_link = getlinks.get_youtube_link(track_name)
            if yt_link:
                print(f"Downloading: {track_name} from {yt_link}")
                download.download_audio(yt_link, folder_location)
                print(f"Downloaded: {track_name}")
            else:
                print(f"No YouTube link found for: {track_name}")
        except Exception as e:
            print(f"Error downloading {track_name}: {e}")


if __name__ == "__main__":
    download_tracks()
