import tkinter 
from tkinter import messagebox

# hide main window
root = tkinter.Tk()
#root.wihtdraw()

# message box display
messagebox.showerror("Error","error.message")
messagebox.showerror("warning","warning message")
messagebox.showinfo("Information","Informative message")
root.mainloop()
