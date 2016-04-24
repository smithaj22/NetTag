#!/usr/bin/env python

'''This class is called by mian_window.py when a board is found and displays
in a combo box the available binary files that can be flashed to this board
using binaries_available.py.
It also dislays an option to run or debug the program and then a button to
start the process to flash the file to run or debug it.'''
#new comment
# example radiobuttons.py
import pygtk
pygtk.require('2.0')
import gtk
import binaries_available
#import startGDB

binary_selected = "0"

class OptionWindow:

    def close_application(self, widget, event, data=None):
        #Change this to maybe turn off NetTag
        gtk.main_quit()
        return False

    def change_bin_file(self, widget):
        binary_selected = widget.get_active_text()
        message = str(binary_selected) +" file selected\nNow select Flash or Debug"
        self.upperLabel.set_text(message)
        print str(binary_selected) + " selected"

    def text_change(self, widget):
        # bin_ava_binary_to_flash = widget.get_active_text()
        print "text changed"

    def flash_to_board(self, widget):
        print "file will now flash"
        ####Path hardcoded for now
 #       startGDB.startGDB(binaries_available.binary_exe[0])

    def debug(self, widget, data=None):
        print "debug function will be called"


    def __init__(self):
        ####window settings###
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        gtk.Window.fullscreen(self.window)
        # self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.connect("delete_event", self.close_application)
        self.window.set_size_request(240,150)
        self.window.set_title("NetTag")
        self.box = gtk.VBox()
        self.window.maximize()

        ####Label###
        self.upperLabel = gtk.Label("\tSelect a file\nThen Flash or Debug")
        self.box.pack_start(self.upperLabel)

        ##List for comboBox -  http://stackoverflow.com/questions/23757738/python-gtk-how-to-insert-items-from-list-to-combobox
        
        self.fileList = gtk.ListStore(str)
        files = binaries_available.binary_names

        for row in files:
            self.fileList.append([row[0]])
        cell = gtk.CellRendererText()
        comboB = gtk.ComboBox(model=self.fileList)
        self.box.pack_start(cell)
        comboB.set_attributes(cell, text = 0)




        ####Combo box###
        # '''having trouble clicking on the combo box when it shows on GUI'''
        # self.comboList = gtk.combo_box_new_text()
        # self.comboList.connect("changed", self.change_bin_file)
        # self.comboList.set_active(0)
        # self.comboList.append_text("Text 0")
        # self.comboList.append_text("Text 1")
        # self.comboList.append_text("Text 2")

        # self.box.pack_start(self.comboList, False, False)

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

        self.box.pack_start(self.twoButtonBox)

        self.window.add(self.box)
        self.window.show_all()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    OptionWindow()
    main()
