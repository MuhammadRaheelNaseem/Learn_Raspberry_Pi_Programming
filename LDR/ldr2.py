from gpiozero import LED, MotionSensor, LightSensor
from signal import pause
pir = MotionSensor(21)
ldr = LightSensor(26)
light = LED(25)
def daytime():
    pir.when_motion = None
    pir.when_no_motion = None
    light.off()
def nighttime():
    pir.when_motion = light.on
    pir.when_no_motion = light.off
ldr.when_light = daytime
ldr.when_dark = nighttime
pause()
