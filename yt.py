from pytube import YouTube
from pytube.cli import on_progress #this module contains the built in progress bar. 
while True:
	link=input('enter url:')
	yt=YouTube(link,on_progress_callback=on_progress)
	videos=yt.streams.filter(res="720p").first()
	videos.download()
	print("(:")
