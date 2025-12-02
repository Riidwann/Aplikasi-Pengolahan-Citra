from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 

def rotation(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    # Dialog input sudut rotasi (integer)
    angle_val = simpledialog.askinteger(
        "Rotasi Gambar", 
        "Masukkan sudut rotasi (derajat):\nPositif = Berlawanan arah jarum jam",
        initialvalue=45,
        minvalue=-360,
        maxvalue=360,
    )
    
    # Penanganan pembatalan input
    if angle_val is None:
      return 
      
  except Exception as e:
    # Notifikasi error input
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  try:
    # Referensi gambar asli
    img_a = image_label.original_image
    # Eksekusi rotasi dengan perluasan kanvas dan interpolasi halus
    result_img = img_a.rotate(
        angle_val, 
        resample=Image.BICUBIC,
        expand=True, 
        fillcolor='black' 
    )
    
    # Penyimpanan hasil pada atribut label
    image_result_label.image_result = result_img

    # Duplikasi dan resize untuk preview
    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    # Konversi format Tkinter
    tk_image = ImageTk.PhotoImage(img_display)
    
    # Rendering gambar ke layar
    image_result_label.config(image=tk_image)
    
    # Pencegahan penghapusan memori otomatis
    image_result_label.image = tk_image 
    
    # Update teks label status
    result_text_label.config(text=f"Hasil Rotasi ({angle_val}°)")

  except Exception as e:
      # Penanganan eksepsi proses
      messagebox.showerror("Error", f"Gagal rotasi: {e}")