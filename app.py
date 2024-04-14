from flask import Flask, redirect, render_template, url_for, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required, error
from sqlalchemy.sql.expression import func


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///glodny.db'
db=SQLAlchemy(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/posty")
def end():
    return render_template("posty.html")

@app.route("/komentarze")
def end():
    return render_template("komentarze.html")

@app.route("/albumy")
def end():
    return render_template("albumy.html")

@app.route("/zdjecia")
def end():
    return render_template("zdjecia.html")
