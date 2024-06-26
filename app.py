from flask import Flask
from api.routes import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')

    return app

if __name__ == "__main__":
    app = create_app()


from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return 'server is running on main routh'



# server with flask not work as expected:

# //////// project structure

# // main folder
# // - api
# // -- route.py
# // - app.py

# # // this code works fine:

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def main():
#     return 'server is running on main routh'



# # ////////////this doesen't (but do locally)

# from flask import Flask
# from api.routes import api


# def create_app():
#     app = Flask(__name__)
#     app.register_blueprint(api, url_prefix='/api')

#     return app

# if __name__ == "__main__":
#     app = create_app()


