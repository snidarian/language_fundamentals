# Sample pico's onboard temperature sensor and display value to 32x128

from machine import Pin, ADC, I2C
from ssd1306 import SSD1306_I2C
import utime

# symbolic constants
OLED_HEIGHT = 32
OLED_WIDTH = 128

# set up pins for color LED status indication
green_led = Pin(16, Pin.OUT)
orange_led = Pin(17, Pin.OUT)
blue_led = Pin(18, Pin.OUT)
red_led = Pin(19, Pin.OUT)

# Setup up variables for onboard temperature sensor
sensor_temp = ADC(4)
# converting analog value to temperature
conversion_factor = 3.3 / (65535)

# Setup the I2C interface
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

def blank_screen() -> None:
    oled.fill(0)
    oled.show()

def flash_normal_status() -> None:
    green_led.value(1)
    orange_led.value(1)
    utime.sleep(.5)
    green_led.value(0)
    orange_led.value(0)

def flash_irregular_status() -> None:
    blue_led.value(1)
    red_led.value(1)
    utime.sleep(.5)
    blue_led.value(0)
    red_led.value(0)


try:
    while True:
        # get the temperature in celsius
        reading = sensor_temp.read_u16() * conversion_factor
        celsius_temperature = 27 - (reading - 0.706)/0.001721
        # convert celsius to fahrenheit with conversion formula
        fahrenheit_temperature = (celsius_temperature * 1.8) + 32
        print(fahrenheit_temperature)
        fahrenheit_string = "{0:.3g} F".format(fahrenheit_temperature)
        # Display temp sensor reading to screen
        oled.text(fahrenheit_string, 0, 0)
        oled.show()
        utime.sleep(1)
        if fahrenheit_temperature < 80:
            oled.text("Normal status", 0, 10)
            oled.show()
            flash_normal_status()
            utime.sleep(3)
            blank_screen()
        else:
            oled.text("Temp elevated", 0, 10,)
            oled.text("Check system...", 0, 20)
            oled.show()
            flash_irregular_status()
            utime.sleep(3)
        blank_screen()
finally:
    oled.fill(0)
    oled.show()
    





