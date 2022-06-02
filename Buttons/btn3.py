from gpiozero import Button

button = Button(2)


button.wait_for_press()
print("You have press the button")


button.wait_for_release()
print("you have release the Button")