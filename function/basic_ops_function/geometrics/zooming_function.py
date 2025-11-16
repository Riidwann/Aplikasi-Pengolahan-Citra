from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 

def zooming(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:  
    zoom_factor = simpledialog.askfloat(
        "Zooming/Scaling", 
        "Masukkan faktor zoom (contoh: 2.0 atau 0.5):",
        initialvalue=1.5,
        minvalue=0.1,
        maxvalue=10.0,
    )

    if zoom_factor is None:
      return 
      
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  try:
    img_a = image_label.original_image
    old_width, old_height = img_a.size
    new_width = int(old_width * zoom_factor)
    new_height = int(old_height * zoom_factor)
    
    result_img = img_a.resize(
        (new_width, new_height), 
        resample=Image.LANCZOS 
    )
    
    image_result_label.image_result = result_img

    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image 
    result_text_label.config(text=f"Hasil Zoom ({zoom_factor}x)")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan zooming: {e}")