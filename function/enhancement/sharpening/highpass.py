# enhancement/sharpening/highpass.py
import cv2
import numpy as np

def highpass_filter(img_cv):
    if img_cv is None:
        return None
    # simple kernel highpass (Laplacian-like)
    kernel = np.array([[-1,-1,-1],
                       [-1, 8,-1],
                       [-1,-1,-1]])
    out = cv2.filter2D(img_cv, -1, kernel)
    # normalize and convert
    out = cv2.convertScaleAbs(out)
    return out
