from PIL import ImageTk, ImageOps
from tkinter import messagebox, simpledialog

def flipping(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  flipping_type = simpledialog.askstring("Tentukan jenis Flipping",
  "Pilihan anda (Horizontal atau Vertikal): ")
  flipping_choice = flipping_type.lower()

  if flipping_type is None:
    return
  
  if flipping_choice == "horizontal":
    try:
      img_a = image_label.original_image
      result_img = ImageOps.mirror(img_a)
      image_result_label.image_result = result_img
      img_display = result_img.copy()
      img_display.thumbnail((760, 560))
      tk_image = ImageTk.PhotoImage(img_display)
      image_result_label.config(image=tk_image)
      image_result_label.image = tk_image
      result_text_label.config(text="Hasil Operasi Flip Horizontal")

    except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan flip horizontal: {e}")
  else:
    try:
      img_a = image_label.original_image
      result_img = ImageOps.flip(img_a)
      image_result_label.image_result = result_img
      img_display = result_img.copy()
      img_display.thumbnail((760, 560))
      tk_image = ImageTk.PhotoImage(img_display)
      image_result_label.config(image=tk_image)
      image_result_label.image = tk_image
      result_text_label.config(text="Hasil Operasi Flip Vertikal")

    except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan flip vertikal: {e}")


