from matplotlib import pyplot as plt
import numpy as np
from scipy.io import loadmat
import cv2

# Returns the Frobenius norm of A
def norm(A):
    return np.linalg.norm(A)

def Personalnorm():
    row, col = A.shape
    val = np.float32(0.0)
    for x in range(row):
        for y in range(col):
            val += np.float32(A[x][y]) * np.float32(A[x][y])
    return np.sqrt(val)

# Retrurns the relative error between image and reconstruction
def relativeError(image, recon):
    return norm(recon - image)

# Projects the image on to the eigenbasis and gets a reconstruction
def projectImage(eigbasis, image, image_name):
    # Image norm
    image_norm = norm(image)
    # Flatten the image to get a vector. Transpose is necessary for
    # compatability with eigenbasis column ordering.
    image_vector = image.T.flatten()   # Changed rows to cols
    # Get the projections on to the eigenbasis (eigenbasis is orthogonal)
    projections = np.dot(image_vector, eigbasis).flatten()
    # Sort projections according to the magnitude of the contributions
    indices = np.argsort(np.abs(projections))[::-1]
    # Reconstruction vector
    recon_vector = np.zeros((8464, ))
    # Loop through all eiegenvectors in the basis
    for i in np.arange(0, recon_vector.shape[0], 1):
        # Index of the ith most contributing eigenvector
        index = indices[i]
        # Add this vector to the reconstruction
        recon_vector += projections[index] * eigbasis[:, index] # Changed cols to rows
        # This is the top-k eigenvector reconstruction
        recon_image = recon_vector.reshape((92, 92)).T
        cv2.imwrite('dump/%s.jpg' % str(i + 1), recon_image)
        # Relative error between error image and original image
        error = relativeError(image, recon_image) / image_norm
        if error < 0.01:
            print 'Relative error drops below 0.01 at %s eigenfaces for %s' % (str(i + 1), image_name)
            return recon_image, str(i + 1)
    print 'Alarm : Could not get a reconstruction. Is your eigenbasis correct?'
    return False, '0'

if __name__ == '__main__':
    # Load the eigenbasis
    eigbasis = loadmat('data/EigenVectors.mat')['COEFF']
    # File to store the top-k values for each image
    topk = open('reconstructions/top-k.txt', 'w')
    # Loop through all 10 images
    for i in np.arange(1, 12, 1):
        image_name = 'face%d.pgm' % i
        image_path = 'data/images/%s' % image_name
        print 'Projection and reconstruction for %s' % image_name
        # Load the image
        image = cv2.imread(image_path, 0)
        # Get the reconstruction and top-k values
        recon, eig = projectImage(eigbasis, image, image_name)
        # Write results to disk
        if recon is not False:
            cv2.imwrite('reconstructions/%s' % image_name, recon)
            topk.write('%s,%s\n' % (image_name, eig))
    topk.close()

