from utils import *


def applyBrightnessAdjustment(src_img: np.ndarray, gamma: float) -> np.ndarray:
    """
    Adjust the brightness of a monochromatic image using gamma correction.
    
    Parameters
    ----------
    src_img : np.ndarray
        The input monochromatic image.
    gamma : float
        The gamma value for brightness adjustment. A value less than 1 will decrease brightness,
        while a value greater than 1 will increase brightness.

    Returns
    -------
    np.ndarray
        The brightness-adjusted image.
    """

    if (isRGB(src_img)):
        src_img = color.rgb2gray(src_img)

    # (i) Normalize image
    normalized_image = np.clip(src_img / 255.0, 0, 1)

    # (ii) Apply gamma correction
    adjusted_image = np.power(normalized_image, 1 / gamma)

    # (iii) Scale back to 0-255 range
    adjusted_image = (adjusted_image * 255).astype(np.uint8)

    return adjusted_image