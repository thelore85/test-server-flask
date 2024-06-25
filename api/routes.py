from flask import Blueprint, jsonify, request

# blueprint setting
api = Blueprint('api', __name__)

@api.route('/')
def home():
    return 'this is the back running'