from tkinter import messagebox,simpledialog
from PIL import ImageTk 

def cmy(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    # Dialog seleksi komponen CMY
    cmy_type = simpledialog.askstring("Tentukan Komponen CMY",
      "Pilihan anda (CYAN, MAGENTA, atau YELLOW): ",
    )

    # Penanganan pembatalan input
    if cmy_type is None:
      return
    
    # Normalisasi string input
    cmy_choice = cmy_type.lower()

    # Referensi gambar asli
    img_a = image_label.original_image
    # Konversi mode warna CMYK
    img_cmyk = img_a.convert('CMYK')
    # Pemisahan channel warna (C, M, Y, K)
    (c, m, y, k) = img_cmyk.split()
    
    # Inisialisasi variabel teks status
    text = ""

    # Logika seleksi channel berdasarkan input
    if cmy_choice == "cyan":
      # Pengambilan channel Cyan
      result_img = c
      text="Hasil Operasi CMY (Cyan Channel)"
      
    elif cmy_choice == "magenta":
      # Pengambilan channel Magenta
      result_img = m 
      text="Hasil Operasi CMY (Magenta Channel)"
      
    elif cmy_choice == "yellow":
      # Pengambilan channel Yellow
      result_img = y 
      text="Hasil Operasi CMY (Yellow Channel)"
      
    else:
      # Notifikasi input tidak valid
      messagebox.showwarning("Input Tidak Valid", f"Pilihan '{cmy_type}' tidak dikenali.")
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
      messagebox.showerror("Error", f"Gagal melakukan CMY: {e}")