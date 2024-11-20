from flask import jsonify, request
from models import db, User

# Create User
def create_user():
    data = request.json
    new_user = User(username=data['username'], password=data['password'], active=data.get('active', True))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created", "user": data}), 201

# Read All Users
def get_users():
    users = User.query.all()
    users_list = [{"id": user.id, "username": user.username, "active": user.active} for user in users]
    return jsonify(users_list)

# Read a specific User
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({"id": user.id, "username": user.username, "active": user.active})

# Update User
def update_user(user_id):
    data = request.json
    user = User.query.get_or_404(user_id)
    user.username = data.get('username', user.username)
    user.password = data.get('password', user.password)
    user.active = data.get('active', user.active)
    db.session.commit()
    return jsonify({"message": "User updated", "user": data})

# Delete User
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})
