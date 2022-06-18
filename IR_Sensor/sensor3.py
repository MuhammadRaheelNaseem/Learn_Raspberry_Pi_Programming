import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN) #GPIO 14 -> IR sensor as input

while True:

    if(GPIO.input(14)==True): #object is far away
        print("No object")
    if(GPIO.input(14)==False): #object is near
        print("move the object")
