# Global imports
from flask import Blueprint, jsonify, request

# Local Imports
from .source import Hash

api = Blueprint('api', __name__)

@api.route('/generate/')
def generate() -> dict :
    return jsonify({'hash' : Hash().generate_hash(request.args.get('value'))})

@api.route('/compare/')
def compare() -> dict :
    return jsonify({'status' : Hash().compare_hash(request.args.get('value'), request.args.get('hash'))})