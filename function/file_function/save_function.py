from tkinter import messagebox
from function.file_function.save_as_function import *

def save(image_result):
    # Validasi ketersediaan atribut gambar
    if not hasattr(image_result, 'image_result'):
        return
    
    # Pengecekan riwayat lokasi file
    if hasattr(image_result, 'file_path') and image_result.file_path:
        try:
            # Penyimpanan ulang ke path asal (overwrite)
            image_result.image_result.save(image_result.file_path)
            
            # Konfirmasi status sukses
            messagebox.showinfo("Sukses", f"Gambar berhasil disimpan")
            
        except Exception as e:
            # Manajemen error sistem
            messagebox.showerror("Error", f"Gagal menyimpan file: {e}")
    else:
        # Pengalihan ke fungsi "Save As"
        save_as(image_result)