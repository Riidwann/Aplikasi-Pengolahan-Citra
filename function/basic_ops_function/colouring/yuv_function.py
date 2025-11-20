from tkinter import messagebox,simpledialog
from PIL import ImageTk, Image
import numpy as np

def yuv(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    # Pengambilan referensi jendela induk
    parent_window = image_label.winfo_toplevel()
    # Dialog input seleksi komponen YUV
    yuv_type = simpledialog.askstring("Tentukan Komponen YUV",
      "Pilihan anda (Y, U, atau V): ",
      parent=parent_window
    )

    # Penanganan pembatalan input
    if yuv_type is None:
      return
    
    # Normalisasi string input
    yuv_choice = yuv_type.lower()
    
    # Referensi gambar asli
    img_a = image_label.original_image
    # Konversi mode warna RGB
    img_rgb = img_a.convert('RGB')
    # Transformasi ke array numerik float
    rgb_array = np.array(img_rgb, dtype=np.float32)

    # Ekstraksi channel warna individual
    r = rgb_array[:, :, 0]
    g = rgb_array[:, :, 1]
    b = rgb_array[:, :, 2]

    # Kalkulasi manual konversi RGB ke YUV
    y_channel = 0.299*r + 0.587*g + 0.114*b #luminance (grayscale)
    u_channel = -0.147*r - 0.289*g + 0.436*b #chrominance 1 (biru)
    v_channel = 0.615*r - 0.515*g - 0.100*b #chrominance 2 (merah)
    
    # Inisialisasi variabel hasil
    text = ""
    result_array = None

    # Logika seleksi channel berdasarkan input
    if yuv_choice == "y":
      result_array = y_channel
      text="Hasil: YUV (Y/Luma Channel)"
      
    elif yuv_choice == "u":
      result_array = u_channel
      text="Hasil: YUV (U Channel)"
      
    elif yuv_choice == "v":
      result_array = v_channel
      text="Hasil: YUV (V Channel)"
      
    else:
      # Notifikasi input tidak valid
      messagebox.showwarning("Input Tidak Valid", f"Pilihan '{yuv_type}' tidak dikenali.")
      return
    
    # Kalkulasi nilai minimum dan maksimum
    min_val = np.min(result_array)
    max_val = np.max(result_array)
    
    # Normalisasi rentang nilai array (0-255)
    if max_val == min_val:
        result_norm = np.zeros_like(result_array)
    else:
        result_norm = 255 * (result_array - min_val) / (max_val - min_val)

    # Konversi tipe data ke integer 8-bit
    result_uint8 = result_norm.astype('uint8')
    # Rekonstruksi objek gambar grayscale
    result_img = Image.fromarray(result_uint8, 'L')
    # Konversi ulang ke mode RGB
    result_img = result_img.convert('RGB')

    # Penyimpanan hasil pada atribut label
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
    result_text_label.config(text=text)

  except Exception as e:
      # Penanganan eksepsi proses
      messagebox.showerror("Error", f"Gagal melakukan YUV: {e}")