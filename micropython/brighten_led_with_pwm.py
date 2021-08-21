# A basic program illustrating the use of PWM output in micropython
# information on using PWM in micropython can be found here:
# https://docs.micropython.org/en/latest/library/machine.PWM.html

from machine import PWM, Pin
import utime

# an led is connected to GP0 and a Ground pin in connected to ground

led0 = Pin(0, Pin.OUT)

pwm = PWM(led0)
pwm.duty_u16(32768)
utime.sleep(3)

count = 0

while count < 5:
    for adjustment in range(65353):
        pwm.duty_u16(adjustment)
        utime.sleep(0.0001)
    for adjustment in range(65353, 0, -1):
        pwm.duty_u16(adjustment)
        utime.sleep(0.0001)
    count+=1


# deinitializes the pwm LED
pwm.deinit()
