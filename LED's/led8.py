import RPi.GPIO as GPIO
import time
led = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

for i in range(10):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.4)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.4)
GPIO.cleanup()