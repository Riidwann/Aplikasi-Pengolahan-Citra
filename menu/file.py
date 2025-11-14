from tkinter import Menu
from function.file_function.open_function import *

def file_menu(menubar, image_label, window):
  file = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="File", menu=file)
  file.add_command(label="Open", command=lambda: open_file(image_label))
  file.add_command(label="Save")
  file.add_command(label="Save As")
  file.add_separator()
  file.add_command(label="Exit", command=window.quit)