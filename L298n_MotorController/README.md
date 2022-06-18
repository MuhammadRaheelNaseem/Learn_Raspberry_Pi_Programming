<div class="jumbotron alert-info"><h1> 9.) L298d Motor Controller</h1></div>

![image](https://user-images.githubusercontent.com/63813881/174444984-6e46bdb6-30d6-4bc8-a21e-8644b9c30d7c.png)
The L298N is a dual H-Bridge motor driver which allows speed and direction control of two DC motors at the same time. The module can drive DC motors that have voltages between 5 and 35V, with a peak current up to 2A.
![image](https://user-images.githubusercontent.com/63813881/174444995-f980a644-262d-43ba-9564-99914231fb1d.png)

# `Saved this code in l298n.py`
<pre>
import RPi.GPIO as io

class L298N():
    """A class to control one side of an L298N dual H bridge motor driver."""
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        all_pins = [self.in1, self.in2]
        io.setmode(io.BCM)
        io.setup(all_pins, io.OUT)
        io.setwarnings(False)

    def forwards(self):
        io.output(self.in1, 1)
        io.output(self.in2, 0)

    def backwards(self):
        io.output(self.in1, 0)
        io.output(self.in2, 1)

    def stop(self):
        io.output(self.in1, 0)
        io.output(self.in2, 0)

    def cleanup(self):
        io.cleanup()
        io.setmode(io.BCM)
</pre>

# `Code: 1`
<pre>
from l298n import l298n
motor = l298n(2, 3)
motor.forwards()
motor.backwards()
motor.stop()
</pre>

# `Code: 2`
<pre>
import RPi.GPIO as GPIO
import time

forward = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(forward, GPIO.OUT)

while True:
    GPIO.output(forward,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(forward,GPIO.LOW)
    time.sleep(2)
</pre>

# `Code: 3`
<pre>
import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

Forward=26
Backward=20
sleeptime=1

def forward(x):
    GPIO.output(Forward, GPIO.HIGH)
    print("Moving Forward")
    time.sleep(x)
    GPIO.output(Forward, GPIO.LOW)

def reverse(x):
    GPIO.output(Backward, GPIO.HIGH)
    print("Moving Backward")
    time.sleep(x)
    GPIO.output(Backward, GPIO.LOW)

while 1:
    forward(5)
    reverse(5)

GPIO.cleanup()
</pre>
