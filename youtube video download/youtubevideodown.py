from pytube import YouTube

link = ""
youtube_1 = YouTube(link)
#For All format
videos = youtube_1.streams.all
#For only audio
videos = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(videos))
for i in vid:
    print(i)

strm = int(input("enter : "))
videos[strm].download()
print("Sucessfully")

#video thumbnail
print(youtube_1.thumbnail_url)

#print video title
print(youtube_1.title)



