from tkinter import Menu
from function.edge_detection_function.first_differential_gradient import sobel_function as sobel_custom
from function.edge_detection_function.first_differential_gradient.prewitt_function import *
from function.edge_detection_function.first_differential_gradient.robert_function import *
from function.edge_detection_function.second_differential_gradient.laplacian_function import *
from function.edge_detection_function.second_differential_gradient.log_function import *
from function.edge_detection_function.second_differential_gradient.canny_function import *
from function.edge_detection_function.compass_function import *

def edge_detection_menu(menubar, image_label, image_result_label, result_text_label):
    # Menu utama Edge Detection
    edgeDetectionMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Edge Detection", menu=edgeDetectionMenu)

    # 1st Differential Gradient
    firstDiffMenu = Menu(edgeDetectionMenu, tearoff=0)
    edgeDetectionMenu.add_cascade(label="1st Differential Gradient", menu=firstDiffMenu)
    firstDiffMenu.add_command(label="Sobel", command=lambda: sobel_custom.sobel(image_label, image_result_label, result_text_label))
    firstDiffMenu.add_command(label="Prewitt", command=lambda: prewitt(image_label, image_result_label, result_text_label))
    firstDiffMenu.add_command(label="Robert", command=lambda: robert(image_label, image_result_label, result_text_label))

    # 2nd Differential Gradient
    secondDiffMenu = Menu(edgeDetectionMenu, tearoff=0)
    edgeDetectionMenu.add_cascade(label="2nd Differential Gradient", menu=secondDiffMenu)
    secondDiffMenu.add_command(label="Laplacian", command=lambda: laplacian(image_label, image_result_label, result_text_label))
    secondDiffMenu.add_command(label="Laplace of Gaussian (LoG)", command=lambda: log_filter(image_label, image_result_label, result_text_label))
    secondDiffMenu.add_command(label="Canny", command=lambda: canny(image_label, image_result_label, result_text_label))

    # Compass
    edgeDetectionMenu.add_command(label="Compass", command=lambda: compass_edge_detection(image_label, image_result_label, result_text_label))
