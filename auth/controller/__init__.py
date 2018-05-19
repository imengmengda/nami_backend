from main import app, auth, db
from auth.model.user import User
from auth import auth as nami_auth
from flask import request, jsonify, g
from utils.password_encrypter import PasswordEcrypter

@nami_auth.route('/register', methods=['POST'])
def register():
    print('register')
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user is not None or username is None:
        return jsonify({'error': 'user exist'})
    user = User(username, password)
    token = user.generate_token(2)
    user.hash_password()
    db.session.add(user)
    db.session.commit()
    print('token: %s...'%(token))
    return jsonify({'token': str(token)})

@nami_auth.route('/login', methods=['GET'])
def login():
    print('login')
    print(request.json)
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'error': 'user not exist'})
    else:
        password_encrypter = PasswordEcrypter()
        if user.password != password_encrypter.create_md5(password, user.salt):
            return jsonify({'error': 'password error'})
    user.generate_token(600)
    return jsonify({'token': user.token.decode('ascii'), 'duration': 600})

@nami_auth.route('/auth_test')
@auth.login_required
def get_auth_token():   #TODO
    return jsonify({'status':'auth'})

@auth.verify_token
def verify_token(token):
    print(token)
    print('checking token %s ...' % token)
    user = User.verify_auth_token(token)
    if user is None:
        return False
    else:
        g.user = user
        return True



