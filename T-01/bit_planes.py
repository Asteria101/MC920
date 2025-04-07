from imports import *

def extractBitPlanes(src_img: np.ndarray) -> list[np.ndarray]:
    """
    Extract the bit planes of a grayscale image.
    The function extracts the 8 bit planes of the image and returns them as a list of numpy arrays.
    
    Parameters
    ----------
    src_img : np.ndarray
        The input image in grayscale format.
        
    Returns
    -------
    list of np.ndarray
        A list containing the 8 bit planes of the image.
    """

    bit_planes_array = []
    for i in range(8):
        bit_planes_array.append((src_img >> i) & 1)

    return bit_planes_array