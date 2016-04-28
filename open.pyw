#!/usr/bin/python

import os
#os.system("sudo openocd -f /home/pi/NetTag/Project/jtag_connection/rpi_gpio_jtag_stellaris.cfg")
os.system("sudo openocd -f /home/pi/NetTag/Project/jtag_connection/rpi_gpio_swd_stm32f4.cfg")
raw_input()
