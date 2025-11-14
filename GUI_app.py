from tkinter import *
from menu.basic_ops import *
from function.basic_ops_function.add_function import *

#Setup window
window = Tk()
window.geometry("800x600")
window.title("Aplikasi Pengolahan Citra Digital-copyright © dedlain.Dev(2023)")

#Menubar
menubar = Menu(window)
window.config(menu=menubar)

#Tab file
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_separator()
file.add_command(label="Exit", command=quit)

#Tab operasi
basic_ops_menu(menubar)

window.mainloop()