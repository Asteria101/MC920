from utils import *

class Ditherer:
    def __init__(self, src_img: np.ndarray) -> None:
        self.img = src_img
        
        if len(self.img.shape) == 2:
            self.img = self.img[:, :, np.newaxis]
            
        self.height, self.width, self.channels = self.img.shape
                

    def dither(self, technic: list[list], xmax: int, ymax: int) -> np.ndarray:

        for y in range(0, self.height - ymax):
            for x in range(xmax, self.width - xmax):
                if y % 2 == 1:
                    x = self.width - x - 1
                for c in range(self.channels):
                    old_pixel = self.img[x, y, c]
                    new_pixel = np.round(old_pixel / 255) * 255
                    self.img[x, y, c] = np.uint8(new_pixel)
                    err = old_pixel - new_pixel

                    for j, i, coefficient in technic:
                        self.img[x + j, y + i, c] += np.int8(err * coefficient)
                        
    
    def show(self) -> None:
        plt.imshow(self.img, cmap='gray')
        plt.axis('off')
        plt.show()


    def save(self, filepath: str) -> None:
        if self.channels == 1:
            self.img = self.img[:, :, 0]

        plt.imsave(filepath, self.img, cmap='gray')