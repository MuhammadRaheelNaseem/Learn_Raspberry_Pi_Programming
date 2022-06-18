import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
IR_PIN = 40
Buzzer_Pin = 38
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(Buzzer_Pin, GPIO.OUT)
GPIO.setwarnings(False)

while True:
    not_got_something = GPIO.input(IR_PIN)
    if not_got_something==0:
        GPIO.output(Buzzer_Pin, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(Buzzer_Pin, GPIO.LOW)
        time.sleep(1)
