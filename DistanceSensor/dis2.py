from gpiozero import DistanceSensor

dis = DistanceSensor(echo=17, trigger=4)

while True:
    print("%.3f"%dis.distance)