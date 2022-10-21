from machine import Pin, PWM
import time

servo1 = PWM(Pin(13))
servo1.freq(50)
print("PROGRAMA PARA MOVER EL SERVOMOTOR CON UN INPUT DEL USUARIO")
while True:
    entrada = input("Introduzca el valor del angulo: ")
    if entrada == "":
        print("Fin del programa")
        break
    else:
        ton = ((int(entrada)+45)*100000)/9
        servo1.duty_ns(int(ton))
    '''
    
    for pulso in range(500000, 2500000, 1000):
        servo1.duty_ns(pulso)
        time.sleep_ms(1)
    for pulso in range(2500000,500000, -1000):
        servo1.duty_ns(pulso)
        time.sleep_ms(1)
    '''    