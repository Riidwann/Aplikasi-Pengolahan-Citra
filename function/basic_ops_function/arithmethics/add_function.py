from PIL import Image, ImageTk, ImageChops
from tkinter import messagebox, filedialog 

def add(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  try:
    # Dialog seleksi file gambar kedua
    file_path = filedialog.askopenfilename(title="Pilih gambar kedua", filetypes=[("Image Files", "*.jpg *.png"), ("All Files", "*.*")])
    if not file_path:
      return
    # Objek gambar kedua
    img_b = Image.open(file_path)
  
  except Exception as e:
    messagebox.showerror("Error", f"Gagal membuka gambar kedua: {e}")
    return
  
  try:
    # Referensi gambar asli
    img_a = image_label.original_image
    
    # Penyamaan dimensi gambar kedua dengan gambar asli
    target_size = img_a.size
    img_b_resized = img_b.resize(target_size, Image.LANCZOS)

    # Konversi mode warna ke RGB
    img_a_rgb = img_a.convert('RGB')
    img_b_rgb = img_b_resized.convert('RGB')
    
    # Eksekusi aritmatika penjumlahan pixel
    result_img = ImageChops.add(img_a_rgb, img_b_rgb)
    
    # Penyimpanan hasil pada atribut label
    image_result_label.image_result = result_img

    # Duplikasi dan resize untuk preview GUI
    img_display = result_img.copy()
    img_display.thumbnail((760,560))

    # Konversi ke format kompatibel Tkinter
    tk_image = ImageTk.PhotoImage(img_display)
    
    # Rendering gambar ke layar
    image_result_label.config(image=tk_image)
    
    # Pencegahan penghapusan memori otomatis (garbage collection)
    image_result_label.image = tk_image
    
    # Update teks label
    result_text_label.config(text="Hasil Operasi Add")

  except Exception as e:
      # Penanganan eksepsi/error
      messagebox.showerror("Error", f"Gagal melakukan add: {e}")