from tkinter import messagebox,simpledialog
from PIL import ImageTk 

def cmy(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    cmy_type = simpledialog.askstring("Tentukan Komponen CMY",
      "Pilihan anda (CYAN, MAGENTA, atau YELLOW): ",
    )

    if cmy_type is None:
      return
    
    cmy_choice = cmy_type.lower()

    img_a = image_label.original_image
    img_cmyk = img_a.convert('CMYK')
    (c, m, y, k) = img_cmyk.split()
    
    text = ""

    if cmy_choice == "cyan":
      result_img = c
      text="Hasil Operasi CMY (Cyan Channel)"
      
    elif cmy_choice == "magenta":
      result_img = m 
      text="Hasil Operasi CMY (Magenta Channel)"
      
    elif cmy_choice == "yellow":
      result_img = y 
      text="Hasil Operasi CMY (Yellow Channel)"
      
    else:
      messagebox.showwarning("Input Tidak Valid", f"Pilihan '{cmy_type}' tidak dikenali.")
      return

    result_img = result_img.convert('RGB')
    image_result_label.image_result = result_img
    img_display = result_img.copy()
    img_display.thumbnail((760,560))
    tk_image = ImageTk.PhotoImage(img_display)
    
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    result_text_label.config(text=text)

  except Exception as e:
      messagebox.showerror("Error", f"Gagal melakukan CMY: {e}")