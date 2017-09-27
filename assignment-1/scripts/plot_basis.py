import numpy as np
from scipy.io import loadmat
import cv2

def plotBasis(eigbasis):
    for i in range(100):
        image = eigbasis[i].reshape([92, 92]).T
        image = image / np.max(image) * 255
        cv2.imwrite('eigfaces/eigface-%s.jpg' % str(i), image)

if __name__ == '__main__':
    eigbasis = loadmat('data/EigenVectors.mat')['COEFF']
    plotBasis(eigbasis)

