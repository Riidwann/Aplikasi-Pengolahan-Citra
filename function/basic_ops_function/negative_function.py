from PIL import Image, ImageOps, ImageTk
from tkinter import messagebox

def negative(image_label):
    if not hasattr(image_label, 'original_image'):
        messagebox.showwarning("Error", "Belum ada gambar yang dibuka")
        return
    
    # 'try' DIMULAI DI SINI
    try:
        img = image_label.original_image
        
        # HAPUS baris 'ImageOps.invert()' yang salah dari sini

        # (Semua logika ini sekarang DI DALAM 'try')
        if img.mode == 'RGBA':
            r, g, b, a = img.split()
            r = ImageOps.invert(r)
            g = ImageOps.invert(g)
            b = ImageOps.invert(b)
            negative_img = Image.merge('RGBA', (r, g, b, a))
        
        elif img.mode == 'P':
            # PERBAIKI typo 'RBA' -> 'RGB'
            rgb_img = img.convert('RGB') 
            negative_img = ImageOps.invert(rgb_img)
            
        else: # Untuk 'RGB', 'L', dll.
            negative_img = ImageOps.invert(img)

        # (Seluruh blok ini juga harus di dalam 'try')
        
        # Simpan gambar hasil operasi
        image_label.original_image = negative_img
        
        # Buat thumbnail untuk ditampilkan
        img_display = negative_img.copy()
        img_display.thumbnail((760, 560)) # (Asumsi ukuran thumbnail)
        
        tk_image = ImageTk.PhotoImage(img_display)

        # --- PENTING: TAMBAHKAN DUA BARIS INI UNTUK UPDATE TAMPILAN ---
        image_label.config(image=tk_image)
        image_label.image = tk_image 
    
    # 'except' sekarang sejajar dengan 'try'
    except Exception as e:
        messagebox.showerror("Error", f"Gagal melakukan operasi digital: {e}")
