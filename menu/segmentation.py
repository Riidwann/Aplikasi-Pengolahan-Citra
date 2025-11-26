from tkinter import Menu
from function.segmentation.otsu_thresholding_function import *
from function.segmentation.morphological_operations_function import *
from function.segmentation.color_quantization_function import *

def segmentation_menu(menubar, image_label, image_result_label, result_text_label):
  segmentation = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="Segmentation", menu=segmentation)
  segmentation.add_command(label="Otsu Thresholding",command=lambda:otsu(image_label, image_result_label, result_text_label))
  segmentation.add_command(label="Morphological",command=lambda:morphology(image_label, image_result_label, result_text_label))
  segmentation.add_command(label="Color Quantization",command=lambda:color(image_label, image_result_label, result_text_label))