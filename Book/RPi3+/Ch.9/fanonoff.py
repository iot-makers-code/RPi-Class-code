import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
print("Fan on/off")
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,False)
cnt=0
status=False
while cnt<30:
    a=raw_input('Press enter key to turn on and off !')
    status=~status
    GPIO.output(18,status)
    cnt+=1
GPIO.cleanup()
