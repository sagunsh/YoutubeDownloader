from pytube import YouTube
from pytube import exceptions

def download_video(url, filename, path):
	yt = YouTube(url)

	# Show the default video name
	print('Default filename:',yt.filename)

	# Set name for the video
	yt.set_filename(filename)

	# Show the list of available formats
	print('\nAvailable formats')
	[print(vids) for vids in yt.get_videos()]

	try:
		video = yt.get('mp4', '1040p')
	except exceptions.DoesNotExist:
		video = yt.get('mp4', '720p')

	# Download video to the path
	video.download(path)


if __name__ == '__main__':
	path = '/home/sagunsh/Desktop'
	url = 'https://www.youtube.com/watch?v=QqWfZseQtoY'
	filename = 'Tungnako Dhoon Ma (cover) by Prayatna Shrestha'

	download_video(url,filename,path)
	print('\nDownload Successful')