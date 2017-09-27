import numpy as np
from scipy.io import loadmat
import cv2

# Function to plot the basis
def plotBasis(eigbasis):
    # Plotting just 100 elements from the eigenbasis
    for i in range(100):
        # Get the image - the transpose is necessary because the 
        # order of flattening was different while getting the 
        # eigenvectors
        image = eigbasis[i].reshape([92, 92]).T
        # Normalize image
        image = image / np.max(image) * 255
        # Write image to disk
        cv2.imwrite('eigfaces/eigface-%s.jpg' % str(i), image)

if __name__ == '__main__':
    # Load the eigenbasis
    eigbasis = loadmat('data/EigenVectors.mat')['COEFF']
    # Plot the eigenbasis
    plotBasis(eigbasis)

