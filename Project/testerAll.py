#!/usr/bin/python
import sys
import subprocess
import os
import mmap

def hexToChip ():
    os.chdir("boards")
    chipNames = subprocess.check_output("ls") #list of boards we have
    chipNames= chipNames.split("\n") #trim up carriage return
    techName = [] #second array to store lookup values

    #go into each board folder, pull the techName and store it in corresponding point in array
    for x in range(0, len(chipNames)-1):
        os.chdir(chipNames[x])
        f = open('techName.txt', 'r')
        techName.append(f.readline())
        techName[x]=techName[x].rstrip('\n')
        f.close()
        os.chdir("..")
    os.chdir("..")

    #check output file for preset hex values
    f = open('output.txt') #change to output once openocd spits out again
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) #reduces load on memory if output gets big
    for x in range(0, len(techName)):
        if s.find(techName[x]) != -1:
            return chipNames[x]    #hex match found quit looking
    #Look through file no hex files found
    return  ('This Chip has not been logged yet')
    # return chipNames[techName.index(tName)]


def binaries_available (targetChip):
    print(targetChip)
    homepath="boards"
    if 'This Chip has not been logged yet' in targetChip:
        quit()
    # if len(sys.argv) <2:
    #     board = input('Please enter a board: ')
    # else:
    #     board = sys.argv[1]
    os.chdir(homepath)
    # ls = subprocess.check_output("ls")
    # ls=ls.decode("utf-8")
    # ls="\n"+ls
    # #print(ls)
    # formatBoard = "\n"+targetChip+"\n"  #used so substring doesnt get caught

    # if formatBoard not in ls: #board not found
    #     makeDir = input("That board does not exist.  Would you like to add it? (Y/N)\n")
    #     if makeDir == 'Y' or makeDir == 'y':
    #         os.mkdir(targetChip)
    #         print("Directory Created\nExiting")
    # else: #board found create arrays from directory tree
    #     os.chdir(targetChip)
    os.chdir(targetChip)
    #http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
    binary_names = []
    binary_exe = []
    for root, directories, files in os.walk("."):
        for filename in files:
            filepath = os.path.join(root, filename)
            binary_names.append(filename)
            binary_exe.append(filepath)
    #need to walk path and delete techName to clean it up
    print(binary_names)
    print(binary_exe)
    print("Program Complete")


def findBoard ():
    var = "output.txt"
    path =  "/usr/local/share/openocd/scripts/target"
    target = "Error Chip Not Found"
    boardVar = "Could not find board"
    configVar = "Could not find config file"
    os.system("sudo openocd -f jtag\ connection/rp.cfg -c 'init' -c 'shutdown' 2>"+ var)


    # # searchfile = open(var)
    # # for line in searchfile:
    # #     if "0x4ba00477" in line:
    # #         #print line
    # #         target = "stm32f4x.cfg"
    # #         boardVar =  "Found target board: " + target
    # # searchfile.close()
    # targetChip = "arm-cortex-m4"
    # targetBoard = "stm32f4x"
    #
    # #
    # # print boardVar
    # #
    # # files = []
    # # for (path, dirnames, filenames) in os.walk(path):
    # #     files.extend(os.path.join(name) for name in filenames)
    # #
    # # for i in files:
    # # 	if i == target:
    # # 		configVar = "Found config file: " + i
    # # 		#f = open( 'file.txt', 'w' )
    # # 		#f.write( i)
    # # 		#f.close()
    # #
    # #
    # # print configVar
    # # return target
    # return targetChip
#call order
findBoard()
binaries_available(hexToChip())

# targetChip = findBoard()
# binaries_available(targetChip)
