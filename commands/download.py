import yt_dlp
import os

def download_audio(link,folder):
    download_path = rf'{folder}'  

    if not os.path.exists(download_path):
        os.makedirs(download_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  
            'preferredquality': '192',  
        }],
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  
        'noplaylist': True,  
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    video_link = 'https://www.youtube.com/watch?v=quyne48QRK4'
    download_audio(video_link)