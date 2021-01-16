import pytube

print('Just put a url here and let me take the rest')

url = input('url:' )

youtube = pytube.YouTube(url)

video = youtube.streams.get_highest_resolution()

video.download()
