import explorerhat
from time import sleep


def wheel (channel, event):
	explorerhat.motor.one.backward(100)
	sleep(int(num))
	explorerhat.motor.one.stop()
	print("That is where you are going on vacation, press one to try again")
	explorerhat.light.on()

num = input("Enter you favorite number (under ten):")

print("Press one to play")

explorerhat.touch.one.pressed(wheel)
