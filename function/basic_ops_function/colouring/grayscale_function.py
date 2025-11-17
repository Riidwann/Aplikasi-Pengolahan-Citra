from tkinter import messagebox
from PIL import ImageTk 

def grayscale(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return

  try:
    img_a = image_label.original_image
    img_gray = img_a.convert('L')
    result_img = img_gray.convert('RGB')
    image_result_label.image_result = result_img
    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image 
    result_text_label.config(text="Hasil Operasi Grayscale")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan grayscale: {e}")