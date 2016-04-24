import sys
import os
import subprocess

'''Input is a board name, board names each have their own
folder.  In my example boards/board1/a.out a2.out...
'homepath' is the directory from your current where the boards are stored,
example: current working directory is the Desktop, boards would be a folder.

From there either pass a name or enter it when the program is running.
It will move into that folder or create a directory if not there already.
The return values can either be an array of program names
or two arrays one with the path the other with the name depending on how
someone would want it served up.  Email me or text me with questions'''
binary_names = []
binary_exe = []

def binAvailable (board):

    print board
    homepath="boards"
    if len(board) <1: #if len(sys.argv) <2:
        board = raw_input('Please enter a board: ')
    # else:
    #     board = sys.argv[1]

    os.chdir(homepath)
    ls = subprocess.check_output("ls")
    ls=ls.decode("utf-8")
    ls="\n"+ls
    # print(ls)
    formatBoard = "\n"+board+"\n"  #used so substring doesnt get caught
    print formatBoard
    if formatBoard not in ls: #board not found
        makeDir = input("That board does not exist.  Would you like to add it? (Y/N)\n")
        if makeDir == 'Y' or makeDir == 'y':
            os.mkdir(board)
            print("Directory Created\nExiting")
    else: #board found create arrays from directory tree
        os.chdir(board)

    #http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
        # binary_names = [] #set there as attribures
        # binary_exe = []
        for root, directories, files in os.walk("."):
            for filename in files:
                filepath = os.path.join(root, filename)
                binary_names.append(filename)
                binary_exe.append(filepath)
        #print(binary_names)
        #print(binary_exe)
        print("Program Complete")
