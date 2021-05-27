import RPi.GPIO as GPIO
import smbus
import time

GPIO.setmode(GPIO.BCM)
pins=[12,16,21,05]
for p in pins: GPIO.setup(p, GPIO.OUT)

address = 0x48
A0 = 0x40
A1 = 0x42
A2 = 0x41
A3 = 0x43

bus = smbus.SMBus(1)
while True:
    bus.write_byte(address,A0)
    x = bus.read_byte(address)
    print " Joy X : ", x,
    GPIO.output(pins[0], x > 129)
    GPIO.output(pins[1], x < 129)

    bus.write_byte(address,A1)
    y = bus.read_byte(address)
    print " Joy Y : ", y,
    GPIO.output(pins[2], y > 129)
    GPIO.output(pins[3], y < 129)

    bus.write_byte(address,A2)
    print " Switch : ", bus.read_byte(address)

    time.sleep(0.1)
