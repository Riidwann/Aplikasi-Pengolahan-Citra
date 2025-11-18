# edge_detection_function/second_differential_gradient/compass_function.py

import numpy as np
from PIL import Image, ImageTk
from tkinter import messagebox

def compass_edge_detection(image_label, image_result_label, result_text_label):
    """Compass edge detection dengan beberapa kernel arah kompas."""

    # Cek apakah sudah ada gambar asli
    if not hasattr(image_label, "original_image"):
        messagebox.showwarning("Error", "Belum ada gambar")
        return

    try:
        # Ambil gambar asli dan ubah ke grayscale
        img = image_label.original_image.convert("L")
        img_array = np.array(img, dtype=np.int32)

        # 8 kernel kompas (bisa dianggap seperti Kirsch sederhana)
        kernels = [
            np.array([[ -1, -1, -1],
                      [  1,  1,  1],
                      [  1,  1,  1]]),  # South

            np.array([[  1,  1,  1],
                      [  1,  1,  1],
                      [ -1, -1, -1]]),  # North

            np.array([[ -1,  1,  1],
                      [ -1,  1,  1],
                      [ -1,  1,  1]]),  # East

            np.array([[  1, -1, -1],
                      [  1, -1, -1],
                      [  1, -1, -1]]),  # West

            np.array([[ -1, -1,  1],
                      [ -1,  1,  1],
                      [  1,  1,  1]]),  # SE

            np.array([[  1,  1,  1],
                      [ -1,  1,  1],
                      [ -1, -1,  1]]),  # NE

            np.array([[  1,  1,  1],
                      [  1,  1, -1],
                      [  1, -1, -1]]),  # NW

            np.array([[  1, -1, -1],
                      [  1,  1, -1],
                      [  1,  1,  1]]),  # SW
        ]

        h, w = img_array.shape
        edge_map = np.zeros_like(img_array, dtype=np.int32)

        # Hitung respon tiap kernel dan ambil maksimum (tepi terkuat)
        for k in kernels:
            resp = np.zeros_like(img_array, dtype=np.int32)
            for i in range(1, h - 1):
                for j in range(1, w - 1):
                    patch = img_array[i-1:i+2, j-1:j+2]
                    resp[i, j] = np.sum(k * patch)
            edge_map = np.maximum(edge_map, resp)

        edge_map = np.clip(edge_map, 0, 255).astype(np.uint8)
        result_img = Image.fromarray(edge_map)

        # Simpan hasil “mentah”
        image_result_label.image_result = result_img

        # Resize untuk display
        img_display = result_img.copy()
        img_display.thumbnail((760, 560))

        tk_image = ImageTk.PhotoImage(img_display)
        image_result_label.config(image=tk_image)
        image_result_label.image = tk_image

        result_text_label.config(text="Hasil Operasi Compass Edge Detection")

    except Exception as e:
        messagebox.showerror("Error", f"Gagal melakukan Compass Edge Detection: {e}")
