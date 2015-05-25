from datetime import datetime

def calibrate(position1, position2, wavelength1 = 546.5, wavelength2 = 611.6):
    m = (wavelength2 - wavelength1)/(position2 - position1)
    b = wavelength1 - m*position1
    with open('static/calibration.txt', 'w') as f:
        f.write('{:g}\n{:g}\n'.format(m, b))
        f.write(str(datetime.now()))
    return m, b
