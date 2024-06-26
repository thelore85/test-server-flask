from flask import Flask, render_template

# file api import
# from api.admin import setup_admin
from api.routes import api
# from api.model import db

# App - server
def create_app():
    app = Flask(__name__)

    #setting
    app.register_blueprint(api, url_prefix='/api')
    # setup_admin(app)

    # Interface
    @app.route('/')
    def index():
        return render_template('index.html')

    return app

app = create_app()