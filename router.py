from flask import Blueprint, jsonify, request
from controller import create_user, get_users, get_user, update_user, delete_user

user_bp = Blueprint("user_bp", __name__)

# CRUD operations

 # Create User
user_bp.route('/users', methods=['POST'])(create_user)

# Read All Users
user_bp.route('/users', methods=['GET'])(get_users)

# Read a specific User
user_bp.route('/users/<int:user_id>', methods=['GET'])(get_user)

# Update User
user_bp.route('/users/<int:user_id>', methods=['PUT'])(update_user)

# Delete User
user_bp.route('/users/<int:user_id>', methods=['DELETE'])(delete_user)