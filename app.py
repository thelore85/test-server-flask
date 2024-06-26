from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# file api import
from api.admin import setup_admin
from api.routes import api
# from api.model import db

# App - server
def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://default:kVtLIcRm3o4s@ep-twilight-bird-a2o7tszp.eu-central-1.aws.neon.tech:5432/verceldb?sslmode=require"
    
    # Initialize SQLAlchemy and defining a simple Book model
    db = SQLAlchemy(app)

    #setting
    app.register_blueprint(api, url_prefix='/api')
    setup_admin(app)


    # Interface
    @app.route('/')
    def index():
        return render_template('index.html')
   
    # with app.app_context():
    #     db.create_all()

    return app

app = create_app()