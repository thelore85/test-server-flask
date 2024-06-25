from flask import Flask
from api.routes import api


def create_app():
    print('... creating server app ... 2')
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')

    return app


if __name__ == "__main__":
    print('... creating server app ... 1')
    app = create_app()