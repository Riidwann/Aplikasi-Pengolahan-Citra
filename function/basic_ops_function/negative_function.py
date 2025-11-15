from PIL import Image, ImageOps, ImageTk
from tkinter import messagebox

def negative(image_label, image_result_label, result_text_label):
    if not hasattr(image_label, 'original_image'):
        messagebox.showwarning("Error", "Belum ada gambar yang dibuka")
        return
    try:
        img = image_label.original_image
        
        if img.mode == 'RGBA':
            r, g, b, a = img.split()
            r = ImageOps.invert(r)
            g = ImageOps.invert(g)
            b = ImageOps.invert(b)
            negative_img = Image.merge('RGBA', (r, g, b, a))
        
        elif img.mode == 'P':
            rgb_img = img.convert('RGB') 
            negative_img = ImageOps.invert(rgb_img)
            
        else:
            negative_img = ImageOps.invert(img)
        
        image_result_label.image_result = negative_img
        
        img_display = negative_img.copy()
        img_display.thumbnail((760, 560))
        
        tk_image = ImageTk.PhotoImage(img_display)

        image_result_label.config(image=tk_image)
        image_result_label.image = tk_image
        result_text_label.config(text="Hasil Operasi Negative")
    

    except Exception as e:
        messagebox.showerror("Error", f"Gagal melakukan operasi digital: {e}")
