from tkinter import *
from tkinter.ttk import *

window = Tk ()
window.geometry ("300x200")
window.config (bg = "white")
window.title ("Lesson 2 | menu bar")

def startProgress ():
    import time as t
    progress ["value"] = 20
    window.update_idletasks ()
    t.sleep (1)
    progress ["value"] = 40
    window.update_idletasks ()
    t.sleep (1)
    progress ["value"] = 60
    window.update_idletasks ()
    t.sleep (1)
    progress ["value"] = 80
    window.update_idletasks ()
    t.sleep (1)
    progress ["value"] = 100

progress = Progressbar (window, orient = HORIZONTAL, length = 100, mode = "determinate")
progress.pack (pady = 50)

start = Button (window, text = "start", command = startProgress)
start.pack ()

bar = Menu (window)

file = Menu (bar, tearoff = 0)
bar.add_cascade (label = "file", menu = file)
file.add_command (label = "new", command = None)
file.add_separator ()
file.add_command (label = "open", command = None)
file.add_separator ()
file.add_command (label = "save", command = None)

edit = Menu (bar, tearoff = 0)
bar.add_cascade (label = "edit", menu = edit)
edit.add_command (label = "Undo", command = None)
edit.add_command (label = "Redo", command = None)
edit.add_separator ()
edit.add_command (label = "Cut", command = None)
edit.add_command (label = "Copy", command = None)
edit.add_command (label = "Paste", command = None)

window.config (menu = bar)

mainloop ()