# from flask import Flask
# from api.routes import api


# def create_app():
#     print('running server app')
#     app = Flask(__name__)
#     app.register_blueprint(api, url_prefix='/api')

#     return app

# if __name__ == "__main__":
#     app = create_app()





from flask import Flask

app = Flask(__name__)

print('running server app')

@app.routes("/")
def main():
    print('response')
    return 'server is running on main routh'
