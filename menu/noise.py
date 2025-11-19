from tkinter import Menu
from function.noise_function.gaussian_noise_function import *
from function.noise_function.rayleigh_noise_function import *
from function.noise_function.erlang_noise_function import *
from function.noise_function.exponential_noise_function import *
from function.noise_function.uniform_noise_function import *
from function.noise_function.impulse_noise_function import *

def noise_menu(menubar, image_label, image_result_label, result_text_label):
  noise = Menu(menubar, tearoff=0)
  menubar.add_cascade(label="Noise", menu=noise)
  noise.add_command(label="Gaussian Noise",command=lambda:gaussian_noise(image_label, image_result_label, result_text_label))
  noise.add_command(label="Rayleigh Noise", command=lambda:rayleigh_noise(image_label, image_result_label, result_text_label))
  noise.add_command(label="Erlang (Gamma) Noise", command=lambda:erlang_noise(image_label, image_result_label, result_text_label))
  noise.add_command(label="Exponential Noise", command=lambda:exponential_noise(image_label, image_result_label, result_text_label))
  noise.add_command(label="Uniform Noise", command=lambda:uniform_noise(image_label,image_result_label, result_text_label))
  noise.add_command(label="Impulse Noise", command=lambda:impulse_noise(image_label,image_result_label, result_text_label))