<div class="jumbotron alert-info"><h1>5.) HC-SR04 Ultrasonic Distance Sensor</h1></div>

![image](https://user-images.githubusercontent.com/63813881/173551963-b8b16873-388f-407d-8e7b-7aca3008c6e9.png)
```In air, sound travels at a speed of 343 metres per second. An ultrasonic distance sensor sends out pulses of ultrasound which are inaudible to humans, and detects the echo that is sent back when the sound bounces off a nearby object. It then uses the speed of sound to calculate the distance from the object.```

# `How Distance Sensor Works:`
![image](https://user-images.githubusercontent.com/63813881/173552007-ad7d5eb0-5414-4491-9fc5-2231880f01b6.png)
<!-- ![image-5.png](attachment:image-5.png) -->

## `Circuit Diagram:`

`The circuit connects to two GPIO pins (one for echo, one for trigger), the ground pin, and a 5V pin. You’ll need to use a pair of resistors (330Ω and 470Ω) as a potential divider:`

![image](https://user-images.githubusercontent.com/63813881/173552068-4868e266-9a8f-49e7-ba21-b531fb6df5c1.png)
![image](https://user-images.githubusercontent.com/63813881/173552109-77551b45-ca6f-4afd-bb70-9aeb41e19c70.png)
## `Sensor Measurement:`
## `Max distance: 4 meters = 400 cm`
## `Min distacne: 20 mm = 0.2 cm`

# `Code: 1`
<pre>
from gpiozero import DistanceSensor

dis = DistanceSensor(echo=17, trigger=4)

while True:
    print(dis.distance)
</pre>

# `Code: 2`
<pre>
from gpiozero import DistanceSensor

dis = DistanceSensor(echo=17, trigger=4)

while True:
    print("%.3f"%dis.distance)
</pre>

# `Code: 3`

<pre>
from gpiozero import DistanceSensor

dis = DistanceSensor(echo=17, trigger=4)

while True:
    ultrasonic.wait_for_in_range()
    print("In range")
    ultrasonic.wait_for_out_of_range()
    print("Out of range")
</pre>

# `Code: 4`
<pre>
from gpiozero import DistanceSensor

# The default range threshold is 0.3m. This can be configured when the sensor is initiated:
dis = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5)

while True:
    print("%.3f"%dis.distance, ' cm')
</pre>

# `Code: 5`
<pre>
from gpiozero import DistanceSensor

dis = DistanceSensor(echo=17, trigger=4)

def hello():
    print("Hello")
 
def bye():
    print("Bye")
    
dis.when_in_range = hello

dis.when_out_of_range = bye

</pre>

# `Code: 6`
<pre>
from gpiozero import DistanceSensor
from time import sleep
import requests

server_url = 'http://localhost:9090'
threshold_distance = 0.9

#sensor = DistanceSensor(echo=18, trigger=17, threshold_distance=threshold_distance)
sensor = DistanceSensor(echo=18, trigger=17)

while True:
	#sensor.wait_for_in_range()
	r = requests.post(server_url, json={'distance': (sensor.distance * 100)});
	if r.status_code == 200:
		print('Pushed distance of ', sensor.distance * 100, ' to the server')
	else:
		print('Failed to push distance to server')
	print('Detected Distance: ', sensor.distance * 100)
        sleep(1)
</pre>

![image](https://user-images.githubusercontent.com/63813881/173552235-0bf3327d-1fe0-4710-bc4b-cddf2b7579a7.png)



# `Code: 7`
<pre>
import RPi.GPIO as GPIO                               #Import GPIO library
import time                                           #Import time library
GPIO.setmode(GPIO.BCM)                                #Set GPIO pin numbering 

TRIG = 23                                             #Associate pin 23 to TRIG
ECHO = 24                                             #Associate pin 24 to ECHO

print("Distance measurement in progress")           

GPIO.setup(TRIG,GPIO.OUT)                             #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                              #Set pin as GPIO in

while True:

  GPIO.output(TRIG, False)                            #Set TRIG as LOW
  print("Waitng For Sensor To Settle")          
  time.sleep(2)                                       #Delay of 2 seconds

  GPIO.output(TRIG, True)                             #Set TRIG as HIGH
  time.sleep(0.00001)                                 #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                            #Set TRIG as LOW

  while GPIO.input(ECHO)==0:                          #Check whether the ECHO is LOW
    pulse_start = time.time()                         #Saves the last known time of LOW pulse

  while GPIO.input(ECHO)==1:                          #Check whether the ECHO is HIGH
    pulse_end = time.time()                           #Saves the last known time of HIGH pulse 

  pulse_duration = pulse_end - pulse_start            #Get pulse duration to a variable

  distance = pulse_duration * 17150                   #Multiply pulse duration by 17150 to get distance
  distance = round(distance, 2)                       #Round to two decimal points

  if distance > 2 and distance < 400:                 #Check whether the distance is within range
    print("Distance:",distance - 0.5,"cm")            #Print distance with 0.5 cm calibration
  else:
    print("Out Of Range")                             #display out of range
</pre>

# `Code: 8`

<pre>


import RPi.GPIO as GPIO 
import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail= MIMEMultipart()
server = smtplib.SMTP('smtp.gmail.com',587) #SMTP Server and Port Number
server.starttls() #Server Starting
sender = ' ' # Type your own email ID
senpass = ' ' # Enter the password associated with the email
receiver = 'mrahilnasim@gmail.com' # Receiver's Email ID
server.login(sender,senpass) #Authentication Point


GPIO.setmode(GPIO.BOARD)#Numbering the GPIO pin
GPIO.setwarnings(False)
GPIO_TRIGGER = 24
GPIO_ECHO = 23
pulse_start=0
pulse_end=0
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) #GPIO Mapping 
GPIO.setup(GPIO_ECHO,GPIO.IN)

while True:

    GPIO.output(GPIO_TRIGGER, True)
     # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because reflected or echo signal
    distance = (TimeElapsed * 34300) / 2
    print(distance)
    if distance < 50 : #Only sends mail when sensor reads object from less than 50 cm
        mail['From']='Home Automation Systems'
        mail['To'] = receiver
        mail['Subject']='Sensor Data – Alert'
        body='Object detected'
        mail.attach(MIMEText(body,'plain')) 
        msg=mail.as_string()
        server.sendmail(sender,receiver,msg)
        print('Mail Sent')
    time.sleep(5)   #The sensor checks the object in every 5 seconds
GPIO.cleanup()

</pre>

# `Code: 9`
<pre>
import vango  # Importing the nexmo library
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)#Numbering the GPIO pin
GPIO.setwarnings(False)
GPIO_TRIGGER = 24
GPIO_ECHO = 23
pulse_start=0
pulse_end=0
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) #GPIO Mapping 
GPIO.setup(GPIO_ECHO,GPIO.IN)

# Connecting to the vonago using API key and API secret
client = vonage.Client(key="f9xxxxxx", secret="5ahxxxxxxxxxxxxxxx") 
sms = vonage.Sms(client)


# Function to send message
def send_sms():
    # Sending the message
    responseData = sms.send_message(
                                    {
                                        "from": "IOT",
                                         "to": "Enter Reciever Number",
                                         "text": "Enter Message",
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

# `Code: 10`
## pip install pushbullet.py==0.9.1

<pre>
from pushbullet import Pushbullet
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)#Numbering the GPIO pin
GPIO.setwarnings(False)
GPIO_TRIGGER = 24
GPIO_ECHO = 23
pulse_start=0
pulse_end=0
GPIO.setup(GPIO_TRIGGER,GPIO.OUT) #GPIO Mapping 
GPIO.setup(GPIO_ECHO,GPIO.IN)
pb = Pushbullet("o.t8XGOI0l8fEuYdqerxxxxxxxxxxxxxxxx") # your access token
print(pb.devices)
        
while True:
    try:
        # Reading the motion sensor pin state
        pin_state = GPIO.input(sensor_pin)
        if pin_state==0:                 #When output from motion sensor is LOW
            print("Body Not Detected",pin_state)
            sleep(0.5)

        elif pin_state==1:               #When output from motion sensor is HIGH
            print("Body Detected",pin_state)
            dev = pb.get_device('INFINIX X650B')
            push = dev.push_note("Alert!!", "Body Detected In Our Range")
            sleep(1)
            
    except KeyboardInterrupt:
        GPIO.cleaup()
</pre>
