# A basic program illustrating the use of PWM output in micropython
# information on using PWM in micropython can be found here:
# https://docs.micropython.org/en/latest/library/machine.PWM.html

from machine import PWM, Pin
import utime

# an led is connected to GP0 and a Ground pin in connected to ground
# initialize the pin as an output pin
led0 = Pin(14, Pin.OUT)
led1 = Pin(17, Pin.OUT)
# Onboard green LED. The value keyword allows you to set state on creation.
onboard_led = Pin(25, Pin.OUT, value=1)

# setup the pin as a PWM pin.
pwm0 = PWM(led0)
pwm1 = PWM(led1)
# Set the frequency in Hz - (min frequency is 8Hz)
pwm0.freq(50)
pwm1.freq(50)

count = 0
while count < 3:
    for adjustment in range(65353):
        # change duty cycle with to 16bit integer value
        pwm0.duty_u16(adjustment)
        utime.sleep(0.0001)
        onboard_led.off()
    pwm0.duty_u16(0)
    for adjustment in range(65353, 0, -1):
        pwm1.duty_u16(adjustment)
        utime.sleep(0.0001)
        onboard_led.on()
    count+=1


# deinitializes the pwm LED
onboard_led.off()
pwm0.deinit()
pwm1.deinit()
utime.sleep(1)
