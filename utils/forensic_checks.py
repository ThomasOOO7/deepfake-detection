import cv2, numpy as np, os
from scipy import fftpack

def ela_analysis(image_path: str, quality: int = 85) -> float:
    img = cv2.imread(image_path)
    temp = "temp_ela.jpg"
    cv2.imwrite(temp, img, [cv2.IMWRITE_JPEG_QUALITY, quality])
    comp = cv2.imread(temp)
    os.remove(temp)
    diff = cv2.absdiff(img, comp)
    return np.mean(diff)

def frequency_analysis(image_path: str) -> str:
    gray = cv2.imread(image_path, 0)
    fft = fftpack.fft2(gray)
    shifted = fftpack.fftshift(fft)
    mag = np.log(np.abs(shifted) + 1e-5)
    return "High anomaly" if np.var(mag) > 10 else "Normal"
