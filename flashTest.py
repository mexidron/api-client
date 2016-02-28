from neo import easyGpio
from time import sleep

flash = easyGpio(21)
flash.pinOUT()

while True:
    flash.on()
    sleep(1)
    flash.off()
    sleep(1)
    flash.on()
    sleep(2)
    flash.off()
    sleep(1)

