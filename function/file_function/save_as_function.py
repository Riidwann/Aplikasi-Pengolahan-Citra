from tkinter import filedialog, messagebox

def save_as(image_result_label):
  if not hasattr(image_result_label, 'image_result'):
    messagebox.showwarning("Belum ada gambar")
    return
  try:
    file_types = [
      ("PNG", "*.png"),
      ("JPG", "*.jpg"),
      ("PDF", "*.pdf"),
      ("All", "*.*")
    ]
    save_path = filedialog.asksaveasfilename(filetypes=file_types, defaultextension=".png")

    if not save_path:
      return
    
    image_result_label.image_result.save(save_path)
    image_result_label.file_path = save_path
    messagebox.showinfo("Sukses", f"Gambar berhasil disimpan")
  
  except Exception as e:
    messagebox.showerror("Error", f"Gagal menyimpan file: {e}")
