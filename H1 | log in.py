from tkinter import *

#window
window = Tk()
window.geometry("500x500")
window.title("Homework 1 | ")
window.config(bg="white")

#username
username = StringVar()
userlabel = Label(window, text="username:", font=("calibri", 30, "bold"), bg="white", fg="black")
userlabel.place(relx=0.25, rely=0.1, anchor = "center")

userinput = Entry(window, width=25, textvariable=username)
userinput.place(relx=0.7, rely=0.1, anchor = "center")

#password
passwordlabel = Label(window, text="password:", font=("calibri", 30, "bold"), bg="white", fg="black")
passwordlabel.place(relx=0.25, rely=0.275, anchor = "center")

passwordinput = Entry(window, width=25, show="*")
passwordinput.place(relx=0.7, rely=0.275, anchor = "center")

#password / toggle
def togglePassword():
    passwordinput.config(show="" if showPass.get() else "*")

showPass = BooleanVar()
checkbox = Checkbutton(window, text="show password", variable=showPass, command=togglePassword)
checkbox.place(relx=0.25, rely=0.45, anchor = "center")

#terms of service
tosTxt = """
Please accept these terms before logging in. 
By checking the box, you agree to use this software responsibly. 
The developers are not liable for any data loss or errors.
"""
toslabel = StringVar()
toslabel = Label(window, text=tosTxt, font=("calibri", 13, "bold"), bg="white", fg="black",)
toslabel.place(relx=0.5, rely=0.8, anchor = "center")

#terms of service / toggle
def toggleTOS():
    toslabel.config(text="" if showTOS.get() else tosTxt)

showTOS = BooleanVar()
toscheckbox = Checkbutton(window, text="agree to the terms of service", variable=showTOS, command=toggleTOS)
toscheckbox.place(relx=0.5, rely=0.65, anchor = "center")

#error label
errorlabel = Label(window, text="", font=("calibri", 20, "bold", "italic"), bg="white", fg="black")
errorlabel.place(relx=0.5, rely=0.55, anchor = "center")

#error function
def error():
    if len(username.get()) < 6:
        errorlabel.config(text="username must be longer than 5 characters")
    elif len(username.get()) > 12:
        errorlabel.config(text="username must be shorter than 13 characters")
    elif len(passwordinput.get()) < 6:
        errorlabel.config(text="password must be longer than 5 characters")
    elif len(passwordinput.get()) > 12:
        errorlabel.config(text="password must be shorter than 13 characters")
    elif not showTOS.get():
        errorlabel.config(text="please agree to the terms of service")
    else:
        errorlabel.config(text="")
        window.destroy()

button = Button(window, text="submit", command=error)
button.place(relx=0.7, rely=0.45, anchor = "center")

#menubar
bar = Menu(window)

file = Menu(bar, tearoff=0)
bar.add_cascade(label="file", menu=file)
file.add_command(label="open", command=None)
file.add_command(label="save", command=None)
file.add_separator()
file.add_command(label="new", command=None)

window.config(menu=bar)

mainloop()