<div class="jumbotron alert-success"><h1>11.) LDR (Light Dependent Resistor</h1></div> 

![image](https://user-images.githubusercontent.com/63813881/175463008-b2ac6640-3fca-4d9d-9cdb-1d5192f99b3b.png)
![image](https://user-images.githubusercontent.com/63813881/175463022-0f7c8024-01c8-45bc-864c-54598490b9f3.png)
![image](https://user-images.githubusercontent.com/63813881/175463034-29556fe0-b49d-478f-9862-0e55811b7059.png)

<p>The light-dependent resistor or also known as the LDR sensor is the most important piece of equipment in our circuit. Without it, we wouldn’t be able to detect whether it is dark or light.

In the light, this sensor will have a resistance of only a few hundred ohms while in the dark, it can have a resistance of several megohms.</p>

# `Circuit Diagram`

![image](https://user-images.githubusercontent.com/63813881/175463077-67c4048d-2776-4601-bfd9-0ed1d8fc451b.png)
![image](https://user-images.githubusercontent.com/63813881/175463051-08b6c76c-7894-4ab7-ae85-ca30e3b5ddf8.png)
![image](https://user-images.githubusercontent.com/63813881/175463090-b5c2e9dc-2693-4ff9-9013-0a7bcc46307d.png)

# `Code: 1`

![image](https://user-images.githubusercontent.com/63813881/175463111-525b4da6-3098-4569-acd2-aab9cc64640c.png)

<pre>
from gpiozero import LightSensor

ldr = LightSensor(4)  # alter if using a different pin

while True:
    print(ldr.value)
</pre>    

# `Code: 2`
<pre>
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LIGHT_PIN = 2
GPIO.setup(LIGHT_PIN, GPIO.IN)

sense = not GPIO.input(LIGHT_PIN)
print('Starting up the LIGHT Module (click on STOP to exit)')
time.sleep(0.5)

while True:
  if GPIO.input(LIGHT_PIN) != sense:
    if GPIO.input(LIGHT_PIN):
      print('MOON: \u263e')
    else:
      print ('SUN: \u263c') 
  sense = GPIO.input(LIGHT_PIN)
  time.sleep(0.2)
</pre>

# `Code: 3`
<pre>
#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 7

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print(rc_time(pin_to_circuit))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
</pre>
