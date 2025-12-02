from tkinter import messagebox
from PIL import ImageTk
import numpy as np

def otsu(image_label, image_result_label, result_text_label):
    # Validasi keberadaan gambar
    if not hasattr(image_label, 'original_image'):
        messagebox.showwarning("Error", "Belum ada gambar")
        return
    
    try:
        # Referensi gambar asli
        img_a = image_label.original_image
        # Konversi ke grayscale
        img_gray = img_a.convert('L')
        img_array = np.array(img_gray)
        
        # Perhitungan Histogram
        pixel_counts, bins = np.histogram(img_array, bins=256, range=(0, 256))
        
        # Inisialisasi variabel Otsu
        total_pixels = img_array.size
        current_max, threshold = 0, 0
        sum_total, sum_b, weight_b = 0, 0, 0
        
        # Hitung total intensitas
        for i in range(256):
            sum_total += i * pixel_counts[i]
            
        # Iterasi mencari threshold optimal
        for i in range(256):
            weight_b += pixel_counts[i]
            if weight_b == 0: continue
            
            weight_f = total_pixels - weight_b
            if weight_f == 0: break
            
            sum_b += i * pixel_counts[i]
            mean_b = sum_b / weight_b
            mean_f = (sum_total - sum_b) / weight_f
            
            # Rumus "Between Class Variance"
            var_between = weight_b * weight_f * (mean_b - mean_f) ** 2
            
            if var_between > current_max:
                current_max = var_between
                threshold = i
        
        # Penerapan nilai threshold terpilih
        result_img = img_gray.point(lambda p: 255 if p > threshold else 0)
        
        # Konversi ke RGB untuk display
        result_img = result_img.convert('RGB')
        
        # Penyimpanan dan display hasil
        image_result_label.image_result = result_img
        img_display = result_img.copy()
        img_display.thumbnail((760,560))
        tk_image = ImageTk.PhotoImage(img_display)
        
        image_result_label.config(image=tk_image)
        image_result_label.image = tk_image
        result_text_label.config(text=f"Hasil Otsu Threshold (Nilai: {threshold})")

    except Exception as e:
        messagebox.showerror("Error", f"Gagal Otsu: {e}")