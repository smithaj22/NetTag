#!/usr/bin/python

import os

def findBoard ():
    var = "output.txt"
    path =  "/usr/local/share/openocd/scripts/target"
    target = "Error Chip Not Found"
    boardVar = "Could not find board"
    configVar = "Could not find config file"
    os.system("sudo openocd -f /usr/local/share/openocd/scripts/interface/rp.cfg -c 'init' -c 'shutdown' 2>"+ var)

    searchfile = open(var)
    for line in searchfile:
        if "0x4ba00477" in line:
            #print line
            target = "stm32f4x.cfg"
            boardVar =  "Found target board: " + target
    searchfile.close()


    print boardVar

    files = []
    for (path, dirnames, filenames) in os.walk(path):
        files.extend(os.path.join(name) for name in filenames)

    for i in files:
    	if i == target:
    		configVar = "Found config file: " + i
    		#f = open( 'file.txt', 'w' )
    		#f.write( i)
    		#f.close()


    print configVar
    return target
