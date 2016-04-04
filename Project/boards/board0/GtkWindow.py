
#!/usr/bin/python


import gtk

window = gtk.Window()

button = gtk.Button('Hello')

window.connect("delete-event", gtk.main_quit)

window.show_all()
