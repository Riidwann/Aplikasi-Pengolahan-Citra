# robert_function.py (Kode Perbaikan)
import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox

def robert(image_label, image_result_label, result_text_label):
    # Validasi input (Sangat disarankan seperti pada fungsi Sobel)
    if not hasattr(image_label, 'original_image'):
        messagebox.showwarning("Error", "Gambar asli belum dimuat.")
        return

    try:
        img = image_label.original_image.convert('L')
        # Gunakan dtype=float untuk perhitungan
        img_array = np.array(img, dtype=float) 

        # Kernel Robert
        robert_x = np.array([[1, 0], [0, -1]], dtype=float) 
        robert_y = np.array([[0, 1], [-1, 0]], dtype=float)

        grad_x = np.zeros_like(img_array)
        grad_y = np.zeros_like(img_array)

        h, w = img_array.shape

        # Melakukan konvolusi
        for i in range(h - 1):
            for j in range(w - 1):
                patch = img_array[i:i+2, j:j+2]
                grad_x[i, j] = np.sum(robert_x * patch)
                grad_y[i, j] = np.sum(robert_y * patch)

        # Menghitung magnitude gradien
        grad = np.sqrt(grad_x**2 + grad_y**2)
        
        # --- NORMALISASI MIN-MAX ---
        grad_min = np.min(grad)
        grad_max = np.max(grad)
        
        if grad_max > grad_min:
             # Peregangan nilai gradien ke rentang 0-255
             grad = 255 * (grad - grad_min) / (grad_max - grad_min)
        
        # Konversi akhir ke uint8
        grad = np.uint8(np.clip(grad, 0, 255)) 
        # --- END NORMALISASI ---

        # ... (Kode menampilkan hasil, sama seperti sebelumnya)
        result_img = Image.fromarray(grad)
        image_result_label.image_result = result_img

        img_display = result_img.copy()
        img_display.thumbnail((760, 560))

        tk_image = ImageTk.PhotoImage(img_display)
        image_result_label.config(image=tk_image)
        image_result_label.image = tk_image
        result_text_label.config(text="Hasil Operasi Robert")

    except Exception as e:
        messagebox.showerror("Error", f"Gagal melakukan Robert: {e}")