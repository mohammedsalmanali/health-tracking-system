# routes.py
from flask import Blueprint, jsonify, request
from app import db
from models import User, HealthActivity

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@user_bp.route('/record_activity', methods=['POST'])
def record_activity():
    data = request.json
    user_id = data['user_id']
    name = data['name']
    date = data['date']
    new_activity = HealthActivity(user_id=user_id, name=name, date=date)
    db.session.add(new_activity)
    db.session.commit()
    return jsonify({'message': 'Activity recorded successfully'})
