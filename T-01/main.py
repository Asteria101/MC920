from utils import *
from pencil_sketch import *
from brightness_adjustment import *
from mosaic import *
from filters import *
from bit_planes import *
from combine_images import *
from intensity import *
from quantization import *


def main() -> None:
    input_rgb_images: list[str] = [
        'baboon_colored.png',
        'monalisa.png',
        'peppers.png',
        'watch.png'
    ]

    input_monochromatic_images: list[str] = [
        'baboon_monochromatic.png',
        'butterfly.png',
        'city.png',
        'house.png'
    ]


    # 1.1 - Pencil Sketch
    #for i, img in enumerate(input_rgb_images):
    #    pencil_sketch_img = turn2PencilSketch(io.imread('T-01/in-images/' + img))    
    #    plt.imsave("T-01/out-images/1/" + "1." + img, pencil_sketch_img, cmap="gray")


    # 1.2 - Brightness Adjustment
    #gamma_values = [0.05, 0.2, 0.5, 1, 1.5, 2.5, 5]
    #for i in range(len(gamma_values)):
    #    brightness_adjusted_img = applyBrightnessAdjustment(io.imread('T-01/in-images/baboon_monochromatic.png'), gamma_values[i])
    #    plt.imsave(f'T-01/out-images/2/2.{i+1}.baboon_monochromatic_{gamma_values[i]}.png', brightness_adjusted_img, cmap="gray")


    # 1.3 - Mosaic
    #for i, img in enumerate(input_monochromatic_images):
    #    mosaic_img = createMosaic(io.imread('T-01/in-images/' + img), 4)    
    #    plt.imsave("T-01/out-images/3/" + "3." + img, mosaic_img, cmap="gray")

    
    # 1.4 - Color change
    #for i, img in enumerate(input_rgb_images):
    #    old_photo_img = applyOldPhotoFilter(io.imread('T-01/in-images/' + img))
    #    plt.imsave("T-01/out-images/4/" + "4." + img, old_photo_img, cmap="gray")

    
    # 1.5 - Change colored images
    # img_a and img_b are of type np.ndarray
    #for i, img in enumerate(input_rgb_images):
    #    img_a, img_b = transformColorImage(io.imread('T-01/in-images/' + img))
    #    plt.imsave("T-01/out-images/5/a/" + "5.a." + img, img_a, cmap="gray")
    #    plt.imsave("T-01/out-images/5/b/" + "5.b." + img, img_b)

    
    # 1.6 - Extract bit planes
    #bit_planes: list[np.ndarray] = extractBitPlanes(io.imread('T-01/in-images/baboon_monochromatic.png'))
    #for i in range(len(bit_planes)):
    #    plt.imsave(f"T-01/out-images/6/6.{i}.babbon.png", bit_planes[i], cmap="gray")


    # 1.7 - Combine images
    #combined_img = combineImages(io.imread('T-01/in-images/baboon_monochromatic.png'), io.imread('T-01/in-images/butterfly.png'), 0.3, 0.7)
    #plt.imsave("T-01/out-images/7/7.1.baboon_butterfly.png", combined_img, cmap="gray")


    # 1.8 - Intensity transformation
    #negative_img, contrast_img, inverted_even_lines_img, reflected_lines_img, vertical_mirror_img = applyIntensityTransformation(io.imread('T-01/in-images/city.png'))
    #plt.imsave("T-01/out-images/8/8.1.city_negative.png", negative_img, cmap="gray")
    #plt.imsave("T-01/out-images/8/8.2.city_contrast.png", contrast_img, cmap="gray")
    #plt.imsave("T-01/out-images/8/8.3.city_inverted_even_lines.png", inverted_even_lines_img, cmap="gray")
    #plt.imsave("T-01/out-images/8/8.4.city_reflected_lines.png", reflected_lines_img, cmap="gray")
    #plt.imsave("T-01/out-images/8/8.5.city_vertical_mirror.png", vertical_mirror_img, cmap="gray")

    
    # 1.9 - Quantization
    #for i in range(1, 9):
    #    quantizaded_img = quantization(io.imread('T-01/in-images/baboon_monochromatic.png'), i)
    #    plt.imsave(f"T-01/out-images/9/9.{i-1}.baboon_{2**i}.png", quantizaded_img, cmap="gray")

    
    # 1.10 - Filter application
    h1 = np.array([[0, 0, -1, 0, 0], 
                   [0, -1, -2, -1, 0],
                   [-1, -2, 16, -2, -1],
                   [0, -1, -2, -1, 0],
                   [0, 0, -1, 0, 0]])
    
    h2 = np.array([[1, 4, 6, 4, 1],
                   [4, 16, 24, 16, 4],
                   [6, 24, 36, 24, 6],
                   [4, 16, 24, 16, 4],
                   [1, 4, 6, 4, 1]]) / (256)
    
    h3 = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    
    h4 = np.array([[-1, -2, -1], 
                   [0, 0, 0],
                   [1, 2, 1]])

    h5 = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])
    
    h6 = np.array([[1, 1, 1], 
                   [1, 1, 1],
                   [1, 1, 1]]) / 9
    
    h7 = np.array([[-1, -1, 2], 
                   [-1, 2, -1],
                   [2, -1, -1]])
    
    h8 = np.array([[2, -1, -1],
                   [-1, 2, -1],
                   [-1, -1, 2]])
    
    h9 = np.array(([1, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1])) / 9
    
    h10 = np.array([[-1, -1, -1, -1, -1],
                    [-1, 2, 2, 2, -1],
                    [-1, 2, 8, 2, -1],
                    [-1, 2, 2, 2, -1],
                    [-1, -1, -1, -1, -1]]) / 8
    
    h11 = np.array([[-1, -1, 0],
                    [-1, 0, 1],
                    [0, 1, 1]])
    
    h12 = np.sqrt(h3**2 + h4**2)

    final_img = applyFilter(io.imread('T-01/in-images/house.png'), h12)

    plt.imsave('T-01/out-images/10/10.12.house.png', final_img, cmap="gray")
    

if __name__ == '__main__':
    main()
