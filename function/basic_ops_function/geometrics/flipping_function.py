from PIL import ImageTk, ImageOps
from tkinter import messagebox, simpledialog

def flipping(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  # Dialog input jenis flipping
  flipping_type = simpledialog.askstring("Tentukan jenis Flipping",
  "Pilihan anda (Horizontal atau Vertikal): ")

  # Penanganan pembatalan input
  if flipping_type is None:
    return
  
  # Normalisasi string input
  flipping_choice = flipping_type.lower()

  # Logika seleksi horizontal
  if flipping_choice == "horizontal":
    try:
      # Referensi gambar asli
      img_a = image_label.original_image
      # Eksekusi pencerminan horizontal (Mirror)
      result_img = ImageOps.mirror(img_a)
      # Penyimpanan hasil pada atribut
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
      result_text_label.config(text="Hasil Operasi Flip Horizontal")

    except Exception as e:
      # Penanganan eksepsi proses
      messagebox.showerror("Error", f"Gagal melakukan flip horizontal: {e}")
  
  # Logika seleksi vertikal (Default)
  else:
    try:
      # Referensi gambar asli
      img_a = image_label.original_image
      # Eksekusi pencerminan vertikal (Flip)
      result_img = ImageOps.flip(img_a)
      # Penyimpanan hasil pada atribut
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
      result_text_label.config(text="Hasil Operasi Flip Vertikal")

    except Exception as e:
      # Penanganan eksepsi proses
      messagebox.showerror("Error", f"Gagal melakukan flip vertikal: {e}")