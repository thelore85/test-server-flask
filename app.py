from flask import Flask
from api.routes import api


def create_app():
    # Flask configuration
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')

    return app

# On server launch
if __name__ == "__main__":
    app = create_app()