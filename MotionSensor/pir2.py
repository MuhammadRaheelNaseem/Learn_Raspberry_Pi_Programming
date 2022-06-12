from gpiozero import MotionSensor

pir = MotionSensor(4)

print("Waiting for the sensor to settle")

pir.wait_for_motion()
print("Someone is here!")