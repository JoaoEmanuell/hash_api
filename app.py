# Imports
from flask import Flask, redirect

app = Flask(__name__)

# Routes
from routers import api, docs

app.register_blueprint(api, url_prefix='/api/')
app.register_blueprint(docs, url_prefix='/docs/')

@app.route('/')
def index():
    return redirect('/docs/?language=pt-br')

if __name__ == '__main__':
    app.run(debug=False)