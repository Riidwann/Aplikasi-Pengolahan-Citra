from tkinter import messagebox, simpledialog
from PIL import ImageTk, ImageOps

def pseudo(image_label, image_result_label, result_text_label):
  # Validasi keberadaan gambar sumber
  if not hasattr(image_label, 'original_image'):
    messagebox.showwarning("Error", "Belum ada gambar")
    return
  
  try:
    # Pengambilan referensi jendela induk
    parent_window = image_label.winfo_toplevel()

    # Dialog input warna area gelap
    color_dark = simpledialog.askstring(
        "Pseudocolor (1/2)", 
        "Masukkan warna untuk area GELAP:\n(Contoh: 'blue', 'black', atau '#FF0000')",
        initialvalue="blue",
        parent=parent_window
    )
    # Penanganan pembatalan input
    if color_dark is None: return

    # Dialog input warna area terang
    color_bright = simpledialog.askstring(
        "Pseudocolor (2/2)", 
        "Masukkan warna untuk area TERANG:\n(Contoh: 'red', 'yellow', atau '#00FF00')",
        initialvalue="yellow",
        parent=parent_window
    )
    # Penanganan pembatalan input
    if color_bright is None: return

  except Exception as e:
    # Notifikasi error input
    messagebox.showerror("Error", f"Input tidak valid: {e}")
    return
  
  try:
    # Referensi gambar asli
    img_a = image_label.original_image
    # Konversi mode grayscale (L)
    img_gray = img_a.convert('L')
    # Penerapan pewarnaan palsu (pseudocolor)
    result_img = ImageOps.colorize(
        img_gray, 
        black=color_dark, 
        white=color_bright
    )

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
    result_text_label.config(text=f"Hasil Pseudo ({color_dark} -> {color_bright})")

  except Exception as e:
      # Penanganan eksepsi proses (termasuk validitas nama warna)
      messagebox.showerror("Error", f"Gagal Pseudo-Coloring: {e}\n(Pastikan nama warna valid)")