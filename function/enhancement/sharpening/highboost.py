# enhancement/sharpening/highboost.py
import cv2
import numpy as np

def highboost_filter(img_cv, A=1.5):
    """
    High-boost filtering: g = A * f - lowpass(f)
    """
    if img_cv is None:
        return None
    low = cv2.GaussianBlur(img_cv, (5,5), 0)
    mask = cv2.subtract(img_cv, low)
    out = cv2.addWeighted(img_cv, A, mask, 1.0, 0)
    out = cv2.convertScaleAbs(out)
    return out
