<div class="jumbotron alert-info"><h1>4.) PIR Motion Sensor (Passive Infrared Ray Sensor)</h1></div>

![image](https://user-images.githubusercontent.com/63813881/173230581-f55cdf18-1454-443e-be13-a5be7d7903b3.png)
![image](https://user-images.githubusercontent.com/63813881/173230594-3fbf962d-7447-403d-81b3-ff32cfdacd20.png)

# `How PIR Motion Sensor Works:`
![image](https://user-images.githubusercontent.com/63813881/173230605-36808b74-8dbe-43f4-a2f0-cb38072bfa80.png)

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
# `Goto this link` https://dashboard.nexmo.com/sign-up ` click Try Now Button`

<!-- ![image-6.png](attachment:image-6.png) -->
![image](https://user-images.githubusercontent.com/63813881/173230619-c8057ba2-dcb4-4f5e-b34f-d0d1fac33e31.png)

# `After filling all requirement press signup, Then Login and select communication API`

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
client = vonage.Client(key="f9xxxxxx", secret="5ahmSsxxxxxxxxxx") 
sms = vonage.Sms(client)

# Function to send message
def send_sms():
    # Sending the message
    responseData = sms.send_message({
                                        "from": "IOT",
                                         "to": "923172144424",
                                         "text": "Motion Detected!",
                                    })
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

# `goto this link` https://www.pushbullet.com/ `signup and then login`
![image](https://user-images.githubusercontent.com/63813881/173230659-30dc0321-e00d-43b6-bb6c-dcc0b3dc86b2.png)
# `click setting button`
![image](https://user-images.githubusercontent.com/63813881/173230666-bf09e22c-88e2-4cd4-bae3-2f1f76d1a8ff.png)
# `then scroll down you can see "Change Access Token" click here`
![image](https://user-images.githubusercontent.com/63813881/173230679-a9d7d438-149d-4d17-b150-364522596331.png)
# `After the click "Change Access Token" API will be generate like this:`
![image](https://user-images.githubusercontent.com/63813881/173230684-1e74c363-6215-426b-bde7-467831b3dcd0.png)
# `Code: 9`
<pre>
import smtplib, ssl
from gpiozero import MotionSensor

pir = 2 # gpio pin number


def mail():
    print("Motion Detected!")
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "Your Gmail | Other Email Address"
    password = "Your Gmail Password"
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be comitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be comitted
        server.login(sender_email, password)
        print("Successfully login") 
        subject="mail from Raspberry Pi "
        body="Motion Has Been Detected!"
        message="Subject: {}\n\n{}".format(subject,body)
        address=['mrahilnasim@gmail.com']
        server.sendmail("johnmalton734",address,message)
        print('Mail send successfully')
    except Exception:
        print("Login Failed")
        print("Try to enter correct password")
    finally:
        print('Server Has Been Successfully Close')
        server.quit() 

def no_mail():
    print("No Motion Detected!")
        
pir.when_motion = mail
pir.when_no_motion = no_mail
</pre>

# `Code: 10`
<pre>
from pushbullet import Pushbullet
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) 
pb = Pushbullet("o.t8XGOI0l8fEuYdqerxxxxxxxxxxxxxxx") # your access token
print(pb.devices)

while True:
    i = GPIO.input(11)
    if i == 0:
        print("no motion")
        sleep(1)
    elif i == 1:
        print("motion")
        
        dev = pb.get_device('INFINIX MOBILITY LIMITED Infinix X650B')
        push = dev.push_note("Alert!!", "Someone is in your house")
        sleep(1)
</pre>
