from tkinter import filedialog
from PIL import Image, ImageTk

def open_file(image_label):
  file_types = [
    ("Image Files", "*.png *.jpg"),
    ("All Files", "*.*")
  ]
  file_path = filedialog.askopenfilename(filetypes=file_types)

  if not file_path:
    return
  
  try:
    original_image = Image.open(file_path)
    original_image.thumbnail((200, 200))
    image_label.file_path = file_path
    image_label.original_image = original_image

    image_display = original_image.copy()
    tk_image = ImageTk.PhotoImage(image_display)
    image_label.config(image=tk_image)
    image_label.image = tk_image

  except Exception as e:
    print(f"Gagal membuka file:{e}")