# enhancement/geometrics.py
import cv2
import numpy as np

def geometric_correction(img_cv):
    """
    Example geometric correction: simple rotation by 10 degrees + center scaling.
    You can replace this with interactive transform later.
    """
    if img_cv is None:
        return None
    h, w = img_cv.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 10, 1.0)  # rotate 10 degrees
    out = cv2.warpAffine(img_cv, M, (w, h))
    return out
