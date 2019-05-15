
from gpiozero import PWMOutputDevice
import time

pin1 = 23
pin2 = 24

pin3 = 17
pin4 = 27

forwardRight=PWMOutputDevice(pin1, True, 0, 1000)
reverseRight=PWMOutputDevice(pin2, True, 0, 1000)

forwardLeft=PWMOutputDevice(pin3, True, 0, 1000)
reverseLeft=PWMOutputDevice(pin4, True, 0, 1000)

try:
	forwardRight.value=1
	reverseRight.value=0
	forwardLeft.value=1
	reverseLeft.value=0
	time.sleep(0.5)
	
	forwardRight.value=0
	reverseRight.value=1
	forwardLeft.value=0
	reverseLeft.value=1
	time.sleep(0.5)
                                                             
        forwardRight.value=0        
      reverseRight.value=0
        forwardLeft.value=1
        reverseLeft.value=0
        time.sleep(1)
                                                             
        forwardRight.value=1
        reverseRight.value=0
        forwardLeft.value=0
        reverseLeft.value=0
        time.sleep(1)
       
finally:
      forwardRight.value=0
      reverseRight.value=0
      forwardLeft.value=0
      reverseLeft.value=0
