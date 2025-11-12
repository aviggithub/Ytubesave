from pytubefix import YouTube
from pytubefix.cli import on_progress  # optional for progress
yt = YouTube('https://www.youtube.com/watch?v=A0nnD9abDBAhfhfhfhfhfgh', on_progress_callback=on_progress)
yt.streams.get_highest_resolution().download()
print("Download Complete!")