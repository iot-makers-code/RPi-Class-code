import smbus
import time

address = 0x48
A0 = 0x40

bus = smbus.SMBus(1)
while True:
    bus.write_byte(address,A0)
    value = bus.read_byte(address)
    print("AIN:%1.2f  " %(value*100/255))
    time.sleep(0.1)
