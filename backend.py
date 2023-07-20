from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_default_https_context = ssl._create_unverified_context


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occured")
    print("Download is successful")


link = input("Enter the YouTube video URL: ")
Download(link)