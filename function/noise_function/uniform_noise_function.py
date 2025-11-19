from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 
import numpy as np

def uniform_noise(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    parent_window = image_label.winfo_toplevel()
    
    low_val = simpledialog.askfloat(
        "Uniform Noise (1/2)", 
        "Masukkan batas BAWAH noise (misal: -50.0):",
        initialvalue=-50.0,
        minvalue=-255.0,
        maxvalue=255.0, 
        parent=parent_window
    )
    if low_val is None: 
      return

    high_val = simpledialog.askfloat(
        "Uniform Noise (2/2)", 
        "Masukkan batas ATAS noise (misal: 50.0):",
        initialvalue=50.0,
        minvalue=-255.0,
        maxvalue=255.0, 
        parent=parent_window
    )
    if high_val is None: 
      return
    
    if high_val <= low_val:
        messagebox.showwarning("Error", "'Batas Atas' harus lebih besar dari 'Batas Bawah'.")
        return
      
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  try:
    img_a = image_label.original_image
  
    img_rgb = img_a.convert('RGB')
    img_array = np.array(img_rgb, dtype=np.float32)

    height, width, channels = img_array.shape
    noise = np.random.uniform(low_val, high_val, (height, width, channels))

    noisy_array = img_array + noise
    noisy_array = np.clip(noisy_array, 0, 255)

    result_array = noisy_array.astype(np.uint8)
    result_img = Image.fromarray(result_array, 'RGB')

    image_result_label.image_result = result_img

    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)    
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    
    result_text_label.config(text=f"Hasil Uniform Noise (Range: {low_val} s/d {high_val})")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan Uniform Noise: {e}")