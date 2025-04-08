from utils import *

def quantization(src_img: np.ndarray, bit_level: int) -> np.ndarray:
    """
    Reduces the number of intensity levels in a grayscale image by performing quantization.

    Parameters:
    -----------
    src_img : np.ndarray
        The input image in RGB format.
    bit_level : int
        The desired bit depth for the quantized image.

    Returns:
    --------
    np.ndarray
        The quantized grayscale image as a 2D NumPy array with reduced intensity levels.
    """

    level = 2 ** (8 - bit_level)

    # Ensures all pixel are values multiples of level 
    quantizaded_image = (src_img // level) * level
    
    return quantizaded_image