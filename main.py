import machine
import time
from pca9685 import PCA9685  # This imports the file you made above!

# 1. Initialize I2C (Pins G21 and G22)
i2c = machine.I2C(0, sda=machine.Pin(21), scl=machine.Pin(22), freq=100000)

# 2. Initialize the Servo Board
servo_board = PCA9685(i2c)
servo_board.set_freq(50)

print("Project Started: Running continuous smooth sweep...")

try:
    while True:
        # Smooth Forward Sweep
        for angle in range(0, 181, 2):
            servo_board.set_angle(0, angle)
            time.sleep(0.01)
            
        # Smooth Backward Sweep
        for angle in range(180, -1, -2):
            servo_board.set_angle(0, angle)
            time.sleep(0.01)
            
except KeyboardInterrupt:
    print("Program stopped by user.")