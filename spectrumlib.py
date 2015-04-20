import numpy as np
import cv2
from matplotlib import pyplot as plt

def getSpectrum(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    spectrum = np.mean(gray, 0)
    return spectrum
    

if __name__ == '__main__':
    spectrum = getSpectrum('shear.png')
    plt.plot(spectrum)
    plt.show()
