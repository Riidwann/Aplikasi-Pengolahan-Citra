# sobel_function.py
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox
from scipy.ndimage import convolve as nd_convolve # Menggunakan convolve dari scipy untuk kecepatan

def sobel(image_label, image_result_label, result_text_label):
    # --- VALIDASI PENTING ---
    if not hasattr(image_label, 'original_image') or not isinstance(image_label.original_image, Image.Image):
        messagebox.showwarning("Error", "Gambar asli belum dimuat atau tidak valid. Silakan muat gambar terlebih dahulu.")
        return
    # -------------------------

    try:
        # 1. Persiapan Gambar
        # Konversi ke grayscale dan array float untuk perhitungan yang akurat
        img = image_label.original_image.convert('L')
        img_array = np.array(img, dtype=float)

        # 2. Kernel Sobel
        sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=float)
        sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=float)

        # 3. Konvolusi (Menggunakan scipy.ndimage.convolve untuk kecepatan tinggi)
        # Mode 'constant' dengan cval=0 mengisi border dengan nol, setara dengan padding
        grad_x = nd_convolve(img_array, sobel_x, mode='constant', cval=0.0)
        grad_y = nd_convolve(img_array, sobel_y, mode='constant', cval=0.0)

        # 4. Menghitung Magnitude Gradien
        # Menggunakan np.hypot(grad_x, grad_y) lebih efisien dan stabil daripada sqrt(x**2 + y**2)
        grad = np.hypot(grad_x, grad_y)

        # 5. Normalisasi dan Konversi
        
        # Normalisasi ke rentang [0, 255] (Min-Max Scaling)
        grad_min = np.min(grad)
        grad_max = np.max(grad)
        
        if grad_max > grad_min:
             grad = 255 * (grad - grad_min) / (grad_max - grad_min)

        # Konversi ke integer 8-bit
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
        result_text_label.config(text="Hasil Operasi Sobel")

    except Exception as e:
        # Menampilkan error yang terjadi jika bukan karena masalah gambar belum dimuat
        messagebox.showerror("Error", f"Gagal melakukan Sobel: {e}")