from utils import *


# - Dithering technics - 
# where each row has the cofficients of the error and 
# the column (x_offset) and row (y_offset) that the error 
# is propagated to. Thus, each row should look like:
# [x_offset, y_offset, coefficient]

floyd_steinberg = [[1, 0, 7/16],
                  [-1, 1, 3/16],
                  [0, 1, 5/16],
                  [1, 1, 1/16]]

stevenson_arce = [[2, 0, 32/200],
                  [-3, 1, 12/200],
                  [-1, 1, 26/200],
                  [1, 1, 30/200],
                  [3, 1, 16/200],
                  [-2, 2, 12/200],
                  [0, 2, 26/200],
                  [2, 2, 12/200],
                  [-3, 3, 5/200],
                  [-1, 3, 12/200],
                  [1, 3, 12/200],
                  [3, 3, 5/200]]

burkes = [[1, 0, 8/32],
          [2, 0, 4/32],
          [-2, 1, 2/32],
          [-1, 1, 4/32],
          [0, 1, 8/32],
          [1, 1, 4/32],
          [2, 1, 2/32]]

sierra = [[1, 0, 5/32],
          [2, 0, 3/32],
          [-2, 1, 2/32],
          [-1, 1, 4/32],
          [0, 1, 5/32], 
          [1, 1, 4/32],
          [2, 1, 2/32],
          [-1, 2, 2/32],
          [0, 2, 3/32],
          [1, 2, 2/32]]

stucki = [[1, 0, 8/42],
          [2, 0, 4/42],
          [-2, 1, 2/42],
          [-1, 1, 4/42],
          [0, 1, 8/42],
          [1, 1, 4/42],
          [2, 1, 2/42],
          [-2, 2, 1/42],
          [-1, 2, 2/42],
          [0, 2, 4/42],
          [1, 2, 2/42],
          [2, 2, 1/42]]

jarvis_judice_ninke = [[1, 0, 7/48],
                       [2, 0, 5/48],
                       [-2, 1, 3/48],
                       [-1, 1, 5/48],
                       [0, 1, 7/48],
                       [1, 1, 5/48],
                       [2, 1, 3/48],
                       [-2, 2, 1/48],
                       [-1, 2, 3/48],
                       [0, 2, 5/48],
                       [1, 2, 3/48],
                       [2, 2, 1/48]]


def squareComparison(img: np.ndarray, side: int) -> np.ndarray:
    if len(img.shape) == 3:
        height, width = img.shape[:-1]
    else:
        height, width = img.shape
    cy, cx = height // 2, width // 2
    mask = img[cy - side :  cy + side, cx - side : cx + side]
    return mask


def dither(img: np.ndarray, technic: list[list], m: int, n: int, traverse: int) -> np.ndarray:
    if len(img.shape) == 2:
            img = img[:, :, np.newaxis]

    height, width, channels = img.shape
    for y in range(0, height - n):
        for x in range(m, width - m):
            # Ensures that the traverse is alternated
            if y % 2 == 1 and traverse == 1:
                x = width - x - m
            for c in range(channels):
                old_pixel = img[x, y, c]
                new_pixel = np.round(old_pixel / 255) * 255
                img[x, y, c] = np.uint8(new_pixel)
                err = old_pixel - new_pixel

                for x_offset, y_offset, coefficient in technic:
                    img[x + x_offset, y + y_offset, c] += np.int8(err * coefficient)

    return img