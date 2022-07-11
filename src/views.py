from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from werkzeug.wrappers import request
from flask import flash, request
# from .. import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("base.html")
    