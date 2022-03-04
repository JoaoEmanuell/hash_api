# Global imports
from flask import Blueprint, jsonify, request
from json import loads
from json.decoder import JSONDecodeError

# Local Imports
from .source import Hash

api = Blueprint('api', __name__)

@api.route('/generate/', methods=['GET', 'POST'])
def generate() -> dict :
    if request.method == 'GET':
        return jsonify({'hash' : Hash().generate_hash(request.args.get('value'))})
    elif request.method == 'POST':
        try : 
            data = loads(request.data)
            return jsonify({'hash' : Hash().generate_hash(data['value'])})
        except KeyError:
            return jsonify({'hash' : 'Invalid Key'})
        except (JSONDecodeError, TypeError) :
            return jsonify({'hash' : 'Invalid JSON'})
    else :
        return 'Method not allowed'

@api.route('/compare/', methods=['GET', 'POST'])
def compare() -> dict :
    if request.method == 'GET':
        return jsonify({'status' : Hash().compare_hash(request.args.get('value'), request.args.get('hash'))})
    elif request.method == 'POST':
        try : 
            data = loads(request.data)
            return jsonify({'status' : Hash().compare_hash(data['value'], data['hash'])})
        except KeyError :
            return jsonify({'status' : 'Invalid Key'})
        except (JSONDecodeError, TypeError) :
            return jsonify({'status' : 'Invalid JSON'})
    else :
        return 'Method not allowed'
