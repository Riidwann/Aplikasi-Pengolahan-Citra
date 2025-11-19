# enhancement/brightness.py
import cv2
import numpy as np

def adjust_brightness(img_cv, value=30):
    """
    Simple brightness adjustment: add value to pixels (clamped).
    img_cv: BGR OpenCV image (numpy)
    value: int (-255..255)
    """
    if img_cv is None:
        return None
    # convert to int16 to avoid overflow then clip
    out = cv2.convertScaleAbs(img_cv, alpha=1.0, beta=value)
    return out
