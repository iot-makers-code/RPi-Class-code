import smbus
import time

address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)
while True:
    bus.write_byte(address,A0)
    value = bus.read_byte(address)
    print( "*" * (value/4) )
    time.sleep(0.1)
