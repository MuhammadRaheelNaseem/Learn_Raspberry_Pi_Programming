from gpiozero import Buzzer
from time import sleep

buz = Buzzer(17)

buz.on()
sleep(1)
buz.off()
sleep(1)
