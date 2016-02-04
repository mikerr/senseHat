#Multi-coloured flash message - MrC's version
from sense_hat import SenseHat
import random
import time

sense=SenseHat()
message = "flashy letters"


#Create a loop which displays each term in order, and picks a new colour for each term.
while True:
	for i in list(message):
		r=random.randint(0,255)      			
		r1=random.randint(0,255)     		
		r2=random.randint(0,255)     	
		sense.show_letter( i, text_colour = [r,r1,r2])
		time.sleep(0.2)
