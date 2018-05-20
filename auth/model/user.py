from main import db, app
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)
from utils.password_encrypter import PasswordEcrypter

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    salt = db.Column(db.String(32))
    token = db.Column(db.String(64))
    repo = db.relationship('Repository', backref='user', lazy='dynamic')
    commit = db.relationship('Commit', backref='user', lazy='dynamic')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def generate_token(self, expire_time=3600*360):
        #defaule token expire time: 1 month
        s = Serializer(app.config['SECRET_KEY'], expires_in= expire_time)
        token = s.dumps({'id': self.id})
        self.token = token
        return token

    def hash_password(self):
        password_encrypter = PasswordEcrypter()
        self.salt = password_encrypter.create_salt(4)
        self.password = password_encrypter.create_md5(self.password, self.salt)

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            print('token %s expired'%token)
            return None    # valid token, but expired
        except BadSignature:
            print('token %s invalida'%token)
            return None    # invalid token
        user = User.query.get(data['id'])
        return user