from machine import Pin, PWM
from time import sleep

led = Pin(15, Pin.OUT)
sen_1 = Pin(28,Pin.IN)
buzzer = Pin(4, Pin.OUT)
led.value(0)
buzzer.value(0)
sleep(20)
print("LISTO")
cont = 0

#SERVO
servo1 = PWM(Pin(16))
servo1.freq(50)

while True:
    
    if sen_1.value():
        cont = cont + 1
        #print("Objeto detectado: " + str(cont))
        
        #for i in range(20):
        servo1.duty_ns(2500000)
        led.toggle()
        buzzer.value(1)
        #sleep(2)
        
    else:
        led.value(0)
        buzzer.value(0)
        servo1.duty_ns(1500000)
    
        #sleep(0.2)