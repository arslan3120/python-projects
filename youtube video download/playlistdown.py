from pytube import Playlist

py = Playlist("url")
print(f'Downloading : {py.title}')

for video in py.videos:
    video.streams.first().download()
