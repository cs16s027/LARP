import numpy as np

def getProjectionMatrix(A):
    aTa = np.dot(A.T, A)
    print aTa
    try:
        aTaInv = np.linalg.inv(aTa)
    except np.linalg.linalg.LinAlgError:
        print 'Matrix is singular'
        return 'better luck next time'
    a_aTaInv_aT = np.dot(A, np.dot(aTaInv, A.T))
    P = a_aTaInv_aT
    return P

# PC
A = np.array([[3], [4]])
print A.shape
Pc = getProjectionMatrix(A)
print Pc
# PR
A = np.array([[1, 2, 2]])
print A.shape
Pr = getProjectionMatrix(A.T)
print Pr

# Pc A Pr
A = np.array([[3, 6, 6], [4, 8, 8]])
PcAPr = np.dot(np.dot(Pc, A), Pr)
print PcAPr

