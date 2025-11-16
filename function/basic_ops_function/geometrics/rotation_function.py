from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 

def rotation(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    angle_val = simpledialog.askinteger(
        "Rotasi Gambar", 
        "Masukkan sudut rotasi (derajat):\nPositif = Berlawanan arah jarum jam",
        initialvalue=45,
        minvalue=-360,
        maxvalue=360,
    )
    
    if angle_val is None:
      return 
      
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  try:
    img_a = image_label.original_image
    result_img = img_a.rotate(
        angle_val, 
        resample=Image.BICUBIC,
        expand=True, 
        fillcolor='black' 
    )
    
    image_result_label.image_result = result_img

    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    
    image_result_label.config(image=tk_image)
    
    image_result_label.image = tk_image 
    
    result_text_label.config(text=f"Hasil Rotasi ({angle_val}°)")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal rotasi: {e}")