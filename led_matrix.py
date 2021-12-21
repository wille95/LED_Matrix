# Sven Wille
# LED - Matrix 
# Version 1

import max7219
from machine import Pin, SPI
from HTU2X import HTU21D
from time import sleep

htu = HTU21D(22,21)  
spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(15), mosi=Pin(2))
ss = Pin(17)

display = max7219.Matrix8x8(spi, ss, 4)
display.brightness(7)

while True:

    for i in range (-16,33):
        display.fill(0)
        htu_temp = round(htu.temperature)
        ausgabe_htu_temp = str(htu_temp)
        display.text(ausgabe_htu_temp + "Grad",i,0,1)
        display.show()
        sleep(0.1)
            
        

