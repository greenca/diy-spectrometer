from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def hello():
    os.system("wmctrl -a ' fps)'")
    os.system("wmctrl -r ' fps)' -b toggle,fullscreen")
    os.system("gnome-screenshot -w -B -f static/test.jpg")
    os.system("wmctrl -r ' fps)' -b toggle,fullscreen")
    os.system("wmctrl -a localhost")
    return '<img src="' + url_for('static', filename='test.jpg') + '">'

if __name__ == '__main__':
    app.debug = True
    app.run()
