from gpiozero import DistanceSensor, Buzzer
from signal import pause
dis = DistanceSensor(echo=20, trigger=26,threshold_distance=0.5)
buz = Buzzer(2)
def hello():
    print("Hello")
    print("%.3f"%dis.distance)
    buz.on()
def bye():
    print("Bye")
    print("%.3f"%dis.distance)
    buz.off()
dis.when_in_range = hello
dis.when_out_of_range = bye
pause()