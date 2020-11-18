# -*- coding: utf-8 -*-

import numpy as np

# Implementation of algorithms to convert an RGB image to grayscale (Average, Luminosity).

def rgb2gray_avge(img):
  """
  Conversion of a RGB image to a gray image by the Average method

  Parameters
  ----------------
  img : The function receives a grayscale image of N * M dimensions

  Returns
  ----------------
  OUT : The function returns a grayscale image by the average method
  """

  [r, c, ch] = img.shape
  OUT = [([0] * c) for i in range(r)]
  # OUT = np.zeros((r, c), dtype = np.uint8)

  R = np.double(img[:, :, 0])
  G = np.double(img[:, :, 1])
  B = np.double(img[:, :, 2])

  OUT = np.uint8((R + G + B) / ch)

  return OUT

def rgb2gray_lmsty(img):
    """
    Conversion of a RGB image to a gray image by the Luminosity method

    Parameters
    ----------------
    img : The function receives a grayscale image of N * M dimensions

    Returns
    ----------------
    OUT : The function returns a grayscale image by the Luminosity method
    """

    [r, c, ch] = img.shape

    OUT = np.zeros((r, c), dtype = np.uint8)

    R = 0.2125 * (np.double(img[:,:,0]))
    G = 0.7154 * (np.double(img[:,:,1]))
    B = 0.0721 * (np.double(img[:,:,2]))

    OUT = np.uint8(R + G + B)

    return OUT

def rgb2gray_lgtns(img):
    """
    Conversion of a RGB image to a gray image by the Ligthness method

    Parameters
    ----------------
    img : The function receives a grayscale image of N * M dimensions

    Returns
    ----------------
    OUT : The function returns a grayscale image by the Ligthness method
    """

    [r, c, ch] = img.shape
    OUT = np.zeros((r, c), dtype = np.uint8)

    R = np.double(img[:,:,0])
    G = np.double(img[:,:,1])
    B = np.double(img[:,:,2])

    max_ = np.asarray(np.maximum(np.maximum(R, G), B))
    min_ = np.asarray(np.minimum(np.minimum(R, G), B))

    OUT = np.uint8((max_ + min_) / 2)

    return OUT
