from flask import Flask, url_for, render_template
import os
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def hello():
    filename = "spectrum_{:s}.jpg".format(datetime.now().isoformat())
    os.system("wmctrl -a ' fps)'")
    os.system("wmctrl -r ' fps)' -b toggle,fullscreen")
    time.sleep(0.1)
    os.system("gnome-screenshot -w -B -f static/" + filename)
    os.system("wmctrl -r ' fps)' -b toggle,fullscreen")
    os.system("wmctrl -a localhost")
    return render_template('spectrometer.html', filepath=url_for('static', filename=filename))

if __name__ == '__main__':
    app.debug = True
    app.run()
