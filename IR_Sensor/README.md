<div class="jumbotron alert-info"><h1>8.) IR Sensor </h1></div>

![image](https://user-images.githubusercontent.com/63813881/174444384-d63b8ab2-8b7d-4c55-8ee8-e932bd1d39bb.png)
### An infrared sensor (IR sensor) is a radiation-sensitive optoelectronic component with a spectral sensitivity in the infrared wavelength range 780 nm … 50 µm. IR sensors are now widely used in motion detectors, which are used in building services to switch on lamps or in alarm systems to detect unwelcome guests.
![image](https://user-images.githubusercontent.com/63813881/174444401-f6400cb3-25fd-4af2-9561-eee846f19847.png)
![word-image-15](https://user-images.githubusercontent.com/63813881/174444510-a54e09a6-33b2-419a-9842-d3bd0d088d42.gif)


# `Code: 1`
<pre>
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.IN)

while 1:
    state=GPIO.input(40)
    if state==False:
        time.sleep(1)
    else:
        print("Object Detected")
        time.sleep(1)
</pre>

# `Code: 2`
<pre>
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
</pre>

# `Code: 3`
</pre>
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.IN) #GPIO 14 -> IR sensor as input

while True:

    if(GPIO.input(14)==True): #object is far away
        print("No object")
    if(GPIO.input(14)==False): #object is near
        print("move the object")
        
</pre>

# `Code: 4`
<pre>
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
</pre>

![image](https://user-images.githubusercontent.com/63813881/174444532-f145ff66-5a23-4577-91d7-e8eef5cf2a45.png)

# `Code: 5`
<pre>
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
</pre>
