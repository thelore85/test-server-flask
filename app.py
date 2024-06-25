from flask import Flask

app = Flask(__name__)

@app.routes("/")
def home():
    return 'server is running on main routh'
