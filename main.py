import machine
import time
from pca9685 import PCA9685  # This imports the file you made above!

# 1. Initialize I2C (Pins G21 and G22)
i2c = machine.I2C(0, sda=machine.Pin(21), scl=machine.Pin(22), freq=100000)

# 2. Initialize the Servo Board
servo_board = PCA9685(i2c)
servo_board.set_freq(50)

print("Project Started: Running continuous smooth sweep...")

degree = 0

try:
    while True:
        # Move servo first (like do-while)
        servo_board.set_angle(0, degree)
        print("Current degree:", degree)

        mas = input("Enter value to ADD (or 'q' to quit): ")

        if mas == 'q':
            break

        try:
            mas = int(mas)
            degree = degree + mas

            # Limit between 0 and 180
            degree = max(0, min(180, degree))

        except ValueError:
            print("Invalid number")

except KeyboardInterrupt:
    print("Program stopped")