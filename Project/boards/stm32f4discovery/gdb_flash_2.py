#!/usr/bin/python
import gdb
#print(sys.argv(1))
#prog = argv[4]
gdb.execute("target remote localhost:3333")
gdb.execute("monitor reset halt")
gdb.execute("monitor flash write_image erase /home/pi/NetTag/Project/boards/stm32f4discovery/blinky_sequence.elf")
gdb.execute("monitor reset run")
#gdb.execute("monitor reset halt")
#gdb.execute("file /home/pi/NetTag/target_bin/stm32f4/blinky_flash_all.elf ")
#gdb.execute("load ")
gdb.execute('set confirm off')
gdb.execute('quit')

