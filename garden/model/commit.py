from main import db
from time import time
from datetime import datetime

class Commit(db.Model):
    __tablename__ = 'commit'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    update_time = db.Column(db.DATETIME(64), index=True, default=datetime.now())
    commiter_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    content = db.Column(db.String(128), nullable=False)
    repo_id = db.Column(db.INTEGER, db.ForeignKey("repository.id"), nullable=False)

    @property
    def serialize(self):
        return {"update_time": self.update_time, "repo_id": self.repo_id}
