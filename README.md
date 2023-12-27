# iot-gists

Little pieces of code related to IoT programming on ESP32 etc

## Heltec Lora Wifi 32 V3 (not V2!)

Code for the Heltec Lora Wifi 32 V3 (not V2!)

### OLED_MPython_Heltec_Lora_Wifi_V3.py

1. Shows how to manipulate the reset the OLED on the Heltec Lora Wifi 32 V3 using Micropython ...
2. ... and puts some text on the OLED. 

### LED_Blink_MPython_Heltec_Lora_Wifi_V3.py

1. Make the onboard LED blink (asymmetrically)

## Stuff related to Raspberry Pi

### rpi-clone compatible with Debian Bookworm

The original [rpi-clone from billw](https://github.com/billw2/rpi-clone) probably doesn't work with bookworm.  
However, for me, a patched version of [rpi-clone from framps](https://github.com/framps/rpi-clone) did the job!

### Upgrading from buster to bookworm

Upgrading a Raspberry Pi from buster to bookworm is currently NOT recommended (as of December 2023)!
If you want to try it anyway, here is a [HOWTO: Upgrade Raspberry Pi OS from Bullseye to Bookworm](<https://gist.github.com/jauderho/6b7d42030e264a135450ecc0ba521bd8>).  

But be sure to clone (backup) your installation BEFORE upgrading - cloning my Buster Openhab installation with rpi-clone (see above, either version) did the job! Make sure the clone you created is bootable before proceeding!
