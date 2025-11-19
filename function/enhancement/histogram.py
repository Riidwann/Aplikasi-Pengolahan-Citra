# enhancement/histogram.py
import cv2
import numpy as np

def histogram_equalization(img_cv):
    if img_cv is None:
        return None
    if len(img_cv.shape) == 3:
        # convert to YCrCb and equalize Y channel
        ycrcb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2YCrCb)
        ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])
        out = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
    else:
        out = cv2.equalizeHist(img_cv)
    return out
