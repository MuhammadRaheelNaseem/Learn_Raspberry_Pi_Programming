from gpiozero import OutputDevice
import time

relay = OuputDeveice(4, active_high=False, initial_value=True)

while 1:
    relay.on()
    time.sleep(1)
    relay.off()
