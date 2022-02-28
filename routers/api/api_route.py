# Global imports
from flask import Blueprint, jsonify, request

# Local Imports
from .source import Hash

api = Blueprint('api', __name__)

@api.route('/generate/')
def generate() -> dict :
    # try :
    return jsonify({'hash' : Hash().generate_hash(request.args.get('value'))})
    '''except (AttributeError):
        return jsonify({'hash' : f'Error {request.args[0]} not found'})'''

@api.route('/compare/<string:value>/<string:hash>')
def compare(value : str, hash : str) -> dict :
    return jsonify({'status' : Hash().compare_hash(value, hash)})