import RPi.GPIO as gp  
from time import sleep 
gp.setmode(gp.BOARD)  
gp.setup(12,gp.IN)  
gp.setup(32,gp.OUT)  
gp.setup(36,gp.OUT)  
while True:  
    print(not gp.input(12))  
    gp.output(32,not gp.input(12))  
    gp.output(36,not gp.input(12))
