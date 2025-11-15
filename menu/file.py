from tkinter import Menu
from function.file_function.open_function import *
from function.file_function.save_as_function import *
from function.file_function.save_function import *

def file_menu(menubar, image_label, window, image_result_label):
  file = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="File", menu=file)
  file.add_command(label="Open", command=lambda: open_file(image_label))
  file.add_command(label="Save", command=lambda: save(image_result_label))
  file.add_command(label="Save As", command=lambda:save_as(image_result_label))
  file.add_separator()
  file.add_command(label="Exit", command=window.quit)