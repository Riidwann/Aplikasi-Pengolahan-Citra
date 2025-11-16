from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import numpy as np

def divide(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showerror("Error", "Belum ada gambar")
    return
  
  try:
    file_path = filedialog.askopenfilename(title="Pilih gambar")
    if not file_path:
      return
    img_b = Image.open(file_path)
  
  except Exception as e:
    messagebox.showerror("Error", f"Gagal membuka gambar: {e}")
    return

  try:
    img_a = image_label.original_image
    target_size = img_a.size
    img_b_resized = img_b.resize(target_size, Image.LANCZOS)

    img_a_rgb = img_a.convert('RGB')
    img_b_rgb = img_b_resized.convert('RGB')

    a_np = np.array(img_a_rgb).astype(float)
    b_np = np.array(img_b_rgb).astype(float)
    b_np[b_np == 0] = 1.0
    result_np = (a_np * 255.0) / b_np
    result_np = np.clip(result_np, 0, 255)

    result_img = Image.fromarray(result_np.astype('uint8'), 'RGB')
    image_result_label.image_result = result_img

    img_display = result_img.copy()
    img_display.thumbnail((760,560))
    tk_image = ImageTk.PhotoImage(img_display)
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image

    result_text_label.config(text="Hasil Operasi Divide")
  
  except Exception as e:
    messagebox.showerror("Error", f"Gagal melakukan divide: {e}")