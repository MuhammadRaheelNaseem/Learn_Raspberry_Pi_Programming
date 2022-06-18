from gpiozero import OutputDevice
import time

relay = OuputDeveice(4, active_high=False, initial_value=True)

relay.on()
time.sleep(2)
relay.off()
