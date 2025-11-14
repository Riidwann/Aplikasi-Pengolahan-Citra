from tkinter import filedialog, messagebox
from function.file_function.save_as_function import *

def save(image_label):
  if not hasattr(image_label, 'original_image'):
    return
  
  if hasattr(image_label, 'file_path') and image_label.file_path:
    try:
      image_label.original_image.save(image_label.file_path)
      messagebox.showinfo("Sukses", f"Gambar berhasil disimpan")
    except Exception as e:
      messagebox.showerror("Error", f"Gagal menyimpan file: {e}")
  else:
    save_as(image_label)