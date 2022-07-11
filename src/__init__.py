from flask import Flask
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from os import path
from flask_login import LoginManager, login_manager

# Routes
from .views import views

# Database
from .db import db, app


# Blueprints
# app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(views, url_prefix='/')

## Aqui pongo los modelos (tablas)
# from .models import user
# from ..models.models import User, Note
