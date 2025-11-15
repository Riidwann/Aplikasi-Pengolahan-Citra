from tkinter import filedialog, messagebox
from function.file_function.save_as_function import *

def save(image_result):
  if not hasattr(image_result, 'image_result'):
    return
  
  if hasattr(image_result, 'file_path') and image_result.file_path:
    try:
      image_result.image_result.save(image_result.file_path)
      messagebox.showinfo("Sukses", f"Gambar berhasil disimpan")
    except Exception as e:
      messagebox.showerror("Error", f"Gagal menyimpan file: {e}")
  else:
    save_as(image_result)