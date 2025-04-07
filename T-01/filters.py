from imports import *

def applyOldPhotoFilter(src_img: np.ndarray) -> np.ndarray:
    """
    Apply a filter to give the colored source image an old photo effect.
    The filter is applied to the RGB channels of the image.
    
    Parameters
    ----------
    src_img : np.ndarray
        The input image in RGB format.
        
    Returns
    -------
    np.ndarray
        The image with the old photo effect applied.
    """

    # filter is a 3x3 matrix that defines the sepia filter
    filter = np.array([[0.393, 0.769, 0.189],
                      [0.349, 0.686, 0.168],
                      [0.272, 0.534, 0.131]])

    # Multiplies each pixel (excluding a posible alpha channel for RGBA images) of the image by 
    # the filter and then clips the values so it stays in the range [0, 255] and converts to uint8
    # Note: the filter is transposed to match the shape of the image
    final_img = np.dot(src_img[..., :3], filter.T).clip(0, 255).astype(np.uint8)

    return final_img


def transformColorImage(src_img: np.ndarray) -> tuple[np.ndarray]:
    """
    Apply two different filters to the colored source image.
    The filters are applied to the RGB channels of the image.
    
    Parameters
    ----------
    src_img : np.ndarray
        The input image in RGB format.
        
    Returns
    -------
    tuple of np.ndarray
        A tuple containing two images with different filters applied.
    """

    filter_a = np.array([[0.393, 0.769, 0.189],
                        [0.349, 0.686, 0.168],
                        [0.272, 0.534, 0.131]])
    
    filter_b = np.array([0.2989, 0.5870, 0.1140])

    # (a)
    final_img_a = np.dot(src_img[..., :3], filter_a.T).clip(0, 255).astype(np.uint8)

    # (b)
    final_img_b = np.dot(src_img[..., :3], filter_b.T)

    return final_img_a, final_img_b