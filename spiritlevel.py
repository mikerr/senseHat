# 2d spirit level

from sense_hat import SenseHat
import time

sense = SenseHat()
       
sense.clear()

red = [255,0,0]
center = 4

while True:
    o = sense.orientation

    pitch = o['pitch'] 
    roll = o['roll'] 

    if pitch > 180 : pitch = pitch - 360
    if roll > 180 : roll = roll - 360

    x = center - pitch
    y = center + roll

    if (x > 7) : x = 7
    if (x < 0) : x = 0

    if (y > 7) : y = 7
    if (y < 0) : y = 0

    sense.clear()
    sense.set_pixel(x,y,red)

    time.sleep (0.01)

