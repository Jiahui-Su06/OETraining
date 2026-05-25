import cv2
import numpy as np

from PIL import Image
from sklearn.cluster import DBSCAN
from PySide6.QtCore import QThread, Signal

PIXEL_SIZE = 5.2e-3  # pixel size (mm)
LAMBDA = 632.8e-6  # wavelength (mm)
STEP = 0.2  # z direction sweep step (mm)


class ReconWorker(QThread):
    # define signal for progress
    progress_update = Signal(int)
    finished_data = Signal(list)
    error_occurred = Signal(str)

    def __init__(self, file_path, z_start, z_end):
        super().__init__()
        self.file_path = file_path
        self.z_start = z_start
        self.z_end = z_end

    def run(self):
        try:
            hologram = np.array(
                Image.open(self.file_path).convert('L'), 
                dtype=np.float32
            )  # to gray level
            hologram = (
                (hologram - hologram.min()) / 
                (hologram.max() - hologram.min())
            )  # normalization
            N, M = hologram.shape
            fx = np.fft.fftfreq(M, d=PIXEL_SIZE)
            fy = np.fft.fftfreq(N, d=PIXEL_SIZE)
            FX, FY = np.meshgrid(fx, fy)
            
            z = np.arange(self.z_start, self.z_end + STEP, STEP)
            steps = len(z)

            bubbles = []
            k = 2 * np.pi / LAMBDA  # wave vector
            for i, zi in enumerate(z):
                H = (np.exp(1j*k*zi) *  # transfer function
                     np.exp(-1j*np.pi*LAMBDA*zi*(FX**2+FY**2)))
                U0 = np.fft.ifft2(np.fft.fft2(hologram) * H)
                intensity = np.abs(U0)**2  # get object origin info

                # Object Light Processing
                img = cv2.normalize(
                    intensity, None,
                    0, 255,
                    cv2.NORM_MINMAX
                ).astype(np.uint8)
                background = cv2.medianBlur(img, 51) # get backgound light
                img = cv2.subtract(img, background)
                img = cv2.GaussianBlur(img, (7, 7), 0)
                # open calculation
                kernel = np.ones((3,3), np.uint8)
                img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
                img = cv2.Canny(img, 80, 200)

                # circle detection
                h, w = img.shape
                circles = cv2.HoughCircles(
                    img, cv2.HOUGH_GRADIENT,
                    dp=1.2, minDist=20,
                    param1=50, param2=15,
                    minRadius=15, maxRadius=92
                )
                if circles is not None:
                    for c in circles[0]:
                        x, y, r = c
                        if 0 <= int(y) < h and 0 <= int(x) < w:
                            score = img[int(y), int(x)]
                        else:
                            score = 0
                        bubbles.append({
                            'x': x,
                            'y': y,
                            'z': zi,
                            'r': r,
                            'score': score
                        })
                
                progress = int(((i + 1) / steps) * 90)
                self.progress_update.emit(progress)

            # 3D localization of bubbles (DBSCAN)
            bubbles_3d = []
            if bubbles:
                data = np.array([[b['x'], b['y'], b['r']] for b in bubbles])
                clustering = DBSCAN(eps=35, min_samples=1).fit(data)  # < 35 is the same one
                labels = clustering.labels_
                for label in set(labels):
                    if label == -1:
                        continue
                    group = [b for b, l in zip(bubbles, labels) if l == label]
                    best = max(group, key=lambda b: b['score'])
                    bubbles_3d.append(best)
            
            self.progress_update.emit(100)
            self.finished_data.emit(bubbles_3d)
        except Exception as e:
            self.error_occurred.emit(str(e))