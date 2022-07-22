from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from decouple import config
import os

import urllib

# params = urllib.parse.quote_plus("DRIVER={SQL Server Native Client 10.0};SERVER=dagger;DATABASE=test;UID=user;PWD=password")
# engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

# Connect String: mssql+pyodbc://{dbuser}:{dbpass}@{dbhost}/{dbname}
database_uri = 'mssql+pyodbc://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser = os.getenv('DBUSER'),
    dbpass = os.getenv('DBPASS'),
    dbhost = os.getenv('DBHOST'),
    dbname = os.getenv('DBNAME')
)

# app = Flask(__name__)
# engine = create_engine(database_uri)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # # def create_app():
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
API_KEY = ('API_KEY')

app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
# migrate = Migrate(app, db)

