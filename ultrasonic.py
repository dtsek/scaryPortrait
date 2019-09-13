#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
TRIG = 18
ECHO = 24

#set GPIO direction
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#delay for the sensor to settle
GPIO.output(TRIG,0)
time.sleep(0.1)


def distance():
   	# set Trigger to HIGH
	GPIO.output(TRIG, 1)

	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)

	startTime = time.time()
	stopTime = time.time()

	# set startTiem when ECHO goes HIGH
	while GPIO.input(ECHO) == 0:
		startTime = time.time()

	# set stopTime when ECHO is back to LOW
	while GPIO.input(ECHO) == 1:
		stopTime = time.time()

	# echo pulse lenght
	timeElapsed = stopTime - startTime
	# distance calculation
	distance = (timeElapsed * 34300) / 2

	return distance

def cleanPins():
	GPIO.cleanup()

if __name__ == '__main__':
	try:
		while True:
			dist = distance()
			print ('Measured Distance = %.1f cm' % dist)
			time.sleep(1)

		# Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print('Measurement stopped by User')
		GPIO.cleanup()
