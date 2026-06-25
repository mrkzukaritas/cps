# Servo Motor Manual Control — ESP32 + PCA9685

A MicroPython script for manually controlling a servo motor connected to an ESP32 microcontroller via a PCA9685 servo driver board. Angle values are entered directly in the terminal, allowing real-time control of the motor position.

---

## Hardware Requirements

- ESP32 microcontroller
- PCA9685 16-channel servo driver board
- Servo motor
- Wiring:
  - ESP32 **GPIO 21** → PCA9685 **SDA**
  - ESP32 **GPIO 22** → PCA9685 **SCL**
  - PCA9685 powered via external 5V supply

---

## Software Requirements

- [MicroPython](https://micropython.org/) flashed on the ESP32
- `pca9685.py` driver file uploaded to the ESP32 (must be present on the device)
- A serial terminal tool such as [Thonny](https://thonny.org/) or `mpremote`

---

## Files

| File | Description |
|---|---|
| `servo_control.py` | Main script for manual servo control |
| `pca9685.py` | PCA9685 driver library (must be uploaded to the ESP32) |

---

## How to Run

1. Flash MicroPython onto your ESP32 if not already done.
2. Upload both `pca9685.py` and `servo_control.py` to the ESP32 using Thonny or `mpremote`.
3. Open the serial terminal and run `servo_control.py`.
4. The script will prompt you to enter a value to add to the current angle.
5. Type a positive or negative integer and press Enter to move the servo.
6. Type `q` to quit.

---

## Usage Example

```
Project Started: Running continuous smooth sweep...
Current degree: 0
Enter value to ADD (or 'q' to quit): 30
Current degree: 30
Enter value to ADD (or 'q' to quit): -10
Current degree: 20
Enter value to ADD (or 'q' to quit): q
```

---

## Notes

- The servo angle is clamped between **0° and 180°** to prevent mechanical damage.
- The PWM frequency is set to **50 Hz**, which is standard for hobby servo motors.
- The servo is connected to **channel 0** of the PCA9685 board. To use a different channel, change the first argument in `servo_board.set_angle(0, degree)`.
- Press `Ctrl+C` at any time to stop the program safely.

---

## Part of

This script was developed as part of the **VR Tracking — Humanoid** project at Montanuniversität Leoben (Summer Semester 2026), as the hardware validation stage before integrating live headset tracking data.
