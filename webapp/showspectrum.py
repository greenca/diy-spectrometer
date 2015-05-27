#! /usr/bin/python

import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys

def getSpectrum(filename):
    img = cv2.imread(filename)
    if img is None:
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    spectrum = np.mean(gray, 0)
    return spectrum

def calibrateSpectrum(spectrum):
    x = range(len(spectrum))
    with open('static/calibration.txt') as f:
        params = f.read().split('\n')
        m = float(params[0])
        b = float(params[1])
        x = [m*i + b for i in x]
    return x

def exportSpectrum(filename, description):
    spectrum = getSpectrum(filename)
    x = calibrateSpectrum(spectrum)
    plotfile = '{:s}_plot.png'.format(filename.split('.')[0])
    plt.plot(x, spectrum)
    plt.title(description)
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Intensity")
    plt.savefig(plotfile)
    plt.close()
    return plotfile
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        spectrum = getSpectrum(sys.argv[1])
        plt.plot(spectrum)
        plt.show()
