# Imports
from flask import Flask, render_template

app = Flask(__name__)

# Routes
from routers import api, docs

app.register_blueprint(api, url_prefix='/api/')
app.register_blueprint(docs, url_prefix='/docs/')

@app.route('/')
def index():
    return render_template('index.html')