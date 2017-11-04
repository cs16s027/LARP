import os
import itertools
import sys
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing.dummy import Pool as ThreadPool 


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

def runExperiment(N):
    for i in np.arange(0, N, 1):
        samples[i] = samplePoisson()
    sample_means[exp] = np.mean(samples)
    return sample_means

def runExperiments(N, num_exp):
    pool = ThreadPool(4)
    sample_means = pool.map(runExperiment, itertools.repeat(N))
    pool.close()
    pool.join()
    return sample_means

def plotMeans(sample_means, plot):
    fig = plt.figure() 
    ax = fig.gca()
    ax.hist(sample_means, 1000)
    plt.plot()
    plt.savefig(plot)

def writeMeans(sample_means, f):
    f = open(f, 'w')
    for mean in sample_means:
        f.write('%s\n' % mean)
    f.close()

def readMeans(f):
    return [float(line.strip()) for line in open(f, 'r').readlines()]

def countInterval(sample_means, low, high):
    count = 0
    for mean in sample_means:
        if mean > low and mean < high:
            count += 1
    return count

if __name__ == '__main__':
    _, N = sys.argv
    N = int(N)
    num_exp = 10000
    np.random.seed(0)
    if not os.path.isfile('results/problem_3/%s.txt' % N):
        sample_means = runExperiments(N, num_exp)
        #writeMeans(sample_means, 'results/problem_3/%s.txt' % N)
    sample_means = readMeans('results/problem_3/%s.txt' % N)
    plotMeans(sample_means, 'plots/problem_3/%s.jpg' % N)
    count_1 = countInterval(sample_means, 9.99, 10.01)
    count_2 = countInterval(sample_means, 9.9, 10.1)
    print '[9.99, 10.01] : %s' % count_1
    print '[9.9, 10.1]   : %s' % count_2

