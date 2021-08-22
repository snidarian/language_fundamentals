# Using an analog joystick with the RPi PICO

from machine import ADC, Pin, PWM
import utime

# setup GP pins 27 and 26 (board pins 32 and 31) as analog inputs for x coordinate and y coordinate respectively
Xanalog = ADC(Pin(27))
Yanalog = ADC(Pin(26))


# lets use the joystick to control the brightness of a few LEDS
led0 = PWM(Pin(17))
led1 = PWM(Pin(14))

# as the joystick moves and the analog signal is converted to a
# 16bit integer and then used as the duty for the leds
try:
    while True:
        xint = Xanalog.read_u16()
        yint = Yanalog.read_u16()
        print("X: " + str(xint))
        print("Y: " + str(yint))
        # Modify duty cycle to reflect joystick
        led0.duty_u16(xint)
        led1.duty_u16(yint)
        utime.sleep(.1)
finally:
    led0.duty_u16()
    led1.duty_u16()






