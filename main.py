from flask import Flask, g
from flask_httpauth import HTTPTokenAuth
from flask_sqlalchemy import SQLAlchemy
import os

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# extensions

auth = HTTPTokenAuth(scheme='Token')

users = {
    "nami":"pass"
}

tokens = {
    "nami": "token"
}
db = SQLAlchemy(app)



@app.route('/')
def index():
    return 'hi, %s'%(auth.username())


if __name__ == '__main__':
    from auth import auth as nami_auth
    app.register_blueprint(nami_auth, url_prefix='/auth')
    from garden import garden
    app.register_blueprint(garden, url_prefix='/garden')

    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)