from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__)

@api.route('/')
def main():
    return jsonify({ "msg": "API Rest Flask"}), 200

