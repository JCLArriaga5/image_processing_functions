import numpy as np
import matplotlib.pyplot as plt

# Function to obtain the histogram of an image
def imhist(Image):
    """
    Calculate the histogram of a grayscale image

    Parameters
    ----------------
    Image : The function receives a grayscale image of N * M dimensions

    Returns
    ----------------
    ImageHistogram : The function returns the histogram of the image on a scale of 0 to 255
    """

    I = np.uimt8(Image)
    [r, c] = In.shape
    H = np.zeros((256, 1))

    for i in range (r):
        for j in range (c):
            k = I[i, j]
            H[k] = H[k] + 1

    ImageHistogram = H
    plt.stem(ImageHistogram, linefmt = 'k-', markerfmt = 'none', basefmt = 'r-')
    plt.title("Histogram")
