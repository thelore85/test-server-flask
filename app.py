from flask import Flask, render_template
from api.routes import api

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)