#PROBANDO EL IDE THONNY
from machine import *
import utime
from grove_lcd_i2c import Grove_LCD_I2C

utime.sleep(1)
led = Pin(25, Pin.OUT)

LCD_SDA = Pin(0)
LCD_SCL = Pin(1)
LCD_ADDR = 39# 0x3E or 62
i2c = I2C(0, sda=LCD_SDA, scl=LCD_SCL)

lcd = Grove_LCD_I2C(i2c, LCD_ADDR)

lcd.home()
lcd.write("Raspberry Pi \nPico")
