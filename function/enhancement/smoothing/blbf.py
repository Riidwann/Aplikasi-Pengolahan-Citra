# enhancement/smoothing/blpf.py
import cv2
import numpy as np

def blpf_filter(img_cv, D0=30, n=2):
    """
    Butterworth Lowpass Filter (frequency domain) applied to grayscale.
    """
    if img_cv is None:
        return None
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    rows, cols = gray.shape
    # DFT
    dft = cv2.dft(np.float32(gray), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    crow, ccol = rows//2, cols//2
    # create butterworth mask
    u = np.arange(0, rows)
    v = np.arange(0, cols)
    V, U = np.meshgrid(v, u)
    D = np.sqrt((U - crow)**2 + (V - ccol)**2)
    H = 1 / (1 + (D / (D0+1e-8))**(2*n))
    H = H.astype(np.float32)
    H = np.stack([H, H], axis=-1)
    fshift = dft_shift * H
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    out = cv2.cvtColor(np.uint8(img_back), cv2.COLOR_GRAY2BGR)
    return out
