from machine import I2C, Pin, ADC
from time import sleep
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
led = Pin(15, Pin.OUT)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)


def read_temp():
    sensor_temp = ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = 27 - (reading - 0.706)/0.001721
    formatted_temperature = "{:.2f}".format(temperature)
    string_temperature = str("Temp:" + formatted_temperature)
    print(string_temperature)
    sleep(0.5)
    return string_temperature



while True:
   
    temperature = read_temp()
    lcd.move_to(0,0)
    lcd.putstr(temperature)


   
   
   
   
   
   # time = utime.localtime()
    #lcd.putstr(str(ds.year()) + "/" +  str(ds.month()) + "/" + str(ds.day()) + " " + str(ds.hour()) + ":" + str(ds.minute()))
    
