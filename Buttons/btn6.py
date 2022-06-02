import time
import RPi.GPIO as GPIO
# Pins definitions
btn_pin = 2
# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN)

while True:
    GPIO.input(btn_pin)
    print("Button is Pressed!")
    time.sleep(1)
GPIO.cleanup()


