from picamera import PiCamera
from gpiozero import Button
from time import sleep

camera = PiCamera()
button = Button(17)

camera.start_preview(alpha=192)
camera.framerate = 24
button.wait_for_press()
camera.start_recording("vid1.h264")
camera.wait_recording(15)
camera.stop_recording()
camera.stop_preview()
