<div class="jumbotron alert-info"><h1>10.) PiCamera</h1></div>

![image](https://user-images.githubusercontent.com/63813881/174445246-5dd4be71-7f46-47f9-9978-3dfa0f704107.png)

# `How to insert camera in raspberry pi:`

![camera](https://user-images.githubusercontent.com/63813881/174445376-fd634ff8-5430-4284-bf93-9972fb8991f0.gif)


# `First enable camera like this:`

![image](https://user-images.githubusercontent.com/63813881/174445296-340ce01c-fbc0-4f3a-beec-eb48ed09948c.png)
![image](https://user-images.githubusercontent.com/63813881/174445310-aea85052-a0f8-475d-9cd1-77b025edd3d5.png)

# `Then reboot Pi:`
![image](https://user-images.githubusercontent.com/63813881/174445325-b29fa1f7-ebd8-45b1-a472-accd56f7a801.png)

# `Then restart Raspberry Pi `
# `Other way:`

Start up your Raspberry Pi.

Go to the main menu and open the Raspberry Pi Configuration tool.

![image](https://user-images.githubusercontent.com/63813881/174445336-4b056394-2af1-41b4-a731-d06ffe59143e.png)

Select the Interfaces tab and ensure that the camera is enabled:

![image](https://user-images.githubusercontent.com/63813881/174445341-e9df0699-7581-46a7-ae08-65eab2a13381.png)

# `Reboot your Raspberry Pi.`

# `How to control the Camera Module via the command line:`

<p class="alert-success">pi@raspberrypi:~ $ raspistill -o Desktop/image.jpg</p>
Press Enter to run the command image will be saved!.

<p class="alert-success">pi@raspberrypi:~ $ raspistill -o Desktop/image-small.jpg -w 640 -h 480</p>

<p class="alert-success">pi@raspberrypi:~ $ raspivid -o Desktop/video.h264</p>

# `Code: 1`
<pre>
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.stop_preview()
</pre>

# `Code: 2`
<pre>
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()
</pre>

# `Code: 3`
<pre>
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
</pre>

# `Code: 4`
<pre>
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
</pre>

# `Code: 5`
<pre>
from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Use the following code to set the resolution to maximum and take a picture.
# Note: you also need to set the frame rate to 15 to enable this maximum resolution.
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()
</pre>

# `Code: 6`
<pre>
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

# An annotation is extra information associated with a particular point in a document or other piece of information.
# You can add text to your image using the command annotate_text.
camera.annotate_text = "Hello world!"
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()
</pre>

# `Code: 7`
<pre>
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

camera.annotate_text = "Hello world!"
camera.annotate_text_size = 50
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()
</pre>

# `Code: 8`
<pre>
from picamera import PiCamera, Color

camera = PiCamera()
# Then below the import line, amend the rest of your code so it looks like this:
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()
</pre>

# `Code: 9`
<pre>
from picamera import PiCamera, Color

camera = PiCamera()

camera.start_preview()
camera.brightness = 70
sleep(5)
camera.capture('/home/pi/Desktop/bright.jpg')
camera.stop_preview()
</pre>

# `Code: 10`
<pre>
from picamera import PiCamera, Color

camera = PiCamera()

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: %s" % i
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()
</pre>

# `Code: 11`
<pre>
from picamera import PiCamera, Color

camera = PiCamera()

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()
</pre>

# `Code: 12`
<pre>
from picamera import PiCamera, Color

camera = PiCamera()

camera.start_preview()
camera.image_effect = 'colorswap'
sleep(5)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()
</pre>

# `Code: 13`
<pre>
from picamera import PiCamera, Color

camera = PiCamera()
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
camera.stop_preview()
</pre>
