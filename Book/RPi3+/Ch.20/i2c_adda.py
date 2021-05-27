import smbus
import time

address = 0x48
DA = 0x40
A0 = 0x41
max = 50

bus = smbus.SMBus(1)
while True:
    bus.write_byte(address,A0)
    inp = bus.read_byte(address)
    max = inp if inp > max else max
    value = int(255 * inp / max)
    bus.write_byte_data(address,DA,value)
    print("AOUT:%3d @%3d / %3d " %(value, inp,max))
    time.sleep(0.02)
