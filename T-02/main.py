from ditherer import *
from frequency_domain import *
from compression import *


def main() -> None:
    image: np.ndarray = io.imread("T-02/in-images/baboon_mono.png")
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    save(dither(image, floyd_steinberg, 1, 1, 1), "T-02/out-images/floyd_steinberg.png")

    """save(dither(image, stevenson_arce, 3, 3, 1), "T-02/out-images/stevenson_arce.png")

    save(dither(image, burkes, 1, 2, 1), "T-02/out-images/burkes.png")

    save(dither(image, sierra, 2, 2, 1), "T-02/out-images/sierra.png")

    save(dither(image, stucki, 2, 2, 1), "T-02/out-images/stucki.png")

    save(dither(image, jarvis_judice_ninke, 2, 2, 1), "T-02/out-images/jarvis_judice_ninke.png")"""


    #frenquencyDomainFiltering(image)
    #histogramIt(compress(image, 90), "T-02/out-images/histogram.png")
    #histogramIt(compress(image, 10))
    #histogramIt(compress(image, 90))
    #histogramIt(compress(image, 150))
    
if __name__ == '__main__':
    main()