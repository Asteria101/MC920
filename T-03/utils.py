import matplotlib.pyplot as plt
import numpy as np
import cv2
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


def prepare(img: np.ndarray) -> np.ndarray:
    """
    Prepares the image for processing by converting it to 
    grayscale, inverting colors, and applying a binary threshold.

    Parameters
    ----------
    img : np.ndarray
        The input image to be prepared.
    
    Returns
    -------
    np.ndarray
        The prepared image.
    """

    if len(img.shape) > 2:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.bitwise_not(img)

    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    img[img == 0] = 1
    img[img == 255] = 0

    return img


def histogramIt(horizontal_projection: np.array, width : int, height : int) -> np.ndarray:
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