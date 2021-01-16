import pytube

url = input('url:' )

youtube = pytube.YouTube(url)

video = youtube.streams.get_highest_resolution()

video.download()
