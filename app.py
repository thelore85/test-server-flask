from flask import Flask

app = Flask(__name__)

@app.routes("/")
def main():
    return 'server is running on main routh'
