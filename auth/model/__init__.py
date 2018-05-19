from auth.controller import db
print('create auth model...')
from auth.model.user import User
db.create_all()