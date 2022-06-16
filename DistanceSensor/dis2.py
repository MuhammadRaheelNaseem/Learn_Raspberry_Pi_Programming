from gpiozero import DistanceSensor

dis = DistanceSensor(echo=20, trigger=26)

while True:
    print("%.3f"%dis.distance)