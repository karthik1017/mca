from tkinter import *
window = Tk()
window.title("Welcome to MCA app")
window.geometry('400x400')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me")
btn.grid(column=1, row=0)
window.mainloop()