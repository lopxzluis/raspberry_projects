from machine import I2C, Pin, ADC, PWM
from time import sleep

adc = ADC(Pin(26))
servo1 = PWM(Pin(16))
servo1.freq(50)
while True:
    
    angulo = int(adc.read_u16()*180/65535)
    print(angulo, adc.read_u16())
    ton = (angulo + 45)*100000/9
    #servo1.duty_ns(int(ton))
    sleep(0.2)