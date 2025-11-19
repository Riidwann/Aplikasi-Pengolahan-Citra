# function/enhancement/brightness.py
import cv2
import numpy as np

def adjust_brightness_cv(img_cv, value=30):
    """Return brightness adjusted image (cv2 BGR). value: -255..255"""
    if img_cv is None:
        return None
    return cv2.convertScaleAbs(img_cv, alpha=1.0, beta=int(value))
