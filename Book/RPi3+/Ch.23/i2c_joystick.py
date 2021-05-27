import smbus
import time

address = 0x48
A0 = 0x40
A1 = 0x42
A2 = 0x41
A3 = 0x43

bus = smbus.SMBus(1)
while True:
    bus.write_byte(address,A0)
    print " Joy X : ", bus.read_byte(address),

    bus.write_byte(address,A1)
    print " Joy Y : ", bus.read_byte(address),

    bus.write_byte(address,A2)
    print " Switch : ", bus.read_byte(address)

    time.sleep(0.1)
