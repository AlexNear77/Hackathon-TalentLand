from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config


database_uri = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser = config('DBUSER'),
    dbpass = config('DBPASS'),
    dbhost = config('DBHOST'),
    dbname = config('DBNAME')
)

# def create_app():
app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')

app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# initialize the database connection
db = SQLAlchemy(app)

# initialize database migration management
migrate = Migrate(app, db)