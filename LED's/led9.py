import RPi.GPIO as GPIO
import time

led2 = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led2, GPIO.OUT)

while True:
 
    GPIO.output(led2,GPIO.HIGH)
    print("BOARD is Runining!")
    time.sleep(2)
    GPIO.output(led2,GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()