import json
from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from werkzeug.wrappers import request
from flask import flash, request
# from .. import db
from .utils import form_recognizer

d = form_recognizer.datos

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("index.html")
    

@views.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@views.route('/register', methods=['GET'])
def register():
    return render_template("register.html")


@views.route('/createA', methods=['GET'])
def createA():
    return render_template("createA.html")


@views.route('/createP', methods=['GET'])
def createP():
    return render_template("createP.html")


@views.route('/createPF', methods=['GET'])
def createPF():
    return render_template("createPF.html")


@views.route('/revision', methods=['GET'])
def revision():
    return render_template("revision.html")


@views.route('/gView', methods=['GET'])
def gView():
    return render_template("gView.html")


@views.route('/felicidades', methods=['GET'])
def felicidades():
    return render_template("felicidades.html")


@views.route('/sHorario', methods=['GET'])
def sHorario():
    return render_template("sHorario.html")


@views.route('/sHora', methods=['GET'])
def sHora():
    return render_template("sHora.html")


@views.route('/sAsesoria', methods=['GET'])
def sAsesoria():
    return render_template("sAsesoria.html")

@views.route('/createP2', methods=['GET'])
def createP2():
    return render_template("createP2.html")

@views.route('/index', methods=['GET'])
def index():
    return render_template("index.html")

@views.route('/test', methods=['GET'])
def test():
    return render_template("test.html", dic=d, nombre="FirstName", apellido="LastName", edad=str(2022-d["DateOfBirth"].year))