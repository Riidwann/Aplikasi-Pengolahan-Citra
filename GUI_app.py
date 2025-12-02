from tkinter import *
from tkinter import font as tkfont
from menu.basic_ops import *
from menu.file import *
from menu.noise import *
from menu.edge_detection import *
from menu.about import *
from menu.enhancement import enhancement_menu
from menu.segmentation import *
from menu.about import *

COLOR_BG = "#2b2b2b"        # Background utama (Gelap)
COLOR_FRAME = "#3c3f41"     # Background frame (Sedikit lebih terang)
COLOR_TEXT = "#ffffff"      # Warna teks (Putih)
COLOR_IMAGE_BG = "#000000"  # Background tempat gambar (Hitam pekat)

# Setup window
window = Tk()
window.geometry("1000x700")
window.title("Aplikasi Pengolahan Citra Digital")
window.configure(bg=COLOR_BG) # Set warna background window

# --- MENUBAR ---
menubar = Menu(window)
window.config(menu=menubar)

# --- JUDUL HEADER ---
header_frame = Frame(window, bg=COLOR_BG)
header_frame.pack(fill=X, pady=(15, 0))

app_title = Label(
  header_frame, 
  text="IMAGE PROCESSING TOOLS", 
  font=("Segoe UI", 16, "bold"), 
  bg=COLOR_BG, 
  fg=COLOR_TEXT
)
app_title.pack()

# --- FRAME UTAMA ---
main_frame = Frame(window, bg=COLOR_BG)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# --- KOLOM KIRI (GAMBAR ASLI) ---
left_column_frame = LabelFrame(
  main_frame, 
  text="  Original Image  ", 
  font=("Segoe UI", 11, "bold"),
  bg=COLOR_BG, 
  fg=COLOR_TEXT,
  bd=2, 
  relief="groove"
)
left_column_frame.pack(side=LEFT, fill="both", expand=True, padx=10, pady=10)

# Area Gambar Kiri
image_label = Label(
  left_column_frame, 
  text="Belum ada gambar yang dimuat", 
  font=("Segoe UI", 10),
  bg=COLOR_IMAGE_BG, 
  fg="gray"
) 
image_label.pack(fill="both", expand=True, padx=10, pady=10)


# --- KOLOM KANAN (GAMBAR HASIL) ---
right_column_frame = LabelFrame(
  main_frame, 
  text="  Result Image  ", 
  font=("Segoe UI", 11, "bold"),
  bg=COLOR_BG, 
  fg=COLOR_TEXT,
  bd=2, 
  relief="groove"
)
right_column_frame.pack(side=RIGHT, fill="both", expand=True, padx=10, pady=10)

# Area Gambar Kanan
image_result_label = Label(
  right_column_frame, 
  text="Belum ada hasil pemrosesan", 
  font=("Segoe UI", 10),
  bg=COLOR_IMAGE_BG, 
  fg="gray"
)
image_result_label.pack(fill="both", expand=True, padx=10, pady=10)

# --- FOOTER (STATUS BAR) ---
footer_frame = Frame(window, bg=COLOR_FRAME, height=30)
footer_frame.pack(side=BOTTOM, fill=X)

copyright_label = Label(
  footer_frame, 
  text="© 2025 ekstrakDaunBajakah.Dev | Teknik Informatika UNRI", 
  font=("Segoe UI", 8),
  bg=COLOR_FRAME, 
  fg="lightgray"
)
copyright_label.pack(pady=5)

# --- LABEL STATUS HASIL (Disembunyikan/Disatukan) ---
result_text_label = Label(
  right_column_frame, 
  text="", 
  font=("Segoe UI", 10, "italic"),
  bg=COLOR_BG, 
  fg="#4caf50"
) # Warna hijau untuk status
result_text_label.pack(side=BOTTOM, pady=5)


## --- MENU --- ##
file_menu(menubar, image_label, window, image_result_label)
basic_ops_menu(menubar, image_label, image_result_label, result_text_label)
noise_menu(menubar, image_label, image_result_label, result_text_label)
edge_detection_menu(menubar, image_label, image_result_label, result_text_label)
enhancement_menu(menubar, image_label, image_result_label, result_text_label)
segmentation_menu(menubar, image_label, image_result_label, result_text_label)
about(menubar)

window.mainloop()