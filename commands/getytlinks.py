from youtubesearchpython import VideosSearch

def get_youtube_link(song_name):
    videos_search = VideosSearch(song_name, limit=1)
    results = videos_search.result() 

    # Check if results contain 'result' and it's not empty
    if 'result' in results and results['result']:
        # Get the first result
        video = results['result'][0]
        video_url = video['link']
        
        return (video_url)
        
    else:
        return None
        
    
if __name__ == '__main__':
    get_youtube_link('Shape of you')

