pip install pushbullet.py==0.9.1
from pushbullet import Pushbullet
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)#Numbering the GPIO pin
GPIO.setwarnings(False)
GPIO_TRIGGER = 24
GPIO_ECHO = 23
pulse_start=0
pulse_end=0
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) #GPIO Mapping 
GPIO.setup(GPIO_ECHO,GPIO.IN)
pb = Pushbullet("o.t8XGOI0l8fEuYdqerwYs0vAHtQ2kCkMu") # your access token
print(pb.devices)

while True:
    try:
        # Reading the motion sensor pin state
        pin_state = GPIO.input(sensor_pin)
        if pin_state==0:                 #When output from motion sensor is LOW
            print("Body Not Detected",pin_state)
            sleep(0.5)

        elif pin_state==1:               #When output from motion sensor is HIGH
            print("Body Detected",pin_state)
            dev = pb.get_device('INFINIX MOBILITY LIMITED Infinix X650B')
            push = dev.push_note("Alert!!", "Body Detected In Our Range")
            sleep(1)

    except KeyboardInterrupt:
        GPIO.cleaup()