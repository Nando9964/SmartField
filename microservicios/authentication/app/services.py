import jwt
from datetime import datetime, timedelta
from .models import User

SECRET_KEY = 'your_secret_key'

class AuthService:
    @staticmethod
    def create_user(user):
        # Simulate saving the user to a database
        print(f"User {user.username} created successfully.")

    @staticmethod
    def get_user_by_username(username):
        # Simulate fetching the user from a database
        if username == "testuser":
            return User(username=username, password="hashed_password_here")
        return None

    @staticmethod
    def generate_token(user):
        payload = {
            'sub': user.username,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(hours=1)
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
