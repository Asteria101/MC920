from utils import *

class Ditherer:
    def __init__(self, src_img: np.ndarray) -> None:
        self.img = src_img
        
        if len(self.img.shape) == 2:
            self.img = self.img[:, :, np.newaxis]
            
        self.height, self.width, self.channels = self.img.shape


    def roundBW(pixel_val) -> tuple:
        if pixel_val > 127:
            return 255, pixel_val - 255
        return 0, pixel_val
                

    def floydSteinberg(self) -> None:
        err_arr = np.zeros((self.height, self.width, self.channels))

        for y in range(self.height):
            for x in range(self.width):
                # change traverse order
                if y % 2 == 1:
                    x = self.width - 1 - x
                    
                for c in range(self.channels):
                    pixel = self.img[x, y, c] + err_arr[x, y, c]

                    pixel, err = Ditherer.roundBW(pixel)

                    self.img[x, y, c] = pixel

                    err = float(err)

                    # Apply error diffusion
                    if x < self.width - 1:
                        err_arr[x + 1, y, c] += (err * (7 / 16))
                    if y < self.height - 1:
                        if x > 0:
                            err_arr[x - 1, y + 1, c] += (err * (3 / 16))
                        if x < self.width - 1:
                            err_arr[x + 1, y + 1, c] += (err * (1 / 16))
                        err_arr[x, y + 1, c] += (err * (5 / 16))


    def stevensonArce(self) -> None:
        err_arr = np.zeros((self.height, self.width, self.channels))

        for y in range(self.height):
            for x in range(self.width):
                # change traverse order
                if y % 2 == 1:
                    x = self.width - 1 - x
                    
                for c in range(self.channels):
                    pixel = self.img[x, y, c] + err_arr[x, y, c]

                    pixel, err = Ditherer.roundBW(pixel)

                    self.img[x, y, c] = pixel
                    err = float(err)

                    # Apply error diffusion
                    if x < self.width - 2:
                        err_arr[x + 2, y, c] += (err * (32 / 200))

                    if y < self.height - 1:
                        if x - 3 >= 0:
                            err_arr[x - 3, y + 1, c] += (err * (12 / 200))

                        if x - 1 >= 0:
                            err_arr[x - 1, y + 1, c] += (err * (26 / 200))

                        if x + 1 < self.width:
                            err_arr[x + 1, y + 1, c] += (err * (30 / 200))

                        if x + 3 < self.width:
                            err_arr[x + 3, y + 1, c] += (err * (16 / 200))

                    if y < self.height - 2:
                        err_arr[x, y + 2, c] += (err * (26 / 200))
                        
                        if x - 2 >= 0:
                            err_arr[x - 2, y + 2, c] += (err * (12 / 200))

                        if x + 2 < self.width:
                            err_arr[x + 2, y + 2, c] += (err * (12 / 200))

                    if y < self.height - 3:
                        if x - 3 >= 0:
                            err_arr[x - 3, y + 3, c] += (err * (5 / 200))

                        if x - 1 >= 0:
                            err_arr[x - 1, y + 3, c] += (err * (12 / 200))

                        if x + 1 < self.width:
                            err_arr[x + 1, y + 3, c] += (err * (12 / 200))

                        if x + 3 < self.width:
                            err_arr[x + 3, y + 3, c] += (err * (5 / 200))

    
    def show(self) -> None:
        plt.imshow(self.img, cmap='gray')
        plt.axis('off')
        plt.show()


    def save(self, filepath: str) -> None:
        if self.channels == 1:
            self.img = self.img[:, :, 0]

        plt.imsave(filepath, self.img, cmap='gray')