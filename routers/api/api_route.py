# Global imports
from flask import Blueprint, jsonify

# Local Imports
from .source import Hash

api = Blueprint('api', __name__)

@api.route('/generate/<string:value>')
def generate(value : str) -> dict :
    return jsonify({'hash' : Hash().generate_hash(value)})

@api.route('/compare/<string:value>/<string:hash>')
def compare(value : str, hash : str) -> dict :
    return jsonify({'status' : Hash().compare_hash(value, hash)})