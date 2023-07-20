import youtube_dl
from youtube_dl import std_headers
import ssl

ssl._create_default_https_context = ssl._create_default_https_context = ssl._create_unverified_context


def Download(link):
    ydl_opts = {
        'format' : 'best',
        'outtmpl' : 'downloads/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


youtube_link = input("Enter the YouTube video URL: ")
Download(youtube_link)
print("Download complete!")