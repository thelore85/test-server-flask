from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'this is the back running'



