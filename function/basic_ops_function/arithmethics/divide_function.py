from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
import numpy as np

def divide(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showerror("Error", "Belum ada gambar")
    return
  
  try:
    # Dialog seleksi file gambar pembagi
    file_path = filedialog.askopenfilename(title="Pilih gambar")
    if not file_path:
      return
    # Pemuatan objek gambar kedua
    img_b = Image.open(file_path)
  
  except Exception as e:
    # Notifikasi kegagalan input
    messagebox.showerror("Error", f"Gagal membuka gambar: {e}")
    return

  try:
    # Referensi gambar utama
    img_a = image_label.original_image
    # Penyesuaian dimensi gambar kedua
    target_size = img_a.size
    img_b_resized = img_b.resize(target_size, Image.LANCZOS)

    # Konversi mode warna RGB
    img_a_rgb = img_a.convert('RGB')
    img_b_rgb = img_b_resized.convert('RGB')

    # Transformasi ke array numerik float
    a_np = np.array(img_a_rgb).astype(float)
    b_np = np.array(img_b_rgb).astype(float)
    # Pencegahan error pembagian nol
    b_np[b_np == 0] = 1.0
    # Kalkulasi pembagian pixel dengan skala
    result_np = (a_np * 255.0) / b_np
    # Pembatasan rentang nilai (0-255)
    result_np = np.clip(result_np, 0, 255)

    # Rekonstruksi objek gambar hasil
    result_img = Image.fromarray(result_np.astype('uint8'), 'RGB')
    # Penyimpanan hasil pada atribut
    image_result_label.image_result = result_img

    # Duplikasi dan resize untuk preview
    img_display = result_img.copy()
    img_display.thumbnail((760,560))
    # Konversi ke format Tkinter
    tk_image = ImageTk.PhotoImage(img_display)
    # Rendering gambar ke layar
    image_result_label.config(image=tk_image)
    # Pencegahan penghapusan memori otomatis
    image_result_label.image = tk_image

    # Update teks label status
    result_text_label.config(text="Hasil Operasi Divide")
  
  except Exception as e:
    # Penanganan eksepsi proses
    messagebox.showerror("Error", f"Gagal melakukan divide: {e}")