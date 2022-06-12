from gpiozero import MotionSensor
import time 

pir = MotionSensor(4)

while True:
    print("Waiting for the sensor to settle")

    pir.wait_for_motion()
    print("Someone is here!")
    time.sleep(1)
    pir.wait_for_no_motion()
    print("No one is here!")
    time.sleep(1)