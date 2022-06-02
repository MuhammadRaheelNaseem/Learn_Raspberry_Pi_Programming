import RPi.GPIO as GPIO
import time
led1 = 5
led2 = 3
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
while True:
    GPIO.output(led1,GPIO.HIGH)
    #print("BCM is Running!")
    time.sleep(1)
    GPIO.output(led1,GPIO.LOW)
    time.sleep(1)
    GPIO.output(led2,GPIO.HIGH)
    #print("BOARD is Runining!")
    time.sleep(2)
    GPIO.output(led2,GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()

