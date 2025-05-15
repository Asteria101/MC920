from utils import *
from horizontal_projection import *
from hough_transform import *


def main():
    # Input format
    # python3 align.py <input-image> <mode : hp (Horizontal Projection) | ht (Hough Transform)> 
    # <input-image> : filename, which must be in in-images
    if len(argv) != 3:
        print("Usage: python3 align.py <input-image> <mode : hp | ht>")
        return
    
    input_image = argv[1]
    mode = argv[2]

    source = cv2.imread(os.path.join("in-images", input_image))
    source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    
    if mode == "hp":
        # Binarization of source image, using otsu
        image = otsuThreshold(source)

        # Histogram of the source image
        hist = getHistogram(
                            np.sum(image, axis=1),
                            image.shape[0],
                            image.shape[1]
                            )
        save(hist, os.path.join("out-images/horizontal-projection", f"hist_{input_image}"))
        
        angle = projectHorizontally(image)
        rotated_img = rotate(image, angle)

        hist = getHistogram(
                            np.sum(rotated_img, axis=1), 
                            rotated_img.shape[0], 
                            rotated_img.shape[1]
                            )
        
        save(cv2.bitwise_not(rotated_img), os.path.join("out-images/horizontal-projection", f"rot_{input_image}"))
        save(hist, os.path.join("out-images/horizontal-projection", f"hist_rot_{input_image}"))

    elif mode == "ht":
        image = otsuThreshold(source)
        angle = applyHoughTransform(image)

        if angle != "No line detected":
            rotated_img = rotate(image, angle)
            save(cv2.bitwise_not(rotated_img), os.path.join("out-images/hough-transform", f"rot_{input_image}"))
        else:
            print(angle)
            return
        
    else:
        print("Invalid mode. Use 'hp' for Horizontal Projection or 'ht' for Hough Transform.")
        return

    
if __name__ == "__main__":
    main()