import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LIGHT_PIN = 2
GPIO.setup(LIGHT_PIN, GPIO.IN)

sense = not GPIO.input(LIGHT_PIN)
print('Starting up the LIGHT Module (click on STOP to exit)')
time.sleep(0.5)

while True:
  if GPIO.input(LIGHT_PIN) != sense:
    if GPIO.input(LIGHT_PIN):
      print('MOON: \u263e')
    else:
      print ('SUN: \u263c') 
  sense = GPIO.input(LIGHT_PIN)
  time.sleep(0.2)
