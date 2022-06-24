from gpiozero import LightSensor

ldr = LightSensor(4)  # alter if using a different pin

while True:
    print(ldr.value)
