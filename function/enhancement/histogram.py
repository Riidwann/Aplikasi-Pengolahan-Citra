# function/enhancement/histogram.py
import cv2
import numpy as np

def histogram_equalization_cv(img_cv):
    """Return histogram equalized image (works on color via YCrCb)."""
    if img_cv is None:
        return None
    if len(img_cv.shape) == 3 and img_cv.shape[2] == 3:
        ycrcb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        out = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    else:
        out = cv2.equalizeHist(img_cv)
    return out
