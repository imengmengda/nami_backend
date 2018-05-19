from garden import garden
from flask import request, g, jsonify
from ..model.repository import Repository
from main import db, auth as garden_auth

@garden.route('/repo/add')
@garden_auth.login_required
def add_garden():
    repo_name = request.json.get('name')
    secret = request.json.get('secret')
    owner_id = g.user.id
    repository = Repository(name=repo_name, secret=secret, owner_id=owner_id)
    db.session.add(repository)
    db.session.commit()
    return jsonify({'status': 'success'})