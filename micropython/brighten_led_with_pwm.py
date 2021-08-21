# A basic program illustrating the use of PWM output in micropython
# information on using PWM in micropython can be found here:
# https://docs.micropython.org/en/latest/library/machine.PWM.html

from machine import PWM, Pin
import utime

# an led is connected to GP0 and a Ground pin in connected to ground
# initialize the pin as an output pin
led0 = Pin(0, Pin.OUT)

# setup the pin as a PWM pin.
pwm = PWM(led0)
# Set the frequency in Hz
pwm.freq(500)

count = 0
while count < 5:
    for adjustment in range(65353):
        # change duty cycle with to 16bit integer value
        pwm.duty_u16(adjustment)
        utime.sleep(0.0001)
    for adjustment in range(65353, 0, -1):
        pwm.duty_u16(adjustment)
        utime.sleep(0.0001)
    count+=1


# deinitializes the pwm LED
pwm.deinit()
