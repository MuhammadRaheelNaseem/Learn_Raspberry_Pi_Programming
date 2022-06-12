import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN) #PIR
GPIO.setup(26, GPIO.OUT) #BUzzer
try:
    #time.sleep(2) # to stabilize sensor
    x = 0
    while True:
        if GPIO.input(4):
            x += 1
            GPIO.output(26, True)
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
            GPIO.output(26, False)
            print("Motion Detected..."+ "\n" + "Total detections : {}".format(x))
            time.sleep(1) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()