from garden import garden
from flask import request, g, jsonify
from ..model.repository import Repository
from main import db, auth as garden_auth
from ..model.commit import Commit

@garden.route('/repo/add')
@garden_auth.login_required
def add_garden():
    print('adding repo')
    repo_name = request.json.get('name')
    url = request.json.get('url')
    secret = request.json.get('secret')
    owner_id = g.user.id
    if Repository.get_repo_by_name(repo_name) is not None:
        return jsonify({'error': 'repository %s existed'%(repo_name)})
    repository = Repository(name=repo_name, secret=secret, url=url, owner_id=owner_id)
    db.session.add(repository)
    db.session.commit()
    return jsonify({'status': 'success'})

@garden.route('/repo')
@garden_auth.login_required
def get_repo():
    user = g.user
    print('getting repo for user: %d'%user.id)
    a = user.repo.all()
    return jsonify({'repo':[i.serialize for i in a]})

@garden.route('/repo/get')
@garden_auth.login_required
def get_repo_by_name():
    repo_name = request.json.get('repo_name', None)
    repo = Repository.get_repo_by_name(repo_name=repo_name)
    return jsonify({'repo': repo.serialize})


@garden.route('/commit/add')
@garden_auth.login_required
def add_commit():
    print('adding commit')
    repo_name = request.json.get('repo_name', None)
    if repo_name is None or Repository.get_repo_by_name(repo_name) is None:
        return jsonify({'error: repositroy %s not exist'%repo_name})
    repo_id = Repository.get_repo_by_name(repo_name).id
    commiter_id = g.user.id
    content = request.json.get('content', None)
    commit = Commit(repo_id=repo_id, content=content, commiter_id=commiter_id)
    db.session.add(commit)
    db.session.commit()
    return jsonify({'status': 'success'})

@garden.route('/commit')
@garden_auth.login_required
def get_commit():
    user = g.user
    print('getting commit for user: %d'%user.id)
    a = user.commit.all()
    return jsonify({'commit':[i.serialize for i in a]})





