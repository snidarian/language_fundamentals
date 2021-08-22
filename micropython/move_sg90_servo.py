# move servo back and forth

from machine import Pin, PWM, ADC
import utime


servo0 = PWM(Pin(17))
servo0.freq(50)


delay = .5


while True:
    # 0 degrees
    servo0.duty_u16(1350)
    utime.sleep(delay)
    # 90 degrees
    servo0.duty_u16(4587)
    utime.sleep(delay)
    # 180 degrees
    servo0.duty_u16(8200)
    utime.sleep(delay)






