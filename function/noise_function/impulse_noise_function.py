from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 
import numpy as np
import random

# Fungsi untuk menambahkan Impulse (Salt & Pepper) Noise pada gambar
def impulse_noise(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    amount = simpledialog.askfloat(
        "Impulse (Salt & Pepper) Noise", 
        "Masukkan 'amount' (densitas) noise (0.01 s/d 1.0):",
        initialvalue=0.05,
        minvalue=0.01,
        maxvalue=1.0, 
    )
    if amount is None: 
      return
      
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  # Menambahkan Impulse (Salt & Pepper) Noise pada gambar
  try:
    img_a = image_label.original_image

    img_rgb = img_a.convert('RGB')
    img_array = np.array(img_rgb)

    noisy_array = np.copy(img_array)
    height, width, _ = noisy_array.shape
    
    num_salt = int(np.ceil(amount * noisy_array.size * 0.5 / 3))
    num_pepper = int(np.ceil(amount * noisy_array.size * 0.5 / 3))

    # Koordinat salt (y, x) acak
    for _ in range(num_salt):
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)
        noisy_array[y, x] = 255 # Set ke Putih
        
    # Koordinat pepper (y, x) acak
    for _ in range(num_pepper):
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)
        noisy_array[y, x] = 0 # Set ke Hitam

    result_img = Image.fromarray(noisy_array, 'RGB')
    # Menyimpan hasil pada label hasil
    image_result_label.image_result = result_img

    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image # Jaga referensi
    
    result_text_label.config(text=f"Hasil Impulse Noise (Amount: {amount*100}%)")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan Impulse Noise: {e}")