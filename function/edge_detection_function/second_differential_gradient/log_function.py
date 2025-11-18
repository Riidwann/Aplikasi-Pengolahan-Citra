# log_function.py
import numpy as np
from PIL import Image, ImageTk
from scipy.ndimage import gaussian_filter
from tkinter import messagebox

def log_filter(image_label, image_result_label, result_text_label, sigma=1.0):
    """Menerapkan deteksi tepi Laplacian of Gaussian (LoG)."""
    
    # --- VALIDASI INPUT ---
    if not hasattr(image_label, 'original_image') or not isinstance(image_label.original_image, Image.Image):
        messagebox.showwarning("Error", "Gambar asli belum dimuat atau tidak valid.")
        return
    # ----------------------

    try:
        # 1. Persiapan Gambar
        img_array = np.array(image_label.original_image.convert('L'), dtype=float)

        # 2. Apply Gaussian filter (smoothing)
        smoothed_img = gaussian_filter(img_array, sigma=sigma)

        # 3. Laplacian Kernel
        # Menggunakan float untuk perhitungan yang akurat
        laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=float)

        grad = np.zeros_like(smoothed_img)
        h, w = smoothed_img.shape

        # 4. Apply convolution (Laplacian)
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                patch = smoothed_img[i-1:i+2, j-1:j+2]
                grad[i, j] = np.sum(laplacian_kernel * patch)

        # 5. Normalisasi dan Konversi
        # Menggunakan nilai absolut untuk visualisasi tepi
        grad = np.abs(grad) 
        
        # Normalisasi Min-Max
        grad_min = np.min(grad)
        grad_max = np.max(grad)
        
        if grad_max > grad_min:
             grad = 255 * (grad - grad_min) / (grad_max - grad_min)

        grad = np.uint8(np.clip(grad, 0, 255)) 

        # 6. Menampilkan Hasil
        result_img = Image.fromarray(grad)
        image_result_label.image_result = result_img

        # Menampilkan gambar hasil dengan ukuran thumbnail
        img_display = result_img.copy()
        img_display.thumbnail((760, 560))

        tk_image = ImageTk.PhotoImage(img_display)
        image_result_label.config(image=tk_image)
        image_result_label.image = tk_image
        result_text_label.config(text=f"Hasil Operasi LoG (Sigma={sigma})")
        
    except Exception as e:
        messagebox.showerror("Error", f"Gagal melakukan LoG: {e}")