from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=192)
sleep(2)
camera.capture("~preview2.jpg")
camera.stop_preview()
