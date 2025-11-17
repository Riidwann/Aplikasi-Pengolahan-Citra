from tkinter import messagebox, simpledialog
from PIL import ImageTk, ImageOps

def pseudo(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    parent_window = image_label.winfo_toplevel()

    color_dark = simpledialog.askstring(
        "Pseudocolor (1/2)", 
        "Masukkan warna untuk area GELAP:\n(Contoh: 'blue', 'black', atau '#FF0000')",
        initialvalue="blue",
        parent=parent_window
    )
    if color_dark is None: return

    color_bright = simpledialog.askstring(
        "Pseudocolor (2/2)", 
        "Masukkan warna untuk area TERANG:\n(Contoh: 'red', 'yellow', atau '#00FF00')",
        initialvalue="yellow",
        parent=parent_window
    )
    if color_bright is None: return

  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  try:
    img_a = image_label.original_image
    img_gray = img_a.convert('L')
    result_img = ImageOps.colorize(
        img_gray, 
        black=color_dark, 
        white=color_bright
    )

    image_result_label.image_result = result_img

    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    
    result_text_label.config(text=f"Hasil Pseudo ({color_dark} -> {color_bright})")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal Pseudo-Coloring: {e}\n(Pastikan nama warna valid)")