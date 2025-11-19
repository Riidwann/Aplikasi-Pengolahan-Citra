# function/enhancement/smoothing/median.py
import cv2
import numpy as np

def median_filter_cv(img_cv, ksize=5):
    if img_cv is None:
        return None
    k = int(ksize)
    if k % 2 == 0:
        k += 1
    return cv2.medianBlur(img_cv, k)
