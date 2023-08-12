# backend/routes.py
from flask import jsonify, request   # pylint: disable=import-error
from app import app, db
from models import User, HealthActivity

# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

# Health Activity Recording
@app.route('/record_activity', methods=['POST'])
def record_activity():
    data = request.json
    user_id = data['user_id']
    name = data['name']
    date = data['date']
    new_activity = HealthActivity(user_id=user_id, name=name, date=date)
    db.session.add(new_activity)
    db.session.commit()
    return jsonify({'message': 'Activity recorded successfully'})

if __name__ == '__main__':
    app.run(debug=True)
