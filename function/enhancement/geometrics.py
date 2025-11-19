# function/enhancement/geometrics.py
import cv2
import numpy as np

def geometric_correction_cv(img_cv, angle=0, scale=1.0):
    """Simple wrapper to rotate + scale around center."""
    if img_cv is None:
        return None
    h, w = img_cv.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), float(angle), float(scale))
    out = cv2.warpAffine(img_cv, M, (w, h))
    return out
