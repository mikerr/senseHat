from sense_hat import SenseHat
sense = SenseHat()
while True:
	t = sense.get_temperature()
	p = sense.get_pressure()
	h = sense.get_humidity()
	t = round(t,1)
	p = round(p,1)
	h = round(h,1)
	msg = "Temp %s Pressure %s Humidity %s" % (t,p,h)

	print msg
	sense.show_message(msg,scroll_speed=0.05)
