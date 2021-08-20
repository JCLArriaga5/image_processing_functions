# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as mpimg
from rgb2gray import *
import sys
import os

def img2uint8(img):
    '''
    Convert image to 8-bit format [0, 255].
    '''

    vmin = img.min()
    vmax = img.max()

    img = ((img - vmin) / (vmax - vmin)) * 255.0

    return np.uint8(img)

def plothist(h, color='k'):
    '''
    Show histogram of an image.
    Parameters
    ----------
    h : Array with a size (255, 1) that contains the intensity values of the
        pixels of the grayscale image.
    color : Color to display the histogram e.g. 'r'
    '''

    fig, ax = plt.subplots(1, 1)

    ax.stem(h, linefmt = '{}-'.format(color), markerfmt = 'none', basefmt = 'k-', use_line_collection=True)
    ax.set_xlim(0, 255)
    ax.grid('on')
    ax.set_xticklabels([])

    cmap = plt.get_cmap('gray', 255)
    norm = mpl.colors.Normalize(vmin=0, vmax=255)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    fig.colorbar(sm, orientation='horizontal')
    plt.show()

def hist(img):
    '''
    Get array of pixel intensity values in a grayscale image.
    img : Image in grayscale.
    '''

    if len(img.shape) > 2:
        raise ValueError('Image not in grayscale')

    h = np.zeros((256, 1))

    for m in range(img.shape[0]):
        for n in range(img.shape[1]):
            h[img[m, n]] += 1

    return h

def cumhist(img):
    '''
    Get cumulative histogram of grayscale image.
    '''

    h = hist(img)

    for i in range(1, len(h)):
        h[i] += h[i - 1]

    return h

def imread(str):
    img = mpimg.imread(str)

    if img.dtype != np.uint8:
        img = img2uint8(img)

    return img

if __name__ == '__main__':

    img = imread('./images/Lenna.png')

    histvals = hist(grayaverage(img))
    plothist(histvals, color='k')
