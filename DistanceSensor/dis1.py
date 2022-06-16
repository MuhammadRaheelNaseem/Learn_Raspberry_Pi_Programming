from gpiozero import DistanceSensor
import time

dis = DistanceSensor(echo=20, trigger=26)
while True:
    print(dis.distance)
    time.sleep(1)