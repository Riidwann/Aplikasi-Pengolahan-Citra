from tkinter import filedialog
from PIL import Image, ImageTk

def open_file(image_label):
    # Definisi ekstensi
    file_types = [
        ("Image Files", "*.png *.jpg"),
        ("All Files", "*.*")
    ]
    
    # Dialog pemilihan file
    file_path = filedialog.askopenfilename(filetypes=file_types)

    # Validasi path kosong
    if not file_path:
        return
    
    try:
        # Inisialisasi objek gambar
        original_image = Image.open(file_path)
        
        # Ukuran (thumbnail)
        original_image.thumbnail((200, 200))
        
        # Referensi atribut
        image_label.file_path = file_path
        image_label.original_image = original_image

        # Duplikasi untuk tampilan
        image_display = original_image.copy()
        
        # Konversi format Tkinter
        tk_image = ImageTk.PhotoImage(image_display)
        
        # Pembaruan visual widget
        image_label.config(image=tk_image)
        image_label.image = tk_image

    except Exception as e:
        # Penanganan error
        print(f"Gagal membuka file:{e}")