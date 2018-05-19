from main import db
from datetime import datetime

class Repository(db.Model):
    __tablename__ = 'repository'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True,  index=True)
    create_time = db.Column(db.DATETIME(64), default=datetime.now())
    secret = db.Column(db.String(64))
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    owner = db.relationship('User', backref='user')


