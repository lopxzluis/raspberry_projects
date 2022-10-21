from machine import I2C, Pin, ADC, PWM
from time import sleep
from pico_i2c_lcd import I2cLcd
adc = ADC(Pin(26))
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
led = PWM(Pin(15))
led.freq(10000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

while True:
    valor_poten = adc.read_u16()
    print(valor_poten)
    led.duty_u16(valor_poten)
    sleep(0.7)
    lcd.move_to(1,0)
    lcd.putstr("EL VALOR ES:    ")
    lcd.putstr(str(valor_poten))
    
    #LED
    