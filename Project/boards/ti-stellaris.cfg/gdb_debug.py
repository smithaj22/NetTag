#!/usr/bin/python
import gdb

prog=""
gdb.execute("target remote localhost:3333")
gdb.execute("monitor reset halt")
#gdb.execute("monitor flash write_image erase /home/pi/NetTag/Project/boards/stm32f4discovery/" + prog + ".elf")
#gdb.execute("monitor reset run")
#gdb.execute("monitor reset halt")
gdb.execute("file /home/pi/NetTag/Project/boards/stm32f4discovery/" + prog + ".elf")
gdb.execute("load ")
#gdb.execute('set confirm off')
#gdb.execute('quit')

