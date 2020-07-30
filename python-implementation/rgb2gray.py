import numpy as np

# Implementation of algorithms to convert an RGB image to grayscale (Average, Luminosity).

def rgb2grayAverage(Image):
    """
    Conversion of a RGB image to a gray image by the Average method

    Parameters
    ----------------
    Image : The function receives a grayscale image of N * M dimensions

    Returns
    ----------------
    IOUT : The function returns a grayscale image by the average method
    """

    Im = Image
    [r, c, ch] = Im.shape
    IOUT = np.zeros((r, c), dtype = np.uint8)

    ImR = np.double(Im[:,:,0])
    ImG = np.double(Im[:,:,1])
    ImB = np.double(Im[:,:,2])

    IOUT = np.uint8((ImR + ImG + ImB) / ch)

    return IOUT

def rgb2grayLuminosity(image):
    """
    Conversion of a RGB image to a gray image by the Luminosity method

    Parameters
    ----------------
    Image : The function receives a grayscale image of N * M dimensions

    Returns
    ----------------
    IOUT : The function returns a grayscale image by the Luminosity method
    """

    Im = image
    [r, c, ch] = Im.shape

    IOUT = np.zeros((r, c), dtype = np.uint8)

    ImR = np.double(Im[:,:,0])
    ImG = np.double(Im[:,:,1])
    ImB = np.double(Im[:,:,2])

    R = 0.21 * ImR
    G = 0.72 * ImG
    B = 0.07 * ImB

    IOUT = np.uint8(R + G + B)

    return IOUT

def rgb2grayLigthness(Image):
    """
    Conversion of a RGB image to a gray image by the Ligthness method

    Parameters
    ----------------
    Image : The function receives a grayscale image of N * M dimensions

    Returns
    ----------------
    IOUT : The function returns a grayscale image by the Ligthness method
    """

    Im = Image
    [r, c, ch] = Im.shape
    IOUT = np.zeros((r, c), dtype = np.uint8)

    R = np.double(Im[:,:,0])
    G = np.double(Im[:,:,1])
    B = np.double(Im[:,:,2])

    Mmax = np.asarray(np.maximum(np.maximum(R, G), B))
    Mmin = np.asarray(np.minimum(np.minimum(R, G), B))

    IOUT = np.uint8((Mmax + Mmin) / 2)

    return IOUT
