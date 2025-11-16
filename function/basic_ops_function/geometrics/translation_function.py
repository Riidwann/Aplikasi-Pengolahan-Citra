from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

def translation(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    parent_window = image_label.winfo_toplevel()
    x_val = simpledialog.askinteger(
      "Translasi Sumbu X",
      "Masukkan nilai X:",
      initialvalue=50,
      parent=parent_window
    )
    if x_val is None:
      return
    
    y_val = simpledialog.askinteger(
      "Translasi Sumbu Y",
      "Masukkan nilai Y: ",
      initialvalue=30,
      parent=parent_window
    )
    if y_val is None:
      return
  
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  try:
    img_a = image_label.original_image
    transform_matrix = (1, 0, -x_val, 0, 1, -y_val)
    result_img = img_a.transform(
      img_a.size,
      Image.AFFINE,
      transform_matrix,
      fillcolor = 'black'
    )

    image_result_label.image_result = result_img
    img_display = result_img.copy()
    img_display.thumbnail((760, 560))
    tk_image = ImageTk.PhotoImage(img_display)
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    result_text_label.config(text=f"Hasil Translasi (X:{x_val}, Y:{y_val})")
  
  except Exception as e:
    messagebox.showerror("Error", f"Gagal translasi: {e}")
     
