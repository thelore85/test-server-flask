from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# file api import
from api.admin import setup_admin
from api.routes import api

# App - server
app = Flask(__name__)

#setting
app.register_blueprint(api, url_prefix='/api')
setup_admin(app)

# Interface
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)