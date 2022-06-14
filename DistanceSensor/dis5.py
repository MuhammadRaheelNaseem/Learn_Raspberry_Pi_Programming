from gpiozero import DistanceSensor

dis = DistanceSensor(echo=17, trigger=4)

def hello():
    print("Hello")

def bye():
    print("Bye")

dis.when_in_range = hello

dis.when_out_of_range = bye