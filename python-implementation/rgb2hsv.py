import numpy as np
np.seterr(divide = 'ignore', invalid = 'ignore')

def rgb2hsv(Image):
    """
    Convert an RGB image to an HSV image

    Parameters
    ----------------
    Image : The function receives a 3-channel image

    Returns
    ----------------
    HSV : The function returns an HSV image
    """

    I = Image
    [r, c, ch] = I.shape
    HSV = np.zeros((r, c, ch), dtype = np.double)

    Rp = np.double(I[:,:,0])
    Gp = np.double(I[:,:,1])
    Bp = np.double(I[:,:,2])

    H = np.double(HSV[:,:,0])
    S = np.double(HSV[:,:,1])
    V = np.double(HSV[:,:,2])

    R = np.asarray((Rp / 255), dtype = np.double)
    G = np.asarray((Gp / 255), dtype = np.double)
    B = np.asarray((Bp / 255), dtype = np.double)

    Mmax = np.asarray(np.maximum(np.maximum(R, G), B))
    Mmin = np.asarray(np.minimum(np.minimum(R, G), B))

    delta = np.asarray((Mmax - Mmin), dtype = np.double)

    #-----------------For chanel R----------------------------------------------
    Rx, Ry = np.where(Mmax == R) and np.where(G >= B)
    HSV[Rx, Ry, 0] = np.double(( G[Rx, Ry] - B[Rx, Ry] )/delta[Rx, Ry])

    Rxb, Ryb = np.where(Mmax == R) and np.where(G < B)
    HSV[Rxb, Ryb, 0] = np.double(1 + (( G[Rxb, Ryb] - B[Rxb, Ryb] )/delta[Rxb, Ryb]))

    #-------------------For chanel G--------------------------------------------
    Gx, Gy = np.where(Mmax == G)
    HSV[Gx, Gy, 0] = np.double(2 + (( B[Gx, Gy] - R[Gx, Gy] )/delta[Gx, Gy]))
    #-------------------For chanel B--------------------------------------------
    Bx, By = np.where(Mmax == B)
    HSV[Bx, By, 0] = np.double(4 + (( R[Bx, By] - G[Bx, By] )/delta[Bx, By])
    
    Sx, Sy = np.where(Mmax == 0)
    HSV[Sx, Sy, 1] = 0
    Sxa, Sya = np.where(Mmax != 0)
    HSV[Sxa, Sya, 1] = np.double(delta[Sxa, Sya]/Mmax[Sxa, Sya])

    HSV[:,:,2] = np.double(Mmax)

    return HSV
