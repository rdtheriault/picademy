from picamera import PiCamera
from gpiozero import Button
from time import sleep

camera = PiCamera()
button = Button(17)

camera.start_preview(alpha=192)
button.wait_for_press()
for i in range(3):
	#button.wait_for_press()
	sleep(1)
	camera.capture("previewbtn{0}.jpg".format(i))

camera.stop_preview()
