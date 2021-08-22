# use analog joystick to control two SG90 servo motors

from machine import Pin, PWM, ADC
import utime


# set up two output pins to control servos with PWM
servo0 = PWM(Pin(14))
servo1 = PWM(Pin(17))
# set std frequency for SG90 which is 50Hz
servo0.freq(50)
servo1.freq(50)

# setup analog pins to read 0-3.3v logic from joystick potentiometer and convert it to 16bit integer
Xanalog = ADC(Pin(27))
Yanalog = ADC(Pin(26))

# SG90s accept a duty cycle of 2% to 12.5% at 50Hz
# 12.5% of 65535 = 8191.875
# 2% of 65535 = 1310.7

# The one real problem I've come across in this program is funding a way to map 16bit int range (65535) to the range of 1310-8200
# Symbolic constants that will help with mapping the 0-65535 range to 1310-8200
MIN_PWM = 1310
MAX_PWM = 8200

# The one real problem I've come across in this program is funding a way to map 16bit int range (65535) to the range of 1310-8200
# Here's a function that seems to solve the problem.
# maps an input number range equally to an output number range
def map_range(number, input_min, input_max, output_min, output_max) -> int:
    return max(min(output_max, (number - input_min) * (output_max - output_min) // (input_max - input_min) + output_min), output_min)


# main loop
try:
    while True:
        # read analog input from joystick
        xint = Xanalog.read_u16()
        xint = map_range(xint, 0, 65535, 1310, 8200)
        yint = Yanalog.read_u16()
        yint = map_range(yint, 0, 65535, 1310, 8200)
        print("X: " + str(xint))
        print("Y: " + str(yint))
        servo0.duty_u16(yint)
        servo1.duty_u16(xint)
        utime.sleep(.2)  
finally:
    #servo0.duty_u16(90)
    servo1.duty_u16(90)



