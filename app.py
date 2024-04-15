from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/komentarze')
def page1():
    return render_template('komentarze.html')

@app.route('/albumy')
def page2():
    return render_template('albumy.html')

@app.route('/zdjecia')
def page2():
    return render_template('zdjecia.html')

@app.route('/posty')
def page2():
    return render_template('posty.html')