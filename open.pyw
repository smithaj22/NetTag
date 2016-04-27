#!/usr/bin/python

import os
os.system("sudo openocd -f /home/pi/NetTag/Project/jtag_connection/rpi_gpio_jtag_stellaris.cfg")

raw_input()
