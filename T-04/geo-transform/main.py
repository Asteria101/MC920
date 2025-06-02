import numpy as np
import cv2
import skimage as ski
import matplotlib.pyplot as plt
from sys import argv
import argparse

def entry() -> argparse.Namespace:
    """
    Parses command line arguments for the geometric transformation program.

    Input format
    ----------
    python3 main.py [-a angle] 
                    [-s scale] 
                    [-d width height] 
                    [m interpolation] 
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
    
    parser.add_argument("-d", type=int, nargs=2, default=[0, 0],
                        help="Dimensions of the output image as width and height (default: 0 0)")
    
    parser.add_argument("-m", required=True, type=str, choices=["n", "b", "bi", "l"],
                        help="Interpolation method: \n- n [nearest];\n- b [bilinear];\n- bi [bicubic];\n- l [lagrange polynomial].")
    
    parser.add_argument("-i", required=True, type=str, help="Input image file path")

    return parser.parse_args()


def main():
    args = entry()

    src = cv2.imread(args.i)
    plt.imshow(src)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
