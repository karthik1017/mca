from tkinter import *
window = Tk()
window.title("Welcome to MCA app")
window.geometry('400x400')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()