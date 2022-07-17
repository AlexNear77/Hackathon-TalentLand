from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from werkzeug.wrappers import request
from flask import flash, request
# from .. import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("index.html")
    

@views.route('/login', methods=['GET'])
def login():
    return render_template("login.html")


@views.route('/register', methods=['GET'])
def register():
    return render_template("register.html")


@views.route('/createA', methods=['GET'])
def createA():
    return render_template("createA.html")


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


