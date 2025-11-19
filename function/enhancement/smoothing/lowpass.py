# function/enhancement/smoothing/lowpass.py
import cv2
import numpy as np

def lowpass_filter_cv(img_cv, ksize=5):
    if img_cv is None:
        return None
    k = max(1, int(ksize))
    if k % 2 == 0:
        k += 1
    return cv2.blur(img_cv, (k, k))
