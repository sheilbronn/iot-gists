# Code to output a message on the builtin OLED display of a Heltec Lora Wifi Kit V3 (emphasis on V3!)
# 1. Pins had to be adapted for a V3 (as compared to V2)
# 2. reset sequence "1-0-1" need to reset OLED

# https://heltec.org/project/wifi-kit32-v3/
# vs
# ODER V2? https://ae01.alicdn.com/kf/HTB18J0tSVXXXXb9XFXXq6xXFXXXW.jpg
# vs
# https://escapequotes.net/wp-content/uploads/2021/02/WIFI_LoRa_32_V2-Heltec-pinout-diagram-scaled.jpg

from time import sleep_ms, sleep  # in ms
from machine import Pin, SoftI2C, freq
reset_pin = Pin(21, Pin.OUT, value=1)   # pin 16 > 21 # "1-0-1" not needed anymore when lib is modified ?!
sleep_ms(1)
reset_pin = Pin(21, Pin.OUT, value=0)   # pin 16 > 21 
sleep_ms(2)
reset_pin = Pin(21, Pin.OUT, value=1)   # pin 16 > 21 

# according to http://community.heltec.cn/t/heltec-wifi-kit-32-v3-no-oled-with-micropython/13166
scl_pin = Pin(18, Pin.IN, Pin.PULL_UP)  # pin 15 > 18
sda_pin = Pin(17, Pin.IN, Pin.PULL_UP)  # pin 4  > 17
i2c = SoftI2C(scl=scl_pin, sda=sda_pin, freq=400000)
i2c.scan()

# TODO: https://forum.micropython.org/viewtopic.php?t=4002
import ssd1306
# oled = ssd1306.SSD1306_I2C(128, 64, i2c, res=Pin(21))  # Parameter "res" only understood by a modified version of lib ssd1306.py!
oled = ssd1306.SSD1306_I2C(128, 64, i2c)  # ... or use "1-0-1" reset code on pin 21 above
oled.fill(0)
oled.text(" FREQ: " + str(freq()/1000000) + " MHz", 0, 0)
oled.text("     SOME     ", 0, 24)
oled.text("  MORE LINES ", 0, 32)
oled.text("    ON THE    ", 0, 40)
oled.text("    SCREEN.   ", 0, 48)
#oled.fill(1)

oled.show()
sleep(1)
#oled.poweroff()     # power off the display, pixels persist in memory
oled.text("    INDEED    ", 0, 16)
oled.show()

sleep(1)
# oled.poweron()      # power on the display, pixels redrawn
oled.contrast(1)    # dim
oled.show()
sleep(1)
oled.contrast(255)  # bright
oled.invert(1)      # display inverted
# oled.invert(0)      # display normal
# oled.rotate(True)   # rotate 180 degrees
# oled.rotate(False)  # rotate 0 degrees
oled.text("     DONE.    ", 0, 56)
oled.show()