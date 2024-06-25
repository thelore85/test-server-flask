from flask import Flask
from api.routes import api

app = Flask(__name__)

@app.routes("/")
def main():
    print('response')
    return 'server is running on main routh'
