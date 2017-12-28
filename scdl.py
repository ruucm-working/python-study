import webbrowser
import urllib
import urllib.request
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import mutagen.id3
import time
import soundcloud
import sys
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
client = soundcloud.Client(client_id='761LMfrpB07DQlPhf7rbKo5fLsBuMaKH') # create client access
next = True

def downloadTrack(): # called in 'running code'
	global filename	# set to global to access it in more areas

	trackUrl = input("trackUrl:") # ask for info in console
	artist = input("artist:")
	title = input("title:")
	filename = artist + " - " + title + ".mp3"
	
	track = client.get('/resolve', url=trackUrl) # resolve track data for url
	api_key = "761LMfrpB07DQlPhf7rbKo5fLsBuMaKH" # your api key
	stream_link = "https://api.soundcloud.com/tracks/"+ str(track.id) + "/stream?client_id=" + api_key
	logging.info('I told you so')
	logging.info(stream_link)
	logging.info(filename)
	urllib.request.urlopen(stream_link) # this downloads the song
	# urllib.urlretrieve(stream_link, filename, reporthook=dlProgress) # this downloads the song
	data = response.read()      # a `bytes` object
	text = data.decode('utf-8') # a `str`; this step can't be used if data is binary

	addTags(filename, title, artist)

def addTags(filename, title, artist): # called in downloadTrack() function
	audio = MP3(filename, ID3=EasyID3) # MP3 tags for better overview on phone etc
	audio["title"] = title
	audio["artist"] = artist
	audio.save()

def dlProgress(soFar, blockSize, totalSize): # tracks progress
      percent = int((soFar*blockSize*100/totalSize)/4) # if 100 too big so /4
      sys.stdout.write("\r" + filename+ " ")
      for i in range(0,25):
      	if i < percent:
      		 sys.stdout.write("#")	
      	else:
      		sys.stdout.write("_")
      sys.stdout.write("..." + str(percent*4)+ "%")
      sys.stdout.flush()

# everything starts here
while (next): # while next == True
	next = False # set next to False
	downloadTrack()												                            			
	print ('\nfinished downloading: ' + filename)
	next = bool(input("more? y/n")=="y") # set next to True if yes

print ('Done Running')