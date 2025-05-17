from utils import *

def projectHorizontally(src_img: np.ndarray) -> int:
    """
    Algorithm that rotates the image based on its horizontal projection.
    
    Parameters
    ----------
    src_img : np.ndarray
        Input image to be rotated.
    
    Return
    -------
    np.ndarray
        Rotated image.
    """

    height, width = src_img.shape
    center = (width // 2, height // 2)

    values = {}

    for theta in range(0, 181):
        # transformation matrix
        M = cv2.getRotationMatrix2D(center, theta, 1)

        # rotate the image
        rotated = cv2.warpAffine(src_img, M, (width, height))

        # calculate the horizontal projection
        hp_rotated = np.sum(rotated, axis=1)

        values[theta] = np.sum((hp_rotated[:-1] - hp_rotated[1:]) ** 2)

    max_theta = max(values, key=values.get)
    
    if max_theta > 90:
        max_theta = max_theta - 180

    return max_theta