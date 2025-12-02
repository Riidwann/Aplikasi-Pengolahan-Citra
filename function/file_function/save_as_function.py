from tkinter import filedialog, messagebox

def save_as(image_result_label):
    # Validasi ketersediaan objek gambar
    if not hasattr(image_result_label, 'image_result'):
        messagebox.showwarning("Belum ada gambar")
        return

    try:
        # Opsi format file
        file_types = [
            ("PNG", "*.png"),
            ("JPG", "*.jpg"),
            ("PDF", "*.pdf"),
            ("All", "*.*")
        ]
        
        # Pemilihan lokasi simpan
        save_path = filedialog.asksaveasfilename(filetypes=file_types, defaultextension=".png")

        # Validasi pembatalan dialog
        if not save_path:
            return
        
        # Penyimpanan file
        image_result_label.image_result.save(save_path)
        
        # Pembaruan referensi path
        image_result_label.file_path = save_path
        
        messagebox.showinfo("Sukses", f"Gambar berhasil disimpan")
    
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan file: {e}")