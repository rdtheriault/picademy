from gpiozero import LED
from time import sleep

myled = LED(17)
myled2 = LED(18)

for x in range(0,10):
	myled.on()
	myled2.off()
	sleep(0.5)
	myled.off()
	myled2.on()
	sleep(0.5)
