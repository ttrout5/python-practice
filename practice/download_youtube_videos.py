import pytubefix
print(pytubefix.__version__)

from pytubefix import YouTube

url = "https://www.youtube.com/watch?v=nn_0zPAfyo8"
yt = YouTube(url)

yt.title

print(yt.length)
print(yt.author)
print(yt.publish_date)
print(yt.views)

stream = yt.streams.get_highest_resolution()
stream.download()

stream = yt.streams.filter(res="1080p").first()
stream.download(filename="1080p_format.mp4")
