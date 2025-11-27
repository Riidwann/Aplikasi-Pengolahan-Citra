from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 
import numpy as np

# Fungsi untuk menambahkan Exponential Noise pada gambar
def exponential_noise(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  # Meminta input parameter dari user
  try:
    scale = simpledialog.askfloat(
        "Exponential Noise", 
        "Masukkan 'scale' noise (kekuatan, misal: 20.0):",
        initialvalue=20.0,
        minvalue=0.1,
        maxvalue=255.0, 
    )
    
    if scale is None:
      return
      
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  # Menambahkan Exponential Noise pada gambar
  try:
    img_a = image_label.original_image
    # Konversi gambar ke array numpy
    img_rgb = img_a.convert('RGB')
    img_array = np.array(img_rgb, dtype=np.float32)
    
    height, width, channels = img_array.shape
    noise = np.random.exponential(scale, (height, width, channels))
    noisy_array = img_array + noise
    noisy_array = np.clip(noisy_array, 0, 255)
    
    result_array = noisy_array.astype(np.uint8)
    result_img = Image.fromarray(result_array, 'RGB')
    # Menyimpan hasil pada label hasil
    image_result_label.image_result = result_img

    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    
    result_text_label.config(text=f"Hasil Exponential Noise (Scale: {scale})")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan Exponential Noise: {e}")