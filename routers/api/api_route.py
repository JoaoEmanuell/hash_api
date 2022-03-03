# Global imports
from flask import Blueprint, jsonify, request

# Local Imports
from .source import Hash

api = Blueprint('api', __name__)

@api.route('/generate/', methods=['GET', 'POST'])
def generate() -> dict :
    if request.method == 'GET':
        return jsonify({'hash' : Hash().generate_hash(request.args.get('value'))})
    elif request.method == 'POST':
        try : 
            return jsonify({'hash' : Hash().generate_hash(request.form['value'])})
        except KeyError:
            return jsonify({'hash' : 'Invalid Key'})
    else :
        return 'Method not allowed'

@api.route('/compare/')
def compare() -> dict :
    return jsonify({'status' : Hash().compare_hash(request.args.get('value'), request.args.get('hash'))})