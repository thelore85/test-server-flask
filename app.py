from flask import Flask
from api.routes import api


app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')



# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def main():
#     return 'server is running on main routh'
