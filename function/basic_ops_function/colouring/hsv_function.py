from tkinter import messagebox,simpledialog
from PIL import ImageTk 

def hsv(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    # Pengambilan referensi jendela induk
    parent_window = image_label.winfo_toplevel()
    
    # Dialog input seleksi HSV
    hsv_type = simpledialog.askstring("Tentukan Komponen HSV",
      "Pilihan anda (HUE, SATURATION, atau VALUE): ",
      parent=parent_window
    )

    # Penanganan pembatalan input
    if hsv_type is None:
      return
    
    # Normalisasi string input
    hsv_choice = hsv_type.lower()

    # Referensi gambar asli
    img_a = image_label.original_image
    # Konversi mode warna HSV
    img_hsv = img_a.convert('HSV')
    # Pemisahan channel warna (H, S, V)
    (h, s, v) = img_hsv.split()
    
    # Inisialisasi variabel teks status
    text = ""

    # Logika seleksi channel berdasarkan input
    if hsv_choice == "hue":
      # Pengambilan channel Hue
      result_img = h
      text="Hasil Operasi HSV (Hue Channel)"
      
    elif hsv_choice == "saturation":
      # Pengambilan channel Saturation
      result_img = s
      text="Hasil Operasi HSV (Saturation Channel)"
      
    elif hsv_choice == "value":
      # Pengambilan channel Value
      result_img = v
      text="Hasil Operasi HSV (Value Channel)"
      
    else:
      # Notifikasi input tidak valid
      messagebox.showwarning("Input Tidak Valid", f"Pilihan '{hsv_type}' tidak dikenali.")
      return
    
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
      messagebox.showerror("Error", f"Gagal melakukan HSV: {e}")