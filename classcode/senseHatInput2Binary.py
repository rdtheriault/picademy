
#from sense_emu import SenseHat
from sense_hat import SenseHat

sense = SenseHat()

blue=(0, 0, 255)
yellow=(255,255,0)
white=(255,255,255)
num = 0;
sense.clear(yellow)

for x in range(0,5):
	num = int(input('Enter a number under 256: '))
	sense.clear(yellow)
	if (num >= 128):	
		sense.set_pixel(0,0, blue)
		num = num -128
	else:
		sense.set_pixel(0,0, white)
	if (num >= 64):
		sense.set_pixel(0,1,blue)
		num = num - 64
	else:
		sense.set_pixel(0,1,white)
	if (num >= 32):
		sense.set_pixel(0,2,blue)
		num = num - 32
	else:
		sense.set_pixel(0,2,white)
	if (num >= 16):
		sense.set_pixel(0,3,blue)
		num = num - 16
	else:
		sense.set_pixel(0,3,white)
	if (num >= 8):
		sense.set_pixel(0,4,blue)
		num = num - 8
	else:
		sense.set_pixel(0,4,white)
	if (num >= 4):
		sense.set_pixel(0,5,blue)
		num = num - 4
	else:
		sense.set_pixel(0,5,white)
	if (num >= 2):
		sense.set_pixel(0,6,blue)
		num = num - 2
	else:
		sense.set_pixel(0,6,white)
	if (num >= 1):
		sense.set_pixel(0,7,blue)
		num = num - 1
	else:
		sense.set_pixel(0,7,white)
