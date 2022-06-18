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
