from flask import Blueprint, jsonify, request
from connectors.mysql_connectors import Session
from models.user import User
from sqlalchemy import select



user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/user', methods=['GET'])
def get_user():
    response_data = dict()
    session = Session()

    try:
        user_query = select(User)
        user = session.execute(user_query).scalars()
        user_data = [dict(users) for users in user]
        response_data['users'] = user_data

    
    except Exception as a:
        print(a)
        return "error"
    
    return jsonify(response_data)

from flask import request, jsonify
import bcrypt

@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    try:
        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Create a new User object with the hashed password
        new_user = User(username=username, email=email, password=hashed_password)

        # Add the new user to the session and commit the transaction
        session = Session()
        session.add(new_user)
        session.commit()

        return jsonify({'message': 'User registered successfully'})
    except Exception as e:
        # Handle any errors that occur during the registration process
        print(e)
        return jsonify({'error': 'An error occurred during registration'})

    
@user_routes.route('/login', methods=['POST'])
def login_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    try:
        session = Session()
        user = session.query(User).filter_by(username=username, password=password).first()

        if user:
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'error': 'Invalid username or password'})
        
    except Exception as a:
        print(a)
        return jsonify({'error': 'An error occurred'})
    
@user_routes.route('/user', methods=['DELETE'])
def delete_user():
    data = request.json
    user_id = data.get('id')

    if not user_id:
        return "No user ID found"

    try:
        session = Session()
        user = session.query(User).filter_by(id=user_id).first()

        if not user:
            return jsonify({'error': 'User not found'})

        session.delete(user)
        session.commit()

        return jsonify({'message': 'Deletion successful'})

    except Exception as a:
        print(a)
        return jsonify({'error': 'An error occurred'})

    