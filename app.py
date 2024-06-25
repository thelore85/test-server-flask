from flask import Flask
from api.routes import api

app = Flask(__name__)

@app.route('/')
def home():
    return 'this is the back running'


# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(api, url_prefix='/api')

#     return app

# On server launch
# if __name__ == "__main__":
#     app = create_app()