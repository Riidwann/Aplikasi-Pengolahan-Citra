from tkinter import messagebox, filedialog, simpledialog
from PIL import Image, ImageTk

def cropping(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  img_a = image_label.original_image
  width, height = img_a.size

  try:
    parent_window = image_label.winfo_toplevel()

    left = simpledialog.askinteger(
      "Cropping (1/4)",
      f"Masukkan koordinat X-Kiri: ",
      initialvalue=0, minvalue=0, maxvalue=width, parent=parent_window
    )
    if left is None:
      return
    
    upper = simpledialog.askinteger(
      "Cropping (2/4)",
      f"Masukkan koordinat Y-Atas: ",
      initialvalue=0, minvalue=0, maxvalue=height, parent=parent_window
    )
    if upper is None:
      return
    
    right = simpledialog.askinteger(
      "Cropping (3/4)",
      f"Masukkan koordinat X-Kanan\n({left+1} s/d {width}): ",
      initialvalue=left+1, minvalue=left+1, maxvalue=width, parent=parent_window
    )
    if right is None:
      return
    
    bottom = simpledialog.askinteger(
      "Cropping (4/4)",
      f"Masukkan koordinat Y-Bawah\n({upper+1} s/d {height}): ",
      initialvalue=upper+1, minvalue=upper+1, maxvalue=height, parent=parent_window
    )
    if bottom is None:
      return
    
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  if left >= right or upper >= bottom:
    messagebox.showwarning("Error Koordinat", "Koordinat tidak valid\n'Kanan' harus > 'Kiri' dan 'Bawah' harus > 'Atas'.")
    return
  
  try:
    box = (left, upper, right, bottom)
    result_img = img_a.crop(box)
    image_result_label.image_result = result_img
    img_display = result_img.copy()
    img_display.thumbnail((760, 560))
    tk_image = ImageTk.PhotoImage(img_display)
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    result_text_label.config(text=f"Hasil Cropping")
  
  except Exception as e:
    messagebox.showerror("Error", f"Gagal crop: {e}")