from gpiozero import LED
from time import sleep
led = LED(4)
beeper= LED(23)
for x in range(5):
led.on()
beeper.on()
sleep(1)
led.off()
beeper.off()
sleep(1)
