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
