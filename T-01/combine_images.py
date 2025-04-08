from utils import *

def combineImages(image1: np.ndarray, image2: np.ndarray, weight1: float, weight2: float) -> np.ndarray:
    """
    Combine two images using weighted average.
    The images are assumed to be in the range [0, 255] and are converted to the range [0, 1]
    before combining them.
    
    Parameters
    ----------
    image1 : np.ndarray
        The first input image.
    image2 : np.ndarray
        The second input image.
    weight1 : float
        The weight for the first image.
    weight2 : float
        The weight for the second image.
    
    Returns
    -------
    np.ndarray
        The combined image.
    """

    # Ensure the images are normalized to the range [0, 1]
    #image1_normalized = np.clip(image1 / 255.0, 0, 1)
    #image2_normalized = np.clip(image2 / 255.0, 0, 1)

    # Combine the images using weighted average
    combined_image = (weight1 * image1 + weight2 * image2)

    return combined_image