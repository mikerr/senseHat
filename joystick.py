# uses edev
# sudo pip3 install evdev

from evdev import InputDevice, ecodes,list_devices
from select import select
devices = [InputDevice(fn) for fn in list_devices()]
for dev in devices:
	if dev.name == "Raspberry Pi Sense HAT Joystick":
		js = dev
while True:
	r, w, x = select([dev.fd], [], [],0.01)
	for fd in r:
		for event in dev.read():
			if event.type == ecodes.EV_KEY:# and event.value == 1:
				if event.code == ecodes.KEY_UP:
					print("up")
				elif event.code == ecodes.KEY_LEFT:
					print("left")
				elif event.code == ecodes.KEY_RIGHT:
					print("right")
				elif event.code == ecodes.KEY_DOWN:
					print("down")
				else:
					print("enter")
