from flask import Blueprint
garden = Blueprint('gardent', __name__,)
from garden import controller, model

