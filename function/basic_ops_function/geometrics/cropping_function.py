from tkinter import messagebox, filedialog, simpledialog
from PIL import Image, ImageTk

def cropping(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  # Referensi gambar asli dan dimensi
  img_a = image_label.original_image
  width, height = img_a.size

  try:
    # Pengambilan referensi jendela induk
    parent_window = image_label.winfo_toplevel()

    # Dialog input koordinat X-Kiri
    left = simpledialog.askinteger(
      "Cropping (1/4)",
      f"Masukkan koordinat X-Kiri: ",
      initialvalue=0, minvalue=0, maxvalue=width, parent=parent_window
    )
    # Penanganan pembatalan input
    if left is None:
      return
    
    # Dialog input koordinat Y-Atas
    upper = simpledialog.askinteger(
      "Cropping (2/4)",
      f"Masukkan koordinat Y-Atas: ",
      initialvalue=0, minvalue=0, maxvalue=height, parent=parent_window
    )
    if upper is None:
      return
    
    # Dialog input koordinat X-Kanan (batas minimal > X-Kiri)
    right = simpledialog.askinteger(
      "Cropping (3/4)",
      f"Masukkan koordinat X-Kanan\n({left+1} s/d {width}): ",
      initialvalue=left+1, minvalue=left+1, maxvalue=width, parent=parent_window
    )
    if right is None:
      return
    
    # Dialog input koordinat Y-Bawah (batas minimal > Y-Atas)
    bottom = simpledialog.askinteger(
      "Cropping (4/4)",
      f"Masukkan koordinat Y-Bawah\n({upper+1} s/d {height}): ",
      initialvalue=upper+1, minvalue=upper+1, maxvalue=height, parent=parent_window
    )
    if bottom is None:
      return
    
  except Exception as e:
    # Notifikasi error input
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  # Validasi logika koordinat crop
  if left >= right or upper >= bottom:
    messagebox.showwarning("Error Koordinat", "Koordinat tidak valid\n'Kanan' harus > 'Kiri' dan 'Bawah' harus > 'Atas'.")
    return
  
  try:
    # Definisi area potong (tuple)
    box = (left, upper, right, bottom)
    # Eksekusi pemotongan gambar
    result_img = img_a.crop(box)
    
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
    result_text_label.config(text=f"Hasil Cropping")
  
  except Exception as e:
    # Penanganan eksepsi proses
    messagebox.showerror("Error", f"Gagal crop: {e}")