# menu/enhancement.py
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

# import cv functions from function/enhancement
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

def _get_img_from_label(image_label):
    """
    Ambil gambar dari image_label dengan cara aman:
    1. Jika ada img_cv → pakai (untuk OpenCV)
    2. Jika tidak → convert original_image (PIL) ke OpenCV
    3. Jika masih tidak ada → baca dari file_path
    """

    # 1. Jika img_cv sudah ada (case: setelah enhancement sebelumnya)
    img_cv = getattr(image_label, "img_cv", None)
    if img_cv is not None:
        return img_cv

    # 2. Jika PIL image ada → convert ke OpenCV
    pil_img = getattr(image_label, "original_image", None)
    if pil_img is not None:
        img_cv = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
        return img_cv

    # 3. Jika file path ada → baca ulang
    img_path = getattr(image_label, "file_path", None)
    if img_path:
        try:
            img_cv = cv2.imdecode(np.fromfile(img_path, dtype=np.uint8), cv2.IMREAD_COLOR)
            return img_cv
        except:
            pass

    return None


def _update_result_label(image_result_label, result_text_label, out_cv):
    """Update the result label widget and text label. Expects cv2 BGR image."""
    if out_cv is None:
        messagebox.showerror("Error", "Proses gagal atau hasil None.")
        return
    # Convert BGR -> RGB -> PIL -> ImageTk
    out_rgb = cv2.cvtColor(out_cv, cv2.COLOR_BGR2RGB) if len(out_cv.shape)==3 else out_cv
    pil = Image.fromarray(out_rgb)
    # resize to reasonable preview if needed
    pil_resized = pil.resize((300,300), Image.ANTIALIAS) if pil.size[0] > 400 else pil
    tkimg = ImageTk.PhotoImage(pil_resized)
    image_result_label.configure(image=tkimg, text="")
    image_result_label.image = tkimg
    # store cv to result label too (for further processing)
    image_result_label.img_cv = out_cv
    if result_text_label is not None:
        result_text_label.config(text="Hasil: selesai")

def enhancement_menu(menubar, image_label, image_result_label, result_text_label):
    enhancementMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Enhancement", menu=enhancementMenu)

    # simple wrappers: fetch cv image from image_label, call underlying cv function,
    # then update result widget
    enhancementMenu.add_command(label="Brightness", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: adjust_brightness_cv(img, value=30)))

    enhancementMenu.add_command(label="Contrast", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: adjust_contrast_cv(img, alpha=1.4)))

    enhancementMenu.add_command(label="Histogram Equalization", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: histogram_equalization_cv(img)))

    # Smoothing submenu
    smoothing_menu = Menu(enhancementMenu, tearoff=0)
    spatial = Menu(smoothing_menu, tearoff=0)
    spatial.add_command(label="Lowpass Filtering", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: lowpass_filter_cv(img, ksize=5)))
    spatial.add_command(label="Median Filtering", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: median_filter_cv(img, ksize=5)))
    freq = Menu(smoothing_menu, tearoff=0)
    freq.add_command(label="ILPF", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: ilpf_filter_cv(img, D0=30)))
    freq.add_command(label="BLPF", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: blpf_filter_cv(img, D0=30, n=2)))
    smoothing_menu.add_cascade(label="Spatial Domain", menu=spatial)
    smoothing_menu.add_cascade(label="Frequency Domain", menu=freq)
    enhancementMenu.add_cascade(label="Smoothing", menu=smoothing_menu)

    # Sharpening submenu
    sharpening_menu = Menu(enhancementMenu, tearoff=0)
    s_spatial = Menu(sharpening_menu, tearoff=0)
    s_spatial.add_command(label="Highpass Filtering", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: highpass_filter_cv(img)))
    s_spatial.add_command(label="Highboost Filtering", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: highboost_filter_cv(img, A=1.6)))
    s_freq = Menu(sharpening_menu, tearoff=0)
    s_freq.add_command(label="IHPF", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: ihpf_filter_cv(img, D0=30)))
    s_freq.add_command(label="BHPF", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: bhpf_filter_cv(img, D0=30, n=2)))
    sharpening_menu.add_cascade(label="Spatial Domain", menu=s_spatial)
    sharpening_menu.add_cascade(label="Frequency Domain", menu=s_freq)
    enhancementMenu.add_cascade(label="Sharpening", menu=sharpening_menu)

    enhancementMenu.add_command(label="Geometrics Correction", command=lambda:
        _run_and_update(image_label, image_result_label, result_text_label,
                        lambda img: geometric_correction_cv(img, angle=10, scale=1.0)))

def _run_and_update(image_label, image_result_label, result_text_label, func):
    """Common routine to get image, run func(cv_img)->cv_img, update widget"""
    img_cv = _get_img_from_label(image_label)
    if img_cv is None:
        messagebox.showerror("Error", "Tidak ada gambar yang dipilih.")
        return
    try:
        out = func(img_cv)
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat proses:\n{e}")
        return
    _update_result_label(image_result_label, result_text_label, out)
