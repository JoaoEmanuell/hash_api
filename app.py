# Imports
from flask import Flask, render_template

app = Flask(__name__)

# Routes
from routers import api

app.register_blueprint(api, url_prefix='/api/')

@app.route('/')
def index():
    return render_template('index.html')