from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np
import cv2

def show(img: np.ndarray) -> None:
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()


def save(img: np.ndarray, filepath: str) -> None:
    if img.shape[-1] == 1:
        img = img[:, :, 0]

    plt.imsave(filepath, img, cmap='gray')


def histogramIt(img : np.ndarray)-> np.ndarray:
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    plt.hist(img.flatten(), 256, [0, 256], color='black')
    plt.xlim([0, 256])
    plt.show()
