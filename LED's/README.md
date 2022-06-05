# `Let's play with Raspberry Pi`

# `Breadboard`
# `What is Breadboard?`
`A breadboard is used to build and test circuits quickly before finalizing any circuit
design. The breadboard has many holes into which circuit components like ICs and
resistors can be inserted. A typical breadboard is shown below:`

![image](https://user-images.githubusercontent.com/63813881/172048499-93c1f3d3-ffd8-49fb-9ac6-b9128edcd34d.png)

## `connection:`
![image](https://user-images.githubusercontent.com/63813881/172048507-0ad8ae34-bdef-424e-a7e9-e77e2e228924.png)


## `After Connections board look like:`
<!-- ![image-3.png](attachment:image-3.png)
 -->
<img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/complete.gif" alt="Complete project example">


<div class="c-project-panel__content">
    <h2 id="what-you-will-need">What you will need</h2>

<h3 id="hardware">Hardware</h3>

<p>As well as a Raspberry Pi with an SD card and the usual peripherals, you’ll also need:</p>

<table>
  <thead>
    <tr>
      <th style="text-align: center">1x Solderless breadboard</th>
      <th style="text-align: center">Male-to-female jumper leads</th>
      <th style="text-align: center">Female-to-female jumper leads</th>
      <th style="text-align: center">Male-to-male jumper leads</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/breadboard.png" alt="breadboard"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/jumper-male-to-female.png" alt="m to f jumper leads"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/jumper-female-to-female.png" alt="f to f jumper leads"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/jumper-male-to-male.png" alt="m to m jumper leads"></td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th style="text-align: center">1x Tactile button</th>
      <th style="text-align: center">3x LEDs</th>
      <th style="text-align: center">Ultrasonic distance sensor</th>
      <th style="text-align: center">Passive infrared motion sensor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/tactile-push-button.png" alt="tactile button"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/led.png" alt="LED"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/ultrasonic-distance-sensor.png" alt="ultrasonic distance sensor"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/pir.png" alt="PIR sensor"></td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th style="text-align: center">Light Dependent Resistor</th>
      <th style="text-align: center">5V Motor</th>
      <th style="text-align: center">3x 330Ω Resistor</th>
      <th style="text-align: center">470Ω Resistor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/ldr.png" alt="LDR"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/motor2.png" alt="motor"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/resistor-330r.png" alt="330 resistor"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/resistor-470r.png" alt="470 resistor"></td>
    </tr>
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <th style="text-align: center">1x 1μF Capacitor</th>
      <th style="text-align: center">Buzzer</th>
      <th style="text-align: center">Motor Controller</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/capacitor.png" alt="capacitor"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/piezo-buzzer.png" alt="buzzer"></td>
      <td style="text-align: center"><img src="https://projects-static.raspberrypi.org/projects/physical-computing/765b944f3fe3d57bd3568794ff6527f72b57ddc8/en/images/motor-controller.png" alt="motor controller"></td>
    </tr>
  </tbody>
</table>


<h3 id="software">Software</h3>

<p>There are no additional software requirements for this resource beyond what is pre-installed in the current Raspbian image.</p>

  </div>
  
# `GPIO's Pin`
![image](https://user-images.githubusercontent.com/63813881/172048617-2964a78c-de6b-41ba-b98a-193ed8055695.png)
![image](https://user-images.githubusercontent.com/63813881/172048624-db2adcf7-7c52-4a1c-b671-11ec41b5c81b.png)
![image](https://user-images.githubusercontent.com/63813881/172048634-ff5006ed-d75b-4f9a-80c2-c7319884c7c6.png)


# `Lighting an LED`

`LEDs are delicate little things. If you put too much current through them they will pop (sometimes quite spectacularly). To limit the current going through the LED, you should always use a resistor in series with it.`

`Try connecting the long leg of an LED to the Pi’s 3V3 and the short leg to a GND pin. The resistor can be anything over about 50Ω.`

# `Circuit Diagram`
![image](https://user-images.githubusercontent.com/63813881/172048643-d21abb3e-0620-4f4c-9148-a432889b66e3.png)


`The LED should light up. It will always be on, because it’s connected to a 3V3 pin, which is itself always on.`
`Now try moving it from 3V3 to GPIO pin 17:`

![image](https://user-images.githubusercontent.com/63813881/172048649-44d7b0dc-de77-45d2-b7fa-49189b4ef87f.png)

`The LED should now turn off, but now it’s on a GPIO pin, and can therefore be controlled by code.`

# `GPIOZERO`

`GPIO Zero builds on a number of underlying pin libraries, including RPi. GPIO and pigpio, each with their own benefits. You can select a particular pin library to be used, either for the whole script or per-device, according to your needs.`

|

`GPIO Zero is a zero-boilerplate Python library that makes physical computing with Python more accessible and helps people progress from zero to hero.`



<h1 class='jumbotron alert-info'>1.) LED Codes</h1>

## `Ohm's Law`
![image](https://user-images.githubusercontent.com/63813881/172048682-00548df3-48b5-434e-92b5-9c6aba37dc11.png)

# `Code: 1`
<div>
<p>from gpiozero import LED

led = LED(17)

led.on()
    
led.off()
    </p>    
</div>

# `Code: 2`
<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">LED</span>
<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>

<span class="n">led</span> <span class="o">=</span> <span class="n">LED</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>

<span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="n">led</span><span class="o">.</span><span class="n">on</span><span class="p">()</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">led</span><span class="o">.</span><span class="n">off</span><span class="p">()</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</pre>

# `Code: 3`
<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">LED</span>
<span class="kn">from</span> <span class="nn">signal</span> <span class="kn">import</span> <span class="n">pause</span>

<span class="n">red</span> <span class="o">=</span> <span class="n">LED</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>

<span class="n">red</span><span class="o">.</span><span class="n">blink</span><span class="p">()</span>

<span class="n">pause</span><span class="p">()</span>
</pre>

## `Any regular LED can have its brightness value set using PWM (pulse-width-modulation). In GPIO Zero, this can be achieved using PWMLED using values between 0 and 1:`

# `Code: 4`
<pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">PWMLED</span>
<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>

<span class="n">led</span> <span class="o">=</span> <span class="n">PWMLED</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>

<span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="n">led</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="mi">0</span>  <span class="c1"># off</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">led</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="mf">0.5</span>  <span class="c1"># half brightness</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">led</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># full brightness</span>
    <span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</pre>

# `Code: 5`
<div class="highlight-python3 notranslate"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">gpiozero</span> <span class="kn">import</span> <span class="n">PWMLED</span>
<span class="kn">from</span> <span class="nn">signal</span> <span class="kn">import</span> <span class="n">pause</span>

<span class="n">led</span> <span class="o">=</span> <span class="n">PWMLED</span><span class="p">(</span><span class="mi">17</span><span class="p">)</span>

<span class="n">led</span><span class="o">.</span><span class="n">pulse</span><span class="p">() # like heart beat beep</span>

<span class="n">pause</span><span class="p">()</span>
</pre></div>
</div>

# `RPI.GPIO`
`RPI.GPIO pins allow the Raspberry Pi to control and monitor the outside world by being connected to electronic circuits. The Pi is able to control LEDs, turning them on or off, run motors, and many other things. It's also able to detect whether a switch has been pressed, the temperature, and light.`

### ` Install in terminal if it not!`
### `pip install rpi.gpio`


# `Code: 6`
<pre data-trimmed="true" class="rainbow-show"><code data-language="python" class="rainbow rainbow-show"><span class="keyword">import</span> time
<span class="keyword">import</span> RPi.GPIO <span class="keyword">as</span> GPIO

<span class="comment"># Pin definitions</span>
led_pin <span class="keyword operator">=</span> <span class="constant numeric">17</span>

<span class="comment"># Suppress warnings</span>
GPIO.<span class="function call">setwarnings</span>(<span class="constant language">False</span>)

<span class="comment"># Use "GPIO" pin numbering</span>
GPIO.<span class="function call">setmode</span>(GPIO.BCM)

<span class="comment"># Set LED pin as output</span>
GPIO.<span class="function call">setup</span>(led_pin, GPIO.OUT)

<span class="comment"># Blink forever</span>
<span class="keyword">while</span> <span class="constant language">True</span>:
    GPIO.<span class="function call">output</span>(led_pin, GPIO.HIGH) <span class="comment"># Turn LED on</span>
    time.<span class="function call">sleep</span>(<span class="constant numeric">1</span>)                   <span class="comment"># Delay for 1 second</span>
    GPIO.<span class="function call">output</span>(led_pin, GPIO.LOW)  <span class="comment"># Turn LED off</span>
    time.<span class="function call">sleep</span>(<span class="constant numeric">1</span>)                   <span class="comment"># Delay for 1 second</span>
</code><div class="preloader"><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div></pre>

<div class=alert-warning>
<p>Code to Note:</p>

<p>To control hardware from the Raspberry Pi, we rely on the RPi.GPIO module. This module (likely known as a "library" in other languages) is specifically designed to help us toggle pins and talk to other pieces of hardware. Lucky for us, it comes pre-packaged with Raspbian!</p>

<p>In the first two lines, you see that we imported modules, but we added a few things onto those imports. First up, we used the keyword <code>as</code>:</p>

<pre><code>language:python
import RPi.GPIO as GPIO
</code></pre>

<p><code>RPi.GPIO</code> is the name of the module. By saying <code>as GPIO</code>, we change how we want to refer to that module in the rest of the program. This allows us to type</p>

<pre><code>language:python
GPIO.output(led_pin, GPIO.HIGH)
</code></pre>

<p>instead of the much longer</p>

<pre><code>language:python
RPi.GPIO.output(led_pin, RPi.GPIO.HIGH)
</code></pre>

<p>While it's generally not a good idea to disable warnings while coding, we added the following line:</p>

<pre><code>language:python
GPIO.setwarnings(False)
</code></pre>

<p>Without it, you'll get a warning from the interpreter when you try to run the blink program again:</p>

<pre><code>language:python
blink.py:14: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(led_pin, GPIO.OUT)
</code></pre>

<p>This is because we did not shut down the GPIO 12 pin nicely when we exited the program. To do this, we would want to add a <code>GPIO.cleanup()</code> line at the end of our program. However, because we wrote our program to run forever, we have to interrupt the program to stop it (and a call to <code>cleanup()</code> would never occur). For the time being, it's enough to just ignore the warnings.</p>

<p>Challenge: Change the program to make the LED blink like a heartbeat: 2 quick flashes in succession and then a longer delay.</p>
</div>

# `Code: 7`

<pre><code>
import time
import RPi.GPIO as GPIO

# Pin definitions
led_pin = 12

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

# Initialize pwm object with 50 Hz and 0% duty cycle
pwm = GPIO.PWM(led_pin, 50)
pwm.start(0)

# Set PWM duty cycle to 50%, wait, then to 90%
pwm.ChangeDutyCycle(50)
time.sleep(2)
pwm.ChangeDutyCycle(90)
time.sleep(2)

# Stop, cleanup, and exit
pwm.stop()
GPIO.cleanup()
</code></pre>

# `Code: 9`

<p>import RPi.GPIO as GPIO<br />
import time</p>

<p>led = 18<br />
switch = 31</p>

<p>GPIO.setmode(GPIO.BOARD)<br />
GPIO.setup(led, GPIO.OUT)<br />
GPIO.setup(switch, GPIO.IN)</p>

<p>for i in range(10):<br />
&nbsp; &nbsp; GPIO.output(led, GPIO.HIGH)<br />
&nbsp; &nbsp; time.sleep(0.2)<br />
&nbsp; &nbsp; GPIO.output(led, GPIO.LOW)<br />
&nbsp; &nbsp; time.sleep(0.2)<br />
&nbsp; &nbsp; print('Switch status = ', GPIO.input(switch))</p>

<p>GPIO.cleanup()</p>
