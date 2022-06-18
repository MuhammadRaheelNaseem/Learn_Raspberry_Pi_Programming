import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.IN)

while 1:
    state=GPIO.input(40)
    if state==False:
        time.sleep(1)
    else:
        print("Object Detected")
        time.sleep(1)
