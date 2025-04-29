from utils import *

def masking(mask_type: int, height: int, width: int, r1: int, r2: int = None) -> np.array:
    # Find center of the image
    cx, cy = width // 2, height // 2
    # Generates a series of points from the image in order to calculate the function for the circle
    x, y = np.ogrid[: height, : width]

    # Low pass
    if mask_type == 0:
        mask = np.zeros((height, width), np.uint8)
        circle1 = (x - cx) ** 2 + (y - cy) ** 2 <= r1 ** 2
        mask[circle1] = 1
        return mask
    
    # High pass
    elif mask_type == 1:
        mask = np.ones((height, width), np.uint8)
        circle1 = (x - cx) ** 2 + (y - cy) ** 2 <= r1 ** 2
        mask[circle1] = 0
        return mask
    
    # Band pass
    elif mask_type == 2:
        mask = np.zeros((height, width), np.uint8)
        circle1 = (x - cx) ** 2 + (y - cy) ** 2 >= r1 ** 2
        circle2 = (x - cx) ** 2 + (y - cy) ** 2 <= r2 ** 2
        mask[circle1&circle2] = 1
        return mask
    
    # Band reject
    elif mask_type == 3:
        mask = np.ones((height, width), np.uint8)
        circle1 = (x - cx) ** 2 + (y - cy) ** 2 >= r1 ** 2
        circle2 = (x - cx) ** 2 + (y - cy) ** 2 <= r2 ** 2
        mask[circle1&circle2] = 0
        return mask
    
    return None


def inverseFDT(img: np.ndarray) -> np.ndarray:
    fishift = np.fft.ifftshift(img)
    fi_img = np.fft.ifft2(fishift)
    fi_img = np.abs(fi_img)
    return fi_img


def frenquencyDomainFiltering(img: np.ndarray) -> None:
    # Apply fft
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)

    # Fourier spectrum
    magnitude_spectrum = 20 * np.log(np.abs(fshift))
    save(magnitude_spectrum, "T-02/out-images/1.2/peppers/magnitude_spectrum.png")

    # Apply fft inversed
    inverse_img = inverseFDT(fshift)
    save(inverse_img, "T-02/out-images/1.2/peppers/inverse_img.png")

    # Low pass
    lp_mask = masking(0, img.shape[0], img.shape[1], 60)
    save(lp_mask, "T-02/out-images/1.2/peppers/lp_mask.png")
    save(lp_mask * magnitude_spectrum, "T-02/out-images/1.2/peppers/lp_mask_mag.png")
    lp_img = fshift * lp_mask
    lp_img = inverseFDT(lp_img)
    save(lp_img, "T-02/out-images/1.2/peppers/lp_img.png")
    
    # High pass
    hp_mask = masking(1, img.shape[0], img.shape[1], 60)
    save(hp_mask, "T-02/out-images/1.2/peppers/hp_mask.png")
    save(hp_mask * magnitude_spectrum, "T-02/out-images/1.2/peppers/hp_mask_mag.png")
    hp_img = fshift * hp_mask
    hp_img = inverseFDT(hp_img)
    save(hp_img, "T-02/out-images/1.2/peppers/hp_img.png")

    # Band pass
    bp_mask = masking(2, img.shape[0], img.shape[1], 40, 100)
    save(bp_mask, "T-02/out-images/1.2/peppers/bp_mask.png")
    save(bp_mask * magnitude_spectrum, "T-02/out-images/1.2/peppers/bp_mask_mag.png")
    bp_img = fshift * bp_mask
    bp_img = inverseFDT(bp_img)
    save(bp_img, "T-02/out-images/1.2/peppers/bp_img.png")

    # Band reject
    br_mask = masking(3, img.shape[0], img.shape[1], 40, 100)
    save(br_mask, "T-02/out-images/1.2/peppers/br_mask.png")
    save(br_mask * magnitude_spectrum, "T-02/out-images/1.2/peppers/br_mask_mag.png")
    br_img = fshift * br_mask
    br_img = inverseFDT(br_img)
    save(br_img, "T-02/out-images/1.2/peppers/br_img.png")

    return None