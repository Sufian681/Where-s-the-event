from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showinfo("Virus Detected", "A virus has been detected on your system!")
button = Button(root, text="Scan for Viruses", command=msg)
button.place(x=40, y=80)
root.mainloop()

