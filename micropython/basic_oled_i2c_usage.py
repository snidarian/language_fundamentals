
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C


# symbolic constants
OLED_HEIGHT = 32
OLED_WIDTH = 128

# Setup the I2C interface
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)







