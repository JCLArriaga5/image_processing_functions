import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as mpimg
from rgb2gray import *

def img2uint8(img):
    '''
    Convert image to 8-bit format [0, 255].
    '''

    vmin = img.min()
    vmax = img.max()

    img = ((img - vmin) / (vmax - vmin)) * 255.0

    return np.uint8(img)

def im2bw(img, threshold):
    """
    Convert an RGB image to a binary image (values ​​from 0 to 1)

    Parameters
    ----------------
    Image : The function receives a gray scale image
    umbral : The function receives the value of an integer type threshold

    Returns
    ----------------
    IOUT : The function returns a binary image
    """

    np.putmask(img, img <= threshold, 0)
    np.putmask(img, img > threshold, 1)

    return np.uint8(img)

if __name__ == '__main__':
    img = mpimg.imread('./images/Lenna.png')

    if img.dtype != np.uint8:
        img = img2uint8(img)

    imgbw = im2bw(grayaverage(img), 120)
    plt.imshow(imgbw, cmap='gray')
    plt.show()
