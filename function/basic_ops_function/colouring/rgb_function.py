from tkinter import messagebox,simpledialog
from PIL import ImageTk 

def rgb(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  rgb_type = simpledialog.askstring("Tentukan warna RGB",
  "Pilihan anda (RED, GREEN, ATAU BLUE): ")
  rgb_choice = rgb_type.lower()

  if rgb_type is None:
    return
  
  if rgb_choice == "red":
    try:
      img_a = image_label.original_image
      img_rgb = img_a.convert('RGB')
      
      (r, g, b) = img_rgb.split()
      result_img = r
      result_img = result_img.convert('RGB')

      image_result_label.image_result = result_img
      img_display = result_img.copy()
      img_display.thumbnail((760,560))

      tk_image = ImageTk.PhotoImage(img_display)
      
      image_result_label.config(image=tk_image)
      image_result_label.image = tk_image
      result_text_label.config(text="Hasil Operasi RGB (RED)")

    except Exception as e:
        messagebox.showerror("Error", f"Gagal mengambil Red Channel: {e}")

  elif rgb_choice == "green":
    try:
      img_a = image_label.original_image
      img_rgb = img_a.convert('RGB')
      (r, g, b) = img_rgb.split()

      result_img = g.convert('RGB')
      image_result_label.image_result = result_img
      img_display = result_img.copy()
      img_display.thumbnail((760,560))
      tk_image = ImageTk.PhotoImage(img_display)

      image_result_label.config(image=tk_image)
      image_result_label.image = tk_image
      result_text_label.config(text="Hasil Operasi RGB(Green)")

    except Exception as e:
        messagebox.showerror("Error", f"Gagal mengambil Green Channel: {e}")
  else:
    try:
      img_a = image_label.original_image
      img_rgb = img_a.convert('RGB')
      (r, g, b) = img_rgb.split()
      result_img = b.convert('RGB')
      
      image_result_label.image_result = result_img
      img_display = result_img.copy()
      img_display.thumbnail((760,560))
      tk_image = ImageTk.PhotoImage(img_display)
      image_result_label.config(image=tk_image)
      image_result_label.image = tk_image
      result_text_label.config(text="Hasil Operasi RGB(BLUE)")

    except Exception as e:
        messagebox.showerror("Error", f"Gagal mengambil Blue Channel: {e}")
