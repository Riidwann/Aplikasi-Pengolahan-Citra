from tkinter import *
from menu.basic_ops import *
from menu.file import *

#Setup window
window = Tk()
window.geometry("800x600")
window.title("Aplikasi Pengolahan Citra Digital-copyright © dedlain.Dev(2023)")

#Menubar
menubar = Menu(window)
window.config(menu=menubar)

#Image holder
image_label = Label(window, text="Belum ada gambar yang dibuka")
image_label.pack(fill="both", expand=True, padx=20, pady=20)

#Tab file
file_menu(menubar, image_label, window)

#Tab operasi
basic_ops_menu(menubar)

window.mainloop()