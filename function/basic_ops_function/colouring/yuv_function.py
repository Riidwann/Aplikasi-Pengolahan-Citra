from tkinter import messagebox,simpledialog
from PIL import ImageTk, Image
import numpy as np

def yuv(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    parent_window = image_label.winfo_toplevel()
    yuv_type = simpledialog.askstring("Tentukan Komponen YUV",
      "Pilihan anda (Y, U, atau V): ",
      parent=parent_window
    )

    if yuv_type is None:
      return
    
    yuv_choice = yuv_type.lower()
    
    img_a = image_label.original_image
    img_rgb = img_a.convert('RGB')
    rgb_array = np.array(img_rgb, dtype=np.float32)

    r = rgb_array[:, :, 0]
    g = rgb_array[:, :, 1]
    b = rgb_array[:, :, 2]

    y_channel = 0.299*r + 0.587*g + 0.114*b
    u_channel = -0.147*r - 0.289*g + 0.436*b
    v_channel = 0.615*r - 0.515*g - 0.100*b
    
    text = ""
    result_array = None

    if yuv_choice == "y":
      result_array = y_channel
      text="Hasil: YUV (Y/Luma Channel)"
      
    elif yuv_choice == "u":
      result_array = u_channel
      text="Hasil: YUV (U Channel)"
      
    elif yuv_choice == "v":
      result_array = v_channel
      text="Hasil: YUV (V Channel)"
      
    else:
      messagebox.showwarning("Input Tidak Valid", f"Pilihan '{yuv_type}' tidak dikenali.")
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
      messagebox.showerror("Error", f"Gagal melakukan YUV: {e}")