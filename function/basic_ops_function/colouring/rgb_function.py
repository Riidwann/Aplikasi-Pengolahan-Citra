from tkinter import messagebox,simpledialog
from PIL import ImageTk 

def rgb(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  # Dialog input seleksi RGB
  rgb_type = simpledialog.askstring("Tentukan warna RGB",
  "Pilihan anda (RED, GREEN, ATAU BLUE): ")

  # Penanganan pembatalan input (Cancel)
  if rgb_type is None:
    return
  
  # Normalisasi string input
  rgb_choice = rgb_type.lower()

  # Logika seleksi channel Merah
  if rgb_choice == "red":
    try:
      # Referensi gambar asli
      img_a = image_label.original_image
      # Konversi mode warna RGB
      img_rgb = img_a.convert('RGB')
      
      # Pemisahan channel warna
      (r, g, b) = img_rgb.split()
      # Pengambilan channel Merah
      result_img = r
      # Konversi ulang ke format RGB
      result_img = result_img.convert('RGB')

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
      result_text_label.config(text="Hasil Operasi RGB (RED)")

    except Exception as e:
        # Penanganan eksepsi proses
        messagebox.showerror("Error", f"Gagal mengambil Red Channel: {e}")

  # Logika seleksi channel Hijau
  elif rgb_choice == "green":
    try:
      # Referensi gambar asli
      img_a = image_label.original_image
      # Konversi mode warna RGB
      img_rgb = img_a.convert('RGB')
      # Pemisahan channel warna
      (r, g, b) = img_rgb.split()

      # Pengambilan channel Hijau & konversi
      result_img = g.convert('RGB')
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
      result_text_label.config(text="Hasil Operasi RGB(Green)")

    except Exception as e:
        # Penanganan eksepsi proses
        messagebox.showerror("Error", f"Gagal mengambil Green Channel: {e}")
  
  # Logika seleksi channel Biru (Default/Else)
  else:
    try:
      # Referensi gambar asli
      img_a = image_label.original_image
      # Konversi mode warna RGB
      img_rgb = img_a.convert('RGB')
      # Pemisahan channel warna
      (r, g, b) = img_rgb.split()
      # Pengambilan channel Biru & konversi
      result_img = b.convert('RGB')
      
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
      result_text_label.config(text="Hasil Operasi RGB(BLUE)")

    except Exception as e:
        # Penanganan eksepsi proses
        messagebox.showerror("Error", f"Gagal mengambil Blue Channel: {e}")