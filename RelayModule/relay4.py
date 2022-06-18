import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(4, GPIO.OUT) #set Relay 1 output
GPIO.setup(17, GPIO.OUT) #set Relay 2 output

while True:
    GPIO.Output(4,HIGH)
    GPIO.Output(17,HIGH)
    time.sleep(3)
    GPIO.Ouput(4,LOW)
    GPIO.Ouput(17,LOW)
    time.sleep(3)
