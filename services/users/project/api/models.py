from sqlalchemy.sql import func

from project import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    create_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
