#!/usr/bin/python
import smbus
import time

def read_word_2c(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

bus = smbus.SMBus(1)
address = 0x68

while True:
    time.sleep(0.1)
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    print "gyro_xout : ", gyro_xout, \
          " scaled: ", (gyro_xout / 131)
    print "gyro_yout : ", gyro_yout, \
          " scaled: ", (gyro_yout / 131)
    print "gyro_zout : ", gyro_zout, \
          " scaled: ", (gyro_zout / 131)

    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    print "accel_xout: ", accel_xout, \
          " scaled: ", (accel_xout / 16384.0)
    print "accel_yout: ", accel_yout, \
          " scaled: ", (accel_yout / 16384.0)
    print "accel_zout: ", accel_zout, \
          " scaled: ", (accel_zout / 16384.0)

    time.sleep(0.5)
