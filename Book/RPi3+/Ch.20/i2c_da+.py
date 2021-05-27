import smbus
import time
import math

address = 0x48
DA = 0x40
value = 0

bus = smbus.SMBus(1)
while True:
    radian = math.radians(180*(value/256.0))
    out = int(255 * math.sin(radian))
    bus.write_byte_data(address,DA,out)
    print("AOUT:%3d %3d@ " %(value, out))
    value += 1
    if value >= 256:value =0
    time.sleep(0.02)
