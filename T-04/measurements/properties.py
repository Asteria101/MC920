import matplotlib.pyplot as plt
import numpy as np
import cv2
import skimage as ski
from sys import argv


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


def getContours(src_img: np.ndarray) -> list[np.array]:
    """
    Extracts contours from a binary image.

    Parameters
    ----------
    src_img : np.ndarray
        The binary image from which contours will be extracted.

    Returns
    -------
    list[np.array]
        A list of contours found in the image.
    """

    canvas = np.ones_like(src_img, np.uint8) * 255
    contours = cv2.findContours(src_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

    contoured_image = cv2.drawContours(canvas, contours, -1, (0, 0, 0), 0)
    save(contoured_image, f"out-images/contoured_{argv[1]}")

    return contours



def getEccentricity(obj: np.array) -> float:
    """
    Calculates the eccentricity of a contour.
    
    Parameters
    ----------
    obj : np.array
        The contour of the object.
        
    Returns
    -------
    float
        The eccentricity of the contour, defined as the ratio of the lengths of the major and minor axes.
    """

    extreme_points = [tuple(obj[obj[:,:,0].argmin()][0]),
                      tuple(obj[obj[:,:,0].argmax()][0]),
                      tuple(obj[obj[:,:,1].argmin()][0]),
                      tuple(obj[obj[:,:,1].argmax()][0])
                      ]

    axis_a = np.linalg.norm(np.array(extreme_points[0]) - np.array(extreme_points[1]))
    axis_b = np.linalg.norm(np.array(extreme_points[2]) - np.array(extreme_points[3]))

    return axis_a / axis_b if axis_a > axis_b else axis_b / axis_a


def getSolidity(obj: np.array) -> float:
    """
    Calculates the solidity of a contour.
    
    Parameters
    ----------
    obj : np.array
        The contour of the object.
        
    Returns
    -------
    float
        The solidity of the contour, defined as the ratio of the area of the contour to the area of its convex hull.
    """

    area = cv2.contourArea(obj)
    hull = cv2.convexHull(obj)
    hull_area = cv2.contourArea(hull)

    return float(area) / hull_area


def areaHistogram(areas: list[int]) -> None:
    """
    Displays a histogram of the areas of the regions.

    Parameters
    ----------
    areas : list[float]
        List of areas of the regions.
    """
    
    plt.hist(areas, bins=[min(areas) if min(areas) < 1500 else 0, 1500, 3000, max(areas) if max(areas) >= 3000 else 4500], color='blue', edgecolor='darkblue')
    plt.xlabel('Área')
    plt.ylabel('Número de Objetos')
    plt.savefig(f"out-images/histogram_{argv[1]}")
