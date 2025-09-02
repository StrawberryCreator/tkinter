from tkinter import *
from tkinter.ttk import *

window = Tk ()
window.geometry ("300x300")
window.config (bg = "white")
window.title ("Lesson 2 | menu bar")

progress = Progressbar (window, orient = HORIZONTAL, length = 100, mode = "indeterminate")

"""
def updateProgress (value):
    progress["value"] = value
    if value < 100:
        window.after (1000, updateProgress, value + 20)

def startProgress ():
    progress ["value"] = 0
    updateProgress (20)
"""

def startProgress ():
    progress.start (10)
    window.after (10000, progress.stop)

progress.pack (pady = 50)

start = Button (window, text = "start", command = startProgress)
start.pack ()

spin = Spinbox (window, from_ = 0, to = 10)
spin.pack (pady = 50)

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