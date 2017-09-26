import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Plot intensity historgram
def plotIntensity(image, plot):
    # Plot the histogram
    fig = plt.figure(1)
    ax = fig.gca()
    ax.hist(image.flatten(), 256, [0, 256])
    # Label the plot 
    ax.set_title('Intensity histogram')
    ax.set_xlabel('Pixel values')
    ax.set_ylabel('Frequency')
    ax.set_xlim([0, 256])
    # Save the plot
    plt.savefig(plot)

if __name__ == '__main__':
    # Enter image as an argument
    _, image = sys.argv
    # Get the path of the plot
    plot = image.split('.pgm')[0].split('/')[-1]
    # Read the image 
    image = cv2.imread(image, 0)
    # Plot the intensity histogram
    plotIntensity(image, 'plots/%s.jpg' % plot)
