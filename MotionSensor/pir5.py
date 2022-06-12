from gpiozero import MotionSensor
from signal import pause
import time

pir = MotionSensor(4)

def motion():
    print("In time, Someone has Joined")

print("Waiting for sensor to settle")

pir.when_motion = motion
while 1:
    print("Stop!")
    time.sleep(1)
pause()