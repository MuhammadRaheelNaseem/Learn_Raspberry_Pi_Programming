from gpiozero import DistanceSensor, Buzzer

ultrasonic = DistanceSensor(echo=20, trigger=26)
buz = Buzzer(2)
while True:
    ultrasonic.wait_for_in_range()
    buz.on()
    print("In range")
    ultrasonic.wait_for_out_of_range()
    buz.off()
    print("Out of range")