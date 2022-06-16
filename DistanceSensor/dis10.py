#pip install pushbullet.py==0.9.1
from pushbullet import Pushbullet
import RPi.GPIO as GPIO
import time

pb = Pushbullet("o.t8XGOI0l8fEuYdqerwYs0vAHtQ2kCkMu") # your access token
print(pb.devices)

def DistanceMeasure():
    global pb
    try:
        GPIO.setmode(GPIO.BCM)
        PIN_TRIGGER = 26
        PIN_ECHO = 20
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        print("Waiting for sensor to settle")
        time.sleep(2)
        print("Calculating distance")
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        while GPIO.input(PIN_ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        distance = round(pulse_duration * 17150, 2)
        print("Distance:",distance,"cm")
        #dev = pb.get_device('INFINIX MOBILITY LIMITED Infinix X650B')
        push = pb.push_note("Alert!!", distance ,"cm")
    
    finally:
        GPIO.cleanup()
        
DistanceMeasure()