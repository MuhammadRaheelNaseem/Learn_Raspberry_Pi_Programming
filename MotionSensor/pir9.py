import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(37, GPIO.OUT)         #LED output pin

while True:
    i=GPIO.input(7)
    if i==0:                 #When output from motion sensor is LOW
        print("No Detected ",i)
        GPIO.output(37, 0)  #Turn OFF LED
        time.sleep(0.8)
    elif i==1:               #When output from motion sensor is HIGH
        print("Detected ",i)
        GPIO.output(37, 1)  #Turn ON LED
        time.sleep(0.8)