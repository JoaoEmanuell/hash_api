from flask import Blueprint, render_template

docs = Blueprint('docs', __name__, template_folder='templates')

@docs.route('/')
def index():
    return render_template('documentation/index.html')