# This was not used in the end because of messing with the sleeps

# Libraries
from picamera import PiCamera
from time import sleep
import datetime

def record(time):

	# get current time
	now = datetime.datetime.now()
	timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')

	# create camera object
	camera = PiCamera()

	#camera options
	#camera.rotation = 180
	#camera.resolution = (1920, 1080)
	#camera.framerate = 30
	#camera.brightness = 100
	#cameera.contrast = 1

	# start camera
	camera.start_preview()
	camera.start_recording('/home/pi/Desktop/projectScaryPortrait/videos/' + timestamp + '.h264')

	# record for time seconds
	sleep(time)

	# stop recording
	camera.stop_recording()
	camera.stop_preview()

	exit()

if __name__ == '__main__':
	time = input('Enter the amount of seconds you want to record: ')
	intTime = int(time)
	record(intTime)
