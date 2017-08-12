from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#data = sense.get_orientation()
for x in range(0,10):
	data = sense.get_orientation()
	pitch=data['pitch']
	print(pitch)
	sleep(0.5)
