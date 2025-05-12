from utils import *
from horizontal_projection import *
from hough_transform import *

def main():
    # Production of output images
    filenames = os.listdir("T-03/in-images/")

    folders = [
        "T-03/out-images/horizontal-projection/",
        "T-03/out-images/hough-transform/"
    ]

    for i in range(len(filenames)):
        for j in range(len(folders)):
            image = cv2.imread(f"T-03/in-images/{filenames[i]}")
            
            if j == 0:
                out_img = projectHorizontally(prepare(image))
                # Store the output image and its histogram  
                save(cv2.bitwise_not(out_img), f"{folders[j]}{filenames[i]}")
                save(
                    histogramIt(np.sum(out_img, axis=1), out_img.shape[1], out_img.shape[0]),
                    f"{folders[j]}hist_{filenames[i]}"
                )
            elif j == 1:
                print("oi")


    
    
if __name__ == "__main__":
    main()