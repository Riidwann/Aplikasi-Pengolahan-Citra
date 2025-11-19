from tkinter import *
from menu.basic_ops import *
from menu.file import *
from menu.noise import *
from menu.edge_detection import *
from menu.enhancement import enhancement_menu


#Setup windowp
window = Tk()
window.geometry("800x600")
window.title("Aplikasi Pengolahan Citra Digital-copyright © ekstrakDaunBajakah.Dev(2025)")

#Menubar
menubar = Menu(window)
window.config(menu=menubar)

#Frame image
main_frame = Frame(window)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

#Original image
left_column_frame = Frame(main_frame)
left_column_frame.pack(side=LEFT, fill="both", expand=True, padx=10)
original_text_label = Label(left_column_frame, text="Gambar Asli", font=("Arial", 14, "bold"))
original_text_label.pack(side=TOP, pady=(0, 5))

image_label = Label(left_column_frame, text="Belum ada gambar", relief="sunken", bd=1)
image_label.pack(fill="both", expand=True)

#Result image
right_column_frame = Frame(main_frame)
right_column_frame.pack(side=RIGHT, fill="both", expand=True, padx=10)
result_text_label = Label(right_column_frame, text="Gambar Hasil", font=("Arial", 14, "bold"))
result_text_label.pack(side=TOP, pady=(0, 5))

image_result_label = Label(right_column_frame, text="Belum ada hasil", relief="sunken", bd=1)
image_result_label.pack(fill="both", expand=True)

## APP MENU ##
#Tab file
file_menu(menubar, image_label, window, image_result_label)

#Tab operasi
basic_ops_menu(menubar, image_label, image_result_label, result_text_label)

#Tab noise
noise_menu(menubar, image_label, image_result_label, result_text_label)

#Tab edge detection
edge_detection_menu(menubar, image_label, image_result_label, result_text_label)

#Tab enhancement
enhancement_menu(menubar, image_label, image_result_label, result_text_label)

window.mainloop()