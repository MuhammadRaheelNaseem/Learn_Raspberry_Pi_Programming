import RPi.GPIO as GPIO
import time
led1 = 21
led2 = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)

while True:
    GPIO.output(led1,GPIO.HIGH)
    print("BCM is Running!")
    GPIO.output(led1,GPIO.LOW)
    
    GPIO.output(led2,GPIO.HIGH)
    print("BOARD is Runining!")
    time.sleep(2)
    GPIO.output(led2,GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()
