from utils import *

def applyHoughTransform(src_img : np.ndarray) -> int:
    """
    Applies the Hough Transform to detect lines in the input image.

    Parameters
    ----------
    src_img : np.ndarray
        The input image on which to apply the Hough Transform.

    Returns
    -------
    int
        The angle of the detected line in degrees.
    """

    gx = cv2.Sobel(src_img, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
    gy = cv2.Sobel(src_img, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)

    gx = cv2.convertScaleAbs(gx)
    gy = cv2.convertScaleAbs(gy)

    # Magnitude of edges
    edge_map = cv2.addWeighted(gx, 0.5, gy, 0.5, 0)

    # Apply Hough Transform
    linesP = cv2.HoughLinesP(
                             edge_map, 
                             1, 
                             np.pi / 180, 
                             threshold=90,
                             minLineLength=200,
                             maxLineGap=10
                             )

    accumulator = {}
    max_theta = None

    if linesP is not None:
        for line in linesP:
            x1, y1, x2, y2 = line[0]

            theta = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
            theta = theta % 360
            
            rho = int(x1 * np.cos(np.radians(theta)) + y1 * np.sin(np.radians(theta)))

            theta_rounded = int(np.round(theta)) % 360

            if (rho, theta_rounded) not in accumulator:
                accumulator[(rho, theta_rounded)] = 0   
            accumulator[(rho, theta_rounded)] += 1

    max_theta = max(accumulator, key=accumulator.get)[1]

    return max_theta if max_theta is not None else "No line detected"