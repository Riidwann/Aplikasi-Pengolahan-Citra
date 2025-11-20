from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

def translation(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    # Pengambilan referensi jendela induk
    parent_window = image_label.winfo_toplevel()

    # Dialog input translasi sumbu X
    x_val = simpledialog.askinteger(
      "Translasi Sumbu X",
      "Masukkan nilai X:",
      initialvalue=50,
      parent=parent_window
    )
    # Penanganan pembatalan input
    if x_val is None:
      return
    
    # Dialog input translasi sumbu Y
    y_val = simpledialog.askinteger(
      "Translasi Sumbu Y",
      "Masukkan nilai Y: ",
      initialvalue=30,
      parent=parent_window
    )
    if y_val is None:
      return
  
  except Exception as e:
    # Notifikasi error input
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  try:
    # Referensi gambar asli
    img_a = image_label.original_image
    
    # Definisi matriks transformasi Affine (translasi)
    transform_matrix = (1, 0, -x_val, 0, 1, -y_val)
    
    # Eksekusi transformasi geometri
    result_img = img_a.transform(
      img_a.size,
      Image.AFFINE,
      transform_matrix,
      fillcolor = 'black'
    )

    # Penyimpanan hasil pada atribut label
    image_result_label.image_result = result_img
    # Duplikasi dan resize untuk preview
    img_display = result_img.copy()
    img_display.thumbnail((760, 560))
    # Konversi format Tkinter
    tk_image = ImageTk.PhotoImage(img_display)
    
    # Rendering gambar ke layar
    image_result_label.config(image=tk_image)
    # Pencegahan penghapusan memori otomatis
    image_result_label.image = tk_image
    # Update teks label status
    result_text_label.config(text=f"Hasil Translasi (X:{x_val}, Y:{y_val})")
  
  except Exception as e:
    # Penanganan eksepsi proses
    messagebox.showerror("Error", f"Gagal translasi: {e}")