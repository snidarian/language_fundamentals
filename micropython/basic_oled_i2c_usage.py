
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime

# symbolic constants
OLED_HEIGHT = 32
OLED_WIDTH = 128

# Setup the I2C interface
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

def blank_screen() -> None:
    oled.fill(0)
    oled.show()

try:
    while True:
        oled.text("OLED TEST MSG.", 0, 0)
        oled.show()
        utime.sleep(1)
        blank_screen()
        oled.text("What up?", 0, 0)
        oled.show()
        utime.sleep(1)
        blank_screen()
finally:
    oled.fill(0)
    oled.show()
    



