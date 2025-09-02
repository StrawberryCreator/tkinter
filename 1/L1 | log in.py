from tkinter import *

window = Tk ()
window.geometry ("500x250")
window.title ("Lesson 1 | log in")
window.config (bg = "white")

userlabel = Label (window, text = "username:", font = ("calibri", 30, "bold"), bg = "white", fg = "black")
userlabel.place (x = 25, y = 25)

userinput = Entry (window, width = 30)
userinput.place (x = 200, y = 35)

passwordlabel = Label (window, text = "password:", font = ("calibri", 30, "bold"), bg = "white", fg = "black")
passwordlabel.place (x = 25, y = 100)

passwordinput = Entry (window, width = 30)
passwordinput.place (x = 200, y = 110)

def togglePassword ():
    passwordinput.config (show = "" if showPass.get () else "*")

showPass = BooleanVar ()
checkbox = Checkbutton (window, text = "show password", variable = showPass, command = togglePassword)
checkbox.place (x = 25, y = 175)

button = Button (window, text = "submit", command = window.destroy)
button.place (x = 300, y = 175)

#menubar

from tkinter.ttk import *

bar = Menu (window)

file = Menu (bar, tearoff = 0)
bar.add_cascade (label = "file", menu = file)
file.add_command (label = "open", command = None)
file.add_command (label = "save", command = None)
file.add_separator ()
file.add_command (label = "new", command = None)

window.config (menu = bar)

mainloop ()