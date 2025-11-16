import numpy as np
from numpy.fft import fft2, fftshift
from PIL import Image, ImageTk
from tkinter import messagebox

def fourier_transform(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    img_a = image_label.original_image
    img_gray = img_a.convert('L')
    f = np.array(img_gray)
    
    f_transform = fft2(f)
    f_shift = fftshift(f_transform)
    
    magnitude_spectrum = np.log(1 + np.abs(f_shift))
    min_val = np.min(magnitude_spectrum)
    max_val = np.max(magnitude_spectrum)
    
    if max_val == min_val:
        result_normalized = np.zeros_like(magnitude_spectrum, dtype='uint8')
    else:
        result_normalized = 255 * (magnitude_spectrum - min_val) / (max_val - min_val)
    
    result_uint8 = result_normalized.astype('uint8')
    result_img = Image.fromarray(result_uint8, 'L')
    
    image_result_label.image_result = result_img

    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    result_text_label.config(text="Hasil Fourier Transform")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal Fourier Transform: {e}")