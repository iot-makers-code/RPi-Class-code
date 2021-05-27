import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
print('Test photo register')
GPIO.setup(24,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,False)
cnt=60*50
for i in range(0,cnt,1):
    time.sleep(0.01)
    inx = GPIO.input(24)
    print('input :', inx)
    GPIO.output(18,True if inx else False)
GPIO.cleanup()
