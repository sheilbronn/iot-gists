# LED_Blink_MPython_Heltec_Lora_Wifi_V3.py

from machine import Pin
from time import sleep

led = Pin(35, Pin.OUT) # Pin 35 is the LED on the Heltec Lora Wifi V3 board

while True:
  led.value(not led.value()) # toggle the onboard LED
  sleep(1+(not led.value())*2) # sleep 1 second if LED was on, 2 seconds if LED was off