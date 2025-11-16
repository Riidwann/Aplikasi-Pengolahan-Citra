from PIL import Image, ImageTk, ImageChops
from tkinter import messagebox, filedialog

def substract(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    return
  
  try:
    file_path = filedialog.askopenfilename(title="Pilig gambar kedua")
    if not file_path:
      return
    
    img_b = Image.open(file_path)

  except Exception as e:
    messagebox.showerror("Error", f"Gagal membuka gambar kedua: {e}")
    return
  
  try:
    img_a = image_label.original_image
    target_size = img_a.size
    img_b_resize = img_b.resize(target_size, Image.LANCZOS)

    img_a_rgb = img_a.convert('RGB')
    img_b_rgb = img_b_resize.convert('RGB')
    result_img = ImageChops.subtract(img_a_rgb, img_b_rgb)

    image_result_label.image_result = result_img
    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    result_text_label.config(text="Hasil Operasi Substract")
  
  except Exception as e:
    messagebox.showerror("Error", f"Gagal melakukan substract: {e}")