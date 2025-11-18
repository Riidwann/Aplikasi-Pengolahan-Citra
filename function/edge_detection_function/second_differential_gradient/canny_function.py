# canny_function.py
import numpy as np
from PIL import Image, ImageTk
from scipy.ndimage import sobel, gaussian_filter
from tkinter import messagebox
import math 

def canny(image_label, image_result_label, result_text_label, low_threshold=50, high_threshold=150, sigma=1.0):
    """Applies Canny Edge Detection."""
    
    # --- VALIDASI INPUT ---
    if not hasattr(image_label, 'original_image') or not isinstance(image_label.original_image, Image.Image):
        messagebox.showwarning("Error", "Gambar asli belum dimuat atau tidak valid. Silakan muat gambar terlebih dahulu.")
        return
    # ----------------------

    try:
        # 1. Ambil Gambar Asli & Smoothing (Biasanya langkah pertama Canny adalah Gaussian Blur)
        img_pil = image_label.original_image.convert('L')
        img_array = np.array(img_pil, dtype=float)

        # Apply Gaussian filter (Smoothing)
        smoothed_img = gaussian_filter(img_array, sigma=sigma)

        # 2. Apply Sobel operator to detect gradients in both directions
        grad_x = sobel(smoothed_img, axis=0)
        grad_y = sobel(smoothed_img, axis=1)
        
        # 3. Compute gradient magnitude and direction
        grad_magnitude = np.hypot(grad_x, grad_y)
        grad_direction = np.arctan2(grad_y, grad_x)

        # 4. Non-maximum suppression (NMS)
        non_max_suppressed = np.zeros_like(grad_magnitude, dtype=float)
        angle = grad_direction * (180.0 / np.pi) 
        angle[angle < 0] += 180 

        for i in range(1, grad_magnitude.shape[0] - 1):
            for j in range(1, grad_magnitude.shape[1] - 1):
                # Penentuan arah kuadran
                direction = angle[i, j]
                
                # 0° (Horizontal)
                if (0 <= direction < 22.5) or (157.5 <= direction <= 180):
                    neighbor1 = grad_magnitude[i, j+1]
                    neighbor2 = grad_magnitude[i, j-1]
                # 45° (Diagonal Barat Laut - Tenggara)
                elif (22.5 <= direction < 67.5):
                    neighbor1 = grad_magnitude[i+1, j-1]
                    neighbor2 = grad_magnitude[i-1, j+1]
                # 90° (Vertikal)
                elif (67.5 <= direction < 112.5):
                    neighbor1 = grad_magnitude[i+1, j]
                    neighbor2 = grad_magnitude[i-1, j]
                # 135° (Diagonal Timur Laut - Barat Daya)
                else:
                    neighbor1 = grad_magnitude[i-1, j-1]
                    neighbor2 = grad_magnitude[i+1, j+1]

                if grad_magnitude[i, j] >= neighbor1 and grad_magnitude[i, j] >= neighbor2:
                    non_max_suppressed[i, j] = grad_magnitude[i, j]
                else:
                    non_max_suppressed[i, j] = 0

        # 5. Double thresholding
        # Normalisasi untuk ambang batas yang lebih bermakna
        non_max_suppressed = non_max_suppressed / non_max_suppressed.max() * 255 if non_max_suppressed.max() > 0 else non_max_suppressed
        
        strong_edges = non_max_suppressed > high_threshold
        weak_edges = (non_max_suppressed >= low_threshold) & (non_max_suppressed <= high_threshold)
        
        # 6. Edge Tracking by Hysteresis (Simplified)
        final_edges = np.copy(strong_edges)
        
        # Lakukan iterasi sampai tidak ada lagi tepi lemah yang terhubung ke tepi kuat
        # (Implementasi sederhana, versi robust menggunakan rekursi atau antrian)
        for i in range(1, final_edges.shape[0] - 1):
            for j in range(1, final_edges.shape[1] - 1):
                if weak_edges[i, j]:
                    # Cek 8 tetangga
                    if np.any(strong_edges[i-1:i+2, j-1:j+2]):
                        final_edges[i, j] = True
                    else:
                        final_edges[i, j] = False

        final_edges = final_edges.astype(np.uint8) * 255 

        # 7. Menampilkan Hasil
        result_img = Image.fromarray(final_edges)
        image_result_label.image_result = result_img

        # Menampilkan gambar hasil dengan ukuran thumbnail
        img_display = result_img.copy()
        img_display.thumbnail((760, 560))

        tk_image = ImageTk.PhotoImage(img_display)
        image_result_label.config(image=tk_image)
        image_result_label.image = tk_image
        result_text_label.config(text=f"Hasil Operasi Canny (Tinggi={high_threshold}, Rendah={low_threshold})")

    except Exception as e:
        messagebox.showerror("Error", f"Gagal melakukan Canny: {e}")