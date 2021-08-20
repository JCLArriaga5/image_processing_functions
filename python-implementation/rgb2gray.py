# -*- coding: utf-8 -*-

import numpy as np

def grayaverage(img):
    """
    Conversion of a RGB image to a gray image by the Average method

    Parameters
    ----------------
    img : The function receives a grayscale image of N * M dimensions

    Returns
    ----------------
    The function returns a grayscale image by the average method
    """

    R = np.double(img[:, :, 0])
    G = np.double(img[:, :, 1])
    B = np.double(img[:, :, 2])

    return np.uint8((R + G + B) / img.shape[2])

def grayluminosity(img):
    """
    Conversion of a RGB image to a gray image by the Luminosity method

    Parameters
    ----------------
    img : The function receives a grayscale image of N * M dimensions

    Returns
    ----------------
    The function returns a grayscale image by the Luminosity method
    """

    R = 0.2125 * (np.double(img[:,:,0]))
    G = 0.7154 * (np.double(img[:,:,1]))
    B = 0.0721 * (np.double(img[:,:,2]))

    return np.uint8(R + G + B)

def grayligthness(img):
    """
    Conversion of a RGB image to a gray image by the Ligthness method

    Parameters
    ----------------
    img : The function receives a grayscale image of N * M dimensions

    Returns
    ----------------
    OUT : The function returns a grayscale image by the Ligthness method
    """

    R = np.double(img[:,:,0])
    G = np.double(img[:,:,1])
    B = np.double(img[:,:,2])

    __max = np.asarray(np.maximum(np.maximum(R, G), B))
    __min = np.asarray(np.minimum(np.minimum(R, G), B))

    return np.uint8((__max + __min) / 2)
