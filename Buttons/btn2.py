from gpiozero import Button
import time

button = Button(2)

counter = 0
while 1:
    counter = counter + 1
    button.wait_for_press()
    print("You have press the button is: %s"%(counter))
    time.sleep(1)