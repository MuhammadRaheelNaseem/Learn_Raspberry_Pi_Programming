from gpiozero import LED
from time import sleep

led = LED(17)

led.on()
print("Led is ON")
sleep(3)

led.off()
print("LED off")