# function/enhancement/sharpening/ihpf.py
import cv2
import numpy as np

def ihpf_filter_cv(img_cv, D0=30):
    if img_cv is None:
        return None
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    rows, cols = gray.shape
    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    fshift = np.fft.fftshift(dft)
    mask = np.ones((rows, cols, 2), np.uint8)
    cv2.circle(mask, (cols//2, rows//2), int(D0), (0,0), -1)  # block low freq
    fshift = fshift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    out = cv2.cvtColor(np.uint8(img_back), cv2.COLOR_GRAY2BGR)
    return out
