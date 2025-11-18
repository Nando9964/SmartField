from datetime import datetime

class User:
    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password
        self.created_at = datetime.utcnow()
    
    def __repr__(self):
        return f"<User {self.username}>"
