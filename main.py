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
        # Mover a la derecha
        servo_board.set_angle(0, 180)
        #servo_board.set_angle(1, 180)  # Servo 2
        print("Derecha")
        time.sleep(5)

        # Mover a la izquierda
        servo_board.set_angle(0, 0)
        #servo_board.set_angle(1, 0)  # Servo 2
        print("Izquierda")
        time.sleep(5)

except KeyboardInterrupt:
    print("Programa detenido")