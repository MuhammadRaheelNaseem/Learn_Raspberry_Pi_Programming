from picamera import PiCamera, Color

camera = PiCamera()
# Then below the import line, amend the rest of your code so it looks like this:
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()
