from gpiozero import MotionSensor
import time

pir = MotionSensor(4)

while True:
    if pir.motion_detected:
        print("Motion Detected!")
    else:
        print("No Motion Detected!")
    time.sleep(1)
