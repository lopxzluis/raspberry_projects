from machine import Pin
import time
led = Pin(2, Pin.OUT)
led.value(1)
time.sleep(2)
led.value(0)

#este es un cambio
while True:
    led.on()
    print("prendido")
    time.sleep(1)
    led.off()
    print("apagado")
    time.sleep(1)

