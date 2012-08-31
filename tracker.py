import pygtk
pygtk.require("2.0")

import gtk
import gtk.glade

class MainWin:

    def __init__(self):
        self.widgets = gtk.glade.XML("mainWindow.glade")
        signals = { \
            "on_entri1_activate" : self.on_button1_clicked, \
            "on_button1_clicked" : self.on_button1_clicked,
            "gtk_main_quit" : gtk.main_quit
        }

        self.widgets.signal_autoconnect(signals)