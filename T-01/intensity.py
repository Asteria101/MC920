from utils import *

def applyIntensityTransformation(src_img: np.ndarray) -> np.ndarray:
    """
    Apply intensity transformations to the input image.
    The transformations include:
    1. Negative transformation
    2. Contrast stretching
    3. Inversion of even lines
    4. Reflection of lines
    5. Vertical mirror
    
    Parameters
    ----------
    src_img : np.ndarray
        The input image in grayscale format.

    Returns
    -------
    np.ndarray
        A tuple containing the transformed images.
    """

    negative_image = -src_img

    contrast_image = np.clip(src_img, 100, 200)

    inverted_even_lines_image = src_img.copy()
    inverted_even_lines_image[::2] = src_img[::2, ::-1]

    reflected_lines_image = src_img.copy()
    height = src_img.shape[0]
    top_half = src_img[:height // 2]
    reflected_lines_image[height // 2:] = top_half[::-1]

    vertical_mirror_image = src_img.copy()
    vertical_mirror_image = src_img[::-1]

    return negative_image, contrast_image, inverted_even_lines_image, reflected_lines_image, vertical_mirror_image