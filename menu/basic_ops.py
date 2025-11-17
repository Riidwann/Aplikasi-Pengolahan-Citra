from tkinter import Menu
from function.basic_ops_function.arithmethics.add_function import *
from function.basic_ops_function.arithmethics.negative_function import *
from function.basic_ops_function.arithmethics.substract_function import *
from function.basic_ops_function.arithmethics.multiply_function import *
from function.basic_ops_function.arithmethics.divide_function import *
from function.basic_ops_function.boolean.not_function import *
from function.basic_ops_function.boolean.and_function import *
from function.basic_ops_function.boolean.or_function import *
from function.basic_ops_function.boolean.xor_function import *
from function.basic_ops_function.thresholding_function import *
from function.basic_ops_function.convolution_function import *
from function.basic_ops_function.fourier_transform_function import *
from function.basic_ops_function.geometrics.translation_function import *
from function.basic_ops_function.geometrics.rotation_function import *
from function.basic_ops_function.geometrics.zooming_function import *
from function.basic_ops_function.geometrics.flipping_function import *
from function.basic_ops_function.geometrics.cropping_function import *
from function.basic_ops_function.colouring.binary_function import *
from function.basic_ops_function.colouring.grayscale_function import *
from function.basic_ops_function.colouring.rgb_function import *
from function.basic_ops_function.colouring.hsv_function import *

def basic_ops_menu(menubar, image_label, image_result_label, result_text_label):
  #Tab basic ops
  basicOps = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="Basic Ops", menu=basicOps)
  basicOps.add_command(label="Negative", command=lambda:negative(image_label, image_result_label, result_text_label), )
  basicOps.add_command(label="Thresholding", command=lambda:thresholding(image_label, image_result_label, result_text_label))
  basicOps.add_command(label="Convolution", command=lambda:convolution(image_label, image_result_label, result_text_label))
  basicOps.add_command(label="Fourier Transform", command=lambda:fourier_transform(image_label, image_result_label, result_text_label))

  #Submenu arithmetic -start-
  arithmeticMenu = Menu(basicOps, tearoff=0)
  basicOps.add_cascade(label="Arithmetic", menu=arithmeticMenu)
  arithmeticMenu.add_command(label="Add (+)", command=lambda:add(image_label, image_result_label, result_text_label))
  arithmeticMenu.add_command(label="Subtract (-)", command=lambda:substract(image_label, image_result_label, result_text_label))
  arithmeticMenu.add_command(label="Multiply (x)", command=lambda:multiply(image_label, image_result_label, result_text_label))
  arithmeticMenu.add_command(label="Divide (/)", command=lambda:divide(image_label, image_result_label, result_text_label))
  #Submenu arithmetic -end-

  #Submenu boolean -start-
  booleanMenu = Menu(basicOps, tearoff=0)
  basicOps.add_cascade(label="Boolean", menu=booleanMenu)
  booleanMenu.add_command(label="NOT", command=lambda:boolean_not(image_label, image_result_label, result_text_label))
  booleanMenu.add_command(label="AND", command=lambda:boolean_and(image_label, image_result_label, result_text_label))
  booleanMenu.add_command(label="OR", command=lambda:boolean_or(image_label, image_result_label, result_text_label))
  booleanMenu.add_command(label="XOR", command=lambda:boolean_xor(image_label, image_result_label, result_text_label))
  #Submenu boolean -end-

  #Submenu geometrics -start-
  geometricMenu = Menu(basicOps, tearoff=0)
  basicOps.add_cascade(label="Geometrics", menu=geometricMenu)
  geometricMenu.add_command(label="Translation", command=lambda:translation(image_label, image_result_label, result_text_label))
  geometricMenu.add_command(label="Rotation", command=lambda:rotation(image_label, image_result_label, result_text_label))
  geometricMenu.add_command(label="Zooming", command=lambda:zooming(image_label, image_result_label, result_text_label))
  geometricMenu.add_command(label="Flipping", command=lambda:flipping(image_label, image_result_label, result_text_label))
  geometricMenu.add_command(label="Cropping", command=lambda:cropping(image_label, image_result_label, result_text_label))
  #Submenu geometrics -end-
 
  #Submenu colouring -start-
  colouringMenu = Menu(basicOps, tearoff=0)
  basicOps.add_cascade(label="Colouring", menu=colouringMenu)
  colouringMenu.add_command(label="Binary", command=lambda:binary(image_label, image_result_label, result_text_label))
  colouringMenu.add_command(label="Grayscale", command=lambda:grayscale(image_label, image_result_label, result_text_label))
  colouringMenu.add_command(label="RGB", command=lambda:rgb(image_label, image_result_label, result_text_label))
  colouringMenu.add_command(label="HSV", command=lambda:hsv(image_label, image_result_label, result_text_label))
  colouringMenu.add_command(label="CMY")
  colouringMenu.add_command(label="YUV")
  colouringMenu.add_command(label="YIQ")
  colouringMenu.add_command(label="Pseudo")
  #Submenu colouring -end-