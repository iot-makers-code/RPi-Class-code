import smbus
import time

address = 0x48
DA = 0x40
value = 0

bus = smbus.SMBus(1)
while True:
    bus.write_byte_data(address,DA,value)
    print("AOUT:%3d @ " %value)
    value += 1
    if value >= 256:value =0
    time.sleep(0.02)
