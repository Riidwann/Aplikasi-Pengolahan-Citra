from tkinter import messagebox,simpledialog
from PIL import Image, ImageTk
import numpy as np

def yiq(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    parent_window = image_label.winfo_toplevel()
    yiq_type = simpledialog.askstring("Tentukan Komponen YIQ",
      "Pilihan anda (Y, I, atau Q): ",
      parent=parent_window
    )

    if yiq_type is None:
      return
    
    yiq_choice = yiq_type.lower()
    
    img_a = image_label.original_image
    img_rgb = img_a.convert('RGB')
    rgb_array = np.array(img_rgb, dtype=np.float32)

    r = rgb_array[:, :, 0]
    g = rgb_array[:, :, 1]
    b = rgb_array[:, :, 2]

    y_channel = 0.299*r + 0.587*g + 0.114*b
    i_channel = 0.596*r - 0.274*g - 0.322*b
    q_channel = 0.211*r - 0.523*g + 0.312*b
    
    text = ""
    result_array = None

    if yiq_choice == "y":
      result_array = y_channel
      text="Hasil: YIQ (Y/Luma Channel)"
      
    elif yiq_choice == "i":
      result_array = i_channel
      text="Hasil: YIQ (I Channel)"
      
    elif yiq_choice == "q":
      result_array = q_channel
      text="Hasil: YIQ (Q Channel)"
      
    else:
      messagebox.showwarning("Input Tidak Valid", f"Pilihan '{yiq_type}' tidak dikenali.")
      return
    
    min_val = np.min(result_array)
    max_val = np.max(result_array)
    if max_val == min_val:
        result_norm = np.zeros_like(result_array)
    else:
        result_norm = 255 * (result_array - min_val) / (max_val - min_val)

    result_uint8 = result_norm.astype('uint8')
    result_img = Image.fromarray(result_uint8, 'L')
    
    result_img = result_img.convert('RGB')

    image_result_label.image_result = result_img
    img_display = result_img.copy()
    img_display.thumbnail((760,560))
    tk_image = ImageTk.PhotoImage(img_display)
    
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    result_text_label.config(text=text)

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan YIQ: {e}")