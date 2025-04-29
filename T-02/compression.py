from utils import *
from frequency_domain import *

def compress(img: np.ndarray, k: int) -> np.ndarray:
    # apply svd (singular value decomposition)
    # u : left singular vectors
    # d : singular values
    # v : right singular vectors
    u, d, v = np.linalg.svd(img, full_matrices=True)

    uk = u[:, 0:k]
    dk = d[0:k]
    vk = v[0:k, :]

    # reconstruct the image using only the first k singular values returning a compressed image
    compressed_img = np.dot(np.dot(uk, np.diag(dk)), vk)

    return compressed_img
