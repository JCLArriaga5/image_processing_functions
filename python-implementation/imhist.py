# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.image as mpimg
from rgb2gray import rgb2gray_avge
import sys
import os

def imhist(img, *args, **kwargs):
  """
  Calculate the histogram of a grayscale image

  Parameters
  ----------------
  img : The function receives a grayscale image of N * M dimensions

  Returns
  ----------------
  H : The function returns the array with the image histogram values on a scale
  from 0 to 255 and plots the histogram
  """

  if len(img.shape) > 2:
    raise ValueError('The image is not in grayscale')
  else:
    tmp = np.uint8(img)
    H = np.zeros((255, 1))

    for i in range(img.shape[0]):
      for j in range(img.shape[1]):
        K = tmp[i, j]
        H[K] += 1

    fig, ax = plt.subplots(1, 1)
    ax.set_title(*args, **kwargs)
    ax.stem(H, linefmt = 'k-', markerfmt = 'none', basefmt = 'k-', use_line_collection=True)
    ax.set_xlim(0, 255)
    ax.grid('on')
    ax.set_xticklabels([])

    cmap = plt.get_cmap('gray', 255)
    norm = mpl.colors.Normalize(vmin=0, vmax=255)
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])

    fig.colorbar(sm, orientation='horizontal')
    fig.show()

def main():
    abspath = os.getcwd()
    sys.path.append(abspath)
    img_path = '/examples/Lenna.png'
    img = mpimg.imread(abspath + img_path)

    imhist(rgb2gray_avge(img), label='Histogram')

if __name__ == '__main__':
    main()
