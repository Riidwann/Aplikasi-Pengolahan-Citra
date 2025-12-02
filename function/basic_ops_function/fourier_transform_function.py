import numpy as np
from numpy.fft import fft2, fftshift
from PIL import Image, ImageTk
from tkinter import messagebox

def fourier_transform(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    # Referensi gambar asli
    img_a = image_label.original_image
    # Konversi mode grayscale (L)
    img_gray = img_a.convert('L')
    # Transformasi ke array numerik
    f = np.array(img_gray)
    
    # Eksekusi Fast Fourier Transform 2D
    f_transform = fft2(f)
    # Pergeseran komponen frekuensi nol ke tengah
    f_shift = fftshift(f_transform)
    
    # Kalkulasi spektrum magnitudo
    magnitude_spectrum = np.log(1 + np.abs(f_shift))
    # Pencarian nilai minimum dan maksimum
    min_val = np.min(magnitude_spectrum)
    max_val = np.max(magnitude_spectrum)
    
    # Normalisasi rentang nilai ke format 8-bit (0-255)
    if max_val == min_val:
        result_normalized = np.zeros_like(magnitude_spectrum, dtype='uint8')
    else:
        result_normalized = 255 * (magnitude_spectrum - min_val) / (max_val - min_val)
    
    # Konversi tipe data array
    result_uint8 = result_normalized.astype('uint8')
    # Rekonstruksi objek gambar dari array
    result_img = Image.fromarray(result_uint8, 'L')
    
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
    result_text_label.config(text="Hasil Fourier Transform")

  except Exception as e:
      # Penanganan eksepsi proses
      messagebox.showerror("Error", f"Gagal Fourier Transform: {e}")