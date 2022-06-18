import sys
import RPi.GPIO as GPIO
from time import sleep

def main(argv):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT)
	GPIO.output(25, True)
	sleep(1)
	GPIO.output(25, False)
	sleep(1)
	GPIO.output(25, True)
	sleep(2)
	GPIO.output(25, False)
	GPIO.cleanup()
	return 0

if __name__ == "__main__":
	main(sys.argv[1:])
