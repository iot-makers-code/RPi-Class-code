
from gpiozero import PWMOutputDevice
import time

pin1 = 23
pin2 = 24

forward=PWMOutputDevice(pin1, True, 0, 1000)
reverse=PWMOutputDevice(pin2, True, 0, 1000)

try:
	forward.value=1
	reverse.value=0
	time.sleep(1)

	forward.value=0.5
	reverse.value=0
	time.sleep(1)
	
	forward.value=0
	reverse.value=1
	time.sleep(1)

finally:
	forward.value=0
	reverse.value=0
