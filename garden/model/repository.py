from main import db
from datetime import datetime
from flask import jsonify

class Repository(db.Model):
    __tablename__ = 'repository'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True,  index=True, nullable=False)
    create_time = db.Column(db.DATETIME(64), default=datetime.now())
    secret = db.Column(db.String(64), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    url = db.Column(db.String(128), nullable=False)

    @property
    def serialize(self):
        return {"repo_name": self.name, "owner_id": self.owner_id,
                "create_time": self.create_time, "url": self.url}

    @staticmethod
    def get_repo_by_name(repo_name):
        return Repository.query.filter_by(name=repo_name).first()


