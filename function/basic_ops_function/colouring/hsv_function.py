from tkinter import messagebox,simpledialog
from PIL import ImageTk 

def hsv(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    parent_window = image_label.winfo_toplevel()
    
    hsv_type = simpledialog.askstring("Tentukan Komponen HSV",
      "Pilihan anda (HUE, SATURATION, atau VALUE): ",
      parent=parent_window
    )

    if hsv_type is None:
      return
    
    hsv_choice = hsv_type.lower()

    img_a = image_label.original_image
    img_hsv = img_a.convert('HSV')
    (h, s, v) = img_hsv.split()
    
    text = ""


    if hsv_choice == "hue":
      result_img = h
      text="Hasil Operasi HSV (Hue Channel)"
      
    elif hsv_choice == "saturation":
      result_img = s
      text="Hasil Operasi HSV (Saturation Channel)"
      
    elif hsv_choice == "value":
      result_img = v
      text="Hasil Operasi HSV (Value Channel)"
      
    else:
      messagebox.showwarning("Input Tidak Valid", f"Pilihan '{hsv_type}' tidak dikenali.")
      return
    
    result_img = result_img.convert('RGB')

    image_result_label.image_result = result_img
    img_display = result_img.copy()
    img_display.thumbnail((760,560))
    tk_image = ImageTk.PhotoImage(img_display)
    
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    result_text_label.config(text=text)

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan HSV: {e}")