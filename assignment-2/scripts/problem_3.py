import os
import sys
import numpy as np
import matplotlib.pyplot as plt

def poisson(lamb, x):
    return np.exp(-lamb) * (lamb ** x) / np.math.factorial(x)

def samplePoisson(lamb = 10):
    r = np.random.uniform(0, 1)
    s = 0
    i = 0 
    while (s <= 1):
        s += poisson(lamb, i)
        if s >= r:
            return i
        i = i + 1

def runExperiment(N, num_exp):
    sample_means = np.zeros((num_exp))
    sample_sigmas = np.zeros((num_exp))
    for exp in np.arange(0, num_exp, 1):
        samples = np.zeros((N, ))
        for i in np.arange(0, N, 1):
            samples[i] = samplePoisson()
        sample_means[exp] = np.mean(samples)
        sample_sigmas[exp] = np.std(samples)
    return sample_means, sample_sigmas

def plotMeans(sample_means, plot):
    fig = plt.figure() 
    ax = fig.gca()
    ax.hist(sample_means, 1000)
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

if __name__ == '__main__':
    _, N = sys.argv
    lamda = 10
    N = int(N)
    num_exp = 10000
    np.random.seed(0)
    if not os.path.isfile('results/problem_3/%s.txt' % N):
        sample_params = runExperiment(N, num_exp)
        writeParams(sample_params, 'results/problem_3/%s.txt' % N)
    sample_params = readParams('results/problem_3/%s.txt' % N)
    sample_means, sample_sigmas = sample_params
    plotMeans(sample_means, 'plots/problem_3/%s.jpg' % N)
    count_1 = countInterval(sample_means, 9.99, 10.01)
    count_2 = countInterval(sample_means, 9.9, 10.1)
    print '[9.99, 10.01] : %s' % count_1
    print '[9.9, 10.1]   : %s' % count_2
    conf = buildConfidenceIntervals(sample_means, sample_sigmas, 1.96)
    count = 0.0
    for c in conf:
        if c[0] < lamda and c[1] > lamda:
            count += 1
    print count / num_exp * 100
