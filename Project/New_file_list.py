#!/usr/bin/env python

'''This class is called by mian_window.py when a board is found and displays
in a combo box the available binary files that can be flashed to this board
using binaries_available.py.
It also dislays an option to run or debug the program and then a button to
start the process to flash the file to run or debug it.'''

# example radiobuttons.py
import pygtk
pygtk.require('2.0')
import gtk
import binaries_available
import os
import testerAll
import main_window
#import startGDB

binary_selected = "0"
board_selected =""# testerAll.hexToChip()

class OptionWindow:

    def close_application(self, widget):
        #Change this to maybe turn off NetTag
        os.system("sudo shutdown -h now")
	#gtk.main_quit()
        return False

    def change_bin_file(self, widget):
        binary_selected = "./" + str(widget.get_active_text())
        message = "File selected:  " + str(widget.get_active_text())
        self.fileLabel.set_text(message)
	self.extraLabel.set_text("Now select Flash or Debug")
        print str(binary_selected) + " selected"
	
    def text_change(self, widget):
        # bin_ava_binary_to_flash = widget.get_active_text()
        print "text changed"

    def flash_to_board(self, widget):
        print "file will now flash"
	#Add call to FLASH CODE
       	startGDB.startGDB(binary_selected)

    def debug(self, widget, data=None):
	#Add call to DEBUG CODE
        print "debug function will be called"

    def __init__(self):
	message = " "
	
	binaries_available.binAvailable(main_window.board)
       ####window settings###
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	gtk.Window.fullscreen(self.window)
        # self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.connect("delete_event", self.close_application)
        self.window.set_size_request(240,150)
        self.window.set_title("NetTag")
        self.box = gtk.VBox()
#        self.window.maximize()

        ####Label###
        self.upperLabel = gtk.Label("\tSelect a file")
        self.upperLabel.set_text("Board found:  " + str(board_selected))
		
	#Exit button
	self.upperBox = gtk.HBox()
	self.exitButton = gtk.Button("X")
	self.exitButton.connect("clicked" , self.close_application)
	self.upperBox.pack_start(self.exitButton)

	self.upperBox.pack_start(self.upperLabel)

	self.box.pack_start(self.upperBox)
	#file label button
	self.fileLabel = gtk.Label("Select file")
	self.fileLabel.set_text("Select File")	
	self.box.pack_start(self.fileLabel)

	#Run or debug button
	self.extraLabel = gtk.Label(" ");


        ####Combo box###
        self.comboList = gtk.combo_box_new_text()
        self.comboList.connect("changed", self.change_bin_file)
#        self.comboList.set_active(0)

        for indexFile in range(len(binaries_available.binary_names)):
            self.comboList.append_text(binaries_available.binary_names[indexFile])
            #print 'File: ', binaries_available.binary_names[indexFile]
	    
        self.box.pack_start(self.comboList, False, False)

        ###Two buttons (to run or debug)###
        self.twoButtonBox = gtk.HBox()
        #Flash
        self.FlashButton = gtk.Button("Flash");
        self.FlashButton.connect("clicked", self.flash_to_board)
        self.twoButtonBox.pack_start(self.FlashButton)
        #Debug
        self.DebugButton = gtk.Button("Debug");
        self.DebugButton.connect("clicked", self.debug)
        self.twoButtonBox.pack_start(self.DebugButton)

	self.box.pack_start(self.extraLabel)
        self.box.pack_start(self.twoButtonBox)

        self.window.add(self.box)
        self.window.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    OptionWindow()
    main()
