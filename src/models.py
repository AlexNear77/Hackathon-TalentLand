from .db import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model):
    pass