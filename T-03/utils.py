import matplotlib.pyplot as plt
import numpy as np
import cv2

from sys import argv
import subprocess
import os



def show(img: np.ndarray) -> None:
    """
    Display an image using matplotlib.

    Parameters
    ----------
    img : np.ndarray
        The image to be displayed in grayscale.
    """

    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.show()


def save(img: np.ndarray, filepath: str) -> None:
    """
    Stores an image in a specified path.

    Parameters
    ----------
    img : np.ndarray
        The image to be stored.
    
    filepath : str
        The path where the image will be stored.
    """

    if img.shape[-1] == 1:
        img = img[:, :, 0]

    plt.imsave(filepath, img, cmap='gray')


def rotate(img: np.ndarray, angle: float) -> np.ndarray:
    """
    Rotates the image by a specified angle.

    Parameters
    ----------
    img : np.ndarray
        The input image to be rotated.
    
    angle : float
        The angle by which to rotate the image.
    
    Returns
    -------
    np.ndarray
        The rotated image.
    """

    height, width = img.shape[:2]
    center = (width // 2, height // 2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_img = cv2.warpAffine(img, M, (width, height))

    return rotated_img


def getHistogram(horizontal_projection: np.array, height : int, width : int) -> np.ndarray:
    """
    Create a histogram image based on the horizontal projection of an image.
    
    Parameters
    ----------
    horizontal_projection : np.array
        The horizontal projection of the image.
        
    width : int
        The width of the histogram image.
        
    height : int
        The height of the histogram image.
        
    Returns
    -------
    np.ndarray
        The histogram image.
    """

    # Create the histogram image
    hist = np.ones((height, width), np.uint8)
    for i in range(height):
        cv2.line(
            hist,
            (0, i),
            (int(horizontal_projection[i] * width / height), i),
            (0, 0, 0), 
            1
        )

    return hist


def otsuThreshold(img: np.ndarray) -> np.ndarray:
    """
    Applies Otsu's thresholding method to the input image.

    Parameters
    ----------
    img : np.ndarray
        The input image to be thresholded.
    
    Returns
    -------
    np.ndarray
        The thresholded image.
    """

    _, th_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    th_img[th_img == 0] = 1
    th_img[th_img == 255] = 0
    return th_img
