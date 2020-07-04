import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User  # noqa


@app.route('/users', methods=['GET'])
def users_get():
    users = User.query.all()
    response = [user.as_dict() for user in users]
    return jsonify(response), 200


@app.route('/users', methods=['POST'])
def users_create():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    response = user.as_dict()
    return jsonify(response), 200
