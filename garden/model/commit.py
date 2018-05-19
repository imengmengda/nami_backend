from main import db
from time import time

class Commit(db.Model):
    __tablename__ = 'commit'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    update_time = db.Column(db.DATETIME(64), index=True, default=time())
    salt = db.Column(db.String(32))
    token = db.Column(db.String(64))
