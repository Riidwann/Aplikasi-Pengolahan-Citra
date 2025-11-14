from tkinter import filedialog
from PIL import Image, ImageTk

def open_file(image_label):
  file_types = [
    ("Image Files", "*.png *.jpg *.gif *.bmp"),
    ("All Files", "*.*")
  ]
  file_path = filedialog.askopenfilename(filetypes=file_types)

  if not file_path:
    return
  
  try:
    image = Image.open(file_path)
    image.thumbnail((200, 200))
    tk_image = ImageTk.PhotoImage(image)
    image_label.config(image=tk_image)
    image_label.image = tk_image

  except Exception as e:
    print(f"Gagal membuka file:{e}")