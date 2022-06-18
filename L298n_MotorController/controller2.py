import RPi.GPIO as GPIO
import time

forward = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(forward, GPIO.OUT)

while True:
    GPIO.output(forward,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(forward,GPIO.LOW)
    time.sleep(2)
