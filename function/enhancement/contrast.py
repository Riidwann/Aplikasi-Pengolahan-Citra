# enhancement/contrast.py
import cv2
import numpy as np

def adjust_contrast(img_cv, alpha=1.3):
    """
    Simple contrast adjustment using alpha multiplier.
    alpha >1 increases contrast, 0..1 reduces.
    """
    if img_cv is None:
        return None
    out = cv2.convertScaleAbs(img_cv, alpha=alpha, beta=0)
    return out
