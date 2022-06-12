from pushbullet import Pushbullet
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN) 
pb = Pushbullet("o.t8XGOI0l8fEuYdqerwYs0vAHtQ2kCkMu") # your access token
print(pb.devices)

while True:
    i = GPIO.input(7)
    if i == 0:
        print("no motion")
        sleep(1)
    elif i == 1:
        print("motion")

        #dev = pb.get_device('INFINIX MOBILITY LIMITED Infinix X650B')
        push = pb.push_note("Alert!!", "Someone is in your house")
        sleep(1)