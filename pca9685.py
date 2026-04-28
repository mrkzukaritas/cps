import machine
import time

class PCA9685:
    def __init__(self, i2c, address=0x40):
        self.i2c = i2c
        self.address = address
        self.reset()

    def reset(self):
        self.i2c.writeto_mem(self.address, 0x00, b'\x00') 
        time.sleep(0.01)

    def set_freq(self, freq):
        prescale = int((25000000.0 / 4096 / freq) - 0.5)
        self.i2c.writeto_mem(self.address, 0x00, b'\x10') 
        self.i2c.writeto_mem(self.address, 0xfe, bytes([prescale]))
        self.i2c.writeto_mem(self.address, 0x00, b'\x20')
        time.sleep(0.005)

    def set_angle(self, channel, angle):
        # Maps 0-180 degrees to 150-600 pulse width
        pulse = int(150 + (angle / 180) * (600 - 150))
        data = bytes([0, 0, pulse & 0xFF, pulse >> 8])
        self.i2c.writeto_mem(self.address, 0x06 + 4 * channel, data)