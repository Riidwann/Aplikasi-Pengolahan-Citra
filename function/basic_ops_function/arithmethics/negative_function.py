from PIL import Image, ImageOps, ImageTk
from tkinter import messagebox

def negative(image_label, image_result_label, result_text_label):
    # Validasi keberadaan gambar sumber
    if not hasattr(image_label, 'original_image'):
        messagebox.showwarning("Error", "Belum ada gambar yang dibuka")
        return
    try:
        # Referensi objek gambar asli
        img = image_label.original_image
        
        # Penanganan khusus mode RGBA (transparansi)
        if img.mode == 'RGBA':
            # Pemisahan channel warna dan alpha
            r, g, b, a = img.split()
            # Inversi channel warna saja
            r = ImageOps.invert(r)
            g = ImageOps.invert(g)
            b = ImageOps.invert(b)
            # Penggabungan ulang channel dengan alpha asli
            negative_img = Image.merge('RGBA', (r, g, b, a))
        
        # Penanganan mode Palette (0 -255)
        elif img.mode == 'P':
            # Konversi ke format RGB
            rgb_img = img.convert('RGB') 
            # Inversi warna standar
            negative_img = ImageOps.invert(rgb_img)
            
        else:
            # Inversi langsung untuk mode umum (RGB/L)
            negative_img = ImageOps.invert(img)
        
        # Penyimpanan objek hasil pada atribut
        image_result_label.image_result = negative_img
        
        # Duplikasi dan resize untuk preview GUI
        img_display = negative_img.copy()
        img_display.thumbnail((760, 560))
        
        # Konversi ke format kompatibel Tkinter
        tk_image = ImageTk.PhotoImage(img_display)

        # Rendering gambar ke layar
        image_result_label.config(image=tk_image)
        # Pencegahan penghapusan memori otomatis
        image_result_label.image = tk_image
        # Update teks label status
        result_text_label.config(text="Hasil Operasi Negative")
    
    except Exception as e:
        # Penanganan eksepsi proses
        messagebox.showerror("Error", f"Gagal melakukan operasi digital: {e}")