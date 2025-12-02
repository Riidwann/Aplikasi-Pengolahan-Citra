# menu/enhancement.py
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

# import cv functions
from function.enhancement.brightness import adjust_brightness_cv
from function.enhancement.contrast import adjust_contrast_cv
from function.enhancement.histogram import histogram_equalization_cv
from function.enhancement.geometrics import geometric_correction_cv
from function.enhancement.smoothing.lowpass import lowpass_filter_cv
from function.enhancement.smoothing.median import median_filter_cv
from function.enhancement.smoothing.ilpf import ilpf_filter_cv
from function.enhancement.smoothing.blpf import blpf_filter_cv
from function.enhancement.sharpening.highpass import highpass_filter_cv
from function.enhancement.sharpening.highboost import highboost_filter_cv
from function.enhancement.sharpening.ihpf import ihpf_filter_cv
from function.enhancement.sharpening.bhpf import bhpf_filter_cv


# ----------------------------------------------------------
# Ambil gambar dari label (CV2)
# ----------------------------------------------------------
def _get_img_from_label(image_label):

    img_cv = getattr(image_label, "img_cv", None)
    if img_cv is not None:
        return img_cv

    pil_img = getattr(image_label, "original_image", None)
    if pil_img is not None:
        return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

    img_path = getattr(image_label, "file_path", None)
    if img_path:
        try:
            return cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        except:
            return None

    return None


# ----------------------------------------------------------
# Update label hasil + integrasi dengan SAVE / SAVE AS
# ----------------------------------------------------------
def _update_result_label(image_result_label, result_text_label, out_cv, operation_name):

    if out_cv is None:
        messagebox.showerror("Error", "Proses gagal (hasil None).")
        return

    # CV2 → PIL
    if len(out_cv.shape) == 3:
        out_rgb = cv2.cvtColor(out_cv, cv2.COLOR_BGR2RGB)
    else:
        out_rgb = out_cv

    pil_img = Image.fromarray(out_rgb)

    # Resize preview
    display_pil = pil_img.resize((300, 300), Image.ANTIALIAS) if pil_img.width > 400 else pil_img
    tk_img = ImageTk.PhotoImage(display_pil)

    # tampilkan preview
    image_result_label.config(image=tk_img, text="")
    image_result_label.image = tk_img

    # ============================================
    # BAGIAN PALING PENTING UNTUK SAVE / SAVE AS
    image_result_label.image_result = pil_img  # hasil PIL untuk save()
    image_result_label.file_path = None        # supaya SAVE memaksa SAVE AS
    # ============================================

    # update teks
    if result_text_label:
        result_text_label.config(text=f"Hasil Operasi {operation_name}")


# ----------------------------------------------------------
# Jalankan operasi enhancement (wrapper)
# ----------------------------------------------------------
def _run_and_update(image_label, image_result_label, result_text_label, func, operation_name):

    img_cv = _get_img_from_label(image_label)
    if img_cv is None:
        messagebox.showerror("Error", "Tidak ada gambar yang dipilih.")
        return

    try:
        out = func(img_cv)
    except Exception as e:
        messagebox.showerror("Error", f"Kesalahan saat proses:\n{e}")
        return

    _update_result_label(image_result_label, result_text_label, out, operation_name)


# ----------------------------------------------------------
# Enhancement Menu
# ----------------------------------------------------------
def enhancement_menu(menubar, image_label, image_result_label, result_text_label):

    enhancementMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Enhancement", menu=enhancementMenu)

    # Brightness
    enhancementMenu.add_command(label="Brightness", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: adjust_brightness_cv(img, value=30),
                        "Brightness"))

    # Contrast
    enhancementMenu.add_command(label="Contrast", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: adjust_contrast_cv(img, alpha=1.4),
                        "Contrast"))

    # Histogram Equalization
    enhancementMenu.add_command(label="Histogram Equalization", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: histogram_equalization_cv(img),
                        "Histogram Equalization"))

    # ======================================================
    # Smoothing Menu
    # ======================================================
    smoothing_menu = Menu(enhancementMenu, tearoff=0)

    # Spatial
    spatial = Menu(smoothing_menu, tearoff=0)
    spatial.add_command(label="Lowpass Filtering", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: lowpass_filter_cv(img, ksize=5),
                        "Lowpass Filtering"))

    spatial.add_command(label="Median Filtering", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: median_filter_cv(img, ksize=5),
                        "Median Filtering"))

    # Frequency
    freq = Menu(smoothing_menu, tearoff=0)
    freq.add_command(label="ILPF", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: ilpf_filter_cv(img, D0=30),
                        "ILPF"))

    freq.add_command(label="BLPF", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: blpf_filter_cv(img, D0=30, n=2),
                        "BLPF"))

    smoothing_menu.add_cascade(label="Spatial Domain", menu=spatial)
    smoothing_menu.add_cascade(label="Frequency Domain", menu=freq)
    enhancementMenu.add_cascade(label="Smoothing", menu=smoothing_menu)

    # ======================================================
    # Sharpening Menu
    # ======================================================
    sharpening_menu = Menu(enhancementMenu, tearoff=0)

    # Spatial
    s_spatial = Menu(sharpening_menu, tearoff=0)
    s_spatial.add_command(label="Highpass Filtering", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: highpass_filter_cv(img),
                        "Highpass Filtering"))

    s_spatial.add_command(label="Highboost Filtering", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: highboost_filter_cv(img, A=1.6),
                        "Highboost Filtering"))

    # Frequency
    s_freq = Menu(sharpening_menu, tearoff=0)
    s_freq.add_command(label="IHPF", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: ihpf_filter_cv(img, D0=30),
                        "IHPF"))

    s_freq.add_command(label="BHPF", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: bhpf_filter_cv(img, D0=30, n=2),
                        "BHPF"))

    sharpening_menu.add_cascade(label="Spatial Domain", menu=s_spatial)
    sharpening_menu.add_cascade(label="Frequency Domain", menu=s_freq)
    enhancementMenu.add_cascade(label="Sharpening", menu=sharpening_menu)

    # ======================================================
    # Geometric Correction
    # ======================================================
    enhancementMenu.add_command(label="Geometrics Correction", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: geometric_correction_cv(img, angle=10, scale=1.0),
                        "Geometric Correction"))
