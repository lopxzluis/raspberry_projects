from machine import Pin
from time import sleep
from dht import DHT11

pin = Pin(20, Pin.OUT, Pin.PULL_UP)
sensor = DHT11(pin)

while True:
    T  = (sensor.temperature)
    H = (sensor.humidity)
    try:
        print("Temperatura {} C".format(T))
        print("HUMEDAD {}%\n".format(H))
    except:
        print("ERROR!")
    sleep(2)
              