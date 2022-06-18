<div class="jumbotron alert-info"><h1>7.) Relay Module</h1></div>
A power relay module is an electrical switch that is operated by an electromagnet. The electromagnet is activated by a separate low-power signal from a micro controller. When activated, the electromagnet pulls to either open or close an electrical circuit.

![image](https://user-images.githubusercontent.com/63813881/174443809-7e575913-fcc5-41e2-bae6-4a782d5f7704.png)
![image](https://user-images.githubusercontent.com/63813881/174443811-a4aeef58-ab05-4380-8d27-b76298fdba5e.png)

![image](https://user-images.githubusercontent.com/63813881/174443814-02ce1353-ba66-44cd-94d4-59bcebd6e408.png)

# `Code: 1`
<pre>
from gpiozero import OutputDevice

relay = OuputDeveice(4, active_high=False, initial_value=True)

relay.on()
relay.off()
</pre>

# `Code: 2`
<pre>
from gpiozero import OutputDevice
import time

relay = OuputDeveice(4, active_high=False, initial_value=True)

while 1:
    relay.on()
    time.sleep(1)
    relay.off()
</pre>

# `Code: 3`
<pre>
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(4, GPIO.OUT) #set Relay 1 output
GPIO.setup(17, GPIO.OUT) #set Relay 2 output

while True:
    GPIO.Output(4,HIGH)
    GPIO.Output(17,HIGH)
    time.sleep(3)
    GPIO.Ouput(4,LOW)
    GPIO.Ouput(17,LOW)
    time.sleep(3)
</pre>

# `Code: 4`
<pre>
from gpiozero import OutputDevice
import time

control = [2,4]
relay = OuputDeveice(controll, active_high=False, initial_value=True)

while True:
    relay.on()
    time.sleep(1)
    relay.off()
</pre>

# `Code: 5`
<pre>
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
</pre>

# `Code: 6`
<pre>
#getting the main GPIO libraly
import RPi.GPIO as GPIO
#time and json
import time
import json

# setting a list of used pins 
pins = [18,17,15,14]

# setting GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# create empty list 
arr = []
# for loop from 0 to 3 
for x in range(0,4) : 
	#putting all relays in on state if GPIO is not setup
	GPIO.setup(pins[x],GPIO.OUT)
	#putting the relay state in the empty list 
	arr.append(not GPIO.input(pins[x]))

# printing the list of state's in json format
print json.dumps({0:arr[0],1:arr[1],2:arr[2],3:arr[3]})

</pre>

# `Code: 7`
<pre>
import sys
import RPi.GPIO as GPIO
from time import sleep

def main(argv):
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.OUT)
	GPIO.output(25, True)
	sleep(1)
	GPIO.output(25, False)
	sleep(1)
	GPIO.output(25, True)
	sleep(2)
	GPIO.output(25, False)
	GPIO.cleanup()
	return 0

if __name__ == "__main__":
	main(sys.argv[1:])
</pre>

# `Code: 8`
<pre>
# getting the main GPIO libraly
import RPi.GPIO as GPIO
# getting the time libraly
import time

# setting a current mode
GPIO.setmode(GPIO.BCM)
#removing the warings 
GPIO.setwarnings(False)
#creating a list (array) with the number of GPIO's that we use 
pins = [18,17,15,14] 

#setting the mode for all pins so all will be switched on 
GPIO.setup(pins, GPIO.OUT)

#for loop where pin = 18 next 17 ,15, 14 
for pin in pins :
	#setting the GPIO to HIGH or 1 or true
	GPIO.output(pin,  GPIO.HIGH)
	#wait 0,5 second
	time.sleep(0.5)
	#setting the GPIO to LOW or 0 or false
	GPIO.output(pin,  GPIO.LOW)
	#wait 0,5 second
	time.sleep(0.5)

	#Checking if the current relay is running and printing it 
	if not GPIO.input(pin) : 
		print("Pin "+str(pin)+" is working" )
		

#same but the difference is that  we have 
#for loop where pin = 14 next 15,17,18
# backwards
for pin in reversed(pins) :
	GPIO.output(pin,  GPIO.HIGH)
	time.sleep(0.5)

	GPIO.output(pin,  GPIO.LOW)
	time.sleep(0.5)


#cleaning all GPIO's 
GPIO.cleanup()
print("Shutdown All relays")
</pre>
