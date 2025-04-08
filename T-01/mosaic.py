from utils import *

def createMosaic(src_img: np.ndarray, n_blocks: int) -> np.ndarray:
    """
    Create a mosaic grayscale image by rearranging blocks of the original grayscale image in a specific pattern.

    Parameters
    ----------
    src_img : np.ndarray
        The input image in grayscale format.
    n_blocks : int
        The number of blocks to divide the image into. Making it be a n_blocks x n_blocks grid.

    Returns
    -------
    np.ndarray
        The mosaic image created by rearranging the blocks of the original image.
    """

    if (isRGB(src_img)):
        src_img = color.rgb2gray(src_img)

    # Reshape the original image into the desired number of blocks 
    array_blocks = src_img.reshape(n_blocks, src_img.shape[0]//n_blocks, n_blocks, src_img.shape[1]//n_blocks).swapaxes(1, 2)

    # Create a new array to hold the mosaic image
    mosaic_image = np.zeros_like(array_blocks)

    # Rearrange the blocks in a specific pattern
    mosaic_image[0, 0] = array_blocks[1, 1]
    mosaic_image[0, 1] = array_blocks[2, 2]
    mosaic_image[0, 2] = array_blocks[3, 0]
    mosaic_image[0, 3] = array_blocks[0, 2]

    mosaic_image[1, 0] = array_blocks[1, 0]
    mosaic_image[1, 1] = array_blocks[3, 3]
    mosaic_image[1, 2] = array_blocks[0, 0]
    mosaic_image[1, 3] = array_blocks[2, 0]

    mosaic_image[2, 0] = array_blocks[2, 3]
    mosaic_image[2, 1] = array_blocks[3, 1]
    mosaic_image[2, 2] = array_blocks[0, 1]
    mosaic_image[2, 3] = array_blocks[1, 2]

    mosaic_image[3, 0] = array_blocks[0, 3]
    mosaic_image[3, 1] = array_blocks[3, 2]
    mosaic_image[3, 2] = array_blocks[2, 1]
    mosaic_image[3, 3] = array_blocks[1, 0]

    # Reshape the mosaic image back to the original dimensions
    return mosaic_image.swapaxes(1, 2).reshape(src_img.shape[0], src_img.shape[1])
