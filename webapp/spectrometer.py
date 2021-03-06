from flask import Flask, url_for, render_template, request, redirect
from datetime import datetime
from string import punctuation, whitespace
import external
import showspectrum
import calibrate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def spectrum():
    if request.method == 'GET':
        return render_template('spectrometer.html', filepath=None, plotfile=None)
    else:
        description = request.form['description']
        filetag = description.translate({ord(c): None for c in punctuation + whitespace})
        filename = "spectrum_{:s}_{:s}.png".format(filetag, datetime.now().isoformat().split('.')[0])
        external.takePicture(filename)
        plotfile = showspectrum.exportSpectrum("static/spectra/" + filename, description)
        return render_template('spectrometer.html', 
                               filepath=url_for('static', filename="spectra/" + filename), 
                               plotfile=plotfile)

@app.route('/calibrate', methods=['GET', 'POST'])
def calibration():
    if request.method == 'GET':
        filename = "calibration_{:s}.png".format(datetime.now().isoformat())
        external.takePicture(filename)
        external.showSpectrum(filename)
        return render_template('calibration.html', filepath=None)
    else:
        calibration_type = request.form['calibration_type']
        position1 = float(request.form['position1'])
        position2 = float(request.form['position2'])
        if calibration_type == 'led':
            wavelength1 = float(request.form['wavelength1'])
            wavelength2 = float(request.form['wavelength2'])
            calibrate.calibrate(position1, position2, wavelength1, wavelength2)
        else:
            calibrate.calibrate(position1, position2)
        return redirect('/')

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'GET':
        filelist = external.getSpectrumFiles()
        return render_template('comparison.html', files=filelist)
    else:
        selectedfiles = request.form.getlist('file')
        plotFile = showspectrum.compareSpectra(selectedfiles)
        return "<img src='{:s}'>".format(plotFile)

if __name__ == '__main__':
    app.debug = True
    app.run()
