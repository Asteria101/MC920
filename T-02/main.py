from ditherer import *
from frequency_domain import *
from compression import *


def main() -> None:
    image: np.ndarray = io.imread("T-02/in-images/baboon_mono.png")
    #image: np.ndarray = io.imread("T-02/in-images/peppers.png")
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image2 = io.imread("T-02/in-images/baboon.png")
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #save(squareComparison(image, 40), "T-02/out-images/1.1/m_src_square.png")

    #save(dither(image, floyd_steinberg, 1, 1, 1), "T-02/out-images/1.1/c_floyd_steinberg.png")
    #save(squareComparison(dither(image, floyd_steinberg, 1, 1, 1), 40), "T-02/out-images/1.1/m_fs_square.png")

    #save(dither(image, stevenson_arce, 3, 3, 1), "T-02/out-images/1.1/stevenson_arce.png")
    #save(squareComparison(dither(image, stevenson_arce, 3, 3, 1), 40), "T-02/out-images/1.1/m_sa_square.png")
    #save(squareComparison(dither(image2, stevenson_arce, 3, 3, 1), 40), "T-02/out-images/1.1/c_sa_square.png")

    #save(dither(image, burkes, 2, 1, 1), "T-02/out-images/1.1/colored_burkes.png")
    #save(squareComparison(dither(image, burkes, 2, 1, 1), 40), "T-02/out-images/1.1/m_b_square.png")
    #save(squareComparison(dither(image2, burkes, 2, 1, 1), 40), "T-02/out-images/1.1/c_b_square.png")

    #save(dither(image, sierra, 2, 2, 1), "T-02/out-images/1.1/m_sierra.png")
    #save(squareComparison(dither(image, sierra, 2, 2, 1), 40), "T-02/out-images/1.1/m_s_square.png")
    #save(squareComparison(dither(image2, sierra, 2, 2, 1), 40), "T-02/out-images/1.1/c_s_square.png")

    #save(dither(image, stucki, 2, 2, 1), "T-02/out-images/1.1/c_stucki.png")
    #save(squareComparison(dither(image, stucki, 2, 2, 1), 40), "T-02/out-images/1.1/m_st_square.png")
    #save(squareComparison(dither(image2, stucki, 2, 2, 1), 40), "T-02/out-images/1.1/c_st_square.png")

    #save(dither(image, jarvis_judice_ninke, 2, 2, 1), "T-02/out-images/1.1/m_jarvis_judice_ninke.png")
    #save(squareComparison(dither(image, jarvis_judice_ninke, 2, 2, 1), 40), "T-02/out-images/1.1/m_jjn_square.png")
    #save(squareComparison(dither(image2, jarvis_judice_ninke, 2, 2, 1), 40), "T-02/out-images/1.1/c_jjn_square.png")

    #frenquencyDomainFiltering(image)
    #histogramIt(compress(image, 90), "T-02/out-images/histogram.png")
    #histogramIt(compress(image, 10))
    #histogramIt(compress(image, 90))
    #histogramIt(compress(image, 150))
    
if __name__ == '__main__':
    main()