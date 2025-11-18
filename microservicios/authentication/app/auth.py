from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app.services import AuthService

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    hashed_password = generate_password_hash(password, method='sha256')
    user = User(username=username, password=hashed_password)
    
    try:
        AuthService.create_user(user)
        return jsonify({"message": "User created successfully!"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = AuthService.get_user_by_username(username)
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = AuthService.generate_token(user)
    return jsonify({"token": token}), 200

if __name__ == "__main__":
    app.run(debug=True)
