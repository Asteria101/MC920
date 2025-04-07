from imports import *

def turn2PencilSketch(src_img: np.ndarray) -> np.ndarray:
    """
    Convert a colored image to a pencil sketch

    Parameters
    ----------
    src_img : np.ndarray
        The input image in RGB format.

    Returns
    -------
    np.ndarray
        The pencil sketch of the input image.
    """

    # (i) Convert image to grayscale
    gray_image = color.rgb2gray(src_img)

    # Invert the grayscale image
    inverted_image = 1 - gray_image

    # (ii) Apply Gaussian blur to the grayscale image
    blurred_image = filters.gaussian(inverted_image, sigma=np.sqrt(21-1)/2)

    # (iii) Enhance contrast of the image according to the grayscale image and the blurred image
    final_image = gray_image / (1 - blurred_image + 1e-5)

    # It ensures that pixel values are contained within the range [0, 1]
    final_image = np.clip(final_image, 0, 1)

    return final_image
