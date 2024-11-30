from pytubefix import YouTube
from pytubefix.cli import on_progress
 
# url = "https://www.youtube.com/watch?v=j64SctPKmqk"
# url = "https://www.youtube.com/watch?v=KKU6gs_s_0Y"
 
url = "https://www.youtube.com/shorts/GHQ4j0alPy4"

yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
 
ys = yt.streams.get_highest_resolution()
ys.download()