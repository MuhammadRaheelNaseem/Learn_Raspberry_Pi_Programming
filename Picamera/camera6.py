
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
