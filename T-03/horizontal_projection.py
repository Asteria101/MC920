from utils import *

def projectHorizontally(src_img: np.ndarray) -> np.ndarray:
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

    hp = np.sum(src_img, axis = 1)

    def objective_function(hp):
        return np.sum((hp[:-1] - hp[1:]) ** 2)

    values = dict()

    # working with neighborhood 4
    for theta in range(-360, 361):
        # transformation matrix
        M = cv2.getRotationMatrix2D(center, theta, 1)

        # rotate the image
        rotated = cv2.warpAffine(src_img, M, (width, height))

        # calculate the horizontal projection
        hp_rotated = np.sum(rotated, axis=1)

        values[theta] = objective_function(hp_rotated)

    max_theta = max(values, key=values.get)
    M = cv2.getRotationMatrix2D(center, 180 + max_theta, 1)

    return cv2.warpAffine(src_img, M, (width, height), flags=cv2.INTER_CUBIC)
