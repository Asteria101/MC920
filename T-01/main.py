from imports import *
from pencil_sketch import *
from brightness_adjustment import *
from mosaic import *
from filters import *
from bit_planes import *


def combine_images(image1: np.ndarray, image2: np.ndarray, weight1: float, weight2: float) -> None:
    # Ensure the images are normalized to the range [0, 1]
    image1_normalized = image1 / 255.0
    image2_normalized = image2 / 255.0

    # Combine the images using weighted average
    combined_image = (weight1 * image1_normalized + weight2 * image2_normalized)


    plt.imsave('T-01/out-images/1.7_combined_image.png', combined_image, cmap="gray")


def intensity_transformation(image: np.ndarray) -> None:
    negative_image = -image
    plt.imsave('T-01/out-images/1.8.1_negative_image.png', negative_image, cmap="gray")

    contrast_image = np.clip(image, 100, 200)
    plt.imsave('T-01/out-images/1.8.2_contrast_image.png', contrast_image, cmap="gray")

    inverted_even_lines_image = image.copy()
    inverted_even_lines_image[::2] = image[::2, ::-1]
    plt.imsave('T-01/out-images/1.8.3_inverted_even_lines_image.png', inverted_even_lines_image, cmap="gray")

    reflected_lines_image = image.copy()
    height, width = image.shape[:2]
    top_half = image[:height // 2]
    reflected_lines_image[height // 2:] = top_half[::-1]
    plt.imsave('T-01/out-images/1.8.4_reflected_lines_image.png', reflected_lines_image, cmap="gray")

    vertical_mirror_image = image.copy()
    vertical_mirror_image = image[::-1]
    plt.imsave('T-01/out-images/1.8.5_vertical_mirror_image.png', vertical_mirror_image, cmap="gray")


def quantization(image: np.ndarray, bit_level: int) -> None:
    quantizaded_image = (image // (256 // (2 ** bit_level))) * (256 // (2 ** bit_level))
    plt.imsave('T-01/out-images/1.9_baboon_monocromatica_quantization.png', quantizaded_image, cmap="gray")


def filter_aplication(image: np.ndarray) -> None:
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

    def apply_filter(image: np.ndarray, filter: np.array) -> np.ndarray:
        filtered_image = np.zeros_like(image, dtype=np.float32)
        pad_size = filter.shape[0] // 2
        padded_image = np.pad(image, pad_size, mode='constant', constant_values=0)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                filtered_image[i, j] = np.sum(filter * padded_image[i:i + filter.shape[0], j:j + filter.shape[1]])

        np.clip(filtered_image, 0, 255).astype(np.uint8)

        return filtered_image
    
    plt.imsave('T-01/out-images/1.10.1_house.png', apply_filter(image, h1), cmap="gray")
    plt.imsave('T-01/out-images/1.10.2_house.png', apply_filter(image, h2), cmap="gray")
    plt.imsave('T-01/out-images/1.10.3_house.png', apply_filter(image, h3), cmap="gray")
    plt.imsave('T-01/out-images/1.10.4_house.png', apply_filter(image, h4), cmap="gray")
    plt.imsave('T-01/out-images/1.10.5_house.png', apply_filter(image, h5), cmap="gray")
    plt.imsave('T-01/out-images/1.10.6_house.png', apply_filter(image, h6), cmap="gray")
    plt.imsave('T-01/out-images/1.10.7_house.png', apply_filter(image, h7), cmap="gray")
    plt.imsave('T-01/out-images/1.10.8_house.png', apply_filter(image, h8), cmap="gray")
    plt.imsave('T-01/out-images/1.10.9_house.png', apply_filter(image, h9), cmap="gray")
    plt.imsave('T-01/out-images/1.10.10_house.png', apply_filter(image, h10), cmap="gray")
    plt.imsave('T-01/out-images/1.10.11_house.png', apply_filter(image, h11), cmap="gray")

def main() -> None:
    ### 
    # Note: create a script to run all images from in-images folder
    # ###
    #image = io.imread('T-01/in-images/' + 'baboon_monocromatica.png')

    # 1.1 - Pencil Sketch
    pencil_sketch_img = turn2PencilSketch(io.imread('T-01/in-images/watch.png'))

    # 1.2 - Brightness Adjustment
    brightness_adjusted_img = applyBrightnessAdjustment(io.imread('T-01/in-images/baboon_monocromatica.png'), 1.5)

    # 1.3 - Mosaic
    mosaic_img = createMosaic(io.imread('T-01/in-images/baboon_monocromatica.png'), 4)

    # 1.4 - Color change
    old_photo_img = applyOldPhotoFilter(io.imread('T-01/in-images/watch.png'))

    # 1.5 - Change colored images
    img_a, img_b = transformColorImage(io.imread('T-01/in-images/watch.png'))

    # 1.6 - Extract bit planes
    bit_planes: list[np.ndarray] = extractBitPlanes(io.imread('T-01/in-images/baboon_monocromatica.png'))

    for i in range(len(bit_planes)):
        plt.imshow(bit_planes[i], cmap='gray')
        plt.axis('off')
        plt.show()

    # 1.7 - Combine images
    #combine_images(io.imread('T-01/in-images/baboon_monocromatica.png'), io.imread('T-01/in-images/butterfly.png'), 0.8, 0.2)

    # 1.8 - Intensity transformation
    #intensity_transformation(io.imread('T-01/in-images/city.png'))

    # 1.9 - Quantization
    #quantization(io.imread('T-01/in-images/baboon_monocromatica.png'), 8)

    # 1.10 - Filter application
    #filter_aplication(io.imread('T-01/in-images/house.png'))



if __name__ == '__main__':
    main()
