from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk 

def zooming(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:  
    # Dialog input faktor zoom (float)
    zoom_factor = simpledialog.askfloat(
        "Zooming/Scaling", 
        "Masukkan faktor zoom (contoh: 2.0 atau 0.5):",
        initialvalue=1.5,
        minvalue=0.1,
        maxvalue=10.0,
    )

    # Penanganan pembatalan input
    if zoom_factor is None:
      return 
      
  except Exception as e:
    # Notifikasi error input
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  try:
    # Referensi gambar asli
    img_a = image_label.original_image
    # Pengambilan dimensi awal
    old_width, old_height = img_a.size
    # Kalkulasi dimensi baru berdasarkan faktor zoom
    new_width = int(old_width * zoom_factor)
    new_height = int(old_height * zoom_factor)
    
    # Eksekusi resizing gambar dengan interpolasi Lanczos
    result_img = img_a.resize(
        (new_width, new_height), 
        resample=Image.LANCZOS 
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
    result_text_label.config(text=f"Hasil Zoom ({zoom_factor}x)")

  except Exception as e:
      # Penanganan eksepsi proses
      messagebox.showerror("Error", f"Gagal melakukan zooming: {e}")