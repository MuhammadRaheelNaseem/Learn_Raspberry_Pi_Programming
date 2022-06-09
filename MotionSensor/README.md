<div class="jumbotron alert-info"><h1>4.) PIR Motion Sensor (Passive Infrared Ray Sensor)</h1></div>

![image](https://user-images.githubusercontent.com/63813881/172776786-54859834-0933-4d81-8343-3b80b1b05464.png)
![image](https://user-images.githubusercontent.com/63813881/172776801-ba84b683-dfef-49cf-b8fe-439f1e278b69.png)
# `How PIR Motion Sensor Works:`
![image](https://user-images.githubusercontent.com/63813881/172776832-6beb3825-e58d-41fb-b549-e7584e2db3d2.png)

# `Code: 1`
<pre> 
from gpiozero import MotionSensor
import time

pir = MotionSensor(2)

while True:
    if pir.motion_detected:
        print("Motion Detected!")
    else:
        print("No Motion Detected!")
</pre>

# `Code: 2`
<pre> 
from gpiozero import MotionSensor

pir = MotionSensor(2)

print("Waiting for the sensor to settle")

pir.wait_for_motion()
print("Someone is here!")

pir.wait_for_no_motion()
print("No one is here!")
</pre>

# `Code: 3`
<pre> 
from gpiozero import MotionSensor
import time 

pir = MotionSensor(2)

while True:
    print("Waiting for the sensor to settle")

    pir.wait_for_motion()
    print("Someone is here!")
    time.sleep(1)
    pir.wait_for_no_motion()
    print("No one is here!")
    time.sleep(1)
</pre>

# `Code: 4`
<pre>
form gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(4)

def motion():
    print("In time, Someone has Joined")
    
def no_motion():
    print("Out time, Someone has left")
    
print("Waiting for sensor to settle")

pir.when_motion = motion

pir.when_no_motion = no_motion

pause()
</pre>

# `Code: 5`
<pre>
from gpiozero import MotionSensor, LED
from signal import pause

pir = MotionSensor(4)
led = LED(16)

pir.when_motion = led.on
pir.when_no_motion = led.off

pause()
</pre>

# `Code: 6`

<pre>
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(24, GPIO.OUT) #BUzzer

try:
    time.sleep(2) # to stabilize sensor
    x = 0
    while True:
        if GPIO.input(23):
            x += 1
            GPIO.output(24, True)
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
            GPIO.output(24, False)
            print("Motion Detected..."+ "\n" + "Total detections : {}".format(x))
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()
</pre>

# `Code: 7`
<pre>
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin

while True:
    i=GPIO.input(11)
    if i==0:                 #When output from motion sensor is LOW
        print("No Detected ",i)
        GPIO.output(3, 0)  #Turn OFF LED
        time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        print("Detected ",i)
        GPIO.output(3, 1)  #Turn ON LED
        time.sleep(0.1)
</pre>

# `Before working first we need API like (SMS, Calling, Whatsapp Message, `
# `OTP, )`
# `Goto this link` https://www.vonage.com/ ` click Try Now Button`

![image](https://user-images.githubusercontent.com/63813881/172776901-e2d14d0c-1197-4665-bc9f-ee7c0d0533b5.png)

# `Then Sign up or login and select communication API` 


# `Code: 8`
<pre>
        
import vango  # Importing the nexmo library
import RPi.GPIO as GPIO
from time import sleep

sensor_pin = 17		# Initialized GPIO 17 for motion sensor
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)         # Declared GPIO 17 as input pin

# Connecting to the vonago using API key and API secret
client = vonage.Client(key=" Enter Your API Key ", secret=" Enter Your Secret Key ") 
sms = vonage.Sms(client)


# Function to send message
def send_sms():
    # Sending the message
    responseData = sms.send_message(
                                    {
                                        "from": "IOT",
                                         "to": " Enter Receiver Contact Number ",
                                         "text": "Motion Detected!",
                                    }
                                    )
    # Checking whether we are successful or we got a error
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")

while True:
    try:
        # Reading the motion sensor pin state
        pin_state = GPIO.input(sensor_pin)
        if pin_state==0:                 #When output from motion sensor is LOW
            print("Body Not Detected",pin_state)
            sleep(0.1)
            
        elif pin_state==1:               #When output from motion sensor is HIGH
            print("Body Detected",pin_state)
            send_sms()
            sleep(5)
    except KeyboardInterrupt:
        GPIO.cleaup()
</pre>
