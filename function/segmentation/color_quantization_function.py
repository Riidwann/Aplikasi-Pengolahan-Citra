from tkinter import messagebox, simpledialog
from PIL import ImageTk

def color(image_label, image_result_label, result_text_label):
    # Validasi keberadaan gambar
    if not hasattr(image_label, 'original_image'):
        messagebox.showwarning("Error", "Belum ada gambar")
        return
    
    try:
        parent = image_label.winfo_toplevel()
        # Input jumlah segmen warna (K)
        k_colors = simpledialog.askinteger(
            "Color Segmentation",
            "Masukkan jumlah warna/segmen (K):",
            initialvalue=8, minvalue=2, maxvalue=256,
            parent=parent
        )
        if k_colors is None: return

        # Referensi gambar asli
        img_a = image_label.original_image
        
        # Mode RGB
        img_rgb = img_a.convert('RGB')
        
        # Proses Quantization (Pengelompokan warna)
        result_img_p = img_rgb.quantize(colors=k_colors, method=2)
        
        # Konversi kembali ke RGB
        result_img = result_img_p.convert('RGB')
        
        # Penyimpanan dan display hasil
        image_result_label.image_result = result_img
        img_display = result_img.copy()
        img_display.thumbnail((760,560))
        tk_image = ImageTk.PhotoImage(img_display)
        
        image_result_label.config(image=tk_image)
        image_result_label.image = tk_image
        result_text_label.config(text=f"Hasil Segmentasi Warna ({k_colors} Segmen)")

    except Exception as e:
        messagebox.showerror("Error", f"Gagal Segmentasi Warna: {e}")
