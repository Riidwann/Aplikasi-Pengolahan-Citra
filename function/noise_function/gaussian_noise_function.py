from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 
import numpy as np

# Fungsi untuk menambahkan Gaussian Noise pada gambar
def gaussian_noise(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    sigma = simpledialog.askinteger(
        "Gaussian Noise", 
        "Masukkan kekuatan noise:",
        initialvalue=25,
        minvalue=1,
        maxvalue=255, 
    )
    
    if sigma is None:
      return
      
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  # Menambahkan Gaussian Noise pada gambar
  try:
    img_a = image_label.original_image
    img_rgb = img_a.convert('RGB')
    img_array = np.array(img_rgb, dtype=np.float32)
    
    height, width, channels = img_array.shape    
    mean = 0
    noise = np.random.normal(mean, sigma, (height, width, channels))
    noisy_array = img_array + noise
    noisy_array = np.clip(noisy_array, 0, 255)
    
    result_array = noisy_array.astype(np.uint8)
    result_img = Image.fromarray(result_array, 'RGB')
    image_result_label.image_result = result_img
    # Menampilkan hasil pada label hasil
    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    
    result_text_label.config(text=f"Hasil Operasi Gaussian Noise (Sigma: {sigma})")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan Gaussian Noise: {e}")