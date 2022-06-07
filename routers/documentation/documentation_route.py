from flask import Blueprint, render_template, request
from jinja2.exceptions import TemplateNotFound

docs = Blueprint('docs', __name__, template_folder='templates')

@docs.route('/')
def index():
    language = request.args.get('language')
    try :
        return render_template(f'documentation/{language}/index.html')
    except TemplateNotFound:
        print(f'Language not found : {language}')
        return render_template('documentation/pt/index.html')
