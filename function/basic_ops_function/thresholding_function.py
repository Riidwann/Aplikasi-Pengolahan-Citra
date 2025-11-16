from tkinter import messagebox, simpledialog 
from PIL import Image, ImageTk 

def thresholding(image_label, image_result_label, result_text_label):
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    thresh_val = simpledialog.askinteger(
        "Nilai Threshold", 
        "Masukkan nilai threshold (0-255):",
        initialvalue=128,  
        minvalue=0,         
        maxvalue=255        
    )
    
    if thresh_val is None:
      return
      
  except Exception as e:
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return

  try:
    img_a = image_label.original_image
    
    img_gray = img_a.convert('L')
    result_img = img_gray.point(lambda p: 255 if p > thresh_val else 0)

    image_result_label.image_result = result_img
    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    tk_image = ImageTk.PhotoImage(img_display)
    image_result_label.config(image=tk_image)
    image_result_label.image = tk_image
    
    result_text_label.config(text=f"Hasil Thresholding (Nilai: {thresh_val})")

  except Exception as e:
      messagebox.showerror("Error", f"Gagal thresholding: {e}")