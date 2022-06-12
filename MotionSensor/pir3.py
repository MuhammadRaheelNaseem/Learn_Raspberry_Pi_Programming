from gpiozero import MotionSensor

pir = MotionSensor(4)

print("Waiting for the sensor to settle")

pir.wait_for_motion()
print("Someone is here!")

pir.wait_for_no_motion()
print("No one is here!")