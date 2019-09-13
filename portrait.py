#!/usr/bin/env python3
#Original created by scarethetots
#Heavily modified by dtsek

import sys
import datetime
from os import system
from ultrasonic import *	#custom script for distance measurements
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
from picamera import PiCamera

# path of the scary video
scaryVideo = '/home/pi/Desktop/projectScaryPortrait/lovelyLady/UP_Lady_LivingNightmare_TV_V.mp4'

# path to save the taken videos
videosDir ='/home/pi/Desktop/projectScaryPortrait/videos/'

# omxplayer parameters
slength = 1920
swidth = 1080

# create camera object and parameters
camera = PiCamera()
camera.resolution = (1280, 720)	#default is monitor resolution or 1280*720
camera.framerate = 20		#default is 30
camera.rotation = 270

# minumux distance for video trigger
minDistance = 80

# for debugging
print("Starting up....")
tgr = 0

try:
	VIDEO_PATH = Path(scaryVideo)
	player = OMXPlayer(VIDEO_PATH,  args=['--no-osd', '--loop', '--win', '0 0 %d %d' % (slength, swidth)])
	sleep(1)
	print("Ready to trigger")
	while True:
		player.pause()
		if distance() < minDistance:
			# for debugging
			print("trigger count %d" % tgr)
			# create unique filename
			now = datetime.datetime.now()
			timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
			# core actions
			camera.start_recording(videosDir + timestamp + '.h264')
			sleep(1)
			player.play()
			sleep(player.duration())
			camera.stop_recording()
			#for debugging
			tgr = tgr + 1
		else:
			pass
		player.set_position(0.0)

except KeyboardInterrupt:
	player.quit()
	sleep(1)
	cleanPins()
	exit()
