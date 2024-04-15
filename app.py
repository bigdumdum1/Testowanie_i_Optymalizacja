from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/komentarze')
def komentarze():
    return render_template('komentarze.html')

@app.route('/albumy')
def albumy():
    return render_template('albumy.html')

@app.route('/zdjecia')
def zdjecia():
    return render_template('zdjecia.html')

@app.route('/posty')
def posty():
    return render_template('posty.html')