from sense_hat import SenseHat

sense = SenseHat()

b=(0, 0, 255)
w=(255,255,0)

image = [
w, w, b, b, b, w, w, w,
w, w, b, w, w, b, w, w, 
w, w, b, w, w, b, w, w,
w, w, b, b, b, w, w, w,
w, w, b, b, w, w, w, w,
w, w, b, w, b, w, w, w,
w, w, b, w, w, b, w, w,
w, w, b, w, w, b, w, w
]

sense.set_pixels(image)
