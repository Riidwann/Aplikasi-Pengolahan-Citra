# enhancement/smoothing/lowpass.py
import cv2
import numpy as np

def lowpass_filter(img_cv, ksize=5):
    if img_cv is None:
        return None
    out = cv2.blur(img_cv, (ksize, ksize))
    return out
