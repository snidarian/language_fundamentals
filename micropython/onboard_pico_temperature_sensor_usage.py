from machine import ADC, Pin, I2C
import utime


sensor_temp = ADC(4)
# converting analog value to temperature
conversion_factor = 3.3 / (65535)


try:
    while True:
        # get the temperature in celsius
        reading = sensor_temp.read_u16() * conversion_factor
        celsius_temperature = 27 - (reading - 0.706)/0.001721
        # convert celsius to fahrenheit with conversion formula
        fahrenheit_temperature = (celsius_temperature * 1.8) + 32
        print(fahrenheit_temperature)
        utime.sleep(2)
finally:
    print("Program terminated...")
    utime.sleep(1)
        