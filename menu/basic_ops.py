from tkinter import Menu

def basic_ops_menu(menubar):
  #Tab basic ops
  basicOps = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="Basic Ops", menu=basicOps)
  basicOps.add_command(label="Negative")
  basicOps.add_command(label="Thresholding")
  basicOps.add_command(label="Convolution")
  basicOps.add_command(label="Fourier Transform")

  #Submenu arithmetic -start-
  arithmeticMenu = Menu(basicOps, tearoff=0)
  basicOps.add_cascade(label="Arithmetic", menu=arithmeticMenu)
  arithmeticMenu.add_command(label="Add (+)")
  arithmeticMenu.add_command(label="Subtract (-)")
  arithmeticMenu.add_command(label="Multiply (x)")
  arithmeticMenu.add_command(label="Divide (/)")
  #Submenu arithmetic -end-

  #Submenu boolean -start-
  booleanMenu = Menu(basicOps, tearoff=0)
  basicOps.add_cascade(label="Boolean", menu=booleanMenu)
  booleanMenu.add_command(label="NOT")
  booleanMenu.add_command(label="AND")
  booleanMenu.add_command(label="OR")
  booleanMenu.add_command(label="XOR")
  #Submenu boolean -end-

  #Submenu geometrics -start-
  geometricMenu = Menu(basicOps, tearoff=0)
  basicOps.add_cascade(label="Geometrics", menu=geometricMenu)
  geometricMenu.add_command(label="Translation")
  geometricMenu.add_command(label="Rotation")
  geometricMenu.add_command(label="Zooming")
  geometricMenu.add_command(label="Flipping")
  geometricMenu.add_command(label="Cropping")
  #Submenu geometrics -end-

  #Submenu colouring -start-
  colouringMenu = Menu(basicOps, tearoff=0)
  basicOps.add_cascade(label="Colouring", menu=colouringMenu)
  colouringMenu.add_command(label="Binary")
  colouringMenu.add_command(label="Grayscale")
  colouringMenu.add_command(label="RGB")
  colouringMenu.add_command(label="HSV")
  colouringMenu.add_command(label="CMY")
  colouringMenu.add_command(label="YUV")
  colouringMenu.add_command(label="YIQ")
  colouringMenu.add_command(label="Pseudo")
  #Submenu colouring -end-