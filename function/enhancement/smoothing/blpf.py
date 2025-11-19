# function/enhancement/smoothing/blpf.py
import cv2
import numpy as np

def blpf_filter_cv(img_cv, D0=30, n=2):
    """Butterworth lowpass (grayscale -> return BGR)"""
    if img_cv is None:
        return None
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY) if len(img_cv.shape)==3 else img_cv
    rows, cols = gray.shape
    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    fshift = np.fft.fftshift(dft)
    u = np.arange(rows)
    v = np.arange(cols)
    V, U = np.meshgrid(v, u)
    crow, ccol = rows//2, cols//2
    D = np.sqrt((U-crow)**2 + (V-ccol)**2)
    H = 1.0 / (1.0 + (D/(D0+1e-8))**(2*n))
    H = np.stack([H, H], axis=-1).astype(np.float32)
    fshift = fshift * H
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    out = cv2.cvtColor(np.uint8(img_back), cv2.COLOR_GRAY2BGR)
    return out
