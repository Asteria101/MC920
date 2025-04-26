from ditherer import *


def main() -> None:
    image: np.ndarray = io.imread("T-02/references/baboon_colored.png")
    image: np.ndarray = io.imread("T-02/in-images/baboon_monochromatic.png")
    dithered_img = Ditherer(image)

    dithered_img.floydSteinberg()

    #dithered_img.stevensonArce()

    dithered_img.show()
    dithered_img.save("T-02/out-images/baboon_monochromatic_dithered.png")
    #dithered_img.save("T-02/out-images/baboon_colored_dithered.png")


    
if __name__ == '__main__':
    main()