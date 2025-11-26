from tkinter import messagebox, simpledialog
from PIL import ImageTk, ImageFilter

def morphology(image_label, image_result_label, result_text_label):
    if not hasattr(image_label, 'original_image'):
        messagebox.showwarning("Error", "Belum ada gambar")
        return
    
    try:
        parent = image_label.winfo_toplevel()
        # Pilihan jenis operasi morfologi
        morph_type = simpledialog.askstring(
            "Morfologi", 
            "Pilih operasi: 'Erosi' (mengecilkan) atau 'Dilasi' (menebalkan)",
            parent=parent
        )
        if morph_type is None: return
        
        choice = morph_type.lower()
        
        # Input ukuran kernel (kekuatan filter)
        size = simpledialog.askinteger(
            "Ukuran Kernel",
            "Masukkan ukuran filter (ganjil, misal 3, 5, 7):",
            initialvalue=3, minvalue=3, maxvalue=21,
            parent=parent
        )
        if size is None: return

        # Referensi gambar
        img_a = image_label.original_image
        # Konversi Grayscale/Binary
        img_gray = img_a.convert('L') 
        
        text_hasil = ""
        
        if "erosi" in choice or "erosion" in choice:
            # MinFilter = Erosi (mengambil piksel tergelap/terkecil)
            result_img = img_gray.filter(ImageFilter.MinFilter(size))
            text_hasil = f"Hasil Erosi (Kernel {size})"
            
        elif "dilasi" in choice or "dilation" in choice:
            # MaxFilter = Dilasi (mengambil piksel terterang/terbesar)
            result_img = img_gray.filter(ImageFilter.MaxFilter(size))
            text_hasil = f"Hasil Dilasi (Kernel {size})"
            
        else:
            messagebox.showwarning("Error", "Pilihan tidak dikenal. Ketik 'Erosi' atau 'Dilasi'")
            return

        # Konversi balik ke RGB
        result_img = result_img.convert('RGB')
        
        # Penyimpanan dan display
        image_result_label.image_result = result_img
        img_display = result_img.copy()
        img_display.thumbnail((760,560))
        tk_image = ImageTk.PhotoImage(img_display)
        
        image_result_label.config(image=tk_image)
        image_result_label.image = tk_image
        result_text_label.config(text=text_hasil)

    except Exception as e:
        messagebox.showerror("Error", f"Gagal Morfologi: {e}")
