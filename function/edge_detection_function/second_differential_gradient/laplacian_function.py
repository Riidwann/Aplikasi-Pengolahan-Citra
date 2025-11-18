# laplacian_function.py
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox

def laplacian(image_label, image_result_label, result_text_label):
    """Menerapkan deteksi tepi Laplacian."""
    
    # --- VALIDASI INPUT (Pola yang sama dengan fungsi sebelumnya) ---
    if not hasattr(image_label, 'original_image') or not isinstance(image_label.original_image, Image.Image):
        messagebox.showwarning("Error", "Gambar asli belum dimuat atau tidak valid. Silakan muat gambar terlebih dahulu.")
        return
    # -----------------------------------------------------------------

    try:
        # 1. Mengambil gambar dari image_label dan konversi ke array float
        img = image_label.original_image.convert('L')
        img_array = np.array(img, dtype=float) 

        # Laplacian kernel
        laplacian_kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=float)

        grad = np.zeros_like(img_array)
        h, w = img_array.shape

        # 2. Apply convolution dengan kernel Laplacian
        for i in range(1, h - 1):
            for j in range(1, w - 1):
                patch = img_array[i-1:i+2, j-1:j+2]
                grad[i, j] = np.sum(laplacian_kernel * patch)

        # 3. Normalisasi Hasil
        # Laplacian menghasilkan nilai positif dan negatif.
        # Kita menggunakan nilai absolut (magnitudo) untuk visualisasi tepi.
        grad = np.abs(grad) 
        
        # Normalisasi Min-Max
        grad_min = np.min(grad)
        grad_max = np.max(grad)
        
        if grad_max > grad_min:
             grad = 255 * (grad - grad_min) / (grad_max - grad_min)

        grad = np.uint8(np.clip(grad, 0, 255)) 

        # 4. Menampilkan Hasil ke Tkinter
        result_img = Image.fromarray(grad)
        image_result_label.image_result = result_img

        # Menampilkan gambar hasil dengan ukuran thumbnail
        img_display = result_img.copy()
        img_display.thumbnail((760, 560))

        tk_image = ImageTk.PhotoImage(img_display)
        image_result_label.config(image=tk_image)
        image_result_label.image = tk_image
        result_text_label.config(text="Hasil Operasi Laplacian")
        
    except Exception as e:
        messagebox.showerror("Error", f"Gagal melakukan Laplacian: {e}")