import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def invSquare(x):
    A = 6 / (np.pi ** 2)
    return A / (x ** 2)

def sampleinvSquare():
    r = np.random.uniform(0, 1)
    s = 0
    i = 1
    while (s <= 1):
        s += invSquare(i)
        if s >= r:
            sign = np.random.uniform(0, 1)
            if sign > 0.5:
                return i
            else:
                return -i
        i = i + 1

def runExperiment(N, num_exp):
    sample_means = np.zeros((num_exp))
    sample_sigmas = np.zeros((num_exp))
    for exp in np.arange(0, num_exp, 1):
        samples = np.zeros((N, ))
        for i in np.arange(0, N, 1):
            samples[i] = sampleinvSquare()
        sample_means[exp] = np.mean(samples)
        sample_sigmas[exp] = np.std(samples)
    return sample_means, sample_sigmas

def plotMeans(sample_means, plot):
    fig = plt.figure() 
    ax = fig.gca()
    ax.hist(sample_means, bins = np.arange(-10, 11, 1))
    ax.set_xlim([-10, 10])
    ax.set_ylim([0, 4000])
    plt.plot()
    plt.savefig(plot)

def writeParams(sample_params, f):
    sample_means, sample_sigmas = sample_params
    N = sample_means.shape[0]
    f = open(f, 'w')
    for i in range(N):
        f.write('%s,%s\n' % (sample_means[i], sample_sigmas[i]))
    f.close()

def readParams(f):
    params = [line.strip().split(',') for line in open(f, 'r').readlines()]
    means, sigmas = [], []
    for param in params:
        means.append(float(param[0]))
        sigmas.append(float(param[1]))
    return np.array(means), np.array(sigmas)

def countInterval(sample_means, low, high):
    count = 0
    for mean in sample_means:
        if mean > low and mean < high:
            count += 1
    return count

def buildConfidenceIntervals(means, sigmas, z):
    N = means.shape[0]
    mult = z / np.sqrt(N)
    conf = []
    for i in range(N):
        bound = sigmas[i] * mult
        conf.append((means[i] - bound, means[i] + bound))
    return conf

# |x - mu| / (sigma / root(n)) = z
# => n = (z * sigma / (x - mu)) ** 2
def sampleEstimate(sigma):
    errors = [0.1, 0.01, 0.001]
    ns = []
    for error in errors:
        z = -norm.ppf(error / 2)
        n = (z * sigma / error) ** 2
        ns.append(n)
    return ns

if __name__ == '__main__':
    _, N = sys.argv
    N = int(N)
    num_exp = 10000
    mu = 0
    np.random.seed(0)
    if not os.path.isfile('results/problem_4/%s.txt' % N):
        sample_params = runExperiment(N, num_exp)
        writeParams(sample_params, 'results/problem_4/%s.txt' % N)
    sample_params = readParams('results/problem_4/%s.txt' % N)
    sample_means, sample_sigmas = sample_params
    plotMeans(sample_means, 'plots/problem_4/%s.jpg' % N)
    count_1 = countInterval(sample_means, -0.01, 0.01)
    count_2 = countInterval(sample_means, -0.1, 0.1)
    print '[-0.01, 0.01] : %s' % count_1
    print '[-0.1, 0.1]   : %s' % count_2
    conf = buildConfidenceIntervals(sample_means, sample_sigmas, 1.96)
    count = 0.0
    for c in conf:
        if c[0] < mu and c[1] > mu:
            count += 1
    print count / num_exp * 100
    '''
    for sigma in sample_sigmas:
        ns = sampleEstimate(sigma)
        print sigma, ns[0], ns[1], ns[2]
    '''
