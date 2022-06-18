import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup(23)
GPIO.setmode(GPIO.BOARD)
i=GPIO.setup(23,GPIO.IN)
#GPIO.setup(23,GPIO.OUT)

try:
    while True:
        if i==1:
#            GPIO.output(23,1)
            print("Detected");
#            time.sleep(1)
#            GPIO.output(23,0)
except:
    print("error")
finally:
    GPIO.cleanup(23)
