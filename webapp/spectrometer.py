from flask import Flask, url_for, render_template, request
import os
from datetime import datetime
import time
from string import punctuation, whitespace

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def spectrum():
    if request.method == 'POST':
        description = request.form['description']
        description = description.translate({ord(c): None for c in punctuation + whitespace})
        filename = "spectrum_{:s}_{:s}.jpg".format(description, datetime.now().isoformat())
        os.system("wmctrl -a ' fps)'")
        os.system("wmctrl -r ' fps)' -b toggle,fullscreen")
        time.sleep(0.1)
        os.system("gnome-screenshot -w -B -f static/" + filename)
        os.system("wmctrl -r ' fps)' -b toggle,fullscreen")
        os.system("wmctrl -a localhost")
        return render_template('spectrometer.html', filepath=url_for('static', filename=filename))
    else:
        return render_template('spectrometer.html', filepath=None)

if __name__ == '__main__':
    app.debug = True
    app.run()
