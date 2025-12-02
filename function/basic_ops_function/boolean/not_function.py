from PIL import ImageTk, ImageChops
from tkinter import messagebox

def boolean_not(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    # Referensi gambar asli
    img_a = image_label.original_image
    # Konversi mode warna RGB
    img_a_rgb = img_a.convert('RGB')
    # Eksekusi inversi warna (Boolean NOT)
    result_img = ImageChops.invert(img_a_rgb)
    # Penyimpanan hasil pada atribut
    image_result_label.image_result = result_img

    # Duplikasi dan resize untuk preview
    img_display = result_img.copy()
    img_display.thumbnail((760, 560))

    # Konversi ke format Tkinter
    tk_image = ImageTk.PhotoImage(img_display)
    # Rendering gambar ke layar
    image_result_label.config(image=tk_image)
    # Pencegahan penghapusan memori otomatis
    image_result_label.image = tk_image

    # Update teks label status
    result_text_label.config(text="Hasil Operasi NOT")
  
  except Exception as e:
    # Penanganan eksepsi proses
    messagebox.showerror("Error", f"Gagal melakukan NOT: {e}")