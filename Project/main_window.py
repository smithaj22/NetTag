#!/usr/bin/env python
'''This is the main window of the NetTag GUI. It displays a logo and
has a button to start the process. When button is clicked, get_id.py is
called to find the board to then call New_file_list.py to get the available
binaries and options.'''

import pygtk
pygtk.require('2.0')
import gtk
#import testerAll.py
import New_file_list
import os
import sys
import subprocess

board = "will get Id from get_id"
target_selected = "file manually selected"
binary_file = "bin file to flasH"
runOrDebug = 0 #0 for run 1 for debug

class StartWin:
    def callback_getId(self, widget):
	New_file_list.board_selected = "board0" 
	print New_file_list.board_selected
       	print "Start was selected.."
 #       board = testerAll.findBoard()
        print board
#	New_file_list.board_selected = board
        New_file_list.OptionWindow()

    def callback_file_window(self, widget):
        New_file_list.board_selected = target_selected
        print New_file_list.board_selected
        print "Board was selected.."
	self.manualStartButton.set_text(str(target_selected))
        New_file_list.OptionWindow()


    def change_target(self, widget):
	target_selected = str(widget.get_active_text())
    
    def close_application(self, widget):
        #Change this to maybe turn off NetTag
        os.system("sudo shutdown -h now")
	gtk.main_quit()
        return False

    def __init__(self):
        #window settings
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
	gtk.Window.fullscreen(self.window)
        # self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.connect("delete_event", self.close_application)
        self.window.set_size_request(480,250)
        self.window.set_title("NetTag")
	

        #Logo - inserted as image
        self.logo = gtk.Image()
        self.logo.set_from_file("Pics/miniLogo.png")
        # self.logo.queue_resize
	
	####Combo box###
        self.comboList = gtk.combo_box_new_text()
        self.comboList.connect("changed", self.change_target)
#        self.comboList.set_active(0)
	os.chdir("boards")
	chipNames = subprocess.check_output("ls")
	chipNames = chipNames.split("\n")

        for indexFile in range(len(chipNames)):
            self.comboList.append_text(chipNames[indexFile])
#            #print 'File: ', binaries_available.binary_names$
		
#        self.comboList.append_text("STM ")
 #       self.comboList.append_text("TI ")

	


	
        #Button- auto start
        self.startButton = gtk.Button("Search for board")
        self.startButton.connect("clicked", self.callback_getId)
        self.startButton.set_tooltip_text("Click to find board")

	#Button- manual start
        self.manualStartButton = gtk.Button("Select board")
        self.manualStartButton.connect("clicked", self.callback_file_window)
        
        

	#exit button and logo
	self.exitBox = gtk.HBox()

	self.exitButton = gtk.Button(" X ")
	self.exitButton.connect("clicked", self.close_application)
	self.exitBox.pack_start(self.exitButton)

	self.welcomeLabel = gtk.Label("Welcome! Connect board then select 'Start'")	
	self.exitBox.pack_start(self.welcomeLabel)


        self.box = gtk.VBox()
	self.box.pack_start(self.exitBox)
        self.box.pack_start(self.logo)
        self.box.pack_start(self.comboList, False, False)

	self.startBox = gtk.HBox()
	
        self.startBox.pack_start(self.startButton)
	self.startBox.pack_start(self.manualStartButton)
	self.box.pack_start(self.startBox)
        # self.box.pack_start(self.shut_down_pi)

        #add and display on window
        self.window.add(self.box)
	#Added here
#	self.window.add(self.exitButton)
        self.window.set_border_width(0)
        self.window.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    StartWin()
    main()
