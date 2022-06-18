
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()

camera.annotate_text = "Hello world!"
camera.annotate_text_size = 50
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()
