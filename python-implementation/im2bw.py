def im2bw(Image, umbral):
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

    # The function receives a grayscale image and a threshold value
    I = np.double(Image)
    U = umbral
    [r, c] = I.shape
    IOUT = np.zeros((r, c), dtype = np.double)

    for i in range(r):
        for j in range(c):
            k = I[i, j]
            if (k <= U):
                IOUT[i, j] = 0
            else:
                IOUT[i, j] = 1

    IOUT = np.uint8(IOUT)

    return IOUT
