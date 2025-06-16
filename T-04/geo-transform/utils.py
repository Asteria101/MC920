import numpy as np
import cv2
import skimage as ski
import matplotlib.pyplot as plt
from sys import argv
import argparse

def read() -> argparse.Namespace:
    """
    Parses command line arguments for the geometric transformation program.

    Input format
    ----------
    python3 main.py [-a angle] 
                    [-s scale] 
                    [-d width height] 
                    [-m interpolation] 
                    [-i input] 
                    [-o output]

    Returns
    -------
    argparse.Namespace
        An object containing the parsed command line arguments.
    """

    parser = argparse.ArgumentParser(description="Program for operating scale or rotation \
                                     on digital images, through geometric transformations.")
    
    parser.add_argument("-a", type=float, default=0.0,
                        help="Angle of rotation in degrees (default: 0.0)")
    
    parser.add_argument("-s", type=float, default=1.0,
                        help="Scale factor (default: 1.0)")
    
    parser.add_argument("-d", type=int, nargs=2, default=None,
                        help="Dimensions of the output image as width and height (default: 0 0)")
    
    parser.add_argument("-m", required=True, type=str, choices=["n", "b", "bi", "l"],
                        help="Interpolation method: \n- n [nearest];\n- b [bilinear];\n- bi [bicubic];\n- l [lagrange polynomial].")
    
    parser.add_argument("-i", required=True, type=str, help="Input image file path")

    return parser.parse_args()


def show(img: np.ndarray) -> None:
    """
    Display an image using matplotlib.

    Parameters
    ----------
    img : np.ndarray
        The image to be displayed in grayscale.
    """

    plt.imshow(img) 
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