from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 
import numpy as np

# Fungsi untuk menambahkan Erlang/Gamma Noise pada gambar
def erlang_noise(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    parent_window = image_label.winfo_toplevel()
    # Meminta input parameter dari user
    shape_b = simpledialog.askinteger(
        "Erlang/Gamma Noise (1/2)", 
        "Masukkan 'Shape' (b) (bilangan bulat, misal: 2):",
        initialvalue=2,
        minvalue=1,
        maxvalue=100, 
        parent=parent_window
    )
    if shape_b is None: return
    # Meminta input parameter dari user
    scale_a = simpledialog.askfloat(
        "Erlang/Gamma Noise (2/2)", 
        "Masukkan 'Scale' (a) (kekuatan noise, misal: 20.0):",
        initialvalue=20.0,
        minvalue=0.1,
        maxvalue=255.0, 
        parent=parent_window
    )
    if scale_a is None: return
      
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  # Menambahkan Erlang/Gamma Noise pada gambar
  try:
    img_a = image_label.original_image
    # Konversi gambar ke array numpy
    img_rgb = img_a.convert('RGB')
    img_array = np.array(img_rgb, dtype=np.float32)

    height, width, channels = img_array.shape
    noise = np.random.gamma(shape_b, scale_a, (height, width, channels))
    # Menambahkan noise ke gambar asli
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
    
    result_text_label.config(text=f"Hasil Erlang Noise (Shape:{shape_b}, Scale:{scale_a})")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan Erlang Noise: {e}")