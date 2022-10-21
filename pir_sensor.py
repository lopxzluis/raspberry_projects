from machine import I2C, Pin
from time import sleep

led = Pin(15, Pin.OUT)
sen_1 = Pin(28,Pin.IN)
buzzer = Pin(4, Pin.OUT)
led.value(0)
buzzer.value(0)
sleep(10)
print("LISTO")
cont = 0
def detected_motion():
    led.value(1)
    buzzer.value(1)
    sleep(0.2)
    return "Objeto detectado"
while True:
    
    if sen_1.value():
        cont = cont + 1
        #print("Objeto detectado: " + str(cont))
        
        #for i in range(20):
        led.value(1)
        buzzer.value(1)
        #sleep(0.1)
    else:
        led.value(0)
        buzzer.value(0)
        
        sleep(0.4)

'''
while True:
    if sen_1.value():
    #if sen_1.value():
        #cont = cont + 1
        #print("Objeto detectado: " + str(cont))
        
        #for i in range(20):
        led.value(1)
        buzzer.value(1)
        sleep(0.5)
        
    elif sen_1.value() == 0:
        led.value(0)
        buzzer.value(0)
        #sleep(1) 
        
 '''  

 