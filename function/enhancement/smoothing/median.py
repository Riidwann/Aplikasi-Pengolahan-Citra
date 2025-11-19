# enhancement/smoothing/median.py
import cv2
import numpy as np

def median_filter(img_cv, ksize=5):
    if img_cv is None:
        return None
    # ksize must be odd
    if ksize % 2 == 0:
        ksize += 1
    out = cv2.medianBlur(img_cv, ksize)
    return out
