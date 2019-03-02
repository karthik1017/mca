from tkinter import *
top = Tk()
mb = Checkbutton(top,text = "savory",relief = RAISED)
mb.grid()
mb.menu = Menu(mb,tearoff = 0)
mb["menu"] = mb.menu

mb.menu.add_checkbutton(label = 'Bajji')
mb.menu.add_checkbutton(label = 'pakkoda')
top.mainloop()