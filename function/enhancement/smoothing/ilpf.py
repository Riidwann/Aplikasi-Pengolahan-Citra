# function/enhancement/smoothing/ilpf.py
import cv2
import numpy as np

def ilpf_filter_cv(img_cv, D0=30):
    """Ideal lowpass filter on grayscale (returns BGR)"""
    if img_cv is None:
        return None
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY) if len(img_cv.shape)==3 else img_cv
    rows, cols = gray.shape
    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    fshift = np.fft.fftshift(dft)
    crow, ccol = rows//2, cols//2
    mask = np.zeros((rows, cols, 2), np.uint8)
    cv2.circle(mask, (ccol, crow), int(D0), (1,1), -1)
    fshift = fshift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    out = cv2.cvtColor(np.uint8(img_back), cv2.COLOR_GRAY2BGR)
    return out
