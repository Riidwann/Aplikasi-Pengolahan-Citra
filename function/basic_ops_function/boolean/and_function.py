from PIL import Image, ImageTk, ImageChops 
from tkinter import messagebox, filedialog 

def boolean_and(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    # Dialog seleksi gambar kedua
    file_path = filedialog.askopenfilename(title="Pilih gambar kedua")
    if not file_path:
      return
    # Pemuatan objek gambar kedua
    img_b = Image.open(file_path)
  
  except Exception as e:
    # Notifikasi kegagalan input file
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
    
    # Eksekusi operasi Boolean AND (Darker)
    result_img = ImageChops.darker(img_a_rgb, img_b_rgb)
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
    result_text_label.config(text="Hasil Operasi AND")

  except Exception as e:
      # Penanganan eksepsi proses
      messagebox.showerror("Error", f"Gagal melakukan AND: {e}")