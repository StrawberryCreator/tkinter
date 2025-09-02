from tkinter import *
from tkinter.ttk import *

window = Tk ()
window.geometry ("300x200")
window.config (bg = "white")
window.title ("Lesson 2 | menu bar")

progress = Progressbar (window, orient = HORIZONTAL, length = 100, mode = "determinate")

def startProgress ():
    import time
    progress ["value"] = 20
    window.update_idletasks ()
    time.sleep (1)
    progress ["value"] = 40
    window.update_idletasks ()
    time.sleep (1)
    progress ["value"] = 60
    window.update_idletasks ()
    time.sleep (1)
    progress ["value"] = 80
    window.update_idletasks ()
    time.sleep (1)
    progress ["value"] = 100

progress.pack (pady = 50)

start = Button (window, text = "start", command = startProgress)
start.pack ()

mainloop ()