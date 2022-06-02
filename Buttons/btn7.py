import time
import RPi.GPIO as GPIO
# Pins definitions
btn_pin = 2
# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN)
# If button is pushed, msg will print
try:
    while True:
        if GPIO.input(btn_pin):
            print("Button is not pressed!")
        else:
            print("Button is pressed!")
# When you press ctrl+c, this will be called
finally:
    GPIO.cleanup()