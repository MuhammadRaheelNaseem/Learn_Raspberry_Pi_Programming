from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(4)

def motion():
    print("In time, Someone has Joined")
def no_motion():
    print("Out time, Someone has left")

print("Waiting for sensor to settle")

pir.when_motion = motion
pir.when_no_motion = no_motion
pause()

