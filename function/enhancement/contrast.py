# function/enhancement/contrast.py
import cv2
import numpy as np

def adjust_contrast_cv(img_cv, alpha=1.3):
    """Return contrast adjusted image (cv2 BGR). alpha >1 increases contrast."""
    if img_cv is None:
        return None
    return cv2.convertScaleAbs(img_cv, alpha=float(alpha), beta=0)
