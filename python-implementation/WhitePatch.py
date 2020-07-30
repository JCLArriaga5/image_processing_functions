import numpy as np

def WhitePatch(image):
    """
    Application of the white patch algorithm to an RGB image

    Parameters
    ----------------
    Image : The function receives a 3-channel image

    Returns
    ----------------
    IOUT : The function returns an image that assumes a perfect reflectance (white patch)
    """

    Im = image
    [r, c, ch] = Im.shape
    IOUT = np.zeros((r, c, ch), dtype = np.double)

    IR = np.double(Im[:,:,0])
    IG = np.double(Im[:,:,1])
    IB = np.double(Im[:,:,2])

    KR = 255 / (np.amax(IR))
    KG = 255 / (np.amax(IG))
    KB = 255 / (np.amax(IB))


    IOUT[:,:,0] = KR * IR
    IOUT[:,:,1] = KG * IG
    IOUT[:,:,2] = KG * IB


    IOUT = np.uint8(IOUT)

    return IOUT
