from PIL import ImageTk, ImageChops
from tkinter import messagebox

def boolean_not(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    img_a = image_label.original_image
    img_a_rgb = img_a.convert('RGB')
    result_img = ImageChops.invert(img_a_rgb)
    image_result_label.image_result = result_img

    img_display = result_img.copy()
    img_display.thumbnail((760, 560))

    tk_image = ImageTk.PhotoImage(img_display)
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image

    result_text_label.config(text="Hasil Operasi NOT")
  
  except Exception as e:
    messagebox.showerror("Error", f"Gagal melakukan NOT: {e}")