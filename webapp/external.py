import os
import time
import sys

def takePicture(filename):
    os.system("wmctrl -a ' fps)'")
    os.system("wmctrl -r ' fps)' -b toggle,fullscreen")
    time.sleep(0.2)
    os.system("import -window root -crop 350x250+1280+480 static/spectra/" + filename)
    os.system("wmctrl -r ' fps)' -b toggle,fullscreen")
    os.system("wmctrl -a localhost")

def showSpectrum(filename):
    os.system("./showspectrum.py static/spectra/" + filename + " &")

