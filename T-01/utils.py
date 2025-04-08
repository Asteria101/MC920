from skimage import io, filters, color
import matplotlib.pyplot as plt
import numpy as np

def isRGB(image):
    """
    Verifies if the given image is in RGB format.

    Parameters:
        image (numpy.ndarray): The image to check.

    Returns:
        bool: True if the image is RGB, False otherwise.
    """
    return len(image.shape) == 3 and image.shape[2] == 3