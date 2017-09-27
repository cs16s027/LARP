import numpy as np
from scipy.io import loadmat
import cv2

# Returns the Frobenius norm of A
def norm(A):
    row, col = A.shape
    val = np.float32(0.0)
    for x in range(row):
        for y in range(col):
            val += np.float32(A[x][y]) * np.float32(A[x][y])
    return np.sqrt(val)

def relativeError(image, recon):
    return norm(recon - image)

def projectImage(eigbasis, image, image_name):
    image_norm = norm(image)
    image_vector = image.T.flatten().reshape([1, -1])
    projections = np.dot(image_vector, eigbasis).flatten()
    indices = np.argsort(np.abs(projections))[::-1]
    recon_vector = np.zeros((8464, ))
    for i in np.arange(0, recon_vector.shape[0], 1):
        index = indices[i]
        recon_vector += projections[index] * eigbasis[:, index]
        recon_image = recon_vector.reshape((92, 92)).T
        error = relativeError(image, recon_image) / image_norm
        if error < 0.01:
            print 'Relative error drops below 0.01 at %s eigenfaces for %s' % (str(i + 1), image_name)
            return recon_image, str(i + 1)
    
    print 'Alarm : Could not get a reconstruction. Is your eigenbasis correct?'
    return False, '0'

if __name__ == '__main__':
    eigbasis = loadmat('data/EigenVectors.mat')['COEFF']
    topk = open('reconstructions/top-k.txt', 'w')
    for i in np.arange(1, 11, 1):
        image_name = 'face%d.pgm' % i
        image_path = 'data/images/%s' % image_name
        print 'Projection and reconstruction for %s' % image_name
        image = cv2.imread(image_path, 0)
        recon, eig = projectImage(eigbasis, image, image_name)
        if recon is not False:
            cv2.imwrite('reconstructions/%s' % image_name, recon)
            topk.write('%s,%s\n' % (image_name, eig))
    topk.close()

