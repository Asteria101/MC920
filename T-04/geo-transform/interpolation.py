from utils import *

def bilinear(src : np.ndarray, c : int, r : int, ch : int) -> np.ndarray:
    """
    Bilinear interpolation function.

    Parameters
    ----------
    src : np.ndarray
        The source image from which to interpolate.
    c : int
        The x-coordinate in the source image.
    r : int
        The y-coordinate in the source image.
    ch : int
        The channel index to interpolate

    Returns
    -------
    np.ndarray
        The interpolated pixel value at (r, c, ch).
    """

    x = int(np.trunc(c))
    y = int(np.trunc(r))

    dx = c - x
    dy = r - y

    if x + 1 < src.shape[1] and y + 1 < src.shape[0]:
        B1 = (1 - dx) * (1 - dy) * src[y, x, ch]
        B2 = dx * (1 - dy) * src[y, x + 1, ch]
        B3 = (1 - dx) * dy * src[y + 1, x, ch]
        B4 = dx * dy * src[y + 1, x + 1, ch]

        return B1 + B2 + B3 + B4
    
    else:
        return 255


def bicubic(src : np.ndarray, c : int, r : int, ch : int) -> np.ndarray:
    """
    Bicubic interpolation function.
    
    Parameters
    ----------
    src : np.ndarray
        The source image from which to interpolate.
    c : int
        The x-coordinate in the source image.
    r : int
        The y-coordinate in the source image.
    ch : int
        The channel index to interpolate.
        
    Returns
    -------
    np.ndarray
        The interpolated pixel value at (r, c, ch).
    """

    def P(t):
        return t if t > 0 else 0
    
    def R(s):
        return ((P(s + 2) ** 3) - 4 * (P(s + 1) ** 3) + 6 * (P(s) ** 3) - 4 * (P(s - 1) ** 3)) / 6
    
    x = int(np.trunc(c))
    y = int(np.trunc(r))

    dx = c - x
    dy = r - y

    p_bicubic = 0
    for m in range(-1, 3):
        for n in range(-1, 3):
            if (0 <= x + m < src.shape[1]) and (0 <= y + n < src.shape[0]):
                p_bicubic += src[y + n, x + m, ch] * R(m - dx) * R(dy - n)
            else:
                p_bicubic = 0
    
    return p_bicubic


def lagrange(src : np.ndarray, c : int, r : int, ch : int) -> np.ndarray:
    """
    Lagrange polynomial interpolation function.

    Parameters
    ----------
    src : np.ndarray
        The source image from which to interpolate.
    w : int
        The width of the source image.
    h : int
        The height of the source image.
    c : int
        The x-coordinate in the source image.
    r : int
        The y-coordinate in the source image.
    ch : int
        The channel index to interpolate.

    Returns
    -------
    np.ndarray
        The interpolated pixel value at (r, c, ch).
    """

    def L(src, n, x, y, dx, ch):
        if (0 <= x < src.shape[1]) and (0 <= y < src.shape[0]) and (0 <= x - 1 < src.shape[1]) and (0 <= x + 1 < src.shape[1]) and (0 <= x + 2 < src.shape[1]) and (0 <= y + n - 2 < src.shape[0]):
            L1 = (-dx * (dx - 1) * (dx - 2) * src[y + n - 2, x - 1, ch]) / 6
            L2 = ((dx + 1) * (dx - 1) * (dx - 2) * src[y + n - 2, x, ch]) / 2
            L3 = (-dx * (dx + 1) * (dx - 2) * src[y + n - 2, x + 1, ch]) / 2
            L4 = (dx * (dx + 1) * (dx - 1) * src[y + n - 2, x + 2, ch]) / 6

            return L1 + L2 + L3 + L4
        
        return 0
    
    x = int(np.trunc(c))
    y = int(np.trunc(r))

    dx = c - x
    dy = r - y

    L1 = (-dy * (dy - -1) * (dy - 2) * L(src, 1, x, y, dx, ch)) / 6
    L2 = ((dy + 1) * (dy - 1) * (dy - 2) * L(src, 2, x, y, dx, ch)) / 2
    L3 = (-dy * (dy + 1) * (dy - 2) * L(src, 3, x, y, dx, ch)) / 2
    L4 = (dy * (dy + 1) * (dy - 1) * L(src, 4, x, y, dx, ch)) / 6

    return L1 + L2 + L3 + L4
