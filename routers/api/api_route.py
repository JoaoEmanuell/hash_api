# Global imports
from flask import Blueprint, jsonify

# Local Imports
from .source import Hash

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return 'api'

@api.route('/generate/<string:value>')
def generate(value : str) -> dict :
    hash = {'hash' : Hash().generate_hash(value)}
    return jsonify(hash)