# function/enhancement/sharpening/highboost.py
import cv2
import numpy as np

def highboost_filter_cv(img_cv, A=1.5):
    if img_cv is None:
        return None
    low = cv2.GaussianBlur(img_cv, (5,5), 0)
    mask = cv2.subtract(img_cv, low)
    out = cv2.addWeighted(img_cv, float(A), mask, 1.0, 0)
    return cv2.convertScaleAbs(out)
