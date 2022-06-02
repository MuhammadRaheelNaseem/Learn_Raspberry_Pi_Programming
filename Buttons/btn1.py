from gpiozero import Button
import time

button = Button(2)

count = 0
while True:
    count+=1
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
    time.sleep(1)
    print(count)