from gpiozero import MotionSensor, LED
from signal import pause
import time

pir = MotionSensor(4)
led = LED(21)

pir.when_motion = led.on
pir.when_no_motion = led.off

pause()